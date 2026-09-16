# Daily learning — 2026-09-16

**Skill.** A JSONL `fields` mapping with two keys keeps insertion order. Body lines follow that order: `{"gates": "PASS", "lint": "ok"}` yields `- gates: PASS` then `- lint: ok`. This is `_text_from_fields` joining in mapping order, not a sort.

**Why.** Without a named two-key order lock, a later change that sorted keys would rewrite the synthesized body. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 137. `"fields": {"gates": "PASS", "lint": "ok"}` yields keys `gates` then `lint` and text `- gates: PASS\n- lint: ok`.

```bash
python -m pytest -q
# 137 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_two_key_fields_keep_insertion_order
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with two keys keeps insertion order?

Answer: Yes. Named test `test_adapter_locks_two_key_fields_keep_insertion_order` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W296
