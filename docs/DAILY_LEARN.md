# Daily learning — 2026-09-16

**Skill.** A JSONL `fields` mapping with an empty-string value still parses. That value is not missing fields. `"fields": {"gates": ""}` yields `gates=""` and text `- gates: `. An empty mapping `{}` is still missing fields; a present key with `""` is not.

**Why.** Without a named empty-string-value lock, a later change that treated `""` like a missing mapping would ERROR a line that still has a key. Null field values also become empty strings, on a different path. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 131. `"fields": {"gates": ""}` yields `gates=""` and text `- gates: `.

```bash
python -m pytest -q
# 131 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_empty_string_field_values_still_parse
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with an empty-string value still parses?

Answer: Yes. Named test `test_adapter_locks_empty_string_fields_values_still_parse` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W275
