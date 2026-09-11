# LOOP_STATE - agent-constraint-auditor (LIVE Week focus 2026-09-07)

> Public: https://github.com/homayoun-safarpour/agent-constraint-auditor  
> Local: `D:\ship\agent-constraint-auditor`

## BENCHMARK GATE

Week: opened Mon 2026-09-07 · repo: agent-constraint-auditor

### A. Our benchmarks (always)

| # | Check | Status 2026-09-07 |
| --- | --- | --- |
| 1 | CI green 3.10 / 3.11 / 3.12 | PASS — Actions success on `f166fa2` (2026-09-11, run 34575165277); first public green `0a916b2` |
| 2 | Named claim tests | PASS — `pytest` 67 passed; `ruff check .` clean (2026-09-11) |
| 3 | Worked example real output | PASS — stable/decaying + required_* + empty/headerless + jsonl_stable/jsonl_decaying |
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
- [x] W16 Document `examples/required_present` and `examples/required_missing` in `examples/README.md` (2026-09-05)
- [x] W17 Named test locks `examples/README.md` required-pair rows (exit 0 / 2) (2026-09-05)
- [x] W18 Worked ERROR fixtures under `examples/` for empty and headerless transcripts (exit 1) (2026-09-06)
- [x] W19 Named test locks `examples/README.md` empty/headerless ERROR rows (exit 1) (2026-09-06)
- [x] W20 Document `examples/empty` and `examples/headerless` in `docs/ADAPTER.md` (2026-09-06)
- [x] W21 Named test locks `docs/ADAPTER.md` ERROR fixture rows (exit 1) (2026-09-07)
- [x] W22 Parse `--format jsonl` transcripts (timestamp + text/fields; invalid/empty → exit 1) (2026-09-07)
- [x] W23 `parse-transcript` fail-closed empty / headerless (exit 1, not OK: 0 events) (2026-09-08)
- [x] W24 `parse-transcript --format jsonl|journal|auto` matching `audit` (2026-09-08)
- [x] W25 Worked JSONL fixture under `examples/jsonl_stable` for `--format jsonl` (2026-09-08)
- [x] W26 Named test locks `examples/README.md` jsonl_stable row (exit 0) (2026-09-08)
- [x] W27 Worked JSONL DECAY fixture under `examples/` (forbid match, exit 2) (2026-09-09)
- [x] W28 Named test locks `examples/README.md` jsonl_decaying row (exit 2) (2026-09-09)
- [x] W29 Named `--report` lock for `examples/jsonl_decaying` (Verdict: DECAY) (2026-09-10)
- [x] W30 Named `--report` lock for `examples/jsonl_stable` (Verdict: CLEAN) (2026-09-10)
- [x] W31 Document `--format jsonl` fixtures in `docs/ADAPTER.md` (2026-09-10)
- [x] W32 Named test locks `docs/ADAPTER.md` jsonl_stable / jsonl_decaying rows (2026-09-10)
- [x] W33 Heartbeat quality pass on JSONL Quickstart claims (2026-09-10)
- [x] W34 Interview + reliability card document JSONL demo/claim (2026-09-10)
- [x] W35 Named tests lock INTERVIEW + RELIABILITY_CARD JSONL rows (2026-09-10)
- [x] W36 Prep Sunday: example matrix checklist under `examples/MATRIX.md` (2026-09-10)
- [x] W37 CI tip green on main after matrix merge (run 34492448163) (2026-09-10)
- [x] W38 README Quickstart links `examples/MATRIX.md` (2026-09-10)
- [x] W39 Sat: dry-run full MATRIX commands locally (2026-09-10 — early; all 8 exits match)
- [x] W40 Fri: growth pulse + LinkedIn draft refresh in LOOP_STATE (2026-09-10)
- [x] W41 Close stranded cursor/* draft PRs (2026-09-10)
- [x] W42 BENCHMARK GATE pytest count bumped to 61 (2026-09-10)
- [x] W43 Fri hold: named test locks `examples/MATRIX.md` exit rows (2026-09-11)
- [ ] W44 Sun 2026-09-13 usefulness gate (CI + eight MATRIX exits + claim check)
- [x] W45 Fail-closed JSONL objects missing text and/or fields (exit 1) (2026-09-11)

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
- 2026-09-05: `examples/README.md` lists `required_present` (exit 0) and `required_missing` (exit 2) beside the `forbid: true` pair.
- 2026-09-05: named test locks `examples/README.md` required-pair rows (exit 0 CLEAN / exit 2 DECAY, `forbid: false`).
- 2026-09-06: `examples/empty` and `examples/headerless` audit to ERROR exit 1 (no parseable events); not CLEAN.
- 2026-09-06: named test locks `examples/README.md` empty/headerless ERROR rows (exit 1).
- 2026-09-06 local run: Midday gates green (36 pytest); Sunday close landed on main; W20 ADAPTER ERROR fixtures documented.
- 2026-09-07: week retarget Mon 2026-09-07; named test locks `docs/ADAPTER.md` ERROR rows (`examples/empty` / `examples/headerless`, exit 1).
- 2026-09-07: `--format jsonl` parses one object per line (`timestamp` + `text`/`fields`); invalid or empty JSONL is ERROR.
- 2026-09-08: `parse-transcript` fail-closes empty / headerless journals (exit 1, not `OK: 0 events`).
- 2026-09-08: `parse-transcript --format jsonl|journal|auto` matches `audit`; `--format jsonl` forces JSONL parse when sniffing would not.
- 2026-09-08: `examples/jsonl_stable` worked JSONL fixture (4 events, CLEAN exit 0) + Quickstart commands.
- 2026-09-09: `examples/jsonl_decaying` worked JSONL fixture (forbid match, DECAY exit 2) + Quickstart commands.
- 2026-09-09: named test locks `examples/README.md` jsonl_decaying row (exit 2 DECAY, `--format jsonl`).
- 2026-09-10: named `--report` lock for `examples/jsonl_decaying` (Verdict: DECAY, 3 violations, first event 2).
- 2026-09-10: named `--report` lock for `examples/jsonl_stable` (Verdict: CLEAN, holds-all-constraints across 4 events).
- 2026-09-10: `docs/ADAPTER.md` documents JSONL CLEAN/DECAY fixtures + verify commands; named test locks those rows.
- 2026-09-10: heartbeat W33 green (57 pytest, JSONL matrix 0/2); INTERVIEW + RELIABILITY_CARD JSONL claims + named locks.
- 2026-09-10: `examples/MATRIX.md` Sunday prep exit matrix for all eight fixtures.
- 2026-09-11: named tests lock `examples/MATRIX.md` eight expected exits and re-run the live audits.
- 2026-09-11: JSONL objects with `timestamp` but neither `text` nor `fields` are ERROR (exit 1).

## SUNDAY CLOSE (2026-09-06)

Week opened Mon 2026-08-31. Usefulness gate re-run on `ae1879c` (HEAD = origin/main).

| Signal | Result |
| --- | --- |
| CI status | PASS — Actions success 3.10 / 3.11 / 3.12 on `ae1879c` ([run 34019459544](https://github.com/homayoun-safarpour/agent-constraint-auditor/actions/runs/34019459544)) |
| Local gate | PASS — `ruff check .` clean; `pytest` 36 passed |
| Claim still true? | YES — YAML spec + loop-engine journal → deterministic CLEAN / DECAY / ERROR; decaying fixture still reports 3 violations, first_index=2, slope=2.000 |
| Example still runnable? | YES — stable 0, decaying 2, required_present 0, required_missing 2, empty 1, headerless 1; `--report` still opens `Verdict: CLEAN\|DECAY` |

### LinkedIn draft (field pain first; no employer demand)

1. Long-horizon agent loops can drop the rules you wrote down and still look busy - the transcript has no fail-closed check.
2. I keep a narrow public CLI that audits *your* journal or JSONL events against *your* YAML constraint spec (regex/predicate, not an LLM judge).
3. Exit contract: `0` CLEAN, `2` DECAY, `1` ERROR. Empty, headerless, or empty JSONL is ERROR, not a free CLEAN.
4. This week locked markdown and JSONL polarities in fixtures (stable/decaying + jsonl_stable/jsonl_decaying) with named `--report` verdicts.
5. Fork path: README Quickstart + `examples/MATRIX.md` (eight worked exits), `pip install -e ".[dev]"`, under 30 minutes.

## Journal

- 2026-09-04 heartbeat: OK (W15 matches `df3882e`; named `--report` CLEAN lock; CI green). ENRICH. Next tick: W16 document required fixtures in `examples/README.md`.
- 2026-09-05 daily: W16 done; `examples/README.md` documents required_present (exit 0) and required_missing (exit 2). Next tick: W17 named test lock on those rows.
- 2026-09-05 daily: W17 shipped; named test locks required-pair rows in `examples/README.md`. Next tick: W18 worked ERROR fixtures (empty / headerless, exit 1).
- 2026-09-06 daily: W18 shipped; `examples/empty` and `examples/headerless` are ERROR exit 1 (no parseable events). Next tick: W19 named test lock on those `examples/README.md` rows.
- 2026-09-06 daily: W19 shipped; named test locks empty/headerless ERROR rows in `examples/README.md`. Next tick: W20 document those fixtures in `docs/ADAPTER.md`.
- 2026-09-06 sunday: usefulness gate green (CI `ae1879c`, ruff + 36 pytest, six examples). Claim holds. Next tick: W20 + Monday week retarget 2026-09-07.
- 2026-09-06 local Midday+Daily+Sunday: W20 ADAPTER ERROR docs on main; growth pulse + second-brain card written. ENRICH→SHIP. Next: Monday week retarget.
- 2026-09-07 daily: week header 2026-09-07; W21 named test locks `docs/ADAPTER.md` ERROR fixture rows (exit 1). Next tick: W22 `parse-transcript` fail-closed on empty/headerless.
- 2026-09-07 daily: W22 JSONL transcript parse (`--format jsonl` / `{` auto-detect). Next tick: W23 `parse-transcript` fail-closed on empty/headerless.
- 2026-09-07 heartbeat: OK (W22 matches `7dbfb34`; named JSONL audit locks; CI green run 34096249251). ENRICH. Next tick: W23 `parse-transcript` fail-closed empty/headerless.
- 2026-09-08 daily: W23 shipped; `parse-transcript` on empty/headerless journals exits 1 (ERROR), not `OK: 0 events`. Next tick: W24 `parse-transcript --format`.
- 2026-09-08 daily: W24 shipped; `parse-transcript --format jsonl|journal|auto` matches `audit`. Next tick: W25 worked JSONL fixture under `examples/`.
- 2026-09-08 daily: W25 shipped; `examples/jsonl_stable` CLEAN via `--format jsonl`. Next tick: W26 named test lock on that README row.
- 2026-09-08 daily: W26 shipped; named test locks `examples/README.md` jsonl_stable row. Next tick: W27 JSONL DECAY fixture.
- 2026-09-09 daily: W27 shipped; `examples/jsonl_decaying` DECAY via `--format jsonl` (exit 2). Next tick: W28 named test lock on that README row.
- 2026-09-09 daily: W28 shipped; named test locks `examples/README.md` jsonl_decaying row (exit 2 DECAY). Next tick: W29 named `--report` lock.
- 2026-09-09 heartbeat: OK (W28 matches `d68e442`; named jsonl_decaying README lock; CI green run 34324487698). ENRICH. Next tick: W29 named `--report` lock for `examples/jsonl_decaying`.
- 2026-09-10 daily: W29 shipped; named `--report` lock for `examples/jsonl_decaying` (Verdict: DECAY, 3 violations, first event 2). Next tick: W30 named `--report` lock for `examples/jsonl_stable`.
- 2026-09-10 daily: W30 shipped; named `--report` lock for `examples/jsonl_stable` (Verdict: CLEAN, holds all constraints across 4 events). Next tick: W31 document JSONL fixtures in `docs/ADAPTER.md`.
- 2026-09-10 daily: W31 shipped via PR #23; ADAPTER documents jsonl_stable/decaying. Next tick: W32 named ADAPTER lock.
- 2026-09-10 daily: W32 shipped; named test locks ADAPTER JSONL rows. Next tick: W33 heartbeat quality pass.
- 2026-09-10 daily: W33 green (57 pytest, jsonl_stable 0 / jsonl_decaying 2, CI main green). Next: W34 interview JSONL.
- 2026-09-10 daily: W34–W35 shipped; INTERVIEW + RELIABILITY_CARD JSONL + named locks. Next: W36 Sunday prep checklist.
- 2026-09-10 daily: W36 shipped; `examples/MATRIX.md` lists all fixture exits for Sunday gate. Next: W37 CI tip green check.
- 2026-09-10 daily: W37–W38 shipped; CI green run 34492448163; README links MATRIX. Next: W39 dry-run.
- 2026-09-10 daily: W39 MATRIX dry-run ALL OK (stable0 decaying2 required 0/2 empty1 headerless1 jsonl 0/2). Next: W40 growth pulse + LinkedIn refresh.
- 2026-09-11 daily: W43 Fri hold; named MATRIX exit-row lock (table + live 0/2/0/2/1/1/0/2). Next: W44 Sunday usefulness gate.
- 2026-09-11 daily: W45 shipped; timestamp-only JSONL is ERROR exit 1 (`needs text and/or fields`). Next: W44 Sunday usefulness gate.
- 2026-09-11 heartbeat: OK (W45 matches `f166fa2`; timestamp-only JSONL ERROR named locks; CI green run 34575165277). HOLD. Next tick: W44 Sunday usefulness gate.

## NEXT TICK (daily 2026-09-11)

- W44: Sunday 2026-09-13 usefulness gate (CI 3.10/3.11/3.12 + pytest/ruff + eight MATRIX exits + claim still true). If this tick fires Sat 2026-09-12, hold — do not invent a new fixture or CLI surface.
- Why next: week graph closes Sunday; JSONL body fail-closed is locked so the gate cannot treat timestamp-only lines as CLEAN.
- Verify: `python -m pytest -q`; `python -m ruff check .`; eight MATRIX audit exits 0/2/0/2/1/1/0/2; timestamp-only JSONL audit exit 1; LOOP_STATE Sunday checklist

## NEXT TICK (heartbeat 2026-09-11)

- W44: Sunday 2026-09-13 usefulness gate (CI 3.10/3.11/3.12 + pytest/ruff + eight MATRIX exits 0/2/0/2/1/1/0/2 + timestamp-only JSONL exit 1 + claim still true). Do not invent a new fixture or CLI surface before Sunday.
- Why: quality pass on `f166fa2` holds (README timestamp-only ERROR claim + named tests); remaining week graph is the close gate, not new product.
- Verify: `python -m pytest -q`; `python -m ruff check .`; eight MATRIX audits 0/2/0/2/1/1/0/2; timestamp-only JSONL audit exit 1; Actions 3.10/3.11/3.12 green on the Sunday HEAD
