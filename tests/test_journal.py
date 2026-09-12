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


def test_parse_jsonl_invalid_line_is_transcript_error(tmp_path):
    path = tmp_path / "bad.jsonl"
    path.write_text(
        '{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS"}\nnot-json\n',
        encoding="utf-8",
    )
    with pytest.raises(TranscriptError, match="invalid JSONL"):
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


def test_parse_jsonl_empty_fields_without_text_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "fields": {}}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(path)


def test_parse_jsonl_whitespace_text_without_fields_is_transcript_error(tmp_path):
    path = tmp_path / "events.jsonl"
    path.write_text('{"timestamp": "2026-08-11 09:00", "text": "   "}\n', encoding="utf-8")
    with pytest.raises(TranscriptError, match="needs text and/or fields"):
        parse_jsonl_transcript(path)


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
