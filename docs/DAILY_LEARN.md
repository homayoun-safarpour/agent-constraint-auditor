# Daily learning — 2026-10-19

**Skill.** The stdout hire line is one string: `verdict=` `exit=` `violations=` `first_index=` `slope=`. Not `--json`. Not `--report`.

**Why.** Last week: join keys on each hit (`detail`, `timestamp`, `constraint_id`, `event_index`, `spec_name`). Monday retarget: the line a reviewer greps. `--json` and `--report` reprint the same three numbers, split. `required_missing` is also DECAY with `slope=0.000` — read `verdict=` first. ERROR writes no hire line.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl
# same hire line (JSONL decaying)

constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# verdict=DECAY exit=2 violations=4 first_index=0 slope=0.000  — slope 0 is not CLEAN

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# ERROR: transcript contains no parseable events  — no hire line, exit 1
```

**Recall probe.** Recite the decaying stdout hire line. What does CLEAN print for `first_index`? Does `required_missing` `slope=0.000` mean CLEAN?

Answer: `verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000`. CLEAN is `first_index=None`. No — `required_missing` is DECAY (`violations=4 first_index=0`). ERROR has no hire line. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/cli.py` · `examples/decaying/` · `examples/required_missing/` · `examples/MATRIX.md`
