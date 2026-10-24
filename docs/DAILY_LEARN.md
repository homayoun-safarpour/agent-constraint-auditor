# Daily learning — 2026-10-24

**Skill.** Saturday Sunday-prep is one string: `0/2/0/2/1/1/0/2/1`. Fixture order is stable, decaying, required_present, required_missing, empty, headerless, jsonl_stable, jsonl_decaying, jsonl_bad_timestamp. The live lock is `test_examples_matrix_live_exits_match_table`; the table lock is `test_examples_matrix_locks_exit_rows`.

**Why.** Mon–Fri named one audit (hire line → JSON → report → process exit → who consumes it). Saturday names the week-close set Sunday re-runs with ruff + pytest. INTERVIEW Q3 stays "exit 2 is decay"; the MATRIX is how the other seven rows cannot drift. Do not open a JSONL parser family or scaffold `agent-trust-gate` from this checkout.

**Worked example** (this repo).

```bash
python -m pytest tests/test_examples.py::test_examples_matrix_live_exits_match_table -q
# nine audits; lock is 0/2/0/2/1/1/0/2/1

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# 2 — forbid:false missing pattern; slope 0.000 is still DECAY

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# 1 — fail-closed, not a free CLEAN

constraint-auditor audit --constraints examples/jsonl_bad_timestamp/constraints.yaml --transcript examples/jsonl_bad_timestamp/events.jsonl --format jsonl
# 1 — ISO T timestamp is not YYYY-MM-DD HH:MM

python -m pytest tests/test_examples.py::test_linkedin_draft_locks_nine_fixture_matrix -q
# LinkedIn paste names the same nine-exit row
```

**Recall probe.** Recite the nine exits. Which row is `forbid: false` DECAY? Which is JSONL ERROR?

Answer: `0/2/0/2/1/1/0/2/1`. required_missing is the fourth 2. jsonl_bad_timestamp is the last 1. empty/headerless are the middle 1/1. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `tests/test_examples.py` · `docs/LINKEDIN_DRAFT.md` · `docs/INTERVIEW.md` · README Quickstart
