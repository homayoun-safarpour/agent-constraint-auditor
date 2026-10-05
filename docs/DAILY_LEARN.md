# Daily learning — 2026-10-05

**Skill.** `parse-transcript` is a dry-run. The decaying journal still prints `OK: 4 events` and exits 0. Those same events audit `verdict=DECAY exit=2`. Preflight is not the gate.

**Why.** The hire-visible lock is `audit` exit `0` / `2` / `1`. Parse only asks whether dated events exist. `check-constraints` only asks whether the regexes compile. A `--gate` wired to either dry-run would green a decaying week.

**Worked example** (this repo). Replay decaying parse, then audit. Contrast empty so you do not treat every exit 0 as CLEAN.

```bash
constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events   exit 0

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints)   exit 0

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

constraint-auditor parse-transcript examples/empty/journal.md
# ERROR: transcript contains no parseable events   exit 1
```

**Recall probe.** Why does decaying `parse-transcript` exit 0 while `audit` exits 2?

Answer: Parse counts dated events. It does not run forbid rules. Event 2 and 3 still match `never_skip_lint` / `no_force_push`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/cli.py` · `examples/decaying` · `examples/empty` · README Exit codes · `docs/ADAPTER.md` Gate wiring
