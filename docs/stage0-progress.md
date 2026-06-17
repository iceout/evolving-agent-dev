# Stage 0 Progress Tracker

Last updated: 2026-06-17

This is a manually maintained tracker for Stage 0 progress. It distinguishes accepted real dogfood evidence from bootstrap work, smoke tests, and seed artifacts. It is not an automation or metrics source.

## Counting Rule

Count a task only when it is an installed-skill dogfood edit task, has a session report, has been reviewed/accepted, and is traceable to a commit. Do not count bootstrap setup, smoke-test harness results, seed casebook entries, or seed evaluation cases as real Stage 0 evidence.

Known caveat: sandboxed execution remains unverified because this environment uses `--dangerously-bypass-approvals-and-sandbox`.

## Accepted Real Dogfood Tasks

| # | Commit | Task | Evidence | Notes |
|---|---|---|---|---|
| 1 | `821d50c` | Clarify skill install flow | `docs/session-reports/2026-06-15-skill-install-flow-clarification.md` | Accepted real dogfood task; sandbox caveat applies. |
| 2 | `c946d5f` | Add evaluation case metadata | `docs/session-reports/2026-06-15-evaluation-case-metadata.md` | Accepted real dogfood task; evaluation cases remain seed candidates. |
| 3 | `52afa4a` | Add Stage 0 progress tracker | `docs/session-reports/2026-06-15-stage0-progress-tracker.md` | Accepted real dogfood task; sandbox caveat applies. |
| 4 | `9f88c67` | Add sandbox execution caveat case | `docs/session-reports/2026-06-15-sandboxed-execution-casebook.md` | Accepted real dogfood task; added `docs/casebook/0003-sandboxed-execution-unverified.md`. |
| 5 | `c7bf810` | Add evaluation missing evidence notes | `docs/session-reports/2026-06-15-evaluation-missing-evidence-notes.md` | Accepted real dogfood task; E001-E004 remain seed candidates. |
| 6 | `b225ca9` | Add evaluation verification hygiene | `docs/session-reports/2026-06-15-evaluation-verification-hygiene.md` | Accepted real dogfood task; no new real or partial evidence for E001/E002. |
| 7 | `717ef1c` | Add response language behavior | `docs/session-reports/2026-06-15-response-language-rule.md` | Accepted real dogfood task; added E005 as a real-evidence evaluation candidate for final response language. |
| 8 | `b4a73e1` | Normalize Stage 0 friction accounting | `docs/session-reports/2026-06-15-stage0-friction-accounting.md` | Accepted real dogfood task; added E006 as a real-evidence evaluation candidate for Stage readiness metric-unit hygiene. |
| 9 | `b07ef63` | Add Stage 0 exit blocker summary | `docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md` | Accepted real dogfood task; clarified Stage 0 cannot exit while repeated problem categories remain 1 / 3. |
| 10 | `f1292c2` | Add cross-artifact consistency evaluation candidate | `docs/session-reports/2026-06-16-cross-artifact-consistency-evaluation-review.md` | Accepted real dogfood task; added E007 as a real-evidence evaluation candidate for cross-artifact consistency. |

## Calibration / Not Counted

- Smoke Test C (`96039a9`, `docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md`) is a calibration candidate, not currently counted as an accepted real dogfood task.
- `docs/session-reports/2026-06-15-codex-skill-smoke-tests.md` is smoke-test harness evidence, not an additional real task.
- Bootstrap, installation, canonical-skill-draft, and skill-design-hardening reports are setup evidence, not real dogfood tasks.
- Public hygiene pass (`4d35e24`, `docs/session-reports/2026-06-16-public-hygiene-pass.md`) is publication bookkeeping, not a real dogfood task.
- External pilots are cross-artifact consistency evidence, but they are not accepted internal Stage 0 dogfood tasks.
- Seed casebook entries and E001-E004 in `docs/evaluations/behavior-cases.md` remain seed artifacts unless later linked to accepted real sessions or friction entries.

## Friction Accounting

Friction item count, unique themes/categories, and repeated problem categories are tracked separately. Count only explicit friction from accepted dogfood session reports or accepted tracker evidence; do not count bootstrap, smoke, setup, seed artifacts, or pending dogfood tasks.

Current tracker totals: 12 accepted dogfood friction items; 6 evidence-backed themes/categories; 3 repeated problem categories.

