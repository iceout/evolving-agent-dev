# Case 0002: Over-Defensive Code

## Status

Open

## Evidence Type

`seed` - initial hypothesis. Does not count toward Stage 0 exit criteria until linked to a real session report or friction log entry.

## Category

- implementation
- review

## Scenario

Agent-written code tends to add many guards, fallback branches, catch wrappers, and validations even when callers or schemas already guarantee the input shape.

## Observed Behavior

The implementation looks safe at first glance, but becomes verbose and harder to read.

## Why It Feels Wrong

The code optimizes for appearing careful rather than being clear. Many branches do not correspond to realistic failures.

## Impact

- lower readability
- more branches to test and maintain
- duplicated validation logic
- hidden behavior through fallbacks
- larger surface area for bugs

## Initial Root Cause Guess

The agent has a bias toward defensive programming and lacks a boundary-based validation policy.

## Candidate Policy Change

Validate at untrusted boundaries. Avoid repeated defensive checks inside trusted internal calls unless there is a concrete reason.

## Candidate Evaluation

Give the agent a task where input is already validated by a schema. Expected behavior: internal functions stay simple and do not repeat type/null checks everywhere.

## Related Documents

- `docs/policies/implementation-style.md`
