# Daily learning — 2026-10-30

**Skill.** Exit 2 is what a decay gate fails on. This repo's Actions job does not run `audit` as a step; pytest `test_examples_matrix_live_exits_match_table` re-runs the nine audits and locks `0/2/0/2/1/1/0/2/1`. `loop-engine --gate` binds `return result.exit_code`. Grepping the hire line, reading `--json`, or opening `--report` is not the gate.

**Why.** Thursday: process exit is the decision. Friday: who consumes it. INTERVIEW Q3 — exit 2 is measurable constraint decay. `check-constraints` / `parse-transcript` on decaying stay exit 0 and would pass a naive "command succeeded" gate.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# exit 2 — --gate / a decay CI step fail here

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# DECAY exit=2 slope=0.000 — slope 0 is still a fail

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# ERROR exit 1 — fail-closed, not a free CLEAN

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints) — exit 0, compile only

constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events — exit 0, not an audit

python -m pytest tests/test_examples.py::test_examples_matrix_live_exits_match_table -q
# this repo's CI lock of 0/2/0/2/1/1/0/2/1
```

**Recall probe.** If `--gate` wraps `check-constraints` on decaying, does the tick fail? Does `.github/workflows/ci.yml` invoke `constraint-auditor audit`?

Answer: No and no. check-constraints is exit 0 (regex compile). Actions here is ruff + pytest; the live MATRIX test is the lock. Empty stays 1. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `.github/workflows/ci.yml` · `tests/test_examples.py` (`test_examples_matrix_live_exits_match_table`) · `src/constraintauditor/cli.py` (`return result.exit_code`) · `docs/INTERVIEW.md` (exit 2 in CI) · README (`loop-engine --gate`) · `examples/MATRIX.md`
