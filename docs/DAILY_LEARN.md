# Daily learning — 2026-09-16

**Skill.** Whitespace-only JSONL `text` with `fields` uses the fields body. `"text": "   "` is not `has_text`. Without fields that is ERROR; with fields, body is synthesized from `fields`.

**Why.** `has_text` requires a non-empty string after strip. Without a named test, a later change that kept the whitespace `text` instead of synthesizing from `fields` would look like a parser bug. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 111. Whitespace text plus `{"gates": "lint=PASS"}` yields `- gates: lint=PASS`.

```bash
python -m pytest -q
# 111 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_whitespace_text_with_fields_uses_fields
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say whitespace-only JSONL `text` with `fields` uses the fields body?

Answer: Yes. Named test `test_adapter_locks_whitespace_jsonl_text_with_fields_uses_fields` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W205
