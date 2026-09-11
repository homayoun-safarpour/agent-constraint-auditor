---
name: Fixture or claim lock
about: Track a named exit-code claim or worked example
labels: docs
---

**Claim** (one sentence):

**Expected exit:** 0 / 2 / 1

**Command to reproduce:**

```bash
constraint-auditor audit --constraints examples/... --transcript examples/...
```

**Done when:** named pytest lock exists and `python -m pytest -q` is green.
