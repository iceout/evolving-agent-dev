# Session Report: Coding Review Loop Case-Capture Refinement

## Goal

Implement the accepted narrow refinement that separates a required medium/high-risk case-capture decision from conditional case creation, adds a designated-observation path, and replaces the target-project case template with a compact factual transfer shape.

## Status And Accepted Direction

- Dogfood: yes; this evolving-agent-dev edit used the repo-tracked `evolving-agent-process` and `skill-creator` skills.
- Scope: canonical `coding-review-loop` guidance, its case-note reference, the local-evidence design boundary, and this report only.
- Accepted direction: require the decision but not a note for every invocation; preserve friction/failure capture; add only a narrow independently designated observation trigger with a version-evidence boundary; keep target-project notes local, factual, privacy-preserving, and free of central routing responsibilities.
- Explicit non-goals: no full PDCA framework, usage ledger, per-invocation log, telemetry, automation, central synchronization, policy, ADR, casebook/inbox entry, evaluation, lineage, or runtime installation.
- Behavioral effectiveness: not established by this implementation.

## Current Problem

The absence of a case file could not distinguish a deliberate no-signal decision from an omitted capture check. At the same time, failure-only capture could not preserve known-version correct-trigger, nearby correct-non-trigger, early-constraint, reviewer-context, or real-opportunity non-recurrence observations.

Requiring a note for every invocation would solve the ambiguity by creating low-value usage records, inflate target repositories, and turn absence-of-failure into a misleading quality metric. The refinement therefore requires an explicit decision and final-response status for medium/high-risk tasks while leaving no-signal tasks file-free.

## Trigger Model

The primary case trigger is exactly notable process friction, a review miss, packet gap, verification gap, or reusable lesson. Handoff is not an extra trigger, though a handoff can expose one of those signals. Evaluation candidacy remains a central distiller decision.

The designated-observation trigger is separate and narrow. It applies only when the user or orchestrator designates it before execution, or when context or a packet supplied by another authority or independently approved before execution identifies the opportunity. The executing agent cannot self-designate through its own packet; an opportunity discovered after execution begins can only be proposed for a future task. It can record success or a correct non-trigger only when the task presents a real opportunity to exercise or miss that behavior. Ordinary successful tasks do not become observations automatically.

A comparable known-version observation also requires the task's skill source/version from the designating authority or information already visible during the task. The executing agent must not query history. Without that version, the facts can be retained only as an ordinary primary-trigger supporting case or an explicitly version-inconclusive observation, not as known-version comparable or effectiveness evidence.

## Template Mapping

The previous `Context` fields become one `Task context` line plus a skill source/version that remains optional or `unknown` for ordinary cases but is required for a comparable designated observation. `What Happened`, `Why It Mattered`, `Trace`, and `Verification Gap` are replaced by `Expected And Observed` and `Action And Evidence`. `Privacy Boundary` moves under `Transfer Signal` beside one factual `Reusable signal` and the conditional independently designated `Comparable opportunity`.

`Pattern Tags`, standalone `Why It Mattered`, standalone `Trace`, standalone `Verification Gap`, and `Suggested Routing Back To evolving-agent-dev` are removed. Inbox, casebook, skill-refinement, evaluation, lineage, root-cause, change/no-change, promotion, and regression classification belong to the central evolving-agent-dev distiller rather than the target-project agent.

## Lightweight PDCA Correspondence

`Expected` supplies the planned or contractual comparison point; `Observed` and `Detection` preserve what happened and how it was found; `Action` records the local correction, decision, or no-change; `Verification` and `Remaining gap` close the local evidence loop; `Reusable signal` supports later transfer. This absorbs a lightweight plan-do-check-act discipline without creating a PDCA log, framework, validator, or retrospective requirement.

Entries normally keep each field to one or two sentences and stay near 100-200 English words or 150-300 Chinese characters. Consecutive planning/review/review-fix/follow-up-review phases default to one batch. Full chats, packets, diffs, logs, transcripts, and large code excerpts remain excluded.

## Local Evidence Ledger Consistency

The design note now mirrors the two-trigger model exactly: five primary triggers plus independently designated observation, with no separate handoff or evaluation-adjacent trigger. It also mirrors the required medium/high-risk decision, designated-authority and version boundaries, and the no-signal no-file rule. A no-op decision cannot create a narrative note or case-index entry. Per-invocation usage logging, telemetry, cross-project global ledgers, automated capture, and quality claims from usage counts remain out of scope; the optional usage summary remains unimplemented.

Target-project notes preserve local facts only, including successful or correct-non-trigger observations when explicitly designated. The central distiller retains lineage, comparability, root-cause, change/no-change, promotion, regression classification, and later outcome responsibilities.

## Role Separation

### Plan Decision

Implement only the user-accepted capture and template refinement within the four-file allowlist. Do not reopen the design or extend it into central evidence machinery.

### Test Responsibility

Verify trigger precision, no-op behavior, final-response status, template structure, removed routing fields, privacy and version boundaries, ledger consistency, unchanged frozen files, links, whitespace, and package validity.

### Implementation Responsibility

Change the canonical skill, case-note reference, local-evidence design note, and this report only. Preserve runtime state, central lineage, evaluations, policies, ADRs, casebook/inbox, fixtures, automation, and process version.

### Review Check

Confirm that the rule requires a capture decision rather than a note, ordinary success does not trigger observation, target-project users do not perform central classification, and no behavioral-effectiveness claim is made.

