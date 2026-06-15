# Evolving Agent Development

This project is not the agent implementation yet. It is the working system for discovering, recording, and refining how the agent should behave.

## Purpose

Build an evolvable development system before building the agent itself.

The core loop is:

```text
real usage -> friction captured -> root cause analyzed -> policy updated -> evaluation added -> next usage verifies improvement
```

## Working Artifacts

- `docs/principles.md` - stable beliefs that guide the system.
- `docs/process-v0.1.md` - current draft of the development workflow.
- `docs/policies/` - concrete policies for testing, implementation, review, and role boundaries.
- `docs/playbooks/` - task workflows for feature work, bug fixes, refactors, and retrospectives.
- `docs/casebook/` - historical friction cases with context and traceability.
- `docs/decisions/` - Agent Decision Records explaining why process rules exist.
- `docs/evaluations/` - behavior-level regression cases for future agents.
- `docs/session-reports/` - per-session development reports and retrospectives.

## Current Stage

Stage 0: capture real discomfort and draft the process.

Do not rush into implementation. The first goal is to collect enough real cases to know what kind of agent should be built.
