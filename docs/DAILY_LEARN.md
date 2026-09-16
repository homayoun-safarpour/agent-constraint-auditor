# Daily learning — 2026-09-16

**Skill.** A JSONL `fields` mapping with a whitespace-only key still parses. The key is not stripped: `" "` stays `" "`. Body is `-  : lint=PASS`. Empty-string keys remain a separate case.

**Why.** Without a named whitespace-key lock, a later change that stripped keys would merge `" "` into `""`. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 127. `"fields": {" ": "lint=PASS"}` yields key `" "` and text `-  : lint=PASS`.

```bash
python -m pytest -q
# 127 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_whitespace_only_field_keys_still_parse
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `fields` mapping with a whitespace-only key still parses?

Answer: Yes. Named test `test_adapter_locks_whitespace_only_fields_keys_still_parse` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W261
