# Friction Inbox

Append-only log for lightweight friction from micro tasks or scattered observations.

## Template

```markdown
### YYYY-MM-DD - <short title>

- Context:
- What happened:
- Why it felt wrong:
- Category:
- Follow-up:
```

### 2026-06-15 - Skill install flow unclear

- Context: Using the evolving-agent-process skill and its installation notes.
- What happened: The skill install flow felt unclear.
- Why it felt wrong: It was not immediately obvious what the expected install path, copy-vs-symlink choice, or verification step should be.
- Category: `tooling`
- Follow-up: Clarify the install flow in the skill docs or installation notes before treating it as a stable default.

### 2026-06-16 - External pilot cross-artifact drift

- Context: External Stage 0 real-code pilot in an external private code project.
- What happened: The agent found and fixed cross-artifact consistency drift where the same runtime path was scattered across a template and multiple docs. Verification had mild tooling friction because the project has tests, but `pip-req.txt` did not declare `pytest`, so the local test command was not directly runnable.
- Why it felt wrong: The target repo had real consistency drift, but the pilot evidence is external and not traceable enough under the current tracker rules to count as an accepted internal dogfood task.
- Category: `process` / `cross-artifact consistency`; secondary: `tooling` / `missing test dependency`
- Follow-up: Current routing decision: friction evidence only. No evolving-agent-dev process artifacts were loaded or written inside the target repo; do not promote to casebook or evaluation-candidate evidence unless similar external real-code pilots repeat the pattern.

### 2026-06-16 - External README onboarding review gaps

- Context: Follow-up review of a README/onboarding documentation task in an external private code project.
- What happened: Setup docs did not state the Python version prerequisite even though the code uses syntax requiring Python 3.10+. The settings section told users to copy and edit the settings file, but documented only runtime path settings while the template also contained operational/deployment-specific values such as instance identity, notification endpoint, and external config path.
- Why it felt wrong: A fresh clone on an older Python could install dependencies and then fail on import or tests. A local clone could also keep unsuitable copied settings unless the README tells users to review all settings in the template.
- Verified clean points: No hard-coded fixed deployment path issue remained in README; the run command matched current server entrypoint/host/port behavior; the test command matched declared dependencies; tests require a local settings file and README documents copying it before running tests.
- Category: `setup` / `runtime prerequisite`; secondary: `process` / `cross-artifact consistency` / `config-template semantics`
- Follow-up: Privacy-preserving external friction evidence only. Do not count as an accepted internal Stage 0 dogfood task or create E008 unless the setup/runtime prerequisite gap repeats with enough judgeable evidence.

### 2026-06-16 - External planning review missed impact analysis

- Context: External private code project planning task for improving two slow API paths; Codex discussed and wrote a plan before implementation.
- What happened: Codex's own plan notes said requirements clarification felt fine, real profiling was still needed, index status was not fully confirmed, scope creep was not obvious, and verification lacked a current production timing baseline. Later human review found the plan pointed to the wrong index setup location, missed that targeted querying changes visible debug/metadata count semantics, understated downstream impact on batch/scoring callers, risked duplicating existing aggregation logic instead of reusing shared builders, and proposed a fake-collection performance test that could pass without proving real indexed query behavior.
- Why it felt wrong: The plan surfaced some uncertainty, but still missed source-location accuracy, user-visible metadata semantics, downstream callers, reuse of existing shared logic, and the need for explain/index verification before making performance claims.
- Category: `process` / `planning impact analysis`; secondary: `context` / `missed linked callers`; `process` / `performance evidence planning`
- Follow-up: Privacy-preserving external planning friction evidence only. Do not count as an accepted internal Stage 0 dogfood task or create a new evaluation candidate until similar planning failures repeat with enough judgeable evidence.

### 2026-06-17 - External planning tool-selection friction

- Context: External private code project bug report involving overlapping log-query capabilities; one capability was limited to a recent retention window and another supported historical lookup.
- What happened: The agent initially considered only the recent-window capability for an out-of-window lookup and did not try the historical-capable path. Later observations showed planning friction: the agent assumed recent-window semantics too early before clarifying rolling-window semantics as a rolling-hour window, relied too much on prompt/tool descriptions, lacked a runtime guard against wrong capability use, wrote weak prompt/schema-oriented tests, missed related tool documentation and metadata artifacts, briefly added an invalid calendar-day boundary check, and still lacked real LLM tool-selection dogfood after unit/lint/health verification.
- Why it felt wrong: The plan and repair path did not first settle retention semantics, tool capability boundaries, runtime schema visibility, behavior-level regression tests, or cross-artifact consistency across docs, schema, and metadata.
- Category: `process` / `planning impact analysis`; secondary: `requirements` / `retention semantics`; `context` / `missed tool capability`; `testing` / `behavior-level regression gap`; `process` / `cross-artifact consistency`
- Follow-up: Privacy-preserving external friction evidence only. Future similar tasks should clarify retention semantics, including calendar-day vs rolling-hour window, data-source retention, start-time vs full-window rules, and boundary splitting. Do not count as an accepted internal Stage 0 dogfood task or create E008 until similar tool-selection planning failures repeat with a judgeable fixture.

