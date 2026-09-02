# Daily learning — 2026-09-02

**Skill.** `forbid: false` is a required regex: every journal event must match. Miss = violation (`required pattern missing`). Default `forbid: true` is the inverse: a match is a violation (`forbid pattern matched`).

**Why.** This week's next tick is a named test locking that polarity. Both public fixtures (`examples/stable`, `examples/decaying`) are `forbid: true` only. Hire signal: deterministic decay gate over a declared spec — not an LLM judge.

**Worked example** (this repo). Stable fixture is CLEAN: no event contains `lint=FAIL` or `git push --force`.

```bash
constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0
```

Polarity lives in `check_event` (`src/constraintauditor/checkers.py`):

```python
if constraint.forbid and matched:            # banned string appeared
if (not constraint.forbid) and not matched:  # required string absent
```

YAML may omit `forbid`; `Constraint` defaults it to `True` (`src/constraintauditor/spec.py`). Required-pattern lock:

```python
from constraintauditor.checkers import check_transcript
from constraintauditor.journal import JournalEvent
from constraintauditor.spec import Constraint, ConstraintSpec

spec = ConstraintSpec("t", (Constraint("must_log_gates", "", r"gates:", forbid=False),))
events = [JournalEvent("2026-09-02 07:00", "- decision: advance", {})]
assert check_transcript(spec, events)[0].detail.startswith("required pattern missing")
```

**Recall probe.** Event text is `- gates: tests=PASS` (no lint line). Spec: `pattern: "lint="`, `forbid: false`. CLEAN or DECAY? Is the check over the whole transcript or per event?

Answer: DECAY — required pattern missing on that event. `check_transcript` multiplies constraints × events; a required pattern must hit *every* event, not once somewhere.

**Retrieve.** `src/constraintauditor/checkers.py` · `spec.py` · `tests/test_checkers.py` · `LOOP_STATE.md` NEXT TICK · `docs/INTERVIEW.md`
