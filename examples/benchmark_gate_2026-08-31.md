# Benchmark gate paste — 2026-08-31 (Europe/Dublin)

Commands run on local tree before first public push.

```
pip install -e ".[dev]"
python -m pytest -q
# 16 passed

constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# exit 0

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# exit 2

python D:\live_memory\scripts\public_git_guard.py .
# PASS (Homayoun identity)
```

Field/external (§B): N/A for v0.1.
