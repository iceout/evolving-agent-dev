# Case 0003: Sandboxed Execution Unverified

## Status

Open

## Evidence Type

`real tooling/process friction` - repeated caveat from smoke testing and accepted Stage 0 dogfood reports. This is not an agent behavior evaluation.

## Category

- tooling
- process

## Scenario

Codex dogfood tasks ran successfully only after using `--dangerously-bypass-approvals-and-sandbox` because sandboxed execution could not be verified in this environment.

## Observed Behavior

The skill loaded and the requested process behavior was validated, but the runs did not prove behavior under normal sandboxed Codex execution.

## Why It Feels Wrong

Dogfood evidence can look stronger than it is if the runtime caveat is not stated next to the evidence. The skill behavior is useful evidence, but sandbox compatibility remains unknown.

## Impact

- Accepted dogfood tasks need a caveat until a sandboxed run succeeds.
- Smoke and dogfood results should not be treated as proof of sandboxed execution.
- Future process reviews need to distinguish skill behavior from environment/tooling limitations.

## Root Cause Guess

The local environment cannot initialize the Codex Linux sandbox; the smoke report recorded `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted` before rerunning with `--dangerously-bypass-approvals-and-sandbox`.

## Current Handling

Record that sandboxed execution remains unverified in dogfood reports and the Stage 0 tracker. Do not treat this as a policy, ADR, or evaluation candidate unless a later task exposes an agent behavior regression or a durable process decision.

## Related Documents

- `docs/session-reports/2026-06-15-codex-skill-smoke-tests.md`
- `docs/session-reports/2026-06-15-skill-install-flow-clarification.md`
- `docs/session-reports/2026-06-15-evaluation-case-metadata.md`
- `docs/session-reports/2026-06-15-stage0-progress-tracker.md`
- `docs/stage0-progress.md`
