# Daily learning  -  2026-09-15

**Skill.** JSONL `timestamp` is a closed grammar, not a date parser. After a non-empty string exists, it must `TIMESTAMP_RE.fullmatch`: `YYYY-MM-DD HH:MM` (space, no `T`, no seconds). Fail → `TranscriptError` → CLI exit 1. Same digits as journal `HEADER_RE`.

**Why.** Missing/blank/non-string is a different error (`missing timestamp`). A present but shapeless value (`yesterday`, `2026-08-11T09:00`, `2026-08-11`) is `timestamp must be YYYY-MM-DD HH:MM`. Both `parse-transcript` and `audit` die in parse; `run_audit` never returns CLEAN. Hire signal: fail-closed transcript gate, not dateutil.

**Worked example** (this repo). Legal shape is what `examples/jsonl_stable` already ships:

```bash
constraint-auditor parse-transcript --format jsonl examples/jsonl_stable/events.jsonl
# OK: 4 events   # "2026-08-11 09:00"
python -m pytest tests/test_journal.py::test_parse_jsonl_non_shaped_timestamp_is_transcript_error \
  tests/test_cli.py::test_audit_jsonl_non_shaped_timestamp_exit_1 \
  tests/test_cli.py::test_parse_transcript_jsonl_non_shaped_timestamp_exit_1 -q
```

Lock in `src/constraintauditor/journal.py`:

```python
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
# ...
if TIMESTAMP_RE.fullmatch(timestamp) is None:
    raise TranscriptError(f"JSONL line {line_no} timestamp must be YYYY-MM-DD HH:MM")
```

**Recall probe.** Line: `{"timestamp": "2026-08-11T09:00", "text": "- gates: lint=PASS"}`. `parse-transcript --format jsonl` and `audit --format jsonl` — exit codes? CLEAN?

Answer: both exit 1. `T` is not a space; `fullmatch` fails. stderr carries `timestamp must be YYYY-MM-DD HH:MM`. Not CLEAN. (Date-only `2026-08-11` is the same ERROR. Missing key is `missing timestamp`, still exit 1.)

**Retrieve.** `src/constraintauditor/journal.py` (`TIMESTAMP_RE`) · `tests/test_journal.py` · `tests/test_cli.py` · `docs/ADAPTER.md` JSONL ERROR row · `LOOP_STATE.md` W57
