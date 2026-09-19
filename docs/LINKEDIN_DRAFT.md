# LinkedIn draft (public-safe) — week close 2026-09-20

Field pain first. No employer demand language. No unpublished research.

**Angle:** golden set → frozen floor → CI exit 0/2.

The field already has the front of that chain. [Ragas](https://github.com/explodinggradients/ragas) is metrics plus synthetic gold. [DeepEval](https://github.com/confident-ai/deepeval) is pytest-style agent/RAG checks; LangChain even published a [CI pipeline example](https://github.com/langchain-ai/cicd-pipeline-example). Anthropic's [building effective agents](https://www.anthropic.com/engineering/building-effective-agents) note is the same idea as their [agent cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents): a loop with a stop condition, not a one-shot walkthrough. Walkthroughs like [sentinel-agent](https://github.com/armanavasthi/sentinel-agent) (LangGraph + MCP + RAGAS) show people wiring those pieces together.

What still fails in production is the last arrow. Teams generate gold, then let the set drift, or they score it in a notebook that never fails the build.

So the sentence is: **golden set → pin it → run it in CI → exit 0 or 2 tells you what moved.**

I do not wrap Ragas. This week I closed a narrower instrument, [constraint-auditor](https://github.com/homayoun-safarpour/agent-constraint-auditor): your YAML rules against your journal or JSONL. Nine fixtures. Exits `0` CLEAN, `2` DECAY, `1` ERROR. Empty input and a JSONL timestamp that is not `YYYY-MM-DD HH:MM` (`examples/jsonl_bad_timestamp`) are ERROR, not a free pass. [rag-eval](https://github.com/homayoun-safarpour/rag-eval-service) does the same job for retrieval floors (frozen floor + baseline).

Fork path: README first screen is pip plus one CLEAN audit. `examples/MATRIX.md` is the nine worked exits (0/2/0/2/1/1/0/2/1).

---

Paste block:

Long-horizon agents can drop the rules you wrote down and still look busy. The missing piece is not another metric library. It is a golden set you freeze, then a CI exit that moves when the set does.

Ragas covers metrics and synthetic gold. DeepEval (and LangChain's CI example) puts evals next to pytest. Anthropic's agent notes are about a loop with a stop, not a one-shot walkthrough. I ship the last arrow: pin the gold, fail the build on decay.

constraint-auditor audits your transcript against your YAML spec (regex/predicate, not an LLM judge). Exit 0 CLEAN, 2 DECAY, 1 ERROR. This week the nine-fixture matrix still returns 0/2/0/2/1/1/0/2/1.

https://github.com/homayoun-safarpour/agent-constraint-auditor
