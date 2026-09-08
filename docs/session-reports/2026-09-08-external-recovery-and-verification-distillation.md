# Session Report: External Recovery and Verification Distillation

## Goal

Record the selected external evidence under existing CRL-X04, CRL-X06, and
CRL-X07 only. Mode: `record-only`; Conditional External-Evidence Distillation
entered after all seven ADR-0002 conditions were established. The direct-subagent
path stopped at review with `needs decision`; the user then requested the
`codex review` CLI alternative. Its read-only review returned approval for the
documentary mapping. This completes the evidence review through the user-directed
alternative, not a newly validated fresh-context orchestration surface.

## Source And Evidence Boundary

- Privacy-safe alias: `ext-crl-2026-09-b`; C01-C11 follow source order, including
  entries whose dates are out of order. The alias denotes central intake, not
  a historical skill version.
- Eleven source records do not establish eleven independent repetitions.
  C01-C03 describe connected repair/recovery work; C04-C08 concern related
  performance, cache, and storage follow-ups; C10-C11 concern related report
  and provenance work. C09 explicitly follows earlier discovery failures.
  Preserve these correlations without assigning an exact independent-batch
  total or claiming independent projects/domains or a matched comparison.
  Findings, review rounds, fixes, tests, and multiple mappings add no units.
- The user explicitly selected the privacy-reviewed note for record-only
  distillation. It remains read-only. Source evidence is external, not internal
  dogfood or Stage 0 evidence.
- All source tasks have `loaded version unknown`; note naming and dates do
  not establish skill loading. Current HEAD and runtime linkage cannot supply
  historical versions.
- Repository evidence omits the external location/project identity, private
  identifiers, paths, schedules, commands, credentials, payloads, detailed
  fixture values, and lengthy source excerpts.

## Source Dispositions

| Case | Normalized observation | Existing route |
|---|---|---|
| C01 | Retained authority, request-scoped paths, and recovery before candidate registration were not composed. | CRL-X06 B/C: actual transaction boundaries and recovery-state consistency. |
| C02 | Pure sealed-input validation after ownership acquisition caused avoidable rollback. | CRL-X06 A: preflight-detectable blockers before mutation. |
| C03 | Physical rename changed authenticated path identity; a code change also affected checkpoint recovery identity. | CRL-X06 B/C: identity continuity and bounded recovery compatibility. |
| C04 | Separate test repositories shared global locks; malformed metrics could appear valid. | Report-only under existing verification, concurrency-context, and schema/output guidance. |
| C05 | Observation reuse covered only an opening edge instead of the actual locked invocation. | CRL-X06 B: observation lifetime and control revalidation across boundaries. |
| C06 | A later topology walk reused an earlier content hash without authenticating continuity. | CRL-X06 B: the reused observation must remain bound to its authenticated evidence. |
| C07 | Bounded query results still incurred large physical file-scan cost, disproving the performance premise. | Report-only under existing evidence-chain, dataflow, source-of-truth, and verification guidance. |
| C08 | A recovery fake omitted stricter storage schema/provenance and failed before the intended injection point. | CRL-X04: test-double boundary fidelity. |
| C09 | A test asserted an obsolete executable artifact path while the real scheduled entrypoint failed. | CRL-X07 B: target-environment/default-entrypoint fidelity. |
| C10 | A successful report concealed false provenance, configuration, domain-validation, and lock-authority mismatches. | Report-only under existing schema/output, config, authority, and behavior-test guidance. |
| C11 | Provenance omitted temporal/version constraints; fixed-input reads missed parent-path authentication. | Report-only under existing schema/API, temporal, source-of-truth, authority, and bad-path guidance. |

The existing recovery and scheduled-environment records contain related
patterns, not an already-recorded instance of these specific facts. C09 is
behaviorally related to `ext-bil-2026-08-a/C01` and C02 but adds the later
stale-artifact assertion failure. Its operational recurrence does not establish
a known-version skill recurrence or require resolving private project identity.
Existing historical reports remain unchanged.

## Reported Actions And Verification Limits

All actions and checks in this section are reported by the source, not centrally
reproduced. Central intake received narrative facts, not original packets,
code, command records, logs, test outputs, production state, or live effects.

- C01 reports recovery/path support and candidate restoration, with focused
  checks and a fast suite; rollback returned to ownerless readiness. Live
  publication remained externally gated. Fail-closed fresh-preview handling
  does not establish safe whole-operation replay.
