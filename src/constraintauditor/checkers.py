"""Deterministic constraint checkers over journal events."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .journal import JournalEvent
from .spec import Constraint, ConstraintSpec


@dataclass(frozen=True)
class Violation:
    constraint_id: str
    event_index: int
    timestamp: str
    detail: str


def check_event(constraint: Constraint, event: JournalEvent, event_index: int) -> Violation | None:
    matched = re.search(constraint.pattern, event.text, flags=re.IGNORECASE | re.MULTILINE)
    if constraint.forbid and matched:
        return Violation(
            constraint_id=constraint.id,
            event_index=event_index,
            timestamp=event.timestamp,
            detail=f"forbid pattern matched: {constraint.pattern}",
        )
    if (not constraint.forbid) and not matched:
        return Violation(
            constraint_id=constraint.id,
            event_index=event_index,
            timestamp=event.timestamp,
            detail=f"required pattern missing: {constraint.pattern}",
        )
    return None


def check_transcript(spec: ConstraintSpec, events: list[JournalEvent]) -> list[Violation]:
    violations: list[Violation] = []
    for i, event in enumerate(events):
        for constraint in spec.constraints:
            v = check_event(constraint, event, i)
            if v is not None:
                violations.append(v)
    return violations
