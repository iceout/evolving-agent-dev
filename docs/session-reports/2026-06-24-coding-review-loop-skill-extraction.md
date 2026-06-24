# Session Report: coding-review-loop Skill Extraction

## Goal

First record the external-project skill trigger-boundary evidence, then create a minimal generic coding skill for real code projects by extracting the reusable v0.3 plan/review packet behavior validated in external dogfood.

## Status

- Dogfood: yes.
- Stage 0 evidence status: post-Stage 0 v0.3 skill extraction; not a Stage 0 task.
- Stage 0 counts: unchanged.
- v0.3 process status: no v0.3 process finalized.

## Changes

- First recorded one privacy-preserving inbox note that external real-code project plan artifacts sometimes stayed only in chat because the meta-process skill is scoped to this repo.
- Added `skills/coding-review-loop/SKILL.md` for real code projects that need non-trivial planning, repo-local review packets, high-risk bad-case debugging, implementation traceability, and independent review or cross-agent handoff.
- Added `skills/coding-review-loop/references/review-packet-shape.md` as a generic packet shape loaded only when a packet is needed.
- Did not modify `skills/evolving-agent-process/SKILL.md`.
- Did not create `docs/process-v0.3.md`, E008, policy, ADR, automation, tooling, metrics, subagent framework, or install scripts.

## Verification

- Python assertion block passed: `skills/coding-review-loop/SKILL.md` starts with YAML frontmatter, has only `name` and `description`, uses `name: coding-review-loop`, has a non-empty trigger description, and references `references/review-packet-shape.md`.
- Python assertion block passed: `skills/coding-review-loop/references/review-packet-shape.md` exists and contains all required sections, contract examples, and review-target / handoff-artifact language.
- Python assertion block passed: the new skill and reference do not mention Stage 0, E008, `docs/stage0-progress.md`, `docs/process-v0.2.md`, casebook routing, or session report routing.
- Python assertion block passed: only the expected files changed; the inbox entry is privacy-preserving and marked v0.3 external evidence only; `docs/process-v0.3.md` does not exist; `skills/evolving-agent-process/SKILL.md`, `docs/stage0-progress.md`, `docs/evaluations/behavior-cases.md`, and `docs/v0.3-review-packet-shape.md` are unchanged; no `## Case E008` exists.
- Skill-creator `quick_validate.py` was attempted but could not run because PyYAML is unavailable in this environment; the local assertion block covered the required frontmatter and structure checks.
- `git diff --check` passed; a temporary-index `git diff --cached --check` covering new untracked files also passed.

## Good

The reusable real-project behavior is now separated from evolving-agent-dev-specific process machinery, so it can trigger in external code repos without bringing tracker, casebook, or session-report routing into target projects.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no.
