# Daily learning — 2026-10-01

**Skill.** Quartile rate can exceed 1.0. Four decaying events map one-per-bucket. The last event hits two forbid rules, so Q4 is `2.00`, not `1.00`. Slope is Q4 rate minus Q1 rate: `2.000`.

**Why.** The hire-visible lock is a rate trend, not a hit counter. `violations=3` counts constraint matches. `slope=2.000` reads the quartile table. Those are different numbers on purpose.

**Worked example** (this repo). Replay decaying, then read the report table. Contrast stable so you do not treat `2.000` as a count.

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# --report quartile row: 0.00 | 0.00 | 1.00 | 2.00

# Event 0/1 clean (Q1/Q2). Event 2 lint=FAIL (Q3 rate 1.00).
# Event 3 lint=FAIL + force-push (Q4 rate 2/1 = 2.00). Slope = 2.00 - 0.00.

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl
# same line: slope=2.000

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000
```

**Recall probe.** Why is decaying Q4 `2.00` and slope `2.000`, not `3`?

Answer: Rate = hits in the bucket / events in the bucket. Event 3 holds `never_skip_lint` and `no_force_push`. Slope = Q4 − Q1 = `2.00 − 0.00`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying` · `examples/jsonl_decaying` · `examples/stable` · `src/constraintauditor/decay.py` · README first-screen line
