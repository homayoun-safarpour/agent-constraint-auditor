"""Load and validate constraint specs (YAML)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class SpecError(ValueError):
    """Invalid or unreadable constraint spec."""


@dataclass(frozen=True)
class Constraint:
    id: str
    description: str
    pattern: str  # regex matched against event text; violation if match when forbid=True
    forbid: bool = True  # if True, a match is a violation; if False, absence of match is violation


@dataclass(frozen=True)
class ConstraintSpec:
    name: str
    constraints: tuple[Constraint, ...]


def load_constraint_spec(path: str | Path) -> ConstraintSpec:
    raw = Path(path).read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise SpecError(f"invalid YAML: {exc}") from exc
    return parse_constraint_spec(data)


def parse_constraint_spec(data: Any) -> ConstraintSpec:
    if not isinstance(data, dict):
        raise SpecError("spec root must be a mapping")
    name = data.get("name")
    items = data.get("constraints")
    if not isinstance(name, str) or not name.strip():
        raise SpecError("spec.name must be a non-empty string")
    if not isinstance(items, list) or not items:
        raise SpecError("spec.constraints must be a non-empty list")
    parsed: list[Constraint] = []
    seen: set[str] = set()
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            raise SpecError(f"constraints[{i}] must be a mapping")
        cid = item.get("id")
        desc = item.get("description", "")
        pattern = item.get("pattern")
        forbid = item.get("forbid", True)
        if not isinstance(cid, str) or not cid.strip():
            raise SpecError(f"constraints[{i}].id required")
        if cid in seen:
            raise SpecError(f"duplicate constraint id: {cid}")
        if not isinstance(pattern, str) or not pattern:
            raise SpecError(f"constraints[{i}].pattern required")
        if not isinstance(forbid, bool):
            raise SpecError(f"constraints[{i}].forbid must be bool")
        seen.add(cid)
        parsed.append(
            Constraint(id=cid, description=str(desc), pattern=pattern, forbid=forbid)
        )
    return ConstraintSpec(name=name.strip(), constraints=tuple(parsed))
