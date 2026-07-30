# Local Evidence Ledger

Status: design note.

## Purpose

Record local, privacy-preserving, high-signal evidence that helps evaluate and improve agent skills over time.

This borrows the useful idea behind gstack's local analytics, learnings, timeline, and eureka logs, but not its telemetry system. The goal is not usage metrics for their own sake; the goal is to make skill effectiveness, repeated friction, and reusable process lessons easier to distill.

The design boundary is intentionally conservative: do not track everything, and do not add runtime logging or automation from this note. Triggered narrative guidance may evolve independently without turning this design into a usage ledger.

## Principles

- Local-first.
- Privacy-preserving by default.
- High-signal over comprehensive.
- Evidence for improvement, not vanity metrics.
- Project-local before global.
- Opt-in before cross-project aggregation.
- Human-reviewable before metrics-driven.
- No remote telemetry in current scope.

## Non-Goals

- Remote telemetry.
- Recording code, prompts, arbitrary file paths, branch names, repo basenames, user data, customer identifiers, secrets, raw errors with private data, or raw payloads.
- Writing logs on every skill invocation.
- Complex dashboards or metrics automation.
- Treating usage counts as proof of skill quality.
- Creating a cross-project global ledger by default.
- Runtime capture or logging behavior beyond explicit triggered narrative guidance.

## Recommended Local Files

### Case Notes

Already used or intended:

- `.agent/coding-review-loop-cases.md`
- `.agent/idea-framing-notes.md`
- `.agent/bug-investigation-cases.md`

These capture high-signal narrative evidence. For `coding-review-loop`, write them only when the task produces notable process friction, a review miss, a packet gap, a verification gap, a reusable lesson, or a narrow designated observation. A handoff can be recorded when it exposes one of those signals, such as a reusable lesson; evaluation candidacy remains a central distillation decision rather than a target-project trigger.

A designated observation requires the user or orchestrator to designate it before execution, or task context or a packet supplied by another authority or independently approved before execution to identify the opportunity. The executing agent cannot self-designate through its own packet or context; an opportunity noticed after execution begins can only be proposed for a future task. A comparable known-version observation also requires the task's source/version from the designating authority or information already visible during the task. Without it, retain the facts only as a primary-trigger supporting case or an explicitly version-inconclusive observation, never as known-version effectiveness evidence.

An authorized designated observation may record a successful trigger, nearby correct non-trigger, early constraint exposure, reviewer context sufficiency, or non-recurrence when a real failure opportunity existed. Ordinary successful tasks and smooth tasks without a real comparable opportunity are not automatically evidence.

### Case Index

Optional future local index:

`.agent/skill-case-index.jsonl`

Use one line per high-signal case note for batch distillation. A case index entry should exist only when a narrative case note exists. A no-op capture decision must not create an index entry.

Example:

```json
{"ts":"2026-07-09T10:12:00Z","skill":"coding-review-loop","event":"case_note","outcome":"friction","note_file":".agent/coding-review-loop-cases.md","tags":["review-fix","dataflow"],"privacy":"local-transfer"}
```

The example's `friction` outcome is illustrative, not a rule that narrative notes can record only failures. This design does not implement the JSONL index.

The `note_file` field should point only to an approved local agent-note file, not to product source files or arbitrary paths.

### Rare Insight Log

Optional future local log:

`.agent/agent-insights.jsonl`

Use only for rare reusable insights that would save future time or prevent repeated mistakes.

Example:

```json
{"ts":"2026-07-09T10:20:00Z","skill":"coding-review-loop","type":"insight","summary":"Helper API shape is insufficient; review must trace caller preservation of streaming or time-window contracts.","confidence":8,"source":"observed","privacy":"local-transfer"}
```

Rare insight entries should be short, generalized, and free of code, prompts, private payloads, source paths, customer identifiers, or project names.

### Skill Usage Summary

Optional future local log:

`.agent/skill-usage.jsonl`

Use only if low-sensitive skill effectiveness analysis becomes necessary. Do not record repo basename, branch, arbitrary file paths, prompts, code, raw command output, raw errors, or raw payloads.

Example:

```json
{"ts":"2026-07-09T10:30:00Z","skill":"bug-investigation-loop","event":"completed","outcome":"blocked","case_note":true,"handoff":"coding-review-loop","privacy":"local-transfer"}
```

This file should not be a default write-on-every-invocation analytics stream. It is a possible future summary log for explicit opt-in designs and remains unimplemented in this refinement.

## Suggested Fields

Allowed low-sensitive fields:

- `ts`
- `skill`
- `event`
- `outcome`
- `case_note`
- `note_file`, limited to approved `.agent/*` note files
- `tags`
- `handoff`
- `privacy`
- `confidence`
- `source`

Avoid by default:

- repo basename
- branch name
- arbitrary file paths
- product source file paths
- full commands
- code snippets
- prompts
- raw errors with private data
- raw command output
- customer or account identifiers
- secrets or tokens
- production payloads

## Trigger Rules

At the end of every medium/high-risk `coding-review-loop` task, make an explicit case-capture decision. This is a decision requirement, not a narrative-note requirement; small and trivial tasks have no additional capture burden.

