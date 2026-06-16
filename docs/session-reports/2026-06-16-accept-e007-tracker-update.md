# Session Report: Accept E007 Tracker Update

## Goal

Accept the tenth real dogfood task and E007, then update the Stage 0 tracker and behavior evaluation metadata consistently.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: bookkeeping/acceptance update for an already reviewed dogfood task; this update itself is not a new real dogfood task.
- Accepted task: `f1292c2` is accepted as real dogfood task #10.
- Accepted evaluation candidate: E007 is accepted as the third real-evidence evaluation candidate.
- Repeated category decision: `process` / cross-artifact consistency drift is counted as the second repeated problem category based on privacy-preserving external pilots plus internal stale-verification evidence, not accepted internal dogfood task count.
- Exclusions: external pilots are not accepted internal Stage 0 dogfood tasks; public hygiene pass `4d35e24` is not a Stage 0 real dogfood task.
- Sandbox caveat: unchanged; sandboxed execution remains unverified in the tracker.

## Changes

- Updated `docs/stage0-progress.md` to add task #10, accept E007, keep public hygiene/external pilots out of accepted internal dogfood task counts, and move repeated problem categories from 1 / 3 to 2 / 3.
- Updated `docs/evaluations/behavior-cases.md` so E007 is accepted consistently with E005/E006.
- Updated `docs/casebook/0004-cross-artifact-consistency-drift.md` so the casebook no longer describes E007 as pending review/acceptance.
- Did not edit `docs/process-v0.2.md`, policies, ADRs, automation, or tooling.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

tracker = Path("docs/stage0-progress.md").read_text()
cases = Path("docs/evaluations/behavior-cases.md").read_text()
casebook = Path("docs/casebook/0004-cross-artifact-consistency-drift.md").read_text()
report = Path("docs/session-reports/2026-06-16-accept-e007-tracker-update.md").read_text()

accepted = tracker.split("## Accepted Real Dogfood Tasks", 1)[1].split("## Calibration / Not Counted", 1)[0]
accepted_rows = re.findall(r"^\| \d+ \| `([0-9a-f]{7})` \| ([^|]+) \| ([^|]+) \|", accepted, re.M)
assert len(accepted_rows) == 10, accepted_rows
assert any(row[0] == "f1292c2" and "cross-artifact consistency" in row[1] for row in accepted_rows)
assert "4d35e24" not in accepted
assert "Public hygiene pass (`4d35e24`" in tracker
assert "External pilots are cross-artifact consistency evidence, but they are not accepted internal Stage 0 dogfood tasks." in tracker

for short_hash, subject, _evidence in accepted_rows:
    resolved_subject = subprocess.check_output(["git", "log", "-1", "--format=%s", short_hash], text=True).strip()
    assert resolved_subject == subject.strip(), (short_hash, resolved_subject, subject)

def section(case_id, next_case_id=None):
    marker = f"## Case {case_id}:"
    start = cases.index(marker)
    end = cases.index(f"## Case {next_case_id}:", start) if next_case_id else len(cases)
    return cases[start:end]

for case_id in ("E001", "E002", "E003", "E004"):
    body = section(case_id, f"E{int(case_id[1:]) + 1:03d}")
    assert "Status: `candidate`" in body, case_id
    assert "Evidence type: `seed`" in body, case_id
    assert "Counts toward Stage 0 exit criteria: no" in body, case_id

for case_id, count_text in (
    ("E005", "Counts toward Stage 0 exit criteria: yes, as 1 of 3 real-evidence evaluation candidates after tracker acceptance"),
    ("E006", "Counts toward Stage 0 exit criteria: yes, as 2 of 3 real-evidence evaluation candidates after tracker acceptance"),
    ("E007", "Counts toward Stage 0 exit criteria: yes, as 3 of 3 real-evidence evaluation candidates after tracker acceptance"),
):
    next_id = f"E{int(case_id[1:]) + 1:03d}" if case_id != "E007" else None
    body = section(case_id, next_id)
    assert "Status: `candidate`" in body, case_id
    assert "Evidence type: `real`" in body, case_id
    assert count_text in body, case_id

for required in (
    "10 accepted / target 3-5",
    "12 accepted friction items / target 10",
    "3 accepted from real evidence / target 2",
    "2 repeated categories visible / target 3",
    "Stage 0 cannot exit yet",
    "external pilots are not accepted internal dogfood tasks",
):
    assert required in tracker, required

assert "supports E007 as an accepted privacy-preserving real-evidence evaluation candidate" in casebook
assert "E007 counts as an accepted real-evidence evaluation candidate after tracker acceptance." in casebook
for stale in (
    "E007 as a privacy-preserving real-evidence evaluation candidate pending review/acceptance",
    "Do not count E007 toward Stage 0 until it is reviewed and accepted",
):
    assert stale not in casebook, stale

public_text = "\n".join(path.read_text() for path in (
    Path("docs/stage0-progress.md"),
    Path("docs/evaluations/behavior-cases.md"),
    Path("docs/casebook/0004-cross-artifact-consistency-drift.md"),
    Path("docs/session-reports/2026-06-16-accept-e007-tracker-update.md"),
))
local_path_pattern = re.compile(r"(?<![\w.-])(?:/(?:home|Users|private)/[^\s`)]+|[A-Za-z]:\\[^\s`)]+)")
assert not local_path_pattern.search(public_text), "local absolute path found"

for token in set(re.findall(r"\b[0-9a-f]{7,40}\b", public_text)):
    subprocess.check_call(["git", "cat-file", "-e", f"{token}^{{commit}}"], stdout=subprocess.DEVNULL)

for path in (
    Path("docs/stage0-progress.md"),
    Path("docs/evaluations/behavior-cases.md"),
    Path("docs/casebook/0004-cross-artifact-consistency-drift.md"),
    Path("docs/session-reports/2026-06-16-accept-e007-tracker-update.md"),
):
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        assert line.rstrip() == line, (path, lineno)

subprocess.check_call(["git", "diff", "--quiet", "--", "docs/process-v0.2.md"])
print("accept e007 tracker update ok")
PY
```

Result: passed; printed `accept e007 tracker update ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors in tracked diffs. The Python block also checks trailing whitespace in the new session report.

Manual privacy review: no private repo names, local absolute paths, private commit hashes, or private file contents were introduced; public repo commit hashes are intentionally retained for tracker traceability.

## Good

The tracker now separates accepted internal dogfood task count from external/internal evidence used to recognize a repeated category.

## Friction

### Cross-artifact status drift during E007 acceptance

- What happened: The tracker and evaluation file accepted E007, but the related casebook entry still described E007 as pending review/acceptance.
- Why it felt wrong: The task was specifically about cross-artifact consistency, yet one linked evidence artifact kept stale status language.
- Impact: Readers could see conflicting E007 status across tracker, evaluation cases, and casebook evidence.
- Category: `process`
- Root cause guess: Verification covered tracker and evaluation metadata but did not include the linked casebook evidence file.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no.
- Evaluation candidate? completed by accepting E007.
