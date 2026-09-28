# Daily learning — 2026-09-28

**Skill.** Decay slope is Q4 minus Q1 violation rate, not a vibe that "later events look worse." Monday retarget stays on this repo and reprints `slope=2.000` from `examples/decaying/`. Do not scaffold a second public week from this checkout.

**Why.** The hire-visible lock is measurable constraint decay: `violations=3 first_index=2 slope=2.000`. Exit 2 fails CI. Exit 1 is unreadable input, a different polarity.

**Worked example** (this repo). Four events, one per quartile. Event 2 matches `never_skip_lint`. Event 3 matches that rule and `no_force_push`. Q1 rate 0, Q4 rate 2, slope 2.000.

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000
```

**Recall probe.** Why is decaying slope `2.000`, and which event is `first_index`?

Answer: four events → Q1–Q4 each size 1. Zero violations in Q1; two in Q4 (lint FAIL + force-push). Slope = 2 − 0 = 2.000. `first_index=2` is the first lint-FAIL event (0-based). Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/decay.py` · `examples/decaying/` · README first screen · `examples/MATRIX.md`
