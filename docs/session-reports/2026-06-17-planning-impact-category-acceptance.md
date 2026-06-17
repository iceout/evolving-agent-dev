# Session Report: Planning Impact Category Acceptance

## Goal

Update the Stage 0 tracker so `process` / `planning impact analysis` is accepted as the third repeated Stage 0 problem category based on Case 0005, without counting external observations as accepted internal dogfood tasks or declaring Stage 0 complete.

## Status

- Dogfood: yes.
- Stage 0 evidence status: bookkeeping/category acceptance only; not a new accepted internal Stage 0 dogfood task.
- Accepted category decision: `process` / `planning impact analysis` is accepted as the 3rd repeated Stage 0 problem category based on `docs/casebook/0005-planning-impact-analysis-gaps.md`.
- Accepted internal dogfood task count remains 10.
- Accepted dogfood friction item count remains 12.
- Accepted real-evidence evaluation candidates remain E005-E007.
- No E008, policy, ADR, automation, or tooling was created.
- Stage 0 is not declared complete; a separate Stage 0 exit review is required.

## Changes

- Updated `docs/stage0-progress.md` to count `process` / `planning impact analysis` as a repeated problem category.
- Kept external planning observations separate from accepted internal dogfood tasks and accepted dogfood friction items.
- Updated the real-task criterion status so it says numeric criteria appear met but a separate Stage 0 exit review is required.

## Verification

Ran:

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

tracker = Path('docs/stage0-progress.md').read_text()
cases = Path('docs/evaluations/behavior-cases.md').read_text()
report = Path('docs/session-reports/2026-06-17-planning-impact-category-acceptance.md').read_text()

assert '10 accepted / target 3-5' in tracker
assert '12 accepted friction items / target 10' in tracker
assert '3 accepted from real evidence / target 2' in tracker
assert 'Current tracker totals: 12 accepted dogfood friction items; 6 evidence-backed themes/categories; 3 repeated problem categories.' in tracker
assert 'Planning impact analysis is counted as a repeated problem category' in tracker
assert '3 repeated categories visible / target 3' in tracker
assert 'numeric criteria appear met, but separate Stage 0 exit review is required' in tracker
assert 'Stage 0 is not declared complete in this tracker update' in tracker
assert 'Stage 0 cannot exit yet' not in tracker
assert 'continue only for missing exit criteria' not in tracker

accepted_section = tracker.split('## Accepted Real Dogfood Tasks', 1)[1].split('## Calibration / Not Counted', 1)[0]
assert len(re.findall(r'^\\| \\d+ \\| `[^`]+` \\|', accepted_section, flags=re.M)) == 10
friction_section = tracker.split('### Friction Items Captured', 1)[1].split('### Themes / Categories', 1)[0]
assert len(re.findall(r'^\\| \\d+ \\| ', friction_section, flags=re.M)) == 12
repeated_section = tracker.split('### Repeated Problem Categories', 1)[1].split('## Stage 0 Exit Review Status', 1)[0]
assert repeated_section.count('Repeated problem category visible.') == 3

for label in ('E001', 'E002', 'E003', 'E004'):
    chunk = cases.split(f'## Case {label}:', 1)[1].split('## Case E', 1)[0]
    assert 'Evidence type: `seed`' in chunk, label
    assert 'Counts toward Stage 0 exit criteria: no' in chunk, label
for label in ('E005', 'E006', 'E007'):
    chunk = cases.split(f'## Case {label}:', 1)[1]
    next_case = re.search(r'\\n## Case E\\d+:', chunk)
    if next_case:
        chunk = chunk[:next_case.start()]
    assert 'Evidence type: `real`' in chunk, label
    assert 'Counts toward Stage 0 exit criteria: yes' in chunk, label
assert '## Case E008:' not in cases

for required in (
    'not a new accepted internal Stage 0 dogfood task',
    'Accepted internal dogfood task count remains 10',
    'Accepted dogfood friction item count remains 12',
    'Accepted real-evidence evaluation candidates remain E005-E007',
    'No E008, policy, ADR, automation, or tooling was created',
    'Stage 0 is not declared complete',
    'separate Stage 0 exit review is required',
):
    assert required in report, required

for path in ('docs/evaluations/behavior-cases.md', 'docs/process-v0.2.md'):
    subprocess.check_call(['git', 'diff', '--quiet', '--', path])
subprocess.check_call(['git', 'diff', '--quiet', '--', 'docs/casebook'])

for path in ('docs/stage0-progress.md', 'docs/session-reports/2026-06-17-planning-impact-category-acceptance.md'):
    for line_no, line in enumerate(Path(path).read_text().splitlines(), 1):
        assert line.rstrip() == line, f'{path}:{line_no}: trailing whitespace'

print('planning impact category acceptance update ok')
PY

git diff --check
```

Result: both commands passed.

## Good

The tracker now separates numeric exit-criteria readiness from the separate Stage 0 exit review decision.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no; E005-E007 remain the accepted real-evidence candidates, and E008 was not created.
