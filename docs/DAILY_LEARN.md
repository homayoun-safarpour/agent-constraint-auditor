# Daily learning — 2026-09-16

**Skill.** JSONL nested-object `fields` values still parse and are stringified. A nested JSON object such as `{"lint": "PASS"}` becomes the string `"{'lint': 'PASS'}"` via `str(value)`. Same path as numeric, boolean, and list field values.

**Why.** Without a named nested-object lock, a later change that rejected objects in `fields` would look like a parser bug. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 123. `"fields": {"gates": {"lint": "PASS"}}` yields `gates="{'lint': 'PASS'}"`.

```bash
python -m pytest -q
# 123 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_object_field_values_are_stringified
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with nested object values still parses?

Answer: Yes. Named test `test_adapter_locks_object_fields_values_are_stringified` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W247
