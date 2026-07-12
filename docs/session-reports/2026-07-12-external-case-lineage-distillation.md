# Session Report: External Case Lineage Distillation

## Goal

Distill one privacy-reviewed external `coding-review-loop` case batch into a lightweight, reviewable lineage from source case to normalized pattern, root-cause hypothesis, change or no-change decision, version attribution, later evidence, and current outcome. Reuse existing v0.3 artifacts, keep target-project capture lightweight, and avoid a new ledger, tracker, process document, policy, ADR, formal evaluation, or automation.

## Status

- Dogfood: yes; this evolving-agent-dev edit used the repo-tracked `evolving-agent-process` skill.
- Source evidence: external privacy-preserving evidence, not an internal dogfood task.
- Stage 0 evidence status: not accepted Stage 0 evidence; frozen counts remain unchanged.
- v0.3 status: manual lineage/watchlist and narrow skill refinement only; no `docs/process-v0.3.md`.

## Source

- Central source ID: `ext-crl-2026-07-a`.
- `C01`: small-helper readability and test-double call-shape observations.
- `C02`: compact decision-contract actionability observation.
- `C03`: private row-contract exposure through a public helper observation.
- `C04`: user-impacting side-effect task started before a durable review packet.
- `C05`: shared-symbol removal missed runnable entrypoints and used mocks above the changed boundary.
- The supplied external note was not modified or copied into the repository. Private paths, project identity, notification recipients, user/account/customer identifiers, payloads, and sensitive configuration were omitted.

## Attribution

- `C01`: the base Focused Reuse Scan predates the case, while semantic-responsibility and test-double refinements landed on the same date. Exact task ordering and loaded skill source are unknown; outcome is inconclusive.
- `C02`: Semantic Liveness predates the case date in repository history, but the loaded skill source is unknown. Current guidance still lacked an explicit positive-plus-blocker behavior-test requirement, so a narrow clarification was accepted without claiming an execution failure.
- `C03`: current public-interface, schema/API contract, reuse rationale, and behavior-test guidance already cover the reusable concern. No new rule was accepted; version attribution remains inconclusive.
- `C04`: general packet-first and runnable-acceptance rules predate the case in repository history, but the loaded skill source is unknown. A current operational gap remained in mapping user-impacting side effects to high-risk and the first-edit timing, so a narrow clarification was accepted.
- `C05`: test-double behavior is already covered but cannot be attributed to a known loaded version. The repository skill did lack a removal-specific repository-wide impact and entrypoint-discovery rule, so that general gap was accepted for change.

No case has source-task attribution `known rule present but not executed`, because none records a loaded skill source or version that is known to contain the relevant rule.

## Changes

- Extended `docs/skill-design/local-evidence-ledger.md` with central lineage responsibilities, attribution rules, outcome definitions, and semantic/identity deduplication.
- Kept canonical repository rule state separate from source-task attribution so rule coverage and version/timeline evidence can vary independently.
- Added a current-state `External Evidence Lineage` section to `docs/v0.3-scope.md` for five normalized patterns, including explicit no-change decisions and `awaiting evidence` or `inconclusive` outcomes.
- Clarified in `skills/coding-review-loop/SKILL.md` that user-impacting live writes, notifications, and side-effecting scheduled work are high-risk and need a reviewable packet before the first implementation edit.
- Added repository-wide symbol/reference and repository-native runnable-entrypoint discovery for shared-symbol removal or rename without hard-coding a scripts directory.
- Added a positive-path plus representative blocker/negative-path expectation for decision and action fields in the existing packet section.
- Added one optional case-note field for an already-visible skill source/version; `unknown` is allowed and commit-history investigation is explicitly out of scope for target-project users.
- Strengthened privacy wording so notification recipients and user/account/customer identifiers are excluded.
- Did not add the five cases as independent inbox items; already-covered observations link to existing patterns instead.

## Responsibility Boundary

- Target-project user: local facts, reviewer/test findings, packet or verification gaps, fix direction, and privacy boundary; optionally an already-visible skill source/version.
- Evolving-agent-dev distiller: privacy-safe IDs, cross-case normalization, root-cause hypothesis/confidence, deduplication, version attribution, change/no-change decision, and promotion decisions.
- Skill/process maintainer: changed artifact plus date/version/commit when known.
- Future distiller: comparable-evidence link and `improved` / `repeated` / `inconclusive` outcome, with rationale.

