# Reliability card

| Field | Value |
| --- | --- |
| **Job** | Detect declared-constraint decay in agent transcripts/journals |
| **Primary signal** | `constraint-auditor audit` exit `0` (CLEAN) / `2` (DECAY) / `1` (ERROR) |
| **Claim** | Given a YAML constraint spec and a loop-engine journal **or** JSONL transcript (`--format jsonl`), violations are detected deterministically and quartile decay metrics are reported |
| **Not claimed** | LLM-as-judge of agent quality; inference of hidden policies without a spec; DRIFT-Bench reproduction |

## Field alignment

Constraint decay in long-horizon agents is a known ops pain. This instrument is the agent-behavior sibling of judge-drift-sentinel: narrow CLI, fail-closed exits, fixtures under `examples/` (markdown journals plus `jsonl_stable` / `jsonl_decaying` / `jsonl_bad_timestamp`). A JSONL `timestamp` that is not `YYYY-MM-DD HH:MM` is ERROR exit `1`, never CLEAN; `examples/jsonl_bad_timestamp` is the worked fixture. A JSONL line that is valid JSON but not an object, or a `fields` value that is not a mapping, is the same ERROR.
