# Session Report: Smoke Test C Testing Policy

## Goal

Make a small substantive docs change to `docs/policies/testing-policy.md` clarifying that implementation-detail tests require a stated requirement.

Dogfood status: yes. This task used the installed `evolving-agent-process` skill for a real edit task.

Stage 0 evidence status: real task candidate. This is non-bootstrap dogfood work linked to a session report, but it should only count as Stage 0 evidence if later review accepts the task as substantive enough.

## Changes

- Added one sentence to the proposed testing policy's implementation-detail exception.
- Created this minimal session report.

## Verification

- `rg -n "stated requirement|implementation-detail test" docs/policies/testing-policy.md docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md` - confirmed the policy sentence and this report's status text.
- `git diff --check` - passed with no whitespace errors.
- `git diff -- docs/policies/testing-policy.md` - reviewed the one-sentence policy diff.
- `sed -n '1,120p' docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md` - reviewed this report after creation.

## Good

The skill routed a narrow docs edit into a minimal report without expanding into casebook, ADR, or evaluation work.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no; this updates an existing proposed policy.
- Casebook candidate: no.
- ADR needed? no; there is no new durable trade-off.
- Evaluation candidate? no; this does not create a new high-signal regression case.