## Changed-File Allowlist

- `skills/coding-review-loop/SKILL.md`
- `skills/coding-review-loop/references/case-note-shape.md`
- `docs/skill-design/local-evidence-ledger.md`
- `docs/session-reports/2026-07-30-coding-review-loop-case-capture-refinement.md`

## Verification

- Start state: HEAD was `b36ac13bd88b689cf6dfb86f5aad476281587fa8` and `git status --short --untracked-files=all` was empty. No historical loaded skill version was inferred from the task date, repository state, or runtime linkage; runtime state was not queried or written.
- Read both required skills in full, then the minimum process, report, target-file, local-ledger, original capture, external-lineage, optional-version, central-distillation, correct-trigger, and correct-non-trigger sources. A terminology search covered case triggers, no-friction language, routing, usage logging and summaries, central responsibility, optional versions, and case indexes.
- Read the complete tracked diff and full untracked report during implementation. Final readback is repeated after this verification record is complete.
- `git diff --check` passed. The independent report check produced no whitespace warning and returned the expected `1` because `/dev/null` and the new report differ.
- The changed-file allowlist was exactly the four paths listed above. `review-packet-shape.md` was identical to HEAD, and no skill outside the two allowed `coding-review-loop` files differed from HEAD. No forbidden artifact, runtime installation, runtime-state file, fixture, harness, automation, index, usage summary, or telemetry file changed or was created.
- Structural assertions found one `Case Note Capture` section, one entry template, the three required template sections, and every required field. They confirmed the medium/high-risk decision, small/trivial exemption, no-signal no-file/index behavior, final appended/not-created status, pre-execution independent designation, the self-designation prohibition, future-task-only handling for late opportunities, ordinary-success non-trigger, optional omit/`unknown` version for ordinary cases, required source/version for comparable designated observations, the version-inconclusive fallback, and prohibition on inferring historical versions.
- Template assertions confirmed that `Pattern Tags`, standalone `Why It Mattered`, standalone `Trace`, standalone `Verification Gap`, `Suggested Routing Back To evolving-agent-dev`, and its routing candidates are absent from the active template. Target-project guidance assigns only local facts; central routing and classification remain with evolving-agent-dev.
- Ledger assertions confirmed the same five-primary-plus-designated trigger model, no standalone handoff or evaluation-adjacent trigger, successful/correct-non-trigger authority and version boundaries, no direct `improved`/`repeated`/`regression` classification, no-op index prohibition, no per-invocation usage logging, no telemetry or cross-project global ledger, no usage-count quality claim, and an unimplemented optional usage summary. The friction-only JSON example is explicitly illustrative and no JSONL index is implemented.
- Repository-relative link checks passed for all six linked Markdown paths in the changed scope. Privacy-negative checks found no URL, email, access-key pattern, private-key marker, or password/token/secret/API-key assignment.
- The first canonical-validator attempt failed before content validation with `ModuleNotFoundError: No module named 'yaml'`; no dependency was installed by the agent. After the user installed PyYAML, the same canonical `quick_validate.py` command returned `Skill is valid!` with exit `0`, and it passed again after the independent-review refinements. A Python-standard-library fallback also passed frontmatter delimiters, exactly the `name` and `description` keys, folder/name equality, the three expected package files, both SKILL-to-reference links, and all newly added repository-relative links. The canonical validator now passes.
- One pre-edit search command returned `1` because no `AGENTS.md` matched in the repository and its `&&` prevented the following terminology search from running. Independent replacement commands confirmed there is no repository-local `AGENTS.md` and completed the intended search. Remaining risk from that command failure is none for the intended checks; the behavioral risks below remain.

## Evidence Limits And Remaining Risk

This implementation establishes only that the accepted guidance and template are present and mechanically consistent. It does not establish that future medium/high-risk tasks make the decision, that triggered notes are appended, that no-signal tasks avoid empty records, that designated observations are comparable, that notes stay compact, or that central distillers can use them without reconstructing the original chat.

Remaining risk is behavioral and semantic: agents may omit the final status, attempt to self-designate, accept ambiguous approval timing, misstate the loaded version, over-designate ordinary successes, under-capture real friction, write shallow comparable-opportunity claims, or continue attempting central routing. Mechanical validation cannot establish those outcomes.

## Follow-Up Observation Standard

After independent review and later use, inspect an initial 5-10 natural notes or explicit capture decisions. Observe whether medium/high-risk tasks make the decision; signals produce notes; no-signal tasks stay file-free; designation is independent and established before execution; comparable observations carry the actual task source/version; version-inconclusive facts are not promoted; designated contexts capture correct triggers or nearby correct non-triggers with real opportunity; notes remain compact; central distillers avoid reconstructing raw chat; target-project agents avoid central routing; and decision overhead remains low. Do not manufacture notes to reach the sample size. Use the observations to decide whether to retain, narrow, or redesign the rule.

## Good

The refinement makes omission distinguishable from an explicit no-signal decision without turning case capture into invocation logging.

## Friction

One pre-edit search command used `&&` after an expected no-match `rg --files` check, so the second search did not run. Separate replacement checks found no repository-local `AGENTS.md` and completed the intended terminology search. No files had been changed when the command failed.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook or inbox candidate: no.
- ADR needed: no; the user-approved decision and this implementation report record the rationale.
- Evaluation candidate: no formal evaluation; wait for natural observations.
