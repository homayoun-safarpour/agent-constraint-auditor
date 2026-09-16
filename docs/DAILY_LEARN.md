# Daily learning — 2026-09-16

**Skill.** A JSONL object line with a trailing comma before `}` is ERROR (invalid JSONL). Spaces after `}` still parse; a comma before `}` is not ignored because standard JSON forbids it.

**Why.** Without a named trailing-comma lock, a later JSON5/`json.loads` loosening would silently accept `{...,}`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 155.

```bash
python -m pytest -q
# 155 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_trailing_comma_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a trailing comma before the closing brace is ERROR and the comma is not ignored?

Answer: Yes. Named test `test_adapter_locks_jsonl_trailing_comma_before_brace_is_invalid_jsonl` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W359
