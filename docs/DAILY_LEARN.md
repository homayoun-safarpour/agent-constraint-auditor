# Daily learning — 2026-09-13

**Skill.** Sunday usefulness gate is a replayable eight-exit claim: `0/2/0/2/1/1/0/2`. `run_audit` returns only CLEAN `0` or DECAY `2`. Exit `1` is never an `AuditResult` — the CLI maps `SpecError` / `TranscriptError` / `OSError` / missing path to ERROR.

**Why.** Hire signal: a reviewer forks, runs `examples/MATRIX.md`, and gets those exits. Named tests lock the table *and* the live audits. No employer-demand claim — a deterministic gate over this repo's fixtures.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# verdict=CLEAN exit=0
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# verdict=DECAY exit=2
constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# ERROR: transcript contains no parseable events  →  process exit 1
```

`run_audit` (`src/constraintauditor/audit.py`): successful parse, then `violations` → DECAY/2 else CLEAN/0. Empty `examples/empty/journal.md` raises `TranscriptError` before that dataclass is built. `test_examples_matrix_live_exits_match_table` re-runs all eight.

**Recall probe.** Does `run_audit("examples/empty/constraints.yaml", "examples/empty/journal.md")` return `AuditResult(verdict="ERROR", exit_code=1)`?

Answer: No. It raises `TranscriptError`. Only `main(["audit", ...])` returns `1`. MATRIX `empty/` **1** ERROR is the CLI contract, not an AuditResult variant.

**Retrieve.** `examples/MATRIX.md` · `src/constraintauditor/audit.py` · `cli.py` · `tests/test_examples.py` (`MATRIX_EXIT_ROWS`) · `LOOP_STATE.md` W44
