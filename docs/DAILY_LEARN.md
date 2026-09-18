# Daily learning — 2026-09-18

**Skill.** A JSONL object line with unquoted keys is ERROR (invalid JSONL). Double-quoted keys still parse; `{timestamp: "..."}` is not accepted because standard JSON forbids unquoted keys.

**Why.** Without a named unquoted-key lock, a later JSON5 loosening would silently accept `{timestamp: ...}`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 159.

```bash
python -m pytest -q
# 159 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_unquoted_keys_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object line with unquoted keys is ERROR and unquoted keys are not accepted?

Answer: Yes. Named test `test_adapter_locks_jsonl_unquoted_keys_are_invalid_jsonl` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W373
