# Daily learning — 2026-09-16

**Skill.** A fail-closed JSONL timestamp is not done until every hire surface names the same fixture: parser → worked example → examples table → adapter → MATRIX → reliability card → interview pack → CONTRIBUTING.

**Why.** A reviewer who only reads `docs/RELIABILITY_CARD.md` or `CONTRIBUTING.md` would have missed `jsonl_bad_timestamp` while MATRIX already had nine exits. Hire docs that lag the matrix look like an incomplete instrument.

**Worked example** (this repo). ISO `T` is ERROR, not CLEAN:

```bash
constraint-auditor audit \
  --constraints examples/jsonl_bad_timestamp/constraints.yaml \
  --transcript examples/jsonl_bad_timestamp/events.jsonl \
  --format jsonl
# ERROR: JSONL line 1 timestamp must be YYYY-MM-DD HH:MM
# exit 1
```

Sunday exit matrix is now `0/2/0/2/1/1/0/2/1` (`examples/MATRIX.md`).

**Recall probe.** Does `docs/RELIABILITY_CARD.md` name `jsonl_bad_timestamp` as ERROR exit 1?

Answer: Yes. Primary signal is `0` / `2` / `1`. Field alignment names `jsonl_stable` / `jsonl_decaying` / `jsonl_bad_timestamp`. Interview demo and CONTRIBUTING name the same fixture.

**Retrieve.** `examples/jsonl_bad_timestamp/` · `examples/MATRIX.md` · `docs/RELIABILITY_CARD.md` · `docs/INTERVIEW.md` · `CONTRIBUTING.md` · `tests/test_examples.py` · `LOOP_STATE.md` NEXT TICK W70
