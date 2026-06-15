# Session Report: Codex Skill Install

## Goal

Install the repo-tracked `evolving-agent-process` skill into the local Codex skill directory for upcoming smoke tests.

## Evidence Status

- Dogfood: no.
- Counts as Stage 0 real task: no.
- Reason: this is installation/bootstrap work. Dogfood data starts only after Codex uses the installed skill on smoke tests or real edit tasks.

## Changes

- Confirmed `CODEX_HOME` is not set.
- Confirmed local Codex directory exists at `$HOME/.codex/`.
- Confirmed Codex skill directory exists at `$HOME/.codex/skills/`.
- Installed by symlinking the whole skill directory:
  - Source: `<repo>/skills/evolving-agent-process/`
  - Destination: `$HOME/.codex/skills/evolving-agent-process`
  - Strategy: directory symlink
  - Source commit: `bd4d781`

## Verification

```bash
printf 'CODEX_HOME=%s\n' "${CODEX_HOME-}"
for d in "$HOME/.codex" "$HOME/.codex/skills"; do
  if [ -e "$d" ]; then
    printf 'exists %s\n' "$d"
  fi
done
```

Result: `CODEX_HOME` was empty; `$HOME/.codex` and `$HOME/.codex/skills` existed.

```bash
ln -s <repo>/skills/evolving-agent-process $HOME/.codex/skills/evolving-agent-process
ls -ld $HOME/.codex/skills/evolving-agent-process
readlink $HOME/.codex/skills/evolving-agent-process
test -f $HOME/.codex/skills/evolving-agent-process/SKILL.md
python3 - <<'PY'
from pathlib import Path
installed = Path('$HOME/.codex/skills/evolving-agent-process/SKILL.md')
source = Path('<repo>/skills/evolving-agent-process/SKILL.md')
assert installed.exists()
assert installed.resolve() == source.resolve()
assert 'name: evolving-agent-process' in installed.read_text()
print('symlink install ok')
PY
```

Result: symlink install verified; installed `SKILL.md` resolves to the repo-tracked canonical draft.

## Good

Directory symlink keeps the runnable Codex skill tied to the version-tracked repo source and avoids drift from copying.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no.
- Next: run the four v0.1 smoke tests before counting dogfood data.
