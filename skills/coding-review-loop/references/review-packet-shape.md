# Review Packet Shape

## Purpose

This is a lightweight review target and handoff artifact for real code projects, not a longer prompt. Use it only when a task needs independent review, multi-round review, cross-agent handoff, later implementation, or high-risk implementation review.

Small tasks do not need a packet. Sections are optional; mark `N/A` with a reason when a section is not applicable. Future subagent or automation review should consume packet artifacts, not raw chat context.

## Goal

What outcome should the task produce?

## Non-goals

What is intentionally out of scope?

## User Decisions and Exceptions

Record explicit user choices, accepted exceptions, privacy/output exceptions, and decisions reviewers should not reopen unless new evidence appears.

## Risk Surfaces

List relevant surfaces, such as public interface, hot path, schema/contract, data semantics, sensitive output, batch/action/export, time/window, config/deployment, or multi-module docs/tests changes.

## Debug / Bad-Case Evidence Chain

For a bad case, missed detection, wrong score/selection, surprising output, or similar example, capture observed symptom, expected behavior, affected contract, candidate failure points, source-of-truth data, blockers/filters, and real verification path.

## Reviewable Constraints

State constraints the implementation or review must preserve. Prefer bullets that can be checked against code, tests, docs, or runtime behavior.

## Task-Specific Contracts

Include only relevant contracts; mark others `N/A` with a reason.

- Collection/cardinality/counting.
- Failure/status/degraded behavior.
- Schema/API/output contract.
- Time/window semantics.
- Privacy/sensitive output.
- Source-of-truth/proxy/fallback.
- Mitigation vs final redesign.

## Reuse / Adapter Rationale

Name the existing helper, builder, adapter, serializer, guard, or pattern being reused. If adding a new one, explain the distinct responsibility and why existing same-concern code does not fit.

## Required Behavior Tests

List behavior-level tests or manual checks required to prove the contract. Avoid implementation-detail assertions unless explicitly justified.

## Verification Plan

Record the real verification path: tests, lint/typecheck, manual runtime checks, production-like review, or explicit verification limits.

## Implementation Trace

During or after implementation, map requirement -> changed artifact -> behavior test or verification -> cross-artifact check. For plan-only packets, leave this `N/A until implementation`.

## Independent Reviewer Checklist

List the few questions an independent reviewer should answer before approval.

## Open Questions / Risks

Record unresolved choices, accepted risks, rollout-only checks, or items that need user review before implementation.
