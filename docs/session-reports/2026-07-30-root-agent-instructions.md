# Session Report: Root Agent Instructions

## Goal

Add a concise root `AGENTS.md` that helps future agents find the correct source
of truth, skill, evidence boundary, artifact route, and verification path
without duplicating the repository process or current lineage state.

## Changes

- Added `AGENTS.md` as a stable operating map for agents working in this
  repository.
- Routed agents to `README.md`, `docs/process-v0.2.md`, target files, and the
  session-report guidance rather than copying their detailed content.
- Recorded stable task classification, skill routing, external-evidence and
  version-attribution boundaries, artifact routing, editing rules, verification
  requirements, privacy constraints, and common scope traps.
- Excluded commit IDs, CRL status tables, Stage counts, temporary backlog,
  templates, and detailed process text that would make the file a second source
  of truth or cause frequent drift.

## Verification

- Confirmed the task started with a clean worktree and no existing root
  `AGENTS.md`.
- Read the repository purpose, current process, session-report guidance,
  `evolving-agent-process`, and the current coding-review-loop capture boundary
  before writing the instructions.
- Read the complete new files and final diff.
- Ran `git diff --check`.
- Ran independent `git diff --no-index --check` checks for both new files; each
  produced no whitespace warning and returned the expected file-difference
  status because the file differs from `/dev/null`.
- Verified the changed-file allowlist contains only `AGENTS.md` and this report.
- Verified every repository-relative Markdown path named in `AGENTS.md` exists.
- Checked that `AGENTS.md` contains no commit hashes, CRL status table, Stage
  count, temporary backlog, private external path, runtime-install action, or
  instruction to modify external evidence.

## Good

The root instructions provide a fast, tool-discoverable entry point while
leaving detailed and changing behavior in the existing repository sources of
truth.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no; this is a repository operating map.
- Casebook candidate: no.
- ADR needed? no; the file points to existing decisions and process sources.
- Evaluation candidate: no; observe whether future agents need less startup
  searching and make fewer routing or attribution mistakes.