- C02 reports mixed-precision parsing and shared candidate validation before
  ownership acquisition, retaining validation inside the transaction. Focused
  tests and a subsequent targeted live commit are reported; repeated inventory
  cost remains open. Retaining that recheck is a source action, not a new rule
  requiring duplicate validation in every workflow.
- C03 reports authenticating logical origin across rename and one explicitly
  reviewed recovery compatibility edge, then finalized production recovery.
  Inventory and unchanged-file reuse costs remain open. No generic exception
  for code-hash transitions or proof of safe full replay follows.
- C04 reports isolating test locks, changing read-lease lifetime, and marking
  invalid measurements. The previously failing test pair passed serially;
  collector/derived checks and lint passed. The full generation suite was not
  rerun concurrently, and production-like coverage attribution remained open.
- C05 reports invocation-local observation reuse, continued control checks,
  and scan-count/crash/re-entry tests. Natural production wall-clock improvement
  remained unverified; copying cost is a separate follow-up.
- C06 reports an in-place mutation reproduction, authenticated scan witnesses,
  drift rejection, and trust-lifetime closure with recovery tests. Production
  timing remained open; no historical successful transaction was replayed only
  to benchmark. Neither review detection nor local tests prove prevention.
- C07 preserves a failed hypothesis: real-data timing contradicted the bounded
  scan premise and the experiment was stopped. Replacement-path timing,
  equivalence/boundary/recovery checks, and a fast suite are reported. Natural
  end-to-end timing and evidence freshness at the downstream boundary remain
  open; bounded rows do not establish bounded physical work.
- C08 reports restoring the fake's storage/provenance contract with focused
  and full checks. It does not establish that permissive tests concealed a
  production recovery defect. Natural bootstrap/steady-state timing is open.
- C09 reports a reproducible minimal-environment failure before transaction
  creation. Shared executable resolution and revised regression coverage are
  required actions, not implemented fixes. Root repair and natural schedule
  verification remained pending in the source note; no partial transaction was
  reported. Local incident repetition is not a central `repeated` outcome.
- C10 reports contract/config/authority fixes, expanded bad-path tests, a
  guarded live report, and review. Feature-specific injected-failure,
  concurrency, and replacement-timing end-to-end checks remain absent; guards
  and shared primitives are not represented as those tests having run.
- C11 reports stricter temporal/version/path constraints, compatibility reads,
  tests, and a live research report. No live row exercised the exact provenance
  link; fixture-backed coverage does not establish live exact-link acceptance.

These records do not establish centrally verified correctness, performance
acceptance, complete compatibility, atomicity, replay safety, known-version
trigger/non-trigger behavior, improvement, regression, or causal effectiveness.

## Non-Routes And State Invariants

- No CRL-X01-X03 or X05 update. Composed-recovery gaps do not establish
  packet-first failure; report/provenance semantics do not automatically fit
  actionability or helper-contract lineages.
- C04/C07/C10/C11 remain report-only. No new performance, metric, filesystem,
  provenance, or bug-investigation lineage is created.
- C09 is not X04 merely because its tests assert implementation details;
  no fake call/return defect is established. C11's internal version rules do
  not establish X07 A's target-version evidence mismatch. Open live checks
  alone do not establish X07, and path authentication alone does not establish
  X06's applicable multi-step mutation defect.
- Preserve X04 rule `present` and outcome `inconclusive`; X06 rule `present`
  and outcome `awaiting evidence`; X07 rule `present`, status
  `implemented / awaiting evidence`, and outcome `awaiting evidence`.
  Existing hypotheses/confidence, decisions, implementations, and next
  observation directions remain unchanged, as do all other scope sections.
- No new policy, ADR, evaluation/watchlist, casebook/inbox, skill/reference,
  process version, synthetic pilot, runtime change, or target-project fix.
  Concrete caching, parsing, locking, and recovery mechanisms stay local facts.

## Orchestration Observation

- Guidance actually read: repository-tracked `evolving-agent-process` and its
  orchestration reference at clean HEAD
  `698729f1415495f33b549cd74a681ed4801d8193`; guidance files had no changes.
  This identifies the present orchestration separately from source-task loading.
- Capability check reused [the applicable direct-subagent validation](2026-08-18-external-evidence-distillation-capability-validation.md).
  The current interface retains `fork_turns: none`, and the admission check
  identified no context-semantics change. At review time, both creation of a
  new no-turn reviewer and attempted follow-up to a previous read-only reviewer
  failed with the platform thread-count limit. No direct-subagent reviewer
  executed for this source. Earlier capability validation did not guarantee
  remaining capacity, and those errors did not establish CLI unavailability.
