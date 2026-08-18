# ADR-0002: External-Evidence Distillation Orchestration

## Status

Accepted; reference implementation is recorded separately.

## Context

Privacy-reviewed external case notes can be distilled into an existing central
lineage without changing a rule or making an outcome claim. The current manual
workflow can require the user to move a long analysis prompt from an analysis
agent to a development agent and then request another review. Much of that
prompt repeats stable repository constraints, so the transfer cost is high even
when the case is narrow, record-only, and already has a clear route.

This decision addresses that user coordination cost. It does not automate
evidence promotion, source discovery, central routing, or commits. The user
continues to select and privacy-review the source note, start the task, accept
or reject the resulting decision, and authorize any later commit.

The review produced by the future mechanism is role-separated review intended
to reduce anchoring. It is not a completely independent evidence source and is
not proof of behavioral effectiveness. The ability of a platform to isolate
subagent context is also a capability prerequisite, not an outcome established
by this decision.

Three approaches were considered:

### A. Continue Manual Multi-Round Forwarding

The user gives a source note to an analysis agent, forwards its long prompt to
a development agent, and later requests an independent review manually.

Reject as the default path. It preserves high user transfer cost and repeatedly
moves fixed process constraints. It remains an escape hatch when orchestration
is unavailable, provided nobody describes the resulting review as fresh-context
orchestrated review.

### B. Conditional Orchestrated Distillation

Accept, pending a separate implementation. It is the smallest approach that
can remove repetitive prompt forwarding while preserving user authorization,
privacy, existing-lineage routing, and explicit review boundaries.

### C. Fully Automated Intake, Routing, And Commit

Reject. The system must not scan, upload, or batch-process
`.agent/coding-review-loop-cases.md`; bypass user source selection or privacy
review; create lineage automatically; modify canonical guidance; promote an
outcome; or commit automatically.

## Decision

Adopt option B for bounded editing only when every positive trigger below is
established:

1. The user explicitly requests external evidence distillation.
2. The user explicitly provides a source note that is treated as read-only and
   privacy-reviewed.
3. The task mode is `record-only`.
4. Analysis confirms that an existing central lineage can be reused.
5. The task needs no new rule, lineage, policy, ADR, evaluation, synthetic
   pilot, or outcome promotion.
6. An analysis card clearly limits the files and content that may change.
7. The platform supports a review subagent with isolated, fresh context.

Admission is phased without weakening any trigger. Pre-analysis admission
requires conditions 1, 2, 3, and 7 plus no obvious scope contradiction; it
authorizes only reading the orchestration reference and starting read-only
analysis. Analysis determines conditions 4 and 5 and produces condition 6, the
frozen in-memory Distillation Card. Before any bounded record-only edit, all
seven conditions must be established. If analysis cannot establish conditions
4-6, return `needs decision` or an objection without editing.

The future role protocol is:

```text
orchestrator
  -> baseline / source reading
  -> analysis subagent (read-only, no edits)
  -> frozen in-memory Distillation Card
  -> bounded record-only implementation
  -> fresh-context review subagent (read-only, no edits)
  -> at most one scoped correction + re-review
  -> leave uncommitted worktree for user decision
```

The analysis subagent must return an in-memory Distillation Card. The card is a
task-local handoff, not a persisted ledger or new repository artifact. It must
include at least:

- task mode;
- source and evidence-batch boundary;
- candidate lineage and privacy-safe alias/case ID;
- evidence-backed mapping;
- explicit non-routes;
- state invariants;
- allowed and forbidden changes;
- evidence limits and prohibited attribution or effectiveness claims; and
- required verification.

The orchestrator freezes the card before editing and may implement only the
bounded record-only changes it authorizes. It does not delegate user authority:
the user still supplies the source, starts the task, decides whether to accept
the result, and authorizes any commit.

The review subagent must be role-isolated from the analysis subagent. It does
not receive the Distillation Card or the parent's conclusion-oriented
reasoning. Its inputs are limited to the source note, necessary repository
sources, final diff and new files, and a fixed review rubric. It is read-only,
must not edit files or run `git add` or `git commit`, and returns only findings,
approval, or `blocked`/`inconclusive`.

The review rubric checks factual mapping, lineage routing, privacy, attribution
when the loaded version is unknown, state drift, the changed-file allowlist,
stale language, overclaiming, and verification semantics. This review provides
role separation and lower anchoring risk; it does not create evidence
independence or establish that the mechanism improves behavior.

The orchestrator may automatically correct only a mechanical or documentary
finding that does not change the route or decision. It may perform at most one
correction and one re-review. Any remaining substantive finding is returned to
the user rather than iterated away.

The workflow must stop and return `needs decision` or an objection when:

- a new lineage is needed or the existing-lineage route is unclear;
- a skill/reference, policy, ADR, evaluation, casebook, or process version
  would need to change;
- a synthetic pilot would begin;
- unknown-version evidence would be used to infer effectiveness,
  `improved`, `repeated`, or regression;
- the reviewer finds that evidence mapping or the privacy boundary requires a
  substantive judgment; or
- the platform cannot provide the required fresh-context review.

The last condition has explicit degradation semantics. Without isolated
fresh-context review capability, the orchestrated path is unavailable. The
agent reports the missing capability and returns `needs decision`; it may offer
the existing manual review path, but must not claim that independent or
fresh-context review occurred.

