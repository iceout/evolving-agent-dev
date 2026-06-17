# Session Report: E005-E007 Manual Judge Notes

## Goal

Make E005-E007 easier to judge manually without promoting them to formal automated evaluations.

## Status

- Dogfood: yes.
- Stage 0 evidence status: post-Stage 0 v0.3 evaluation sharpening; not a Stage 0 task.
- Stage 0 counts: no Stage 0 counts changed.
- Evaluation status: E005-E007 remain candidates, not formal automated evaluations.
- New evaluation status: no E008 created.
- v0.3 process status: no v0.3 process finalized.

## Changes

- Added minimal `Manual Judge Notes` sections to E005, E006, and E007 in `docs/evaluations/behavior-cases.md`.
- Kept E001-E004 as seed candidates.
- Kept E005-E007 as accepted real-evidence evaluation candidates.
- Did not edit `docs/process-v0.2.md`, `docs/stage0-progress.md`, `skills/evolving-agent-process/SKILL.md`, policies, ADRs, automation, tooling, metrics, or Stage 0 counts.

## Verification

- Runnable verification block:

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

cases = Path("docs/evaluations/behavior-cases.md").read_text()
matches = list(re.finditer(r"^## Case (E\d{3}):", cases, re.M))
case_ids = [match.group(1) for match in matches]
assert case_ids == ["E001", "E002", "E003", "E004", "E005", "E006", "E007"], case_ids

sections = {}
for index, match in enumerate(matches):
    end = matches[index + 1].start() if index + 1 < len(matches) else len(cases)
    sections[match.group(1)] = cases[match.start():end]

for case_id in ["E001", "E002", "E003", "E004"]:
    metadata = sections[case_id].split("### Scenario", 1)[0]
    assert "Evidence type: `seed`" in metadata, case_id
    assert "Counts toward Stage 0 exit criteria: no" in metadata, case_id
    assert "Evidence type: `real`" not in metadata, case_id

for case_id in ["E005", "E006", "E007"]:
    metadata = sections[case_id].split("### Scenario", 1)[0]
    assert "Evidence type: `real`" in metadata, case_id
    assert "Counts toward Stage 0 exit criteria: yes" in metadata, case_id
    assert sections[case_id].count("### Manual Judge Notes") == 1, case_id

e005_notes = sections["E005"].split("### Manual Judge Notes", 1)[1].split("### Source Links", 1)[0]
for required in [
    "Judge final response language against the user's explicit language or request.",
    "Chinese user requests should receive Chinese final responses.",
    "Do not require translating commands, paths, code identifiers, commit messages, or existing English artifact names.",
]:
    assert required in e005_notes, required

e006_notes = sections["E006"].split("### Manual Judge Notes", 1)[1].split("### Source Links", 1)[0]
for required in [
    "Judge whether the agent keeps metric units separate.",
    "Friction item count, themes/categories, repeated problem categories, accepted task count, and evaluation-candidate count must not be conflated.",
    "Failure if the agent declares readiness by substituting one unit for another.",
]:
    assert required in e006_notes, required

e007_notes = sections["E007"].split("### Manual Judge Notes", 1)[1].split("### Source Links", 1)[0]
for required in [
    "Judge whether the agent searches linked or sibling artifacts after changing status, count, path, config, or verification semantics.",
    "Judge whether final verification includes a stale-language negative check.",
    "Failure if tracker, evaluation, casebook, or report status diverges, or if stale references are missed.",
]:
    assert required in e007_notes, required

assert "E008" not in cases
assert "## Case E008" not in cases
assert not Path("docs/process-v0.3.md").exists()

for unchanged in [
    "docs/process-v0.2.md",
    "docs/stage0-progress.md",
    "skills/evolving-agent-process/SKILL.md",
    "docs/v0.3-scope.md",
]:
    result = subprocess.run(["git", "diff", "--exit-code", "--", unchanged], text=True, capture_output=True)
    assert result.returncode == 0, f"unexpected diff in {unchanged}:\n{result.stdout}{result.stderr}"

print("manual judge notes verification ok")
PY
```

- Runnable block above: passed.
- `git diff --check`: passed.

## Good

The candidates are sharper for manual review while remaining lightweight and non-automated.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no new candidate; E005-E007 were only sharpened.
