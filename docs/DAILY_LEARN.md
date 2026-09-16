# Daily learning — 2026-09-16

**Skill.** A JSONL `fields` mapping with a value containing a colon still parses. The value is not split: `"lint:PASS"` stays `"lint:PASS"` and the body is `- gates: lint:PASS`. Pair to the colon-in-key lock; this is the value side.

**Why.** Without a named colon-value lock, a later change that took only the substring after the first colon would drop `lint` from `lint:PASS`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 135. `"fields": {"gates": "lint:PASS"}` yields `gates="lint:PASS"` and text `- gates: lint:PASS`.

```bash
python -m pytest -q
# 135 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_field_values_containing_a_colon_still_parse
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with a value containing a colon still parses?

Answer: Yes. Named test `test_adapter_locks_fields_values_containing_a_colon_still_parse` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W289
