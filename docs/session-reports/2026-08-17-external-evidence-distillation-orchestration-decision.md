# Session Report: External-Evidence Distillation Orchestration Decision

## Goal

Freeze a narrow, optional process/agent-behavior decision that can reduce user
prompt-forwarding work for future existing-lineage, record-only external case
distillation, without implementing or exercising the mechanism.

This is not an external evidence distillation. It does not inspect or record a
new external source, create or update central lineage, or change an evidence
outcome.

## Status And Method

- Task type: substantive decision-only edit task.
- Skills used: repo-tracked `evolving-agent-process` and `idea-framing-loop`.
- Idea mode: process/agent behavior.
- Decision status: `Accepted pending separate implementation`.
- Implementation status: not started.
- Effectiveness observation status: not started.
- Subagent orchestration: not invoked for this task.
- Dogfood and Stage 0 evidence: this decision task does not establish
  orchestration dogfood, a Stage 0 task, external evidence, or behavioral
  effectiveness.

The user had already supplied the goal, evidence examples, current workaround,
constraints, non-goals, smallest useful boundary, risks, success conditions,
and three candidate approaches. Under the `idea-framing-loop` escape hatch, no
repetitive clarification or separate idea brief was needed; this ADR is the
requested durable decision carrier.

## Options Reviewed

### A. Manual Multi-Round Forwarding

Rejected as the default because it preserves repeated long-prompt transfer and
asks the user to coordinate stable process constraints. It remains an honest
fallback when fresh-context orchestration is unavailable.

### B. Conditional Orchestrated Distillation

Accepted pending separate implementation. It removes user forwarding only for
an explicitly requested, privacy-reviewed, read-only-source, record-only case
whose existing-lineage route and file boundary are clear and that needs no new
rule, lineage, policy, ADR, evaluation, pilot, or outcome promotion. Isolated
fresh-context review capability is mandatory.

### C. Fully Automated Intake, Routing, And Commit

Rejected because it would bypass source selection and privacy review, risk
automatic central classification or outcome promotion, create automation
outside current scope, and remove explicit commit authority from the user.

## Frozen Decision Boundary

The accepted sequence is baseline/source reading, read-only analysis subagent,
an in-memory frozen Distillation Card, bounded record-only editing, and a
role-isolated read-only review subagent. The reviewer receives source and
repository facts, the final diff/new files, and a fixed rubric, but not the card
or the parent's conclusion-oriented reasoning. The orchestrator may make at
most one mechanical or documentary correction that does not alter route or
decision, followed by one re-review.

All seven positive triggers in the ADR are required. Unclear or new lineage;
changes to skill/reference, policy, ADR, evaluation, casebook, or process
version; a synthetic pilot; promotion claims from unknown-version evidence;
substantive mapping or privacy judgment; or absent fresh-context capability
must stop the workflow with `needs decision` or an objection.

When isolated fresh-context review is unavailable, the workflow degrades by
declaring the orchestration unavailable and returning control to the user. A
manual review path may be offered, but it cannot be labeled fresh-context or
independent orchestration.

The external source task's historical `coding-review-loop` version and a later
orchestration observation's loaded implementation version are separate facts.
The former may remain unknown, limiting causal claims about the source task;
the latter must be recorded before attributing trigger, stop, or forwarding
behavior to an orchestration implementation.

The decision distinguishes five concerns:

- role-separated review reduces anchoring but is not an independent evidence
  source;
- evidence independence is not created by changing agent roles;
- behavioral effectiveness requires later applicable observation;
- platform capability and isolation require implementation-time verification;
  and
- user authorization governs source provision, task start, acceptance, and
  commit.

## Changes

- Added [ADR-0002](../decisions/ADR-0002-external-evidence-distillation-orchestration.md)
  with the A/B/C decision, positive triggers, role protocol, card shape, review
  rubric, stop and degradation behavior, non-goals, future implementation
  boundary, consequences, escape hatch, related evidence, and observation plan.
- Added this minimal decision report.
- Changed no skill/reference, existing ADR/report, central lineage, external
  note, process source, policy, casebook, evaluation, fixture, harness,
  automation, runtime state, or Stage 0 artifact.

## Role Separation

### Plan Decision

Record only the accepted durable decision and this report within the exact
two-file allowlist. Do not reopen the accepted direction or implement it.

### Test Responsibility

Verify document structure, A/B/C conclusions, positive and stop conditions,
role and user-authority boundaries, degradation semantics, implementation
limits, links, whitespace, allowlist, staging state, and negative scope claims.

### Implementation Responsibility

There is no mechanism implementation in this task. The only implementation
responsibility is writing the two decision artifacts without changing any
runtime or canonical skill behavior.

