# Session Report: Sandboxed Execution Caveat Casebook

## Goal

Create a lightweight casebook entry for the repeated sandboxed execution caveat so dogfood evidence is interpreted with the right runtime limitation.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the fourth accepted real dogfood task after review/commit.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.

## Changes

- Added `docs/casebook/0003-sandboxed-execution-unverified.md`.
- Classified the case as tooling/process friction.
- Linked the case to the smoke report and accepted dogfood reports that carry the caveat.
- Did not update `docs/stage0-progress.md` because the sandbox theme is already reflected there and this task is not accepted until review/commit.
- Did not update `docs/process-v0.2.md`, create policy notes, ADRs, evaluations, automation, or metrics.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path

case = Path("docs/casebook/0003-sandboxed-execution-unverified.md").read_text()
report = Path("docs/session-reports/2026-06-15-sandboxed-execution-casebook.md").read_text()

required_links = [
    "docs/session-reports/2026-06-15-codex-skill-smoke-tests.md",
    "docs/session-reports/2026-06-15-skill-install-flow-clarification.md",
    "docs/session-reports/2026-06-15-evaluation-case-metadata.md",
    "docs/session-reports/2026-06-15-stage0-progress-tracker.md",
]
for link in required_links:
    assert link in case, f"missing casebook source link: {link}"

for required in [
    "sandboxed execution could not be verified",
    "sandboxed execution remains unverified",
    "--dangerously-bypass-approvals-and-sandbox",
    "tooling",
    "process",
    "not an agent behavior evaluation",
]:
    assert required in case, f"case missing {required}"

for forbidden in [
    "## Candidate Policy",
    "## Candidate Evaluation",
    "## ADR",
    "Policy note candidate: yes",
    "Evaluation candidate? yes",
]:
    assert forbidden not in case, f"case proposes forbidden artifact: {forbidden}"

for required in [
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
]:
    assert required in report, f"report missing {required}"

print("sandboxed execution casebook ok")
PY
```

Result: passed; printed `sandboxed execution casebook ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The repeated sandbox caveat now has one reusable casebook entry without turning an environment/tooling limitation into a policy, ADR, or agent behavior evaluation.

## Friction

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The task records a caveat about sandboxing while still running in the same unsandboxed mode.
- Impact: Stage 0 evidence should keep this caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior smoke and dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: completed by `docs/casebook/0003-sandboxed-execution-unverified.md`.
- ADR needed? no.
- Evaluation candidate? no; this is environment/tooling evidence, not an agent behavior regression.
