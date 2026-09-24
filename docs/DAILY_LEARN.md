# Daily learning — 2026-09-24

**Skill.** First-screen decay line: `violations=3 first_index=2 slope=2.000`. Slope is Q4 rate minus Q1 rate.

**Why.** README now leads with the decaying fixture. The lock is those three numbers staying true, not a new parser or a new repo.

**Worked example** (this repo). Four events, one per quartile. Event 2 hits `never_skip_lint`. Event 3 hits `never_skip_lint` and `no_force_push`. Three violations, first at index 2. Q1 rate 0.00, Q4 rate 2.00, slope 2.000.

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# exit 2
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# report: Verdict: DECAY · First violation index: 2 · Decay slope (Q4-Q1 rate): 2.000

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# exit 0 · first_index=None · slope=0.000
```

**Recall probe.** What three numbers does decaying reprint, and how is slope defined?

Answer: 3 / first_index=2 / slope=2.000. Slope = last-quartile violation rate minus first-quartile rate. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying` · `src/constraintauditor/decay.py` · README first screen
