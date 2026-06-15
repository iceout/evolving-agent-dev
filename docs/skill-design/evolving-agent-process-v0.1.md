# Codex Skill v0.1 Design: evolving-agent-process

## Purpose

Create a thin Codex skill that turns the `evolving-agent-dev` v0.2 process into a practical working protocol.

The skill is not an agent framework. It does not automate the process, replace repository documentation, or define new policy. It only reminds Codex when and how to read the repo docs, execute changes, verify work, and route evidence.

Source of truth remains the repository documentation:

- `README.md`
- `docs/process-v0.2.md`
- `docs/session-reports/TEMPLATE.md`
- `docs/session-reports/GUIDE.md`
- relevant `docs/policies/*.md`
- relevant `docs/decisions/*.md`
- relevant `docs/evaluations/*.md`
- relevant `docs/casebook/*.md`

## Freeze Statement

Freeze `docs/process-v0.2.md` as:

```text
good enough for skill v0.1
```

This means:

- v0.2 is not perfect.
- Do not continue expanding the process for theoretical completeness.
- Only fix gaps that affect skill execution, recording, verification, or artifact routing.
- Future process improvements should come from Codex dogfood data: session reports, friction, casebook entries, and evaluation candidates.

## Proposed Skill Name

Recommended name:

```text
evolving-agent-process
```

Alternatives considered:

- `evolving-agent-dogfood`
- `agent-process-dogfood`
- `evolving-agent-dev-process`

Prefer `evolving-agent-process` because the skill describes a process protocol, not only dogfood.

## Trigger Conditions

### Must Trigger

Trigger when Codex is working in the `evolving-agent-dev` repo and the task modifies or creates:

- `README.md`
- `docs/process-*.md`
- `docs/session-reports/*`
- `docs/casebook/*`
- `docs/policies/*`
- `docs/decisions/*`
- `docs/evaluations/*`
- the skill adapter itself

Also trigger when the user explicitly mentions:

- dogfood
- session report
- friction
- casebook
- policy note
- ADR
- evaluation
- artifact routing
- Stage 0 / v0.3
- Codex skill / skill adapter

### Should Trigger

Trigger lightly when the task affects process evidence or future statistics, even if the immediate edit is elsewhere:

- deciding whether friction should become case / policy / ADR / evaluation
- checking Stage 0 progress
- deciding whether an artifact counts as real evidence
- deciding whether the project is ready for v0.3
- applying review feedback to process-related artifacts

### Should Not Trigger Full Workflow

Do not trigger the full workflow for:

- pure review-only tasks with no file changes
- discussion-only tasks where the user explicitly says not to implement
- simple repo operations like `git status`, explaining commits, or browsing structure
- edits unrelated to the process or its evidence system
- temporary chat ideas not intended to become artifacts

Even when the full workflow does not trigger, Codex may still read minimal docs to avoid misclassification. If the user explicitly asks to record a friction, decision, or follow-up during discussion, perform only that requested routing action rather than the full edit workflow.

## Responsibility Boundaries

### Skill Responsibilities

The skill should help Codex:

- classify the task type as `discussion-only`, `review-only`, or `edit task`
- classify dogfood separately as an evidence/status flag, not as a mutually exclusive task type
- read the minimal necessary repo docs in the correct order
- distinguish bootstrap artifacts from Stage 0 real evidence
- distinguish seed evidence from real evidence
- avoid expanding v0.2 unless the user explicitly asks
- write a session report after substantive changes
- route micro friction to `docs/casebook/inbox.md`
- verify before completion
- avoid completion language when verification did not happen
- apply v0.2 routing before creating casebook, policy, ADR, or evaluation artifacts
- check artifact consistency before the final response

### Non-Responsibilities

The skill should not:

- design the future agent framework
- automate the full process
- create scripts by default
- calculate Stage 0 metrics unless asked
- promote every friction item into case / policy / evaluation
- count seed casebook or seed evaluation artifacts as real evidence
- force session reports for review-only tasks
- override explicit user instructions
- embed the full `docs/process-v0.2.md`
- become a second source of truth

## Read Order

### discussion-only

Use when the user is discussing direction and not asking for file changes.

1. Optionally read `README.md`.
2. Read `docs/process-v0.2.md` only if needed.
3. Do not write artifacts by default.
4. Do not write a session report by default.
5. If the user explicitly asks to record friction, a decision, or follow-up, write only that requested artifact using v0.2 routing.
6. Respond with proposal, trade-offs, or questions.

### review-only

Use when the user asks for review but not edits.

1. Read the reviewed file(s).
2. Read `README.md`.
3. Read `docs/process-v0.2.md`.
4. Read relevant policy / ADR / evaluation only when needed.
5. Output findings.
6. Do not write a session report unless the user asks to record review friction.

### edit task

Use when the user asks to modify process-related artifacts.

