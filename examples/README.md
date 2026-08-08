# Examples

| Path | Expect |
| --- | --- |
| [stable/](stable/) | `constraint-auditor audit` exits **0** (CLEAN) |
| [decaying/](decaying/) | same command exits **2** (DECAY) + optional `--report` |

```bash
pip install -e ".[dev]"
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
```

Reliability limits: [../docs/RELIABILITY_CARD.md](../docs/RELIABILITY_CARD.md).