Cross-artifact consistency is counted as a repeated problem category based on privacy-preserving external pilots plus internal stale-verification evidence. It is not counted as accepted internal dogfood friction items.

Planning impact analysis is counted as a repeated problem category based on three privacy-preserving external planning reviews captured in `docs/casebook/0005-planning-impact-analysis-gaps.md` and `docs/casebook/inbox.md`. Those external observations are not counted as accepted internal dogfood tasks or accepted dogfood friction items.

### Friction Items Captured

| # | Source | Item | Category | Count basis |
|---|---|---|---|---|
| 1 | `docs/casebook/inbox.md` / accepted task `821d50c` | Skill install flow unclear | `tooling` | Inbox friction tied to accepted dogfood task. |
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

| Theme/category | Evidence basis | Repeated? | Notes |
|---|---:|---|---|
| `tooling` / skill install flow unclear | 1 accepted dogfood friction item | no | Installation path/copy-vs-symlink verification was unclear. |
| `tooling` / sandbox remains unverified | 9 accepted dogfood friction items | yes | Repeated across accepted dogfood reports; captured in `docs/casebook/0003-sandboxed-execution-unverified.md`. |
| `requirements` / response language expectation implicit | 1 accepted dogfood friction item | no | Produced accepted real-evidence candidate E005. |
| `process` / stage readiness metric units conflated | 1 accepted dogfood friction item | no | Produced accepted real-evidence candidate E006. |
| `process` / cross-artifact consistency drift | External/internal evidence only; not accepted dogfood friction items | yes | Evidence basis is privacy-preserving external pilots plus internal stale-verification evidence; produced accepted real-evidence candidate E007. |
| `process` / planning impact analysis | Privacy-preserving external evidence only; not accepted dogfood friction items | yes | Evidence basis is three external planning reviews captured in `docs/casebook/0005-planning-impact-analysis-gaps.md`; external observations are not accepted internal dogfood tasks. |

### Repeated Problem Categories

| Category/theme | Evidence | Status |
|---|---|---|
| `tooling` / sandbox remains unverified | 9 accepted dogfood friction items, plus casebook entry `docs/casebook/0003-sandboxed-execution-unverified.md` | Repeated problem category visible. |
| `process` / cross-artifact consistency drift | Privacy-preserving external pilots plus internal stale-verification evidence in `docs/casebook/0004-cross-artifact-consistency-drift.md`; external pilots are not accepted internal dogfood tasks. | Repeated problem category visible. |
| `process` / planning impact analysis | Three privacy-preserving external planning reviews captured in `docs/casebook/0005-planning-impact-analysis-gaps.md` and `docs/casebook/inbox.md`; external observations are not accepted internal dogfood tasks. | Repeated problem category visible. |

## Stage 0 Exit Review Status

Stage 0 is not declared complete in this tracker update. Real dogfood tasks, friction items, real-evidence evaluation candidates, and repeated problem categories now appear to meet the numeric exit criteria, but a separate Stage 0 exit review is required before any exit decision. Keep these units separate: 12 accepted dogfood friction items, 6 evidence-backed themes/categories, and 3 repeated problem categories are different measures.

## Stage 0 Exit Criteria Progress

| Criterion | Current progress | Status |
|---|---:|---|
| 3-5 real tasks run through the process | 10 accepted / target 3-5 | Over target; numeric criteria appear met, but separate Stage 0 exit review is required |
| At least 10 friction items captured | 12 accepted friction items / target 10; see Friction Accounting | Met |
| At least 2 evaluation candidates identified from real evidence | 3 accepted from real evidence / target 2: E005 final response language; E006 Stage readiness metric-unit hygiene; E007 cross-artifact consistency. E001-E004 remain seed candidates | Met |
| Top 3 repeated problem categories visible | 3 repeated categories visible / target 3: `tooling` / sandbox remains unverified; `process` / cross-artifact consistency drift; `process` / planning impact analysis. Evidence-backed themes/categories visible: 6 | Met; separate Stage 0 exit review required |

## Next Update Rule

When a dogfood task is accepted, add its commit, task title, and session report path here. Keep calibration and seed artifacts separate unless a later review explicitly accepts them as Stage 0 real evidence. Post-commit tracker bookkeeping updates do not count as separate Stage 0 tasks.
