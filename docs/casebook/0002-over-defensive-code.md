# Case 0002: Over-Defensive Code

## Status

Open

## Evidence Type

`seed` - initial hypothesis. Does not count toward Stage 0 exit criteria until linked to a real session report or friction log entry.

Note: a privacy-preserving external implementation observation now provides adjacent real external evidence for implementation-style friction, but this case remains seed evidence and does not make E003 accepted real evidence.

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

## Adjacent Real External Evidence

- `docs/casebook/inbox.md` records an external retention-window guard fix that worked and had tests, but split a simple rolling-window check into too many private helpers.
- The observation fits `implementation` / `over-abstraction`, with secondary `testing` / `test seam pollution`, because one production helper mainly existed to support monkeypatching current time in tests.
- This evidence is privacy-preserving and external. It does not count as an accepted internal Stage 0 dogfood task, does not create a new evaluation candidate, and does not make E003 accepted real evidence.

## Related Documents

- `docs/policies/implementation-style.md`
