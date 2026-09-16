# Daily learning — 2026-09-16

**Skill.** A JSONL file with a blank line between objects still parses. The blank line is not invalid JSONL: empty lines are skipped, so two objects with `\n\n` between them both become events. A whitespace-only file still returns no events and CLI still ERROR.

**Why.** Without a named blank-between-objects lock, a later change that treated any blank line as invalid JSONL would fail a normal pretty dump. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 145.

```bash
python -m pytest -q
# 145 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_blank_lines_between_objects_are_skipped
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL file with a blank line between objects still parses?

Answer: Yes. Named test `test_adapter_locks_jsonl_blank_lines_between_objects_are_skipped` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W324
