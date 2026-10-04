# Daily learning — 2026-10-04

**Skill.** `check-constraints` compiles the YAML. It does not read a journal. `OK: decaying-agent (2 constraints)` is exit 0 because the regexes compile, not because the agent stayed clean.

**Why.** The hire-visible lock is fail-closed spec load. A `(` pattern is SpecError exit 1 before any event is scored. A valid spec still needs `audit` for CLEAN or DECAY.

**Worked example** (this repo). Compile three bundled specs, then audit decaying so you do not treat `OK:` as CLEAN.

```bash
constraint-auditor check-constraints examples/stable/constraints.yaml
# OK: stable-agent (2 constraints)

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints)

constraint-auditor check-constraints examples/required_missing/constraints.yaml
# OK: required-missing-agent (1 constraints)

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
```

**Recall probe.** What does `check-constraints examples/decaying/constraints.yaml` print, and is that CLEAN?

Answer: `OK: decaying-agent (2 constraints)` exit 0. Spec compiled. Same fixture still audits DECAY exit 2. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/stable` · `examples/decaying` · `examples/required_missing` · `src/constraintauditor/cli.py` · `docs/ADAPTER.md` Verify