Write a narrative case note only when there is notable process friction, review miss, packet gap, verification gap, reusable lesson, or an independently designated observation opportunity. A designated observation may record successful or correct non-trigger behavior, but the target project must not classify it as `improved`, `repeated`, or `regression`. Handoff is not a separate trigger, and evaluation candidacy belongs to central distillation.

When no trigger applies, record the not-created status and brief reason in the final response only. Do not create or append a narrative note or case-index entry, and do not write a no-op entry merely to record skill use.

Write case index entries only when a narrative case note is created.

Write rare insight entries only when the insight would likely save future time or prevent a repeated mistake.

Do not write usage entries for every skill invocation unless a future explicit opt-in design says so.

Do not create runtime hooks, telemetry clients, dashboard jobs, or background distillation from this design note.

## Batch Distillation Workflow

1. A real project accumulates `.agent/*.md` notes and optional `.agent/*.jsonl` indexes.
2. The user selects and copies privacy-reviewed files back to `evolving-agent-dev`.
3. Distill selected material into one of:
   - `docs/casebook/inbox.md`
   - a casebook entry
   - a skill refinement
   - an evaluation watchlist item
   - no action
4. Treat transferred files as external privacy-preserving evidence, not internal accepted Stage 0 evidence.

This keeps source projects in control of what crosses the boundary and avoids default cross-project aggregation.

### Central Evidence Lineage

Do not create a second ledger for central distillation. Use the distillation session report for the immutable source review and decision record, and the existing `docs/v0.3-scope.md` watchlist for the current cross-session state when a pattern needs later observation.

A central lineage record may contain:

- a privacy-safe source ID and case ID
- normalized pattern
- root-cause hypothesis and confidence
- repository rule state: `absent` / `partial` / `present`
- source-task attribution: `known rule absent` / `known rule present but not executed` / `loaded version unknown` / `timeline inconclusive`
- accepted change or explicit no-change decision
- change date, artifact, version, or commit when known
- later comparable evidence
- current outcome: `awaiting evidence` / `improved` / `repeated` / `inconclusive`
- the evidence supporting that outcome

Repository rule state describes the canonical repository rule at the relevant comparison point. Source-task attribution separately describes what can be established about the rule loaded by the source task.

Use `known rule present but not executed` only when the task's loaded skill source or version is known to include the rule and the task facts show that the gate was skipped. Use `known rule absent` only when the loaded source/version is known and does not contain the rule. Repository commit dates alone do not prove which skill version a task loaded.

Outcome meanings:

- `awaiting evidence`: a change or no-change decision exists, but there is no later comparable evidence from a known relevant version.
- `improved`: later comparable evidence used the changed version and shows the expected behavior with real verification.
- `repeated`: later comparable evidence used the changed version and the normalized problem recurred.
- `inconclusive`: version, comparability, ordering, or verification facts are insufficient.

The target-project user records only local facts and may record a skill source or version only when it is already visible. The target project does not own inbox or casebook routing, skill refinement, evaluation decisions, lineage, root-cause classification, change/no-change decisions, promotion, regression classification, or later outcomes. The evolving-agent-dev distiller owns those central responsibilities.

A designated observation with independently established authority, a real opportunity, and the task's visible or supplied source/version can preserve a successful trigger or correct non-trigger fact for later comparison, but it cannot assign a central outcome. A version-inconclusive observation is supporting evidence only. Central distillation determines comparability and any later `improved`, `repeated`, or `inconclusive` classification from versioned evidence.

Assign privacy-safe source and case IDs during central distillation. Before creating a pattern, search existing inbox entries, distillation reports, and watchlist items. Reuse an existing pattern for supporting or later evidence; do not count a copied or semantically duplicate case as a new independent issue.

## Skill Effectiveness Retro

Future optional workflow:

- Read local case notes and indexes.
- Summarize which skills produced useful outcomes, blocked outcomes, repeated friction, or handoffs.
- Compare repeated patterns before and after skill refinements.
- Recommend whether to update a skill, create a casebook entry, or design an evaluation fixture.

This should remain human-reviewable and should not become automatic metrics-driven policy.

Usage counts alone should not be treated as skill quality evidence. A low-frequency case that prevents a costly repeated mistake can matter more than a high-frequency success counter.

## Relationship to gstack Input

Borrowed design ideas:

- Local usage or case traces can help future distillation.
- Session timelines can separate started, completed, blocked, and handoff outcomes.
- Learnings and rare eureka-style insights are useful only when they are sparse and reusable.
- Cross-project learning should be explicit and opt-in, not assumed.

Not borrowed:

- Remote telemetry.
- Default repo basename or branch recording.
- Per-skill invocation analytics as a default behavior.
- Global cross-project logs as the default storage model.
- Metrics dashboards or automated effectiveness scoring.
- Any runtime behavior change for existing skills.

gstack behavior is design input only. It is not project evidence for Stage 0 or v0.3 acceptance.

## Open Questions

- Whether `.agent/skill-case-index.jsonl` is worth implementing before more real-project dogfood.
- Whether `bug-investigation-loop` should get a dedicated `.agent/bug-investigation-cases.md` template.
- Whether skill usage entries should ever be written for successful no-friction runs.
- Whether repo-local hash IDs are useful or still too risky.
- Whether `note_file` should remain an allowed field or be replaced by a fixed note-type enum.
