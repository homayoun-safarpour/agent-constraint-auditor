# Daily learning — 2026-09-10

**Skill.** `--report` is a projection of `AuditResult`, not of the transcript format. `write_report` calls `markdown_timeline(spec_name, decay, violations)`. JSONL vs journal only picks the parser. Same events + same YAML → same Verdict sentence.

**Why.** Exit `2` is the CI gate. The freeze that holds the claim is the third-person report: `Verdict: DECAY` plus "3 constraint violations, first at event 2." Markdown decaying is locked (`test_decaying_fixture_locks_force_push_line`). JSONL decaying is not (W29).

**Worked example** (this repo). Fields-only JSONL, same two `forbid: true` rules as `examples/decaying`.

```bash
constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl \
  --report /tmp/jsonl-decay.md
# verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000
# report opens: Verdict: DECAY
# The transcript records 3 constraint violations, first at event 2.
```

Event 2: `lint=FAIL` → `never_skip_lint`. Event 3: `lint=FAIL` plus `git push --force` → two rows. Count is constraint×event, not unique dirty events.

**Recall probe.** Drop `--format jsonl` (auto sniff). Does the report still open `Verdict: DECAY` with 3 violations? Why is Q4 rate `2.00` on a 4-event transcript?

Answer: Yes — first line starts with `{`, sniff = jsonl, same parse. Q4 is event 3 only (`(i * 4) // n`); that event fires two forbids, so rate = 2/1 = 2.00. Slope is Q4−Q1 = 2.000.

**Retrieve.** `src/constraintauditor/decay.py` (`markdown_timeline`, `_verdict_sentence`) · `audit.py` (`write_report`) · `examples/jsonl_decaying/` · `tests/test_examples.py` (`test_decaying_fixture_locks_force_push_line`) · `LOOP_STATE.md` NEXT TICK W29
