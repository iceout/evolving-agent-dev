# Principles

These principles should change slowly. Policies and prompts may change often, but they should trace back to these ideas.

## 1. The system must evolve from real usage

Do not design the agent only from theory. Real development sessions produce the best evidence.

## 2. Behavior matters more than ritual

TDD, reviews, planning, and role separation are tools. They are valuable only when they improve correctness, simplicity, and maintainability.

## 3. Tests should protect behavior, not implementation details

A good test should survive internal refactoring when user-visible behavior stays the same.

## 4. Simplicity is a feature

Prefer direct code. Avoid speculative abstractions, speculative options, and speculative defensive programming.

## 5. Boundaries should be explicit

Validation belongs at system boundaries: user input, files, network, database, subprocesses, model calls, and other unreliable external systems.

Trusted internal calls should not repeat the same defensive checks without a concrete reason.

## 6. Roles should reduce conflicts of interest

The agent that writes tests should not silently weaken implementation requirements. The agent that writes implementation should not silently weaken tests.

## 7. Every durable rule needs a traceable reason

A rule should point to a case, decision record, or evaluation. If the reason disappears, the rule should be reconsidered.

## 8. Discomfort is product data

When a workflow feels wrong, record the concrete situation. Do not immediately convert discomfort into a permanent rule.

## 9. Evaluation beats prompt guessing

Prompt changes should eventually be validated with behavior-level evaluation cases.

## 10. The process should stay lightweight

The workflow should help development, not become bureaucracy. Prefer small records, clear decisions, and short feedback loops.
