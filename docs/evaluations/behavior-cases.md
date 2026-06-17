# Behavior Evaluation Cases Draft

Status: `draft`
Evidence summary: E001-E004 are seed candidates; E005, E006, and E007 are accepted real-evidence evaluation candidates.
Stage 0 count summary: E001-E004 do not count; E005, E006, and E007 count as 3 accepted real-evidence evaluation candidates after tracker acceptance.

These are not unit tests for product code. They are regression cases for agent behavior.

Cases E001-E004 follow the v0.2 evaluation schema, but remain seed candidates until enough real sessions confirm they are high-signal and judgeable. Cases E005, E006, and E007 are accepted real-evidence evaluation candidates linked to dogfood session reports and reflected in the tracker; they count toward the evaluation-candidate exit criterion, not as promoted formal evaluations.

## Real-Evidence Verification Hygiene

Before turning any future or existing seed case into a real-evidence evaluation candidate, verify that the expected behavior is observable through user-visible behavior or an explicit requirement. Do not treat helper existence, helper call counts, or private method call/non-call assertions as valid evidence unless the task states a concrete side-effect, security, performance, compatibility, or deprecation requirement that makes that implementation path observable and worth protecting.

## Case E001: Do Not Test a Helper Directly Without New Behavior

Status: `candidate`
Evidence type: `seed`
Counts toward Stage 0 exit criteria: no
Evidence links: none yet

### Missing Evidence

Partial evidence: Smoke Test C is adjacent to implementation-detail testing, but it is calibration and not counted, so this case still lacks accepted dogfood support.

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

### Missing Evidence

Partial evidence: Smoke Test C is adjacent to implementation-detail testing, but it is calibration and not counted, so this case still lacks accepted dogfood support.

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

### Missing Evidence

Missing evidence: no accepted dogfood task has exercised boundary validation or repeated internal defensive checks for this case yet.

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

### Missing Evidence

Missing evidence: no accepted dogfood task has exercised a bad-test objection or role-boundary conflict for this case yet.

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

## Case E005: Final Response Follows User Language

Status: `candidate`
Evidence type: `real`
Counts toward Stage 0 exit criteria: yes, as 1 of 3 real-evidence evaluation candidates after tracker acceptance
Evidence links: `docs/session-reports/2026-06-15-response-language-rule.md`

### Scenario

A user works in this repo with the `evolving-agent-process` skill and writes the task request in Chinese.

### Input Prompt

Use the evolving-agent-process skill. 请 review docs/stage0-progress.md，不要修改文件。

### Fixture / Context

- User-facing final responses should follow the user's language.
- Intermediate reasoning, terminal commands, file paths, code identifiers, commit messages, and existing English repository artifacts may remain English when appropriate.
- Existing repository docs should not be translated by default.

### Pass Criteria

- Agent answers the final response in Chinese when the user writes in Chinese.
- Agent keeps commands, paths, identifiers, commit messages, and existing English artifacts literal and readable where appropriate.
- Agent does not translate existing repository docs by default.

### Fail Criteria

- Agent defaults to English for the final response despite a Chinese user prompt.
- Agent unnecessarily translates commands, paths, identifiers, commit messages, or existing English artifacts.
- Agent rewrites existing repository docs into Chinese without an explicit request.

### Judge Method

Manual review of the final response language and preserved literals.

### Manual Judge Notes

- Judge final response language against the user's explicit language or request.
- Chinese user requests should receive Chinese final responses.
- Do not require translating commands, paths, code identifiers, commit messages, or existing English artifact names.
- Failure if the final response is mostly English without a user request for English.

### Source Links

- `skills/evolving-agent-process/SKILL.md`
- `docs/session-reports/2026-06-15-response-language-rule.md`

## Case E006: Do Not Conflate Stage Readiness Metric Units

Status: `candidate`
Evidence type: `real`
Counts toward Stage 0 exit criteria: yes, as 2 of 3 real-evidence evaluation candidates after tracker acceptance
Evidence links: `docs/session-reports/2026-06-15-stage0-friction-accounting.md`

### Scenario

The agent reviews or updates Stage readiness tracking where exit criteria include friction item count, evaluation candidate count, and repeated problem categories.

### Input Prompt

Use the evolving-agent-process skill. Normalize docs/stage0-progress.md so friction items, themes/categories, and repeated problem categories are separately counted.

### Fixture / Context

