# Case 0001: Implementation-Detail Tests

## Status

Open

## Evidence Type

`seed` - initial hypothesis. Does not count toward Stage 0 exit criteria until linked to a real session report or friction log entry.

## Category

- testing
- process

## Scenario

While introducing a new method, an agent wrote or proposed a test that asserted the old method was not wrapped or called.

## Observed Behavior

The test may be technically correct, but it validates an internal implementation path rather than user-visible behavior.

## Why It Feels Wrong

The test can make future refactoring harder even when behavior remains correct. It may encourage implementation code to satisfy test structure instead of requirements.

## Impact

- brittle tests
- higher refactor cost
- possible design pollution
- test suite becomes a record of implementation choices rather than behavior requirements

## Initial Root Cause Guess

The agent treats TDD as a ritual and writes tests for new internal methods instead of testing behavior protected by those methods.

## Candidate Policy Change

Tests should not assert private method calls or non-calls unless the requirement is explicitly about side effects, security, performance, or removal of a dangerous/deprecated path.

## Candidate Evaluation

Prompt an agent to refactor an internal method while preserving behavior. Expected behavior: it updates behavior tests if needed, but does not add assertions about private method calls.

## Related Documents

- `docs/policies/testing-policy.md`
