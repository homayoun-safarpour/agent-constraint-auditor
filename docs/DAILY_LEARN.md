# Daily learning — 2026-09-17

**Skill.** A JSONL object line with single-quoted strings is ERROR (invalid JSONL). Double-quoted strings still parse; single quotes are not accepted because standard JSON forbids them.

**Why.** Without a named single-quote lock, a later JSON5/`ast.literal_eval` loosening would silently accept `{'timestamp': ...}`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 157.

```bash
python -m pytest -q
# 157 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_single_quoted_strings_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object line with single-quoted strings is ERROR and single quotes are not accepted?

Answer: Yes. Named test `test_adapter_locks_jsonl_single_quoted_strings_are_invalid_jsonl` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W366
