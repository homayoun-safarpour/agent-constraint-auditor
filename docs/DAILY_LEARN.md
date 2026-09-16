# Daily learning — 2026-09-16

**Skill.** A JSONL object line with trailing non-whitespace after `}` is ERROR (invalid JSONL). Spaces after `}` still parse; `} extra` is Extra data for `json.loads`, so the extra text is not stripped.

**Why.** Without a named trailing-junk lock, a later change that truncated at the last `}` would silently accept `} extra`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 151.

```bash
python -m pytest -q
# 151 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_trailing_non_whitespace_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say trailing non-whitespace after the closing brace is ERROR and that extra text is not stripped?

Answer: Yes. Named test `test_adapter_locks_jsonl_trailing_non_whitespace_after_brace_is_invalid_jsonl` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W345
