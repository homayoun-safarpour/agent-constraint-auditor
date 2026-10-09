# Daily learning — 2026-10-09

**Skill.** `slope` is Q4 rate minus Q1 rate, not a fitted trend. Four events → one event per quartile. Rate is hits / events in that bucket and can exceed 1.0 when one event matches two forbids.

**Why.** The hire-visible line ends `slope=2.000`. DECAY does not mean the slope rose. `required_missing` is also exit 2 with `slope=0.000` because every event misses the required pattern at the same rate.

**Worked example** (this repo). Audit decaying, then the constant-miss DECAY, then CLEAN.

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# --report: | 0.00 | 0.00 | 1.00 | 2.00 |  and  Decay slope (Q4-Q1 rate): 2.000
# event 2 is Q3 (lint=FAIL); event 3 is Q4 (lint=FAIL + force-push) → 2.00 − 0.00

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl
# same line: slope=2.000 — format is a parser choice

constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md
# verdict=DECAY exit=2 violations=4 first_index=0 slope=0.000
# quartile row 1.00 | 1.00 | 1.00 | 1.00 → Q4 − Q1 = 0

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000
```

**Recall probe.** Why is decaying `slope=2.000` while `required_missing` is DECAY with `slope=0.000`?

Answer: Slope = Q4−Q1. Decaying piles two hits into the last event (Q4=2.00, Q1=0.00). `required_missing` omits `lint=PASS` on every event (Q4=Q1=1.00). CLEAN is also `slope=0.000`; read `verdict=` first. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying` · `examples/jsonl_decaying` · `examples/required_missing` · `examples/stable` · `src/constraintauditor/decay.py`
