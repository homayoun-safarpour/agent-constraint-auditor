# Daily learning — 2026-09-16

**Skill.** A JSONL `fields` mapping with a key containing a colon still parses. The key is not split: `"gates:lint"` stays `"gates:lint"` and the body is `- gates:lint: PASS`. Markdown `LINE_RE` would stop the key at the first colon; JSONL does not.

**Why.** Without a named colon-key lock, a later change that reused the markdown field regex on JSONL bodies would split `gates:lint` into `gates` / `lint: PASS`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 133. `"fields": {"gates:lint": "PASS"}` yields `gates:lint="PASS"` and text `- gates:lint: PASS`.

```bash
python -m pytest -q
# 133 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_field_keys_containing_a_colon_still_parse
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with a key containing a colon still parses?

Answer: Yes. Named test `test_adapter_locks_fields_keys_containing_a_colon_still_parse` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W282
