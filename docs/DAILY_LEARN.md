# Daily learning — 2026-10-29

**Skill.** Process exit is the gate. The hire line, `--json` `exit_code`, and `--report` Verdict describe the same decision; CI and `loop-engine --gate` bind `return result.exit_code` (0 CLEAN, 2 DECAY, 1 ERROR). `--json` and `--report` do not change it.

**Why.** Monday locked MATRIX `0/2/0/2/1/1/0/2/1`. Tuesday: the object. Wednesday: the file. Thursday: a passing `check-constraints` or `parse-transcript` is not an audit. INTERVIEW Q3 — exit 2 is measurable constraint decay.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# exit 0

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# stdout is JSON (no hire line); process exit still 2

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# DECAY exit=2 slope=0.000 — slope 0 is not CLEAN

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# ERROR exit 1 — no hire line, no JSON object

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints) — exit 0, compile only

constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events — exit 0, not an audit
```

**Recall probe.** Does `check-constraints` on decaying fail CI the same way `audit` does? After `--json` on decaying, is the process still exit 2?

Answer: No — check-constraints is exit 0 (regex compile). `--json` only replaces stdout; `return result.exit_code` is still 2. Empty stays 1. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/cli.py` (`return result.exit_code`) · `src/constraintauditor/audit.py` · `examples/MATRIX.md` · `docs/INTERVIEW.md` (exit 2 in CI)
