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
# exit 0 = CLEAN, exit 2 = DECAY (safe for CI / loop-engine gates)
```

## What this does not do

- Does not call a model to “judge” the agent
- Does not invent constraints — you declare them in YAML

## Verify

```bash
pip install -e ".[dev]"
python -m pytest -q
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
```
