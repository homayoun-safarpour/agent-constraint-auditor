# Daily learning — 2026-09-16

**Skill.** A public ERROR fixture is not done at `examples/`. The lock ladder is parser → worked fixture → `examples/README.md` row → adapter table/verify. W59 froze the examples row; `docs/ADAPTER.md` still names JSONL CLEAN/DECAY only (`jsonl_stable` / `jsonl_decaying`). Markdown ERROR is `empty` / `headerless`.

**Why.** Hire signal: a reviewer who wires loop-engine reads the adapter, not the examples table. Fail-closed JSONL timestamps are a parser fact (W57) and a worked fixture (W58); they are not yet an adapter named row (W60). Same repo this week; regex gate, not an LLM judge.

**Worked example** (this repo). One ISO-`T` line, valid `fields`:

```bash
constraint-auditor parse-transcript --format jsonl examples/jsonl_bad_timestamp/events.jsonl
# ERROR: JSONL line 1 timestamp must be YYYY-MM-DD HH:MM
# exit 1

constraint-auditor audit \
  --constraints examples/jsonl_bad_timestamp/constraints.yaml \
  --transcript examples/jsonl_bad_timestamp/events.jsonl \
  --format jsonl
# same ERROR, exit 1 — never CLEAN
```

`events.jsonl` uses `"timestamp": "2026-08-11T09:00"`. Parse dies before `check_event`. Adapter verify still only audits jsonl_stable (0) and jsonl_decaying (2).

**Recall probe.** Does the `docs/ADAPTER.md` ERROR (fail-closed) row name `examples/jsonl_bad_timestamp`?

Answer: No. That row is `examples/empty` and `examples/headerless`. Shapeless JSONL timestamps are adapter prose (`that is not YYYY-MM-DD HH:MM is ERROR`) without the fixture path. W60 is naming it beside the JSONL pair.

**Retrieve.** `examples/jsonl_bad_timestamp/` · `examples/README.md` · `docs/ADAPTER.md` · `tests/test_examples.py` (`test_adapter_locks_jsonl_fixture_rows`) · `LOOP_STATE.md` NEXT TICK W60
