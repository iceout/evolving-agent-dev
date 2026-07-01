# Session Report: Coding Review Loop Runnable Acceptance

## Goal

Lightly refine the `coding-review-loop` review packet shape so high-risk requirements that promise dry-runs, shadow runs, reports, default entrypoints, or script behavior become executable acceptance items. Keep the change scoped to skill/reference refinement and privacy-safe friction routing; do not create a full v0.3 process, active policy, formal evaluation, ADR, or code change.

## Status

- Dogfood: yes
- Stage 0 evidence status: post-Stage 0 coding-review-loop refinement; not a Stage 0 task
- Stage 0 counts: unchanged
- v0.3 scope/status: skill/reference refinement only; no process-v0.3 created

## Changes

- Added `Runnable Acceptance / Entrypoints` to `skills/coding-review-loop/references/review-packet-shape.md`.
- Added a P0/P1 or acceptance-critical `Requirement Traceability Checklist` mapping requirements to implementation path, user-facing entrypoint or default config, expected output/report fields, and verification command/test.
- Expanded `Verification Plan` guidance to require existing entrypoint tests when runnable scripts, CLIs, jobs, defaults, or report outputs change.
- Added a narrow `Implementation Trace` reminder to `skills/coding-review-loop/SKILL.md` for promised dry-runs, shadow reports, exports, scripts, CLIs, and default entrypoints.
- Appended a privacy-safe friction item to `docs/casebook/inbox.md`.

## Verification

- `git diff -- skills/coding-review-loop/SKILL.md skills/coding-review-loop/references/review-packet-shape.md docs/casebook/inbox.md docs/session-reports/2026-07-01-coding-review-loop-runnable-acceptance.md` showed only the intended tracked edits; the new session report is untracked, so it is covered by the manual read and no-index check below.
- `git status --short -uall` showed three modified files and one untracked session report:
  - `docs/casebook/inbox.md`
  - `skills/coding-review-loop/SKILL.md`
  - `skills/coding-review-loop/references/review-packet-shape.md`
  - `docs/session-reports/2026-07-01-coding-review-loop-runnable-acceptance.md`
- `git diff --name-only -- skills/coding-review-loop docs/casebook docs/session-reports docs/process-v0.3.md docs/process-v0.2.md docs/stage0-progress.md docs/policies docs/evaluations docs/v0.3-scope.md` showed only the three tracked modified files; the untracked report is visible in `git status --short -uall`.
- `git diff --check -- skills/coding-review-loop/SKILL.md skills/coding-review-loop/references/review-packet-shape.md docs/casebook/inbox.md` passed with no output.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-01-coding-review-loop-runnable-acceptance.md` produced no whitespace errors; exit code `1` is expected because `/dev/null` differs from the untracked file.
- `python3 - <<'PY' ...` validated `skills/coding-review-loop/SKILL.md` frontmatter contains `name:` and `description:`.
- Manual read covered the untracked session report content.
- Confirmed `docs/process-v0.3.md` is absent.
- Confirmed no Stage 0 tracker, policy, evaluation, ADR, or code file changed.
- Confirmed wording frames this as skill/reference refinement and privacy-safe friction, not active policy or formal evaluation.

## Good

- The refinement stays close to the observed friction and upgrades a packet field instead of creating broader process machinery.
- The new shape asks reviewers to verify user-facing defaults, not just core implementation logic.

## Friction

- What happened: A real-project review loop still missed promised runnable behavior after subagent review and review-finding fixes.
- Why it felt wrong: Dry-run, shadow, report, and default-entrypoint requirements were reviewable as intent but not forced into concrete commands, outputs, matrix dimensions, and existing entrypoint tests.
- Impact: Reviewers could approve core logic while the default user-facing path did not run the new behavior or expose the promised impact report.
- Category: `review` / `runnable acceptance gap`; secondary: `testing` / `entrypoint regression missed`
- Root cause guess: The review packet emphasized constraints and behavior tests but did not require runnable acceptance traceability for promised scripts, reports, CLIs, exports, or default configs.

## Proposed Follow-up

- Policy note candidate: no; keep observing before proposing a policy.
- Casebook candidate: not yet; recorded in inbox as privacy-safe friction, with possible future casebook only if repeated.
- ADR needed? no; this is a narrow packet-shape refinement without a durable trade-off needing explanation.
- Evaluation candidate? no formal evaluation; a future fixture could test whether packets require runnable acceptance for promised dry-run/shadow/report/default entrypoint behavior.
