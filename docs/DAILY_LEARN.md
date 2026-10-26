# Daily learning — 2026-10-25

**Skill.** Sunday usefulness reprints two locks: MATRIX `0/2/0/2/1/1/0/2/1` and decaying `--report` `3 / first at event 2 / slope 2.000`. This repo's CI is ruff + pytest; the live MATRIX test is the nine-exit lock. Monday retargets the week window. Sunday does not.

**Why.** Saturday named the exit string. Mon–Fri named one audit (hire line → JSON → report → process exit → who consumes it). Sunday asks whether the claim still holds — same nine fixtures, same decaying freeze. INTERVIEW Q3: exit 2 is measurable constraint decay. Do not scaffold `agent-trust-gate`. Do not open a JSONL parser family.

**Worked example** (this repo).

```bash
python -m pytest tests/test_examples.py::test_examples_matrix_live_exits_match_table -q
# 0/2/0/2/1/1/0/2/1

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
# stdout: verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# report: Verdict: DECAY · 3 violations, first at event 2 · slope 2.000

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl --report /tmp/jsonl-decay.md
# same three freeze numbers (`spec_name=jsonl-decaying-agent`)

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# DECAY exit=2 slope=0.000 — still a fail; slope 0 is not CLEAN

python -m ruff check .
```

**Recall probe.** Name the two Sunday locks. Does a green gate retarget the week or open `agent-trust-gate`?

Answer: nine exits `0/2/0/2/1/1/0/2/1`, and decaying 3 / first_index=2 / slope=2.000 (same on JSONL decaying). No and no. Monday retargets. required_missing stays 2. Empty stays 1. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `tests/test_examples.py` (`test_examples_matrix_live_exits_match_table`) · `src/constraintauditor/decay.py` · `docs/INTERVIEW.md` · `LOOP_STATE.md` (`## BENCHMARK GATE`) · README
