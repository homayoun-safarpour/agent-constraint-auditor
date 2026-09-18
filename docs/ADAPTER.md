# Adapter notes — agent-loop-engine journals

`constraintauditor.journal.parse_loop_engine_journal` reads the append-only markdown journal shape used by [agent-loop-engine](https://github.com/homayoun-safarpour/agent-loop-engine).

## Expected shape

- Headings or bullet blocks that mark turns / decisions / tool events
- Constraint checks run as **predicates over those events**, not as an LLM score

## Gate wiring

```bash
constraint-auditor audit \
  --constraints constraints/agent.yaml \
  --transcript path/to/JOURNAL.md
# exit 0 = CLEAN, exit 2 = DECAY, exit 1 = ERROR (empty journal or invalid regex is not CLEAN)
```

## Forbid vs required patterns

| Mode | YAML | Meaning | Worked example |
| --- | --- | --- | --- |
| Forbid (default) | `forbid: true` | Match = decay | `examples/stable` (exit 0) · `examples/decaying` (exit 2) |
| Required | `forbid: false` | Missing match = decay | `examples/required_present` (exit 0) · `examples/required_missing` (exit 2) |
| ERROR (fail-closed) | n/a | No parseable dated events | `examples/empty` (exit 1) · `examples/headerless` (exit 1) |
| JSONL CLEAN | `--format jsonl` | One JSON object per line; no forbid match | `examples/jsonl_stable` (exit 0) |
| JSONL DECAY | `--format jsonl` | Forbid-match decay on JSONL events | `examples/jsonl_decaying` (exit 2) |
| JSONL ERROR | `--format jsonl` | Timestamp not `YYYY-MM-DD HH:MM` | `examples/jsonl_bad_timestamp` (exit 1) |

```bash
# Required pattern present → CLEAN
constraint-auditor audit \
  --constraints examples/required_present/constraints.yaml \
  --transcript examples/required_present/journal.md

# Required pattern missing → DECAY
constraint-auditor audit \
  --constraints examples/required_missing/constraints.yaml \
  --transcript examples/required_missing/journal.md

# Empty or headerless transcript → ERROR (not CLEAN)
constraint-auditor audit \
  --constraints examples/empty/constraints.yaml \
  --transcript examples/empty/journal.md
constraint-auditor audit \
  --constraints examples/headerless/constraints.yaml \
  --transcript examples/headerless/journal.md

# JSONL transcripts (same exit contract as markdown journals)
constraint-auditor parse-transcript --format jsonl examples/jsonl_stable/events.jsonl
constraint-auditor audit \
  --constraints examples/jsonl_stable/constraints.yaml \
  --transcript examples/jsonl_stable/events.jsonl \
  --format jsonl
# expect exit 0 CLEAN

constraint-auditor audit \
  --constraints examples/jsonl_decaying/constraints.yaml \
  --transcript examples/jsonl_decaying/events.jsonl \
  --format jsonl \
  --report /tmp/jsonl-decay.md
# expect exit 2 DECAY; report opens with Verdict: DECAY

constraint-auditor parse-transcript --format jsonl examples/jsonl_bad_timestamp/events.jsonl
constraint-auditor audit \
  --constraints examples/jsonl_bad_timestamp/constraints.yaml \
  --transcript examples/jsonl_bad_timestamp/events.jsonl \
  --format jsonl
# expect exit 1; timestamp not YYYY-MM-DD HH:MM is ERROR, not CLEAN
```

Use forbid rules for "never do X". Use required rules for "every event must still show Y" (for example `lint=PASS`). Empty or headerless journals must fail closed as exit `1`, never a free CLEAN. A dated `## YYYY-MM-DD HH:MM` heading with no body text or fields is ERROR (exit `1`), same as a timestamp-only JSONL object. JSONL fixtures under `examples/jsonl_stable` and `examples/jsonl_decaying` lock the same polarities for `--format jsonl`. A JSONL object without a non-empty string `timestamp` is ERROR (exit `1`). A JSONL `timestamp` of JSON `null`, `true`, `false`, or a number is the same ERROR. A JSONL `timestamp` that is not `YYYY-MM-DD HH:MM` is ERROR (exit `1`); `examples/jsonl_bad_timestamp` is the worked fixture (exit `1`). A JSONL timestamp with seconds (`YYYY-MM-DD HH:MM:SS`) is the same ERROR. A JSONL timestamp with a timezone suffix (`2026-08-11 09:00Z`) is the same ERROR. A JSONL timestamp with a numeric offset (`2026-08-11 09:00+00:00`) is the same ERROR. A JSONL timestamp with an inner double space between date and time is ERROR; a markdown `##` heading with that same inner double space still parses. A JSONL object with `timestamp` but neither `text` nor `fields` is ERROR (exit `1`), not CLEAN. A JSONL `fields` value that is not a mapping is ERROR (exit `1`). A JSONL `fields` mapping with numeric values still parses; those values are stringified. A JSONL line that is valid JSON but not an object is ERROR (exit `1`). An empty JSONL file parses to no events; `audit` and `parse-transcript` still ERROR (exit `1`) via `no parseable events`. A whitespace-only JSONL file is the same: blank lines are skipped, so parse returns no events and CLI still ERROR. A JSONL file with a UTF-8 BOM is ERROR (invalid JSONL). Extra JSONL object keys beyond `timestamp`, `text`, and `fields` are ignored. A JSONL `text` value that is not a string is treated as missing text. An empty JSONL `fields` mapping is treated as missing fields. Whitespace-only JSONL `text` with `fields` uses the fields body. Empty-string JSONL `text` with `fields` uses the fields body. JSONL `fields` keys stay strings; a digit key remains `1` as a string. A JSONL `fields` mapping with boolean values still parses; `true` becomes `True` and `false` becomes `False`. A JSONL `fields` mapping with list values still parses; a JSON array is stringified. A JSONL `fields` mapping with nested object values still parses; a nested JSON object is stringified. A JSONL `fields` mapping with an empty-string key still parses; that key is not missing fields. A JSONL `fields` mapping with a whitespace-only key still parses; the key is not stripped. A JSONL `fields` mapping with a whitespace-only value still parses; the value is not stripped. A JSONL `fields` mapping with an empty-string value still parses; that value is not missing fields. A JSONL `fields` mapping with a key containing a colon still parses; the key is not split. A JSONL `fields` mapping with a value containing a colon still parses; the value is not split. A JSONL `fields` mapping with two keys keeps insertion order; body lines follow that order. A JSONL object with non-empty `text` and `fields` uses the text body; fields still parse. A JSONL object line with trailing whitespace still parses; spaces after the closing brace are stripped. A JSONL object line ending in CRLF still parses; carriage returns are not invalid JSONL. A JSONL file with a blank line between objects still parses; the blank line is not invalid JSONL. A JSONL object line with leading whitespace still parses; spaces before the opening brace are stripped. A JSONL `#` comment line is ERROR (invalid JSONL); it is not skipped. A JSONL object line with trailing non-whitespace after the closing brace is ERROR (invalid JSONL); that extra text is not stripped. A JSONL object line with leading non-whitespace before the opening brace is ERROR (invalid JSONL); that prefix is not stripped. A JSONL object line with a trailing comma before the closing brace is ERROR (invalid JSONL); the comma is not ignored. A JSONL object line with single-quoted strings is ERROR (invalid JSONL); single quotes are not accepted. A JSONL object line with unquoted keys is ERROR (invalid JSONL); unquoted keys are not accepted. A JSONL object line with an unquoted string value is ERROR (invalid JSONL); unquoted values are not accepted.

## What this does not do

- Does not call a model to “judge” the agent
- Does not invent constraints — you declare them in YAML

## Verify

```bash
pip install -e ".[dev]"
python -m pytest -q
constraint-auditor check-constraints examples/stable/constraints.yaml
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
constraint-auditor audit --constraints examples/required_present/constraints.yaml --transcript examples/required_present/journal.md
constraint-auditor audit --constraints examples/empty/constraints.yaml --transcript examples/empty/journal.md
# expect exit 1
constraint-auditor audit --constraints examples/jsonl_stable/constraints.yaml --transcript examples/jsonl_stable/events.jsonl --format jsonl
# expect exit 0
constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --format jsonl
# expect exit 2
constraint-auditor audit --constraints examples/jsonl_bad_timestamp/constraints.yaml --transcript examples/jsonl_bad_timestamp/events.jsonl --format jsonl
# expect exit 1
```
