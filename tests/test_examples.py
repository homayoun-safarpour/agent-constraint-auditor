import json
from pathlib import Path

from constraintauditor.cli import main

ROOT = Path(__file__).parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
DECAYING_JOURNAL = ROOT / "examples" / "decaying" / "journal.md"
DECAYING_CONSTRAINTS = ROOT / "examples" / "decaying" / "constraints.yaml"
REQUIRED_MISSING_JOURNAL = ROOT / "examples" / "required_missing" / "journal.md"
REQUIRED_MISSING_CONSTRAINTS = ROOT / "examples" / "required_missing" / "constraints.yaml"
REQUIRED_PRESENT_JOURNAL = ROOT / "examples" / "required_present" / "journal.md"
REQUIRED_PRESENT_CONSTRAINTS = ROOT / "examples" / "required_present" / "constraints.yaml"


def test_readme_mentions_exit_codes_0_and_2():
    assert "exit `0`" in README or "exit 0" in README or "`0`" in README
    assert "`2`" in README or "exit 2" in README
    assert "Verdict: DECAY" in README
    assert "`forbid: false`" in README
    assert "missing required pattern" in README
    assert "empty transcript" in README
    assert "invalid regex" in README
    assert "required-decay.md" in README
    assert "required-clean.md" in README
    assert "Verdict: CLEAN" in README


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


def test_required_present_fixture_exit_0():
    assert (
        main(
            [
                "audit",
                "--constraints",
                str(ROOT / "examples" / "required_present" / "constraints.yaml"),
                "--transcript",
                str(ROOT / "examples" / "required_present" / "journal.md"),
            ]
        )
        == 0
    )


def test_required_missing_fixture_exit_2(capsys):
    code = main(
        [
            "audit",
            "--constraints",
            str(REQUIRED_MISSING_CONSTRAINTS),
            "--transcript",
            str(REQUIRED_MISSING_JOURNAL),
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "DECAY"
    assert {v["constraint_id"] for v in data["violations"]} == {"require_lint_pass"}
    assert all(v["detail"].startswith("required pattern missing:") for v in data["violations"])


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


def test_required_pattern_missing_yaml_audit_exit_2(tmp_path, capsys):
    constraints = tmp_path / "constraints.yaml"
    constraints.write_text(
        (
            "name: require-lint-pass\n"
            "constraints:\n"
            "  - id: require_lint_pass\n"
            "    description: Every event records lint=PASS\n"
            '    pattern: "lint=PASS"\n'
            "    forbid: false\n"
        ),
        encoding="utf-8",
    )
    journal = tmp_path / "journal.md"
    journal.write_text(
        (
            "# missing required pattern\n"
            "\n"
            "## 2026-08-11 09:00\n"
            "- gates: tests=PASS\n"
            "- decision: **advance**\n"
            "- reason: skipped lint\n"
        ),
        encoding="utf-8",
    )
    code = main(
        [
            "audit",
            "--constraints",
            str(constraints),
            "--transcript",
            str(journal),
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "DECAY"
    ids = {v["constraint_id"] for v in data["violations"]}
    assert ids == {"require_lint_pass"}
    assert data["violations"][0]["detail"].startswith("required pattern missing:")


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


def test_required_missing_fixture_locks_report(tmp_path, capsys):
    journal = REQUIRED_MISSING_JOURNAL.read_text(encoding="utf-8")
    assert "lint line omitted" in journal
    assert "lint=PASS" not in journal
    report = tmp_path / "required-decay.md"
    code = main(
        [
            "audit",
            "--constraints",
            str(REQUIRED_MISSING_CONSTRAINTS),
            "--transcript",
            str(REQUIRED_MISSING_JOURNAL),
            "--report",
            str(report),
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "DECAY"
    assert data["decay"]["n_events"] == 4
    assert data["decay"]["n_violations"] == 4
    assert data["decay"]["first_violation_index"] == 0
    ids = {v["constraint_id"] for v in data["violations"]}
    assert ids == {"require_lint_pass"}
    assert all(v["detail"].startswith("required pattern missing:") for v in data["violations"])
    text = report.read_text(encoding="utf-8")
    assert "Verdict: DECAY" in text
    assert "The transcript records 4 constraint violations, first at event 0." in text
    assert "`require_lint_pass`" in text
    assert "required pattern missing:" in text


def test_required_present_fixture_locks_report_clean(tmp_path, capsys):
    journal = REQUIRED_PRESENT_JOURNAL.read_text(encoding="utf-8")
    spec = REQUIRED_PRESENT_CONSTRAINTS.read_text(encoding="utf-8")
    assert "lint=PASS" in journal
    assert "forbid: false" in spec
    assert "require_lint_pass" in spec
    report = tmp_path / "required-clean.md"
    code = main(
        [
            "audit",
            "--constraints",
            str(REQUIRED_PRESENT_CONSTRAINTS),
            "--transcript",
            str(REQUIRED_PRESENT_JOURNAL),
            "--report",
            str(report),
            "--json",
        ]
    )
    assert code == 0
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "CLEAN"
    assert data["decay"]["n_violations"] == 0
    assert data["decay"]["first_violation_index"] is None
    assert data["violations"] == []
    text = report.read_text(encoding="utf-8")
    assert text.startswith("# Constraint decay report: required-present-agent")
    assert "Verdict: CLEAN" in text
    assert "The transcript holds all declared constraints across 4 events." in text
    assert "None." in text
