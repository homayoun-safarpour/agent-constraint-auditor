# LinkedIn draft (public-safe) — restyle 2026-09-23

Field pain first. No employer demand. No unpublished research.
Named-test locks (keep in this file): `nine-fixture matrix`, `0/2/0/2/1/1/0/2/1`, `examples/MATRIX.md`, `examples/jsonl_bad_timestamp`.

**What was wrong with the old paste:** it led with Ragas/DeepEval/Anthropic (me-too), hid the actual invention (fail-closed rule decay on *your* journal), used a jargon MATRIX string in the public lines, and was one dense paragraph. LinkedIn cuts after two lines. Hiring engineers do not parse `0/2/0/2/1/1/0/2/1`.

**What to imitate (shape, not copy):** Hamel/Eugene-style posts. Hook in line 1. White space. One command with real output. One honest limit. Repo URL. No "excited to share", no fake traction.

**Invention (true, narrow):** not a new eval framework. A CI gate that treats declared agent rules as a spec, scores decay over the transcript, and refuses to call an empty or invalid log CLEAN.

Internal MATRIX: `examples/MATRIX.md` nine-fixture matrix `0/2/0/2/1/1/0/2/1`. `examples/jsonl_bad_timestamp` is ERROR.

---

Paste block (copy from the next line to the URL):

Your agent can break a rule you wrote down and still look busy.

That is a CI problem, not a chat complaint.

constraint-auditor takes two files: a YAML spec of the rules, and the journal (or JSONL) of what the agent actually did. No LLM in the loop. Regex and predicates only.

Exit 0 CLEAN.
Exit 2 DECAY (rule broke; you get when and how fast).
Exit 1 ERROR (empty log, bad JSONL, timestamp not YYYY-MM-DD HH:MM). Empty is not a free pass.

One command:

pip install -e ".[dev]"
constraint-auditor audit --constraints examples/stable/constraints.yaml --transcript examples/stable/journal.md

verdict=CLEAN exit=0 violations=0 first_index=None slope=0.000

If you freeze human labels to watch the *judge*, that is judge-drift-sentinel (`pip install judge-drift-sentinel`). This repo is the sibling: did the *agent* still obey the spec over time.

Repo and worked fixtures:
https://github.com/homayoun-safarpour/agent-constraint-auditor
