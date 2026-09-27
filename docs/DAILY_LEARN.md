# Daily learning — 2026-09-27

**Skill.** Sunday usefulness gate: reprint the nine MATRIX exits. Row stays `0/2/0/2/1/1/0/2/1`. Decaying `--report` still opens `Verdict: DECAY` (3 violations, first event 2, slope 2.000). Do not retarget mid-week.

**Why.** The hire-visible lock is the live nine-exit reprint, not a new repo. Usefulness is "the claim still runs." Monday is the retarget day. Do not scaffold `agent-trust-gate` from this checkout.

**Worked example** (this repo). Replay CLEAN / DECAY / ERROR once each, then lock the decaying report line.

```bash
constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# exit 0 CLEAN

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# exit 2 DECAY; stdout verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# /tmp/decay.md opens: Verdict: DECAY

constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
# exit 1 ERROR — no parseable events, never CLEAN
```

Full row: `stable` 0 · `decaying` 2 · `required_present` 0 · `required_missing` 2 · `empty` 1 · `headerless` 1 · `jsonl_stable` 0 · `jsonl_decaying` 2 · `jsonl_bad_timestamp` 1.

**Recall probe.** What is the nine-exit row, and what must decaying `--report` open with?

Answer: `0/2/0/2/1/1/0/2/1`. Report opens `Verdict: DECAY`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `examples/decaying` · README first screen · Exit codes
