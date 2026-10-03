# Daily learning — 2026-10-03

**Skill.** `forbid: false` treats a missing required pattern as DECAY, not ERROR. `required_missing` parses four dated events that never write `lint=PASS`. That is exit `2`, `violations=4`, `first_index=0`, `slope=0.000`.

**Why.** The hire-visible lock is CI fail on omission, not only on a forbidden match. Friday's empty journal is ERROR because nothing parsed. This fixture parsed; the agent skipped the required gate. Slope is flat because the miss starts at event 0 and never recovers. MATRIX third/fourth exits are `0/2`.

**Worked example** (this repo). Replay present vs missing, then empty so you do not collapse `2` and `1`.

```bash
constraint-auditor audit \
  --constraints examples/required_present/constraints.yaml \
  --transcript examples/required_present/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000

constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md \
  --report /tmp/required-decay.md
# verdict=DECAY exit=2 violations=4 first_index=0 slope=0.000
# report: Verdict: DECAY · 4 violations, first at event 0 · require_lint_pass

constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
# ERROR: transcript contains no parseable events · exit 1
```

**Recall probe.** Why is `required_missing` exit `2` with `slope=0.000`, not exit `1`?

Answer: Four dated events parsed; each lacks `lint=PASS`. Missing required pattern is DECAY. One hit per quartile → rates `1.00|1.00|1.00|1.00`, slope Q4−Q1 = `0`. Empty is ERROR. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/required_present` · `examples/required_missing` · `examples/empty` · `src/constraintauditor/checkers.py` · `examples/MATRIX.md`
