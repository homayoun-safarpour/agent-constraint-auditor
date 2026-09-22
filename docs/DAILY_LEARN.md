# Daily learning — 2026-09-22

**Skill.** Week-close freeze: LOOP_STATE names week counted 2026-09-14 to 2026-09-20. Named-claim pytest stays 163. This file is the auditor close record; do not scaffold a second public repo from this checkout.

**Why.** Monday froze the counted week. The hire signal remains the nine-exit MATRIX and the decaying `--report` triple. A new JSONL parser family would not close the week.

**Worked example** (this repo). Replay the live MATRIX lock and the decaying report numbers.

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

**Recall probe.** What counted week does the freeze name, and what nine-exit row must still reprint?

Answer: week counted 2026-09-14 to 2026-09-20. MATRIX `0/2/0/2/1/1/0/2/1`. Decaying report stays 3 / first_index=2 / slope=2.000. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `LOOP_STATE.md` BENCHMARK GATE §A · `tests/test_examples.py` · `docs/LINKEDIN_DRAFT.md`
