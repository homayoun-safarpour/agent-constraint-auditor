# Daily learning — 2026-10-28

**Skill.** `--json` and `--report` are independent surfaces of one audit. `cli.py` writes the markdown file first, then replaces the stdout hire line with JSON. Process exit is last (`return result.exit_code`). ERROR never reaches either write.

**Why.** Monday locked MATRIX `0/2/0/2/1/1/0/2/1`. Tuesday: the parseable object. Wednesday: a gate can parse JSON while a human reads the report. Same three numbers. Report slope is `2.000`; JSON `decay_slope` is `2.0`. CLEAN report prints `None`; JSON prints `null`.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json --report /tmp/decay.md
# stdout JSON only (no hire line). File: # Constraint decay report: decaying-agent
# Verdict: DECAY — 3 violations, first at event 2, slope 2.000
# JSON: decay.n_violations 3, first_violation_index 2, decay_slope 2.0

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --json --report /tmp/jsonl-decay.md
# same three numbers; report title uses spec_name jsonl-decaying-agent

constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md --json --report /tmp/stable.md
# CLEAN: JSON first_violation_index null; report prints None

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md --json --report /tmp/req.md
# DECAY 4 / 0 / 0.0 — report "first at event 0"; slope 0 is not CLEAN

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md --json --report /tmp/empty.md
# ERROR: no JSON object, no file, exit 1
```

**Recall probe.** On decaying `--json --report /tmp/out.md`, is slope in stdout `2.000` or `2.0`? Does `/tmp/empty.md` exist after the empty fixture?

Answer: JSON `decay_slope` is `2.0`; the report file prints `2.000`. Empty ERROR never calls `write_report`, so the path is missing. Process exit stays 2 / 0 / 1. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/cli.py` · `src/constraintauditor/audit.py` (`write_report`, `to_jsonable`) · `src/constraintauditor/decay.py` (`markdown_timeline`) · `examples/decaying/` · `examples/MATRIX.md`
