# Session Report: CRL-X07 Target-Context Refinement Decision

## Goal And Decision Question

Decide whether the committed `CRL-X07 - Target-context verification fidelity` evidence justifies a narrow, low-noise review-packet refinement and, if so, freeze its minimum behavior, trigger boundaries, and pending implementation shape without changing any skill or reference.

Decision question:

> Should CRL-X07 add a conditional packet contract that makes target-version, target-environment, and peer/protocol evidence fidelity reviewable before implementation, or should the repository continue relying on its existing scattered guidance and independent review?

## Status

- Decision: `accepted pending separate implementation`.
- Selected shape: one conditional, three-field `Target-context` entry under the existing `Task-Specific Contracts`.
- Implementation: not performed in this task.
- Repository rule state: `partial`.
- Source-task attribution: `loaded version unknown`.
- Lineage status: `accepted pending separate implementation`.
- Lineage outcome: `awaiting evidence`.
- Behavioral effectiveness: not established.
- Decision-task dogfood: yes; this repository edit used `evolving-agent-process`.
- Source evidence: external privacy-preserving evidence; the external source tasks are not this repository's dogfood or Stage 0 evidence.
- Active learning, synthetic pilot, policy, ADR, casebook, or formal evaluation promotion: none.

## Evidence Basis And Limits

- `ext-crl-2026-07-d/C01` and `C02` established complementary version-fidelity and environment-fidelity gaps in one external project.
- `ext-crl-2026-07-e/C01` supplied independent-project and runtime-migration-domain natural evidence across version, environment, and peer/protocol fidelity, satisfying the prior reassessment threshold while remaining one correlated plan/review workflow.
- Existing source-of-truth, schema/API/output, Test Double Boundary Fidelity, Runnable Acceptance / Entrypoints, Verification Plan, behavior-test, and adversarial-review guidance is directionally aligned but does not express one complete target-context contract.
- Independent review detected the source gaps at plan level and made the packet more specific. The evidence does not establish that a known canonical version failed, that a refinement changes real-task behavior, or that implementation tests, target builds, peer-originated evidence, or production-like acceptance were completed.
- All source-task attribution remains `loaded version unknown`. External task dates, the current repository state, and current runtime linkage do not identify the historically loaded skill version.

## Option Review

### A. No Change

- Benefit: zero new packet structure and no metadata burden; existing source-of-truth, contract, entrypoint, test-double, verification, and adversarial-review guidance remains available.
- Cost: reviewers must reconstruct the promised target across several sections and infer whether current-version, current-process, or implementation-owned evidence actually represents it.
- Omission risk: the evidence shows that broad compatibility assertions can survive into review without one visible target boundary, independent evidence basis, or remaining-gate disposition. Continued reliance on independent review leaves decision-relevant context implicit and raises late review/rework cost.
- Overtrigger risk: none from a new rule, but no-change does not supply a packet artifact for measuring correct applicability or false confidence.
- Decision: rejected. Existing guidance is not fully equivalent to the A/B/C parent contract, and the cross-project evidence makes the aggregation gap more than a feature-specific execution observation.

### B. Conditional Existing-Section Extension

- Benefit: moves the promised target, its evidence basis, and verification limits into one reviewable pre-implementation artifact while reusing the packet's conditional contract routing.
- Cost: applicable tasks fill three compact fields and may need to identify a target source of truth that was previously implicit. Non-applicable tasks retain a short reasoned `N/A` path.
- Omission risk: a compressed entry could still be filled generically. Independent review must challenge whether the named target and evidence are actually faithful, not merely present.
- Overtrigger risk: compatibility-related vocabulary and task size could pull ordinary work into extra investigation unless the trigger is explicitly promise-based and includes strong negative boundaries.
- Decision: accepted in compressed form. A, B, and C remain in scope, but five candidate semantics collapse into three fields and cross-references instead of a standalone checklist.

### C. SKILL.md Routing-Level Hard Gate

- Benefit: maximum visibility and a possible completion stop if reference-level routing later proves unreliable.
- Cost: duplicates packet-level source, contract, and verification guidance; expands the skill body; and adds high-frequency interpretation cost before a reference-only shape has been observed.
- Omission risk: a hard gate would still need the same target and evidence semantics, so routing visibility alone would not solve shallow packet content.
- Overtrigger risk: high. Tasks could trigger solely because they mention `compatibility`, `migration`, `protocol`, `runtime`, or `legacy`, even without a cross-context promise.
- Decision: rejected. There is no known-version evidence that the packet reference cannot be loaded or applied, so routing-level escalation is premature.

## Existing Packet Fit

