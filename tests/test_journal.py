from dataclasses import asdict
from pathlib import Path

import pytest

from constraintauditor.journal import (
    TranscriptError,
    detect_format,
    parse_jsonl_transcript,
    parse_loop_engine_journal,
)

ROOT = Path(__file__).parent.parent


def test_parse_loop_engine_journal_blocks():
    events = parse_loop_engine_journal(ROOT / "examples" / "stable" / "journal.md")
    assert len(events) == 4
    assert events[0].timestamp.startswith("2026-08-11")
    assert "gates" in events[0].fields
    assert "decision" in events[0].fields


def test_parse_loop_engine_journal_double_space_heading_still_parses(tmp_path):
    path = tmp_path / "double.md"
    path.write_text(
        "## 2026-08-11  09:00\n- gates: lint=PASS\n",
        encoding="utf-8",
    )
    events = parse_loop_engine_journal(path)
    assert len(events) == 1
    assert events[0].timestamp == "2026-08-11  09:00"
    assert events[0].fields["gates"] == "lint=PASS"
    jsonl = tmp_path / "double.jsonl"
    jsonl.write_text(
        '{"timestamp": "2026-08-11  09:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(jsonl)


def test_parse_jsonl_transcript_uses_text_or_fields(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        (
            '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\n'
            '{"timestamp": "2026-08-11 10:00", "fields": {"gates": "lint=PASS",'
            ' "decision": "advance"}}\n'
        ),
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 2
    assert events[0].timestamp == "2026-08-11 09:00"
    assert events[0].text == "- gates: lint=PASS"
    assert events[1].fields == {"gates": "lint=PASS", "decision": "advance"}
    assert "lint=PASS" in events[1].text
    assert detect_format(path) == "jsonl"


def test_parse_jsonl_padded_timestamp_still_parses(tmp_path):
    path = tmp_path / "padded.jsonl"
    path.write_text(
        '{"timestamp": " 2026-08-11 09:00 ", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].timestamp == "2026-08-11 09:00"
    assert events[0].text == "- gates: lint=PASS"


def test_parse_jsonl_invalid_line_is_transcript_error(tmp_path):
    path = tmp_path / "bad.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\nnot-json\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="invalid JSONL"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_empty_file_returns_no_events(tmp_path):
    path = tmp_path / "empty.jsonl"
    path.write_text("", encoding="utf-8")
    assert parse_jsonl_transcript(path) == []


def test_parse_jsonl_whitespace_only_file_returns_no_events(tmp_path):
    path = tmp_path / "whitespace.jsonl"
    path.write_text(" \n\n\t\n", encoding="utf-8")
    assert parse_jsonl_transcript(path) == []


def test_parse_jsonl_object_line_with_trailing_whitespace_still_parses(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}  \n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"


def test_parse_jsonl_object_line_with_leading_whitespace_still_parses(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '  {"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"


def test_parse_jsonl_crlf_object_lines_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_bytes(
        b'{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\r\n'
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"


def test_parse_jsonl_blank_lines_between_objects_are_skipped(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: a"}\n'
        "\n"
        '{"timestamp": "2026-08-11 10:00", "text": "- gates: b"}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 2
    assert events[0].text == "- gates: a"
    assert events[1].text == "- gates: b"


def test_parse_jsonl_utf8_bom_is_transcript_error(tmp_path):
    path = tmp_path / "bom.jsonl"
    path.write_bytes(
        b'\xef\xbb\xbf{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\n'
    )
    with pytest.raises(TranscriptError, match="invalid JSONL"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_non_object_line_is_transcript_error(tmp_path):
    path = tmp_path / "array.jsonl"
    path.write_text(
        '[{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}]\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="must be an object"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_timestamp_only_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_missing_timestamp_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"text": "- gates: lint=PASS"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="missing timestamp"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_blank_or_non_string_timestamp_is_transcript_error(tmp_path):
    blank = tmp_path / "blank.jsonl"
    blank.write_text('{"timestamp": "   ", "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="missing timestamp"):
        parse_jsonl_transcript(blank)
    numeric = tmp_path / "numeric.jsonl"
    numeric.write_text('{"timestamp": 1757664000, "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="missing timestamp"):
        parse_jsonl_transcript(numeric)
    null_ts = tmp_path / "null.jsonl"
    null_ts.write_text('{"timestamp": null, "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="missing timestamp"):
        parse_jsonl_transcript(null_ts)
    false_ts = tmp_path / "false.jsonl"
    false_ts.write_text('{"timestamp": false, "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="missing timestamp"):
        parse_jsonl_transcript(false_ts)
    true_ts = tmp_path / "true.jsonl"
    true_ts.write_text('{"timestamp": true, "text": "- gates: lint=PASS"}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="missing timestamp"):
        parse_jsonl_transcript(true_ts)


def test_parse_jsonl_non_shaped_timestamp_is_transcript_error(tmp_path):
    yesterday = tmp_path / "yesterday.jsonl"
    yesterday.write_text(
        '{"timestamp": "yesterday", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(yesterday)
    iso_t = tmp_path / "iso.jsonl"
    iso_t.write_text(
        '{"timestamp": "2026-08-11T09:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(iso_t)
    date_only = tmp_path / "date.jsonl"
    date_only.write_text(
        '{"timestamp": "2026-08-11", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(date_only)
    with_seconds = tmp_path / "seconds.jsonl"
    with_seconds.write_text(
        '{"timestamp": "2026-08-11 09:00:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(with_seconds)
    zulu = tmp_path / "zulu.jsonl"
    zulu.write_text(
        '{"timestamp": "2026-08-11 09:00Z", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(zulu)
    offset = tmp_path / "offset.jsonl"
    offset.write_text(
        '{"timestamp": "2026-08-11 09:00+00:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(offset)
    double_space = tmp_path / "double_space.jsonl"
    double_space.write_text(
        '{"timestamp": "2026-08-11  09:00", "text": "- gates: lint=PASS"}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="timestamp must be YYYY-MM-DD HH:MM"):
        parse_jsonl_transcript(double_space)


def test_parse_jsonl_empty_fields_without_text_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "fields": {}}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_non_mapping_fields_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": ["gates"]}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="fields must be a mapping"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_numeric_field_values_are_stringified(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": 1}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields["gates"] == "1"


def test_parse_jsonl_boolean_field_values_are_stringified(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00",'
        ' "fields": {"ok": true, "blocked": false}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields["ok"] == "True"
    assert events[0].fields["blocked"] == "False"


def test_parse_jsonl_list_field_values_are_stringified(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": [1]}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields["gates"] == "[1]"


def test_parse_jsonl_object_field_values_are_stringified(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00",'
        ' "fields": {"gates": {"lint": "PASS"}}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields["gates"] == "{'lint': 'PASS'}"


def test_parse_jsonl_field_keys_are_stringified(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"1": "lint=PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    (key,) = events[0].fields
    assert key == "1"
    assert type(key) is str
    assert events[0].fields == {"1": "lint=PASS"}
    assert events[0].text == "- 1: lint=PASS"


def test_parse_jsonl_empty_string_field_keys_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"": "lint=PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields == {"": "lint=PASS"}
    assert events[0].text == "- : lint=PASS"


def test_parse_jsonl_whitespace_only_field_keys_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {" ": "lint=PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields == {" ": "lint=PASS"}
    assert events[0].text == "-  : lint=PASS"


def test_parse_jsonl_whitespace_only_field_values_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": "   "}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields == {"gates": "   "}
    assert events[0].text == "- gates:    "


def test_parse_jsonl_empty_string_field_values_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": ""}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields == {"gates": ""}
    assert events[0].text == "- gates: "


def test_parse_jsonl_field_keys_containing_a_colon_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates:lint": "PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields == {"gates:lint": "PASS"}
    assert events[0].text == "- gates:lint: PASS"


def test_parse_jsonl_field_values_containing_a_colon_still_parse(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": "lint:PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields == {"gates": "lint:PASS"}
    assert events[0].text == "- gates: lint:PASS"


def test_parse_jsonl_two_key_fields_keep_insertion_order(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00",'
        ' "fields": {"gates": "PASS", "lint": "ok"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert list(events[0].fields) == ["gates", "lint"]
    assert events[0].fields == {"gates": "PASS", "lint": "ok"}
    assert events[0].text == "- gates: PASS\n- lint: ok"


def test_parse_jsonl_null_field_values_become_empty_strings(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {"gates": null}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].fields["gates"] == ""


def test_parse_jsonl_extra_object_keys_are_ignored(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS",'
        ' "id": "evt-1", "role": "agent"}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    data = asdict(events[0])
    assert data["timestamp"] == "2026-08-11 09:00"
    assert data["text"] == "- gates: lint=PASS"
    assert "id" not in data
    assert "role" not in data


def test_parse_jsonl_non_string_text_is_treated_as_missing(tmp_path):
    missing = tmp_path / "numeric-text.jsonl"
    missing.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": 1}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(missing)

    with_fields = tmp_path / "numeric-text-fields.jsonl"
    with_fields.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": 1,'
        ' "fields": {"gates": "lint=PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(with_fields)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"
    assert events[0].fields == {"gates": "lint=PASS"}


def test_parse_jsonl_empty_fields_mapping_is_treated_as_missing(tmp_path):
    missing = tmp_path / "empty-fields.jsonl"
    missing.write_text(
        '{"timestamp": "2026-08-11 09:00", "fields": {}}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(missing)

    with_text = tmp_path / "empty-fields-text.jsonl"
    with_text.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS",'
        ' "fields": {}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(with_text)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"
    assert events[0].fields == {}


def test_parse_jsonl_whitespace_text_without_fields_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "text": "   "}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_whitespace_text_with_fields_uses_fields(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "   ",'
        ' "fields": {"gates": "lint=PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"
    assert events[0].fields == {"gates": "lint=PASS"}


def test_parse_jsonl_empty_string_text_with_fields_uses_fields(tmp_path):
    missing = tmp_path / "empty-text.jsonl"
    missing.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": ""}\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(missing)

    with_fields = tmp_path / "empty-text-fields.jsonl"
    with_fields.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "",'
        ' "fields": {"gates": "lint=PASS"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(with_fields)
    assert len(events) == 1
    assert events[0].text == "- gates: lint=PASS"
    assert events[0].fields == {"gates": "lint=PASS"}


def test_parse_jsonl_nonempty_text_with_fields_uses_text(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00",'
        ' "text": "- gates: from-text",'
        ' "fields": {"gates": "from-fields"}}\n',
        encoding="utf-8",
    )
    events = parse_jsonl_transcript(path)
    assert len(events) == 1
    assert events[0].text == "- gates: from-text"
    assert events[0].fields == {"gates": "from-fields"}


def test_parse_loop_engine_journal_empty_bodied_event_is_error(tmp_path):
    path = tmp_path / "empty-body.md"
    path.write_text("## 2026-08-11 09:00\n\n", encoding="utf-8")
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_loop_engine_journal(path)


def test_parse_loop_engine_journal_empty_bodied_event_among_valid_is_error(tmp_path):
    path = tmp_path / "mixed.md"
    path.write_text(
        (
            "## 2026-08-11 09:00\n"
            "- gates: lint=PASS\n"
            "\n"
            "## 2026-08-11 10:00\n"
            "\n"
        ),
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="2026-08-11 10:00"):
        parse_loop_engine_journal(path)


def test_detect_format_keeps_dated_journal():
    assert detect_format(ROOT / "examples" / "stable" / "journal.md") == "journal"
