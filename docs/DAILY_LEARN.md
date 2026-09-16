# Daily learning — 2026-09-16

**Skill.** An empty JSONL `fields` mapping (`{}`) is treated as missing fields. Timestamp plus `{}` and no text is ERROR (`needs text and/or fields`). Timestamp plus text plus `{}` still parses; `fields` on the event is `{}`.

**Why.** `if not has_text and not fields` treats an empty dict as absent. Without a named test, a later change that treated `{}` as present would look like a parser bug. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 107. `"fields": {}` without text raises; with text, the event keeps empty fields.

```bash
python -m pytest -q
# 107 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_empty_fields_mapping_is_treated_as_missing
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say an empty JSONL `fields` mapping is treated as missing fields?

Answer: Yes. Named test `test_adapter_locks_empty_jsonl_fields_mapping_is_treated_as_missing` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W191
