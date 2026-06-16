# Session Report: Cross-Artifact Consistency Casebook

## Goal

Record privacy-preserving evidence from a second external real-code pilot and promote repeated cross-artifact consistency drift from inbox friction to a lightweight casebook entry.

## Evidence Status

- Dogfood: yes, for this recording task in `evolving-agent-dev`.
- Stage 0 evidence status: external pilot friction/casebook evidence only; not an accepted internal Stage 0 dogfood task and not counted in `docs/stage0-progress.md`.
- Privacy status: private repository names, local absolute paths, commit hashes, private file contents, and sensitive deployment paths are intentionally omitted.
- Evaluation status: no new evaluation candidate; E001-E004 remain seed and E005/E006 remain accepted as-is.

## Changes

- Added `docs/casebook/0004-cross-artifact-consistency-drift.md`.
- Sanitized `docs/casebook/inbox.md` so the prior external pilot entry no longer includes a private local path or repository name.
- Kept the casebook category focused on `process / cross-artifact consistency`.
- Recorded missing `pytest` only as verification friction.
- Did not update `docs/stage0-progress.md`, `docs/process-v0.2.md`, policies, ADRs, automation, tooling, or evaluation cases.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

public_artifacts = [
    Path("docs/casebook/inbox.md"),
    Path("docs/casebook/0004-cross-artifact-consistency-drift.md"),
    Path("docs/session-reports/2026-06-16-cross-artifact-consistency-casebook.md"),
]
public_text = "\n".join(path.read_text() for path in public_artifacts)

local_path_prefixes = ["/" + name + "/" for name in ("home", "Users", "private")]
local_path_pattern = re.compile(r"(?<![\w.-])(?:" + "|".join(re.escape(prefix) for prefix in local_path_prefixes) + r"|[A-Za-z]:\\)")
assert not local_path_pattern.search(public_text), "local absolute path found in public-facing artifacts"
assert not re.search(r"\b[0-9a-f]{7,40}\b", public_text), "commit-like hash found in public-facing artifacts"

case = Path("docs/casebook/0004-cross-artifact-consistency-drift.md").read_text()
for required in (
    "Cross-Artifact Consistency Drift",
    "privacy-preserving external pilots and internal stale verification evidence",
    "This case intentionally omits private repository names, local absolute paths, commit hashes, private file contents, and sensitive deployment paths.",
    "- process / cross-artifact consistency",
    "runtime data layout documentation, download security documentation, and a settings template",
    "No active runtime code changed.",
    "stale documentation",
    "old static-file configuration behavior",
    "current code used a different configuration approach",
    "Internal stale-verification evidence",
    "docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md",
    "`pytest` was unavailable and not declared in the project dependency file",
    "casebook evidence only",
    "Do not count the external pilots as accepted internal Stage 0 dogfood tasks",
    "Do not create an evaluation candidate",
):
    assert required in case, required

category_block = case.split("## Category", 1)[1].split("## Privacy Boundary", 1)[0]
assert "tooling / missing test dependency" not in category_block

inbox = Path("docs/casebook/inbox.md").read_text()
assert "external private code project" in inbox
assert "Current routing decision: friction evidence only" in inbox

tracker = Path("docs/stage0-progress.md").read_text()
for required in (
    "9 accepted / target 3-5",
    "12 accepted friction items / target 10",
    "2 accepted from real evidence / target 2",
    "1 repeated category visible / target 3",
):
    assert required in tracker, required

cases = Path("docs/evaluations/behavior-cases.md").read_text()
assert "E005 and E006 are accepted real-evidence evaluation candidates" in cases
assert "## Case E007" not in cases

process = Path("docs/process-v0.2.md").read_text()
assert "Agent Development Process v0.2" in process

print("cross artifact consistency casebook ok")
PY
```

Result: passed; printed `cross artifact consistency casebook ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The repeated cross-artifact consistency pattern is now reusable evidence without exposing private repository identity or sensitive path details.

## Friction

### Privacy boundary needed for external pilot evidence

- What happened: External private pilot evidence was useful, but raw details could expose private repository identity or deployment specifics in a repo that may become public.
- Why it felt wrong: Process evidence should remain shareable without leaking private project details.
- Impact: Future external pilot evidence needs artifact-type and behavior-level summaries unless explicit disclosure is allowed.
- Category: `process`
- Root cause guess: The Stage 0 evidence system was designed around internal repo artifacts and needed a privacy-preserving recording pass for external pilots.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: completed by `docs/casebook/0004-cross-artifact-consistency-drift.md`.
- ADR needed? no.
- Evaluation candidate? no; wait until the pattern becomes high-signal, judgeable, and reproducible without private repository details.
