# Session Report: CRL-X06 Packet Refinement Decision

## Goal

Decide whether the committed cross-domain `CRL-X06` evidence justifies a minimal, low-noise, conditionally triggered mutation/recovery review-packet refinement. Record the decision without changing any skill or reference, starting an experiment, or creating a policy, ADR, casebook entry, or formal evaluation.

## Status

- Decision: `accepted pending separate implementation`.
- Selected shape: `existing-section extension` under `Task-Specific Contracts`; not a new standalone section and not a `SKILL.md` hard gate.
- Implementation: not performed in this task.
- Verification status: not behaviorally verified.
- Lineage outcome: `awaiting evidence`.
- Repository rule state: `partial`.
- Dogfood: yes; this evolving-agent-dev decision task used `evolving-agent-process`.
- Source evidence: external privacy-preserving evidence; the external tasks are not this project's dogfood.
- Stage 0: frozen counts unchanged.
- Active experiment: none.
- Evaluation: not promoted.

## Preconditions And Evidence

- Task-start worktree: clean.
- `9db9d30` was `HEAD`; both `9db9d30` and `9887df6` were confirmed as `HEAD` or ancestors.
- Before this decision, central `CRL-X06` was a `reassessment candidate`, its repository rule state was `partial`, and its outcome was `awaiting evidence`.
- Two independent natural external domains support the parent pattern. Their loaded skill versions remain unknown, so this evidence does not establish that a known current canonical rule failed.
- Independent implementation/final-diff review detected the source gaps, while pre-implementation packet prevention was incomplete. Final source-task fix verification remains unestablished.

## Decision

The evidence is sufficient to accept a narrow generic packet refinement pending implementation. It is not sufficient to claim effectiveness, promote a hard gate, prescribe implementation mechanisms, or change the lineage outcome.

The selected shape is a compact optional extension to the existing `Task-Specific Contracts` section. This reuses the packet's existing conditional contract routing and avoids another top-level checklist section. The future extension should be recorded only when the trigger applies and should cross-reference `Required Behavior Tests` rather than duplicate that section.

The accepted behavior is truthful state-transition, outcome, retry, and recovery contracts. Independent adversarial review remains required: moving the contract into the packet makes high-impact assumptions reviewable before implementation, while final review still checks implementation and packet completeness.

## Option Review

### A. Keep No-Change

Rejected. Independent review detection was effective, but it found high-impact packet gaps only after implementation. With natural evidence across two domains, continuing to rely solely on final review would leave avoidable late discovery around partial mutation, missed writers, unsafe whole-operation retry claims, and state-loss risk. The accepted packet cost is bounded by conditional triggering and one existing-section extension.

No-change would become preferable again if real use shows that the extension adds no decision-relevant information beyond existing packet fields or cannot be triggered without burdening ordinary tasks.

### B. Add A Conditional Contract

Accepted in compressed form. The candidate behavior belongs in the packet, but a seven-bullet standalone `Mutation And Recovery Contract` section is more structure than current evidence requires. The same observable contract fits as one optional `Task-Specific Contracts` entry with four compact fields and a cross-reference to behavior tests.

This preserves one aggregated contract instead of scattering three finding-specific rules. It also makes the refinement reversible without adding routing-level skill text.

### C. Add A SKILL.md Hard Gate

Rejected. There is no evidence that a conditional reference-level contract cannot be loaded or executed reliably. A hard gate would over-trigger on the domain noun "mutation," duplicate packet guidance, expand the skill body, and add cost to simple or fully bounded changes. Routing-level visibility can be reconsidered only if known-version tasks repeatedly fail to load or apply the implemented reference guidance.

## Existing Packet Fit

