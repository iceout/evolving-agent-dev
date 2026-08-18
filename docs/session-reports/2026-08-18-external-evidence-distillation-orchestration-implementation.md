# Session Report: External-Evidence Distillation Orchestration Implementation

## Goal

Implement only ADR-0002's narrow `evolving-agent-process` routing entry and
reference workflow for Conditional Orchestrated Distillation. This is an
implementation task, not a new decision, external evidence distillation, or
effectiveness observation.

## Status

- Skills used: repo-tracked `evolving-agent-process` and system
  `skill-creator`.
- ADR source: commit `19556d6` and
  [ADR-0002](../decisions/ADR-0002-external-evidence-distillation-orchestration.md).
- Task handoff state: the reference-guidance implementation is complete in the
  working tree and is left uncommitted for independent review; full workflow
  executability is not established and commit authorization is separate.
- Behavioral effectiveness, fresh-context review quality, and real workflow
  capability: not established.
- External case distillation, central lineage update, Stage 0 evidence, and
  outcome promotion: none.

## Changes

- Added a short conditional routing entry to
  `skills/evolving-agent-process/SKILL.md`. The `name` and `description`
  trigger metadata remain unchanged; the existing unsupported `author` and
  `version` keys were removed only after the canonical validator required it.
- Added the single detailed
  [orchestration reference](../../skills/evolving-agent-process/references/external-evidence-distillation-orchestration.md).
- Updated ADR-0002 to a stable accepted status and linked this implementation
  record without changing the A/B/C decision.
- Added this report. No runtime installation, agent metadata, automation, or
  other process artifact changed.

## Decision Mapping

- Phased admission: conditions 1, 2, 3, and 7 plus no obvious scope
  contradiction authorize only reading the reference and starting read-only
  analysis. The scope screen is not an eighth trigger.
- Analysis output: analysis determines existing-lineage reuse and whether any
  decision, implementation, or promotion is required, then produces the bounded
  in-memory card for conditions 4, 5, and 6.
- Edit admission: the reference requires all seven ADR conditions before the
  first bounded edit and rejects domain terms, note count, task size, ordinary
  success, and agent usage as substitutes. Failed analysis returns
  `needs decision` or an objection without editing.
- Card: analysis is read-only and returns a task-local, in-memory Distillation
  Card that is frozen before any bounded edit and never persisted.
- Review isolation: review is read-only, excludes the card and parent
  conclusions, and consumes only the source, minimum repository context, final
  diff/new files, and fixed rubric.
- Correction cap: at most one mechanical/documentary correction and one
  re-review; route, decision, classification, privacy judgment, and scope cannot
  change.
- Stop and degradation: unclear/new route, substantive judgment, artifact
  expansion, pilot, promotion, or unavailable/unverifiable fresh context returns
  `needs decision` or an objection, with the existing manual path as an honest
  option.
- Version attribution: the external source task's historical
  `coding-review-loop` version is separate from the orchestration guidance
  version loaded for an observation. An unversioned orchestration observation
  is inconclusive and cannot support retain, narrow, redesign, or promotion.

## Capability Verification

The platform accepted a child-agent request that asked for no inherited
conversation turns, so one neutral, read-only probe was launched with no source
note, privacy data, Distillation Card, repository content, task conclusions, or
permission to use tools. The child returned:

```text
probe_result: fresh-prompt-context received
prior_user_task_context_visible: yes
```

Result: `inconclusive`. The probe establishes only that the platform launched a
child from a fresh/no-context request and delivered the neutral prompt. Because
the child reported prior task context as visible, it does not establish the
fresh-prompt-context isolation required by the workflow. Under the reference,
an actual task on the same unverifiable boundary must return `needs decision`
or offer the existing manual path; it must not claim a fresh-context review.

The probe did not inspect or edit repository files and created no artifact. It
does not prove filesystem non-visibility, model independence, evidence
independence, review quality, end-to-end workflow behavior, or effectiveness.

## Role Separation

### Plan Decision

Implement the accepted ADR within the exact four-file allowlist. Do not reopen
A/B/C or broaden the task into runtime automation or evidence work.

### Test Responsibility

Verify trigger count, card and reviewer boundaries, correction cap, stop and
degradation behavior, version attribution, package validity, links, privacy,
stale language, allowlist, and whitespace.

### Implementation Responsibility

Change only the skill routing entry, one reference, ADR status/link, and this
report. Preserve trigger metadata; make only validator-required frontmatter
changes. Preserve runtime state, central lineage, evidence outcomes, and all
excluded artifacts.

