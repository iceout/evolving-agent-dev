# Session Report: Bug Investigation Loop Skill

## Goal

Add a lightweight repo-tracked Codex skill for real-project bug, failing test, stack trace, unexpected behavior, and regression investigations. The skill should establish root cause before fixes, stay separate from `coding-review-loop`, and borrow selected investigation patterns from gstack without importing gstack's broader ecosystem.

## Status

- Dogfood: yes.
- Stage 0 evidence status: post-Stage 0 skill addition; not a Stage 0 task.
- Stage 0 counts: unchanged.
- v0.3 scope/status: skill addition only; no `docs/process-v0.3.md` created.

## External Input

- `gstack-investigate` was used as design input, not accepted project evidence.
- Borrowed methodology was limited to root-cause-first debugging, symptom collection, reproduction, code-path tracing, recent-change checks, hypothesis testing, stop/escalate after repeated failed hypotheses, regression coverage, fresh verification, debug reporting, and sanitized external search.
- Telemetry, freeze hooks, gstack update/config/bootstrap behavior, cross-project learning automation, and broad runtime automation were intentionally not imported.

## Changes

- Added `skills/bug-investigation-loop/SKILL.md`.
- Added `skills/bug-investigation-loop/references/debug-report-shape.md`.
- Updated `README.md` tracked-skill and install examples to include `bug-investigation-loop`.
- Added this session report.

## Verification

- `git diff -- README.md skills/bug-investigation-loop/SKILL.md skills/bug-investigation-loop/references/debug-report-shape.md docs/session-reports/2026-07-03-bug-investigation-loop-skill.md` showed the tracked README change; new untracked files were inspected separately.
- `git status --short -uall` showed only `README.md` modified and the three expected new files untracked.
- `git diff --name-only -- README.md skills docs/session-reports docs/process-v0.3.md docs/process-v0.2.md docs/stage0-progress.md docs/policies docs/evaluations docs/casebook docs/v0.3-scope.md` returned only `README.md` because the new files are not tracked yet.
- `git diff --check -- README.md` passed with no output.
- `git diff --no-index --check /dev/null skills/bug-investigation-loop/SKILL.md` produced no whitespace errors; exit code 1 was expected for a new file diff.
- `git diff --no-index --check /dev/null skills/bug-investigation-loop/references/debug-report-shape.md` produced no whitespace errors; exit code 1 was expected for a new file diff.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-03-bug-investigation-loop-skill.md` produced no whitespace errors; exit code 1 was expected for a new file diff.
- Manual readback confirmed the new skill and reference contents.
- Frontmatter validation confirmed `name: bug-investigation-loop` and `description:`.
- `python3 /home/iceout/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/bug-investigation-loop` could not run because local Python lacks `yaml`; manual frontmatter assertions were used instead.
- `test ! -e docs/process-v0.3.md` confirmed no `docs/process-v0.3.md` was created.
- Status and path checks confirmed no Stage 0 tracker, policy, evaluation, ADR, casebook, or code file changed.
- Text checks confirmed the skill requires root cause before fix, hands off to `coding-review-loop` for medium/high-risk fixes, and treats gstack as design input rather than project evidence.

## Good

- The new skill fills a clear entry-point gap: bug investigation can start with root-cause evidence before any broader planning or review packet is needed.
- The workflow keeps `coding-review-loop` as the escalation path for medium/high-risk fixes instead of duplicating its planning/review responsibilities.
- External framework input was selectively distilled and bounded by this repo's evidence rules.

## Friction

- What happened: the skill-creator `quick_validate.py` script was present but failed because `yaml` is not installed in the local Python environment.
- Why it felt wrong: a standard skill validation path was unavailable for an environment/tooling reason unrelated to the new skill contents.
- Impact: manual assertions were needed to validate frontmatter instead of the helper.
- Category: `tooling`
- Root cause guess: the validation helper depends on PyYAML, but that dependency is not guaranteed in this repo environment.

## Proposed Follow-up

- Policy note candidate: none.
- Casebook candidate: none.
- ADR needed? no; this is a lightweight skill addition with the durable rationale captured in the session report.
- Evaluation candidate? watch future real bug-fix sessions for whether the skill prevents premature fixes and produces useful evidence chains.
- Tooling follow-up: consider documenting or vendoring the validation dependency if skill validation becomes a repeated need.
