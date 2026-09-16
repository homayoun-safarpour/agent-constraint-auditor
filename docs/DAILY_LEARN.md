# Daily learning — 2026-09-16

**Skill.** An empty JSONL file is not a parse error. The parser returns no events; `audit` and `parse-transcript` still ERROR via `no parseable events`. Hire docs must name that split, or reviewers treat empty JSONL as invalid JSON.

**Why.** Object/fields shape errors raise in the parser. An empty file does not. CLI fail-closed is a second step. Mixing those two looks like one ERROR bucket and hides the contract.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 90. `parse_jsonl_transcript` on an empty file returns `[]`. CLI still exits `1`.

```bash
python -m pytest -q
# 90 passed
constraint-auditor parse-transcript --format jsonl path/to/empty.jsonl
# ERROR: transcript contains no parseable events
# exit 1
```

**Recall probe.** Does `docs/ADAPTER.md` say an empty JSONL file parses to no events and CLI still ERROR?

Answer: Yes. Named test `test_adapter_locks_empty_jsonl_parses_to_no_events` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W127
