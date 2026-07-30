# Agent Instructions

## Project Purpose

This repository is the working system for discovering, recording, and refining
how coding agents should behave. It is not the agent runtime implementation.
Prefer small, evidence-backed changes that make the learning loop more reliable
without creating a second process, tracker, or automation layer.

## Source Of Truth

This file is an operating map, not a replacement for repository documentation.
Read the smallest relevant set in this order:

1. `README.md` for purpose, current process, and artifact locations.
2. `docs/process-v0.2.md` for process and artifact-routing rules.
3. The files directly involved in the task.
4. `docs/session-reports/TEMPLATE.md` and
   `docs/session-reports/GUIDE.md` when a session report is required.
5. Relevant policy, decision, evaluation, casebook, skill-design, or v0.3
   documents only when the task touches them.

If this file conflicts with a more specific repository source of truth, follow
the more specific document and report the mismatch when it affects the task.

## Task And Skill Routing

- For process evidence, session reports, casebook, policy, decision,
  evaluation, skill-design, Stage 0, or v0.3 work in this repository, use
  `evolving-agent-process`.
- When creating or updating an existing skill package, also use
  `skill-creator` and validate the package without installing missing
  dependencies unless authorized.
- Use `coding-review-loop` for non-trivial work in real target code projects,
  not as a replacement process for evolving-agent-dev itself.
- Use `bug-investigation-loop` for root-cause investigation of bugs and
  regressions before implementing a fix.
- Use `idea-framing-loop` for product, process, tool, or agent-behavior ideas
  that need framing before planning or implementation.

Classify the request before acting:

- Discussion-only: analyze and advise; do not create artifacts by default.
- Review-only: provide findings first; do not modify files.
- Edit task: make the smallest authorized change and verify it.

## Evidence And Attribution

- Treat transferred target-project notes as external, privacy-preserving
  evidence, not internal dogfood or Stage 0 evidence.
- Do not infer a historically loaded skill version from a task date, current
  HEAD, commit ordering, or current runtime linkage.
- Keep repository rule state separate from source-task attribution.
- Keep evidence recording, change decisions, implementation, and later
  effectiveness observation distinct when the established lineage uses those
  stages.
- A present rule proves only that canonical guidance exists. It does not prove
  triggering, execution, compatibility, improvement, or regression prevention.
- A task without a real opportunity for the relevant behavior to fail is not
  positive effectiveness evidence.
- Multiple findings or review rounds in one workflow normally form one evidence
  batch. Do not count them as independent repetitions without independent task
  or domain evidence.
- Preserve explicit no-change, inconclusive, and failed-hypothesis decisions;
  do not record only successful modifications.

Target-project users record local facts. Central distillation in this repository
owns privacy-safe source IDs, normalization, root-cause hypotheses,
deduplication, change attribution, promotion, and later outcome classification.

## Artifact Routing

- Substantive edits require a minimal session report.
- Micro or scattered friction goes to `docs/casebook/inbox.md` only when the
  task actually produces such friction.
- Reusable historical friction may become a casebook entry.
- Repeated or high-impact rule hypotheses may become proposed policy notes;
  stable defaults require stronger evidence before becoming active policy.
- Use ADRs for durable trade-offs and evaluations for reproducible, judgeable
  behavior regressions. Do not promote weak signals automatically.
- Reuse the existing central lineage and current-state view. Do not create a
  parallel ledger, tracker, process document, or automation system unless the
  user explicitly authorizes that scope.

## Editing And Verification

- Preserve unrelated user changes and dirty-worktree content. Never revert or
  clean files you did not change.
- External source notes are read-only unless the user explicitly asks to edit
  them.
- Do not broaden a recording task into a decision, a decision into an
  implementation, or an implementation into an effectiveness claim.
- Do not commit, install runtime skills, add dependencies, or perform external
  side effects unless requested or required by the authorized task.
- Prefer the smallest changed-file allowlist and check linked artifacts for
  stale status, counts, paths, or verification semantics.
- Read the complete final diff and all new files, run `git diff --check`, and
  perform the relevant tests or structural checks.
- When validation fails, record the attempted check, failure reason,
  alternative verification, remaining risk, and whether completion can still
  be claimed. Never report a fallback as the canonical validator passing.

## Privacy And Scope Traps

Do not copy external project identities, private absolute paths, endpoints,
credentials, recipients, account or customer identifiers, sensitive payloads,
or large source excerpts into repository evidence. Generalize details while
preserving the engineering behavior needed for review.

Avoid these common scope errors:

- case count is not effectiveness evidence;
- packet improvement is not implementation verification;
- review detection is not prevention;
- unknown-version evidence cannot establish post-change causality;
- one case should not produce a feature-specific checklist by default;
- current-state documents should not contain wording that becomes false as soon
  as the same change is committed.

Keep this file stable. Link to changing state in repository sources rather than
copying commit IDs, lineage status tables, Stage counts, or temporary backlog.
