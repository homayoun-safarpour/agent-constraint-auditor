# Daily learning  —  2026-09-04

**Skill.** Freeze the markdown `--report`, not just the exit code. W9 locked `examples/decaying` (`Verdict: DECAY`, third-person count, constraint ids). `examples/required_missing` is JSON-locked (`test_required_missing_fixture_exit_2`) but has no named report freeze yet — LOOP_STATE NEXT TICK.

**Why.** Hire signal: a CI gate you can read. Exit `2` is the contract; the report is the artifact. Same family as sentinel JUDGE_DRIFT — fail the build, show which rule, when. Deterministic regex over a declared spec, not an LLM judge.

**Worked example** (this repo). Four `##` events, each missing `lint=PASS`, `forbid: false`:

```bash
constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md \
  --report /tmp/required-decay.md
# verdict=DECAY exit=2 violations=4 first_index=0 slope=0.000
```

Report opens:

```
Verdict: DECAY
The transcript records 4 constraint violations, first at event 0.
```

Each bullet is `required pattern missing: lint\s*=\s*PASS` (`markdown_timeline` in `src/constraintauditor/decay.py`). Contrast W9: decaying fixture first_index=2, slope>0 (late `lint=FAIL` / `git push --force`). Uniform required-absence is first_index=0, slope=0 (Q4−Q1 = 1.00−1.00).

**Recall probe.** You add a named test like `test_decaying_fixture_locks_force_push_line` for `examples/required_missing`. Which three strings must the report contain? Why is `first_violation_index` 0, not 2?

Answer: `Verdict: DECAY`; `The transcript records 4 constraint violations, first at event 0.`; `` `require_lint_pass` `` (and `required pattern missing`). Index 0 because the first `##` block already lacks `lint=PASS`. Slope 0 is not CLEAN — it means decay did not *increase* later.

**Retrieve.** `src/constraintauditor/decay.py` · `audit.write_report` · `tests/test_examples.py` · `LOOP_STATE.md` NEXT TICK · `docs/INTERVIEW.md`
