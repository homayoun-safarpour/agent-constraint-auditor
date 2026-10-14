# Daily learning — 2026-10-14

**Skill.** `detail` is a template, not a journal quote. Two prefixes only: `forbid pattern matched:` and `required pattern missing:`. Then the spec `pattern`, not the matching line.

**Why.** Tuesday named the four `--json` keys. Wednesday: the fourth key is the rule that fired. A gate that greps `detail` for `lint=FAIL` or `force-push` misses — those strings live in `event.text`. `--report` reprints the same `detail` after the id.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# exit 2  three rows; none quote "shipping despite red lint"
# [0] never_skip_lint  event 2  detail=forbid pattern matched: lint\s*=\s*FAIL
# [1] never_skip_lint  event 3  same detail (second lint hit)
# [2] no_force_push    event 3  detail=forbid pattern matched: force-push|git push --force

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
# ## Violations reprints the same three details after `never_skip_lint` / `no_force_push`

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md --json
# exit 2  four rows  constraint_id=require_lint_pass
# each detail=required pattern missing: lint\s*=\s*PASS
```

**Recall probe.** Recite the two `detail` prefixes. What is decaying `violations[0].detail` vs required_missing `violations[0].detail`?

Answer: `forbid pattern matched:` and `required pattern missing:`. Decaying[0]: `forbid pattern matched: lint\s*=\s*FAIL`. required_missing[0]: `required pattern missing: lint\s*=\s*PASS`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/checkers.py` · `src/constraintauditor/decay.py` · `examples/decaying/` · `examples/required_missing/`
