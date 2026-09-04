# LOOP_STATE - agent-constraint-auditor (LIVE Week focus 2026-08-31)

> Public: https://github.com/homayoun-safarpour/agent-constraint-auditor  
> Local: `D:\ship\agent-constraint-auditor`

## BENCHMARK GATE

Week: opened Mon 2026-08-31 · repo: agent-constraint-auditor

### A. Our benchmarks (always)

| # | Check | Status 2026-08-31 |
| --- | --- | --- |
| 1 | CI green 3.10 / 3.11 / 3.12 | PASS — Actions success on `df3882e` (2026-09-04); first public green `0a916b2` |
| 2 | Named claim tests | PASS — `pytest` 32 passed (2026-09-04) |
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
- [x] W12 Fail-closed empty / headerless transcript (exit 1, not CLEAN) (2026-09-03)
- [x] W13 Compile constraint regex at spec load (invalid pattern exit 1) (2026-09-03)
- [x] W14 Named `--report` lock for `examples/required_missing` (2026-09-04)
- [x] W15 Named `--report` lock for `examples/required_present` (2026-09-04)
- [ ] W16 Document `examples/required_present` and `examples/required_missing` in `examples/README.md`

## Build log

- 2026-08-31: Local gate re-run green; public create + Homayoun push; benchmark paste under `examples/`.
- 2026-08-31 evening: README live URL; `docs/ADAPTER.md` for loop-engine journal wiring; mind-learn card in live_memory.
- 2026-09-01: `--report` opens with third-person `Verdict: CLEAN|DECAY`; named test locks decaying fixture `git push --force` line and constraint ids.
- 2026-09-02: named tests lock `forbid: false` (required pattern missing) as DECAY; YAML `forbid: false` parses and audits to exit 2.
- 2026-09-02 evening: `examples/required_present` (exit 0) + `examples/required_missing` (exit 2); README Quickstart updated.
- 2026-09-02 freedom pass: `docs/ADAPTER.md` documents forbid vs required pair with verify commands.
- 2026-09-03: empty or headerless journal is ERROR exit 1 (fail-closed); not CLEAN.
- 2026-09-03: uncompilable constraint `pattern` is SpecError at load (`audit` / `check-constraints` exit 1).
- 2026-09-04: named `--report` lock for `examples/required_missing` (Verdict: DECAY, `require_lint_pass`, required-pattern-missing, first event 0).
- 2026-09-04: named `--report` lock for `examples/required_present` (Verdict: CLEAN, holds-all-constraints across 4 events).
- 2026-09-04 evening nudge: gates green on `8698359`; NEXT TICK W16 document required fixtures in `examples/README.md`. Third-person: SHIP

## NEXT TICK (heartbeat 2026-09-04)

- Execute W16: document `examples/required_present` and `examples/required_missing` in `examples/README.md` (exit 0 / 2)
- Why next: W15 froze the `forbid: false` CLEAN report; the examples index still lists only the `forbid: true` pair, so a fork following `examples/README.md` never sees required-pattern polarity
- Verify: `python -m pytest -q` and confirm `examples/README.md` names `required_present` (exit 0) and `required_missing` (exit 2)

## Journal

- 2026-09-04 heartbeat: OK (W15 matches `df3882e`; named `--report` CLEAN lock; CI green). ENRICH. Next tick: W16 document required fixtures in `examples/README.md`.
- 2026-09-04 evening: OK (W16 queued; CI green on `8698359`). SHIP. Next tick: document required fixtures in `examples/README.md`.

## NEXT TICK (evening 2026-09-04)

- Execute W16: document `examples/required_present` and `examples/required_missing` in `examples/README.md` (exit 0 / 2)
- Why next: W15 froze the `forbid: false` CLEAN report; the examples index still lists only the `forbid: true` pair, so a fork following `examples/README.md` never sees required-pattern polarity
- Verify: `python -m pytest -q` and confirm `examples/README.md` names `required_present` (exit 0) and `required_missing` (exit 2)
- Third-person: SHIP
