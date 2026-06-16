# Stage 0 Progress Tracker

Last updated: 2026-06-16

This is a manually maintained tracker for Stage 0 progress. It distinguishes accepted real dogfood evidence from bootstrap work, smoke tests, and seed artifacts. It is not an automation or metrics source.

## Counting Rule

Count a task only when it is an installed-skill dogfood edit task, has a session report, has been reviewed/accepted, and is traceable to a commit. Do not count bootstrap setup, smoke-test harness results, seed casebook entries, or seed evaluation cases as real Stage 0 evidence.

Known caveat: sandboxed execution remains unverified because this environment uses `--dangerously-bypass-approvals-and-sandbox`.

## Accepted Real Dogfood Tasks

| # | Commit | Task | Evidence | Notes |
|---|---|---|---|---|
| 1 | `a1ba604` | Clarify skill install flow | `docs/session-reports/2026-06-15-skill-install-flow-clarification.md` | Accepted real dogfood task; sandbox caveat applies. |
| 2 | `a0aa105` | Add evaluation case metadata | `docs/session-reports/2026-06-15-evaluation-case-metadata.md` | Accepted real dogfood task; evaluation cases remain seed candidates. |
| 3 | `2154dee` | Add Stage 0 progress tracker | `docs/session-reports/2026-06-15-stage0-progress-tracker.md` | Accepted real dogfood task; sandbox caveat applies. |
| 4 | `7326fd3` | Add sandbox execution caveat case | `docs/session-reports/2026-06-15-sandboxed-execution-casebook.md` | Accepted real dogfood task; added `docs/casebook/0003-sandboxed-execution-unverified.md`. |
| 5 | `65b5389` | Add evaluation missing evidence notes | `docs/session-reports/2026-06-15-evaluation-missing-evidence-notes.md` | Accepted real dogfood task; E001-E004 remain seed candidates. |
| 6 | `df269c1` | Add evaluation verification hygiene | `docs/session-reports/2026-06-15-evaluation-verification-hygiene.md` | Accepted real dogfood task; no new real or partial evidence for E001/E002. |
| 7 | `916a83a` | Add response language behavior | `docs/session-reports/2026-06-15-response-language-rule.md` | Accepted real dogfood task; added E005 as a real-evidence evaluation candidate for final response language. |
| 8 | `3091863` | Normalize Stage 0 friction accounting | `docs/session-reports/2026-06-15-stage0-friction-accounting.md` | Accepted real dogfood task; added E006 as a real-evidence evaluation candidate for Stage readiness metric-unit hygiene. |
| 9 | `5f3d1d2` | Add Stage 0 exit blocker summary | `docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md` | Accepted real dogfood task; clarified Stage 0 cannot exit while repeated problem categories remain 1 / 3. |

## Calibration / Not Counted

- Smoke Test C (`b75d5dd`, `docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md`) is a calibration candidate, not currently counted as an accepted real dogfood task.
- `docs/session-reports/2026-06-15-codex-skill-smoke-tests.md` is smoke-test harness evidence, not an additional real task.
- Bootstrap, installation, canonical-skill-draft, and skill-design-hardening reports are setup evidence, not real dogfood tasks.
- Seed casebook entries and E001-E004 in `docs/evaluations/behavior-cases.md` remain seed artifacts unless later linked to accepted real sessions or friction entries.

## Friction Accounting

Friction item count, unique themes/categories, and repeated problem categories are tracked separately. Count only explicit friction from accepted dogfood session reports or accepted tracker evidence; do not count bootstrap, smoke, setup, seed artifacts, or pending dogfood tasks.

Current accepted-evidence totals: 12 friction items; 4 unique themes/categories; 1 repeated problem category.

### Friction Items Captured

| # | Source | Item | Category | Count basis |
|---|---|---|---|---|
| 1 | `docs/casebook/inbox.md` / accepted task `a1ba604` | Skill install flow unclear | `tooling` | Inbox friction tied to accepted dogfood task. |
| 2 | `docs/session-reports/2026-06-15-skill-install-flow-clarification.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 3 | `docs/session-reports/2026-06-15-evaluation-case-metadata.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 4 | `docs/session-reports/2026-06-15-stage0-progress-tracker.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 5 | `docs/session-reports/2026-06-15-sandboxed-execution-casebook.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 6 | `docs/session-reports/2026-06-15-evaluation-missing-evidence-notes.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 7 | `docs/session-reports/2026-06-15-evaluation-verification-hygiene.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 8 | `docs/session-reports/2026-06-15-response-language-rule.md` | Response language expectation was implicit | `requirements` | Accepted session report friction. |
| 9 | `docs/session-reports/2026-06-15-response-language-rule.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 10 | `docs/session-reports/2026-06-15-stage0-friction-accounting.md` | Stage readiness metric units were conflated | `process` | Accepted session report friction. |
| 11 | `docs/session-reports/2026-06-15-stage0-friction-accounting.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |
| 12 | `docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md` | Sandbox remains unverified | `tooling` | Accepted session report friction. |

### Themes / Categories

| Theme/category | Item count | Repeated? | Notes |
|---|---:|---|---|
| `tooling` / skill install flow unclear | 1 | no | Installation path/copy-vs-symlink verification was unclear. |
| `tooling` / sandbox remains unverified | 9 | yes | Repeated across accepted dogfood reports; captured in `docs/casebook/0003-sandboxed-execution-unverified.md`. |
| `requirements` / response language expectation implicit | 1 | no | Produced accepted real-evidence candidate E005. |
| `process` / stage readiness metric units conflated | 1 | no | Produced accepted real-evidence candidate E006. |

### Repeated Problem Categories

| Category/theme | Evidence | Status |
|---|---|---|
| `tooling` / sandbox remains unverified | 9 accepted dogfood friction items, plus casebook entry `docs/casebook/0003-sandboxed-execution-unverified.md` | Repeated problem category visible. |

## Stage 0 Exit Blocker Summary

Stage 0 cannot exit yet. Real dogfood tasks, friction items, and real-evidence evaluation candidates are met, but repeated problem categories remain 1 / 3. Keep these units separate: 12 friction items and 4 unique themes/categories do not imply 3 repeated problem categories.

## Stage 0 Exit Criteria Progress

| Criterion | Current progress | Status |
|---|---:|---|
| 3-5 real tasks run through the process | 9 accepted / target 3-5 | Over target; continue only for missing exit criteria |
| At least 10 friction items captured | 12 accepted friction items / target 10; see Friction Accounting | Met |
| At least 2 evaluation candidates identified from real evidence | 2 accepted from real evidence / target 2: E005 final response language; E006 Stage readiness metric-unit hygiene. E001-E004 remain seed candidates | Met |
| Top 3 repeated problem categories visible | 1 repeated category visible / target 3: `tooling` / sandbox remains unverified. Unique themes/categories visible: 4 | Not met |

## Next Update Rule

When a dogfood task is accepted, add its commit, task title, and session report path here. Keep calibration and seed artifacts separate unless a later review explicitly accepts them as Stage 0 real evidence. Post-commit tracker bookkeeping updates do not count as separate Stage 0 tasks.
