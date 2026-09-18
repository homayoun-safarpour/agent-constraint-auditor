# Daily learning — 2026-09-18

**Skill.** A JSONL object line with unquoted keys is ERROR (invalid JSONL). Quoted keys still parse; `{timestamp: ...}` is not accepted because standard JSON requires double-quoted keys.

**Why.** Without a named unquoted-key lock, a later JSON5 loosening would silently accept `{timestamp: ...}`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 158.

```bash
python -m pytest -q
# 158 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_unquoted_keys_is_transcript_error
# 1 passed
```

**Recall probe.** Does `json.loads` accept `{timestamp: "2026-08-11 09:00", text: "- gates: lint=PASS"}`?

Answer: No. Named test `test_parse_jsonl_object_line_with_unquoted_keys_is_transcript_error` raises `TranscriptError` matching `invalid JSONL`. Adapter sentence is still W367. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W367
