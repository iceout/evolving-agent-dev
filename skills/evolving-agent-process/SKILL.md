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

Use this skill as a thin adapter for working in the `evolving-agent-dev` repository. It does not replace the repo docs or define a second process. The source of truth is the repository documentation, especially `README.md` and `docs/process-v0.2.md`.

The goal is to make Codex dogfood the process: read the right docs, keep v0.2 stable enough for skill v0.1, verify real work, and route evidence without inflating every task into a long workflow.

## When to Use

Use this skill when working in `evolving-agent-dev` on:

- `README.md`
- `docs/process-*.md`
- `docs/session-reports/*`
- `docs/casebook/*`
- `docs/policies/*`
- `docs/decisions/*`
- `docs/evaluations/*`
- `docs/skill-design/*`
- `skills/evolving-agent-process/*`
- this skill or its installation notes

Also use it when the user mentions dogfood, friction routing, Stage 0/v0.3 readiness, seed-vs-real evidence, session reports, casebook, policy notes, ADRs, evaluations, or the skill adapter in the context of this repo.

Do not run the full workflow for generic README/review/evaluation discussions outside this repo, simple `git status`-style questions, or review-only tasks with no requested edits.

## Source of Truth and Read Order

Read the smallest useful set of docs for the task.

Default read order:

1. `README.md`
2. `docs/process-v0.2.md`
3. Target files being changed or reviewed
4. `docs/session-reports/TEMPLATE.md` and `docs/session-reports/GUIDE.md` when session reporting is involved
5. Relevant `docs/policies/*.md`, `docs/decisions/*.md`, `docs/evaluations/*.md`, or `docs/casebook/*.md` only when needed

If this skill conflicts with repo docs, follow repo docs and record the mismatch as friction if it matters.

## Task Classification

Classify the task type first:

- `discussion-only`: user is discussing direction and not asking for file changes
- `review-only`: user asks for findings or review without edits
- `edit task`: user asks to change files or create artifacts

Then classify evidence/status flags separately:

- `dogfood`: yes/no
- `stage0-real-task-candidate`: yes/no
- `evidence`: seed / real / not evidence

Dogfood is not a task type. It is a status flag for edit tasks performed after the skill is installed and used by Codex.

## Response Language

Match the user's language in final responses unless the user explicitly requests another response language. If the user writes in Chinese, answer in Chinese unless they ask otherwise. Intermediate reasoning, terminal commands, file paths, code identifiers, commit messages, and existing English repository artifacts may remain English when appropriate. Do not translate existing repository docs by default.

## Minimal Workflow

### 1. Discussion-only

- Do not write artifacts by default.
- Do not write a session report by default.
- If the user explicitly asks to record friction, a decision, or a follow-up, write only that requested artifact using v0.2 routing.
- Keep the response short and focused on the decision or trade-off.

### 2. Review-only

- Read the reviewed files and the minimal relevant process docs.
- Provide findings first.
- Do not create a session report unless the user explicitly asks to record review friction.

### 3. Edit task

- Read `README.md`, `docs/process-v0.2.md`, and target files.
- Make the smallest necessary change.
- Do not expand v0.2 complexity unless the user explicitly asks.
- Verify before completion.
- For substantive changes, create or update a minimal session report.
- Route friction and follow-up through v0.2 rules.

### 4. Dogfood edit task

When `dogfood: yes`:

- Treat the task as a Stage 0 real task candidate.
- Write a session report for substantive changes.
- In the report, state dogfood status, Stage 0 evidence status, real verification, friction, and any evaluation candidate.
- If the skill feels too heavy, record friction first; do not immediately rewrite the skill unless it blocks execution.

## Artifact Routing

Use v0.2 routing:

- Raw task facts -> session report
- Micro friction -> `docs/casebook/inbox.md`
- Reusable friction -> casebook entry
- Repeated or high-impact rule hypothesis -> `proposed` policy note
- Stable default behavior -> `active` policy
- Trade-off or durable decision -> ADR
- High-signal, reproducible, judgeable regression -> evaluation
- Weak signal -> evaluation candidate only

Avoid recursion for session reports:

- Do not create another report just because you created a report.
- If the only change is adding the required report, that report can document itself briefly.
- If report editing reveals new friction, route it to the report follow-up or inbox instead of starting a report chain.

## Evidence Rules

- Bootstrap commits do not count as Stage 0 real tasks.
- Seed casebook entries and draft evaluations do not count toward Stage 0 exit criteria.
- Installed-skill dogfood edit tasks can count as Stage 0 real task candidates.
- Real evidence should link to a session report or friction log entry.
- Do not mark evidence as real just because it exists in the repo.

## Verification Rules

Before finalizing an edit task, perform real verification. Acceptable verification includes:

- reading modified files to confirm required sections exist
- checking `git diff`
- validating YAML frontmatter when editing skills
- running relevant tests or scripts if present
- recording manual verification explicitly when no command applies

If verification cannot complete, record the attempted verification, failure reason, alternative verification, remaining risk, and whether completion can be claimed. Do not use completion language when there was no real verification.

## Role Separation and Objections

Do not launch multiple agents by default. When v0.2 role separation triggers apply, explicitly separate:

- Plan Decision
- Test Responsibility
- Implementation Responsibility
- Review Check

Submit an objection only when the issue would lower acceptance criteria, violate role boundaries, expand scope, block verification, reveal a substantive conflict, or require user/orchestrator trade-off. Ordinary local corrections do not need objections.

## Installation Boundary

This file is the repo-tracked canonical draft. The local Codex-installed copy is runtime state.

For v0.1 installation, use this order:

- Confirm the runtime destination before writing files: use `$CODEX_HOME/skills/evolving-agent-process/` when `CODEX_HOME` is set; otherwise confirm the local Codex skill path, usually `$HOME/.codex/skills/evolving-agent-process/`.
- Install the whole tracked `skills/evolving-agent-process/` directory, not only `SKILL.md`.
- Prefer a directory symlink from the tracked directory to the runtime destination if Codex loads symlinked skills.
- If symlinks are unavailable, copy the whole directory and record the source commit, destination path, and refresh expectation in the session report.
- Verify the install by checking the runtime `SKILL.md` exists, contains `name: evolving-agent-process`, and either resolves to the tracked source for symlinks or matches the tracked source content for copies.
- Do not add scripts, agents configuration, or automation for v0.1 unless explicitly requested.

## Common Pitfalls

- Treating this skill as the source of truth instead of the repo docs.
- Continuing to polish v0.2 instead of using it.
- Counting bootstrap or seed artifacts as real Stage 0 evidence.
- Writing session reports for review-only tasks without being asked.
- Turning every session report into a long form.
- Forgetting a session report after substantive edits.
- Claiming completion without real verification.
- Promoting one friction item directly to policy, ADR, or evaluation.
- Over-triggering on generic README, review, or evaluation work outside this repo/process context.

## Final Checklist

For discussion-only:

- [ ] No artifact was written unless the user explicitly asked.
- [ ] Response focuses on the decision, trade-off, or question.

For review-only:

- [ ] Findings are first.
- [ ] No session report was written unless requested.

For edit tasks:

- [ ] Required repo docs were read.
- [ ] Changes are minimal and routed correctly.
- [ ] Verification is real and recorded.
- [ ] Session report exists for substantive changes.
- [ ] Dogfood and Stage 0 evidence status are stated when relevant.
- [ ] Final response lists changed files, verification, report path, and follow-up.
