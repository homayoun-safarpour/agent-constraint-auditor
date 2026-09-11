# Contributing

Public repo: https://github.com/homayoun-safarpour/agent-constraint-auditor

This is a narrow CLI. Prefer a failing named test and a worked fixture under `examples/` over a new subsystem.

## Local loop

```bash
pip install -e ".[dev]"
python -m pytest -q
python -m ruff check .
constraint-auditor --version
```

Exit contract: `0` CLEAN, `2` DECAY, `1` ERROR. Empty, headerless, or empty JSONL transcripts must stay ERROR.

Fixture matrix: [examples/MATRIX.md](examples/MATRIX.md).

## Pull requests

1. One change (docs lock, fixture, or CLI behaviour).
2. Named pytest lock if you add a README or adapter claim.
3. Open a PR against `main`. Do not leave work only on a long-lived branch.

Issues: use the template. Close the issue from the PR when the claim is locked.
