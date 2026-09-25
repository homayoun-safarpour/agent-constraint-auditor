# Daily learning — 2026-09-25

**Skill.** `forbid: false`: a missing required pattern is DECAY, not CLEAN. MATRIX reprints `0/2/0/2/1/1/0/2/1`. The second `0`/`2` pair is `required_present` / `required_missing`.

**Why.** Default `forbid: true` punishes a match. The other half of the spec punishes silence. A journal that never writes `lint=PASS` can look busy and still fail the gate.

**Worked example** (this repo). Same rule id `require_lint_pass`, pattern `lint\s*=\s*PASS`. Present on every event → 0. Omitted on all four events → 2, first at index 0.

```bash
constraint-auditor audit \
  --constraints examples/required_present/constraints.yaml \
  --transcript examples/required_present/journal.md
# exit 0 CLEAN — every event records lint=PASS

constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md \
  --report /tmp/required-decay.md
# exit 2
# 4 violations of require_lint_pass, first_index=0
# report: Verdict: DECAY · first at event 0
```

**Recall probe.** What does `forbid: false` do, and what exits do the required_* fixtures print?

Answer: Missing the required pattern is DECAY. `required_present` → 0. `required_missing` → 2. Row stays `0/2/0/2/1/1/0/2/1`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/required_present` · `examples/required_missing` · `src/constraintauditor/checkers.py` · examples/README
