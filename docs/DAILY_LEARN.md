# Daily learning — 2026-10-18

**Skill.** `spec_name` is the YAML `name:`, copied onto the audit object. Not the folder. Not `constraint_id`.

**Why.** Thursday: `timestamp` joins the heading. Friday: `constraint_id` joins the rule. Saturday: `event_index` joins the event list. Sunday: `spec_name` joins the spec document. Journal decaying and JSONL decaying share the same three hits; the name is how you tell which YAML ran. Stdout hire line omits it.

**Worked example** (this repo).

```bash
constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --json
# exit 2
# spec_name=decaying-agent  (YAML `name: decaying-agent`, not examples/decaying/)

constraint-auditor audit --constraints examples/jsonl_decaying/constraints.yaml --transcript examples/jsonl_decaying/events.jsonl --json
# spec_name=jsonl-decaying-agent  — same 3 hits, different YAML name

constraint-auditor audit --constraints examples/decaying/constraints.yaml --transcript examples/decaying/journal.md --report /tmp/decay.md
# # Constraint decay report: decaying-agent

constraint-auditor check-constraints examples/decaying/constraints.yaml
# OK: decaying-agent (2 constraints)  — same name, compile only
```

**Recall probe.** Recite journal decaying `spec_name` vs JSONL decaying `spec_name`. Does stdout print it?

Answer: `decaying-agent` vs `jsonl-decaying-agent`. Stdout hire line does not. CLEAN is `stable-agent`. `parse-transcript` has no spec so no name. Do not pytest-lock this card; it is rewritten each morning.

**Retrieve.** `src/constraintauditor/audit.py` · `src/constraintauditor/spec.py` · `examples/decaying/constraints.yaml` · `examples/jsonl_decaying/constraints.yaml`
