# Session Report: idea-framing-loop skill

## Goal

Create a minimal generic `idea-framing-loop` skill for early-stage idea clarification before planning, coding, or skill changes.

## Changes

- Added `skills/idea-framing-loop/SKILL.md` with required frontmatter only and concise instructions for one-question-at-a-time idea framing.
- Added `skills/idea-framing-loop/references/idea-brief-shape.md` as an optional lightweight idea brief shape.
- Dogfood: yes.
- Stage 0 evidence status: post-Stage 0 v0.3 skill addition; not a Stage 0 task.
- Stage 0 counts unchanged.
- No v0.3 process finalized.
- No E008, policy, ADR, automation, tooling, metrics, subagent framework, runtime install, or sync was created.
- This is a minimal adaptation of useful idea-framing mechanisms observed in external tools, not a full copy of their workflow, voice, telemetry, browser companion, YC pitch, or all-project brainstorming model.

## Verification

- `git status --short` showed only the new session report and `skills/idea-framing-loop/` as untracked.
- Python validation confirmed `skills/idea-framing-loop/SKILL.md` starts with YAML frontmatter, has only `name` and `description`, uses `name: idea-framing-loop`, has a non-empty description, and references `references/idea-brief-shape.md`.
- Python validation confirmed `skills/idea-framing-loop/references/idea-brief-shape.md` exists and contains all required idea brief sections.
- Python validation confirmed the new skill files do not mention the forbidden tracker or routing terms.
- The `skill-creator` quick validation script could not complete because the local Python environment lacks `yaml`; the custom Python validation above covered the required frontmatter, naming, reference-link, and section checks.
- `test ! -e docs/process-v0.3.md` passed.
- `git diff --name-only -- docs/stage0-progress.md docs/evaluations/behavior-cases.md docs/process-v0.2.md skills/evolving-agent-process skills/coding-review-loop` produced no output.
- `rg -n '^## Case E008' . || true` produced no matches.
- `git diff --check` passed.
- Temporary-index `git diff --cached --check` covering the new untracked files passed.

## Good

The skill stays focused on early clarification and keeps small ideas in conversation unless an idea brief is useful for review, handoff, future planning, or implementation.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: none.
- Casebook candidate: none.
- ADR needed? no; this is a narrow skill addition without a durable process trade-off.
- Evaluation candidate? no; no judgeable regression fixture was created.
