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
| ERROR (fail-closed) | n/a | No parseable dated events | `examples/empty` (exit 1) · `examples/headerless` (exit 1) |
| JSONL CLEAN | `--format jsonl` | One JSON object per line; no forbid match | `examples/jsonl_stable` (exit 0) |
| JSONL DECAY | `--format jsonl` | Forbid-match decay on JSONL events | `examples/jsonl_decaying` (exit 2) |

```bash
# Required pattern present → CLEAN
constraint-auditor audit \
  --constraints examples/required_present/constraints.yaml \
  --transcript examples/required_present/journal.md

# Required pattern missing → DECAY
constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md

# Empty or headerless transcript → ERROR (not CLEAN)
constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
constraint-auditor audit \
  --constraints examples/headerless/constraints.yaml \
  --transcript examples/headerless/journal.md

# JSONL transcripts (same exit contract as markdown journals)
constraint-auditor parse-transcript --format jsonl examples/jsonl_stable/events.jsonl
constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format jsonl
# expect exit 0 CLEAN

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl \
  --report /tmp/jsonl-decay.md
# expect exit 2 DECAY; report opens with Verdict: DECAY
```

Use forbid rules for "never do X". Use required rules for "every event must still show Y" (for example `lint=PASS`). Empty or headerless journals must fail closed as exit `1`, never a free CLEAN. JSONL fixtures under `examples/jsonl_stable` and `examples/jsonl_decaying` lock the same polarities for `--format jsonl`. A JSONL object with `timestamp` but neither `text` nor `fields` is ERROR (exit `1`), not CLEAN.

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
constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# expect exit 1
constraint-auditor audit --constraints examples/jsonl_stable/constraints.yaml --transcript examples/jsonl_stable/events.jsonl --format jsonl
# expect exit 0
constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl
# expect exit 2
```
