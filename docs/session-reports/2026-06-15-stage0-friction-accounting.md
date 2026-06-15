# Session Report: Stage 0 Friction Accounting

## Goal

Normalize `docs/stage0-progress.md` so Stage 0 readiness separates friction item count, unique friction themes/categories, and repeated problem categories.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the eighth accepted real dogfood task after review/commit.
- Count status: this task does not count toward accepted Stage 0 progress until review/commit and tracker bookkeeping acceptance.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.
- Accepted evidence counted in this task: 9 friction items, 3 unique themes/categories, and 1 repeated problem category from currently accepted dogfood evidence.
- Evaluation candidate status: yes; this creates E006 as a real-evidence evaluation candidate for Stage readiness metric-unit hygiene, pending review/acceptance.
- Stage 0 exit status: cannot exit now because accepted friction items are below 10, accepted real-evidence evaluation candidates are below 2, and repeated problem categories are below 3.

## Changes

- Updated `docs/stage0-progress.md`.
- Added a `Friction Accounting` section that separates:
  - explicit friction items captured,
  - unique themes/categories,
  - repeated problem categories.
- Updated the Stage 0 exit criteria table to use friction item count rather than theme count.
- Updated `docs/evaluations/behavior-cases.md` with E006, a concise real-evidence evaluation candidate for avoiding Stage readiness metric-unit conflation.
- Kept E001-E004 as seed candidates and E005 as the first accepted real-evidence evaluation candidate.
- Did not update `docs/process-v0.2.md`, create policy notes, ADRs, automation, scripts, new tooling, or skill changes.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

accepted_reports = [
    Path("docs/session-reports/2026-06-15-skill-install-flow-clarification.md"),
    Path("docs/session-reports/2026-06-15-evaluation-case-metadata.md"),
    Path("docs/session-reports/2026-06-15-stage0-progress-tracker.md"),
    Path("docs/session-reports/2026-06-15-sandboxed-execution-casebook.md"),
    Path("docs/session-reports/2026-06-15-evaluation-missing-evidence-notes.md"),
    Path("docs/session-reports/2026-06-15-evaluation-verification-hygiene.md"),
    Path("docs/session-reports/2026-06-15-response-language-rule.md"),
]

report_friction = []
for path in accepted_reports:
    text = path.read_text()
    block = text.split("## Friction", 1)[1].split("## Proposed Follow-up", 1)[0]
    for heading in re.findall(r"^###\s+(.+)$", block, re.M):
        report_friction.append((path.as_posix(), heading))

assert len(report_friction) == 8, report_friction
assert sum(1 for _, heading in report_friction if heading == "Sandbox remains unverified") == 7
assert ("docs/session-reports/2026-06-15-response-language-rule.md", "Response language expectation was implicit") in report_friction

inbox = Path("docs/casebook/inbox.md").read_text()
assert "Skill install flow unclear" in inbox
actual_friction_item_count = len(report_friction) + 1
assert actual_friction_item_count == 9

tracker = Path("docs/stage0-progress.md").read_text()
for required in (
    "## Friction Accounting",
    "9 accepted friction items / target 10",
    "3 unique themes/categories",
    "1 repeated category visible / target 3",
    "E006 is pending review/acceptance and not counted yet",
    "sandboxed execution remains unverified",
    "--dangerously-bypass-approvals-and-sandbox",
):
    assert required in tracker, required
assert "3 dogfood-relevant themes tracked / target 10" not in tracker

cases = Path("docs/evaluations/behavior-cases.md").read_text()
case_matches = list(re.finditer(r"^## Case (E\d{3}):", cases, re.M))
assert [m.group(1) for m in case_matches] == ["E001", "E002", "E003", "E004", "E005", "E006"]
for index, match in enumerate(case_matches):
    case_id = match.group(1)
    end = case_matches[index + 1].start() if index + 1 < len(case_matches) else len(cases)
    body = cases[match.end():end]
    metadata_block = body.split("### Scenario", 1)[0]
    assert "Status: `candidate`" in metadata_block, case_id
    if case_id in {"E001", "E002", "E003", "E004"}:
        assert "Evidence type: `seed`" in metadata_block, case_id
        assert "Counts toward Stage 0 exit criteria: no" in metadata_block, case_id
    elif case_id == "E005":
        assert "Evidence type: `real`" in metadata_block, case_id
        assert "Counts toward Stage 0 exit criteria: yes" in metadata_block, case_id
    else:
        assert "Evidence type: `real`" in metadata_block, case_id
        assert "Counts toward Stage 0 exit criteria: no, pending review/acceptance" in metadata_block, case_id
        assert "docs/session-reports/2026-06-15-stage0-friction-accounting.md" in metadata_block

session_report = Path("docs/session-reports/2026-06-15-stage0-friction-accounting.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "9 friction items, 3 unique themes/categories, and 1 repeated problem category",
    "E006 as a real-evidence evaluation candidate",
    "cannot exit now",
    "sandboxed execution remains unverified",
):
    assert required in session_report, required

print("stage0 friction accounting ok")
PY
```

Result: passed; printed `stage0 friction accounting ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The tracker now separates item occurrences from themes/categories and repeated problem categories, so Stage 0 readiness is less likely to be over-claimed.

## Friction

### Stage readiness metric units were conflated

- What happened: `docs/stage0-progress.md` listed the criterion "At least 10 friction items captured" but reported "3 dogfood-relevant themes tracked."
- Why it felt wrong: Items, themes/categories, and repeated problem categories answer different Stage 0 exit questions.
- Impact: Stage 0 could be judged prematurely or inconsistently if the tracker mixes units.
- Category: `process`
- Root cause guess: The tracker was manually maintained and compressed related evidence into one progress row.

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The task improves evidence accounting, but still does not validate normal sandboxed Codex execution.
- Impact: Stage 0 evidence should keep the sandbox caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior smoke and dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; the metric-unit issue is captured here and as E006, and the sandbox caveat is already in `docs/casebook/0003-sandboxed-execution-unverified.md`.
- ADR needed? no.
- Evaluation candidate? yes; E006 covers Stage readiness metric-unit separation with manual review pass/fail criteria.
