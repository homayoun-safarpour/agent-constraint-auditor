# Daily learning — 2026-09-14

**Skill.** A successful `audit` is one `AuditResult` with three views. Default stdout is the one-liner. `--json` is `to_jsonable()` (machine). `--report PATH` is `markdown_timeline` (human freeze). Both flags together still write the file; stdout becomes JSON, not the one-liner. ERROR never uses these views — stderr + exit `1`.

**Why.** Monday week-open stays on this repo. The hire-facing floor is the golden set (`examples/MATRIX.md` exits `0/2/0/2/1/1/0/2`), not a new instrument. CI takes exit + JSON; a reviewer reads `Verdict: DECAY`. Regex over a declared spec — not an LLM judge.

**Worked example** (this repo).

```bash
constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

constraint-auditor audit \
  --constraints examples/decaying/constraints.yaml \
  --transcript examples/decaying/journal.md \
  --json
# {"verdict":"DECAY","exit_code":2,"decay":{"n_violations":3,"first_violation_index":2,"decay_slope":2.0}}

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl --report /tmp/jsonl-decay.md --json
# stdout JSON; file opens Verdict: DECAY; process exit 2
```

`cli.py` writes the report, then branches on `args.json`. `run_audit` still only returns CLEAN / DECAY.

**Recall probe.** `audit` on `examples/empty` with `--json`. Does stdout contain `"verdict": "ERROR"`?

Answer: No. `run_audit` raises `TranscriptError`. CLI prints `ERROR:` on stderr and returns `1`. No JSON object.

**Retrieve.** `src/constraintauditor/cli.py` · `audit.py` · `decay.py` (`markdown_timeline`) · `tests/test_examples.py` (`test_jsonl_decaying_fixture_locks_report`) · `examples/MATRIX.md`
