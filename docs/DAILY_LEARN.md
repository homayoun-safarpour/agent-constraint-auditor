# Daily learning — 2026-09-16

**Skill.** A UTF-8 BOM on a JSONL file is invalid JSONL, not a silent decode. `json.loads` rejects the BOM; the parser raises `TranscriptError` (`invalid JSONL`). Switching the reader to `utf-8-sig` would hide that ERROR.

**Why.** Windows editors often write a BOM. Without a named test, a later “helpful” decode change would turn ERROR into CLEAN. The adapter sentence exists so hire docs match the parser lock.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 95. A leading UTF-8 BOM on an otherwise valid JSONL line is ERROR (exit `1`).

```bash
python -m pytest -q
# 95 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_utf8_bom_is_transcript_error
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL file with a UTF-8 BOM is ERROR (invalid JSONL)?

Answer: Yes. Named test `test_adapter_locks_utf8_bom_jsonl_is_invalid_jsonl_error` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W145
