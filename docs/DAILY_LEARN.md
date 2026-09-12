# Daily learning  -  2026-09-12

**Skill.** A JSONL object with only `timestamp` is not an empty CLEAN event. `parse_jsonl_transcript` requires `timestamp` plus non-empty `text` and/or `fields`. `fields: {}` and whitespace-only `text` fail the same way: `TranscriptError` → exit `1`.

**Why.** Fail-closed gate: a heartbeat that dropped its payload must not score CLEAN. Same contract as empty/headerless journals. Sunday usefulness (2026-09-13) is `examples/MATRIX.md` (eight fixtures, exits 0/2/0/2/1/1/0/2). This extra JSONL ERROR is locked in tests, not in that table.

**Worked example** (this repo). `examples/jsonl_stable` is fields-only (no `text` key) and is CLEAN:

```bash
constraint-auditor parse-transcript --format jsonl examples/jsonl_stable/events.jsonl
# OK: 4 events  exit 0

constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format jsonl
# verdict=CLEAN exit=0
```

Parser gate (`src/constraintauditor/journal.py`):

```python
has_text = isinstance(text, str) and bool(text.strip())
if not has_text and not fields:
    raise TranscriptError(f"JSONL line {line_no} needs text and/or fields")
```

Named locks: `test_parse_jsonl_timestamp_only_is_transcript_error`, `test_audit_jsonl_timestamp_only_exit_1`.

**Recall probe.** Line is `{"timestamp": "2026-08-11 09:00", "fields": {}}`. You run `parse-transcript --format jsonl`, then `audit --format jsonl` with `examples/stable/constraints.yaml`. Exits?

Answer: both `1`. Empty `fields` is falsy; no body → `TranscriptError`. CLEAN/DECAY are unreachable.

**Retrieve.** `src/constraintauditor/journal.py` · `cli.py` · `tests/test_journal.py` · `tests/test_cli.py` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK
