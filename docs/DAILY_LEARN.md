# Daily learning — 2026-09-16

**Skill.** A JSONL object line with trailing whitespace still parses. Spaces after the closing brace are stripped before `json.loads`. A UTF-8 BOM is a different ERROR (`invalid JSONL`). A whitespace-only file still returns no events.

**Why.** Without a named trailing-whitespace lock, a later change that passed the raw line to `json.loads` would ERROR a valid object with spaces after `}`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 141.

```bash
python -m pytest -q
# 141 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_trailing_whitespace_still_parses
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object line with trailing whitespace still parses?

Answer: Yes. Named test `test_adapter_locks_jsonl_object_line_trailing_whitespace_still_parses` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W310
