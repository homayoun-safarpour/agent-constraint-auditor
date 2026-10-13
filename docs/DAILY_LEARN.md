# Daily learning — 2026-10-13

**Skill.** `--json` `violations` is the hit list. Stdout `violations=3` is the count. Tuesday after Monday's freeze keys: do not treat the array as three numbers.

**Why.** A gate that sums unique `constraint_id`s undercounts decaying. `decay.n_violations` is `len(violations)`, not distinct rules. Two forbid IDs, three hits: event 2 then event 3.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# exit 2  verdict=DECAY  spec_name=decaying-agent
# decay.n_violations=3  (same as len(violations); stdout still prints violations=3)
# violations[0]: constraint_id=never_skip_lint  event_index=2  timestamp=2026-08-11 11:00
# violations[1]: constraint_id=never_skip_lint  event_index=3  timestamp=2026-08-11 12:00
# violations[2]: constraint_id=no_force_push    event_index=3  timestamp=2026-08-11 12:00
# each object: constraint_id, event_index, timestamp, detail

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl --json
# same three hits; spec_name=jsonl-decaying-agent

constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md --json
# verdict=CLEAN exit=0  violations=[]  decay.n_violations=0
```

**Recall probe.** How many unique constraint IDs vs how many `violations[]` rows on decaying? Name the four keys on one row.

Answer: 2 IDs (`never_skip_lint`, `no_force_push`), 3 rows. Keys: `constraint_id`, `event_index`, `timestamp`, `detail`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/checkers.py` · `src/constraintauditor/audit.py` · `examples/decaying/`
