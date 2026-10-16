# Daily learning — 2026-10-16

**Skill.** `constraint_id` is the YAML `id`, copied onto the hit. Not the description. Not a journal quote.

**Why.** Thursday: `timestamp` joins the hit to the heading. Friday: `constraint_id` joins the hit to the spec. Event 3 can fire two rules → two rows, two IDs. `check-constraints` saying `2 constraints` is a compile count, not those IDs.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# exit 2
# [0] event 2  constraint_id=never_skip_lint
# [1] event 3  constraint_id=never_skip_lint
# [2] event 3  constraint_id=no_force_push
# JSONL decaying reprints the same three ids (spec_name=jsonl-decaying-agent)

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
# - [2026-08-11 12:00] event 3 · `never_skip_lint` · ...
# - [2026-08-11 12:00] event 3 · `no_force_push` · ...

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints)  — compile only; exit 0
```

**Recall probe.** Recite decaying `violations[0].constraint_id` vs `[2].constraint_id`. Both event-3 rows share timestamp `12:00` but not the same id.

Answer: `never_skip_lint` vs `no_force_push`. CLEAN `violations=[]` so there is no id to recite. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/checkers.py` · `src/constraintauditor/spec.py` · `examples/decaying/constraints.yaml` · `examples/jsonl_decaying/`
