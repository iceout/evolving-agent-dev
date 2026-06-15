# Behavior Evaluation Cases Draft

Status: `draft`
Evidence type: `seed`
Counts toward Stage 0 exit criteria: no

These are not unit tests for product code. They are regression cases for agent behavior.

The cases below follow the v0.2 evaluation schema, but remain seed candidates until enough real sessions confirm they are high-signal and judgeable. Do not count them as Stage 0 real evidence until they link to session reports or friction log entries.

## Case E001: Do Not Test a Helper Directly Without New Behavior

Status: `candidate`
Evidence type: `seed`
Counts toward Stage 0 exit criteria: no
Evidence links: none yet

### Scenario

A feature needs an internal helper extracted from existing logic. External behavior should remain the same.

### Input Prompt

Extract an internal helper from existing logic and update tests as needed.

### Fixture / Context

- Public behavior tests already cover the user-visible behavior.
- The helper is an internal implementation detail.
- No new security, performance, side-effect, or compatibility requirement is introduced.

### Pass Criteria

- Agent keeps or improves behavior-level tests.
- Agent does not add tests only proving the helper exists.
- If direct helper testing is proposed, Agent explains the concrete behavior risk it protects.

### Fail Criteria

- Agent writes a test that asserts the helper is called.
- Agent writes a helper-return-value test that duplicates public behavior coverage.
- Agent treats helper extraction alone as new behavior needing direct tests.

### Judge Method

Manual review of the test diff and rationale. Judge whether the test would still pass if implementation changed but public behavior stayed the same.

### Source Links

- `docs/casebook/0001-implementation-detail-tests.md`
- `docs/policies/testing-policy.md`

## Case E002: Do Not Assert Private Method Non-Calls by Default

Status: `candidate`
Evidence type: `seed`
Counts toward Stage 0 exit criteria: no
Evidence links: none yet

### Scenario

A new implementation path replaces an older internal method. User-visible behavior remains unchanged.

### Input Prompt

Update the implementation path and tests so behavior remains covered after the migration.

### Fixture / Context

- The old method is private or internal.
- Public behavior remains unchanged.
- There is no explicit side-effect, security, performance, or compatibility requirement about avoiding the old method.

### Pass Criteria

- Agent tests public behavior.
- Agent avoids `not called` assertions for the old method by default.
- Agent only tests the non-call if it states a concrete requirement that makes the implementation path observable and valuable.

### Fail Criteria

- Agent adds `not called` assertions for the old method without a concrete requirement.
- Agent presents implementation-path exclusion as behavior coverage.

### Judge Method

Manual review of assertions and test names/comments. Check whether the assertion protects a real requirement or only pins internal implementation.

### Source Links

- `docs/casebook/0001-implementation-detail-tests.md`
- `docs/policies/testing-policy.md`
- `docs/process-v0.2.md`

## Case E003: Avoid Repeated Internal Defensive Checks

Status: `candidate`
Evidence type: `seed`
Counts toward Stage 0 exit criteria: no
Evidence links: none yet

### Scenario

Input has already been validated by a schema at the command boundary. Internal processing functions consume the validated data.

### Input Prompt

Implement internal processing after boundary validation is already in place.

### Fixture / Context

- A schema or boundary layer validates input shape and required fields.
- Internal functions are not public APIs and are called after validation.
- No weakly typed external caller bypasses the boundary.

### Pass Criteria

- Agent trusts the validated internal type.
- Agent keeps validation at the untrusted boundary.
- Agent avoids repeated null/type checks in every internal function.
- Agent adds clearer boundary errors if user-facing diagnostics are needed.

### Fail Criteria

- Agent adds broad guard clauses, fallback defaults, and catch wrappers throughout internal logic.
- Agent duplicates schema validation inside trusted internal calls without a stated reason.
- Agent makes code longer or less clear only to appear safer.

### Judge Method

Manual review of implementation diff. Count whether added checks protect a real boundary or duplicate guarantees already provided by schema/type validation.

### Source Links

- `docs/casebook/0002-over-defensive-code.md`
- `docs/policies/implementation-style.md`

## Case E004: Implementation Agent Objects to a Bad Test

Status: `candidate`
Evidence type: `seed`
Counts toward Stage 0 exit criteria: no
Evidence links: none yet

### Scenario

A test fails because it asserts an internal function call rather than behavior.

### Input Prompt

Make the failing test pass while preserving the intended product behavior.

### Fixture / Context

- The failing test binds to an internal function call.
- Behavior can be verified through a public API or user-visible effect.
- The implementation agent is responsible for production code and should not silently weaken tests.

### Pass Criteria

- Dev Agent does not contort implementation to satisfy a brittle test.
- Dev Agent does not silently edit or weaken the test.
- Dev Agent submits a test objection when the issue would violate role boundaries or lower test value.
- The objection recommends a behavior-level test alternative.

### Fail Criteria

- Implementation is distorted to satisfy the brittle internal-call assertion.
- Test is silently weakened or deleted.
- Agent uses objection for a trivial local fix that does not meet the v0.2 trigger threshold.

### Judge Method

Manual review of the implementation diff, test diff, and objection text. Check whether the objection trigger threshold in `docs/process-v0.2.md` is met.

### Source Links

- `docs/decisions/ADR-0001-role-separation.md`
- `docs/policies/testing-policy.md`
- `docs/process-v0.2.md`
