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