1. Read `README.md`.
2. Read `docs/process-v0.2.md`.
3. Read the target files.
4. If session reporting is involved, read `docs/session-reports/TEMPLATE.md` and `docs/session-reports/GUIDE.md`.
5. If testing or implementation policy is involved, read relevant `docs/policies/*.md`.
6. If role separation or objection is involved, read relevant ADRs.
7. Make the smallest necessary edits.
8. Verify.
9. Write or update a session report if the change is substantive.
10. Route any friction or follow-up according to v0.2.
11. Final response includes files changed, verification, and report path.

### Dogfood status

Dogfood is not a fourth task type. It is an evidence/status dimension applied on top of `edit task` after the skill is installed and Codex uses it to modify this repo.

When an edit task has dogfood status:

1. Mark the task as a Stage 0 real task candidate.
2. Follow the edit task read order.
3. Write a session report for substantive changes.
4. The session report should state:
   - this is a dogfood task
   - whether it counts as Stage 0 real task
   - what real verification was performed
   - what friction occurred
   - whether it produced an evaluation candidate
5. If the skill feels too heavy, record friction first; do not immediately rewrite the skill unless blocked.

## Minimal Workflow

### Step 1: Classify

Classify the task type:

```text
discussion-only / review-only / edit task
```

Then classify evidence/status flags separately:

```text
dogfood: yes/no
stage0-real-task-candidate: yes/no
seed-vs-real-evidence: seed / real / not evidence
```

Evidence rules:

- bootstrap artifacts do not count as Stage 0 real tasks
- installed-skill dogfood tasks can count as Stage 0 real tasks
- seed artifacts do not count toward Stage 0 exit criteria
- linked session reports or friction log entries are required for real evidence

### Step 2: Read

Read the minimal required docs.

Hard rules:

- Do not read the whole repository for simple tasks.
- Do not treat the skill as source of truth.
- If the skill conflicts with repo docs, follow repo docs.

### Step 3: Plan Lightly

Use a short plan only when editing.

The plan should state:

- which artifacts will change
- why those artifacts are the correct route
- how verification will happen
- whether role separation or objection is triggered
- whether a session report is required

### Step 4: Edit

Make only the smallest necessary change.

Constraints:

- Do not expand v0.2 complexity.
- Do not refactor unrelated documents.
- Do not reclassify seed evidence as real evidence.
- Do not add automation unless explicitly asked.
- Do not promote weak candidates into evaluations.

### Step 5: Verify

Before completion, perform real verification.

Acceptable verification includes:

- reading modified files to confirm key sections exist
- checking `git diff`
- checking Markdown structure or required keywords
- running relevant tests or scripts if any exist
- checking that the session report exists and links are sensible

If verification cannot complete, record:

- attempted verification
- failure reason
- alternative verification
- remaining risk
- whether completion can be claimed

### Step 6: Route Artifacts

After substantive changes:

- write a minimal session report
- send micro friction to `docs/casebook/inbox.md`
- promote only reusable friction to casebook
- promote repeated or high-impact rule hypotheses to `proposed` policy notes
- write ADRs only for trade-offs, future constraints, or likely why-questions
- create evaluations only for high-signal, reproducible, judgeable behavior regressions
- keep weak signals as evaluation candidates

### Step 7: Final Response

Keep the final response proportional to the task.

For discussion-only:

- answer the question or summarize the design trade-off
- mention artifact changes only if the user asked to record something

For review-only:

- findings first
- no session report status unless the user asked to record review friction

For edit tasks:

- files changed
- verification result
- session report path, if applicable
- whether the task counts as Stage 0 real evidence, when relevant
- friction / follow-up, if any

## Session Report Recursion Guard

Editing files under `docs/session-reports/` can itself trigger the session report rule. Avoid infinite recursion:

- If the task only updates `TEMPLATE.md`, `GUIDE.md`, or an existing report as a process artifact, write one normal session report for the substantive task.
- Do not create a second report just because the first report was created.
- If the only change is adding the required session report for a previous substantive task, that report can document itself briefly; no further report is required.
- If a session report update reveals new friction, route it to the inbox or follow-up section instead of starting another report chain.

## Installation Boundary

First implementation should be a personal dogfood install, not a repo-published framework.

Suggested boundary:

- Keep this design document in the repo under `docs/skill-design/`.
- Keep a version-tracked canonical `SKILL.md` draft in the repo at `skills/evolving-agent-process/SKILL.md` before installing it locally.
- Install by copying or symlinking the tracked `skills/evolving-agent-process/` directory into the local Codex skill location for personal dogfood.
- Prefer a directory symlink if Codex supports it; otherwise copy the whole directory and record the source commit plus destination path in the session report.
- Treat `skills/evolving-agent-process/SKILL.md` as reviewable source; the local installed copy is runtime state.
- Do not add scripts, agents configuration, or automation in v0.1.
- Do not require `agents/openai.yaml` for v0.1 unless Codex itself needs it in the local environment.
- After dogfood data shows the skill is useful, decide whether to publish it in-repo, package it as a plugin, or keep it personal.

Open installation questions for implementation time:

- Confirm the actual Codex skill directory on this machine before writing runtime files. Candidate locations may include `$CODEX_HOME/skills/evolving-agent-process/` or another Codex-configured skill path. Do not guess silently.
- Confirm whether Codex loads symlinked skill directories. If not, use a full directory copy and record how to refresh it from the repo-tracked draft.

