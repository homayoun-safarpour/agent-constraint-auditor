import json
import re
from pathlib import Path

from constraintauditor.cli import main

ROOT = Path(__file__).parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
EXAMPLES_README = (ROOT / "examples" / "README.md").read_text(encoding="utf-8")
ADAPTER = (ROOT / "docs" / "ADAPTER.md").read_text(encoding="utf-8")
INTERVIEW = (ROOT / "docs" / "INTERVIEW.md").read_text(encoding="utf-8")
RELIABILITY = (ROOT / "docs" / "RELIABILITY_CARD.md").read_text(encoding="utf-8")
DECAYING_JOURNAL = ROOT / "examples" / "decaying" / "journal.md"
DECAYING_CONSTRAINTS = ROOT / "examples" / "decaying" / "constraints.yaml"
REQUIRED_MISSING_JOURNAL = ROOT / "examples" / "required_missing" / "journal.md"
REQUIRED_MISSING_CONSTRAINTS = ROOT / "examples" / "required_missing" / "constraints.yaml"
REQUIRED_PRESENT_JOURNAL = ROOT / "examples" / "required_present" / "journal.md"
REQUIRED_PRESENT_CONSTRAINTS = ROOT / "examples" / "required_present" / "constraints.yaml"
EMPTY_JOURNAL = ROOT / "examples" / "empty" / "journal.md"
EMPTY_CONSTRAINTS = ROOT / "examples" / "empty" / "constraints.yaml"
HEADERLESS_JOURNAL = ROOT / "examples" / "headerless" / "journal.md"
HEADERLESS_CONSTRAINTS = ROOT / "examples" / "headerless" / "constraints.yaml"
JSONL_STABLE_EVENTS = ROOT / "examples" / "jsonl_stable" / "events.jsonl"
JSONL_STABLE_CONSTRAINTS = ROOT / "examples" / "jsonl_stable" / "constraints.yaml"
JSONL_DECAYING_EVENTS = ROOT / "examples" / "jsonl_decaying" / "events.jsonl"
JSONL_DECAYING_CONSTRAINTS = ROOT / "examples" / "jsonl_decaying" / "constraints.yaml"
EVENT_HEADER_RE = re.compile(r"^##\s+\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}\s*$", re.MULTILINE)




def test_readme_links_examples_matrix():
    assert "examples/MATRIX.md" in README

def test_readme_mentions_exit_codes_0_and_2():
    assert "exit `0`" in README or "exit 0" in README or "`0`" in README
    assert "`2`" in README or "exit 2" in README
    assert "Verdict: DECAY" in README
    assert "`forbid: false`" in README
    assert "missing required pattern" in README
    assert "empty transcript" in README
    assert "headerless transcript" in README
    assert "invalid regex" in README
    assert "required-decay.md" in README
    assert "required-clean.md" in README
    assert "Verdict: CLEAN" in README
    assert "examples/empty/journal.md" in README
    assert "examples/headerless/journal.md" in README
    assert "examples/jsonl_stable/events.jsonl" in README
    assert "examples/jsonl_decaying/events.jsonl" in README
    assert "jsonl-decay.md" in README
    assert "jsonl-clean.md" in README
    assert "--format jsonl" in README
    assert "timestamp" in README
    assert "plus `text` and/or `fields`" in README
    assert "timestamp-only line is ERROR" in README
    assert "JSONL object missing text and fields" in README
    assert "invalid or empty JSONL" in README
    assert "parse-transcript PATH [--format jsonl|journal|auto]" in README
    assert "OK: 0 events" in README
    assert "`audit` and `parse-transcript` both accept `--format jsonl|journal|auto`" in README
    assert "--version" in README
    assert "CONTRIBUTING.md" in README
    assert "agent-constraint-auditor/discussions" in README
    assert "actions/workflows/ci.yml/badge.svg" in README


