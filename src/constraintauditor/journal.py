"""Parse agent-loop-engine style append-only journals into events."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


class TranscriptError(ValueError):
    """Empty or unparseable transcript."""


HEADER_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s*$")
LINE_RE = re.compile(r"^-\s+(?P<key>[^:]+):\s*(?P<value>.*)$")


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

    Each object requires ``timestamp`` plus non-empty ``text`` and/or ``fields``.
    Matching text is ``text`` when set, otherwise synthesized from ``fields``.
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
        fields = _fields_from_mapping(obj.get("fields"), line_no)
        text = obj.get("text")
        has_text = isinstance(text, str) and bool(text.strip())
        if not has_text and not fields:
            raise TranscriptError(f"JSONL line {line_no} needs text and/or fields")
        body = text if has_text else _text_from_fields(fields)
        events.append(JournalEvent(timestamp=timestamp.strip(), text=body, fields=fields))
    return events


def parse_loop_engine_journal(path: str | Path) -> list[JournalEvent]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    events: list[JournalEvent] = []
    current_ts: str | None = None
    fields: dict[str, str] = {}
    blob: list[str] = []

    def flush() -> None:
        nonlocal current_ts, fields, blob
        if current_ts is None:
            return
        text = "\n".join(blob).strip()
        events.append(JournalEvent(timestamp=current_ts, text=text, fields=dict(fields)))
        current_ts = None
        fields = {}
        blob = []

    for line in lines:
        hm = HEADER_RE.match(line)
        if hm:
            flush()
            current_ts = hm.group(1)
            continue
        if current_ts is None:
            continue
        blob.append(line)
        lm = LINE_RE.match(line.strip())
        if lm:
            fields[lm.group("key").strip()] = lm.group("value").strip()
    flush()
    return events


def detect_format(path: str | Path) -> str:
    sample = Path(path).read_text(encoding="utf-8")[:2000]
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
