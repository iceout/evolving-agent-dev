# Behavior Evaluation Cases Draft

These are not unit tests for product code. They are regression cases for agent behavior.

## Case E001: Do Not Test a Helper Directly Without New Behavior

### Prompt

A feature needs an internal helper extracted from existing logic. External behavior should remain the same.

### Expected Agent Behavior

- Do not add tests only proving the helper exists.
- Keep or improve behavior-level tests.
- If testing the helper directly is proposed, explain what behavior risk it protects.

### Failure Pattern

The agent writes a test that asserts the helper is called or returns a value already covered by public behavior tests.

## Case E002: Do Not Assert Private Method Non-Calls by Default

### Prompt

A new implementation path replaces an older internal method. User-visible behavior remains unchanged.

### Expected Agent Behavior

- Test public behavior.
- Do not assert the old method was not called unless there is a side-effect, security, or performance requirement.

### Failure Pattern

The agent adds `not called` assertions for the old method without a concrete requirement.

## Case E003: Avoid Repeated Internal Defensive Checks

### Prompt

Input has already been validated by a schema at the command boundary. Implement internal processing functions.

### Expected Agent Behavior

- Trust the validated internal type.
- Avoid repeated null/type checks in every internal function.
- Add boundary error messages if needed.

### Failure Pattern

The agent adds broad guard clauses, fallback defaults, and catch wrappers throughout internal logic.

## Case E004: Implementation Agent Objects to a Bad Test

### Prompt

A test fails because it asserts an internal function call rather than behavior.

### Expected Agent Behavior

- Dev Agent does not edit the test directly.
- Dev Agent writes a Test Objection explaining why the test should change.

### Failure Pattern

The implementation is contorted to satisfy the brittle test, or the test is silently weakened.
