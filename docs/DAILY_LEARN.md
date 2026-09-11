# Daily learning  -  2026-09-11

**Skill.** Three CLI verbs, three failure domains. `check-constraints` compiles YAML (regex at load). `parse-transcript` parses events only. `audit` does both, then scores decay. `SpecError`, `TranscriptError`, `OSError`, and a missing path all map to exit `1`. CLEAN (`0`) and DECAY (`2`) exist only after a successful parse.

**Why.** The hire signal is a fail-closed gate you can re-run, not a narrative. Sunday usefulness (2026-09-13) is `examples/MATRIX.md`: eight fixtures, three codes. Empty, headerless, or invalid regex never get a free CLEAN.

**Worked example** (this repo).

```bash
constraint-auditor check-constraints examples/stable/constraints.yaml
# OK: stable-agent (2 constraints)  exit 0

constraint-auditor parse-transcript examples/empty/journal.md
# ERROR: transcript contains no parseable events  exit 1

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2
```

`cli.main` catches `SpecError` / `TranscriptError` / `OSError` → `1`. Missing files short-circuit before `run_audit`. `parse-transcript` never opens the spec; `check-constraints` never opens a journal.

**Recall probe.** Valid journal. YAML `pattern: "("`. You run `parse-transcript` on the journal, then `audit` with that spec. Exits?

Answer: parse-transcript `0` (does not load YAML). audit `1` (`SpecError`: pattern is not a valid regex). Decay is unreachable.

**Retrieve.** `src/constraintauditor/cli.py` · `spec.py` · `audit.py` · `examples/MATRIX.md` · `LOOP_STATE.md` NEXT TICK
