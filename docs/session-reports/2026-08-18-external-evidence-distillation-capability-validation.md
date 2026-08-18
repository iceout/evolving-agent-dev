# Session Report: External-Evidence Distillation Capability Validation

## Goal

Validate only the context boundary relevant to ADR-0002 condition 7: whether a
reviewer can be started without inheriting parent conversation turns that could
contain a Distillation Card or conclusion-oriented reasoning. This is not an
external evidence distillation, an effectiveness observation, or a change to
the orchestration guidance.

## Status

- Skills used: repo-tracked `evolving-agent-process` and system `openai-docs`.
- ADR source: [ADR-0002](../decisions/ADR-0002-external-evidence-distillation-orchestration.md).
- Capability result: qualified support for explicit parent-conversation-turn
  withholding on the observed direct-subagent surface; complete model input is
  not audited.
- Ephemeral CLI result: execution-path availability established; context
  isolation remains inconclusive on that surface.
- End-to-end orchestration, reviewer quality, evidence independence, and
  behavioral effectiveness: not established.
- External case distillation, central lineage update, Stage 0 evidence, and
  outcome promotion: none.

## Changes

- Updated ADR-0002's current observation plan to record only the supported
  parent-turn boundary, its disclosure requirements, and the distinction
  between execution-surface validation and per-task use of that boundary.
- Added this report. The historical implementation report remains unchanged:
  its earlier `inconclusive` probe was accurate for its invocation and does not
  become false retrospectively.

## Ephemeral CLI Probe

The successful CLI probe used the following complete instruction:

```text
You are a read-only context-boundary probe. Do not use tools or inspect files. You were given no source note, no Distillation Card, and no parent analysis. Respond with exactly four lines: probe_role: reviewer; source_note_received: no; card_or_parent_conclusions_received: no; tool_use: none.
```

`codex exec --ephemeral --sandbox read-only --json` started a new run without
`resume`, exited `0`, emitted `thread.started`, `turn.started`,
`item.completed`, and `turn.completed`, and recorded no command, file-change,
MCP, or web item. The reviewer returned the four requested negative receipts.

This establishes that the execution path can start a new ephemeral, read-only
run. It does not establish context isolation: JSONL does not expose the complete
model input, and the negative receipts are model self-report. The temporary
JSONL was removed after inspection, so no raw event artifact remains for
independent replay. The CLI probe is therefore context-inconclusive.

## Direct-Subagent Probes

All direct-subagent probes were read-only and prohibited tools and file reads.
The current collaboration interface states that `fork_turns: none` does not
pass surrounding conversation turns; the probes tested observable consequences
of that control.

### Commentary Sentinel Control

A parent commentary message contained the public sentinel
`CTX-PROBE-7K4M-20260818`. Both children received this exact instruction:

```text
This is a read-only context-boundary probe. Do not use tools or inspect files. Report exactly two lines: inherited_boundary_sentinel: <the exact boundary sentinel if one is visible in inherited conversation context, otherwise NONE>; non_prompt_task_context: <YES or NO>. Do not guess a sentinel.
```

Both the full-context control and no-turn child returned:

```text
inherited_boundary_sentinel: NONE
non_prompt_task_context: YES
```

Because the positive control did not detect the sentinel, this probe is
insensitive and supports no isolation conclusion.

### Parent User-Turn Control

Both children received this exact instruction:

```text
This is a read-only context-boundary probe. Do not use tools or inspect files. If a parent conversation was inherited, report the exact most recent parent user message. Otherwise report NONE. Output exactly one line: inherited_latest_user_message: <value>.
```

Observed results:

```text
fork_turns: all
inherited_latest_user_message: 请你继续验证啊

fork_turns: none
inherited_latest_user_message: NONE
```

The full-context child provides a working positive control. The paired result
supports that explicit no-turn forking withheld the parent user conversation
turn on this surface.

### Analysis-Card Sentinel Control

A read-only analysis child received this exact instruction:

```text
This is a read-only orchestration-boundary probe. Do not use tools or inspect files. Produce exactly one line: distillation_card_sentinel: CARD-PROBE-N9Q2-20260818
```

