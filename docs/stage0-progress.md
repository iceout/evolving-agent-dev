# Stage 0 Progress Tracker

Last updated: 2026-06-15

This is a manually maintained tracker for Stage 0 progress. It distinguishes accepted real dogfood evidence from bootstrap work, smoke tests, and seed artifacts. It is not an automation or metrics source.

## Counting Rule

Count a task only when it is an installed-skill dogfood edit task, has a session report, has been reviewed/accepted, and is traceable to a commit. Do not count bootstrap setup, smoke-test harness results, seed casebook entries, or seed evaluation cases as real Stage 0 evidence.

Known caveat: sandboxed execution remains unverified because this environment uses `--dangerously-bypass-approvals-and-sandbox`.

## Accepted Real Dogfood Tasks

| # | Commit | Task | Evidence | Notes |
|---|---|---|---|---|
| 1 | `f62c6b6` | Clarify skill install flow | `docs/session-reports/2026-06-15-skill-install-flow-clarification.md` | Accepted real dogfood task; sandbox caveat applies. |
| 2 | `4875411` | Add evaluation case metadata | `docs/session-reports/2026-06-15-evaluation-case-metadata.md` | Accepted real dogfood task; evaluation cases remain seed candidates. |
| 3 | `1c75db6` | Add Stage 0 progress tracker | `docs/session-reports/2026-06-15-stage0-progress-tracker.md` | Accepted real dogfood task; sandbox caveat applies. |
| 4 | `a2e5310` | Add sandbox execution caveat case | `docs/session-reports/2026-06-15-sandboxed-execution-casebook.md` | Accepted real dogfood task; added `docs/casebook/0003-sandboxed-execution-unverified.md`. |

## Calibration / Not Counted

- Smoke Test C (`a391c7d`, `docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md`) is a calibration candidate, not currently counted as an accepted real dogfood task.
- `docs/session-reports/2026-06-15-codex-skill-smoke-tests.md` is smoke-test harness evidence, not an additional real task.
- Bootstrap, installation, canonical-skill-draft, and skill-design-hardening reports are setup evidence, not real dogfood tasks.
- Seed casebook entries and E001-E004 in `docs/evaluations/behavior-cases.md` remain seed artifacts unless later linked to accepted real sessions or friction entries.

## Stage 0 Exit Criteria Progress

| Criterion | Current progress | Status |
|---|---:|---|
| 3-5 real tasks run through the process | 4 accepted / target 3-5 | In range |
| At least 10 friction items captured | 2 dogfood-relevant themes tracked / target 10: skill install flow unclear; sandbox remains unverified. Casebook entries from real dogfood: 1 (`docs/casebook/0003-sandboxed-execution-unverified.md`) | In progress |
| At least 2 evaluation candidates identified from real evidence | 0 accepted from real evidence / target 2; E001-E004 remain seed candidates | Not met |
| Top 3 repeated problem categories visible | 1 repeated category visible / target 3: tooling/sandbox | Not met |

## Next Update Rule

When a dogfood task is accepted, add its commit, task title, and session report path here. Keep calibration and seed artifacts separate unless a later review explicitly accepts them as Stage 0 real evidence. Post-commit tracker bookkeeping updates do not count as separate Stage 0 tasks.
