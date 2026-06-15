# ADR-0001: Separate Test and Implementation Responsibilities

## Status

Proposed

## Context

Agent-assisted TDD can create conflicts of interest. If the same agent writes tests and implementation, it may unconsciously shape tests around its intended implementation. If an implementation agent can edit tests freely, it may weaken tests to make progress.

Observed concerns:

- tests written for implementation details
- implementation shaped to satisfy brittle tests
- tests changed to pass rather than to preserve requirements

## Decision

Use role separation as a default workflow:

- Test Agent writes behavior tests and fixtures.
- Dev Agent writes production implementation.
- Review Agent checks both test value and implementation simplicity.
- Orchestrator decides whether a failing run indicates wrong tests or wrong implementation.

Dev Agent must not directly edit tests. If it believes a test is wrong, it submits a Test Objection.

## Consequences

Benefits:

- reduces test weakening by implementation pressure
- makes test disputes explicit
- improves traceability of requirement changes

Costs:

- slower for trivial fixes
- requires an orchestrator decision path
- may feel heavy if applied to every small task

## Escape Hatch

For very small tasks, one agent may perform both roles if it records that role separation was skipped and why.

## Related Cases

- `docs/casebook/0001-implementation-detail-tests.md`

## Evaluation Plan

Create evaluation cases where tests are flawed or implementation-specific. Expected behavior: Dev Agent reports a Test Objection instead of editing tests directly.
