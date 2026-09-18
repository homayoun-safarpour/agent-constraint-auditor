# Daily learning — 2026-09-18

**Skill.** A JSONL object line with an unquoted string value is ERROR (invalid JSONL). Quoted strings still parse; `{ "text": gates }` is not accepted because JSON requires quoted strings.

**Why.** Without a named unquoted-value lock, a later JSON5 loosening would silently accept `{ "text": gates }`. Unquoted keys are already locked. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 161.

```bash
python -m pytest -q
# 161 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_unquoted_string_values_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object line with an unquoted string value is ERROR and unquoted values are not accepted?

Answer: Yes. Named test `test_adapter_locks_jsonl_unquoted_string_values_are_invalid_jsonl` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W380
