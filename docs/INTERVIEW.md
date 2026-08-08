# Interview talking points : agent-constraint-auditor

## Three questions

1. **How is this different from agentevals / generic eval harnesses?**
   Narrow instrument - audits *your* declared constraints against *your* transcript over time; deterministic, no LLM judge in the loop.

2. **How does it compose with your other repos?**
   Reads agent-loop-engine journals natively; exit `0`/`2` plugs into `--gate`; sentinel handles judge drift, auditor handles agent rule drift.

3. **What does exit 2 mean in CI?**
   Measurable constraint decay - fail the build, repair before new feature work (same contract family as sentinel JUDGE_DRIFT).

## 2-min demo

```bash
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md
# exit 0
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md
# exit 2
```

## One limitation

v0.1 uses declared constraints and parsed events - it does not infer hidden policies from free-form chat without a spec.
