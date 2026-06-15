# Testing Policy Draft

## Intent

Tests should protect meaningful behavior and make future changes safer. Tests should not exist merely to satisfy a process ritual.

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

## Role Boundary Draft

- Test-writing agents may edit test files and test fixtures.
- Test-writing agents may not edit production implementation.
- Implementation agents may edit production code.
- Implementation agents may not edit tests to make them pass.
- If an implementation agent believes a test is wrong, it must submit a test objection.

## Test Objection Format

```markdown
## Test Objection

Test: <path or name>

Reason:

- why the test may be wrong or low-value
- what behavior should be tested instead
- whether the implementation or the test should change
```
