# Daily learning — 2026-10-08

**Skill.** Checkers search `event.text`, not the JSON object. Fields-only JSONL is turned into `- key: value` lines before the regex runs. `jsonl_decaying` has no `text` key; `lint=FAIL` still matches because it lives in `fields.gates`.

**Why.** Journal and JSONL share one hire-visible line: `verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000`. Format is a parser choice. Matching is always against declared or synthesized text.

**Worked example** (this repo). Parse JSONL to see field keys, then audit. Contrast the markdown journal and the clean JSONL.

```bash
constraint-auditor parse-transcript --format jsonl examples/jsonl_decaying/events.jsonl
# OK: 4 events
# - 2026-08-11 09:00: ['gates', 'decision', 'reason']
# parse lists keys; checkers do not search those names.

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# Event 2: fields.gates holds lint=FAIL → synthesized "- gates: ... lint=FAIL"

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# same line: the markdown body is already event.text

constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format jsonl
# verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000
```

**Recall probe.** Why does fields-only `jsonl_decaying` match `lint\s*=\s*FAIL` when no object has a `text` key?

Answer: Missing or blank `text` is replaced with `- {key}: {value}` from `fields`. Regex runs on that string (`IGNORECASE`). `parse-transcript` prints field keys only; it is not the match surface. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/jsonl_decaying` · `examples/decaying` · `examples/jsonl_stable` · `src/constraintauditor/journal.py` · `src/constraintauditor/checkers.py`
