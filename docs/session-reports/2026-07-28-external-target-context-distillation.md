# Session Report: External Target-Context Distillation

## Goal

Record two new external task cases, update `CRL-X06` supporting evidence and implementation bookkeeping, and establish or reuse a target-context verification lineage without changing canonical skill guidance.

## Status

- Dogfood: yes; only this evolving-agent-dev recording task used the repo-tracked `evolving-agent-process` skill.
- Source evidence: external privacy-preserving evidence.
- External tasks: not this project's dogfood.
- Stage 0: frozen counts unchanged.
- Skill change: none.
- Active experiment: none.
- Evaluation: not promoted.

## Source Boundary

- Privacy-safe source alias: `ext-crl-2026-07-d`.
- `C01 - exact-version compatibility source drift` records a version-context mismatch.
- `C02 - promised offline environment masked by deployment-loaded process` records an environment-context mismatch and a separate pre-mutation preflight observation.
- The cases occurred on different dates in two distinct tasks from the same external project. They are one transferred source with two distinct task cases, not one task batch and not cross-project or cross-domain repetition.
- Only generalized behavior crossed the privacy boundary. This report omits project identity, source-note location, profile contents, certificates, keys, credentials, host-specific paths, recipients, ports, runtime payloads, generated private package data, private configuration values, target addresses, URLs, and account information.

## Finding Routing

- `C01` routes to `CRL-X07` A. Version fidelity: a historical or minimum compatibility claim must use a source of truth that matches the claimed compatibility floor. Exact-version source inspection supports the existing Source-of-truth/proxy/fallback and schema/API/output contract guidance, while showing that current guidance is incomplete on target-version fidelity.
- The environment mismatch in `C02` routes to `CRL-X07` B. Environment fidelity: offline, portable, isolated, or deployment-independent behavior must be checked in the promised environment rather than a deployment-loaded process.
- The malformed-package preflight observation in `C02` routes to `CRL-X06` A. Preflight ordering as natural supporting evidence: portable package validation was not modeled as a pre-mutation blocker. The generalized boundary is complete trust and mutation preflight before runtime changes, not a target-specific symlink checklist.
- The isolated subprocess and clean/default CLI check in `C02` support existing Runnable Acceptance / Entrypoints and Verification Plan guidance. A subprocess is not made mandatory for all CLIs.
- `ext-crl-2026-07-c/C02` remains a related earlier protocol-compatibility observation only. It is not version-fidelity or environment-fidelity evidence and does not create independent-domain repetition. The earlier injected or session-specific runner observation supports environment fidelity and existing clean/default verification guidance, but comes from the same external project context.

## Attribution

- Source-task attribution for both new cases is `loaded version unknown`.
- The source note does not record the loaded skill source or version. Task dates do not establish a loaded repository commit, and current runtime linkage cannot establish a historical task version.
- `C02` therefore is not known-version effectiveness evidence, is not `known rule present but not executed`, and is not `CRL-X06` repeated-after-change evidence. It does not prove that the contract implemented in `47f774f` was loaded or skipped.

## Verification Limits

- For `C01`, exact-release source inspection and repository behavior tests were completed. Exact target-client configuration checking and live connectivity were not completed, so end-to-end compatibility is not established.
- For `C02`, isolated subprocess export, strict package rejection tests, a focused suite, and the repository suite were completed. Authenticated private transfer and target deployment apply were not completed.
- Strict rejection tests support the local package-boundary fix, but do not establish operational transfer/apply or closure of all portable-package risks.
- The evidence does not establish that the exact target core or client, live connectivity, authenticated private transfer, or target deployment apply was verified.
- It does not establish that the `CRL-X06` contract was known to trigger or fail, or that the current skill improved or regressed.

## Decision

- `CRL-X06`: add `C02` as unknown-version supporting evidence for A. Preflight ordering only; keep repository rule state `present`, outcome `awaiting evidence`, existing wording, and the known-version natural positive-trigger and nearby correct non-trigger evidence plan unchanged. Record the implementation as committed in `47f774f`.
- `CRL-X07`: create an `inactive discovery candidate` for Target-context verification fidelity with Version fidelity and Environment fidelity subpatterns. Repository rule state is `partial`; outcome is `awaiting evidence`.
- No generic skill or reference change, active learning bet, synthetic pilot, policy, ADR, casebook entry, formal evaluation, or promotion is created.