- `Task-Specific Contracts` is the semantic home because target context defines the compatibility or runtime-independence promise that implementation and review must preserve.
- `Verification Plan` should remain the source for concrete commands, tests, manual checks, production-like review, and explicit limits; placing the whole refinement there would omit the promised target and evidence-ownership contract.
- `Runnable Acceptance / Entrypoints` remains the place for actual commands, defaults, modes, and outputs when an entrypoint dimension applies.
- `Test Double Boundary Fidelity`, `Required Behavior Tests`, `Requirement Traceability Checklist`, and `Open Questions / Risks` remain adjacent evidence and traceability surfaces. The new entry should cross-reference them when relevant rather than repeat their checklists.
- No existing single section or rule fully combines the applicable target boundary, target-relevant and sufficiently independent evidence, context-faithful verification, and unexecuted acceptance gates.

## Pending Implementation Shape

In a separate implementation task, add one conditional `Target-context` entry under the existing `Task-Specific Contracts`. When applicable, it records only:

1. Target boundary: the applicable promised target version or compatibility floor, runtime environment or independence boundary, default entrypoint, and/or external peer or producer/consumer contract. Record only dimensions the task actually promises.
2. Evidence basis: the target-relevant source of truth and why the evidence is sufficiently independent for the claim. When an existing peer or external protocol determines compatibility, evidence generated entirely by the implementation under test is not sufficient by itself.
3. Proof and remaining gates: cross-reference the context-faithful checks in existing `Verification Plan`, `Runnable Acceptance / Entrypoints`, and `Required Behavior Tests` as applicable; distinguish completed evidence from target build, peer interoperability, deployment acceptance, rollout, or other claim-relevant gates that remain open.

For non-applicable tasks, preserve a short `N/A` reason. The implementation must remain an existing-section extension, not a standalone compatibility section, a second verification checklist, or final wording authored by this decision report.

## Positive Trigger Boundary

Apply only when a task changes, creates, or reviews a compatibility or runtime-independence promise across contexts and at least one target-fidelity dimension is material. Any one of these can qualify:

- historical-version or minimum-version support;
- a runtime or dependency migration that promises existing observable behavior;
- offline, portable, isolated, clean-build, or deployment-independent behavior;
- a default entrypoint whose target environment can differ from the development process;
- compatibility determined by a legacy peer, wire contract, or external producer/consumer;
- a claim for which current documentation, the current environment, or the implementation under test cannot independently establish the target contract; or
- a public compatibility claim that depends on target build, peer interoperability, deployment acceptance, or rollout evidence not yet run.

The conditions are alternatives, not a checklist that all applicable tasks must satisfy.

## Negative Trigger Boundary

Do not trigger solely for:

- ordinary changes supporting only the current version with no historical compatibility promise;
- local refactors that do not change runtime independence, entrypoints, deployment boundaries, or peer contracts;
- internal-interface changes with no external peer or wire contract;
- documentation, copy, formatting, comments, or pure-function changes;
- ordinary getter, serializer, helper, or symbol renames;
- work already covered by one complete, real target-context acceptance path when this task does not change its version, environment, entrypoint, or peer boundary;
- the words `compatibility`, `migration`, `protocol`, `runtime`, or `legacy`; or
- a large task with no cross-version, cross-environment, default-entrypoint, or external-peer promise.

Task size and domain vocabulary are never sufficient triggers.

## Mechanism-Neutral Boundary

The accepted contract requires a declared target boundary, evidence fidelity, and truthful verification status. It does not universally require an exact git tag, source checkout, target binary, subprocess, container, particular operating-system build, offline invocation, live network call, real peer, fixed fixture format, golden file, production deployment, package manager, or dependency probe.

Those are target-system evidence mechanisms. The implementation must not require target-project users to inspect skill commits, classify central-lineage outcomes, or maintain this repository's evidence bookkeeping.

## Role Separation

### Plan Decision

Compared A/B/C against cross-project evidence, existing packet fit, reviewer reconstruction cost, observability, mechanism neutrality, metadata burden, and correct-trigger/correct-non-trigger testability. Selected the conditional three-field existing-section extension.

### Test Responsibility

No fixture or implementation test is created here. After implementation, natural evidence must distinguish correct trigger, correct non-trigger, vocabulary/size overtrigger, environment- or implementation-owned false confidence, and cases with insufficient opportunity or artifacts.

### Implementation Responsibility

N/A in this task. Skill and reference changes are prohibited. A separate task must implement only the frozen shape, independently review it, and commit it separately without reopening the decision by default.

### Review Check

Confirm that the decision does not turn domain nouns into triggers, require all A/B/C dimensions simultaneously, prescribe an evidence mechanism, duplicate verification or entrypoint sections, treat review detection as implementation prevention, or change the lineage outcome.

## CRL-X07 Lineage State

- Repository rule state: `partial`; the accepted shape is not implemented.
- Source-task attribution: `loaded version unknown`.
- Decision/change: `accepted pending separate implementation` as a reference-only existing-section extension.
- Status: `accepted pending separate implementation`.
- Outcome: `awaiting evidence`.
- No active learning bet, synthetic pilot, policy, ADR, casebook, formal evaluation, or CRL-X08 is created.

