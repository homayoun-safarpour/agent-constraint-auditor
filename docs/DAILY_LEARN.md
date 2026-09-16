# Daily learning — 2026-09-16

**Skill.** JSONL `fields` keys stay strings. A digit key such as `"1"` is the string `1`, not an integer. `_fields_from_mapping` uses `str(key)`; `json.loads` already yields string keys, and the named parser keeps that contract.

**Why.** Numeric field *values* already stringify. Without a named key lock, a later change that stored digit keys as ints would break field lookup. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 117. `"fields": {"1": "lint=PASS"}` yields key `"1"` and text `- 1: lint=PASS`.

```bash
python -m pytest -q
# 117 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_field_keys_are_stringified
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say JSONL `fields` keys stay strings?

Answer: Yes. Named test `test_adapter_locks_jsonl_fields_keys_stay_strings` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W226
