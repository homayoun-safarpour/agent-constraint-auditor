# Daily learning — 2026-09-16

**Skill.** A JSONL object line with leading whitespace still parses. Spaces before `{` are stripped before `json.loads`. Pair to trailing spaces after `}`. A UTF-8 BOM is still ERROR.

**Why.** Without a named leading-whitespace lock, a later change that passed the raw line to `json.loads` would ERROR an indented object. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 147.

```bash
python -m pytest -q
# 147 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_line_with_leading_whitespace_still_parses
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object line with leading whitespace still parses?

Answer: Yes. Named test `test_adapter_locks_jsonl_object_line_leading_whitespace_still_parses` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W331
