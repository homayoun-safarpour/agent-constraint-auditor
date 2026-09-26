# Daily learning — 2026-09-26

**Skill.** Journal and JSONL share the exit contract. `decaying` and `jsonl_decaying` both print `verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000`. Format is encoding, not a second product.

**Why.** Interview Q3 and the reliability card rest on one polarity: 0 CLEAN / 2 DECAY / 1 ERROR, markdown or JSONL. Saturday Sunday-prep is replaying that lock, not opening a parser family.

**Worked example** (this repo). Same four events, same two forbid rules (`never_skip_lint`, `no_force_push`). Event 2 hits `lint=FAIL`. Event 3 hits `lint=FAIL` and force-push. Parse still says 4 events; audit applies the spec.

```bash
constraint-auditor parse-transcript --format jsonl examples/jsonl_decaying/events.jsonl
# OK: 4 events — parser does not score decay

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# exit 2 · violations=3 first_index=2 slope=2.000

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl \
  --report /tmp/jsonl-decay.md
# exit 2 · same line · report: Verdict: DECAY

constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format jsonl
# exit 0 · first_index=None · slope=0.000
```

**Recall probe.** Do `decaying` and `jsonl_decaying` share exit and decay line? What does `parse-transcript` print on the JSONL decaying file?

Answer: Both exit 2 with 3 / first_index=2 / slope=2.000. Parse prints `OK: 4 events` — it does not apply constraints. Row stays `0/2/0/2/1/1/0/2/1`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/decaying` · `examples/jsonl_decaying` · `examples/jsonl_stable` · `docs/INTERVIEW.md` · `docs/RELIABILITY_CARD.md`
