# Daily learning  -  2026-09-05

**Skill.** Garbage input is ERROR (exit `1`), never CLEAN. Empty or headerless journals raise `TranscriptError`. An uncompilable `pattern` is `SpecError` at spec load. The CLI maps both to exit `1`. CLEAN / DECAY (`0` / `2`) only after a parsed event stream exists.

**Why.** Interview pack: empty journals and invalid regex are not silent passes. The hire-facing claim is a fail-closed decay gate — a missing `## YYYY-MM-DD HH:MM` header must not read as "holds all constraints".

**Worked example** (this repo). The parser starts an event only on `HEADER_RE`. Title lines before the first `##` are skipped.

```bash
constraint-auditor parse-transcript examples/stable/journal.md
# OK: 4 events

constraint-auditor check-constraints examples/stable/constraints.yaml
# OK: stable-agent (2 constraints)

constraint-auditor audit \
  --constraints examples/stable/constraints.yaml \
  --transcript examples/stable/journal.md
# verdict=CLEAN exit=0
```

`run_audit` after parse (`src/constraintauditor/audit.py`):

```python
if not events:
    raise TranscriptError("transcript contains no parseable events")
```

`parse_constraint_spec` compiles each pattern (`re.compile`). A lone `(` fails `check-constraints` and `audit` with exit `1`.

**Recall probe.** Transcript is `# notes` plus `- gates: lint=PASS` — no `## YYYY-MM-DD HH:MM`. Audit against `examples/stable/constraints.yaml`. Exit `0`, `1`, or `2`?

Answer: `1`. `current_ts` stays `None`; flush never appends; events is empty; CLI prints `ERROR: transcript contains no parseable events`. Same exit if `pattern: "("`.

**Retrieve.** `src/constraintauditor/journal.py` · `audit.py` · `spec.py` · `cli.py` · `tests/test_cli.py` · `docs/INTERVIEW.md` · `LOOP_STATE.md` NEXT TICK (W16)
