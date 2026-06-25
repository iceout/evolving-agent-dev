# Evolving Agent Development

This project is not the agent implementation yet. It is the working system for discovering, recording, and refining how the agent should behave.

## Purpose

Build an evolvable development system before building the agent itself.

The core loop is:

```text
real usage -> friction captured -> root cause analyzed -> policy updated -> evaluation added -> next usage verifies improvement
```

## Current Process

`docs/process-v0.2.md` is the completed Stage 0 process record and current reference until v0.3 scope starts. Existing artifacts should follow its routing and lifecycle rules unless later superseded.

Stage 0 was intentionally lightweight:

- Micro tasks do not need a session report, but useful friction must be captured in `docs/casebook/inbox.md`.
- Tasks with substantive code or document changes need a minimal session report.
- Reusable friction can become casebook entries.
- Repeated or high-impact rule hypotheses start as `proposed` policy notes.
- Stable defaults become `active` policies only after enough evidence.
- ADRs are for decisions with trade-offs, future constraints, or likely "why" questions.
- Evaluations are for high-signal behavior regressions; weak cases stay as evaluation candidates.

## Working Artifacts

- `docs/principles.md` - stable beliefs that guide the system.
- `docs/process-v0.2.md` - completed Stage 0 process record and current reference until v0.3 scope starts.
- `docs/process-v0.1.md` - earlier process draft kept for history.
- `docs/session-reports/` - raw records for tasks with substantive changes.
- `docs/casebook/inbox.md` - append-only inbox for lightweight friction from micro tasks or scattered observations.
- `docs/casebook/` - reusable historical friction cases with context and traceability.
- `docs/policies/` - policy notes and active policies, each with explicit status and source links.
- `docs/decisions/` - Agent Decision Records explaining trade-offs and durable process decisions.
- `docs/evaluations/` - behavior-level regression cases or candidates for future agents.
- `skills/` - repo-tracked Codex skill drafts and related references.

## Installing Skills Locally

The `skills/` directory is the reviewable source for local Codex skills. The runtime install under Codex's skill directory is local state.

Install a skill by linking or copying the whole skill directory, not only `SKILL.md`.

```sh
skill_name=evolving-agent-process
skill_source="$(pwd)/skills/$skill_name"
skill_dest="${CODEX_HOME:-$HOME/.codex}/skills/$skill_name"

mkdir -p "$(dirname "$skill_dest")"
ln -s "$skill_source" "$skill_dest"
```

If symlinks are not available or Codex does not load symlinked skills, copy the whole directory instead and refresh the copy after changing the repo-tracked source:

```sh
cp -R "$skill_source" "$skill_dest"
```

Verify the install before relying on it:

```sh
test -f "$skill_dest/SKILL.md"
grep -q "name: $skill_name" "$skill_dest/SKILL.md"
```

When `CODEX_HOME` is set, use `$CODEX_HOME/skills/<skill-name>/`. Otherwise the usual local path is `$HOME/.codex/skills/<skill-name>/`. If a destination already exists, inspect it before replacing it.

## Current Stage

Stage 0: exited with caveats on 2026-06-17.

The Stage 0 exit decision is `EXIT_WITH_CAVEATS`, not a clean exit. Numeric exit criteria are met, but v0.3 should carry forward the sandbox/tooling caveat, privacy-preserving external evidence caveats, and the accepted evaluation-candidate boundaries recorded in `docs/stage0-progress.md`.

Do not create v0.3 process docs, promote evaluation candidates, or add automation until the v0.3 scope is explicitly started.
