# agent-constraint-auditor

**Your agent stopped following its own rules and nobody noticed.** Long-horizon codegen and agent loops drop declared constraints while still looking productive; this CLI audits the transcript against your constraint spec and reports which rules decayed, when, and how fast.

![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Public: https://github.com/homayoun-safarpour/agent-constraint-auditor  
Reliability limits: [docs/RELIABILITY_CARD.md](docs/RELIABILITY_CARD.md). Interview pack: [docs/INTERVIEW.md](docs/INTERVIEW.md). Adapter notes: [docs/ADAPTER.md](docs/ADAPTER.md).

## Use this when

| Situation | Use this? |
| --- | --- |
| You declare agent rules and want a deterministic decay gate | Yes |
| You need exit `0` / `2` for agent-loop-engine or CI | Yes |
| You want an LLM judge of agent quality | No - this is regex/predicate over your declared spec |
| You want a mega agent-eval platform | No |

## Quickstart

```bash
cd agent-constraint-auditor
pip install -e ".[dev]"
constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# expect exit 0

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# expect exit 2; report starts with Verdict: DECAY
```

## Constraint spec

Each YAML rule is a regex over a journal event. `forbid: true` (default) treats a match as decay. `forbid: false` treats a missing required pattern as decay (exit `2`).

## Exit codes

| Code | Verdict | Meaning |
| --- | --- | --- |
| `0` | CLEAN | No constraint decay |
| `2` | DECAY | One or more constraints violated |
| `1` | ERROR | Bad args / missing files / invalid spec |

Wire into [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine):

```bash
loop-engine tick --state LOOP_STATE.md \
  --gate "constraints=constraint-auditor audit --constraints constraints/agent.yaml --transcript journal/JOURNAL.md"
```

## Related instruments

- [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine) - state, gates, decide, journal
- [judge-drift-sentinel](https://github.com/homayoun-safarpour/judge-drift-sentinel) - judge vs system drift
- [trace-gate](https://github.com/homayoun-safarpour/trace-gate) - trajectory deploy gate

## Author

Homayoun Safarpour - [LinkedIn](https://www.linkedin.com/in/homayoun-safarpour/)

## License

MIT
