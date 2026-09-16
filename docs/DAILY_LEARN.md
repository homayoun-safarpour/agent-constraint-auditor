# Daily learning — 2026-09-16

**Skill.** JSONL boolean `fields` values still parse and are stringified. JSON `true` becomes `"True"` and JSON `false` becomes `"False"` (`str(True)` / `str(False)`). This is values only, not a boolean-field type enum.

**Why.** Numeric field values already stringify. Without a named boolean-value lock, a later change that rejected `true`/`false` in `fields` would look like a parser bug. Do not spray boolean field types.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 119. `"fields": {"ok": true, "blocked": false}` yields `ok="True"` and `blocked="False"`.

```bash
python -m pytest -q
# 119 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_boolean_field_values_are_stringified
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with boolean values still parses?

Answer: Yes. Named test `test_adapter_locks_boolean_fields_values_are_stringified` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W233
