---
name: bug-investigation-loop
description: "Use when the user reports a bug, failing test, stack trace, error, 500, regression, unexpected behavior, broken command/page/job, or asks why something is broken. Performs root-cause investigation before fixing, verifies hypotheses, adds regression coverage when fixing, and reports evidence. Hand off to coding-review-loop when the fix becomes medium/high-risk or needs a plan/review packet."
---

# Bug Investigation Loop

Use this skill for real-code bug investigation. It is for finding root cause before fixing.

Do not jump to a fix before root cause is established. If the issue becomes a non-trivial implementation plan, public interface change, schema/contract change, data semantics change, sensitive-output change, or multi-module refactor, hand off to `coding-review-loop`.

Keep the first pass lightweight: gather enough evidence to avoid guessing, not a complete incident response process.

## Workflow

1. Intake
   - Collect the symptom, expected behavior, reproduction steps, affected command/test/page/job, environment, and recent changes if known.
   - Ask one focused question if critical evidence is missing and cannot be discovered locally.
   - If a stack trace or log includes sensitive data, summarize only the relevant frame, error type, and boundary.

2. Reproduce / Observe
   - Run the failing test, command, or minimal reproduction when available.
   - Capture the exact failure, including command, status, and key output.
   - If the issue is not reproducible, record what evidence is missing and avoid completion claims.

3. Trace
   - Trace the code path from symptom backward through callers, entrypoints, config, feature flags, source-of-truth data, and boundary adapters.
   - Use search to find related references before changing code.
   - Use `git log --oneline -20 -- <affected-files>` when regression timing matters.
   - Separate observed facts from assumptions.

4. Hypothesize
   - State one specific, testable root-cause hypothesis.
   - Explain the evidence chain from symptom to candidate cause.
   - Do not implement yet.

5. Test Hypothesis
   - Confirm with a targeted test, command, assertion, log, debugger output, or code inspection.
   - If the hypothesis fails, update the evidence chain before forming the next one.
   - After three failed hypotheses, stop and ask whether to continue, instrument, or escalate.

6. Fix Boundary
   - If root cause is confirmed and the fix is small, make the minimal root-cause fix.
   - Add or update a regression test that would fail without the fix.
   - If the fix touches public interfaces, schemas/contracts, data semantics, sensitive output, entrypoint behavior, or multiple modules, hand off to `coding-review-loop`.
   - If the fix touches more than a small local area, ask before broadening scope.
   - If only a mitigation is possible, label it as mitigation and keep it separate from a root-cause fix.

7. Verify
   - Rerun the original reproduction.
   - Run the regression test.
   - Run relevant existing tests for touched entrypoints or modules.
   - State verification limits clearly, especially for intermittent, environment-specific, staging-only, or production-only issues.

8. Report
   - Use `references/debug-report-shape.md` for non-trivial investigations.
   - Small investigations can keep the report in the final response.

## External Search Boundary

Search external references only after local evidence is gathered or when the error clearly points to a framework/library issue. Sanitize first: remove hostnames, IPs, file paths, SQL, customer identifiers, internal names, tokens, and sensitive payloads. Search generic error type and framework/library context, not raw private messages.

Treat external results as candidate hypotheses until confirmed against the local code, runtime, or reproduction.

## Case Note Capture

If the investigation produces a reusable pitfall, process friction, verification gap, or future evaluation candidate, capture a privacy-preserving note in the target repo.

Prefer `.agent/bug-investigation-cases.md` when the target repo has no existing convention. If the repo should not keep agent notes, ask the user where to place the note or include the case note in the final response.

Treat these notes as local transfer artifacts by default; do not include them in product commits unless the user or target repo convention explicitly wants agent notes committed.

Do not record private data, credentials, customer identifiers, sensitive payloads, large code excerpts, or full chat transcripts. Generalize file paths, business identifiers, and data samples when needed.

No reusable pitfall, friction, verification gap, or handoff candidate does not require a case note.

## Reference

Read `references/debug-report-shape.md` only when writing a non-trivial debug report.
