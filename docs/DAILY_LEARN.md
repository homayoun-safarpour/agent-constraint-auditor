# Daily learning — 2026-09-16

**Skill.** JSONL list `fields` values still parse and are stringified. A JSON array such as `[1]` becomes the string `"[1]"` via `str(value)`. Same path as numeric and boolean field values.

**Why.** Without a named list-value lock, a later change that rejected arrays in `fields` would look like a parser bug. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 121. `"fields": {"gates": [1]}` yields `gates="[1]"`.

```bash
python -m pytest -q
# 121 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_list_field_values_are_stringified
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with list values still parses?

Answer: Yes. Named test `test_adapter_locks_list_fields_values_are_stringified` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W240
