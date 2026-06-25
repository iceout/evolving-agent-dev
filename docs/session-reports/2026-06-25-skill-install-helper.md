# Session Report: skill install helper

## Goal

Add a minimal helper for listing repo-tracked skills, checking local runtime install status, and installing one selected skill without turning this into a broader tooling framework.

## Changes

- Added `scripts/install-skill.py` as a no-dependency helper for `--list`, `--install <skill>`, `--copy`, `--dry-run`, and optional `--runtime-root`.
- Updated `README.md` to mention `idea-framing-loop` and document the helper while keeping manual install instructions.
- Dogfood / evidence: post-Stage 0 v0.3 install-flow convenience; not a Stage 0 task.
- Stage 0 counts unchanged.

## Non-goals

- Did not install or sync any runtime skill.
- Did not create `docs/process-v0.3.md` or finalize a v0.3 process.
- Did not create E008, policy, ADR, automation framework, metrics, subagent framework, marketplace, registry, background sync, or watcher.

## Verification

- `python3 -m py_compile scripts/install-skill.py` passed.
- Temporary runtime test passed for `--list`, `--install idea-framing-loop --dry-run`, symlink install, post-install status, and `--install coding-review-loop --copy`.
- `git status --short -uall` showed only `README.md`, `scripts/install-skill.py`, and this session report changed.
- `test ! -e docs/process-v0.3.md` passed.
- `rg -n '^## Case E008' . || true` produced no matches.
- `git diff --check` passed.
- Temporary-index `git diff --cached --check` covering README, the new script, and this session report passed.
- Protected artifact check produced no output for process docs, Stage 0 tracker, evaluations, policies, decisions, casebook, or skill directories not in scope.
- Temporary runtime directories created for verification were removed after testing.

## Good

The helper keeps the installation path explicit and safe: it lists current status, installs one selected skill, defaults to symlink, supports copy when needed, and refuses to overwrite an existing destination.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: none.
- Casebook candidate: none.
- ADR needed? no; this is a small repository helper without a durable architectural trade-off.
- Evaluation candidate? no; no judgeable agent regression fixture was created.
