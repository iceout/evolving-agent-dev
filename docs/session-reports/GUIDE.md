# Session Report Guide

Use `TEMPLATE.md` as the minimal report. Add the sections below only when their triggers apply.

## Verification Failure

Trigger: real verification could not be completed.

```markdown
## Verification Failure

- Attempted verification:
- Failure reason:
- Alternative verification:
- Remaining risk:
- Can claim complete? yes/no, with reason.
```

Do not use completion language if there was no real verification.

## Artifact Routing

Trigger: a session produces friction, policy, casebook, ADR, or evaluation follow-up.

- Raw session facts stay in the session report.
- Micro-task or scattered friction goes to `docs/casebook/inbox.md`.
- Reusable friction becomes a casebook entry.
- Repeated or high-impact rule hypotheses become `proposed` policy notes.
- Stable default behavior becomes an `active` policy.
- Decisions with trade-offs become ADRs.
- High-signal regressions become evaluations; weaker cases stay as evaluation candidates.

## Role Separation

Trigger: the task changes tests and implementation, fixes a failing test, crosses modules, changes public API/data structures, touches security/data/permissions/migrations, has unclear requirements, or review finds test-driven design pollution.

```markdown
## Role Separation

### Plan Decision
Goal, boundaries, acceptance criteria, and risk judgment.

### Test Responsibility
External behavior to verify; implementation details tests should not bind to.

### Implementation Responsibility
Implementation changes; explicit non-goals; confirmation that acceptance criteria were not lowered.

### Review Check
Test value, code simplicity, scope control, and verification result.
```

## Objections

Trigger: the issue would lower acceptance criteria, violate role boundaries, expand scope, block real verification, reveal a substantive conflict, or require Orchestrator/user trade-off.

```markdown
## Objections

### Objection: <short title>

#### Type

`test` / `requirement` / `design` / `review` / `tooling`

#### Target

#### Problem

#### Evidence

#### Suggested Alternative

#### Recommendation
```

Ordinary local corrections, naming adjustments, and obvious bug fixes do not need objections.
