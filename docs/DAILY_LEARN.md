# Daily learning — 2026-10-02

**Skill.** Unparseable transcripts exit `1` ERROR, not CLEAN. Empty, headerless, and a JSONL `T` timestamp never print a decay line. Exit `2` is only for a parseable journal that breaks the spec.

**Why.** Interview Q3: CI treats `2` as measurable decay. A missing or malformed transcript must not look green. MATRIX stays `0/2/0/2/1/1/0/2/1` — the last `1` is `jsonl_bad_timestamp`.

**Worked example** (this repo). Replay the three ERROR fixtures, then decaying so you do not collapse `1` and `2`.

```bash
constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
# ERROR: transcript contains no parseable events · exit 1

constraint-auditor audit \
  --constraints examples/headerless/constraints.yaml \
  --transcript examples/headerless/journal.md
# same ERROR · exit 1  (body exists; no dated ## heading)

constraint-auditor audit \
  --constraints examples/jsonl_bad_timestamp/constraints.yaml \
  --transcript examples/jsonl_bad_timestamp/events.jsonl \
  --format jsonl
# ERROR: JSONL line 1 timestamp must be YYYY-MM-DD HH:MM · exit 1
# fixture timestamp is 2026-08-11T09:00

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
```

**Recall probe.** Why does an empty journal exit `1`, not `0`?

Answer: No parseable events is ERROR. CLEAN needs a dated transcript that holds every rule. `parse-transcript` prints the same ERROR. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/empty` · `examples/headerless` · `examples/jsonl_bad_timestamp` · `examples/decaying` · `examples/MATRIX.md` · `docs/INTERVIEW.md`
