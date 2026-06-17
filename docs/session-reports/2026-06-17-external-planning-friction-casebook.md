# Session Report: External Planning Friction Casebook

## Goal

Record a privacy-preserving external planning/tool-selection friction observation and route the repeated planning-impact pattern to a lightweight casebook entry.

## Evidence Status

- Dogfood: yes, for this recording task in `evolving-agent-dev`.
- Stage 0 evidence status: external friction evidence only; not an accepted internal Stage 0 dogfood task and not counted in `docs/stage0-progress.md`.
- Evaluation status: no new evaluation candidate; E001-E004 remain seed and E005-E007 remain accepted as-is.
- Stage 0 status: not complete; tracker counts are unchanged.
- Privacy status: private repository names, local absolute paths, private commit hashes, private code contents, user identifiers, exact tool names, exact dates, and sensitive operational details are omitted.

## Changes

- Added a privacy-preserving inbox entry for external planning/tool-selection friction.
- Added `docs/casebook/0005-planning-impact-analysis-gaps.md` because this is now a repeated reusable planning-impact pattern across external observations.
- Did not update `docs/stage0-progress.md`, create E008, create policy/ADR/automation/tooling, or edit `docs/process-v0.2.md`.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

inbox = Path("docs/casebook/inbox.md").read_text()
casebook = Path("docs/casebook/0005-planning-impact-analysis-gaps.md").read_text()
report = Path("docs/session-reports/2026-06-17-external-planning-friction-casebook.md").read_text()
tracker = Path("docs/stage0-progress.md").read_text()
cases = Path("docs/evaluations/behavior-cases.md").read_text()

entry = inbox.split("### 2026-06-17 - External planning tool-selection friction", 1)[1]
for required in (
    "recent retention window",
    "historical lookup",
    "rolling-hour window",
    "rolling-window semantics",
    "runtime guard",
    "prompt/schema-oriented tests",
    "real LLM tool-selection dogfood",
    "calendar-day vs rolling-hour window",
    "data-source retention",
    "start-time vs full-window rules",
    "boundary splitting",
    "`process` / `planning impact analysis`",
    "`requirements` / `retention semantics`",
    "`context` / `missed tool capability`",
    "`testing` / `behavior-level regression gap`",
    "`process` / `cross-artifact consistency`",
    "Do not count as an accepted internal Stage 0 dogfood task or create E008",
):
    assert required in entry, required

for required in (
    "Planning Impact Analysis Gaps",
    "real external friction",
    "performance-oriented plan",
    "tool-selection repair plan",
    "overlapping log-query capabilities",
    "behavior-level regression tests",
    "calendar-day vs rolling-hour window semantics",
    "boundary splitting",
    "Do not create E008",
):
    assert required in casebook, required

evidence_text = "\n".join([entry, casebook])
local_path_pattern = re.compile(r"(?<![\w.-])(?:/(?:home|Users|private)/[^\s`)]+|[A-Za-z]:\\[^\s`)]+)")
assert not local_path_pattern.search(evidence_text), "local absolute path found"
assert not re.search(r"\b[0-9a-f]{7,40}\b", evidence_text), "commit-like hash found"
for forbidden in (
    "repository name:",
    "local path:",
    "commit hash:",
    "user id:",
    "tool name:",
):
    assert forbidden not in evidence_text.lower(), forbidden

allowed_categories = {"testing", "implementation", "requirements", "process", "context", "review", "tooling"}
for source in (entry, casebook):
    for match in re.findall(r"`([^`]+)` /", source):
        assert match in allowed_categories, match

for required in (
    "10 accepted / target 3-5",
    "12 accepted friction items / target 10",
    "3 accepted from real evidence / target 2",
    "2 repeated categories visible / target 3",
    "Stage 0 cannot exit yet",
):
    assert required in tracker, required

assert "## Case E008" not in cases
for case_id in ("E001", "E002", "E003", "E004"):
    marker = f"## Case {case_id}:"
    start = cases.index(marker)
    next_id = f"E{int(case_id[1:]) + 1:03d}"
    end = cases.index(f"## Case {next_id}:", start)
    body = cases[start:end]
    assert "Evidence type: `seed`" in body, case_id
    assert "Counts toward Stage 0 exit criteria: no" in body, case_id
for case_id in ("E005", "E006", "E007"):
    marker = f"## Case {case_id}:"
    start = cases.index(marker)
    next_id = f"E{int(case_id[1:]) + 1:03d}" if case_id != "E007" else None
    end = cases.index(f"## Case {next_id}:", start) if next_id else len(cases)
    body = cases[start:end]
    assert "Evidence type: `real`" in body, case_id
    assert "Counts toward Stage 0 exit criteria: yes" in body, case_id

for path in (
    "docs/stage0-progress.md",
    "docs/evaluations/behavior-cases.md",
    "docs/process-v0.2.md",
):
    subprocess.check_call(["git", "diff", "--quiet", "--", path])

for path in (
    Path("docs/casebook/inbox.md"),
    Path("docs/casebook/0005-planning-impact-analysis-gaps.md"),
    Path("docs/session-reports/2026-06-17-external-planning-friction-casebook.md"),
):
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        assert line.rstrip() == line, (path, lineno)

print("external planning tool-selection friction ok")
PY
```

Result: passed; printed `external planning tool-selection friction ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The evidence stays privacy-preserving while routing a repeated planning-impact pattern to casebook without creating E008 or changing Stage 0 counts.

## Friction

No notable new friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: completed as `docs/casebook/0005-planning-impact-analysis-gaps.md`.
- ADR needed? no.
- Evaluation candidate? no; wait for a judgeable fixture before creating E008.
