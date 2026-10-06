# Daily learning — 2026-10-06

**Skill.** `--format auto` (the default) is not a guess. A dated `## YYYY-MM-DD HH:MM` heading wins journal. Else the first non-empty `{` is jsonl. Wrong override is ERROR `1`, not DECAY.

**Why.** The hire-visible lock is the same `0`/`2`/`1` contract on both surfaces. Forcing `--format journal` on a CLEAN JSONL fixture is a parse miss, not a rule miss. Do not treat format mismatch as decay.

**Worked example** (this repo). Drop `--format`. Then break it on purpose.

```bash
constraint-auditor parse-transcript examples/jsonl_stable/events.jsonl
# OK: 4 events   (auto: first non-empty line starts with `{`)

constraint-auditor parse-transcript examples/stable/journal.md
# OK: 4 events   (auto: dated `##` heading wins)

constraint-auditor parse-transcript --format journal examples/jsonl_stable/events.jsonl
# ERROR: transcript contains no parseable events   exit=1

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# same line with or without `--format jsonl`

constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format journal
# ERROR exit=1 — not CLEAN, not DECAY
```

**Recall probe.** Why does `--format journal` on `examples/jsonl_stable/events.jsonl` exit `1` instead of `0`?

Answer: Auto would pick jsonl. The journal parser finds no `##` headings, so zero events. Empty parse is ERROR, never CLEAN. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/journal.py` `detect_format` · `examples/jsonl_stable` · `examples/stable` · `examples/jsonl_decaying` · README `--format auto`