- A read-only analysis subagent checked deduplication, correlation, mapping,
  and gates 4-6, then returned an in-memory Distillation Card. The orchestrator
  froze it before editing; it permits only the two files below and is not
  persisted as an artifact.
- Initial stop: `needs decision` under the capability-degradation rule;
  in-context self-review was not substituted. The user subsequently requested
  the CLI review alternative, so it was used without changing repository rules.
- CLI review: local Codex CLI 0.153.4, `codex review` with a custom stdin prompt
  and read-only reviewer sandbox, reviewing staged/unstaged/untracked changes.
  The prompt supplied the source, minimum repository context, final diff/new
  report, and fixed rubric; no parent transcript or Distillation Card was
  supplied, and no existing conversation was resumed. The first launch failed
  because the outer sandbox blocked CLI initialization writes. After host
  initialization was permitted, the reviewer ran with its read-only sandbox
  and exited 0 with approval for all eleven dispositions and the document scope.
- Boundary: this demonstrates an executable separate CLI review with bounded
  supplied inputs. It does not audit complete model input or establish the CLI
  as equivalent to the prior no-turn capability probe. Treat it as the
  user-directed alternative review, not fully verified prompt isolation, model
  or evidence independence, or orchestration effectiveness.
- The one documentary correction records the review and recovery from the tool
  limit without changing mapping, classification, privacy judgment, state, or
  allowed scope. The single CLI re-review result is reported in the final
  response; no substantive finding was raised by the initial review.
- No retain, narrow, redesign, or effectiveness conclusion is made about this
  orchestration mechanism.

## Changes

- `docs/v0.3-scope.md`: supporting evidence in X04, X06, and X07 only.
- This report: all eleven source dispositions and verification limits.

## Verification

- Initial worktree and staging were clean. Current/history searches found
  related patterns but no already-recorded instance of these source facts;
  the alias and report path were unused.
- Source SHA-256 before editing:
  `6b5231480b0175365b6977f78a097eac2caaa73a63860a8d4bcdce2974745bcd`.
- Read the complete final tracked diff and new report. `git diff --check`
  passed. The separate `git diff --no-index --check /dev/null` check for this
  report emitted no whitespace warnings; exit 1 reflects the new-file difference.
- Structural checks passed: exactly two allowed files, empty staging, C01-C11
  table order, local links, unchanged content outside X04/X06/X07, and unchanged
  rule states, outcomes, hypotheses, decisions, status, and next directions.
  Source SHA-256 after editing matched the recorded baseline.
- An initial ad hoc privacy-negative check failed because a tool-name substring
  also matched an ordinary word. A corrected word-boundary check passed;
  no content change was needed. Manual privacy review remains necessary because
  negative searches are not exhaustive; that review was completed, so this
  check failure does not block documentary completion.
- Manual checks preserved correlations, source-order IDs, explicit non-routes,
  failed hypotheses, serial-only checks, unimplemented source actions, and open
  live/timing gates. Source-attribution wording was updated to include this
  note without changing any historical loaded-version or outcome claim.
- Direct-subagent review failed to start on both attempted tool paths. The
  subsequent user-directed CLI review read the external note, complete diff,
  new report, and relevant guidance; it approved documentary mapping, scope,
  attribution, and verification limits. Its read-only shell initially could
  not create a heredoc temporary file; an inline Python check then confirmed
  unchanged out-of-scope sections and valid links. This was a reviewer check
  workaround, not a claim that the failed shell command passed.
- The CLI alternative resolves the missing content review. It does not resolve
  the stronger context-capability question or verify the source implementations.
- Leave the worktree uncommitted; no staging or commit occurs in this task.

## Good

The record preserves failed performance hypotheses, unimplemented actions,
serial-only checks, and live-verification gaps alongside reported successes.

## Friction

The direct collaboration tools accepted analysis but rejected both review-start
attempts at their thread-count limit. The initial response generalized that
failure too broadly; the user's CLI suggestion demonstrated another executable
review path. The temporary stop and later CLI approval remain distinct facts.
No canonical capability rule, automation, or effectiveness outcome was changed.
Correlated workflows and unavailable raw artifacts remain separate evidence limits.

## Proposed Follow-up

Preserve the existing X04/X06/X07 observation directions without new rules,
promotion, or synthetic pilots. The CLI result is not a canonical adoption or
capability-validation decision. Source-specific pending work remains reported
context, not an instruction to operate on the external project. Leave the
record uncommitted for the user's decision.
