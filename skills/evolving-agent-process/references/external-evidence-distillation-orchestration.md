# External-Evidence Distillation Orchestration

## Contents

- [Purpose And Applicability](#purpose-and-applicability)
- [Seven Positive Triggers](#seven-positive-triggers)
- [Baseline And Capability Handling](#baseline-and-capability-handling)
- [CLI Review Fallback](#cli-review-fallback)
- [Analysis And Distillation Card](#analysis-and-distillation-card)
- [Bounded Implementation](#bounded-implementation)
- [Fresh-Context Review](#fresh-context-review)
- [Correction Cap And Stop Conditions](#correction-cap-and-stop-conditions)
- [Observation Version And Final Report](#observation-version-and-final-report)

## Purpose And Applicability

Use this optional conditional workflow only for an existing-lineage,
`record-only` distillation of a user-selected, privacy-reviewed, read-only
external source note. It is not the default for process work or a general
multi-agent requirement.

This workflow does not discover external sources, ingest notes in batches,
automate central routing, or promote evidence. It does not apply merely because
a case note exists, multiple notes exist, a task is large, a task succeeded, a
domain term appears, or agents were used.

## Seven Positive Triggers

All seven conditions must be established before any bounded record-only edit:

1. The user explicitly requests external evidence distillation.
2. The user explicitly provides a source note that is read-only and
   privacy-reviewed.
3. The task mode is `record-only`.
4. Analysis can reuse an existing central lineage.
5. The task requires no new rule, lineage, policy, ADR, evaluation, synthetic
   pilot, or outcome promotion.
6. The in-memory Distillation Card clearly bounds the files and content that
   may change.
7. An available review surface provides the required fresh-context boundary:
   a direct review subagent or a validated new CLI review session.

### Pre-Analysis Admission

Before starting an analysis subagent, establish conditions 1, 2, 3, and 7 and
confirm that the request has no obvious scope contradiction. An obvious
contradiction includes an explicit request for a new lineage, rule or skill
change, decision, policy, evaluation, synthetic pilot, or outcome promotion.
This screen is not an eighth trigger and does not decide conditions 4-6. Passing
it authorizes only loading this reference and starting read-only analysis, not
editing.

### Analysis Stage

Use the read-only analysis subagent to determine conditions 4 and 5 and produce
condition 6, the bounded in-memory Distillation Card. If analysis cannot
establish any of those conditions, return `needs decision` or an objection and
make no edit.

### Edit Admission

Freeze the Distillation Card and confirm all seven conditions before the first
bounded record-only edit. A failed or unclear condition prevents editing; it
does not authorize a new route or a broader task.

## Baseline And Capability Handling

Before any edit:

- inspect the complete worktree and stop on overlapping uncommitted changes;
- read the user-provided source note as read-only; and
- read only the repository sources needed to establish lineage, attribution,
  artifact routing, and verification boundaries.

Use an applicable capability result or explicitly probe whether the selected
surface can start the required fresh-context reviewer. Here, fresh context
means only that the reviewer does not inherit the Distillation Card or the
parent's conclusion-oriented reasoning. It does not mean filesystem
non-visibility, model independence, or
evidence independence.

Treat execution capacity separately from context capability. If a direct review
subagent cannot start, automatically try the applicable CLI path below within
the authorized task. A thread-limit error on one surface does not establish
that all review paths are unavailable.

If no available path has a supportable context boundary, stop with
`needs decision` and explain the limitation. The orchestrator may suggest the
existing manual evidence path, but must not run an in-context reviewer and call
it fresh-context. Capability absence is not an evidence failure, lineage
conclusion, or reason to expand scope.

Do not bind this workflow to a particular child-agent API. Use only a platform
facility whose actual context boundary can be stated accurately.

## CLI Review Fallback

Use a new `codex review` process for reviewer-start failures such as exhausted
subagent capacity, when the CLI's version/configuration and context semantics
are covered by an applicable validation. In the repository, read
`docs/session-reports/2026-09-08-cli-review-context-validation.md` relative to
the repository root for the current controlled CLI evidence.
It supports non-inheritance of a tested existing conversation, not complete
model-input isolation. Revalidate on material changes to the execution surface,
context semantics, or relevant configuration; do not repeat the probe per task.

- Start in the target repository with a read-only reviewer sandbox. Supply
  only the Fresh-Context Review inputs and fixed rubric through a temporary
  prompt file or structured stdin. Explicitly request staged, unstaged, and
  relevant untracked changes, including the new report. For the validated CLI:
  `codex review -c 'sandbox_mode="read-only"' -` reads the custom prompt from
  stdin. Custom prompts conflict with `--uncommitted`, `--base`, and `--commit`;
  do not combine them. Check local help when the installed syntax differs.
- Do not resume or fork a prior conversation, pass chat transcripts or the
  Distillation Card, or ask the reviewer to read session history. Ordinary
  repository guidance/configuration remains visible; keep conclusion-oriented
  analysis out of the reviewer inputs and files.
- Attempt the applicable CLI alternative without another task-scope permission
  question. If the outer sandbox blocks CLI initialization, use the platform's
  required permission mechanism; keep the reviewer sandbox read-only. Do not
  bypass permissions, replace provider configuration, or weaken the rubric.
- Inspect the actual review result and process status. Starting a process or
  exiting successfully without a substantive review is not approval. Preserve
  failures and unresolved findings; use `needs decision` when execution or the
  context boundary cannot be established after the applicable fallback.
- This fallback replaces only an unavailable reviewer execution path. It does
  not replace the analysis subagent, retry a substantive finding with another
  reviewer, reset the one-correction/one-re-review limit, or broaden the task.
  Report which surface ran and the precise evidence supporting its boundary.

## Analysis And Distillation Card

The analysis subagent is read-only. It must not edit, commit, or create an
artifact. It returns one task-local, in-memory Distillation Card and must not
write the card into the repository, source project, global ledger, or case
index.

The card must contain:

- task mode;
- source and evidence-batch boundary;
- candidate existing lineage and privacy-safe alias/case ID;
- evidence-backed mapping;
- explicit non-routes;
- state invariants;
- allowed and forbidden changes;
- evidence limits and prohibited attribution or effectiveness claims; and
- required verification.

The orchestrator freezes the card before editing and permits only the
`record-only` changes it authorizes. If analysis cannot confirm the existing
lineage, privacy boundary, version attribution, allowed files, or evidence
mapping, return `needs decision` or an objection. Do not choose or create a new
route autonomously.

## Bounded Implementation

Apply only the record-only edits authorized by the frozen card. Keep evidence
recording separate from decisions, implementations, policy, evaluations,
synthetic pilots, and outcome promotion.

Do not infer the external source task's historical skill version from its date,
the current `HEAD`, commit ordering, or a runtime symlink. The user retains
control over source provision, task start, result acceptance, and commit
authorization. Never run `git add` or `git commit` automatically.

## Fresh-Context Review

The reviewer, whether a direct subagent or CLI session, is read-only. It must
not edit or run `git add` or `git commit`. Do not provide it with the
Distillation Card or the parent's conclusion-oriented reasoning.

Provide only:

- the source note;
- the minimum necessary repository sources;
- the final diff and new files; and
- this fixed rubric.

The reviewer returns only `approval`, findings, `blocked`, or `inconclusive`.
The rubric checks:

- source facts against the normalized mapping;
- the existing-lineage route and explicit non-routes;
- privacy boundaries;
- unknown-version attribution;
- state drift;
- the changed-file allowlist;
- stale language;
- overclaiming;
- verification semantics; and
- whether a source-specific mechanism was incorrectly made into a generic
  rule.

This is role-separated review intended to reduce anchoring. It is not proof of
evidence independence, platform isolation, review quality, or behavioral
effectiveness.

## Correction Cap And Stop Conditions

The orchestrator may make at most one automatic correction for a mechanical or
documentary finding, followed by at most one re-review. A correction must not
change the route, decision, evidence classification, privacy judgment, or
allowed scope. Return any remaining or substantive finding to the user; do not
iterate indefinitely.

Stop with `needs decision` or an objection when:

- a new lineage is needed or the existing route is unclear;
- a skill/reference, policy, ADR, evaluation, casebook, or process version
  would need to change;
- a synthetic pilot would begin;
- unknown-version source evidence would be used to infer `improved`,
  `repeated`, regression, or effectiveness;
- review exposes a substantive mapping or privacy judgment; or
- no available review surface provides a verified applicable context boundary,
  after the CLI fallback has been considered or attempted as applicable.

## Observation Version And Final Report

For every future orchestration observation, record the orchestration
guidance/source version actually loaded. The external source task's historical
`coding-review-loop` version may remain unknown; that limits causal claims
about the old source task, not attribution of a versioned orchestration
observation.

If the orchestration implementation version is unrecorded, classify the
observation as version-inconclusive. It cannot support a retain, narrow, or
redesign conclusion or outcome promotion.

The final response must report at least:

- the mode and whether the orchestrated path was entered;
- the capability check result and its precise boundary;
- whether an in-memory Distillation Card was produced and used;
- the review result;
- changed files;
- verification performed;
- external source-version versus orchestration-version attribution;
- facts not established; and
- whether the worktree was left uncommitted.

Do not require a case note for every task, write a usage log, or turn the final
response into a permanent tracker.
