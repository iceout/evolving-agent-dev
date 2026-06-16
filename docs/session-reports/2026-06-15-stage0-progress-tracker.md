# Session Report: Stage 0 Progress Tracker

## Goal

Create a lightweight Stage 0 progress tracker so accepted real dogfood evidence is easy to distinguish from bootstrap, smoke, and seed artifacts.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the third accepted real dogfood task after review/commit.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.

## Changes

- Added `docs/stage0-progress.md` as a manually maintained tracker.
- Recorded accepted real dogfood tasks so far:
  - `821d50c` Clarify skill install flow.
  - `c946d5f` Add evaluation case metadata.
- Recorded Smoke Test C as a calibration candidate that is not currently counted.
- Recorded the sandbox caveat and current progress toward Stage 0 exit criteria.
- Did not update `docs/process-v0.2.md`, add automation/metrics scripts, promote seed artifacts, create ADRs, or create policy notes.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path

tracker = Path("docs/stage0-progress.md").read_text()
accepted = tracker.split("## Accepted Real Dogfood Tasks", 1)[1].split("## Calibration / Not Counted", 1)[0]
not_counted = tracker.split("## Calibration / Not Counted", 1)[1].split("## Stage 0 Exit Criteria Progress", 1)[0]
progress = tracker.split("## Stage 0 Exit Criteria Progress", 1)[1]

for commit in ("821d50c", "c946d5f"):
    assert commit in accepted, f"accepted task missing {commit}"
for commit in ("96039a9", "7164b49", "a1c7428", "4a9e083"):
    assert commit not in accepted, f"non-counted artifact appears accepted: {commit}"
assert "Smoke Test C" in not_counted and "not currently counted" in not_counted
assert "Bootstrap" in not_counted or "bootstrap" in not_counted
assert "Seed casebook entries" in not_counted
assert "E001-E004" in not_counted and "remain seed artifacts" in not_counted
assert "sandboxed execution remains unverified" in tracker
assert "--dangerously-bypass-approvals-and-sandbox" in tracker
assert "2 accepted / target 3-5" in progress
assert "2 dogfood-relevant themes tracked / target 10" in progress
assert "0 accepted from real evidence / target 2" in progress
assert "1 repeated category visible / target 3" in progress

report = Path("docs/session-reports/2026-06-15-stage0-progress-tracker.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
):
    assert required in report
print("stage0 progress tracker ok")
PY
```

Result: passed; printed `stage0 progress tracker ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The tracker keeps accepted real dogfood tasks separate from calibration, bootstrap, smoke, and seed artifacts without changing the process or adding automation.

## Friction

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The tracker can clarify evidence status, but this run still does not prove normal sandboxed execution.
- Impact: Stage 0 evidence should keep the caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; same sandbox caveat is already being tracked.
- ADR needed? no.
- Evaluation candidate? no; this tracker does not create or promote evaluation cases.