- `Debug / Bad-Case Evidence Chain` is reactive and bad-case-oriented; it does not proactively state the mutation contract for every applicable planned workflow.
- `Task-Specific Contracts` is the correct semantic home, but its current failure/status and mitigation bullets do not connect effect boundaries, every mutation boundary, replay safety, and alternative state-aware outcomes.
- `Required Behavior Tests` can hold the paired scenarios, so the refinement should reference rather than duplicate it.
- `Runnable Acceptance / Entrypoints`, `Dataflow Contract Preservation`, `Verification Plan`, and `Implementation Trace` provide adjacent execution and traceability evidence but do not replace the state-transition contract.

## Pending Implementation Shape

Add one conditional `Mutation/recovery` entry under the existing `Task-Specific Contracts`. When applicable, the packet records only:

1. Transition map: preflight-detectable blockers, the first mutation, and externally visible or irreversible effect boundaries.
2. Boundary inventory: actual mutation writers, copies, or independently mutable boundaries and the consistency contract for each.
3. Outcome matrix: pre-effect versus post-effect status and retry semantics; whole-operation retry requires explicit replay safety, while unsafe replay directs a state-aware recovery or accurate partial/completed-with-warning outcome.
4. Behavior proof: applicable rejection-before-mutation and failure-after-effect cases listed under `Required Behavior Tests`.

The implementation should keep this compact. It should not add a second copy of generic verification, entrypoint, implementation-trace, or dataflow guidance.

## Trigger Boundary

Apply only when a task changes or reviews a multi-step state-changing workflow and at least one material state-transition risk is present:

- live, durable, external, visible, or irreversible effects;
- multiple writers, copies, or independently mutable boundaries;
- preflight-detectable blockers before the first mutation;
- different status or retry semantics before and after an effect; or
- partial completion that can duplicate an effect, misreport completion, or lose state.

Representative applicable work includes resumable live operations, durable configuration writes, migrations, deploy or cleanup workflows, batch mutation, and multi-writer or multi-copy state. Task size alone is not a trigger; changed capability and state-transition risk are.

Do not trigger solely for:

- read-only analysis;
- documentation, copy, or formatting changes;
- single-step pure functions;
- local refactors with no durable or external effect;
- ordinary getter, serializer, or symbol renames;
- simple changes fully covered by one existing transaction boundary with no additional writer or recovery surface; or
- domain vocabulary that mentions writes or mutations without changing state-transition behavior.

These negative boundaries keep ordinary, single-step, local-only, easily reversible, or read-only tasks lightweight.

## Semantic And Mechanism Boundaries

The contract requires truthful state transitions, outcomes, retryability, and recovery direction. It does not require any particular concurrency, durability, replay, or recovery mechanism. Target systems choose appropriate guards and recovery paths.

Whole-operation retry is safe only when replay itself has an explicit safety guarantee. Reconciliation, forward recovery, compensation, or accurate partial/completed-with-warning reporting are state-aware alternatives when replay is unsafe; their existence does not prove whole-operation retry safety.

The future reference wording must remain free of source-domain commands, APIs, and implementation-specific mechanisms. Mechanisms may appear in a target project's filled packet when relevant, but not as universal requirements.

## Role Separation

### Plan Decision

Compared A/B/C using cross-domain evidence, prevention versus detection, existing packet fit, trigger precision, checklist cost, observable behavior, and reversibility. Selected a conditional existing-section extension pending implementation.

### Test Responsibility

Future applicable packets must expose the transition map, boundary inventory, outcome matrix, and the applicable behavior cases. Behavior tests should distinguish rejection before mutation from failure after an effect and must not confuse a recovery path with replay safety. This task creates no fixture or test.

### Implementation Responsibility

N/A in this task. Skill and reference changes are prohibited. A separate implementation task must make and independently review any reference edit.

### Review Check

Confirmed that the decision does not overgeneralize from source mechanisms, treat recovery as replay safety, mandate a particular mechanism, burden trivial tasks, duplicate existing packet sections, or change the lineage outcome. The future implementation must preserve those checks.

## Known-Version Evidence Plan

After separate implementation and commit, wait for natural real-task evidence that records the loaded refinement version. At minimum, an applicable multi-step state-changing task should show:

- the packet captured the four fields before implementation;
- the trigger was based on changed state-transition risk rather than task size or domain nouns;
- behavior tests covered the applicable pre-mutation rejection and post-effect failure semantics;
- implementation/final-diff review checked the packet against all actual boundaries and resulting outcomes; and
- verification establishes the relevant behavior rather than only packet completion.

A nearby known-version real task that correctly does not trigger is useful low-noise evidence, but no synthetic experiment is authorized.

Retain the refinement if it surfaces decision-relevant constraints before implementation with low overhead and final review confirms the packet-to-implementation trace. Narrow it if applicability is repeatedly ambiguous, N/A use is common, or fields duplicate existing sections. Remove it if it adds no incremental information or persistently burdens non-trigger tasks. Redesign it if correctly completed packets still miss boundaries or conflate replay safety with state-aware recovery.

## Changes

- Updated the current-state `CRL-X06` decision, next step, and evidence status in `docs/v0.3-scope.md`.
- Added this decision/review report.
- No skill, reference, inbox, policy, ADR, evaluation, casebook, Stage 0 tracker, process-version, runtime-install, external-note, implementation-plan, or fixture change.

## Verification

- Confirmed task-start `HEAD` was `9db9d30`, both evidence commits were `HEAD` or ancestors, and the worktree was clean.
- Read the complete tracked diff and the full untracked decision report.
- `git diff --check` passed with no whitespace errors.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-19-crl-x06-packet-refinement-decision.md` produced no whitespace warnings and exited `1` as expected because the files differ.
- A central-heading search found exactly one `CRL-X06` heading. Content checks confirmed repository rule state `partial`, outcome `awaiting evidence`, decision `accepted pending separate implementation`, selected shape `existing-section extension`, implementation not performed, and behavioral verification not established.
- Negative promotion checks found no `improved` or `repeated` outcome and no formal-evaluation promotion in this report. The existing lineage's negated historical wording was not treated as a promoted outcome.
- The report records A/B/C, both positive and negative trigger boundaries, the four-field pending shape, existing-section fit, retry/recovery separation, known-version evidence, and retain/narrow/remove/redesign criteria.
- A scan limited to the pending contract found no source-domain commands, APIs, or implementation-specific mechanism nouns. Manual review confirmed the contract stays at state-transition, effect-boundary, consistency, outcome, replay-safety, and recovery-direction semantics.
- Retry safety remains separate from reconciliation and forward recovery: replay requires its own explicit safety guarantee, while unsafe replay routes to state-aware alternatives.
- Repository-link existence checks passed. Negative privacy searches found no external path, project identity, credential or private-config assignment, recipient or account identifier, port, network address, URL, or runtime payload in the changed files.
- Changed-file checks list only `docs/v0.3-scope.md` and this report. No skill, reference, inbox, policy, ADR, evaluation, casebook, Stage 0 tracker, process-version, runtime-install, external-note, implementation-plan, or fixture changed.
- The initial precondition command's CRL search partially failed because double-quoted Markdown backticks triggered zsh command substitution (`command not found: partial`, `reassessment`, and `awaiting`). The git status and ancestry checks in that command succeeded; the CRL assertions were rerun with single-quoted patterns and passed. Remaining risk from the failed search: none.

## Good

The existing packet structure can absorb the evidence as one conditional contract without adding a hard gate or a new top-level checklist section.

## Friction

The initial precondition search used double quotes around Markdown backticks, so zsh attempted command substitution and reported three `command not found` errors. The repository was unchanged. The same assertions were rerun with single-quoted patterns and passed; remaining risk from the failed command is none.

## Proposed Follow-up

1. Review and commit this decision evidence separately.
2. Open a separate implementation task for the accepted reference-only existing-section extension.
3. Independently review that implementation for trigger precision, semantic generality, retry/recovery separation, duplication, and low-noise behavior.
4. Commit the implementation separately, record its exact version, and then wait for known-version natural real-task evidence.
5. Do not start a synthetic experiment or modify `SKILL.md` unless later evidence shows reference-level routing is unreliable.