### Review Check

Confirm the skill stays concise, the reference is the only detailed carrier,
the probe is reported as inconclusive, and implementation presence is not
described as behavioral proof.

## Verification

- Start state: `HEAD` was
  `19556d6a104c6b0ba52f232dfac52cc2af87945c`, commit `19556d6` was the
  current `HEAD`, and the complete worktree and staging area were empty.
- Read every user-required source in full and also read `docs/v0.3-scope.md` as
  required by `AGENTS.md` for follow-up to an accepted refinement.
- Capability probe: the parent sent one no-context-request child only the
  neutral probe prompt and no permission to use tools. Its reported prior-context
  visibility makes the result `inconclusive`; static degradation behavior, not
  fresh-context success, is the applicable verification result.
- Direct execution of the canonical `quick_validate.py` stopped before content
  validation with exit `126` because the script was not executable. Running the
  same canonical script through `python3` first rejected the pre-existing
  `author` and `version` keys. After the validator-authorized removal, the same
  command returned `Skill is valid!` with exit `0`; no dependency was installed.
- `git diff --check` passed. Independent `git diff --no-index --check` checks
  for the new reference and report produced no whitespace warnings and exited
  `1` only because each file differs from `/dev/null`.
- Structural checks found exactly seven numbered positive triggers; one
  directly linked detailed reference; phased pre-analysis, analysis, and edit
  admission; an in-memory, task-local, non-ledger card; reviewer input that
  excludes the card and parent conclusions; one correction and one re-review
  caps; honest `needs decision` degradation; and separate external-source and
  orchestration-observation version attribution.
- The unrecorded-orchestration-version path is explicitly
  version-inconclusive and cannot support retain, narrow, redesign, or outcome
  promotion. Negative checks found no default multi-agent path, automatic
  intake/promotion/commit, telemetry, dashboard, JSONL index, or API/CLI binding.
- ADR-0002 has a stable accepted status and a valid link to this report. It
  states that guidance presence does not establish platform capability,
  fresh-context review quality, effectiveness, reduced effort, or an external
  evidence outcome.
- The changed-file allowlist is exactly the four authorized paths and the
  staging area is empty. No other skill/reference, agent metadata, root/process
  document, ledger, lineage, evidence artifact, runtime state, fixture, harness,
  script, or automation differs from the start state.
- Every new repository-relative Markdown file link exists and the reference's
  internal contents links match its headings. Privacy-negative checks found no
  external identity, private absolute path, endpoint, payload, credential,
  recipient, or account/customer identifier. The only commit ID added is the
  user-required ADR source in this immutable task report, not a future-state
  claim.
- Read the complete new reference and report and the tracked diff during
  implementation. A final complete readback follows this verification record.

## Remaining Risk

- A platform's fresh-context boundary may be weaker than requested or hard to
  verify honestly.
- A reviewer may still anchor on source or repository wording despite role
  separation.
- The Distillation Card may omit a decision-relevant fact or overbound the
  allowed change.
- Static degradation text and this minimal probe do not prove the end-to-end
  workflow.
- One correction may be insufficient, which must lead to user review rather
  than silent extra iterations.
- Whether the workflow actually reduces forwarding cost remains unobserved.

## Good

The implementation keeps the main skill compact and defines one narrowly
scoped reference protocol in a single directly linked file.

## Friction

Independent review found a sequencing deadlock: the initial routing text
required all seven gates before loading the reference or starting analysis,
while conditions 4-6 can only be established by analysis and condition 6 is the
analysis-produced card. The correction separates pre-analysis admission,
analysis output, and edit admission without removing or weakening any gate.

The platform accepted a no-context child request, but the child reported prior
task context as visible. This makes capability verification inconclusive and
exercises the decision's honest-degradation boundary without creating external
evidence or an effectiveness claim.

The canonical validator script lacked executable permission, so direct
execution stopped before validation. Running the same script through Python
then rejected the pre-existing `author` and `version` frontmatter keys; the
user-authorized validator exception required their removal while leaving
`name` and `description` unchanged.

## Proposed Follow-Up

- Independently review this four-file change before a separately authorized
  commit.
- After commit, and only on a platform that can honestly verify fresh-context
  condition 7, observe natural, user-selected record-only cases that record the
  actually loaded orchestration guidance/source version. The current
  inconclusive probe does not qualify this platform for that path.
- Do not manufacture a fixture, usage count, or repeated probe to prove
  effectiveness.
- Policy, casebook, and evaluation candidate: none.
