# Daily learning — 2026-10-26

**Skill.** Monday retarget stays on this repo. The week lock is the nine-exit row `0/2/0/2/1/1/0/2/1` — stable / decaying / required_present / required_missing / empty / headerless / jsonl_stable / jsonl_decaying / jsonl_bad_timestamp. Do not scaffold `agent-trust-gate`. Do not open a JSONL parser family.

**Why.** Last week: hire line, `--json`, `--report`, then who binds `exit_code`. This week reprints the same 0/2/1 contract. INTERVIEW Q3: exit 2 is measurable constraint decay. `required_missing` is forbid:false DECAY with slope 0.000 — still a fail. Empty / headerless / bad JSONL timestamp stay ERROR 1, not CLEAN.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# exit 0 CLEAN

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# exit 2 — journal DECAY; --report still 3 / first at event 2 / slope 2.000

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# exit 2 — slope 0.000 is still DECAY

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# exit 1 — fail-closed, not a free CLEAN

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl
# exit 2 — JSONL decaying reprints the same three numbers

python -m pytest tests/test_examples.py::test_examples_matrix_live_exits_match_table -q
# live lock of 0/2/0/2/1/1/0/2/1
```

**Recall probe.** Recite the nine-exit row and fixture order. Does Monday retarget start `agent-trust-gate`? Is `required_missing` CLEAN because slope is 0.000?

Answer: `0/2/0/2/1/1/0/2/1` = stable / decaying / required_present / required_missing / empty / headerless / jsonl_stable / jsonl_decaying / jsonl_bad_timestamp. No and no. Empty stays 1. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `tests/test_examples.py` (`test_examples_matrix_live_exits_match_table`) · README (`loop-engine --gate`) · `docs/INTERVIEW.md` (Q3)
