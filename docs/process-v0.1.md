# Agent Development Process v0.1

This is a draft workflow for designing an evolvable coding agent. It is intentionally lightweight.

## Goal

Create a development system that learns from real usage before implementing a new agent.

The process optimizes for:

- traceable history
- behavior-focused tests
- simple implementation
- role clarity
- fast feedback
- continuous improvement

## Main Loop

```text
Use an agent on real work
  -> record friction
  -> classify the problem
  -> identify root cause
  -> propose a policy or workflow change
  -> add an evaluation case when useful
  -> verify in future sessions
```

## Stage 0: Capture

During real usage, record concrete moments of discomfort.

Capture:

- what the agent was asked to do
- what it actually did
- why it felt wrong
- whether the result was technically correct but undesirable
- whether the issue affected tests, implementation, process, context, or review

Do not over-generalize too early. One case is evidence, not a universal law.

## Stage 1: Classify

Assign one or more categories:

- `testing`: low-value tests, implementation-detail tests, mock abuse, coverage theater
- `implementation`: over-defensive code, verbosity, over-abstraction, YAGNI violations
- `process`: wrong role edited wrong artifact, skipped verification, expanded scope
- `context`: ignored project conventions, forgot prior decisions, lacked domain facts
- `review`: missed design issues, approved brittle tests, focused only on syntax
- `tooling`: missing tool, weak command integration, poor observability

## Stage 2: Diagnose

Before changing a prompt, identify the likely root cause:

- prompt wording
- role boundary
- workflow order
- missing context
- weak review checklist
- missing evaluation
- human instruction ambiguity
- tool limitation

## Stage 3: Decide

For recurring or high-impact issues, write an Agent Decision Record.

A decision should include:

- context
- decision
- consequences
- escape hatch
- related cases
- evaluation plan

## Stage 4: Update

Possible updates:

- revise a policy
- revise a playbook
- add or change a role boundary
- add review checklist items
- add a behavior evaluation case
- change a prompt only after the desired behavior is clear

## Stage 5: Evaluate

Turn important cases into behavior-level evaluations.

Example evaluations:

- Given a request to introduce a helper, the agent should not write a test only for the helper if no new behavior exists.
- Given a refactor where behavior is unchanged, the agent should not assert private method calls.
- Given internal functions already protected by a schema boundary, the agent should not repeat defensive type checks everywhere.

## Session Closeout

At the end of any meaningful agent-assisted task, write a short session report:

```markdown
# Session Report: <title>

## Goal

## What Happened

## Good Behavior

## Friction

## Root Cause Guess

## Proposed Change

## Follow-up Evaluation
```

## Change Discipline

Do not add permanent rules from a single weak signal.

Use this threshold:

- one case: record it
- two similar cases: propose a policy note
- three similar cases or one severe case: create a decision record and evaluation

## Current Open Questions

- How strict should role separation be between test and implementation agents?
- When is implementation-detail testing justified?
- How should the system detect over-defensive code automatically?
- What is the minimum useful session report?
- Which parts should be automated first, and which should remain human-reviewed?
