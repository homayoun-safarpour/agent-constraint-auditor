import json
from pathlib import Path

from constraintauditor.cli import main

ROOT = Path(__file__).parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
DECAYING_JOURNAL = ROOT / "examples" / "decaying" / "journal.md"
DECAYING_CONSTRAINTS = ROOT / "examples" / "decaying" / "constraints.yaml"


def test_readme_mentions_exit_codes_0_and_2():
    assert "exit `0`" in README or "exit 0" in README or "`0`" in README
    assert "`2`" in README or "exit 2" in README
    assert "Verdict: DECAY" in README


def test_stable_agent_fixture_exit_0():
    assert (
        main(
            [
                "audit",
                "--constraints",
                str(ROOT / "examples" / "stable" / "constraints.yaml"),
                "--transcript",
                str(ROOT / "examples" / "stable" / "journal.md"),
            ]
        )
        == 0
    )


def test_decaying_agent_fixture_exit_2():
    assert (
        main(
            [
                "audit",
                "--constraints",
                str(ROOT / "examples" / "decaying" / "constraints.yaml"),
                "--transcript",
                str(ROOT / "examples" / "decaying" / "journal.md"),
            ]
        )
        == 2
    )


def test_markdown_report_contains_quartile_timeline(tmp_path):
    report = tmp_path / "report.md"
    code = main(
        [
            "audit",
            "--constraints",
            str(DECAYING_CONSTRAINTS),
            "--transcript",
            str(DECAYING_JOURNAL),
            "--report",
            str(report),
        ]
    )
    assert code == 2
    text = report.read_text(encoding="utf-8")
    assert "Quartile violation rates" in text
    assert "Q1" in text
    assert "Verdict: DECAY" in text


def test_decaying_fixture_locks_force_push_line(tmp_path, capsys):
    journal = DECAYING_JOURNAL.read_text(encoding="utf-8")
    assert "git push --force to unblock" in journal
    assert "lint=FAIL" in journal
    report = tmp_path / "report.md"
    code = main(
        [
            "audit",
            "--constraints",
            str(DECAYING_CONSTRAINTS),
            "--transcript",
            str(DECAYING_JOURNAL),
            "--report",
            str(report),
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["decay"]["first_violation_index"] == 2
    ids = {v["constraint_id"] for v in data["violations"]}
    assert ids == {"never_skip_lint", "no_force_push"}
    text = report.read_text(encoding="utf-8")
    assert "Verdict: DECAY" in text
    assert "The transcript records 3 constraint violations, first at event 2." in text
    assert "`never_skip_lint`" in text
    assert "`no_force_push`" in text
