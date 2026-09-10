# Examples

| Path | Expect |
| --- | --- |
| [stable/](stable/) | `forbid: true`; `constraint-auditor audit` exits **0** (CLEAN) |
| [decaying/](decaying/) | `forbid: true`; same command exits **2** (DECAY) + optional `--report` |
| [required_present/](required_present/) | `forbid: false`; required pattern present; exits **0** (CLEAN) |
| [required_missing/](required_missing/) | `forbid: false`; required pattern missing; exits **2** (DECAY) |
| [empty/](empty/) | empty transcript; exits **1** (ERROR, not CLEAN) |
| [headerless/](headerless/) | no dated `##` events; exits **1** (ERROR, not CLEAN) |
| [jsonl_stable/](jsonl_stable/) | `--format jsonl`; `events.jsonl` + same forbid rules; exits **0** (CLEAN) |
| [jsonl_decaying/](jsonl_decaying/) | `--format jsonl`; forbid match (`lint=FAIL` / force-push); exits **2** (DECAY) |

```bash
pip install -e ".[dev]"
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md --report /tmp/required-clean.md
constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md --report /tmp/required-decay.md
constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
constraint-auditor audit --constraints examples/headerless/constraints.yaml --transcript examples/headerless/journal.md
constraint-auditor parse-transcript --format jsonl examples/jsonl_stable/events.jsonl
constraint-auditor audit --constraints examples/jsonl_stable/constraints.yaml --transcript examples/jsonl_stable/events.jsonl --format jsonl
constraint-auditor parse-transcript --format jsonl examples/jsonl_decaying/events.jsonl
constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl --report /tmp/jsonl-decay.md
```

`forbid: true` (default) treats a match as decay. `forbid: false` treats a missing required pattern as decay.

Reliability limits: [../docs/RELIABILITY_CARD.md](../docs/RELIABILITY_CARD.md).
