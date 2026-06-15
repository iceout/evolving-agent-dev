# Session Report: Evaluation Missing Evidence Notes

## Goal

Review seed evaluation cases E001-E004 against accepted dogfood evidence and add lightweight missing-evidence notes without promoting any case.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the fifth accepted real dogfood task after review/commit.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.

## Changes

- Updated `docs/evaluations/behavior-cases.md`.
- Added `Missing Evidence` notes to E001-E004.
- Marked E001 and E002 as partial only because Smoke Test C is adjacent to implementation-detail testing but remains calibration/not counted.
- Kept E003 and E004 as missing accepted dogfood support.
- Did not update `docs/process-v0.2.md`, create evaluation cases, promote seed cases, add policy notes, ADRs, automation, or metrics.
- Did not update `docs/stage0-progress.md` because this task is not accepted until review/commit.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

cases_path = Path("docs/evaluations/behavior-cases.md")
text = cases_path.read_text()
case_matches = list(re.finditer(r"^## Case (E\d{3}):", text, re.M))
assert [m.group(1) for m in case_matches] == ["E001", "E002", "E003", "E004"]

for index, match in enumerate(case_matches):
    case_id = match.group(1)
    end = case_matches[index + 1].start() if index + 1 < len(case_matches) else len(text)
    body = text[match.end():end]
    metadata_block = body.split("### Scenario", 1)[0]
    assert "Status: `candidate`" in metadata_block, case_id
    assert "Evidence type: `seed`" in metadata_block, case_id
    assert "Counts toward Stage 0 exit criteria: no" in metadata_block, case_id
    assert "Counts toward Stage 0 exit criteria: yes" not in metadata_block, case_id
    assert "### Missing Evidence" in metadata_block, case_id
    note = metadata_block.split("### Missing Evidence", 1)[1]
    lowered_note = note.lower()
    assert "missing evidence" in lowered_note or "partial evidence" in lowered_note, case_id
    assert "real evidence" not in lowered_note, case_id
    assert "Status: `active`" not in metadata_block, case_id
    assert "Evidence type: `real`" not in metadata_block, case_id

report = Path("docs/session-reports/2026-06-15-evaluation-missing-evidence-notes.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
):
    assert required in report
print("evaluation missing evidence notes ok")
PY
```

Result: passed; printed `evaluation missing evidence notes ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The evaluation cases now state their missing or partial support explicitly while remaining seed candidates.

## Friction

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The task reviews agent behavior evaluations while the runtime caveat is tooling-only and cannot support those evaluations.
- Impact: Sandbox/tooling evidence must remain separate from behavior-evaluation support.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior smoke and dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; the sandbox caveat is already captured in `docs/casebook/0003-sandboxed-execution-unverified.md`.
- ADR needed? no.
- Evaluation candidate? no new candidate; E001-E004 remain seed candidates pending accepted behavior evidence.
