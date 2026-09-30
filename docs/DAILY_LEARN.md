# Daily learning — 2026-09-30

**Skill.** `first_index` is 0-based. The decaying journal has four events (09:00, 10:00, 11:00, 12:00). `first_index=2` is the 11:00 turn (`lint=FAIL`, advance anyway), not the 10:00 green event.

**Why.** The public decaying line is `verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000`. Yesterday: `violations` counts hits. Today: `first_index` names the first broken event. Read it as one-based and the story is the wrong hour.

**Worked example** (this repo). Parse the four stamps, then audit. Stable prints `first_index=None`.

```bash
constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events
# 09:00, 10:00, 11:00, 12:00

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000
```

**Recall probe.** Which decaying timestamp is `first_index=2`, and which rule hits first?

Answer: `2026-08-11 11:00`. `never_skip_lint` matches `lint=FAIL`. Event 3 then adds a second lint hit plus `no_force_push`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying/` · `examples/stable/` · `src/constraintauditor/decay.py` · README first screen