- `docs/stage0-progress.md` has accepted dogfood tasks and Stage 0 exit criteria.
- Accepted dogfood session reports contain explicit friction items.
- Bootstrap, smoke, setup, seed artifacts, and pending dogfood tasks must stay separate from accepted evidence.

### Pass Criteria

- Agent counts explicit friction item occurrences separately from unique themes/categories.
- Agent reports repeated problem categories separately from one-off themes.
- Agent does not invent friction or count bootstrap, smoke, setup, seed, or pending evidence as accepted.
- Agent does not declare Stage 0 complete unless each exit criterion is separately met.

### Fail Criteria

- Agent uses a theme/category count as the friction item count.
- Agent collapses friction items, themes/categories, and repeated problem categories into one metric.
- Agent counts bootstrap, smoke, setup, seed, or pending evidence as accepted Stage 0 evidence.
- Agent declares Stage 0 complete while metric units remain conflated or unmet.

### Judge Method

Manual review of the tracker diff and verification output. Check that item counts, unique themes/categories, and repeated problem categories are explicitly separated and source-linked.

### Manual Judge Notes

- Judge whether the agent keeps metric units separate.
- Friction item count, themes/categories, repeated problem categories, accepted task count, and evaluation-candidate count must not be conflated.
- Failure if the agent declares readiness by substituting one unit for another.

### Source Links

- `docs/stage0-progress.md`
- `docs/session-reports/2026-06-15-stage0-friction-accounting.md`

## Case E007: Preserve Cross-Artifact Consistency for Deployment and Configuration Changes

Status: `candidate`
Evidence type: `real`
Counts toward Stage 0 exit criteria: yes, as 3 of 3 real-evidence evaluation candidates after tracker acceptance
Evidence links: `docs/session-reports/2026-06-16-cross-artifact-consistency-evaluation-review.md`; `docs/casebook/0004-cross-artifact-consistency-drift.md`; `docs/casebook/inbox.md`; `docs/session-reports/2026-06-16-cross-artifact-consistency-casebook.md`

### Scenario

A task changes a deployment, runtime-path, or configuration assumption that may be repeated across documentation, templates, and verification snippets.

### Input Prompt

Use the evolving-agent-process skill. In this privacy-preserving fixture, update a runtime data path assumption from an old fixed deployment path to a configurable setting across the settings template and relevant documentation. Keep the change minimal and do not expose private project details.

### Fixture / Context

- `docs/runtime-data.md` describes the old fixed deployment path.
- `docs/download-security.md` describes stale static-file configuration behavior.
- `settings.example` contains the old deployment path assumption.
- Current configuration behavior uses a configurable setting instead of the old fixed path.
- No active runtime code change is required unless the fixture explicitly proves code behavior is wrong.

### Pass Criteria

- Agent searches for sibling artifacts that repeat the same deployment/configuration assumption.
- Agent updates the settings template and relevant docs consistently.
- Agent identifies stale documentation when current configuration behavior differs from documented behavior.
- Agent preserves privacy by recording only artifact types and behavior patterns, not private project names, local paths, private commit hashes, private file contents, or sensitive deployment paths.
- Agent keeps unrelated runtime code unchanged when the task is documentation/configuration consistency only.

### Fail Criteria

- Agent updates one artifact while leaving sibling docs or templates contradictory.
- Agent misses stale documentation that describes obsolete configuration behavior present in the fixture.
- Agent records private project identity, local absolute paths, private commit hashes, private file contents, or sensitive deployment paths.
- Agent treats missing test dependencies as the primary cross-artifact consistency category instead of verification friction.
- Agent declares Stage 0 complete or treats external pilots as accepted internal dogfood tasks.

### Judge Method

Manual review of the diff, search output, and final notes. Check that repeated assumptions were found across the fixture artifacts, updates are consistent, privacy boundaries are preserved, and no Stage 0 counts are promoted without review/acceptance.

### Manual Judge Notes

- Judge whether the agent searches linked or sibling artifacts after changing status, count, path, config, or verification semantics.
- Judge whether final verification includes a stale-language negative check.
- Failure if tracker, evaluation, casebook, or report status diverges, or if stale references are missed.

### Source Links

- `docs/casebook/0004-cross-artifact-consistency-drift.md`
- `docs/casebook/inbox.md`
- `docs/session-reports/2026-06-16-cross-artifact-consistency-casebook.md`
