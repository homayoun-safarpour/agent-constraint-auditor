# Daily learning — 2026-10-15

**Skill.** `timestamp` is the event heading, copied onto the hit. Not wall-clock. Not `--report` write time.

**Why.** Wednesday: `detail` is the spec pattern, so you cannot grep the body out of JSON. Join back to the journal with `timestamp` (and `event_index`). Same string is the `## YYYY-MM-DD HH:MM` heading, the JSONL `timestamp` field, `--json` `violations[i].timestamp`, and the `--report` `[timestamp]` prefix.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# exit 2
# [0] event 2  timestamp=2026-08-11 11:00  never_skip_lint
# [1] event 3  timestamp=2026-08-11 12:00  never_skip_lint
# [2] event 3  timestamp=2026-08-11 12:00  no_force_push
# JSONL decaying reprints the same three timestamps (spec_name=jsonl-decaying-agent)

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
# - [2026-08-11 11:00] event 2 · `never_skip_lint` · forbid pattern matched: ...

constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events
# - 2026-08-11 09:00 / 10:00 / 11:00 / 12:00
```

**Recall probe.** Recite decaying `violations[0].timestamp` vs `[2].timestamp`. CLEAN `violations` is `[]` so there is no timestamp to recite.

Answer: `2026-08-11 11:00` vs `2026-08-11 12:00`. Both event-3 rows share `12:00`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/checkers.py` · `src/constraintauditor/journal.py` · `examples/decaying/` · `examples/jsonl_decaying/`
