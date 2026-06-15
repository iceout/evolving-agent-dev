# Session Report: <title>

## Goal

What were we trying to accomplish?

## Scope

- In scope:
- Out of scope:
- Acceptance criteria:

## Changes

What code, docs, policies, cases, or evaluations changed?

## Verification

Record real verification commands or paths and results.

```text
Command/path:
Result:
```

If verification could not be completed, use the failure rule:

- Attempted verification:
- Failure reason:
- Alternative verification:
- Remaining risk:
- Can claim complete? yes/no, with reason.

Do not use completion language if there was no real verification.

## Good

What should be kept or encouraged?

## Friction

Use `No notable friction.` only if nothing meaningful came up.

For each friction item:

```markdown
### <short title>

#### What happened

#### Why it felt wrong

#### Impact

#### Category

`testing` / `implementation` / `requirements` / `process` / `context` / `review` / `tooling`

#### Root cause guess

#### Proposed follow-up
```

## Artifact Routing

- Raw session facts stay in this report.
- Micro-task or scattered friction goes to `docs/casebook/inbox.md`.
- Reusable friction becomes a casebook entry.
- Repeated or high-impact rule hypotheses become `proposed` policy notes.
- Stable default behavior becomes an `active` policy.
- Decisions with trade-offs become ADRs.
- High-signal regressions become evaluations; weaker cases stay as evaluation candidates.

## Role Separation

Fill this when the task changes tests and implementation, fixes a failing test, crosses modules, changes public API/data structures, touches security/data/permissions/migrations, has unclear requirements, or review finds test-driven design pollution.

### Plan Decision

Goal, boundaries, acceptance criteria, and risk judgment.

### Test Responsibility

External behavior to verify; implementation details tests should not bind to.

### Implementation Responsibility

Implementation changes; explicit non-goals; confirmation that acceptance criteria were not lowered.

### Review Check

Test value, code simplicity, scope control, and verification result.

## Objections

Only record an objection when the issue would lower acceptance criteria, violate role boundaries, expand scope, block real verification, reveal a substantive conflict, or require Orchestrator/user trade-off.

```markdown
### Objection: <short title>

#### Type

`test` / `requirement` / `design` / `review` / `tooling`

#### Target

#### Problem

#### Evidence

#### Suggested Alternative

#### Recommendation
```

## Proposed Follow-up

- Policy note candidate:
- Casebook candidate:
- ADR needed? yes/no, with reason.
- Evaluation candidate? yes/no, with pass/fail idea.
