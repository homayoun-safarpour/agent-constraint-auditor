"""Parse agent-loop-engine style append-only journals into events."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


class TranscriptError(ValueError):
    """Empty or unparseable transcript."""


HEADER_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s*$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
LINE_RE = re.compile(r"^-\s+(?P<key>[^:]+):\s*(?P<value>.*)$")
LEVEL2_RE = re.compile(r"^##(?!#)")


@dataclass(frozen=True)
class JournalEvent:
    timestamp: str
    text: str
    fields: dict[str, str]


def _fields_from_mapping(raw: object, line_no: int) -> dict[str, str]:
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise TranscriptError(f"JSONL line {line_no} fields must be a mapping")
    return {str(key): "" if value is None else str(value) for key, value in raw.items()}


def _text_from_fields(fields: dict[str, str]) -> str:
    return "\n".join(f"- {key}: {value}" for key, value in fields.items())


def parse_jsonl_transcript(path: str | Path) -> list[JournalEvent]:
    """Parse one JSON object per line into journal events.

    Each object requires ``timestamp`` of shape ``YYYY-MM-DD HH:MM`` plus
    non-empty ``text`` and/or ``fields``. Matching text is ``text`` followed by
    a body synthesized from ``fields``, so a rule sees both.
    """
    events: list[JournalEvent] = []
    for line_no, raw_line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise TranscriptError(f"invalid JSONL at line {line_no}: {exc}") from exc
        if not isinstance(obj, dict):
            raise TranscriptError(f"JSONL line {line_no} must be an object")
        timestamp = obj.get("timestamp")
        if not isinstance(timestamp, str) or not timestamp.strip():
            raise TranscriptError(f"JSONL line {line_no} missing timestamp")
        timestamp = timestamp.strip()
        if TIMESTAMP_RE.fullmatch(timestamp) is None:
            raise TranscriptError(f"JSONL line {line_no} timestamp must be YYYY-MM-DD HH:MM")
        fields = _fields_from_mapping(obj.get("fields"), line_no)
        text = obj.get("text")
        has_text = isinstance(text, str) and bool(text.strip())
        if not has_text and not fields:
            raise TranscriptError(f"JSONL line {line_no} needs text and/or fields")
        parts = [text] if has_text else []
        if fields:
            parts.append(_text_from_fields(fields))
        body = "\n".join(parts)
        events.append(JournalEvent(timestamp=timestamp, text=body, fields=fields))
    return events


def parse_loop_engine_journal(path: str | Path) -> list[JournalEvent]:
    lines = Path(path).read_text(encoding="utf-8-sig").splitlines()
    events: list[JournalEvent] = []
    current_ts: str | None = None
    fields: dict[str, str] = {}
    blob: list[str] = []
    orphan_line: int | None = None

    def flush() -> None:
        nonlocal current_ts, fields, blob
        if current_ts is None:
            return
        text = "\n".join(blob).strip()
        if not text and not fields:
            raise TranscriptError(f"journal event {current_ts} needs text and/or fields")
        events.append(JournalEvent(timestamp=current_ts, text=text, fields=dict(fields)))
        current_ts = None
        fields = {}
        blob = []

    for line_no, line in enumerate(lines, 1):
        hm = HEADER_RE.match(line)
        if hm:
            flush()
            current_ts = hm.group(1)
            continue
        if LEVEL2_RE.match(line.strip()):
            raise TranscriptError(
                f"malformed journal heading at line {line_no}: expected ## YYYY-MM-DD HH:MM"
            )
        if current_ts is None:
            if orphan_line is None and LINE_RE.match(line.strip()):
                orphan_line = line_no
            continue
        blob.append(line)
        lm = LINE_RE.match(line.strip())
        if lm:
            fields[lm.group("key").strip()] = lm.group("value").strip()
    flush()
    if events and orphan_line is not None:
        raise TranscriptError(
            f"journal line {orphan_line} comes before the first dated heading"
        )
    return events


def detect_format(path: str | Path) -> str:
    sample = Path(path).read_text(encoding="utf-8-sig")[:2000]
    if HEADER_RE.search(sample):
        return "journal"
    for line in sample.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("{"):
            return "jsonl"
        break
    return "journal"
