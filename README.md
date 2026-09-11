# agent-constraint-auditor

**Your agent stopped following its own rules and nobody noticed.** Long-horizon codegen and agent loops drop declared constraints while still looking productive; this CLI audits the transcript against your constraint spec and reports which rules decayed, when, and how fast.

![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/homayoun-safarpour/agent-constraint-auditor/actions/workflows/ci.yml/badge.svg)

Public: https://github.com/homayoun-safarpour/agent-constraint-auditor  
Reliability limits: [docs/RELIABILITY_CARD.md](docs/RELIABILITY_CARD.md). Interview pack: [docs/INTERVIEW.md](docs/INTERVIEW.md). Adapter notes: [docs/ADAPTER.md](docs/ADAPTER.md). Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). Security: [SECURITY.md](SECURITY.md). Discussions: https://github.com/homayoun-safarpour/agent-constraint-auditor/discussions

## Use this when

| Situation | Use this? |
| --- | --- |
| You declare agent rules and want a deterministic decay gate | Yes |
| You need exit `0` / `2` for agent-loop-engine or CI | Yes |
| You want an LLM judge of agent quality | No - this is regex/predicate over your declared spec |
| You want a mega agent-eval platform | No |

## Quickstart

Full fixture exit matrix (Sunday prep): [examples/MATRIX.md](examples/MATRIX.md).


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

constraint-auditor audit \
  --constraints examples/required_present/constraints.yaml \
  --transcript examples/required_present/journal.md \
  --report /tmp/required-clean.md
# expect exit 0; report starts with Verdict: CLEAN

constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md \
  --report /tmp/required-decay.md
# expect exit 2; report starts with Verdict: DECAY and required pattern missing

constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
# expect exit 1; empty transcript is ERROR, not CLEAN

constraint-auditor audit \
  --constraints examples/headerless/constraints.yaml \
  --transcript examples/headerless/journal.md
# expect exit 1; headerless transcript is ERROR, not CLEAN

constraint-auditor parse-transcript --format jsonl examples/jsonl_stable/events.jsonl
# expect OK: 4 events

constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format jsonl \
  --report /tmp/jsonl-clean.md
# expect exit 0; report starts with Verdict: CLEAN

constraint-auditor parse-transcript --format jsonl examples/jsonl_decaying/events.jsonl
# expect OK: 4 events

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl \
  --report /tmp/jsonl-decay.md
# expect exit 2 (DECAY); report starts with Verdict: DECAY
```

## Constraint spec

Each YAML rule is a regex over a journal event. `forbid: true` (default) treats a match as decay. `forbid: false` treats a missing required pattern as decay (exit `2`). Invalid regex is a spec error (exit `1`).

`--format jsonl` (or auto-detect when the first non-empty line starts with `{`) reads one JSON object per line. Each object needs `timestamp` plus `text` and/or `fields`. A timestamp-only line is ERROR (exit `1`). Invalid or empty JSONL is ERROR (exit `1`). `audit` and `parse-transcript` both accept `--format jsonl|journal|auto`.

## Exit codes

| Code | Verdict | Meaning |
| --- | --- | --- |
| `0` | CLEAN | No constraint decay |
| `2` | DECAY | One or more constraints violated |
| `1` | ERROR | Bad args / missing files / invalid spec / invalid regex / empty or headerless transcript / invalid or empty JSONL / JSONL object missing text and fields |

`parse-transcript PATH [--format jsonl|journal|auto]` dry-runs the parser. Empty or headerless input exits `1` (ERROR), not `OK: 0 events`.

`constraint-auditor --version` prints the package version (`0.1.0`). See [CONTRIBUTING.md](CONTRIBUTING.md) for the local loop.

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
