# Adapter notes — agent-loop-engine journals

`constraintauditor.journal.parse_loop_engine_journal` reads the append-only markdown journal shape used by [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine).

## Expected shape

- Headings or bullet blocks that mark turns / decisions / tool events
- Constraint checks run as **predicates over those events**, not as an LLM score

## Gate wiring

```bash
constraint-auditor audit \
  --constraints constraints/agent.yaml \
  --transcript path/to/JOURNAL.md
# exit 0 = CLEAN, exit 2 = DECAY, exit 1 = ERROR (empty journal or invalid regex is not CLEAN)
```

## Forbid vs required patterns

| Mode | YAML | Meaning | Worked example |
| --- | --- | --- | --- |
| Forbid (default) | `forbid: true` | Match = decay | `examples/stable` (exit 0) · `examples/decaying` (exit 2) |
| Required | `forbid: false` | Missing match = decay | `examples/required_present` (exit 0) · `examples/required_missing` (exit 2) |

```bash
# Required pattern present → CLEAN
constraint-auditor audit \
  --constraints examples/required_present/constraints.yaml \
  --transcript examples/required_present/journal.md

# Required pattern missing → DECAY
constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md
```

Use forbid rules for “never do X”. Use required rules for “every event must still show Y” (for example `lint=PASS`).

## What this does not do

- Does not call a model to “judge” the agent
- Does not invent constraints — you declare them in YAML

## Verify

```bash
pip install -e ".[dev]"
python -m pytest -q
constraint-auditor check-constraints examples/stable/constraints.yaml
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md
```
