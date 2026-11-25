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


def test_cli_version_prints_package_version(capsys):
    try:
        main(["--version"])
    except SystemExit as exc:
        assert exc.code == 0
    else:
        raise AssertionError("expected SystemExit from --version")
    assert "0.1.0" in capsys.readouterr().out


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


def test_parse_transcript_ok_on_dated_journal(capsys):
    code = main(["parse-transcript", str(ROOT / "examples" / "stable" / "journal.md")])
    assert code == 0
    out = capsys.readouterr().out
    assert "OK: 4 events" in out


def test_parse_transcript_empty_is_error_exit_1(capsys):
    code = main(["parse-transcript", str(ROOT / "examples" / "empty" / "journal.md")])
    assert code == 1
    captured = capsys.readouterr()
    assert "no parseable events" in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_headerless_is_error_exit_1(capsys):
    code = main(["parse-transcript", str(ROOT / "examples" / "headerless" / "journal.md")])
    assert code == 1
    captured = capsys.readouterr()
    assert "no parseable events" in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_format_jsonl_ok(tmp_path, capsys):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 0
    assert "OK: 1 events" in capsys.readouterr().out


def test_parse_transcript_format_jsonl_empty_exit_1(tmp_path, capsys):
    path = tmp_path / "empty.jsonl"
    path.write_text("", encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "no parseable events" in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_format_jsonl_whitespace_only_exit_1(tmp_path, capsys):
    path = tmp_path / "whitespace.jsonl"
    path.write_text(" \n\n\t\n", encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "no parseable events" in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_format_jsonl_utf8_bom_exit_1(tmp_path, capsys):
    path = tmp_path / "bom.jsonl"
    path.write_bytes(
        b'\xef\xbb\xbf{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\n'
    )
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "invalid JSONL" in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_format_jsonl_forces_invalid_line(tmp_path, capsys):
    path = tmp_path / "events.jsonl"
    path.write_text("not-an-object\n", encoding="utf-8")
    assert main(["parse-transcript", str(path)]) == 1
    capsys.readouterr()
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    assert "invalid JSONL" in capsys.readouterr().err


def test_parse_transcript_format_journal_on_stable(capsys):
    code = main(
        [
            "parse-transcript",
            str(ROOT / "examples" / "stable" / "journal.md"),
            "--format",
            "journal",
        ]
    )
    assert code == 0
    assert "OK: 4 events" in capsys.readouterr().out


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


def test_audit_jsonl_clean_exit_0(tmp_path):
    constraints = tmp_path / "constraints.yaml"
    constraints.write_text(
        (
            "name: jsonl-clean\n"
            "constraints:\n"
            "  - id: never_skip_lint\n"
            '    pattern: "lint=FAIL"\n'
        ),
        encoding="utf-8",
    )
    transcript = tmp_path / "events.jsonl"
    transcript.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    assert (
        main(
            [
                "audit",
                "--constraints",
                str(constraints),
                "--transcript",
                str(transcript),
                "--format",
                "jsonl",
            ]
        )
        == 0
    )


def test_audit_jsonl_forbid_match_exit_2(tmp_path, capsys):
    constraints = tmp_path / "constraints.yaml"
    constraints.write_text(
        (
            "name: jsonl-decay\n"
            "constraints:\n"
            "  - id: never_skip_lint\n"
            '    pattern: "lint=FAIL"\n'
        ),
        encoding="utf-8",
    )
    transcript = tmp_path / "events.jsonl"
    transcript.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": "lint=FAIL"}}\n',
        encoding="utf-8",
    )
    code = main(
        [
            "audit",
            "--constraints",
            str(constraints),
            "--transcript",
            str(transcript),
            "--json",
        ]
    )
    assert code == 2
    data = json.loads(capsys.readouterr().out)
    assert data["verdict"] == "DECAY"
    assert {v["constraint_id"] for v in data["violations"]} == {"never_skip_lint"}


def test_audit_jsonl_invalid_or_empty_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    empty = tmp_path / "empty.jsonl"
    empty.write_text("", encoding="utf-8")
    assert main(["audit", "--constraints", constraints, "--transcript", str(empty)]) == 1
    assert "no parseable events" in capsys.readouterr().err

    bad = tmp_path / "bad.jsonl"
    bad.write_text("{not json\n", encoding="utf-8")
    assert (
        main(
            [
                "audit",
                "--constraints",
                constraints,
                "--transcript",
                str(bad),
                "--format",
                "jsonl",
            ]
        )
        == 1
    )
    assert "invalid JSONL" in capsys.readouterr().err


def test_audit_jsonl_timestamp_only_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    path = tmp_path / "timestamp-only.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00"}\n', encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            constraints,
            "--transcript",
            str(path),
            "--format",
            "jsonl",
        ]
    )
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_jsonl_timestamp_only_exit_1(tmp_path, capsys):
    path = tmp_path / "timestamp-only.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00"}\n', encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "OK:" not in captured.out


