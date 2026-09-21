# Daily learning — 2026-09-21

**Skill.** Monday week-close freeze: this checkout reprints last week's floor. It does not start the next instrument.

**Why.** Sunday already closed week 2026-09-14. The hire signal is a frozen nine-exit contract, not a new JSONL parser family. Supervisor retargets the next public week elsewhere. Scaffolding that repo from here would be a mid-week new-repo move on a Monday freeze.

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

**Recall probe.** After Sunday's gate, what does Monday do in this repo?

Answer: Freeze. Reprint MATRIX `0/2/0/2/1/1/0/2/1` and decaying `--report` 3 / first_index=2 / slope=2.000. Do not scaffold `agent-trust-gate` from this checkout. Do not open a JSONL parser family. Do not pytest-lock this card.

**Retrieve.** `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W385 · `tests/test_examples.py` · `docs/LINKEDIN_DRAFT.md`
