# Daily learning — 2026-09-16

**Skill.** Extra JSONL object keys beyond `timestamp`, `text`, and `fields` are ignored. `id` and `role` do not ERROR and do not become event attributes. The parsed event still has only those three slots.

**Why.** Loop-engine dumps often carry extra keys. Without a named test, a later “unknown key is ERROR” change would look like a bug in the fixtures. The adapter sentence matches the parser lock.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 101. An object with `id` and `role` beside a valid timestamp and text still parses.

```bash
python -m pytest -q
# 101 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_extra_object_keys_are_ignored
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say extra JSONL object keys beyond `timestamp`, `text`, and `fields` are ignored?

Answer: Yes. Named test `test_adapter_locks_extra_jsonl_object_keys_are_ignored` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W167