def test_audit_jsonl_non_string_text_without_fields_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    path = tmp_path / "numeric-text.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "text": 1}\n', encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            constraints,
            "--transcript",
            str(path),
            "--format",
            "jsonl",
        ]
    )
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_jsonl_non_string_text_without_fields_exit_1(tmp_path, capsys):
    path = tmp_path / "numeric-text.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "text": 1}\n', encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "OK:" not in captured.out


def test_audit_jsonl_empty_fields_mapping_without_text_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    path = tmp_path / "empty-fields.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "fields": {}}\n', encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            constraints,
            "--transcript",
            str(path),
            "--format",
            "jsonl",
        ]
    )
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_jsonl_empty_fields_mapping_without_text_exit_1(tmp_path, capsys):
    path = tmp_path / "empty-fields.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "fields": {}}\n', encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "OK:" not in captured.out


def test_audit_jsonl_empty_string_text_without_fields_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    path = tmp_path / "empty-text.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "text": ""}\n', encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            constraints,
            "--transcript",
            str(path),
            "--format",
            "jsonl",
        ]
    )
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_jsonl_empty_string_text_without_fields_exit_1(tmp_path, capsys):
    path = tmp_path / "empty-text.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "text": ""}\n', encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "OK:" not in captured.out