## Changes

- Updated `docs/v0.3-scope.md` with the `CRL-X06` evidence/bookkeeping update and the inactive `CRL-X07` lineage.
- Added `docs/session-reports/2026-07-28-external-target-context-distillation.md`.
- No skill, reference, inbox, policy, ADR, evaluation, casebook, Stage 0 tracker, process-version, runtime-install, external-note, or fixture change.

## Verification

- Task-start `git status --short` was empty, `HEAD` was `47f774f`, and `git merge-base --is-ancestor 47f774f HEAD` passed.
- Read every required source in full. Pre-edit searches across the inbox, central lineage, session reports, evaluation material, and canonical skill package found no use of `ext-crl-2026-07-d`, no `CRL-X07`, and no complete target-context verification lineage. They found partial source-of-truth, schema/API/output, runnable-entrypoint, verification-plan, compatibility, and clean/default-entrypoint coverage instead.
- Read the complete tracked diff and the full untracked report after editing. `git diff --check` passed.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-28-external-target-context-distillation.md` produced no whitespace warnings and exited `1` as expected because the files differ; a wrapper asserted that expected status.
- Changed-file checks list only `docs/v0.3-scope.md` and this report. `git diff --exit-code -- skills` passed, as did checks for no changes to casebook, policy, ADR, evaluation, Stage 0, and process artifacts.
- Alias and lineage searches show `ext-crl-2026-07-d` only in the two changed files. Heading-count assertions found exactly one central `CRL-X06` and one central `CRL-X07` heading.
- `CRL-X06` checks confirmed repository rule state `present`, implementation commit `47f774f`, source attribution `loaded version unknown`, the new `C02` evidence limited to unknown-version preflight support, unchanged known-version next evidence, and outcome `awaiting evidence`. The historical decision and implementation reports have no diff.
- `CRL-X07` checks confirmed repository rule state `partial`, both cases attributed as `loaded version unknown`, decision `no generic skill change for now`, status `inactive discovery candidate`, no active learning bet or synthetic pilot, no promotion, no independent-project/domain repetition claim, and outcome `awaiting evidence`.
- Semantic searches covered target context, version fidelity, environment fidelity, exact-version and historical schema, offline and deployment-independent behavior, isolated subprocess checks, current documentation, and injected or session-specific execution. Manual review confirmed the earlier compatibility and clean-entrypoint observations are supporting evidence rather than duplicate central lineages.
- Privacy-value negative searches across both changed files found no external project name or source-note path, host path, URL or address, account-like identifier, IP address, or credential/private-value assignment. Manual review confirmed no profile contents, certificates, keys, credentials, recipients, ports, payloads, generated private package data, or private configuration values were recorded.
- The current-state stale-language check found no `implementation commit pending` in `docs/v0.3-scope.md`. Historical `commit pending` wording remains intact in the unchanged implementation report.
- One combined stale/historical verification command exited `1`: its final exact search, `rg -n 'implementation commit pending' docs/session-reports/2026-07-19-crl-x06-packet-refinement-implementation.md`, found no match because the historical report says `commit pending`, not the longer phrase. The preceding current-state negative check and historical no-diff check had passed. The search was safely rerun as `rg -n 'commit pending|Implementation: completed in working tree'` against that report and returned its three expected historical lines. Remaining risk from the failed exact-match command: none; the replacement plus no-diff check covers the intended assertion.

## Good

The current-state lineage can preserve the distinction between evidence that supports existing guidance and evidence that exposes a narrower target-context gap without prematurely changing the skill.

## Friction

One verification search assumed a longer stale phrase than the historical report actually used. The exact-match failure was isolated and replaced with a broader historical wording check plus a no-diff assertion. The loaded-version and operational-verification gaps remain evidence limitations rather than process failures in this recording task.

## Proposed Follow-up

1. Review and commit this evidence separately after inspection.
2. Wait for independent-project or independent-domain natural `CRL-X07` evidence before reconsidering a narrow generic packet refinement.
3. Continue waiting for known-version natural `CRL-X06` positive-trigger and nearby correct non-trigger evidence.
4. Make no skill change and start no synthetic experiment now.
