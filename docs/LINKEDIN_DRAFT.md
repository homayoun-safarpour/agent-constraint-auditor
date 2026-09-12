# LinkedIn draft (public-safe) — agent-constraint-auditor

Field pain first. No employer demand language. No unpublished research.

1. Long-horizon agent loops can drop the rules you wrote down and still look busy - the transcript has no fail-closed check.
2. I keep a narrow public CLI that audits *your* journal or JSONL events against *your* YAML constraint spec (regex/predicate, not an LLM judge).
3. Exit contract: `0` CLEAN, `2` DECAY, `1` ERROR. Empty, headerless, or empty JSONL is ERROR, not a free CLEAN.
4. This week locked markdown and JSONL polarities in fixtures (stable/decaying + jsonl_stable/jsonl_decaying) with named `--report` verdicts.
5. Fork path: README Quickstart + `examples/MATRIX.md` (eight worked exits), `pip install -e ".[dev]"`, under 30 minutes.

Repo: https://github.com/homayoun-safarpour/agent-constraint-auditor