def test_audit_jsonl_missing_timestamp_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    path = tmp_path / "no-timestamp.jsonl"
    path.write_text('{"text": "- gates: lint=PASS"}\n', encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            constraints,
            "--transcript",
            str(path),
            "--format",
            "jsonl",
        ]
    )
    assert code == 1
    captured = capsys.readouterr()
    assert "missing timestamp" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_jsonl_missing_timestamp_exit_1(tmp_path, capsys):
    path = tmp_path / "no-timestamp.jsonl"
    path.write_text('{"text": "- gates: lint=PASS"}\n', encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "missing timestamp" in captured.err
    assert "OK:" not in captured.out


def test_audit_jsonl_non_shaped_timestamp_exit_1(tmp_path, capsys):
    constraints = str(ROOT / "examples" / "stable" / "constraints.yaml")
    path = tmp_path / "yesterday.jsonl"
    path.write_text('{"timestamp": "yesterday", "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    code = main(
        [
            "audit",
            "--constraints",
            constraints,
            "--transcript",
            str(path),
            "--format",
            "jsonl",
        ]
    )
    assert code == 1
    captured = capsys.readouterr()
    assert "timestamp must be YYYY-MM-DD HH:MM" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_jsonl_non_shaped_timestamp_exit_1(tmp_path, capsys):
    path = tmp_path / "yesterday.jsonl"
    path.write_text('{"timestamp": "yesterday", "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    code = main(["parse-transcript", str(path), "--format", "jsonl"])
    assert code == 1
    captured = capsys.readouterr()
    assert "timestamp must be YYYY-MM-DD HH:MM" in captured.err
    assert "OK:" not in captured.out


def test_audit_empty_bodied_journal_event_exit_1(tmp_path, capsys):
    journal = tmp_path / "empty-body.md"
    journal.write_text("## 2026-08-11 09:00\n\n", encoding="utf-8")
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
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "CLEAN" not in captured.err
    assert "OK:" not in captured.out


def test_parse_transcript_empty_bodied_journal_event_exit_1(tmp_path, capsys):
    journal = tmp_path / "empty-body.md"
    journal.write_text("## 2026-08-11 09:00\n\n", encoding="utf-8")
    code = main(["parse-transcript", str(journal)])
    assert code == 1
    captured = capsys.readouterr()
    assert "needs text and/or fields" in captured.err
    assert "OK:" not in captured.out


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


DECAYING_SPEC = str(ROOT / "examples" / "decaying" / "constraints.yaml")


def test_audit_journal_with_utf8_bom_reports_decay(tmp_path, capsys):
    journal = tmp_path / "bom.md"
    journal.write_bytes(
        b"\xef\xbb\xbf## 2026-08-11 09:00\n- gates: tests=PASS, lint=FAIL\n\n"
        b"## 2026-08-11 10:00\n- gates: tests=PASS, lint=PASS\n"
    )
    code = main(["audit", "--constraints", DECAYING_SPEC, "--transcript", str(journal)])
    assert code == 2
    assert "verdict=DECAY" in capsys.readouterr().out


def test_spec_with_utf8_bom_loads(tmp_path, capsys):
    spec = tmp_path / "bom.yaml"
    spec.write_bytes(
        b'\xef\xbb\xbfname: bom\nconstraints:\n  - id: r\n    pattern: "x"\n'
    )
    assert main(["check-constraints", str(spec)]) == 0
    assert "OK: bom (1 constraints)" in capsys.readouterr().out


def test_audit_malformed_first_heading_is_error_exit_1(tmp_path, capsys):
    journal = tmp_path / "pre.md"
    journal.write_text(
        "## 2026-08-11 09:00 UTC\n- gates: lint=FAIL\n\n## 2026-08-11 10:00\n- gates: lint=PASS\n",
        encoding="utf-8",
    )
    code = main(["audit", "--constraints", DECAYING_SPEC, "--transcript", str(journal)])
    captured = capsys.readouterr()
    assert code == 1
    assert "malformed journal heading" in captured.err
    assert "verdict=" not in captured.out


def test_audit_malformed_later_heading_is_error_exit_1(tmp_path, capsys):
    spec = tmp_path / "req.yaml"
    spec.write_text(
        'name: req\nconstraints:\n  - id: r\n    pattern: "lint=PASS"\n    forbid: false\n',
        encoding="utf-8",
    )
    journal = tmp_path / "merge.md"
    journal.write_text(
        "## 2026-08-11 09:00\n- gates: lint=PASS\n\n## 2026-08-11 9:30\n- gates: lint=FAIL\n",
        encoding="utf-8",
    )
    assert main(["audit", "--constraints", str(spec), "--transcript", str(journal)]) == 1
    assert "malformed journal heading" in capsys.readouterr().err
    assert main(["parse-transcript", str(journal)]) == 1
    captured = capsys.readouterr()
    assert "malformed journal heading" in captured.err
    assert "OK:" not in captured.out


def test_audit_non_utf8_transcript_is_error_exit_1(tmp_path, capsys):
    journal = tmp_path / "latin.md"
    journal.write_bytes(b"## 2026-08-11 09:00\n- note: caf\xe9 lint=FAIL\n")
    code = main(["audit", "--constraints", DECAYING_SPEC, "--transcript", str(journal)])
    captured = capsys.readouterr()
    assert code == 1
    assert captured.err.startswith("ERROR: ")
    assert "not valid UTF-8" in captured.err
    assert "Traceback" not in captured.err


def test_check_constraints_non_utf8_spec_is_error_exit_1(tmp_path, capsys):
    spec = tmp_path / "latin.yaml"
    spec.write_bytes(b'name: caf\xe9\nconstraints:\n  - id: r\n    pattern: "x"\n')
    assert main(["check-constraints", str(spec)]) == 1
    captured = capsys.readouterr()
    assert "not valid UTF-8" in captured.err
    assert "OK:" not in captured.out


def test_audit_jsonl_violation_only_in_fields_is_decay(tmp_path, capsys):
    events = tmp_path / "tf.jsonl"
    events.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "all good",'
        ' "fields": {"gates": "lint=FAIL"}}\n',
        encoding="utf-8",
    )
    code = main(["audit", "--constraints", DECAYING_SPEC, "--transcript", str(events)])
    assert code == 2
    assert "verdict=DECAY" in capsys.readouterr().out


def test_failed_report_write_keeps_decay_exit_2(tmp_path, capsys):
    code = main(
        [
            "audit",
            "--constraints",
            DECAYING_SPEC,
            "--transcript",
            str(ROOT / "examples" / "decaying" / "journal.md"),
            "--report",
            str(tmp_path / "nodir" / "r.md"),
        ]
    )
    captured = capsys.readouterr()
    assert code == 2
    assert "verdict=DECAY" in captured.out
    assert captured.err.startswith("ERROR: ")


def test_failed_report_write_on_clean_is_error_exit_1(tmp_path, capsys):
    code = main(
        [
            "audit",
            "--constraints",
            str(ROOT / "examples" / "stable" / "constraints.yaml"),
            "--transcript",
            str(ROOT / "examples" / "stable" / "journal.md"),
            "--report",
            str(tmp_path / "nodir" / "r.md"),
        ]
    )
    assert code == 1
    assert capsys.readouterr().err.startswith("ERROR: ")
