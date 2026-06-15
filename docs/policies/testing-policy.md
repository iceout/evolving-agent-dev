# Testing Policy Draft

Status: `proposed`

Source links:

- `docs/process-v0.2.md` - artifact routing, role separation, objection, and evaluation rules.
- `docs/casebook/0001-implementation-detail-tests.md` - implementation-detail tests as recurring friction.
- `docs/evaluations/behavior-cases.md` - behavior-level regression candidates E001, E002, and E004.
- `docs/decisions/ADR-0001-role-separation.md` - role boundary rationale.

## Intent

Tests should protect meaningful behavior and make future changes safer. Tests should not exist merely to satisfy a process ritual.

This policy is still `proposed`: use it as the default hypothesis, but keep source links and session evidence until the rule is promoted to `active`.

## Preferred Tests

Write tests for:

- user-visible behavior
- public API contracts
- bug regressions
- boundary behavior for files, network, database, subprocesses, model calls, and user input
- important security, performance, or compatibility constraints

## Suspicious Tests

Treat these as suspicious until justified:

- tests that assert a private method was called
- tests that assert an old method was not called
- tests that only prove a new helper exists
- tests that duplicate type-system guarantees
- tests that require changing when implementation changes but behavior does not
- tests that mock most of the system under test

## Test Value Questions

Before adding a test, answer:

1. What realistic regression would this catch?
2. If implementation changes but behavior stays the same, should this test still pass?
3. Does the test describe a requirement or an implementation choice?
4. Would a future maintainer understand the broken behavior from the failure?
5. Is this test cheaper to maintain than the risk it prevents?

## Implementation-Detail Exceptions

Testing implementation paths may be justified when the requirement is specifically about:

- avoiding a dangerous side effect
- preventing use of a deprecated or unsafe path
- enforcing a security boundary
- preventing a known performance regression
- preserving compatibility with an external contract

When using this exception, the test must state the reason in its name or nearby comment.

## Role Boundary

- Test-writing agents may edit test files and test fixtures.
- Test-writing agents may not edit production implementation.
- Implementation agents may edit production code.
- Implementation agents may not edit tests to make them pass.
- If an implementation agent believes a test is wrong, it must submit an objection only when the v0.2 objection trigger threshold is met.

## Test Objection Format

Use the general objection mechanism in `docs/process-v0.2.md`. A narrower test objection can be:

```markdown
## Test Objection

Test: <path or name>

Reason:

- why the test may be wrong or low-value
- what behavior should be tested instead
- whether the implementation, requirement, or test should change
```

## Promotion Criteria

Promote this policy from `proposed` to `active` only after future session reports show it prevents low-value tests without blocking useful regression coverage.
