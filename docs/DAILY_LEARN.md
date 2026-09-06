# Daily learning  -  2026-09-06

**Skill.** `parse-transcript` is a dry-run. It never fail-closes. Empty and headerless files both parse to `[]`; the command prints `OK: 0 events` and exits `0`. Only `audit` raises `TranscriptError` when the event list is empty (`exit 1`). Same exception, two human fixtures — not two code paths.

**Why.** W18 needs forkable ERROR examples. If you verify those files with `parse-transcript`, they look healthy. The hire-facing gate is `audit` exit `1` (ERROR), never CLEAN. Interview pack: empty journals are not silent passes.

**Worked example** (this repo). Parser starts an event only on `HEADER_RE` = `## YYYY-MM-DD HH:MM` (time required; `# notes` does not count). Lines before the first header are skipped.

```bash
constraint-auditor parse-transcript examples/stable/journal.md
# OK: 4 events   exit 0

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0
```

`parse_loop_engine_journal` (`src/constraintauditor/journal.py`) returns `[]` and does not raise. The gate lives in `run_audit`:

```python
if not events:
    raise TranscriptError("transcript contains no parseable events")
```

CLI: `parse-transcript` always `return 0` after a successful read. `audit` maps `TranscriptError` to exit `1`. W18 empty (zero bytes) and headerless (`# notes` + bullets) both hit that one `if not events`.

**Recall probe.** You write `examples/headerless/journal.md` as `# notes` plus `- gates: lint=PASS`. You run `parse-transcript` on it, then `audit` against `examples/stable/constraints.yaml`. What two exit codes? Why is this not DECAY?

Answer: `0` then `1`. Zero parseable events — `current_ts` stays `None`, flush never appends. DECAY (`2`) needs at least one event plus a constraint miss. No events is ERROR, not "holds all constraints".

**Retrieve.** `src/constraintauditor/journal.py` · `audit.py` · `cli.py` · `tests/test_cli.py` (`test_empty_transcript_is_error_exit_1`, `test_headerless_journal_is_error_exit_1`) · `docs/INTERVIEW.md` · `LOOP_STATE.md` NEXT TICK (W18)
