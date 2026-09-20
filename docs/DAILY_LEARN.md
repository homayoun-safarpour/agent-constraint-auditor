# Daily learning — 2026-09-20

**Skill.** Sunday usefulness gate: the week only counts if BENCHMARK GATE §A still reprints the frozen nine-fixture MATRIX `0/2/0/2/1/1/0/2/1`. Named-claim pytest stays 163. Monday retargets; no mid-week new repo.

**Why.** The hire signal is a replayable exit contract, not another JSONL parser family. If Sunday cannot reprint those exits and the decaying `--report` triple, the week did not close.

**Worked example** (this repo). Replay the live MATRIX lock and the decaying report numbers.

```bash
python -m pytest -q
# 163 passed
python -m pytest -q tests/test_examples.py::test_examples_matrix_live_exits_match_table
# 1 passed — 0/2/0/2/1/1/0/2/1
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# exit 2; Verdict: DECAY; 3 violations; first at event 2; slope 2.000
```

**Recall probe.** What nine-exit row and decaying `--report` triple must Sunday reprint?

Answer: `0/2/0/2/1/1/0/2/1`. Decaying report stays 3 / first_index=2 / slope=2.000. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `LOOP_STATE.md` BENCHMARK GATE §A · `tests/test_examples.py` · `docs/LINKEDIN_DRAFT.md`
