# Session Report: Evaluation Verification Hygiene

## Goal

Improve evaluation-case verification hygiene by adding a focused note to `docs/evaluations/behavior-cases.md` about avoiding implementation-detail assertions in future or existing seed cases before they become real-evidence evaluation candidates.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the sixth accepted real dogfood task after review/commit.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.
- E001/E002 evidence status: no new real evidence and no new partial evidence; this task adds hygiene guidance only.

## Changes

- Updated `docs/evaluations/behavior-cases.md`.
- Added a small `Real-Evidence Verification Hygiene` section for future or existing seed cases before real-evidence candidacy.
- Clarified that helper existence, helper call counts, and private method call/non-call assertions should not count as evidence unless tied to a concrete side-effect, security, performance, compatibility, or deprecation requirement.
- Kept E001-E004 as `Status: candidate` and `Evidence type: seed`.
- Did not update `docs/process-v0.2.md`, create policy notes, ADRs, automation, metrics, or new evaluation cases.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

cases_path = Path("docs/evaluations/behavior-cases.md")
text = cases_path.read_text()
assert "## Real-Evidence Verification Hygiene" in text
for required in (
    "future or existing seed case",
    "user-visible behavior or an explicit requirement",
    "helper existence, helper call counts, or private method call/non-call assertions",
    "side-effect, security, performance, compatibility, or deprecation requirement",
):
    assert required in text, required

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
    assert "Status: `active`" not in metadata_block, case_id
    assert "Evidence type: `real`" not in metadata_block, case_id
    assert "Counts toward Stage 0 exit criteria: yes" not in metadata_block, case_id

report = Path("docs/session-reports/2026-06-15-evaluation-verification-hygiene.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
    "E001/E002 evidence status: no new real evidence and no new partial evidence",
):
    assert required in report, required

print("evaluation verification hygiene ok")
PY
```

Result: passed; printed `evaluation verification hygiene ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The evaluation file now has a small shared guardrail for future real-evidence candidates without promoting seed cases or duplicating process rules.

## Evaluation Evidence Result

No notable assertion-style friction observed. No implementation-detail assertion was produced in this task, so E001/E002 receive no new real or partial evidence from this task.

## Friction

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The task improves behavior-evaluation hygiene, but the runtime caveat remains unrelated tooling evidence.
- Impact: Sandbox/tooling evidence must remain separate from E001/E002 behavior evidence.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior smoke and dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? no new candidate; E001-E004 remain seed candidates pending accepted behavior evidence.
