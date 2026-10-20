# Daily learning — 2026-10-20

**Skill.** `--json` replaces the stdout hire line. Same three numbers, different keys: `decay.n_violations`, `decay.first_violation_index`, `decay.decay_slope`.

**Why.** Monday: the greppable string. Tuesday: the object a gate parses. Stdout `violations=` is the count; JSON `violations` is the hit list. CLEAN stdout prints `first_index=None`; JSON prints `null`. `--report` can ride along. ERROR still writes no object.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# verdict DECAY, exit_code 2, spec_name decaying-agent
# decay.n_violations 3, first_violation_index 2, decay_slope 2.0  (stdout was slope=2.000)

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --json
# same three decay keys; spec_name jsonl-decaying-agent

constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md --json
# CLEAN: n_violations 0, first_violation_index null, violations []

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md --json
# DECAY, n_violations 4, first_violation_index 0, decay_slope 0.0  — slope 0 is not CLEAN

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md --json
# ERROR: transcript contains no parseable events  — no JSON object, exit 1
```

**Recall probe.** Map stdout `violations=3 first_index=None` to JSON keys. Does `--json` still print the hire line?

Answer: `decay.n_violations == 3`. CLEAN `first_violation_index` is JSON `null`, not `"None"`. No — `--json` replaces the hire line. ERROR has no object. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/cli.py` · `src/constraintauditor/audit.py` (`to_jsonable`) · `examples/decaying/` · `examples/MATRIX.md`