## Role Separation

### Plan Decision

Reuse the existing local-evidence design note, v0.3 watchlist, and session reports. Make only generalized skill changes supported by a current rule gap; keep covered or version-ambiguous observations as no-change/inconclusive.

### Test Responsibility

Validate artifact links, skill/reference structure, attribution vocabulary, deduplication, privacy exclusions, Stage 0 boundaries, and the absence of new policy/evaluation/process artifacts.

### Implementation Responsibility

Modify only the evidence convention, current watchlist, coding-review skill/references, and this report. Do not modify the external note, Stage 0 tracker, inbox counts, policies, ADRs, evaluations, or runtime automation.

### Review Check

Confirm the target-project template does not assign central analysis to external users, accepted changes are general rather than feature-specific, no post-change improvement is claimed, and every current outcome follows the stated version-evidence rules.

## Verification

- Reviewed the complete tracked diff for the five modified files and manually read this new report, which is untracked and therefore absent from normal `git diff` output.
- `git diff --check` passed with no whitespace errors.
- `git diff --no-index --check /dev/null docs/session-reports/2026-07-12-external-case-lineage-distillation.md` produced no whitespace warnings and exited `1` as expected because the files differ.
- The skill-creator `quick_validate.py` was attempted and failed before validating content because the local Python environment lacks `yaml` (`ModuleNotFoundError: No module named 'yaml'`).
- A shell fallback validation passed: exact four-line frontmatter shape, only `name` and `description` fields, `coding-review-loop` name, body under 500 lines, both referenced files present, and both references reachable from `SKILL.md`.
- Explicit file-existence checks passed for every new repository source link and artifact path.
- Source-ID and lineage-heading checks confirmed one current-state record for each of `CRL-X01` through `CRL-X05`; semantically covered cases are supporting evidence inside existing pattern records rather than new inbox items.
- Attribution-model assertions confirmed all five records separately contain one repository rule state and one source-task attribution, with no legacy combined baseline-attribution field.
- Negative privacy/stale-language search found no external project name, private note path, feature-specific case title, ambiguous configured-recipient wording, or hard-coded scripts glob in the changed scope.
- Target-user boundary assertions confirmed the optional source/version value may be omitted or `unknown`, requires no commit-history investigation, and leaves cross-case attribution, root-cause classification, process decisions, promotion, and later tracking with evolving-agent-dev.
- Packet-rule adjacency check confirmed the high-risk review requirement remains immediately before the side-effect classification and first-edit timing clarification.
- Stage 0 and artifact-boundary assertions passed: no Stage 0 tracker, v0.2 process, inbox, policy, ADR, evaluation, or `docs/process-v0.3.md` changed or was created.
- `python3 scripts/install-skill.py --list` confirmed the runtime `coding-review-loop` install is a symlink to the repo-tracked source. This verifies current runtime linkage only; it is not used to infer historical case versions.
- No automated behavior suite exists for these documentation-only skill changes. The remaining risk is behavioral effectiveness, which is intentionally recorded as `awaiting evidence` or `inconclusive`, not complete regression closure.

## Good

- Existing artifacts were sufficient; no new evidence system was needed.
- The case batch could support both changes and explicit no-change decisions without treating case count as effectiveness proof.
- Separating repository history from loaded skill version prevented false repeated-after-change claims.

## Friction

- What happened: External notes record task dates and `Skill used`, but not the loaded skill source/version.
- Why it felt wrong: Repository commit history alone could make a same-day or later-dated case look like a confirmed regression.
- Impact: Rule absence, execution failure, and repeated-after-change could be conflated.
- Category: `process` / `context`.
- Root cause guess: The target-project capture format lacked a zero-effort way to preserve version information when already visible, while central distillation lacked explicit attribution-state rules.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; current patterns stay in the v0.3 lineage/watchlist.
- ADR needed? no; the change reuses existing routing and has no new durable architecture decision.
- Evaluation candidate? no formal promotion. Existing watchlist candidates still need privacy-safe fixtures, pass/fail rubrics, and judge methods.
- Later evidence: all accepted changes remain `awaiting evidence`; covered patterns with unknown source versions remain `inconclusive`.
