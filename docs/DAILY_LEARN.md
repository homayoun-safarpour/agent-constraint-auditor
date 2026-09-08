# Daily learning  -  2026-09-08

**Skill.** JSONL still matches on `event.text`. Missing or blank `text` is filled from `fields` as `- key: value` lines (`_text_from_fields`). A non-empty `text` wins; the field map is then unused by `check_event`.

**Why.** W22 added `--format jsonl` / `{` auto-detect. Same hire-facing gate as markdown journals: regex over a declared spec, not an LLM judge. Empty or invalid JSONL is ERROR on `audit` (exit `1`). `parse-transcript` still prints `OK: 0 events` and exits `0` (W23).

**Worked example** (this repo). Fields-only JSONL with `lint=FAIL` is DECAY; empty JSONL is ERROR.

```bash
python -m pytest -q tests/test_cli.py::test_audit_jsonl_forbid_match_exit_2
# {"timestamp": "...", "fields": {"gates": "lint=FAIL"}}
# body = "- gates: lint=FAIL"; forbid match; audit exit 2

python -m pytest -q tests/test_cli.py::test_audit_jsonl_invalid_or_empty_exit_1
# empty or invalid JSONL -> audit exit 1

constraint-auditor parse-transcript examples/empty/journal.md
# today: OK: 0 events, exit 0 (dry-run; W23 still open)
```

`detect_format`: `HEADER_RE` in the first 2k chars -> journal; else first non-empty line starting `{` -> jsonl; else journal.

**Recall probe.** Line: `{"timestamp": "2026-08-11 09:00", "text": "- gates: lint=PASS", "fields": {"gates": "lint=FAIL"}}`. Spec: `pattern: "lint=FAIL"`, `forbid: true`. CLEAN or DECAY?

Answer: CLEAN. Non-empty `text` is the match surface. `fields` is not searched.

**Retrieve.** `src/constraintauditor/journal.py` (`parse_jsonl_transcript`, `detect_format`) · `audit.py` · `tests/test_cli.py` · `LOOP_STATE.md` NEXT TICK (W23)
