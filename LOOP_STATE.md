# LOOP_STATE - agent-constraint-auditor (LIVE Week focus 2026-08-31)

> Public: https://github.com/homayoun-safarpour/agent-constraint-auditor  
> Local: `D:\ship\agent-constraint-auditor`

## BENCHMARK GATE

Week: opened Mon 2026-08-31 · repo: agent-constraint-auditor

### A. Our benchmarks (always)

| # | Check | Status 2026-08-31 |
| --- | --- | --- |
| 1 | CI green 3.10 / 3.11 / 3.12 | PASS — Actions success on `0a916b2` (2026-08-31) |
| 2 | Named claim tests | PASS — `pytest` (see latest local/CI) |
| 3 | Worked example real output | PASS — stable/decaying + required_present/missing |
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
- [x] W9 Named decaying-fixture lock + third-person `--report` verdict (2026-09-01)
- [x] W10 Named `forbid: false` required-pattern-missing lock (2026-09-02)
- [x] W11 Worked `forbid: false` fixtures under `examples/required_*` (2026-09-02)

## Build log

- 2026-08-31: Local gate re-run green; public create + Homayoun push; benchmark paste under `examples/`.
- 2026-08-31 evening: README live URL; `docs/ADAPTER.md` for loop-engine journal wiring; mind-learn card in live_memory.
- 2026-09-01: `--report` opens with third-person `Verdict: CLEAN|DECAY`; named test locks decaying fixture `git push --force` line and constraint ids.
- 2026-09-02: named tests lock `forbid: false` (required pattern missing) as DECAY; YAML `forbid: false` parses and audits to exit 2.
- 2026-09-02 evening: `examples/required_present` (exit 0) + `examples/required_missing` (exit 2); README Quickstart updated.
- 2026-09-02 freedom pass: `docs/ADAPTER.md` documents forbid vs required pair with verify commands.
- 2026-09-02 evening nudge: gates green on `604deac`; NEXT TICK HOLD (ADAPTER verify). Third-person: HOLD

## NEXT TICK (daily 2026-09-02)

- Optional: triage sentinel GFI #9 if a community PR arrives; else keep auditor ADAPTER verify commands green
- Why next: W11 ADAPTER required-pattern pair shipped; week deepen stays interview-defensible
- Verify: `python -m pytest -q` and `constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md`

## NEXT TICK (evening 2026-09-02)

- HOLD: re-confirm ADAPTER required-pattern pair; no new auditor scope
- Why next: W1–W11 closed and CI green on `604deac`; Daily 2026-09-03 must not invent product work
- Verify: `python -m pytest -q` && `constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md` && `constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md`
- Third-person: HOLD