def test_examples_readme_locks_required_pair_rows():
    present_line = next(line for line in EXAMPLES_README.splitlines() if "required_present/" in line)
    missing_line = next(line for line in EXAMPLES_README.splitlines() if "required_missing/" in line)
    assert "**0**" in present_line or "exit 0" in present_line
    assert "CLEAN" in present_line
    assert "**2**" in missing_line or "exit 2" in missing_line
    assert "DECAY" in missing_line
    assert "forbid: false" in present_line
    assert "forbid: false" in missing_line
    assert "examples/required_present/constraints.yaml" in EXAMPLES_README
    assert "examples/required_missing/constraints.yaml" in EXAMPLES_README


def test_examples_readme_locks_error_pair_rows():
    empty_line = next(line for line in EXAMPLES_README.splitlines() if "[empty/]" in line)
    headerless_line = next(line for line in EXAMPLES_README.splitlines() if "[headerless/]" in line)
    assert "**1**" in empty_line or "exit 1" in empty_line
    assert "ERROR" in empty_line
    assert "**1**" in headerless_line or "exit 1" in headerless_line
    assert "ERROR" in headerless_line
    assert "examples/empty/constraints.yaml" in EXAMPLES_README
    assert "examples/headerless/constraints.yaml" in EXAMPLES_README


def test_examples_readme_locks_jsonl_stable_row():
    jsonl_line = next(line for line in EXAMPLES_README.splitlines() if "[jsonl_stable/]" in line)
    assert "**0**" in jsonl_line or "exit 0" in jsonl_line
    assert "CLEAN" in jsonl_line
    assert "jsonl" in jsonl_line.lower()
    assert "--report" in jsonl_line
    assert "examples/jsonl_stable/events.jsonl" in EXAMPLES_README
    assert "examples/jsonl_stable/constraints.yaml" in EXAMPLES_README
    assert "jsonl-clean.md" in EXAMPLES_README


def test_examples_readme_locks_jsonl_decaying_row():
    jsonl_line = next(line for line in EXAMPLES_README.splitlines() if "[jsonl_decaying/]" in line)
    assert "**2**" in jsonl_line or "exit 2" in jsonl_line
    assert "DECAY" in jsonl_line
    assert "--format jsonl" in jsonl_line
    assert "examples/jsonl_decaying/events.jsonl" in EXAMPLES_README
    assert "examples/jsonl_decaying/constraints.yaml" in EXAMPLES_README
    assert "jsonl-decay.md" in EXAMPLES_README


def test_jsonl_stable_fixture_locks_report(tmp_path, capsys):
    blob = JSONL_STABLE_EVENTS.read_text(encoding="utf-8")
    spec = JSONL_STABLE_CONSTRAINTS.read_text(encoding="utf-8")
    assert "lint=PASS" in blob
    assert "lint=FAIL" not in blob
    assert "git push --force" not in blob
    assert "never_skip_lint" in spec
    assert "no_force_push" in spec
    report = tmp_path / "jsonl-clean.md"
    code = main(
        [
            "audit",
            "--constraints",
            str(JSONL_STABLE_CONSTRAINTS),
            "--transcript",
            str(JSONL_STABLE_EVENTS),
            "--format",
            "jsonl",
            "--report",
            str(report),
            "--json",
        ]
    )
    assert code == 0
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "CLEAN"
    assert data["decay"]["n_events"] == 4
    assert data["decay"]["n_violations"] == 0
    assert data["decay"]["first_violation_index"] is None
    assert data["violations"] == []
    text = report.read_text(encoding="utf-8")
    assert text.startswith("# Constraint decay report: jsonl-stable-agent")
    assert "Verdict: CLEAN" in text.splitlines()[:5]
    assert "The transcript holds all declared constraints across 4 events." in text
    assert "None." in text


