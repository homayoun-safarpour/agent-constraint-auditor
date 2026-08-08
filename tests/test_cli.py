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
