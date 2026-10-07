# Daily learning — 2026-10-07

**Skill.** `first_index` is the earliest violating event, not the last hit and not `violations`. Decaying journals go clean, clean, lint-FAIL, then lint-FAIL plus force-push. First hit is event 2.

**Why.** The hire-visible line is `verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000`. `violations` counts constraint matches. `first_index` marks when decay started. `slope` reads the quartile table. Those three numbers answer different questions.

**Worked example** (this repo). Replay decaying, then read the report sentence and the JSON key. Contrast stable so you do not treat `None` as zero.

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# --report: "first at event 2" · First violation index: 2

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --json
# decay.first_violation_index == 2  (same index; JSON key, not the stdout label)

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl
# same line: first_index=2

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000
```

**Recall probe.** Why is decaying `first_index=2` and not `3` or `0`?

Answer: Events 0 and 1 are clean. Event 2 is the first `lint=FAIL` (`never_skip_lint`). Event 3 adds a second forbid hit; that does not move the index. CLEAN prints `None`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying` · `examples/jsonl_decaying` · `examples/stable` · `src/constraintauditor/decay.py` · README first-screen line
