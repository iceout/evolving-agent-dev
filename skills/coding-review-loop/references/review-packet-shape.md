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

## Test Double Boundary Fidelity

For test doubles, state the boundary being faked.

Prefer faking the lowest practical external IO boundary instead of a repo-owned helper whose call contract is under test. Fakes should preserve the real call shape needed by the production path, especially for keyword-only parameters, chaining behavior, errors, and return-shape contracts.

If adding fake infrastructure, search existing tests for shared fakes before creating a local fake.

## Runnable Acceptance / Entrypoints

For requirements that promise dry-runs, shadow runs, reports, default scripts, CLIs, exports, or scheduled jobs, list the runnable entrypoints and defaults reviewers must check.

Include:

- script or command
- default parameters, phase, mode, or config
- expected output files, payload fields, report sections, or log markers
- matrix dimensions such as time windows, enabled flags, dry-run vs write mode, or shadow vs production mode
- whether the default entrypoint actually exercises the new behavior

## Semantic Liveness / Report Truthfulness

For action recommendations, report rows, enum-like values, or config-driven classifications, list how acceptance-critical values are produced, consumed, and tested.

Check:

- producer for each acceptance-critical action, status, enum value, or report field
- consumer, renderer, or downstream behavior that uses it
- behavior test showing the expected value is reachable
- negative test for invalid or misleading config labels when config drives behavior
- distinction between research/ablation output and actionable recommendation
- deferred features remain consistent across plan, code, warnings, docs, and tests

## Dataflow Contract Preservation

For time-windowed, streaming, paginated, batched, deduped, or source-filtered data paths, trace whether downstream callers preserve the contract.

Check:

- bounded queries are not widened by later lookups
- streaming or iterator APIs are not immediately materialized in batch paths
- dedupe/source-filter semantics stay tied to the source-of-truth helper
- caller-local state is used before adding a new source helper
- tests include a case that would fail if the caller widens, materializes, or recomputes from the wrong source

## Verification Plan

Record the real verification path: tests, lint/typecheck, manual runtime checks, production-like review, or explicit verification limits.

When changing runnable scripts, CLIs, jobs, default parameters, or report outputs, include existing tests for those entrypoints, not only newly added core logic tests.

## Requirement Traceability Checklist

For each P0/P1 or acceptance-critical requirement, map:

```text
requirement -> implementation path -> user-facing entrypoint/default config -> expected output/report fields -> verification command/test
```

If a requirement has no runnable entrypoint or verification command, mark it as an open risk before implementation or review approval.

## Implementation Trace

During or after implementation, map requirement -> changed artifact -> behavior test or verification -> cross-artifact check. For plan-only packets, leave this `N/A until implementation`.

## Independent Reviewer Checklist

List the few questions an independent reviewer should answer before approval.

## Open Questions / Risks

Record unresolved choices, accepted risks, rollout-only checks, or items that need user review before implementation.
