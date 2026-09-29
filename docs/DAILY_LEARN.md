# Daily learning — 2026-09-29

**Skill.** `violations` counts constraint hits, not events. Two forbid rules can fire on one turn. Decaying reprints `violations=3` because event 2 hits `never_skip_lint` and event 3 hits that rule plus `no_force_push`.

**Why.** The hire-visible lock is a list of matches, not a vibe that later events look worse. Exit 2 is those three hits. `check-constraints` only compiles YAML. `parse-transcript` only counts events.

**Worked example** (this repo). Spec has two rules. Journal has four dated events. `--json` names each hit.

```bash
constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints)

constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events — parser does not score decay

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --json
# verdict DECAY exit 2
# hits: event 2 never_skip_lint; event 3 never_skip_lint + no_force_push
```

**Recall probe.** Why does decaying print `violations=3` when only two events look late?

Answer: Event 2 matches `lint=FAIL` (1). Event 3 matches `lint=FAIL` and force-push (2). Total 3. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying/` · `src/constraintauditor/checkers.py` · `constraint-auditor check-constraints` · README Exit codes
