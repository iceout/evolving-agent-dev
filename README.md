# Evolving Agent Development

This project develops an evolving collection of agent skills, supported by a working system for discovering, recording, and refining agent behavior.

## Purpose

Improve reusable skills through real usage, traceable change decisions, and later behavioral verification. Users select evidence and authorize changes; the repository does not implement an agent runtime or autonomous self-modification.

The core loop is:

```text
real usage -> friction captured -> root cause analyzed -> policy updated -> evaluation added -> next usage verifies improvement
```

## Current Process

`docs/process-v0.2.md` provides the baseline artifact-routing and lifecycle rules. Post-Stage 0 skill refinements and external evidence are maintained in [the v0.3 scope note](docs/v0.3-scope.md), which remains a scope draft rather than a finalized process-v0.3 specification.

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
- `docs/process-v0.2.md` - completed Stage 0 process record and baseline routing rules.
- `docs/v0.3-scope.md` - current refinement and external-evidence state.
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

| Skill | Use and handoff |
|---|---|
| `idea-framing-loop` | Clarify an idea before planning; hand off non-trivial coding work to `coding-review-loop`. |
| `bug-investigation-loop` | Establish a bug's root cause; hand off complex or high-risk fixes to `coding-review-loop`. |
| `coding-review-loop` | Plan, review, implement, and verify non-trivial real-code work; capture notable local evidence when triggered. |
| `evolving-agent-process` | Maintain this repository's process and distill user-selected evidence into existing artifacts. |

List local install status and install a tracked skill with the helper:

```sh
python3 scripts/install-skill.py --list
python3 scripts/install-skill.py --inspect coding-review-loop
python3 scripts/install-skill.py --install idea-framing-loop
python3 scripts/install-skill.py --install coding-review-loop --copy
python3 scripts/install-skill.py --install bug-investigation-loop
```

The helper installs the whole skill directory, not only `SKILL.md`. It uses a symlink by default, supports `--copy`, and refuses to overwrite an existing runtime skill directory.

`--list` compares installed packages with repository content. `--inspect <skill>` also prints full `sha256-v1` package fingerprints for the repository and runtime directory. The fingerprint covers sorted relative paths, directories, file bytes, and executable bits, including references; timestamps and absolute paths are excluded. Internal symlinks and special files are reported as unsupported rather than followed. Missing, unreadable, unsupported, and divergent packages are distinguished without modifying them.

These are on-disk observations, not proof of what a session loaded. For an explicitly designated real-task observation, establish the skill source/version used at task start; do not infer historical loading from a later fingerprint or current symlink. Inspection is opt-in and writes no usage log.

Inspect while the package is not being edited; hashing is not an atomic snapshot. `--inspect` exits 0 when both fingerprints are available (even if they differ), and 1 when either is unavailable. Use the printed status to distinguish equality from drift.

You can also install manually by linking or copying the whole skill directory:

```sh
skill_name=evolving-agent-process  # or coding-review-loop / idea-framing-loop / bug-investigation-loop
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

Stage 0 exited with caveats; its frozen counts and limitations are recorded in [Stage 0 progress](docs/stage0-progress.md). Current work includes skill refinements, external evidence distillation, and the bounded orchestration authorized by [ADR-0002](docs/decisions/ADR-0002-external-evidence-distillation-orchestration.md).

Use [the v0.3 scope note](docs/v0.3-scope.md) for current outcomes and next decisions. An implemented rule does not establish effectiveness. Broader automation, evaluation promotion, or a finalized process-v0.3 document requires an explicit scope decision.