def test_jsonl_stable_fixture_parse_and_audit_exit_0(capsys):
    events = JSONL_STABLE_EVENTS
    constraints = JSONL_STABLE_CONSTRAINTS
    assert events.is_file() and constraints.is_file()
    code = main(["parse-transcript", "--format", "jsonl", str(events)])
    assert code == 0
    assert "OK: 4 events" in capsys.readouterr().out
    assert (
        main(
            [
                "audit",
                "--constraints",
                str(constraints),
                "--transcript",
                str(events),
                "--format",
                "jsonl",
            ]
        )
        == 0
    )


def test_jsonl_decaying_fixture_parse_and_audit_exit_2(capsys):
    events = JSONL_DECAYING_EVENTS
    constraints = JSONL_DECAYING_CONSTRAINTS
    assert events.is_file() and constraints.is_file()
    blob = events.read_text(encoding="utf-8")
    assert "lint=FAIL" in blob
    assert "git push --force to unblock" in blob
    code = main(["parse-transcript", "--format", "jsonl", str(events)])
    assert code == 0
    assert "OK: 4 events" in capsys.readouterr().out
    code = main(
        [
            "audit",
            "--constraints",
            str(constraints),
            "--transcript",
            str(events),
            "--format",
            "jsonl",
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "DECAY"
    assert data["decay"]["first_violation_index"] == 2
    assert {v["constraint_id"] for v in data["violations"]} == {"never_skip_lint", "no_force_push"}


def test_jsonl_decaying_fixture_locks_report(tmp_path, capsys):
    blob = JSONL_DECAYING_EVENTS.read_text(encoding="utf-8")
    assert "git push --force to unblock" in blob
    assert "lint=FAIL" in blob
    report = tmp_path / "jsonl-decay.md"
    code = main(
        [
            "audit",
            "--constraints",
            str(JSONL_DECAYING_CONSTRAINTS),
            "--transcript",
            str(JSONL_DECAYING_EVENTS),
            "--format",
            "jsonl",
            "--report",
            str(report),
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "DECAY"
    assert data["decay"]["n_violations"] == 3
    assert data["decay"]["first_violation_index"] == 2
    assert {v["constraint_id"] for v in data["violations"]} == {"never_skip_lint", "no_force_push"}
    text = report.read_text(encoding="utf-8")
    assert text.startswith("# Constraint decay report: jsonl-decaying-agent")
    assert "Verdict: DECAY" in text
    assert "The transcript records 3 constraint violations, first at event 2." in text
    assert "`never_skip_lint`" in text
    assert "`no_force_push`" in text


def test_adapter_locks_error_fixture_rows():
    error_line = next(line for line in ADAPTER.splitlines() if "ERROR (fail-closed)" in line)
    assert "`examples/empty`" in error_line
    assert "`examples/headerless`" in error_line
    assert "exit 1" in error_line
    assert "examples/empty/constraints.yaml" in ADAPTER
    assert "examples/empty/journal.md" in ADAPTER
    assert "examples/headerless/constraints.yaml" in ADAPTER
    assert "examples/headerless/journal.md" in ADAPTER
    assert "never a free CLEAN" in ADAPTER


def test_adapter_locks_jsonl_fixture_rows():
    stable_line = next(line for line in ADAPTER.splitlines() if "JSONL CLEAN" in line)
    decay_line = next(line for line in ADAPTER.splitlines() if "JSONL DECAY" in line)
    assert "`examples/jsonl_stable`" in stable_line
    assert "exit 0" in stable_line
    assert "`examples/jsonl_decaying`" in decay_line
    assert "exit 2" in decay_line
    assert "examples/jsonl_stable/events.jsonl" in ADAPTER
    assert "examples/jsonl_decaying/events.jsonl" in ADAPTER
    assert "--format jsonl" in ADAPTER
    assert "Verdict: DECAY" in ADAPTER
    assert "jsonl-decay.md" in ADAPTER
    assert "neither `text` nor `fields` is ERROR" in ADAPTER


def test_interview_locks_jsonl_demo():
    assert "examples/jsonl_stable/events.jsonl" in INTERVIEW
    assert "examples/jsonl_decaying/events.jsonl" in INTERVIEW
    assert "--format jsonl" in INTERVIEW
    assert "jsonl-decay.md" in INTERVIEW
    assert "Verdict: DECAY" in INTERVIEW
    assert "Markdown journals and JSONL events share the same exit contract" in INTERVIEW
    assert "--version" in INTERVIEW
    assert "0.1.0" in INTERVIEW


def test_reliability_card_locks_jsonl_claim():
    assert "--format jsonl" in RELIABILITY
    assert "jsonl_stable" in RELIABILITY
    assert "jsonl_decaying" in RELIABILITY
    assert "JSONL transcript" in RELIABILITY or "jsonl" in RELIABILITY.lower()


MATRIX_EXIT_ROWS = (
    ("stable/", 0, "CLEAN"),
    ("decaying/", 2, "DECAY"),
    ("required_present/", 0, "CLEAN"),
    ("required_missing/", 2, "DECAY"),
    ("empty/", 1, "ERROR"),
    ("headerless/", 1, "ERROR"),
    ("jsonl_stable/", 0, "CLEAN"),
    ("jsonl_decaying/", 2, "DECAY"),
)


def test_examples_matrix_locks_exit_rows():
    matrix = (ROOT / "examples" / "MATRIX.md").read_text(encoding="utf-8")
    for fixture, code, verdict in MATRIX_EXIT_ROWS:
        line = next((row for row in matrix.splitlines() if f"`{fixture}`" in row), None)
        assert line is not None, f"MATRIX.md missing row for {fixture}"
        assert f"**{code}**" in line, line
        assert verdict in line
        stem = fixture.rstrip("/")
        assert f"examples/{stem}/" in matrix
    assert "python -m pytest -q" in matrix
    assert "python -m ruff check ." in matrix
    assert "--format jsonl" in matrix
    assert "MATRIX.md" in EXAMPLES_README or "[MATRIX.md]" in EXAMPLES_README


def test_examples_matrix_live_exits_match_table():
    cases = (
        ("stable", "journal.md", None, 0),
        ("decaying", "journal.md", None, 2),
        ("required_present", "journal.md", None, 0),
        ("required_missing", "journal.md", None, 2),
        ("empty", "journal.md", None, 1),
        ("headerless", "journal.md", None, 1),
        ("jsonl_stable", "events.jsonl", "jsonl", 0),
        ("jsonl_decaying", "events.jsonl", "jsonl", 2),
    )
    for name, transcript, fmt, expected in cases:
        args = [
            "audit",
            "--constraints",
            str(ROOT / "examples" / name / "constraints.yaml"),
            "--transcript",
            str(ROOT / "examples" / name / transcript),
        ]
        if fmt:
            args.extend(["--format", fmt])
        assert main(args) == expected, name


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


def test_empty_fixture_exit_1(capsys):
    assert EMPTY_JOURNAL.read_text(encoding="utf-8") == ""
    code = main(
        [
            "audit",
            "--constraints",
            str(EMPTY_CONSTRAINTS),
            "--transcript",
            str(EMPTY_JOURNAL),
        ]
    )
    assert code == 1
    err = capsys.readouterr().err
    assert "no parseable events" in err
    assert "CLEAN" not in err


def test_headerless_fixture_exit_1(capsys):
    journal = HEADERLESS_JOURNAL.read_text(encoding="utf-8")
    assert EVENT_HEADER_RE.search(journal) is None
    assert "lint=PASS" in journal
    code = main(
        [
            "audit",
            "--constraints",
            str(HEADERLESS_CONSTRAINTS),
            "--transcript",
            str(HEADERLESS_JOURNAL),
        ]
    )
    assert code == 1
    err = capsys.readouterr().err
    assert "no parseable events" in err
    assert "CLEAN" not in err


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
