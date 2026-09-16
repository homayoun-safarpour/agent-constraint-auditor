# Daily learning — 2026-09-16

**Skill.** Fail-closed JSONL is more than timestamp shape. A line that is valid JSON but not an object, and a `fields` value that is not a mapping, must ERROR the same way a bad timestamp does: parser named test, then adapter sentence, then adapter lock.

**Why.** Timestamp-shape coverage can look complete while a JSON array line or `fields: ["gates"]` still has no hire-doc sentence. Reviewers who only read the adapter would miss those exits.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 88. A JSONL array line raises `must be an object`. A JSONL `fields` array raises `fields must be a mapping`.

```bash
python -m pytest -q
# 88 passed
constraint-auditor audit \
  --constraints examples/jsonl_bad_timestamp/constraints.yaml \
  --transcript examples/jsonl_bad_timestamp/events.jsonl \
  --format jsonl
# ERROR: JSONL line 1 timestamp must be YYYY-MM-DD HH:MM
# exit 1
```

**Recall probe.** Does `docs/ADAPTER.md` name both a non-object JSONL line and a non-mapping `fields` value as ERROR?

Answer: Yes. Named tests lock those sentences. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W104
