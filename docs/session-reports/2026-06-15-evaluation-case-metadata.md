# Session Report: Evaluation Case Metadata

## Goal

Add lightweight per-case metadata to `docs/evaluations/behavior-cases.md` so E001-E004 do not rely only on file-level status and evidence fields.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; the task may count as real dogfood process evidence after review/commit, but the evaluation cases themselves remain seed candidates.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.

## Changes

- Updated `docs/evaluations/behavior-cases.md` only for evaluation content.
- Added per-case metadata to E001-E004:
  - `Status: candidate`
  - `Evidence type: seed`
  - `Counts toward Stage 0 exit criteria: no`
  - `Evidence links: none yet`
- Preserved the file-level status/evidence overview.
- Did not create new evaluation cases, promote candidates, update `docs/process-v0.2.md`, add automation/metrics, ADRs, or policy notes.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

cases_path = Path("docs/evaluations/behavior-cases.md")
text = cases_path.read_text()
case_matches = list(re.finditer(r"^## Case (E\d{3}):", text, re.M))
case_ids = [match.group(1) for match in case_matches]
assert case_ids == ["E001", "E002", "E003", "E004"], case_ids

required_metadata = [
    "Status: `candidate`",
    "Evidence type: `seed`",
    "Counts toward Stage 0 exit criteria: no",
    "Evidence links: none yet",
]
for index, match in enumerate(case_matches):
    case_id = match.group(1)
    end = case_matches[index + 1].start() if index + 1 < len(case_matches) else len(text)
    body = text[match.end():end]
    metadata_block = body.split("### Scenario", 1)[0]
    for required in required_metadata:
        assert required in metadata_block, f"{case_id} missing {required}"
    assert "Status: `active`" not in metadata_block, f"{case_id} promoted to active"
    assert "Evidence type: `real`" not in metadata_block, f"{case_id} promoted to real"

report = Path("docs/session-reports/2026-06-15-evaluation-case-metadata.md").read_text()
for required in [
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
]:
    assert required in report
print("evaluation case metadata ok")
PY
```

Result: passed; printed `evaluation case metadata ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The change makes seed-vs-real status explicit at the case level without expanding the evaluation file or changing the process.

## Friction

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The content change can be verified, but the run does not prove the skill works under normal sandboxed Codex execution.
- Impact: Stage 0 evidence should keep this caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in earlier dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; same sandbox caveat is already being tracked.
- ADR needed? no.
- Evaluation candidate? no new evaluation candidate; E001-E004 remain seed candidates.
