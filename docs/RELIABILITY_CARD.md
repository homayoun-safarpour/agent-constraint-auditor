# Reliability card

| Field | Value |
| --- | --- |
| **Job** | Detect declared-constraint decay in agent transcripts/journals |
| **Primary signal** | `constraint-auditor audit` exit `0` (CLEAN) / `2` (DECAY) |
| **Claim** | Given a YAML constraint spec and a loop-engine journal, violations are detected deterministically and quartile decay metrics are reported |
| **Not claimed** | LLM-as-judge of agent quality; inference of hidden policies without a spec; DRIFT-Bench reproduction |

## Field alignment

Constraint decay in long-horizon agents is a known ops pain. This instrument is the agent-behavior sibling of judge-drift-sentinel: narrow CLI, fail-closed exits, fixtures under `examples/`.
