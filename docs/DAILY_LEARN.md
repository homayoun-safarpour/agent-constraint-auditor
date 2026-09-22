# Daily learning — 2026-09-22

**Skill.** Mid-week close-record hold: this checkout names week counted 2026-09-14 to 2026-09-20 and reprints that floor. It does not start a new instrument.

**Why.** Monday froze LOOP_STATE to the counted week. The hire signal is a replayable nine-exit contract, not another JSONL parser family. Next public week is a Monday retarget elsewhere. Mid-week scaffolding from here would break the freeze.

**Worked example** (this repo). Replay the closed-week floor. Do not add fixtures.

```bash
python -m pytest -q
# 163 passed
python -m pytest -q tests/test_examples.py::test_examples_matrix_live_exits_match_table
# 1 passed — 0/2/0/2/1/1/0/2/1
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# exit 2; Verdict: DECAY; 3 violations; first at event 2; slope 2.000
```

**Recall probe.** After the Monday freeze, what week does this file hold, and what must still reprint?

Answer: Week counted 2026-09-14 to 2026-09-20. MATRIX `0/2/0/2/1/1/0/2/1`. Decaying `--report` stays 3 / first_index=2 / slope=2.000. Do not scaffold `agent-trust-gate` from this checkout. Do not open a JSONL parser family. Do not pytest-lock this card.

**Retrieve.** `examples/MATRIX.md` · `LOOP_STATE.md` BENCHMARK GATE §A · `tests/test_examples.py` · `docs/LINKEDIN_DRAFT.md`
