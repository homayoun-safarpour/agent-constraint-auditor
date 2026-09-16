# Daily learning — 2026-09-16

**Skill.** A JSONL object line ending in CRLF still parses. `splitlines()` drops the carriage return, so `\r\n` is not invalid JSONL. Trailing spaces after `}` are a different strip; a UTF-8 BOM is still ERROR.

**Why.** Without a named CRLF lock, a later change that required Unix `\n` only would fail a Windows JSONL dump. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 143.

```bash
python -m pytest -q
# 143 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_crlf_object_lines_still_parse
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object line ending in CRLF still parses?

Answer: Yes. Named test `test_adapter_locks_jsonl_crlf_object_lines_still_parse` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W317
