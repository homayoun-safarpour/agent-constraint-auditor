# Daily learning — 2026-09-03

**Skill.** Exit `2` is binary DECAY. `first_violation_index` and `decay_slope` (Q4 rate − Q1 rate) say *when* rules dropped and *how fast*. Quartile rate = violations in that slice / events in that slice. One event can fire several constraints, so a rate can exceed `1.0`.

**Why.** This CLI is a deterministic decay gate, not an LLM judge (`docs/INTERVIEW.md`, `docs/RELIABILITY_CARD.md`). Named tests lock the decaying fixture at first index `2` and three violations. The portable claim is fail-closed measurement, not a model score.

**Worked example** (this repo). Four-event journal: events 0–1 stay `lint=PASS`; event 2 records `lint=FAIL`; event 3 records `lint=FAIL` plus `git push --force`.

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --report /tmp/decay.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
```

`compute_decay` (`src/constraintauditor/decay.py`) buckets with `min(3, (i * 4) // n)`. For `n=4` each event is its own quartile → rates `(0.0, 0.0, 1.0, 2.0)`. Slope `2.0` because Q4 has two hits on one event (`never_skip_lint` + `no_force_push`). Report opens `Verdict: DECAY`.

**Recall probe.** Eight events, violations only at indices 6 and 7 (one each). What is `first_violation_index`? Is `decay_slope` positive, zero, or negative? Which quartile holds the first hit?

Answer: index `6`. Slope positive (`test_decay_slope_detects_increase`: Q4 rate `1.0`, Q1 rate `0.0`). First hit is Q4: `_quartile_index(6, 8) = min(3, 24 // 8) = 3`.

**Retrieve.** `src/constraintauditor/decay.py` · `cli.py` · `tests/test_decay.py` · `tests/test_examples.py` · `examples/decaying/` · `docs/INTERVIEW.md`