## Role Separation

The skill does not require launching multiple agents.

When v0.2 triggers apply, Codex should explicitly separate responsibilities using minimal sections:

```markdown
## Role Separation

### Plan Decision
Goal, boundaries, acceptance criteria, and risk.

### Test Responsibility
External behavior to verify; implementation details not to bind.

### Implementation Responsibility
What changes; what does not change; acceptance criteria not lowered.

### Review Check
Test value, code simplicity, scope control, and verification result.
```

Use this when the task:

- changes tests and implementation together
- fixes a failing test
- crosses modules
- changes public APIs or data structures
- touches high-risk data, security, permissions, or migrations
- has unclear requirements
- reveals implementation being shaped only to satisfy tests

## Objection Rules

Do not use objections for ordinary local corrections.

Submit an objection only when the issue would:

- lower acceptance criteria
- violate role boundaries
- expand scope
- block real verification
- reveal a substantive conflict between requirement, test, implementation, or review
- require Orchestrator or user trade-off

## Common Pitfalls

The skill should explicitly warn Codex not to:

- keep polishing v0.2 instead of using it
- count bootstrap commits as Stage 0 real tasks
- count seed casebook or seed evaluations as real evidence
- write session reports for review-only tasks
- turn every report into a long form
- forget session reports after substantive edits
- claim completion without real verification
- promote one friction item directly to policy / ADR / evaluation
- copy the whole process into the skill and create a second source of truth

## v0.1 Smoke Test Plan

After installing the skill, run small manual smoke tests before counting dogfood data. These tests should use fresh Codex sessions when possible.

### Smoke Test A: Review-only does not over-write

Prompt: ask Codex to review a process artifact without editing.

Pass criteria:

- skill reads relevant docs
- output is findings-oriented
- no session report is created unless explicitly requested

### Smoke Test B: Discussion-only can record explicit friction

Prompt: discuss a workflow issue and explicitly ask to record one friction item.

Pass criteria:

- skill does not run the full edit workflow
- only the requested inbox or follow-up artifact is updated
- no unnecessary session report is created

### Smoke Test C: Edit task writes report and verifies

Prompt: make a small substantive change to an evaluation or policy artifact.

Pass criteria:

- skill reads README, process v0.2, and relevant target docs
- skill verifies the change with a reproducible command or clearly marked manual verification
- skill creates a minimal session report
- session report states dogfood status and Stage 0 evidence status

### Smoke Test D: Seed evidence is not counted

Prompt: ask whether existing seed cases/evaluations satisfy Stage 0 exit criteria.

Pass criteria:

- skill answers no
- skill cites seed-vs-real evidence rule
- no artifact is edited unless requested

## v0.1 Acceptance Criteria

The first skill version succeeds if Codex can:

- pass the smoke tests above
- detect when the skill applies without over-triggering on generic README, review, or evaluation mentions outside this repo/process context
- read the correct repo docs
- distinguish discussion, review, and edit tasks
- treat dogfood as an evidence/status flag rather than a separate task type
- remember that substantive edits require a session report
- route micro friction to inbox
- keep seed evidence separate from real evidence
- verify before completion
- avoid expanding process complexity

The first skill version does not need:

- automatic session report generation
- automatic Stage 0 metrics
- automatic friction classification
- automatic evaluation creation
- v0.3 readiness decisions
- multi-agent orchestration

## Canonical Draft Path

The repo-tracked canonical draft for v0.1 is:

```text
skills/evolving-agent-process/SKILL.md
```

Install this draft into Codex only after reviewing and validating it. Prefer a symlink if Codex supports symlinked skills; otherwise copy it and record the source commit plus destination path.

## Proposed SKILL.md Outline

```markdown
---
name: evolving-agent-process
description: "Use when working in evolving-agent-dev on process evidence: process docs, policies, casebook, evaluations, session reports, skill adapter, dogfood, friction routing, Stage 0/v0.3 readiness, or seed-vs-real evidence. Follow repo docs as source of truth."
version: 0.1.0
author: Bruce / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [dogfood, process, codex, agent-development]
    related_skills: []
---

# Evolving Agent Process

## Overview
Thin adapter for using process v0.2 inside Codex.

## When to Use
Repo/process scoped triggers and non-triggers. Avoid generic over-triggering outside evolving-agent-dev process work.

## Source of Truth
Repo docs and read order.

## Task Classification
discussion-only / review-only / edit task. Dogfood is an evidence/status flag.

## Minimal Workflow
Concrete steps for classify -> read -> plan -> edit -> verify -> route -> respond, with short examples.

## Artifact Routing
Session report, inbox, casebook, policy, ADR, evaluation.

## Evidence Rules
Bootstrap vs Stage 0 real evidence. Seed vs real.

## Verification Rules
Real verification and failure handling.

## Role Separation and Objections
Only triggered when v0.2 says so.

## Common Pitfalls
Avoid over-documenting, over-triggering, and double source of truth.

## Final Checklist
Task-type-specific checklist before final response.
```
