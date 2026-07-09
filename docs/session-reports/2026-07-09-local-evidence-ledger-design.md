# Session Report: Local Evidence Ledger Design

## Goal

Design a conservative local-only evidence ledger for agent skill improvement, borrowing selected ideas from gstack local analytics, timeline, learnings, and eureka logs without importing telemetry, repo identity capture, dashboards, or runtime automation.

## Status

- Dogfood: yes.
- Stage 0 evidence status: post-Stage 0 skill-design note; not a Stage 0 task.
- Stage 0 counts: unchanged.
- v0.3 scope/status: design note only; no `docs/process-v0.3.md` created.

## External Input

gstack local analytics, learnings, timeline, and eureka patterns were used as design input, not project evidence.

## Changes

- Added `docs/skill-design/local-evidence-ledger.md`.
- Added a small `docs/v0.3-scope.md` backlog note for a local evidence ledger design note.
- Added this session report.
- Did not modify code files, current skill behavior, Stage 0 tracker, active policies, ADRs, casebook entries, evaluations, or runtime automation.

## Verification

- Read required process and design context:
  - `README.md`
  - `docs/process-v0.2.md`
  - `docs/v0.3-scope.md`
  - `docs/skill-design/external-framework-scan.md`
  - `skills/coding-review-loop/SKILL.md`
  - `skills/idea-framing-loop/SKILL.md`
  - `skills/bug-investigation-loop/SKILL.md`
  - `docs/session-reports/TEMPLATE.md`
  - `docs/session-reports/GUIDE.md`
- Selectively inspected gstack snippets about local analytics, telemetry, timeline, learnings, and eureka logs.
- `git diff -- docs/skill-design/local-evidence-ledger.md docs/v0.3-scope.md docs/session-reports/2026-07-09-local-evidence-ledger-design.md` showed only the tracked `docs/v0.3-scope.md` backlog note because the two new docs are untracked.
- `git status --short -uall` showed one modified tracked file and two intended untracked docs.
- `git diff --name-only -- docs/skill-design docs/v0.3-scope.md docs/session-reports docs/process-v0.3.md docs/process-v0.2.md docs/stage0-progress.md docs/policies docs/evaluations docs/casebook skills` showed only `docs/v0.3-scope.md` among tracked changes.
- `git diff --check -- docs/v0.3-scope.md` passed.
- `git diff --no-index --check /dev/null docs/skill-design/local-evidence-ledger.md` produced no whitespace errors; non-zero exit was expected for a new untracked file.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-09-local-evidence-ledger-design.md` produced no whitespace errors; non-zero exit was expected for a new untracked file.
- Manual readback confirmed the new docs describe design boundaries only and do not implement runtime automation, telemetry, dashboards, or logging behavior.
- Confirmed `docs/process-v0.3.md` does not exist.
- Confirmed no Stage 0 tracker, policy, evaluation, ADR, casebook, skill, or code file changed.

## Good

- The design keeps the valuable "tools should leave analyzable local traces" idea while narrowing it to high-signal evidence.
- The ledger explicitly separates case notes, optional indexes, rare insights, and optional usage summaries.
- The privacy boundary is more conservative than gstack: no remote telemetry, no repo basename, no branch, no product source paths, no prompts, no code, no customer identifiers, and no raw payloads by default.

## Friction

- What happened: The useful field `note_file` conflicts slightly with the default rule to avoid file paths.
- Why it felt wrong: A path can be privacy-sensitive in product repos, but a fixed `.agent/*` note path is useful for batch distillation.
- Impact: The design needed an explicit boundary: `note_file` is allowed only for approved local agent-note files, not arbitrary product paths.
- Category: `requirements`
- Root cause guess: The task intentionally balances distillation utility against a strict privacy boundary.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed: no.
- Evaluation candidate: no formal evaluation.
