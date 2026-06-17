# Session Report: Stage 0 Exit With Caveats

## Goal

Record the completed Stage 0 exit review decision as `EXIT_WITH_CAVEATS` in the tracker and minimally refresh README stage status without creating v0.3 docs or changing evidence counts.

## Status

- Dogfood: yes.
- Stage 0 evidence status: exit-decision bookkeeping only; not a new accepted internal Stage 0 dogfood task.
- Decision: `EXIT_WITH_CAVEATS`.
- Evidence basis: current tracker totals show 10 accepted internal dogfood tasks, 12 accepted dogfood friction items, 3 accepted real-evidence evaluation candidates, and 3 repeated problem categories.
- Caveats: sandboxed execution remains unverified; cross-artifact consistency and planning impact repeated-category support includes privacy-preserving external evidence; E005-E007 are accepted real-evidence evaluation candidates, not formal promoted evaluations; E001-E004 remain seed; Case 0005 does not create E008 yet.
- v0.3 carryover: keep sandbox/tooling caveat explicit; try one sandboxed smoke/dogfood check if supported; sharpen E005-E007 into manual judge checklists or fixtures before automation; use the three repeated categories as the first v0.3 improvement backlog; preserve Stage 0 evidence boundaries.
- Non-goals: no `docs/process-v0.3.md`, no rewrite to `docs/process-v0.2.md`, no E008, no promotion of E005-E007 to formal evaluations, no policy, ADR, automation, or tooling.

## Changes

- Updated `docs/stage0-progress.md` with the `EXIT_WITH_CAVEATS` decision, required caveats, and v0.3 carryover.
- Updated `README.md` minimally so Current Stage no longer says Stage 0 is still collecting exit evidence.
- Fixed stale stage-transition wording in README and the Stage 0 tracker.
- Did not change accepted task count, friction item count, repeated-category count, or evaluation-candidate count.

## Verification

Ran:

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

readme = Path('README.md').read_text()
tracker = Path('docs/stage0-progress.md').read_text()
cases = Path('docs/evaluations/behavior-cases.md').read_text()
report = Path('docs/session-reports/2026-06-17-stage0-exit-with-caveats.md').read_text()

assert 'Stage 0: exited with caveats on 2026-06-17.' in readme
assert 'EXIT_WITH_CAVEATS' in readme
assert 'completed Stage 0 process record and current reference until v0.3 scope starts' in readme
assert 'active draft of the development workflow' not in readme
assert '## Stage 0 Exit Decision' in tracker
assert 'Stage 0 exits with caveats: `EXIT_WITH_CAVEATS`' in tracker
assert 'This is not a clean exit' in tracker
assert '10 accepted internal dogfood tasks / target 3-5' in tracker
assert '12 accepted dogfood friction items / target 10' in tracker
assert '3 accepted real-evidence evaluation candidates / target 2' in tracker
assert '3 repeated problem categories / target 3' in tracker
assert 'This exit-decision bookkeeping does not count as a new accepted internal Stage 0 dogfood task' in tracker
assert 'Sandboxed execution remains unverified' in tracker
assert 'privacy-preserving external evidence' in tracker
assert 'E005-E007 are accepted real-evidence evaluation candidates, not formal promoted evaluations' in tracker
assert 'E001-E004 remain seed' in tracker
assert 'Case 0005 does not create E008 yet' in tracker
assert 'Preserve Stage 0 evidence boundaries in v0.3' in tracker
assert 'separate Stage 0 exit review is required' not in tracker
assert 'Stage 0 is not declared complete in this tracker update' not in tracker
stale_readme_phrase = 'active ' + 'Stage 0 process draft'
stale_tracker_phrase = 'When a dogfood task is accepted' + ', add its commit'
stale_friction_phrase = 'No notable ' + 'friction'
for text in (readme, tracker, report):
    assert stale_readme_phrase not in text
    assert stale_tracker_phrase not in text
    assert stale_friction_phrase not in text
assert 'Stage 0 counts are frozen after the `EXIT_WITH_CAVEATS` decision' in tracker
assert 'Future dogfood or evidence should belong to v0.3 artifacts once v0.3 starts' in tracker
assert 'Only correction or bookkeeping updates should modify this Stage 0 tracker' in tracker

