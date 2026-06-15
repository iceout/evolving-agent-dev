# Evolving Agent Development

This project is not the agent implementation yet. It is the working system for discovering, recording, and refining how the agent should behave.

## Purpose

Build an evolvable development system before building the agent itself.

The core loop is:

```text
real usage -> friction captured -> root cause analyzed -> policy updated -> evaluation added -> next usage verifies improvement
```

## Current Process

`docs/process-v0.2.md` is the active Stage 0 process draft. Other artifacts should follow its routing and lifecycle rules.

Stage 0 is intentionally lightweight:

- Micro tasks do not need a session report, but useful friction must be captured in `docs/casebook/inbox.md`.
- Tasks with substantive code or document changes need a minimal session report.
- Reusable friction can become casebook entries.
- Repeated or high-impact rule hypotheses start as `proposed` policy notes.
- Stable defaults become `active` policies only after enough evidence.
- ADRs are for decisions with trade-offs, future constraints, or likely "why" questions.
- Evaluations are for high-signal behavior regressions; weak cases stay as evaluation candidates.

## Working Artifacts

- `docs/principles.md` - stable beliefs that guide the system.
- `docs/process-v0.2.md` - active draft of the development workflow.
- `docs/process-v0.1.md` - earlier process draft kept for history.
- `docs/session-reports/` - raw records for tasks with substantive changes.
- `docs/casebook/inbox.md` - append-only inbox for lightweight friction from micro tasks or scattered observations.
- `docs/casebook/` - reusable historical friction cases with context and traceability.
- `docs/policies/` - policy notes and active policies, each with explicit status and source links.
- `docs/decisions/` - Agent Decision Records explaining trade-offs and durable process decisions.
- `docs/evaluations/` - behavior-level regression cases or candidates for future agents.

## Current Stage

Stage 0: capture real discomfort and draft the process.

Do not rush into implementation. The first goal is to collect enough real cases to know what kind of agent should be built.

Exit Stage 0 only after:

- 3-5 real tasks have been run through the process.
- At least 10 friction items have been captured.
- At least 2 evaluation candidates have been identified.
- The top 3 repeated problem categories are visible.

If evaluation candidates are weak, continue Stage 0 instead of forcing low-quality evaluations.
