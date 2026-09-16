# Daily learning — 2026-09-16

**Skill.** A whitespace-only JSONL file is the same contract as an empty file. Blank lines are skipped, the parser returns no events, and `audit` / `parse-transcript` still ERROR via `no parseable events`.

**Why.** Reviewers who only read the empty-file sentence can treat a file of spaces and newlines as a different ERROR class. It is not. The skip is in `parse_jsonl_transcript`; CLI fail-closed is the second step.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 92. `parse_jsonl_transcript` on a whitespace-only file returns `[]`. CLI still exits `1`.

```bash
python -m pytest -q
# 92 passed
constraint-auditor parse-transcript --format jsonl path/to/whitespace.jsonl
# ERROR: transcript contains no parseable events
# exit 1
```

**Recall probe.** Does `docs/ADAPTER.md` say a whitespace-only JSONL file skips blank lines, parses to no events, and CLI still ERROR?

Answer: Yes. Named test `test_adapter_locks_whitespace_only_jsonl_parses_to_no_events` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W134
