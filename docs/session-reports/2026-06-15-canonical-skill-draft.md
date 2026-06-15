# Session Report: Canonical Skill Draft

## Goal

Create the repo-tracked canonical draft for the first `evolving-agent-process` Codex skill without installing it yet.

## Evidence Status

- Dogfood: no.
- Counts as Stage 0 real task: no.
- Reason: this is still Hermes/bootstrap implementation of the canonical draft before Codex has installed and used the skill.

## Changes

- Created `skills/evolving-agent-process/SKILL.md` as the canonical repo-tracked draft.
- Updated `docs/skill-design/evolving-agent-process-v0.1.md` to name that canonical path explicitly.
- Kept v0.1 thin: no scripts, no automation, no agents config, no local Codex install yet.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re, yaml
content = Path('skills/evolving-agent-process/SKILL.md').read_text()
assert content.startswith('---')
match = re.search(r'\n---\s*\n', content[3:])
assert match
frontmatter = yaml.safe_load(content[3:match.start()+3])
assert frontmatter['name'] == 'evolving-agent-process'
assert 'description' in frontmatter
assert len(frontmatter['description']) <= 1024
for needle in [
    '## When to Use',
    '## Source of Truth and Read Order',
    '## Task Classification',
    '## Artifact Routing',
    '## Evidence Rules',
    '## Verification Rules',
    '## Installation Boundary',
    '## Final Checklist',
]:
    assert needle in content, needle
print('skill draft ok')
PY
```

Result: passed; skill frontmatter parsed, description length was within limit, required sections existed, and the design document references the canonical path.

## Good

The canonical draft gives future Codex installation a reviewable source path instead of making the local runtime copy the only version.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no.
