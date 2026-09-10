# Example exit matrix (Sunday prep)

Run from repo root after `pip install -e ".[dev]"`.

| Fixture | Command focus | Expect |
| --- | --- | --- |
| `stable/` | journal audit | **0** CLEAN |
| `decaying/` | journal audit (+ `--report`) | **2** DECAY |
| `required_present/` | `forbid: false` | **0** CLEAN |
| `required_missing/` | `forbid: false` | **2** DECAY |
| `empty/` | fail-closed | **1** ERROR |
| `headerless/` | fail-closed | **1** ERROR |
| `jsonl_stable/` | `--format jsonl` | **0** CLEAN |
| `jsonl_decaying/` | `--format jsonl` (+ `--report`) | **2** DECAY |

```bash
python -m pytest -q
python -m ruff check .
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md
constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
constraint-auditor audit --constraints examples/headerless/constraints.yaml --transcript examples/headerless/journal.md
constraint-auditor audit --constraints examples/jsonl_stable/constraints.yaml --transcript examples/jsonl_stable/events.jsonl --format jsonl
constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl --report /tmp/jsonl-decay.md
```

Named pytest locks keep README / ADAPTER / INTERVIEW claims honest. Full Sunday gate: `LOOP_STATE.md` → `## BENCHMARK GATE` + `WEEKLY_BUILD_BENCHMARK_RULE.md`.
