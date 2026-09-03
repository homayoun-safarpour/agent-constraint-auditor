"""Parse agent-loop-engine style append-only journals into events."""

from __future__ import annotations

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
    return "journal"
