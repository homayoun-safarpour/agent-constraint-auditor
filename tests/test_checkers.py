from constraintauditor.checkers import check_transcript
from constraintauditor.journal import JournalEvent
from constraintauditor.spec import Constraint, ConstraintSpec


def test_checker_flags_violation():
    spec = ConstraintSpec(
        name="t",
        constraints=(Constraint(id="never_skip_lint", description="", pattern=r"lint\s*=\s*FAIL"),),
    )
    events = [
        JournalEvent("2026-08-11 09:00", "- gates: lint=FAIL\n- decision: advance", {"gates": "lint=FAIL"}),
    ]
    v = check_transcript(spec, events)
    assert len(v) == 1
    assert v[0].constraint_id == "never_skip_lint"


def test_checker_passes_clean_transcript():
    spec = ConstraintSpec(
        name="t",
        constraints=(Constraint(id="never_skip_lint", description="", pattern=r"lint\s*=\s*FAIL"),),
    )
    events = [
        JournalEvent("2026-08-11 09:00", "- gates: lint=PASS\n- decision: advance", {"gates": "lint=PASS"}),
    ]
    assert check_transcript(spec, events) == []


def test_required_pattern_missing_is_violation():
    spec = ConstraintSpec(
        name="t",
        constraints=(
            Constraint(
                id="require_lint_pass",
                description="Every event records lint=PASS",
                pattern=r"lint\s*=\s*PASS",
                forbid=False,
            ),
        ),
    )
    events = [
        JournalEvent(
            "2026-08-11 09:00",
            "- gates: tests=PASS\n- decision: advance",
            {"gates": "tests=PASS"},
        ),
    ]
    v = check_transcript(spec, events)
    assert len(v) == 1
    assert v[0].constraint_id == "require_lint_pass"
    assert v[0].event_index == 0
    assert v[0].detail == r"required pattern missing: lint\s*=\s*PASS"


def test_required_pattern_present_is_clean():
    spec = ConstraintSpec(
        name="t",
        constraints=(
            Constraint(
                id="require_lint_pass",
                description="",
                pattern=r"lint\s*=\s*PASS",
                forbid=False,
            ),
        ),
    )
    events = [
        JournalEvent(
            "2026-08-11 09:00",
            "- gates: lint=PASS\n- decision: advance",
            {"gates": "lint=PASS"},
        ),
    ]
    assert check_transcript(spec, events) == []
