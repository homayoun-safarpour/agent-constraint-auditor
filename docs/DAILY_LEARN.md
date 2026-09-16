# Daily learning — 2026-09-16

**Skill.** JSONL `fields` that are a mapping with numeric values still parse. Those values are stringified (`1` becomes `"1"`). That is not the timestamp fail-closed rule: a numeric `timestamp` is ERROR; a numeric field value is not.

**Why.** Hire docs that only say non-mapping `fields` is ERROR leave reviewers guessing whether `{"gates": 1}` is CLEAN or ERROR. The parser `str()`s values. A later fail-closed change would need a named test to fail first.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 98. `{"fields": {"gates": 1}}` parses; `fields["gates"]` is `"1"`.

```bash
python -m pytest -q
# 98 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_numeric_field_values_are_stringified
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with numeric values still parses and those values are stringified?

Answer: Yes. Named test `test_adapter_locks_numeric_fields_values_are_stringified` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W156
