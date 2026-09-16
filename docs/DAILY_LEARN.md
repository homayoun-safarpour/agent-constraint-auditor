# Daily learning — 2026-09-16

**Skill.** Empty-string JSONL `text` (`""`) is treated as missing text. Without `fields` that is ERROR (`needs text and/or fields`). With `fields`, body is synthesized from `fields`. Same `has_text` rule as whitespace-only text.

**Why.** `bool("".strip())` is false, so `""` is not `has_text`. Without a named test, a later change that treated empty string as present text would look like a parser bug. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 113. `"text": ""` plus `{"gates": "lint=PASS"}` yields `- gates: lint=PASS`.

```bash
python -m pytest -q
# 113 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_empty_string_text_with_fields_uses_fields
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say empty-string JSONL `text` with `fields` uses the fields body?

Answer: Yes. Named test `test_adapter_locks_empty_string_jsonl_text_with_fields_uses_fields` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W215