## Known-Version Natural Evidence Plan

After separate implementation and commit, observe natural tasks whose loaded refinement version can be established without shifting central bookkeeping onto target-project users:

- Correct trigger: an applicable task places target-context constraints and their verification disposition in the packet before implementation.
- Correct non-trigger: a nearby low-risk or current-context-only task remains lightweight.
- Overtrigger: a task enters the contract only because of domain vocabulary or size.
- False confidence: verification still inherits the current process/environment or lets the implementation under test generate all peer/protocol evidence while claiming the target contract.
- Inconclusive: the task presents no real target-context failure opportunity, the loaded version is unknown, or packet and verification artifacts are insufficient for comparison.

Natural evidence should show whether the packet reduces hidden-context reconstruction and whether final review can trace the target promise to completed evidence and explicit remaining gates. Packet completion alone does not establish target compatibility or behavioral effectiveness.

## Retain, Narrow, Remove, Or Redesign

- Retain if applicable known-version tasks expose decision-relevant target constraints before implementation with low overhead, while nearby non-trigger tasks remain lightweight.
- Narrow if applicability is repeatedly ambiguous, `N/A` use is common in plausible trigger tasks, or the evidence/proof fields duplicate existing sections.
- Remove if the entry adds no information beyond existing source-of-truth and verification fields or persistently burdens tasks without a cross-context promise.
- Redesign if correctly triggered and completed packets still allow current-context evidence or implementation-owned protocol evidence to stand in for the promised target.

## Why No Skill Change In This Task

This task freezes the decision, not its wording. Keeping implementation separate preserves reviewability, prevents the decision author from silently expanding the accepted shape, and allows the future diff to be checked against the three fields, trigger boundaries, section placement, and mechanism-neutral constraints. `SKILL.md` escalation remains unsupported.

## Changes

- Updated only the current-state CRL-X07 decision, status, and next step in `docs/v0.3-scope.md`.
- Added this decision session report.
- No CRL-X01-CRL-X06, skill, reference, policy, ADR, evaluation, casebook, Stage 0, process-version, README, runtime-install, external-note, or fixture change.

## Verification

- Task-start `HEAD` was `e28e6aa`, `git merge-base --is-ancestor e28e6aa HEAD` passed, and `git status --short` was empty.
- Read the required process docs, complete CRL-X07 evidence reports, CRL-X06 evidence/decision/implementation precedent, current canonical skill and packet reference, and session-report guidance. Searches across canonical guidance and related repository artifacts found partial same-direction rules but no complete equivalent target-context contract.
- Read the complete tracked diff and the full untracked report after editing. `git diff --check` passed.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-29-crl-x07-target-context-refinement-decision.md` produced no whitespace warning; its expected file-difference exit `1` was asserted.
- The changed-file allowlist is exactly `docs/v0.3-scope.md` and this report. Process-substitution comparisons confirmed CRL-X01-CRL-X06 and the evaluation watchlist are byte-equivalent to `HEAD` within `docs/v0.3-scope.md`.
- Diff checks found no skill/reference, README, process, Stage 0, casebook, policy, ADR, or evaluation artifact change.
- Central-lineage checks found exactly one CRL-X07 heading and no CRL-X08 heading. CRL-X07 remains `partial`, `loaded version unknown`, and `awaiting evidence`; decision and status are `accepted pending separate implementation`.
- The current-state CRL-X07 block no longer contains the superseded reassessment status or instruction to open the decision task. It now directs a separate independently reviewed implementation task and known-version correct-trigger/correct-non-trigger observation.
- Structured report checks confirmed A/B/C option reviews, the three-field pending shape, positive and negative triggers, mechanism neutrality, correct-trigger/non-trigger/overtrigger/false-confidence/inconclusive observations, and retain/narrow/remove/redesign criteria.
- New-content checks found no promoted outcome or prohibited causal language. The report explicitly records that implementation was not performed and behavioral effectiveness is not established.
- All newly added repository-relative links exist. Privacy-negative checks found no source path, project identity, URL, network address, account-like identifier, email, or credential/private-value assignment.
- No verification command failed. Remaining risk is semantic rather than mechanical: trigger precision and field usefulness cannot be established until the separate implementation exists and known-version natural tasks supply comparable artifacts.

## Good

The packet can represent target-context fidelity as one conditional promise-and-evidence contract while leaving concrete mechanisms and commands in the target project's existing verification surfaces.

## Friction

No notable process friction. The remaining uncertainty is evidence strength: cross-project plan/review evidence supports a reversible packet refinement, but not a routing hard gate or a behavioral-effect claim.

## Proposed Follow-up

1. Independently review and commit this decision artifact.
2. Open a separate reference-only implementation task for the frozen three-field existing-section extension.
3. Independently review and commit that implementation.
4. Wait for known-version natural correct-trigger and nearby correct-non-trigger evidence; do not start a synthetic pilot.
