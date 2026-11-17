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

Use behavior-level evaluation cases to test uncertain behavior hypotheses and
support effectiveness claims. Evaluation is not a prerequisite for every prompt
maintenance change; apply principle 11 to those changes.

## 10. The process should stay lightweight

The workflow should help development, not become bureaucracy. Prefer small records, clear decisions, and short feedback loops.

## 11. Maintain prompts and process rules as ordinary engineering changes

Simplifying, demoting, rewriting or deleting a prompt or process rule does not
require an A/B experiment or proof of effectiveness first. Maintainer review
and verification proportionate to the risk are sufficient. Keep changes
reviewable and preserve a recovery path, such as Git history and revert.

Review should establish either equivalent behavior or an explicit, acceptable
behavior change. Moving guidance to an on-demand reference can reduce its
visibility; removing a mandatory step can reduce the information collected.
Reversibility helps manage these trade-offs but does not replace verification.

A maintenance decision does not establish that a model has internalized a rule,
that the rule is ineffective, or that outcomes improved. Those claims require
their own evidence. Missing effectiveness evidence is not, by itself, a reason
to retain every existing rule.
