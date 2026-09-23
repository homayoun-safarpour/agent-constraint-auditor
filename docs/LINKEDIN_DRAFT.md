# LinkedIn draft (public-safe) - Cursor applied Claude DECAY paste 2026-09-23

Field pain first. No employer demand. No unpublished research.
Named-test locks (keep in this file): `nine-fixture matrix`, `0/2/0/2/1/1/0/2/1`, `examples/MATRIX.md`, `examples/jsonl_bad_timestamp`.

**What was wrong with the old paste:** it led with Ragas/DeepEval/Anthropic (me-too), hid the actual invention (fail-closed rule decay on *your* journal), used a jargon MATRIX string in the public lines, and was one dense paragraph. LinkedIn cuts after two lines. Hiring engineers do not parse `0/2/0/2/1/1/0/2/1`.

**What to imitate (shape, not copy):** Hamel/Eugene-style posts. Hook in line 1. White space. One command with real output. One honest limit. Repo URL. No "excited to share", no fake traction.

**Invention (true, narrow):** not a new eval framework. A CI gate that treats declared agent rules as a spec, scores decay over the transcript, and refuses to call an empty or invalid log CLEAN.

**Grok critic (HB-LI-CRIT-001):** Cursor direction kept. Wanted command+output earlier. Still showed the CLEAN run.

**Homi rewrite Accepted:** still CLEAN, still no clone URL, em dash, `[dev]` extra, no limit sentence.

**Claude (CLAUDE-LI-001):** re-ran the decaying fixture. Applied below. Hook and sibling line kept. Homayoun posts himself.

Internal MATRIX: `examples/MATRIX.md` nine-fixture matrix `0/2/0/2/1/1/0/2/1`. `examples/jsonl_bad_timestamp` is ERROR.

Paste verified 2026-09-23 on `examples/decaying/`: verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

---

Paste block (copy from the next line to the URL):

Your agent can break a rule you wrote down and still look busy.

That is a CI problem, not a chat complaint.

constraint-auditor reads two files: your rules as YAML, and the journal of what the agent did. No LLM in the loop.

Run it on the bundled journal where the rules start slipping:

git clone https://github.com/homayoun-safarpour/agent-constraint-auditor
cd agent-constraint-auditor && pip install -e .
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md

verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000

Exit 2 fails the CI job. Exit 0 is CLEAN. Exit 1 is ERROR, and an empty or unreadable log counts as ERROR, not as a pass.

The limit: it only checks rules you can write as a regex or a predicate. Whether the agent's work was good is a different question.

If you freeze human labels to watch the judge, that is judge-drift-sentinel (pip install judge-drift-sentinel). This repo is the sibling: did the agent still obey the spec over time.

Repo and worked fixtures:
https://github.com/homayoun-safarpour/agent-constraint-auditor
