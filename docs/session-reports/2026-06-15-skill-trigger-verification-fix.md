# Session Report: Skill Trigger and Verification Fix

## Goal

Fix pre-installation issues that would affect the first Codex dogfood run: missing skill-design triggers, non-reproducible verification, and single-file install guidance.

## Evidence Status

- Dogfood: no.
- Counts as Stage 0 real task: no.
- Reason: this is still Hermes/bootstrap hardening before the skill is installed into Codex.

## Changes

- Added `docs/skill-design/*` and `skills/evolving-agent-process/*` to the skill's explicit trigger file list.
- Updated install guidance to prefer symlinking the whole `skills/evolving-agent-process/` directory, not only `SKILL.md`.
- Updated the design document with the same directory-level install guidance.
- Rewrote the canonical skill draft session report verification command to use only Python stdlib.
- Made the session report verification claim match the command by checking both the skill draft and design document.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

content = Path('skills/evolving-agent-process/SKILL.md').read_text()
assert content.startswith('---')
match = re.search(r'\n---\s*\n', content[3:])
assert match
frontmatter_text = content[3:match.start()+3]
frontmatter = {}
for line in frontmatter_text.splitlines():
    if not line or line.startswith('  ') or line.strip().startswith('-'):
        continue
    if ':' in line:
        key, value = line.split(':', 1)
        frontmatter[key.strip()] = value.strip().strip('"')
assert frontmatter['name'] == 'evolving-agent-process'
assert frontmatter.get('description')
assert len(frontmatter['description']) <= 1024
for needle in [
    '`docs/skill-design/*`',
    '`skills/evolving-agent-process/*`',
    'symlinking the tracked `skills/evolving-agent-process/` directory',
]:
    assert needle in content, needle

design = Path('docs/skill-design/evolving-agent-process-v0.1.md').read_text()
assert 'skills/evolving-agent-process/SKILL.md' in design
assert 'skills/evolving-agent-process/` directory' in design
report = Path('docs/session-reports/2026-06-15-canonical-skill-draft.md').read_text()
assert 'import re' in report
assert 'import re, yaml' not in report
assert "match = re.search(r'\\n---\\s*\\n', content[3:])" in report

# Extract and execute the canonical report's verification command to ensure it is copy-paste runnable.
start = report.index("python3 - <<'PY'") + len("python3 - <<'PY'")
end = report.index('PY', start)
code = report[start:end].strip()
exec(compile(code, 'canonical-skill-draft verification', 'exec'), {})
print('trigger and verification fix ok')
PY
```

Result: passed; stdlib-only verification confirmed trigger paths, directory install guidance, design references, correct regex text, and executed the canonical report command extracted from the report.

## Good

The fix keeps the first dogfood install from starting with known traceability and trigger gaps.

## Friction

### Verification used an undeclared dependency

- What happened: The previous report used `import yaml` even though the project has no dependency management and PyYAML is not guaranteed.
- Why it felt wrong: A traceability-focused project should prefer reproducible stdlib verification unless it declares dependencies.
- Impact: Future readers could fail to rerun the report's verification command.
- Category: `process`
- Root cause guess: I reused a convenient YAML parser instead of matching the repository's no-dependency state.

## Proposed Follow-up

- Policy note candidate: verification snippets in session reports should avoid undeclared dependencies.
- Casebook candidate: not yet; track if this repeats.
- ADR needed? no.
- Evaluation candidate? no.