accepted_section = tracker.split('## Accepted Real Dogfood Tasks', 1)[1].split('## Calibration / Not Counted', 1)[0]
assert len(re.findall(r'^\| \d+ \| `[^`]+` \|', accepted_section, flags=re.M)) == 10
friction_section = tracker.split('### Friction Items Captured', 1)[1].split('### Themes / Categories', 1)[0]
assert len(re.findall(r'^\| \d+ \| ', friction_section, flags=re.M)) == 12
repeated_section = tracker.split('### Repeated Problem Categories', 1)[1].split('## Stage 0 Exit Decision', 1)[0]
assert repeated_section.count('Repeated problem category visible.') == 3

for label in ('E001', 'E002', 'E003', 'E004'):
    chunk = cases.split(f'## Case {label}:', 1)[1].split('## Case E', 1)[0]
    assert 'Evidence type: `seed`' in chunk, label
    assert 'Counts toward Stage 0 exit criteria: no' in chunk, label
for label in ('E005', 'E006', 'E007'):
    chunk = cases.split(f'## Case {label}:', 1)[1]
    next_case = re.search(r'\n## Case E\d+:', chunk)
    if next_case:
        chunk = chunk[:next_case.start()]
    assert 'Evidence type: `real`' in chunk, label
    assert 'Counts toward Stage 0 exit criteria: yes' in chunk, label
assert '## Case E008:' not in cases

for required in (
    'Dogfood: yes',
    'Stage 0 evidence status: exit-decision bookkeeping only; not a new accepted internal Stage 0 dogfood task',
    'Decision: `EXIT_WITH_CAVEATS`',
    'Evidence basis: current tracker totals show 10 accepted internal dogfood tasks, 12 accepted dogfood friction items, 3 accepted real-evidence evaluation candidates, and 3 repeated problem categories',
    'sandboxed execution remains unverified',
    'privacy-preserving external evidence',
    'E005-E007 are accepted real-evidence evaluation candidates, not formal promoted evaluations',
    'E001-E004 remain seed',
    'Case 0005 does not create E008 yet',
    'v0.3 carryover',
    'Non-goals: no `docs/process-v0.3.md`',
):
    assert required in report, required

assert not Path('docs/process-v0.3.md').exists()
for path in ('docs/process-v0.2.md', 'docs/evaluations/behavior-cases.md'):
    subprocess.check_call(['git', 'diff', '--quiet', '--', path])
for dirname in ('docs/policies', 'docs/decisions', 'skills'):
    subprocess.check_call(['git', 'diff', '--quiet', '--', dirname])

changed = set(subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines())
assert changed == {'README.md', 'docs/stage0-progress.md'}, changed
status = subprocess.check_output(['git', 'status', '--short'], text=True).splitlines()
assert status == [
    ' M README.md',
    ' M docs/stage0-progress.md',
    '?? docs/session-reports/2026-06-17-stage0-exit-with-caveats.md',
], status

for path in ('README.md', 'docs/stage0-progress.md', 'docs/session-reports/2026-06-17-stage0-exit-with-caveats.md'):
    for line_no, line in enumerate(Path(path).read_text().splitlines(), 1):
        assert line.rstrip() == line, f'{path}:{line_no}: trailing whitespace'

print('stage0 exit with caveats ok')
PY

git diff --check
```

Result: both commands passed.

## Good

The exit decision is explicit while preserving Stage 0 evidence boundaries and avoiding premature v0.3 design or automation.

## Friction

### Stale stage-transition wording remained after exit

- What happened: The first exit-decision recording left README wording that still described v0.2 as the still-active Stage 0 draft and left a tracker update rule for adding future accepted Stage 0 dogfood tasks.
- Why it felt wrong: After `EXIT_WITH_CAVEATS`, Stage 0 counts should be frozen and future dogfood/evidence should move to v0.3 artifacts once v0.3 starts.
- Impact: Future work could accidentally keep appending accepted tasks to Stage 0 instead of preserving the exit boundary.
- Category: `process`
- Root cause guess: The exit decision updated the main status but missed neighboring stage-transition language.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no; E005-E007 remain accepted real-evidence evaluation candidates, and E008 was not created.
