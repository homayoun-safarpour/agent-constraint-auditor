# Daily learning — 2026-09-09

**Skill.** `detect_format` is a first-line sniff, not a heading scan. `HEADER_RE` is `^## YYYY-MM-DD HH:MM$` *without* `re.MULTILINE`, so `HEADER_RE.search(sample[:2000])` only hits when the *whole sample* is a lone dated heading. Titled journals (`examples/stable/journal.md` starts `# Stable…`) miss that branch. JSONL wins only if the first non-empty line starts with `{`; otherwise default `journal`. `--format jsonl|journal` skips sniffing.

**Why.** Hire signal: fail-closed parser, explicit format, no silent empty CLEAN. W24 added matching `--format` on `audit` and `parse-transcript` because sniffing is not a classifier. W27 (JSONL DECAY fixture) should start with `{` or lock `--format jsonl`. Same YAML as `examples/decaying`; format only picks the parser.

**Worked example** (this repo).

```bash
constraint-auditor parse-transcript examples/jsonl_stable/events.jsonl
# auto → jsonl (line starts with {); OK: 4 events

constraint-auditor parse-transcript --format journal examples/jsonl_stable/events.jsonl
# markdown parser, no ## headers → ERROR exit 1 (not CLEAN)

constraint-auditor parse-transcript examples/stable/journal.md
# first line is # not { → journal; OK: 4 events
```

`run_audit` / CLI: `auto` calls `detect_format`; `jsonl`/`journal` force `parse_jsonl_transcript` vs `parse_loop_engine_journal`. Zero events → `TranscriptError` → exit 1.

**Recall probe.** `audit --format journal --constraints examples/jsonl_stable/constraints.yaml --transcript examples/jsonl_stable/events.jsonl`. Exit 0, 2, or 1? Does `detect_format` classify `examples/stable/journal.md` via `HEADER_RE` matching `## 2026-08-11 09:00`?

Answer: exit **1** (ERROR) — journal parser finds no headers, 0 events, fail-closed. And **no** — `HEADER_RE.search` does not see mid-file headings; the file is `journal` because the first line is not `{`.

**Retrieve.** `src/constraintauditor/journal.py` (`detect_format`, `HEADER_RE`) · `audit.py` · `cli.py` · `examples/jsonl_stable/` · `LOOP_STATE.md` NEXT TICK W27
