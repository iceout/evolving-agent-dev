# Session Report: Skill Note Capture

## Goal

Reduce manual copy/paste friction when useful real-project `coding-review-loop` cases or `idea-framing-loop` ideas need to flow back into evolving-agent-dev, while keeping capture lightweight, privacy-preserving, triggered, and local to the target repo.

## Status

- Dogfood: yes
- Stage 0 evidence status: post-Stage 0 skill evidence-capture refinement; not a Stage 0 task
- Stage 0 counts: unchanged
- v0.3 scope/status: skill/reference refinement only; no `docs/process-v0.3.md` created

## Changes

- Added triggered case note guidance to `skills/coding-review-loop/SKILL.md`.
- Added `skills/coding-review-loop/references/case-note-shape.md` as a compact privacy-preserving template for high-signal real-project review cases.
- Added triggered idea note guidance to `skills/idea-framing-loop/SKILL.md`.
- Added `skills/idea-framing-loop/references/idea-note-shape.md` as a compact privacy-preserving template for reusable idea/process notes that do not need a full idea brief.
- Added a local-transfer artifact boundary so notes are not included in product commits unless explicitly requested or established by target repo convention.
- Added an inbox friction note about manual real-project evidence transfer.

## Verification

Completed verification:

- `git diff -- skills/coding-review-loop/SKILL.md skills/coding-review-loop/references/case-note-shape.md skills/idea-framing-loop/SKILL.md skills/idea-framing-loop/references/idea-note-shape.md docs/casebook/inbox.md docs/session-reports/2026-07-02-skill-note-capture.md` showed only the intended tracked-file changes; untracked new files are checked separately because normal `git diff` does not show them.
- `git status --short -uall` showed modified skill/inbox files and the three new untracked markdown files only.
- `git diff --name-only -- skills/coding-review-loop skills/idea-framing-loop docs/casebook docs/session-reports docs/process-v0.3.md docs/process-v0.2.md docs/stage0-progress.md docs/policies docs/evaluations docs/v0.3-scope.md` showed only `docs/casebook/inbox.md`, `skills/coding-review-loop/SKILL.md`, and `skills/idea-framing-loop/SKILL.md`; this command does not list untracked files.
- `git diff --check -- skills/coding-review-loop/SKILL.md skills/idea-framing-loop/SKILL.md docs/casebook/inbox.md` passed with no output.
- `git diff --no-index --check /dev/null skills/coding-review-loop/references/case-note-shape.md`, `git diff --no-index --check /dev/null skills/idea-framing-loop/references/idea-note-shape.md`, and `git diff --no-index --check /dev/null docs/session-reports/2026-07-02-skill-note-capture.md` produced no whitespace-error output. Exit code `1` is expected because `/dev/null` differs from each new file.

Manual verification:

- Confirmed no `docs/process-v0.3.md` was created.
- Confirmed no Stage 0 tracker, policy, evaluation, ADR, or code file was modified.
- Confirmed wording says note capture is triggered by notable friction/reusable lesson/handoff candidate, not mandatory for every skill use.
- Confirmed wording treats notes as local transfer artifacts by default and says not to include them in product commits unless explicitly requested or established by target repo convention.
- Confirmed transferred notes are external privacy-preserving evidence, not internal accepted Stage 0 evidence.
- Confirmed idea notes do not replace idea briefs; they are lighter notes for reusable lessons/future ideas.

## Good

- The change keeps real-project capture local and privacy-preserving instead of introducing sync automation.
- The default paths are stable enough for batch transfer but optional enough to respect target repo conventions.
- The templates route future notes toward inbox, casebook, skill refinement, or evaluation watchlist without promoting them automatically.

## Friction

- What happened: Useful external cases and process ideas were repeatedly copied from chat into evolving-agent-dev by hand.
- Why it felt wrong: Manual transfer loses structure and makes batch distillation harder.
- Impact: High-signal review misses, packet gaps, verification gaps, and process ideas can be lost or re-summarized inconsistently.
- Category: `process` / `tooling` / `context`
- Root cause guess: The skills had review/idea artifacts, but no lightweight triggered capture shape for privacy-preserving evidence notes in target repos.

## Proposed Follow-up

- Policy note candidate: no; this is skill guidance, not a stable active policy.
- Casebook candidate: no standalone casebook entry yet; inbox entry is enough.
- ADR needed? no; no durable trade-off beyond the existing privacy/evidence boundary.
- Evaluation candidate? not yet; watch whether captured notes reveal a judgeable repeat failure.