### Review Check

Independent review identified an ambiguity in the observation-version
semantics. This scoped correction addresses that finding without claiming a
fresh-context re-review, current capability, or effectiveness; commit remains
a separate user decision.

## Verification

- Start state: `HEAD` was `95e026936187545590a5c0b926188ad51e842f05`,
  and `git status --short --untracked-files=all` was empty.
- Read all user-required sources in full. Also read `docs/v0.3-scope.md` as
  required by `AGENTS.md` for work touching external distillation.
- Read both complete new files and each complete new-file diff before the final
  verification pass.
- `git diff --check` passed with no output.
- Both `git diff --no-index --check /dev/null <file>` checks produced no
  whitespace warning and exited `1` only because each new file differs from
  `/dev/null`.
- `git status --short --untracked-files=all` listed exactly the two allowed new
  files. The tracked diff and staging area were empty.
- `docs/decisions/` contained only ADR-0001 and the new ADR-0002; ADR-0001 had
  no diff. All five repository-relative Markdown link targets in the new files
  existed.
- Structure and terminology checks confirmed the required ADR sections, all
  seven positive triggers, both A/B/C reviews, the role/evidence/effectiveness/
  capability/authorization distinctions, and the explicit prohibited-scope
  language.
- The scoped independent-review correction replaced all three operative uses
  of the ambiguous observation wording. A final terminology search found none
  remaining, and semantic checks confirmed the separate requirements for the
  external source task's historical skill attribution and the orchestration
  observation's actually loaded guidance/source version.
- A manual stale-language and scope-negative review found no claim that the
  orchestration, context isolation, review quality, or effectiveness is already
  implemented or verified; no automatic source discovery, outcome promotion,
  commit, telemetry, dashboard, global ledger, or case index; no completely
  independent-reviewer claim; and no commit-pending or other immediately stale
  current-state language. Mentions of those concepts are explicit non-goals,
  stop conditions, evidence limits, or future observation criteria.
- No skill/reference, `AGENTS.md`, README, process, v0.3 scope, ledger,
  casebook, policy, evaluation, Stage 0, external-note, fixture, harness,
  automation, or runtime-state file changed. The task invoked no subagents,
  network operation, dependency installation, `git add`, or `git commit`.

## Facts Not Established Before Implementation

This decision does not establish that the platform can create the required
fresh-context isolation, that a reviewer will remain unanchored, that the
Distillation Card will be sufficient, that detection and degradation work,
that routing or privacy findings are correct, that one correction is enough,
or that the workflow reduces user effort without excessive overhead. It also
does not establish review quality, evidence independence, behavioral
improvement, regression prevention, or any existing evidence outcome.

## Follow-Up Observation Standard

After a separately accepted reference-only implementation and independent
review, use natural, user-selected record-only tasks with a real opportunity to
trigger or stop the workflow rather than usage counts or manufactured evidence.
Record the orchestration guidance/source version actually loaded for every
observation. The external source task's historical `coding-review-loop` version
may remain unknown; that limits causal claims about the source task, not
attribution of a versioned orchestration observation. If the orchestration
version is unrecorded, the observation remains version-inconclusive and cannot
support a retain, narrow, or redesign conclusion.

Retain the mechanism when version-attributed observations show that triggers
and stops are precise, context isolation and degradation are truthful, review
remains role-separated, the card bounds edits, correction stays capped, work
remains uncommitted, and user transfer cost falls without disproportionate
overhead.

Narrow it when the route remains correct but trigger noise, card size, review
context, or overhead is excessive. Redesign it when user/privacy authority is
bypassed, capability claims are false, review is anchored by conclusions, stop
conditions fail, correction changes a route or decision, or automation expands
into promotion or commit behavior.

## Good

The decision targets one concrete coordination cost while preserving source
selection, privacy, central-lineage ownership, evidence limits, and commit
authority.

## Friction

Independent review found that the original observation wording could mean only
that expected task behavior was known, without requiring the orchestration
guidance/source version actually loaded for the observation. That ambiguity
could conflate an external source task's unknown historical
`coding-review-loop` version with attribution of the new mechanism's behavior.
The scoped correction separates those version facts and makes an unversioned
orchestration observation explicitly inconclusive.

## Proposed Follow-Up

- Confirm the scoped review correction, then make the user commit decision for
  these two artifacts.
- Only after acceptance, open a separate reference-only implementation task
  limited to `skills/evolving-agent-process/`; that task must also use
  `skill-creator`.
- Policy note candidate: no.
- Casebook or inbox candidate: no.
- Evaluation candidate: no; observe natural applicable behavior only after
  implementation.
