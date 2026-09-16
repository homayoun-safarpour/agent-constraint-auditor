# Daily learning — 2026-09-16

**Skill.** A JSONL `text` value that is not a string is treated as missing text. Numeric `text` with no `fields` is ERROR (`needs text and/or fields`). Numeric `text` with `fields` still parses; the body is synthesized from `fields`.

**Why.** `has_text` requires a non-empty string. Without a named test, a later change that stringified `text` the way `fields` values are stringified would look like a parser bug. This is not a timestamp fail-closed case and not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 102. `"text": 1` without fields raises; with fields, body is `- gates: lint=PASS`.

```bash
python -m pytest -q
# 102 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_non_string_text_is_treated_as_missing
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL `text` value that is not a string is treated as missing text?

Answer: Not yet. The parser lock is `test_parse_jsonl_non_string_text_is_treated_as_missing`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W172