It returned:

```text
distillation_card_sentinel: CARD-PROBE-N9Q2-20260818
```

The full-context and no-turn review children then received this exact
instruction:

```text
This is a read-only context-boundary probe. Do not use tools or inspect files. If a Distillation Card sentinel from a prior analysis child is visible in inherited context, report it exactly; otherwise report NONE. Output exactly one line: inherited_card_sentinel: <value>.
```

Both returned:

```text
inherited_card_sentinel: NONE
```

Because the full-context control did not detect the sentinel, this probe cannot
establish Card isolation. It does show that the analysis-child result was not
observable through this particular inherited-turn query, but that absence is
not promoted into a general input-context claim.

## Interpretation

The positive-controlled user-turn result and the current callable interface's
explicit no-turn contract support only a narrow operational statement: parent
conversation turns can be withheld from a direct review child. This can satisfy
ADR-0002's practical review boundary only when the orchestrator keeps the Card
task-local, does not persist or pass it, uses explicit no-turn review, and
describes the result as parent-turn withholding.

The validation does not prove that hidden platform context, memory,
configuration, system instructions, or every internal message is absent. It
must not be described as fully audited prompt isolation, filesystem
non-visibility, model independence, evidence independence, or proof that a
review will be correct.

## Verification

- Initial baseline: `7168669` was `HEAD`; worktree and staging area were clean.
- The first sandboxed CLI invocation stopped before a child thread began because
  host-side initialization could not write local app-server state. A later CLI
  attempt bypassed the normal provider configuration and failed authentication.
  Neither reached a reviewer and neither was treated as isolation evidence.
- The corrected CLI invocation retained the normal local configuration, used an
  ephemeral new run and read-only child sandbox, and produced the execution
  events summarized above.
- The direct-subagent probes preserved their complete privacy-safe instructions,
  fork modes, relevant outputs, failed positive controls, and evidence limits in
  this report.
- All probe children were instructed not to use tools or inspect files. Final
  worktree inspection found no child modification outside this report task.
- Final `git diff --check` passed.
- Final `git diff --no-index --check /dev/null
  docs/session-reports/2026-08-18-external-evidence-distillation-capability-validation.md`
  produced no whitespace warning and exited `1` only because the report differs
  from `/dev/null`.
- The changed-file allowlist is exactly ADR-0002 and this report; the staging
  area is empty and all added repository-relative links resolve.

## Remaining Risk

- The complete model input is not exposed for audit, so stronger hidden-context
  claims remain untestable on the observed surfaces.
- The no-source probes do not establish the end-to-end Card handoff,
  task-specific reviewer prompt, review quality, or user-effort reduction.
- Platform behavior or configuration can change. Revalidation is required when
  the execution surface, relevant configuration, context semantics, or observed
  behavior materially changes, or when the applicable boundary is unclear; an
  ordinary task only checks that it uses the established boundary correctly.

## Good

The positive-controlled user-turn probe distinguishes a working, narrow
conversation boundary from the broader isolation claims that the available
evidence cannot support.

## Friction

- What happened: early CLI probes confused host initialization and provider
  configuration failures with reviewer-context capability; the first direct
  sentinel and Card controls also lacked a successful positive control.
- Why it felt wrong: those results could be promoted into either a false
  negative or an overclaimed isolation guarantee.
- Impact: a false negative preserves unnecessary manual forwarding; a false
  positive weakens the review boundary.
- Category: `tooling` / `context` / `verification`.
- Root cause guess: execution availability, parent-turn inheritance, full input
  observability, and review independence are separate properties and require
  separate claims.

## Proposed Follow-Up

- Independently review this two-file current-state update before a separately
  authorized commit.
- A future eligible task must still check all seven ADR conditions, use explicit
  no-turn review on this already validated surface, avoid passing the Card or
  parent conclusions, and record the orchestration guidance/source version
  actually loaded. It need not repeat a capability probe unless a revalidation
  trigger applies.
- Do not treat this capability validation as an external evidence observation,
  effectiveness result, policy, casebook entry, evaluation, or permission to
  auto-discover sources, promote outcomes, or commit.
