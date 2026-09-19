# Daily learning — 2026-09-19

**Skill.** The nine-row MATRIX is the Sunday usefulness gate: exits `0/2/0/2/1/1/0/2/1`. Empty, headerless, and `jsonl_bad_timestamp` are ERROR (`1`), never a free CLEAN.

**Why.** Interview Q3 and CI both rest on this polarity. Tomorrow is W382 full BENCHMARK GATE. Monday retargets; do not open a second public repo mid-week. This is not a new JSONL parser family.

**Worked example** (this repo). Named-claim pytest is 162. MATRIX stays `0/2/0/2/1/1/0/2/1`.

```bash
python -m pytest -q
# 162 passed
python -m pytest -q tests/test_examples.py::test_examples_matrix_live_exits_match_table
# 1 passed
constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# expect exit 1
```

**Recall probe.** What exits do `examples/empty`, `examples/headerless`, and `examples/jsonl_bad_timestamp` return, and is any of them CLEAN?

Answer: All three exit `1` ERROR. Named tests `test_examples_matrix_locks_exit_rows` and `test_examples_matrix_live_exits_match_table` lock the nine-row table. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `docs/INTERVIEW.md` · `docs/RELIABILITY_CARD.md` · `LOOP_STATE.md` NEXT TICK W382
