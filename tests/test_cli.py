import json
from pathlib import Path

from constraintauditor.cli import main

ROOT = Path(__file__).parent.parent


def test_cli_exit_code_0_when_clean():
    code = main(
        [
            "audit",
            "--constraints",
            str(ROOT / "examples" / "stable" / "constraints.yaml"),
            "--transcript",
            str(ROOT / "examples" / "stable" / "journal.md"),
        ]
    )
    assert code == 0


def test_cli_exit_code_2_on_decay():
    code = main(
        [
            "audit",
            "--constraints",
            str(ROOT / "examples" / "decaying" / "constraints.yaml"),
            "--transcript",
            str(ROOT / "examples" / "decaying" / "journal.md"),
        ]
    )
    assert code == 2


def test_cli_exit_code_1_on_bad_args(tmp_path):
    code = main(
        [
            "audit",
            "--constraints",
            str(tmp_path / "missing.yaml"),
            "--transcript",
            str(tmp_path / "missing.md"),
        ]
    )
    assert code == 1


def test_empty_transcript_is_error_exit_1(tmp_path, capsys):
    journal = tmp_path / "empty.md"
    journal.write_text("", encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            str(ROOT / "examples" / "stable" / "constraints.yaml"),
            "--transcript",
            str(journal),
        ]
    )
    assert code == 1
    assert "no parseable events" in capsys.readouterr().err


def test_invalid_regex_audit_exit_1(tmp_path, capsys):
    constraints = tmp_path / "constraints.yaml"
    constraints.write_text(
        (
            "name: bad-regex\n"
            "constraints:\n"
            "  - id: broken\n"
            '    pattern: "("\n'
        ),
        encoding="utf-8",
    )
    journal = tmp_path / "journal.md"
    journal.write_text(
        "## 2026-08-11 09:00\n- gates: lint=PASS\n",
        encoding="utf-8",
    )
    code = main(
        [
            "audit",
            "--constraints",
            str(constraints),
            "--transcript",
            str(journal),
        ]
    )
    assert code == 1
    assert "not a valid regex" in capsys.readouterr().err


def test_check_constraints_ok():
    code = main(["check-constraints", str(ROOT / "examples" / "stable" / "constraints.yaml")])
    assert code == 0


def test_check_constraints_invalid_regex_exit_1(tmp_path, capsys):
    path = tmp_path / "bad.yaml"
    path.write_text(
        (
            "name: bad-regex\n"
            "constraints:\n"
            "  - id: broken\n"
            '    pattern: "("\n'
        ),
        encoding="utf-8",
    )
    code = main(["check-constraints", str(path)])
    assert code == 1
    assert "not a valid regex" in capsys.readouterr().err


def test_headerless_journal_is_error_exit_1(tmp_path, capsys):
    journal = tmp_path / "headerless.md"
    journal.write_text("# notes\n- gates: lint=PASS\n", encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            str(ROOT / "examples" / "stable" / "constraints.yaml"),
            "--transcript",
            str(journal),
        ]
    )
    assert code == 1
    assert "no parseable events" in capsys.readouterr().err


def test_audit_json_output_schema(capsys):
    code = main(
        [
            "audit",
            "--constraints",
            str(ROOT / "examples" / "stable" / "constraints.yaml"),
            "--transcript",
            str(ROOT / "examples" / "stable" / "journal.md"),
            "--json",
        ]
    )
    assert code == 0
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "CLEAN"
    assert "decay" in data
    assert "violations" in data
