# Session Report: Cross-Artifact Consistency Guard

## Goal

Add a minimal process/skill guard so tasks that change status, counts, paths, config behavior, or verification semantics search linked artifacts for stale references before finalizing.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood task candidate after review/commit; not counted until accepted.
- Evaluation status: no new evaluation candidate; E001-E004 remain seed, E005-E007 remain accepted as-is.
- Stage 0 status: not complete; this task does not change tracker counts.
- Sandbox caveat: unchanged; sandboxed execution remains unverified in the tracker.

## Changes

- Updated `skills/evolving-agent-process/SKILL.md` with a short Cross-Artifact Consistency Guard.
- The guard requires linked/sibling artifact searches when status, counts, paths, config behavior, or verification semantics change.
- The guard includes examples for tracker/evaluation/casebook/session report, config docs/templates/README, and verification command/report summary.
- The guard requires at least one stale-language negative check when status/count/path/config/verification meaning changes.
- Checked `docs/skill-design/evolving-agent-process-v0.1.md`; its existing artifact-consistency responsibility remains compatible, so no design doc edit was needed.
- Checked the runtime-installed skill; it resolves to the repo-tracked `SKILL.md`, so the runtime skill already has the guard.
- Did not edit `docs/process-v0.2.md`, `docs/stage0-progress.md`, policies, ADRs, automation, or tooling.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

skill = Path("skills/evolving-agent-process/SKILL.md").read_text()
design = Path("docs/skill-design/evolving-agent-process-v0.1.md").read_text()
runtime_skill = Path.home() / ".codex" / "skills" / "evolving-agent-process" / "SKILL.md"
assert skill.startswith("---\n")
frontmatter_end = skill.index("\n---\n", 4)
frontmatter = skill[:frontmatter_end]
assert "name: evolving-agent-process" in frontmatter
assert "description:" in frontmatter

section = skill.split("## Cross-Artifact Consistency Guard", 1)[1].split("## Role Separation and Objections", 1)[0]
for required in (
    "status, counts, paths, config behavior, or verification semantics",
    "tracker + evaluation + casebook + session report",
    "config docs + templates + README",
    "verification command + report summary",
    "stale-language negative check",
    "status, count, path, config, or verification meaning changes",
):
    assert required in section, required

# Stale-language negative check for this guard: do not leave a weaker phrasing that
# only covers E007 acceptance instead of general status/count/path/config changes.
for stale in (
    "E007 pending",
    "pending review/acceptance",
    "casebook-only guard",
):
    assert stale not in section, stale

assert "check artifact consistency before the final response" in design
assert "skills/evolving-agent-process/SKILL.md" in design

assert runtime_skill.exists(), runtime_skill
assert runtime_skill.resolve() == Path("skills/evolving-agent-process/SKILL.md").resolve()
runtime_text = runtime_skill.read_text()
assert "## Cross-Artifact Consistency Guard" in runtime_text
assert "stale-language negative check" in runtime_text

for path in (
    "docs/process-v0.2.md",
    "docs/stage0-progress.md",
    "docs/evaluations/behavior-cases.md",
    "docs/skill-design/evolving-agent-process-v0.1.md",
):
    subprocess.check_call(["git", "diff", "--quiet", "--", path])

assert not Path("docs/policies/cross-artifact-consistency.md").exists()
assert not Path("docs/decisions/ADR-0002-cross-artifact-consistency.md").exists()

for path in (
    Path("skills/evolving-agent-process/SKILL.md"),
    Path("docs/session-reports/2026-06-16-cross-artifact-consistency-guard.md"),
):
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        assert line.rstrip() == line, (path, lineno)

print("cross artifact consistency guard ok")
PY
```

Result: passed; printed `cross artifact consistency guard ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

The Python verification also checks trailing whitespace in the new session report.

## Good

The rule stays close to the skill checklist and avoids creating a heavier policy, ADR, or automation layer.

## Friction

No notable new friction. This task directly addresses the previously accepted cross-artifact consistency drift evidence.

## Proposed Follow-up

- Policy note candidate: no; the lightweight skill guard is enough for now.
- Casebook candidate: no; `docs/casebook/0004-cross-artifact-consistency-drift.md` already exists.
- ADR needed? no.
- Evaluation candidate? no; E007 already covers cross-artifact consistency behavior.
