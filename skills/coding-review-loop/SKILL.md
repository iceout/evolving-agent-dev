---
name: coding-review-loop
description: "Use when planning, implementing, or reviewing non-trivial coding tasks in real code projects, not evolving-agent-dev process work, that need independent review, multi-round review, cross-agent handoff, a repo-local plan/review packet, plan-to-implementation traceability, or high-risk debugging/bad-case analysis. Trigger for public interfaces, hot paths, schema/contracts, data semantics, sensitive output, batch/action/export behavior, time windows, config/deployment, missed detections, wrong scores/selections, surprising outputs, or when the user asks to plan first or review before coding."
---

# Coding Review Loop

Use this skill for real code projects. It helps Codex make non-trivial plans reviewable, keep high-risk debugging grounded in evidence, and preserve traceability from plan to implementation and verification.

Do not create evolving-agent-dev artifacts in target repos. Follow the target repo's conventions for plans, docs, tests, and verification.

## Plan Artifact Rule

Keep plan artifacts lightweight and trigger-based.

- Small tasks may keep the plan in the final response.
- Medium-complexity tasks that need independent review, multi-round review, cross-agent handoff, or later implementation should create a repo-local plan/review packet.
- High-risk tasks should have the packet reviewed before implementation.
- Future subagent or automation review should consume packet artifacts, not raw chat context.
- Use existing repo conventions for plan docs. If unclear, ask; use a clearly repo-local temporary plan path only when the user asked for an artifact.

Read `references/review-packet-shape.md` only when a packet is needed. Do not load it for trivial tasks.

## Debug / Bad-Case Root-Cause Gate

For high-risk bad cases, missed detections, wrong scores/selections, surprising output, or similar examples, do not jump straight to a local patch.

First establish the evidence chain:

- observed symptom
- expected behavior
- affected contract
- candidate failure points
- source-of-truth data
- blockers/filters
- real verification path

If a quick patch is proposed before root cause is proven, label it as interim mitigation and keep it separate from final redesign. Avoid feature-specific heuristic patches unless explicitly justified and reviewed.

## Implementation Trace

After implementation, report or write a compact trace:

```text
plan constraint -> implementation anchor -> behavior test -> verification command
```

Distinguish local verification from production-like, rollout, or manual baseline verification. Do not claim strategy calibration from local tests alone.

## Review Behavior

When reviewing, put findings first.

For each major finding, classify it as one of:

- concrete project bug
- missing or ambiguous plan constraint
- implementation violation
- accepted exception
- out-of-scope item

Identify packet gaps when review required manual context reconstruction across plans, existing APIs, legacy behavior, config, tests, or user decisions.
