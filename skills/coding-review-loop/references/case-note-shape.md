# Case Note Shape

Use this only when a coding-review-loop task produces notable process friction, reusable review misses, packet gaps, verification gaps, or evaluation candidates.

Default target path in real projects:

`.agent/coding-review-loop-cases.md`

Append one compact entry per case.

## Entry Template

````markdown
## YYYY-MM-DD - <privacy-safe title>

### Context

- Task type:
- Skill used: coding-review-loop
- Risk surfaces:
- Phase: planning / implementation / review / review-fix / follow-up review

### What Happened

Privacy-safe summary. Avoid private paths, user data, credentials, customer names, sensitive payloads, and large code excerpts.

### Why It Mattered

- Impact:
- What reviewer/user found:
- What the original packet or agent missed:

### Pattern Tags

`review-packet` / `entrypoint` / `verification` / `reuse-scan` / `source-of-truth` / `fallback` / `test-double` / `review-fix` / `plan-trace` / `cross-artifact`

### Trace

```text
expected behavior -> missed implementation/review point -> detection method -> fix direction
```

### Verification Gap

- Expected verification:
- Actual verification:
- Missing command/test/manual check:

### Privacy Boundary

What was intentionally omitted or generalized?

### Suggested Routing Back To evolving-agent-dev

- inbox:
- casebook candidate:
- skill refinement candidate:
- evaluation watchlist candidate:
- no action:
````

## Batch Transfer

When several entries accumulate, the user can copy this file back to evolving-agent-dev for batch distillation. Treat transferred entries as external privacy-preserving evidence, not accepted internal Stage 0 dogfood evidence.

Treat these notes as local transfer artifacts by default; do not include them in product commits unless the user or target repo convention explicitly wants agent notes committed.
