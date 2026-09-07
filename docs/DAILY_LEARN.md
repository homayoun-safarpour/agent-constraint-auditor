# Daily learning  -  2026-09-07

**Skill.** Constraint regexes search `event.text`, not `event.fields` and not the `##` header. The parser keeps the heading in `timestamp`; only following lines enter the blob. `parse-transcript` prints field keys as a debug view — `check_event` never reads that map.

**Why.** Hire signal: a deterministic predicate over the declared event body. A rule aimed at the timestamp, or at the field dict, is a silent miss. Week open 2026-09-07; same repo; exit contract stays `0` CLEAN / `2` DECAY / `1` ERROR.

**Worked example** (this repo). Decaying event 2:

```
## 2026-08-11 11:00
- gates: tests=PASS, lint=FAIL
```

`timestamp` is `2026-08-11 11:00`. `text` is the bullet block. `fields["gates"]` is `tests=PASS, lint=FAIL`. Pattern `lint\s*=\s*FAIL` hits because it is in the body.

```bash
constraint-auditor parse-transcript examples/decaying/journal.md
# OK: 4 events — keys only, not the match surface

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2
```

**Recall probe.** Spec: `pattern: "2026-08-11"`, `forbid: true`. Transcript: `examples/stable/journal.md` (headers dated that day; bodies have no date string). CLEAN or DECAY?

Answer: CLEAN. `HEADER_RE` consumes the heading (`continue`); `re.search` runs on `event.text` only. The date lives in `timestamp`.

**Retrieve.** `src/constraintauditor/journal.py` · `checkers.py` · `docs/ADAPTER.md` · `docs/INTERVIEW.md`
