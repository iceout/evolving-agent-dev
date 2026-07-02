# Idea Note Shape

Use this only when an idea-framing-loop session produces a reusable process lesson, future skill idea, non-trivial product/process decision, or handoff candidate, but does not need a full idea brief.

Default target path in real projects:

`.agent/idea-framing-notes.md`

Append one compact entry per idea.

## Entry Template

````markdown
## YYYY-MM-DD - <privacy-safe idea title>

### Context

- Idea mode: product/user idea / developer tool / process-agent behavior / code feature / research
- Trigger:
- Current workaround:

### Problem / Pain

What friction, opportunity, or repeated pattern prompted the idea?

### Framing Outcome

- Goal:
- Non-goals:
- Smallest useful version:
- Success criteria:

### Options Considered

- Minimal / low-risk:
- Stronger / more structured:
- Too-heavy / not recommended:

### Recommendation

What should be tried first, and why?

### Why This Matters For evolving-agent-dev

- skill idea:
- process lesson:
- evaluation/watchlist candidate:
- handoff to coding-review-loop:
- no action:

### Privacy Boundary

What was intentionally omitted or generalized?
````

## Batch Transfer

When several entries accumulate, the user can copy this file back to evolving-agent-dev for batch distillation. Treat transferred entries as external privacy-preserving evidence, not accepted internal Stage 0 dogfood evidence.

Treat these notes as local transfer artifacts by default; do not include them in product commits unless the user or target repo convention explicitly wants agent notes committed.
