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

Dev Agent must not silently weaken or rewrite tests to make progress. If it believes a test is wrong, it follows the v0.2 objection threshold: submit an objection only when the issue would lower acceptance criteria, violate role boundaries, expand scope, block real verification, reveal a substantive conflict, or require Orchestrator/user trade-off.

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

For very small tasks, one agent may perform both roles if the v0.2 role separation triggers do not apply. If a trigger applies, record the minimal role separation sections instead of creating separate agents by default.

## Related Cases

- `docs/casebook/0001-implementation-detail-tests.md`

## Evaluation Plan

Create evaluation cases where tests are flawed or implementation-specific. Expected behavior: Dev Agent does not edit tests directly, and reports a Test Objection only when the v0.2 objection trigger threshold is met.