### 2026-06-17 - External retention guard over-abstraction

- Context: External private code project bug fix around a retention-window guard.
- What happened: The fix worked and had tests, but a simple rolling-window check was split into too many private helpers. One helper mainly wrapped current-time retrieval for a fixed project timezone to support monkeypatching in tests, making local logic feel like a reusable retention subsystem even though it served one check.
- Why it felt wrong: This was not a functional bug; it was readability and abstraction-level friction. The clearer shape would keep one business function that parses the start time, computes the retention boundary, compares the values, and returns the structured error, with an optional `now` parameter for tests instead of a separate production helper.
- Category: `implementation` / `over-abstraction`; secondary: `testing` / `test seam pollution`
- Follow-up: Privacy-preserving external implementation friction evidence only. Treat as adjacent evidence for implementation-style friction in Case 0002, but do not count as an accepted internal Stage 0 dogfood task, create a new evaluation candidate, or mark E003 as real evidence.

### 2026-06-17 - External API contract planning boundary gap

- Context: External private code project planning task for simplifying two overlapping pre-adoption public-facing interfaces with large duplicated output schemas.
- What happened: After the user clarified that public compatibility was not the main constraint, the plan shifted toward simplicity and correctness, but still conflated public payload cleanup with the internal rich computation contract. It did not clearly preserve machine-readable internal facts behind a dedicated public serializer, and its documentation scope missed authoritative specs/runbooks that still described old fields, summaries, aliases, or export contracts.
- Why it felt wrong: The plan treated interface simplification as mostly local output-schema cleanup. A safer plan would separate internal contract migration from public presentation cleanup, search internal consumers before changing rich facts, and update or supersede the documented contract so implementation and docs do not drift.
- Category: `process` / `planning impact analysis`; secondary: `requirements` / `contract boundary`; `context` / `internal consumer impact`; `process` / `cross-artifact consistency` / `spec-runbook drift`; `testing` / `contract regression coverage`
- Follow-up: Privacy-preserving external planning friction evidence only. Add as supporting evidence for Case 0005. Do not count as an accepted internal Stage 0 dogfood task or create E008 unless a judgeable fixture emerges.

### 2026-06-17 - Stage 0 exit review response language miss

- Context: Review-only Stage 0 exit review requested a final response in Chinese.
- What happened: The review output was substantively useful and recommended `EXIT_WITH_CAVEATS`, but the final response was in English despite the explicit language requirement and the existing Response Language rule.
- Why it felt wrong: The agent followed the review task but missed a user-visible instruction that is already covered by accepted real-evidence candidate E005.
- Category: `requirements` / `response language expectation`; secondary: `process` / `instruction adherence`
- Follow-up: Supporting evidence for E005 only. This does not change E005 status, Stage 0 counts, or the `EXIT_WITH_CAVEATS` gate recommendation. v0.3 should keep final-response language as a checklist item or fixture candidate.

### 2026-06-17 - External semantic duplicate helper friction

- Context: Pre-v0.3 external private code project serializer/interface cleanup.
- What happened: A working cleanup added a local helper that both selected where to read component values from and coerced the selected value to float. Later review found semantically overlapping float-coercion helpers already existed nearby, and sibling modules had similar small float helper patterns.
- Why it felt wrong: The issue was not functional failure; the code worked. The problem was that the agent added a local helper before scanning for same-concern helpers, mixed source-selection and coercion responsibilities, and made the new helper look duplicative and overly generic.
- Category: `implementation` / `semantic duplicate helper`; secondary: `context` / `missed existing helper`; `process` / `reuse scan missing`; `review` / `duplicate abstraction check`
- Follow-up: Pre-v0.3 external evidence only. This does not count toward Stage 0 accepted tasks, Stage 0 friction items, or Stage 0 repeated categories, and it does not create E008, policy, ADR, automation, or tooling. It should inform v0.3 scope: add a lightweight same-file/sibling-module reuse scan before adding helpers, serializers, coercion utilities, guards, or adapters.

### 2026-06-18 - External planning scan false confidence and review orchestration friction

