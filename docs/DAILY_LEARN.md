# Daily learning — 2026-10-10

**Skill.** Saturday Sunday-prep is the nine-exit MATRIX walk. Recite `0/2/0/2/1/1/0/2/1` from `examples/MATRIX.md`. Those are `audit` exits only.

**Why.** Hire-visible contract is CLEAN 0 / DECAY 2 / ERROR 1. `check-constraints` and `parse-transcript` on decaying print OK and exit 0 — they are not in the string. Do not invent a tenth fixture.

**Worked example** (this repo). MATRIX order, then the spec-only trap.

```bash
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# CLEAN exit=0

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# DECAY exit=2 violations=3 first_index=2 slope=2.000

constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md
# CLEAN exit=0

constraint-auditor audit --constraints examples/required_missing/constraints.yaml --transcript examples/required_missing/journal.md
# DECAY exit=2 violations=4 first_index=0 slope=0.000

constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
constraint-auditor audit --constraints examples/headerless/constraints.yaml --transcript examples/headerless/journal.md
# both ERROR exit=1 — no parseable events

constraint-auditor audit --constraints examples/jsonl_stable/constraints.yaml --transcript examples/jsonl_stable/events.jsonl --format jsonl
# CLEAN exit=0

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl
# DECAY exit=2 — same hire line as markdown decaying

constraint-auditor audit --constraints examples/jsonl_bad_timestamp/constraints.yaml --transcript examples/jsonl_bad_timestamp/events.jsonl --format jsonl
# ERROR exit=1 — timestamp must be YYYY-MM-DD HH:MM (ISO T is not that shape)

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints) exit=0 — regexes compile; not an audit
```

**Recall probe.** Recite the nine-exit string. Why is `check-constraints` on decaying exit 0?

Answer: `0/2/0/2/1/1/0/2/1` = stable / decaying / required_present / required_missing / empty / headerless / jsonl_stable / jsonl_decaying / jsonl_bad_timestamp. `check-constraints` only compiles the YAML. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `examples/README.md` · `src/constraintauditor/cli.py`
