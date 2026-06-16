# Session Report: Cross-Artifact Consistency Evaluation Review

## Goal

Review the privacy-preserving evidence around cross-artifact consistency drift and decide whether it should remain casebook-only or become a behavior evaluation candidate.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: this is a real dogfood task candidate, but it counts toward Stage 0 only after review, commit, and explicit acceptance.
- Evaluation status: E007 was added as a real-evidence evaluation candidate pending review/acceptance; E001-E004 remain seed and E005/E006 remain accepted as-is.
- Stage 0 tracker status: unchanged; E007 does not change accepted task counts, accepted evaluation-candidate counts, or repeated-category counts yet.
- Sandbox note: the existing tracker caveat remains unchanged; this task did not re-verify sandboxed execution coverage.

## Changes

- Updated `docs/casebook/0004-cross-artifact-consistency-drift.md` to state that the casebook evidence now supports E007 as a pending candidate.
- Added E007 to `docs/evaluations/behavior-cases.md` for preserving cross-artifact consistency across deployment/configuration docs and templates.
- Did not edit `docs/process-v0.2.md`, `docs/stage0-progress.md`, policies, ADRs, automation, or tooling.

## Decision

The pattern is now strong enough for a candidate because it has repeated privacy-preserving external observations plus related internal stale-verification evidence. It is judgeable by reviewing whether sibling docs/templates and stale references were found and updated consistently. It is reproducible with a synthetic fixture that uses artifact types and generic path assumptions instead of private repository details.

E007 is still not accepted or countable until review/commit acceptance.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess

public_artifacts = [
    Path("docs/casebook/inbox.md"),
    Path("docs/casebook/0004-cross-artifact-consistency-drift.md"),
    Path("docs/session-reports/2026-06-16-cross-artifact-consistency-casebook.md"),
    Path("docs/session-reports/2026-06-16-cross-artifact-consistency-evaluation-review.md"),
    Path("docs/evaluations/behavior-cases.md"),
]
public_text = "\n".join(path.read_text() for path in public_artifacts)

local_path_prefixes = ["/" + name + "/" for name in ("home", "Users", "private")]
local_path_pattern = re.compile(r"(?<![\w.-])(?:" + "|".join(re.escape(prefix) for prefix in local_path_prefixes) + r"|[A-Za-z]:\\)")
assert not local_path_pattern.search(public_text), "local absolute path found in public-facing artifacts"
assert not re.search(r"\b[0-9a-f]{7,40}\b", public_text), "commit-like hash found in public-facing artifacts"

cases = Path("docs/evaluations/behavior-cases.md").read_text()

def case_section(case_id, next_case_id=None):
    marker = f"## Case {case_id}:"
    start = cases.index(marker)
    if next_case_id:
        end = cases.index(f"## Case {next_case_id}:", start)
    else:
        end = len(cases)
    return cases[start:end]

for case_id in ("E001", "E002", "E003", "E004"):
    section = case_section(case_id, f"E{int(case_id[1:]) + 1:03d}")
    assert "Status: `candidate`" in section, case_id
    assert "Evidence type: `seed`" in section, case_id
    assert "Counts toward Stage 0 exit criteria: no" in section, case_id

for case_id, count_line, link in (
    ("E005", "Counts toward Stage 0 exit criteria: yes, as 1 of 2 real-evidence evaluation candidates after tracker acceptance", "docs/session-reports/2026-06-15-response-language-rule.md"),
    ("E006", "Counts toward Stage 0 exit criteria: yes, as 2 of 2 real-evidence evaluation candidates after tracker acceptance", "docs/session-reports/2026-06-15-stage0-friction-accounting.md"),
):
    next_id = "E006" if case_id == "E005" else "E007"
    section = case_section(case_id, next_id)
    assert "Status: `candidate`" in section, case_id
    assert "Evidence type: `real`" in section, case_id
    assert count_line in section, case_id
    assert link in section, case_id

section = case_section("E007")
assert "Status: `candidate`" in section
assert "Evidence type: `real`" in section
assert "Counts toward Stage 0 exit criteria: no, pending review/acceptance" in section
for link in (
    "docs/casebook/0004-cross-artifact-consistency-drift.md",
    "docs/casebook/inbox.md",
    "docs/session-reports/2026-06-16-cross-artifact-consistency-casebook.md",
):
    assert link in section, link
assert "docs/stage0-progress.md" not in section

casebook = Path("docs/casebook/0004-cross-artifact-consistency-drift.md").read_text()
assert "supports E007 as a privacy-preserving real-evidence evaluation candidate pending review/acceptance" in casebook
assert "Do not count E007 toward Stage 0 until it is reviewed and accepted" in casebook

tracker = Path("docs/stage0-progress.md").read_text()
assert "2 accepted from real evidence / target 2" in tracker
assert "1 repeated category visible / target 3" in tracker
assert "Stage 0 cannot exit yet" in tracker
subprocess.check_call(["git", "diff", "--quiet", "--", "docs/process-v0.2.md"])
subprocess.check_call(["git", "diff", "--quiet", "--", "docs/stage0-progress.md"])

print("cross artifact evaluation review ok")
PY
```

Result: passed; printed `cross artifact evaluation review ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

Manual privacy review: the new candidate uses only artifact-type descriptions and generic fixture names; it does not record private project names, local absolute paths, private commit hashes, private file contents, or sensitive deployment paths.

## Good

The casebook-to-evaluation routing stayed conservative: repeated evidence produced a pending candidate, not an accepted count or policy.

## Friction

No notable friction.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; the casebook entry already exists.
- ADR needed? no.
- Evaluation candidate? yes; E007 is now a pending real-evidence candidate for cross-artifact consistency behavior.
