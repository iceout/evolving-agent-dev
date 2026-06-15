# Session Report: Skill Install Flow Clarification

## Goal

Clarify the `evolving-agent-process` skill install flow based on the friction recorded in `docs/casebook/inbox.md`, while keeping the change minimal.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task used the installed skill for a process-doc edit after smoke testing.
- Count status: count only from the commit that contains both the skill change and this report.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.

## Changes

- Updated process guidance only in `skills/evolving-agent-process/SKILL.md`.
- Added this minimal session report.
- Clarified expected destination discovery, whole-directory install, symlink-vs-copy choice, copy refresh recording, and install verification.
- Left `docs/skill-design/evolving-agent-process-v0.1.md` unchanged because its installation boundary remains compatible and the requested clarification belongs in the runtime skill adapter.

## Verification

- Read `README.md`, `docs/process-v0.2.md`, `docs/casebook/inbox.md`, `docs/session-reports/TEMPLATE.md`, and `docs/session-reports/GUIDE.md` before editing.
- Checked the design/install history around `docs/skill-design/evolving-agent-process-v0.1.md`, `docs/session-reports/2026-06-15-codex-skill-install.md`, and `docs/session-reports/2026-06-15-codex-skill-smoke-tests.md` to avoid contradicting existing guidance.

```bash
python3 - <<'PY'
from pathlib import Path
skill = Path("skills/evolving-agent-process/SKILL.md")
text = skill.read_text()
assert text.startswith("---\n")
end = text.find("\n---\n", 4)
assert end != -1
frontmatter = text[4:end]
for required in ("name: evolving-agent-process", "version: 0.1.0"):
    assert required in frontmatter
for required in (
    "use `$CODEX_HOME/skills/evolving-agent-process/` when `CODEX_HOME` is set",
    "Install the whole tracked `skills/evolving-agent-process/` directory, not only `SKILL.md`.",
    "Prefer a directory symlink",
    "If symlinks are unavailable, copy the whole directory",
    "Verify the install by checking the runtime `SKILL.md` exists",
):
    assert required in text
report = Path("docs/session-reports/2026-06-15-skill-install-flow-clarification.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
):
    assert required in report
print("install flow clarification ok")
PY
```

Result: passed; printed `install flow clarification ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The inbox friction was handled as a small clarification in the installed skill adapter instead of expanding v0.2 or creating a new policy.

## Friction

### Sandbox remains unverified

- What happened: This environment still relies on `--dangerously-bypass-approvals-and-sandbox` for Codex execution.
- Why it felt wrong: The dogfood task validates skill behavior, but not behavior under normal sandboxed execution.
- Impact: Stage 0 evidence should carry this caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same environment limitation recorded during smoke testing; sandbox setup still cannot be verified here.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: not yet; keep tracking with the existing sandbox friction if it recurs.
- ADR needed? no; no durable trade-off changed.
- Evaluation candidate? no; this is environment/tooling evidence, not a behavior regression.
