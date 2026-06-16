# Session Report: Stage 0 Exit Blocker Summary

## Goal

Add a short, human-readable summary to `docs/stage0-progress.md` explaining why Stage 0 cannot exit yet.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the ninth accepted real dogfood task after review/commit.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.
- Process-category friction recurred? no; this task kept friction items, unique themes/categories, repeated problem categories, and evaluation candidates separate.
- Non-tooling repeated category found? no; repeated problem categories remain 1 / 3.

## Changes

- Updated `docs/stage0-progress.md`.
- Added a minimal `Stage 0 Exit Blocker Summary`.
- Stated that real dogfood tasks, friction items, and real-evidence evaluation candidates are met.
- Stated that Stage 0 cannot exit because repeated problem categories remain 1 / 3.
- Did not update `docs/process-v0.2.md`, promote seed artifacts, create evaluation cases, policy notes, ADRs, automation, scripts, or new tooling.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

tracker = Path("docs/stage0-progress.md").read_text()
summary = tracker.split("## Stage 0 Exit Blocker Summary", 1)[1].split("## Stage 0 Exit Criteria Progress", 1)[0]

for required in (
    "Stage 0 cannot exit yet.",
    "Real dogfood tasks, friction items, and real-evidence evaluation candidates are met",
    "repeated problem categories remain 1 / 3",
    "12 friction items and 4 unique themes/categories do not imply 3 repeated problem categories",
):
    assert required in summary, required

assert "Stage 0 complete" not in summary
assert "Stage 0 can exit" not in summary
assert "12 friction items / 3 repeated problem categories" not in summary

cases = Path("docs/evaluations/behavior-cases.md").read_text()
case_matches = list(re.finditer(r"^## Case (E\d{3}):", cases, re.M))
assert [m.group(1) for m in case_matches] == ["E001", "E002", "E003", "E004", "E005", "E006"]
for index, match in enumerate(case_matches):
    case_id = match.group(1)
    end = case_matches[index + 1].start() if index + 1 < len(case_matches) else len(cases)
    metadata = cases[match.end():end].split("### Scenario", 1)[0]
    if case_id in {"E001", "E002", "E003", "E004"}:
        assert "Evidence type: `seed`" in metadata, case_id
        assert "Counts toward Stage 0 exit criteria: no" in metadata, case_id
    elif case_id == "E005":
        assert "Evidence type: `real`" in metadata, case_id
        assert "Counts toward Stage 0 exit criteria: yes, as 1 of 2 real-evidence evaluation candidates after tracker acceptance" in metadata, case_id
    else:
        assert "Evidence type: `real`" in metadata, case_id
        assert "Counts toward Stage 0 exit criteria: yes, as 2 of 2 real-evidence evaluation candidates after tracker acceptance" in metadata, case_id

report = Path("docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "Process-category friction recurred? no",
    "Non-tooling repeated category found? no",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
):
    assert required in report, required

print("stage0 exit blocker summary ok")
PY
```

Result: passed; printed `stage0 exit blocker summary ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The tracker now gives a quick human-readable answer before the table while preserving separate counts for items, themes/categories, repeated categories, and evaluation candidates.

## Process Friction Result

Process-category friction recurred? no. No new non-tooling repeated category appeared; repeated problem categories remain 1 / 3.

## Friction

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The tracker summary improves Stage 0 readability, but the run still does not validate normal sandboxed Codex execution.
- Impact: Stage 0 evidence should keep the sandbox caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior smoke and dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; the sandbox caveat is already in `docs/casebook/0003-sandboxed-execution-unverified.md`.
- ADR needed? no.
- Evaluation candidate? no; E005 and E006 remain the accepted real-evidence evaluation candidates, and no new evaluation case was created.
