# Daily learning — 2026-10-31

**Skill.** Sunday-prep is speaking the nine-exit row in fixture order. One string: `0/2/0/2/1/1/0/2/1` = stable / decaying / required_present / required_missing / empty / headerless / jsonl_stable / jsonl_decaying / jsonl_bad_timestamp. Live lock `test_examples_matrix_live_exits_match_table`; table lock `test_examples_matrix_locks_exit_rows`.

**Why.** Tomorrow reprints this string plus decaying `--report` `3 / first at event 2 / slope 2.000` (same freeze on JSONL decaying). Saturday is the speak-it-cold check so Sunday is verification. LinkedIn draft locks the same row; the public paste still leads with the decaying hire line. Week lock remains this repo. Do not scaffold `agent-trust-gate` or open a JSONL parser family.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# 2 — first 2; hire line violations=3 first_index=2 slope=2.000

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# 2 — second 2; forbid:false DECAY; slope 0.000 still fails

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
constraint-auditor audit --constraints examples/headerless/constraints.yaml --transcript examples/headerless/journal.md
# 1 / 1 — middle ERROR pair

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl
# 2 — third 2; same three numbers as journal decaying

constraint-auditor audit --constraints examples/jsonl_bad_timestamp/constraints.yaml --transcript examples/jsonl_bad_timestamp/events.jsonl --format jsonl
# 1 — last 1; timestamp not YYYY-MM-DD HH:MM

python -m pytest tests/test_examples.py::test_examples_matrix_live_exits_match_table -q
# locks 0/2/0/2/1/1/0/2/1
```

**Recall probe.** Name the three 2s. Which 1 is `jsonl_bad_timestamp`? Does `required_missing` slope 0.000 make it CLEAN?

Answer: decaying, required_missing, jsonl_decaying. The last 1 (empty/headerless are the middle 1/1). No — forbid:false DECAY is still exit 2. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `tests/test_examples.py` (`test_examples_matrix_live_exits_match_table`, `test_examples_matrix_locks_exit_rows`) · `docs/LINKEDIN_DRAFT.md` · `docs/INTERVIEW.md` · README Quickstart
