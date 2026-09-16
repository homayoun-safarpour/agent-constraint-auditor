# Daily learning — 2026-09-16

**Skill.** A JSONL object with non-empty `text` and `fields` uses the text body. Fields still parse. `"text": "- gates: from-text"` plus `"fields": {"gates": "from-fields"}` yields body `- gates: from-text` and `gates="from-fields"`. Whitespace-only or empty `text` with `fields` still uses the fields body.

**Why.** Without a named text-wins lock, a later change that always synthesized from `fields` would discard an explicit `text` body. This is not a boolean-field enum.

**Worked example** (this repo). MATRIX stays `0/2/0/2/1/1/0/2/1`. Named-claim pytest is 139.

```bash
python -m pytest -q
# 139 passed
python -m pytest -q tests/test_journal.py::test_parse_jsonl_nonempty_text_with_fields_uses_text
# 1 passed
```

**Recall probe.** Does `docs/ADAPTER.md` say a JSONL object with non-empty `text` and `fields` uses the text body?

Answer: Yes. Named test `test_adapter_locks_nonempty_text_with_fields_uses_text` locks that sentence. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` · `tests/test_journal.py` · `docs/ADAPTER.md` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK W303