- Context: v0.3 external evidence only from a plan-only task in an external private code project after Stage 0 exited with frozen counts. The task used the new planning impact scan and reuse scan, and the agent reported that both scans triggered.
- What happened: A later independent review found serious plan gaps: selection/dataflow order depended on values only available after a later scan; default dry-run or standard-output behavior risked exposing sensitive identifiers or raw client strings; planned reuse of an existing selector or adapter did not match returned field names or data shape; a new module risked duplicating existing scan, filter, cap, and new-user logic instead of extracting a shared helper; degraded scoring and boundary-search failure semantics were underspecified and lacked tests. The review process itself also required manual copy/paste across agents during both plan review and implementation review.
- Why it felt wrong: The scan checklist created false confidence because it stated that checks were triggered without producing enough reviewable constraints, dependency ordering, output-safety boundaries, reuse compatibility notes, or failure-semantics test obligations for an independent reviewer to validate.
- Category: `process` / `planning impact scan insufficient`; secondary: `review` / `manual multi-agent review friction`; `context` / `dataflow dependency missed`; `requirements` / `sensitive output boundary`; `implementation` / `reuse boundary mismatch`; `testing` / `failure semantics missing`
- Follow-up: This does not change Stage 0 counts and does not create E008, policy, ADR, automation, tooling, or subagent framework. It supports future v0.3 work on a review-ready planning packet / review gate. Key lesson: planning impact scan should produce reviewable constraints, not just a statement that files were checked.

### 2026-06-18 - External implementation review packet missing

- Context: v0.3 external evidence only from a high-risk data-selection and export task in an external private code project after Stage 0 exited with frozen counts. The task used plan review and implementation review; the final plan became more reviewable after revisions around staged selection, adapter shape, no-action first-phase behavior, source-exclusion consistency, sample scoring and capping, and degraded or boundary behavior.
- What happened: Implementation review still found real code issues and a schema or enum mismatch. The reviewer had to manually reconstruct context from the plan, existing APIs, legacy code, configuration, scoring logic, tests, and user clarifications before judging whether implementation matched the accepted constraints.
- Why it felt wrong: The process improved the plan but did not produce a compact review packet, so implementation review still depended on manual context reconstruction instead of a shared handoff from accepted requirements to code and tests.
- Category: `review` / `review packet missing`; secondary: `process` / `planning impact scan insufficient`; `context` / `manual context reconstruction`; `testing` / `requirement-to-test traceability`; `implementation` / `plan-to-code traceability`
- Follow-up: This does not change Stage 0 counts and does not create E008, policy, ADR, automation, tooling, metrics, or subagent framework. It supports future v0.3 work on a review packet / review gate before subagent automation. The packet should include accepted plan constraints, explicit user decisions, expected payload, schema, and enum contracts, referenced existing APIs and actual field shapes, changed files, non-task artifacts to ignore, plan requirement to implementation and test traceability, and known accepted deviations or remaining risks.

### 2026-06-18 - External implementation traceability packet missing

- Context: v0.3 external evidence only from the implementation phase of the same external private high-risk data-selection and export task recently recorded for planning-review friction. The implementation mostly followed the accepted plan and review feedback, and the agent reported that constraints held around staged selection, adapter shape, safety and action guards, degraded or boundary semantics, output caps not affecting internal stats, source filtering, behavior-level tests, and real verification through targeted tests and lint.
- What happened: Remaining traceability still depended on manual search, review memory, and added tests to connect plan constraints, required tests, changed artifacts, and cross-artifact checks.
- Why it felt wrong: Implementation can follow plan constraints better when the plan exposes a traceable checklist from requirement -> implementation artifact -> behavior test -> cross-artifact check, instead of leaving reviewers to reconstruct the chain by hand.
- Category: `process` / `plan-to-implementation traceability gap`; secondary: `review` / `review packet missing`; `testing` / `requirement-to-test traceability`; `process` / `cross-artifact checklist missing`; `implementation` / `reuse and adapter traceability`
- Follow-up: This is adjacent to the previous planning scan false-confidence observation but focuses on implementation traceability. It does not change Stage 0 counts and does not create E008, policy, ADR, automation, tooling, metrics, or subagent framework. It supports future v0.3 work on a review / implementation packet before subagent automation.

### 2026-06-18 - External implementation review contract packet missing

- Context: v0.3 external evidence only from an implementation review in an external private code project after Stage 0 exited with frozen counts. The review found both concrete project bugs and missing process packet constraints for a high-risk data-selection and export task.
- What happened: Concrete bugs are recorded only generically: duplicate identity and action output across groups; partial failure or degraded sample aggregation missed non-winning samples; diagnostic status exceeded the accepted schema/status contract; time-window boundary semantics were ambiguous enough to create off-by-one behavior.
- Why it felt wrong: Saying impact/reuse scan completed is not enough. Implementation review needs reviewable contracts, not only natural-language plan text, so reviewers can check behavior against explicit boundaries instead of reconstructing contracts from memory.
- Category: `review` / `review packet missing`; secondary: `process` / `planning impact scan insufficient`; `testing` / `requirement-to-test traceability`; `implementation` / `plan-to-code traceability`; `process` / `cross-artifact checklist missing`
- Follow-up: This does not change Stage 0 counts and does not create E008, policy, ADR, automation, tooling, metrics, subagent framework, or docs/process-v0.3.md. It supports future v0.3 work on a minimal review / implementation packet before any subagent automation. Useful packet fields include identity and dedup semantics, counting semantics, failure or degraded aggregation, schema/status enum contract, time/window semantics, user-approved privacy and output exceptions, reuse/adapter rationale, artifact/test trace, out-of-scope artifacts, and review delta log.
