# Session Report: Skill Design v0.1 Hardening

## Goal

Address review feedback on the first Codex skill design draft before implementing the runnable skill.

## Evidence Status

- Dogfood: no.
- Counts as Stage 0 real task: no.
- Reason: this is Hermes/bootstrap design hardening before the runnable Codex skill is installed.

## Changes

- Quoted the proposed SKILL.md `description` so the frontmatter is valid YAML.
- Tightened the description to reduce generic over-triggering while still covering process evidence scenarios.
- Updated installation boundary so the repo keeps a version-tracked canonical skill draft, while the local Codex install is runtime state.
- Added symlink/copy tracking guidance for local installation.
- Added a v0.1 smoke test plan for review-only, discussion-only friction recording, edit-task session reporting, and seed evidence classification.
- Noted that acceptance criteria should include avoiding over-triggering outside this repo/process context.
- Updated the previous session report with dogfood/Stage 0 evidence status and a reproducible verification command.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
s = Path('docs/skill-design/evolving-agent-process-v0.1.md').read_text()
checks = [
    'description: "Use when working in evolving-agent-dev on process evidence:',
    'Keep a version-tracked canonical `SKILL.md` draft in the repo before installing it locally.',
    '## v0.1 Smoke Test Plan',
    'Smoke Test A: Review-only does not over-write',
    'Smoke Test B: Discussion-only can record explicit friction',
    'Smoke Test C: Edit task writes report and verifies',
    'Smoke Test D: Seed evidence is not counted',
    'over-triggering on generic README, review, or evaluation mentions outside this repo/process context',
]
missing = [c for c in checks if c not in s]
print('missing:', missing)
PY
```

Result: passed; all required strings were present.

## Good

The review caught a concrete YAML failure before implementation and identified the need to keep the runnable skill traceable through a repo-tracked draft.

## Friction

### Verification record was too vague

- What happened: The previous session report said a Python keyword check passed but did not include the exact command or checks.
- Why it felt wrong: The project emphasizes traceability, and vague verification makes the report hard to rerun.
- Impact: Future readers could not distinguish real verification from verification theater.
- Category: `process`
- Root cause guess: The report summarized command output instead of preserving the command.

## Proposed Follow-up

- Policy note candidate: session reports should include reproducible verification commands when practical; otherwise label verification as manual.
- Casebook candidate: not yet; track for repetition.
- ADR needed? no.
- Evaluation candidate? possible later if agents repeatedly write unverifiable verification summaries.
