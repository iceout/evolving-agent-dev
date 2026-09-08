# Session Report: External Worker Boundary Distillation

## Goal

Record privacy-preserving external support for existing CRL-X04 and CRL-X06
only. Mode: `record-only`; Conditional External-Evidence Distillation entered
after all seven ADR-0002 conditions were established.

## Source And Evidence Boundary

- Alias: `ext-crl-2026-09-a`; `C01`-`C03` follow source order.
- C01 is one output/observability workflow. C02 and C03 are conservatively
  treated as two correlated records in one durable-worker workflow evidence
  batch, since C03 is a related execution-boundary review-fix. Three entries
  therefore represent two batches for this record, not three independent
  repetitions. Review rounds, findings, fixes, tests, and mappings add no units.
- Source evidence is external, privacy-preserving narrative evidence, not
  internal dogfood or Stage 0 evidence. The user selected the source and
  authorized this record-only distillation; the external note remains read-only.
- Historical source skill/version: `loaded version unknown`. The note does
  not establish which skill, if any, was loaded. Dates, current repository
  state, and runtime linkage cannot establish historical loading.
- Repository evidence omits the source location and project identity, private
  symbols, identifiers, endpoints, credentials, payloads, and source excerpts.

## Mapping And Disposition

- C01 supports CRL-X04: CI exposed an incomplete test double, and the source
  reports aligning it with the actual acceptance-critical return contract.
  Run correlation and neighboring fail-open privacy findings remain facts
  supporting existing privacy/sensitive-output and failure/degraded guidance.
- C02 supports CRL-X06 B/C: the packet missed actual-first-mutation ordering
  and separate ownership, run, terminal-record, and deletion boundaries.
  Durable client-observable completion, crash/reconnect interleavings, and
  recovery semantics required explicit accounting.
- C03 supports CRL-X06 B/C: database ownership protection did not stop an
  already-running external call; expiry could release ownership while the
  call continued. A later progress event was not a pre-effect guard. Unknown
  execution outcomes cannot by themselves justify replacement or safe replay.
- No CRL-X06 A mapping: neither record establishes a preflight-detectable
  blocker that should have preceded the first mutation. Boundary discovery
  and a pre-effect marker do not independently establish that narrower defect.
- No CRL-X01 mapping: packet incompleteness is not packet-first timing failure.
  No CRL-X02, X03, or X05 mapping. No CRL-X07 update: missing CI dependencies
  and open rollout checks alone do not establish a material cross-context
  promise mismatch.
- No new lineage, inbox/casebook entry, evaluation/watchlist change, rule,
  policy, ADR, implementation, synthetic pilot, or outcome promotion. Concrete
  source mechanisms do not become generic requirements.
- Preserve CRL-X04 rule state `present`, outcome `inconclusive`, and no-new-rule
  decision; preserve CRL-X06 rule state `present`, outcome `awaiting evidence`,
  accepted implementation, hypotheses, and next-observation direction.

## Reported Verification And Limits

C01 reports related tests, CI cases, lint, diff checking, local health smoke,
and independent review. C02 reports lifecycle/frontend checks, lint, a
production build, and host-unit verification. C03 reports lifecycle/store/worker
checks, host-unit verification, lint, diff checking, and independent review.
Detection included review and CI for C01, plan/implementation review for C02,
and a user-provided finding, execution tracing, and review for C03. Review
detection is not prevention and is not wholly attributable to automated review.

Central distillation did not inspect or rerun the original packets, code,
commands, outputs, deployed effects, or external execution. Remaining gates
include production log behavior and near-limit rendering, actual delivery and
redelivery, datastore expiration/index behavior, ambiguous remote acknowledgement,
operator recovery, mixed-version rollout, and unknown datastore outcomes.
The narrative cannot establish final correctness, complete privacy coverage,
deployed exclusion, interoperability, universal atomicity, safe replay, or
regression prevention. It supports no known-version trigger/non-trigger,
`improved`, `repeated`, regression, or causal skill-effectiveness conclusion.

## Orchestration Observation

- Guidance actually read: repository-tracked `evolving-agent-process` and its
  orchestration reference at clean HEAD
  `64adb1d6ff3a8a07a6e467166491ba9d7b86e837`. The runtime skill resolves to that
  tracked source, and guidance files had no worktree changes. This identifies
  this orchestration's guidance separately from unknown external task versions.
- Capability check reused the applicable direct-subagent result in
  [the capability report](2026-08-18-external-evidence-distillation-capability-validation.md).
  The current interface retains explicit `fork_turns: none`. No changed surface
  or boundary requiring revalidation was identified.
- A read-only analysis subagent checked deduplication, batch boundaries,
  existing-lineage mapping, and gates 4-6; it returned an in-memory Distillation
  Card. The orchestrator froze it before editing and restricted changes to the
  two files below. The Card is not persisted.
- Initial fresh-context review returned `approval`. The reviewer received only
  the source, necessary repository sources, final diff/new report, and fixed
  rubric, using explicit no-turn forking without the Card or parent conclusions.
  The one documentary correction records this result; it changes no mapping,
  classification, privacy judgment, state, or scope. The corrected diff is
  subject to the single permitted re-review, reported in the final response.
- This boundary withholds parent conversation turns; it does not establish
  complete prompt isolation, filesystem non-visibility, model or evidence
  independence, review quality, or behavioral effectiveness. No retain, narrow,
  redesign, or effectiveness conclusion is made from this observation.

## Changes

- `docs/v0.3-scope.md`: supporting evidence within CRL-X04 and CRL-X06 only.
- This report: immutable source, routing, and verification record.

## Verification

- Initial worktree and staging area were clean; the privacy-safe alias was
  unused. The analysis found related prior patterns but no already-recorded
  instance of the transferred facts.
- Source SHA-256 before editing:
  `ac72fd9b9e4fcb0fcd83fd1f5bbeeb6776f0e93b02a416ca50847d6d1c7874f1`.
- Read the full tracked diff and new report. `git diff --check` passed;
  `git diff --no-index --check /dev/null` against this report produced no
  whitespace warnings and exited 1 solely because the new file differs.
- Structural checks passed: exactly the two allowed files changed, staging
  remained empty, all other current-state sections were byte-identical, and
  X04/X06 rule states, outcomes, decisions, hypotheses, and next directions
  were unchanged. All local Markdown links resolved.
- Source SHA-256 after editing matched the recorded baseline. Privacy-negative
  checks passed; manual review checked alias/case mappings, batch limits,
  source-specific mechanism boundaries, unknown-version claims, and reported
  versus centrally performed verification. Stale ambiguous source-attribution
  wording in X04 was replaced with explicit source references.
- No staging or commit is authorized; the result is to remain uncommitted.

## Good

Existing lineages accommodate the evidence without inflating correlated
findings or treating open deployment gates as a new compatibility defect.

## Friction

No notable process friction. Unknown versions and unavailable raw artifacts
remain evidence limits.

## Proposed Follow-up

Continue the existing known-version natural observation directions. No new
policy, casebook, ADR, evaluation, synthetic pilot, or skill change.
