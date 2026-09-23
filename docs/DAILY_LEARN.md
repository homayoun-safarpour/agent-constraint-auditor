# Daily learning — 2026-09-23

**Skill.** Fail-closed ERROR: a transcript you cannot parse is exit 1, never CLEAN. MATRIX reprints `0/2/0/2/1/1/0/2/1`. The three `1`s are `empty`, `headerless`, and `jsonl_bad_timestamp`.

**Why.** The hire-visible lock is polarity, not a new parser family. "No violations" is a free pass only if broken input still exits 0. This CLI refuses that.

**Worked example** (this repo). Replay the three ERROR fixtures. Contrast decaying so you do not mix exit 1 with exit 2.

```bash
constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
# exit 1 — no parseable events

constraint-auditor audit \
  --constraints examples/headerless/constraints.yaml \
  --transcript examples/headerless/journal.md
# exit 1 — no dated ## YYYY-MM-DD HH:MM heading

constraint-auditor audit \
  --constraints examples/jsonl_bad_timestamp/constraints.yaml \
  --transcript examples/jsonl_bad_timestamp/events.jsonl \
  --format jsonl
# exit 1 — ISO `T` timestamp is not YYYY-MM-DD HH:MM

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# exit 2 DECAY — events parsed; rules broken
```

**Recall probe.** Which three fixtures print `1` in the nine-exit row, and what exit is decaying?

Answer: `empty`, `headerless`, `jsonl_bad_timestamp` → 1 ERROR. Decaying → 2 DECAY. Row stays `0/2/0/2/1/1/0/2/1`. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `examples/MATRIX.md` · `examples/empty` · `examples/headerless` · `examples/jsonl_bad_timestamp` · README Exit codes
