# Daily learning — 2026-09-16

**Skill.** A JSONL `#` comment line is ERROR (invalid JSONL). It is not skipped. Blank lines between objects still parse; a `#` line is not blank, so `json.loads` fails closed.

**Why.** Without a named hash-comment lock, a later skip-if-starts-with-`#` change would silently drop comments. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 149.

```bash
python -m pytest -q
# 149 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_hash_comment_line_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `#` comment line is ERROR and is not skipped?

Answer: Yes. Named test `test_adapter_locks_jsonl_hash_comment_lines_are_invalid_jsonl` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W338