The following are non-goals:

- Do not create a second central tracker, ledger, queue, dashboard, or case
  index.
- Do not require a case note for every `coding-review-loop` invocation or
  change the target-project case-capture trigger.
- Do not treat usage count as quality evidence.
- Do not change CRL-X01-X07, Stage 0, the evaluation watchlist, or any existing
  evidence outcome.
- Do not treat this decision as evidence that subagent capability,
  fresh-context isolation, review quality, or behavioral improvement has been
  verified.
- Do not require multiple agents for ordinary discussion, micro tasks, or
  clear-route tasks that require no record.
- Do not commit automatically; commit authorization remains with the user.

The reference implementation is limited to a narrow extension under
`skills/evolving-agent-process/` and one short orchestration reference. It
defines stable invariants, the Distillation Card shape, subagent-availability
detection and degradation semantics, analysis/review role separation,
objection conditions, the one-correction cap, and a fixed final-report shape.

It does not preselect a particular agent API, CLI, JSONL format, runtime hook,
network service, background worker, or automatic commit mechanism. It does not
move these details into `AGENTS.md`, rewrite `docs/process-v0.2.md`, or create a
process-v0.3 document. Any later change beyond this boundary requires separate
authorization and must follow the applicable skill-package workflow.

The canonical reference guidance and its verification boundary are recorded in
the [implementation report](../session-reports/2026-08-18-external-evidence-distillation-orchestration-implementation.md).
This establishes that the guidance exists, not behavioral effectiveness,
fresh-context review quality, platform capability for a real workflow, or
reduced user effort. It changes no external evidence outcome.

## Consequences

Benefits:

- reduces repetitive user prompt forwarding for a narrow, repeatable case;
- preserves user control over source selection, privacy review, acceptance, and
  commits;
- separates evidence analysis from final review without overstating review
  independence; and
- keeps existing central lineage and artifact routing as the source of truth.

Costs and risks:

- requires a platform capability that may be absent or weaker than expected;
- adds orchestration overhead that is inappropriate outside the seven positive
  triggers;
- can still anchor the reviewer if context isolation is implemented poorly;
- can encode a wrong route in the card, so the review must inspect source facts
  independently; and
- cannot establish effectiveness from reference guidance alone; that requires
  applicable natural, user-selected record-only observations that record the
  orchestration guidance/source version actually loaded.

## Escape Hatch

Use the current manual handoff and review path when the platform cannot provide
isolated fresh context or when the user prefers manual control. If route,
privacy, attribution, or promotion requires substantive judgment, stop the
record-only task and open the appropriate separate decision task. Do not widen
this mechanism to make the case fit.

## Related Cases / Evidence

- [Local Evidence Ledger](../skill-design/local-evidence-ledger.md) defines
  user-selected, privacy-reviewed transfer and central-lineage ownership.
- [External Cross-Worker Guard Distillation](../session-reports/2026-08-17-external-cross-worker-guard-distillation.md)
  illustrates a narrow existing-lineage, record-only distillation.
- [External Conditional State Contract Distillation](../session-reports/2026-08-17-external-conditional-state-contract-distillation.md)
  illustrates the same route with explicit non-routes and evidence limits.
- [ADR-0001](ADR-0001-role-separation.md) records the repository's broader
  role-separation rationale and lightweight escape hatch.

These case materials establish workflow constraints and examples. They do not
prove platform capability, end-to-end executability, or effectiveness. The
linked implementation report separately establishes only that the canonical
reference guidance exists.

## Evaluation or Observation Plan

The reference guidance is implemented, but platform capability, end-to-end
executability, and behavioral effectiveness remain unestablished. Before any
natural orchestration observation begins, the selected platform must directly
and honestly establish condition 7: it can provide the intended fresh-context
review boundary. An absent or inconclusive capability result requires the
documented `needs decision` degradation and cannot admit an observation.

Only on a platform that establishes condition 7 should natural, user-selected
record-only tasks with a real opportunity to trigger or stop the mechanism be
observed. Record the implemented orchestration guidance/source version actually
loaded for each observation. The external source task's historical
`coding-review-loop` version may remain unknown; that limits causal claims
about the source task, not attribution of whether the versioned orchestration
correctly triggered, stopped, or reduced forwarding. If the orchestration
version itself is unknown, the observation remains version-inconclusive and
cannot support a retain, narrow, or redesign conclusion.

Retain the mechanism if version-attributed observations show that it
consistently applies all seven positive triggers, preserves the frozen card
boundary, stops on substantive judgment, limits correction to one round,
reports capability degradation truthfully, leaves work uncommitted, and
materially reduces user forwarding without adding disproportionate overhead.

Narrow it if the route is sound but triggers are noisy, cards are too large,
review context is broader than necessary, or lightweight tasks incur excessive
cost. Redesign it if privacy or user authority is bypassed, context isolation
cannot be relied upon, review receives conclusion-oriented analysis, stop
conditions are crossed, corrections change decisions, or automatic promotion
or commit behavior appears. Ordinary usage counts are not an observation of
quality. An external source task with an unknown historical skill version
cannot establish historical skill causality, while an orchestration observation
with an unrecorded implementation version cannot establish mechanism-version
behavior; neither supports outcome promotion.
