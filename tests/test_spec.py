from pathlib import Path

import pytest

from constraintauditor.spec import SpecError, load_constraint_spec, parse_constraint_spec

ROOT = Path(__file__).parent.parent
STABLE = ROOT / "examples" / "stable" / "constraints.yaml"


def test_constraint_spec_loads_yaml():
    spec = load_constraint_spec(STABLE)
    assert spec.name == "stable-agent"
    assert len(spec.constraints) >= 1


def test_invalid_spec_raises():
    with pytest.raises(SpecError):
        parse_constraint_spec({"name": "x", "constraints": []})


def test_forbid_false_parses_as_required_pattern():
    spec = parse_constraint_spec(
        {
            "name": "require-lint-pass",
            "constraints": [
                {
                    "id": "require_lint_pass",
                    "description": "Every event records lint=PASS",
                    "pattern": r"lint\s*=\s*PASS",
                    "forbid": False,
                }
            ],
        }
    )
    assert spec.constraints[0].forbid is False
    assert spec.constraints[0].id == "require_lint_pass"
