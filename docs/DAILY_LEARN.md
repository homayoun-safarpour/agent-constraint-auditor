# Daily learning — 2026-10-17

**Skill.** `event_index` is the 0-based event ordinal, copied onto the hit. Not `first_index`. Not the clock.

**Why.** Thursday: `timestamp` joins the heading. Friday: `constraint_id` joins the spec. Saturday: `event_index` joins the parsed event list. `first_index` is `min(event_index)` — one number, not the row list. Event 3 can fire two rules → two rows, same index.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# exit 2
# [0] event_index=2  (11:00, never_skip_lint)
# [1] event_index=3  (12:00, never_skip_lint)
# [2] event_index=3  (12:00, no_force_push)
# first_index=2 is min of those three. JSONL decaying reprints the same three indexes.

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
# - [2026-08-11 11:00] event 2 · `never_skip_lint` · ...
# - [2026-08-11 12:00] event 3 · `never_skip_lint` · ...
# - [2026-08-11 12:00] event 3 · `no_force_push` · ...

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints)  — compile only; no event_index
```

**Recall probe.** Recite decaying `violations[0].event_index` vs `[2].event_index`, then `first_index`.

Answer: `2` vs `3`. `first_index=2` (the min). Both event-3 rows share index `3` but not the same id. CLEAN `violations=[]` so `first_violation_index` is `null`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/checkers.py` · `src/constraintauditor/decay.py` · `examples/decaying/journal.md` · `examples/jsonl_decaying/`
