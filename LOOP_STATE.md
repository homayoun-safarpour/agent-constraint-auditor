# LOOP_STATE - agent-constraint-auditor (LIVE Week focus 2026-08-31)

> Public: https://github.com/homayoun-safarpour/agent-constraint-auditor  
> Local: `D:\ship\agent-constraint-auditor`

## BENCHMARK GATE

Week: opened Mon 2026-08-31 · repo: agent-constraint-auditor

### A. Our benchmarks (always)

| # | Check | Status 2026-08-31 |
| --- | --- | --- |
| 1 | CI green 3.10 / 3.11 / 3.12 | PASS — Actions success on `0a916b2` (2026-08-31) |
| 2 | Named claim tests | PASS — `pytest` 16 passed |
| 3 | Worked example real output | PASS — stable exit 0; decaying exit 2 (see `examples/benchmark_gate_2026-08-31.md`) |
| 4 | Fork/implement under 30 min | PASS — README Quickstart |
| 5 | `public_git_guard.py` PASS | PASS (Homayoun) |
| 6 | AI-tell README ban | PASS on publish commit |
| 7 | `docs/INTERVIEW.md` | Present |

### B. Field benchmark

N/A for v0.1.

## Name field-check

PASS - log: `D:\live_memory\logs\runtime\name_field_check_agent-constraint-auditor.md`

## Backlog

- [x] W1 Constraint spec format (YAML) + transcript/journal parser (local 2026-08-08)
- [x] W2 Deterministic checkers: regex rules per transcript event (local 2026-08-08)
- [x] W3 Decay metrics: quartile rates, first-violation index, decay slope (local 2026-08-08)
- [x] W4 `audit` CLI with verdict + exit codes 0/2/1 (local 2026-08-08)
- [x] W5 Native adapter for agent-loop-engine journals (local 2026-08-08)
- [x] W6 Markdown decay report `--report` (local 2026-08-08)
- [x] W7 GitHub Actions on public repo (2026-08-31 publish)
- [x] W8 Two worked examples stable vs decaying (local 2026-08-08)

## Build log

- 2026-08-31: Local gate re-run green; public create + Homayoun push; benchmark paste under `examples/`.

## NEXT TICK

- Confirm CI green on first Actions run
- Boss: retarget Cursor Autos 1–6 to this repo @ `main`
- Profile table row + growth pulse if not done in this tick
