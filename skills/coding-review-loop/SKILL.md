---
name: coding-review-loop
description: "Use when planning, implementing, or reviewing non-trivial coding tasks in real code projects, not evolving-agent-dev process work, that need independent review, multi-round review, cross-agent handoff, a repo-local plan/review packet, plan-to-implementation traceability, or high-risk debugging/bad-case analysis. Trigger for public interfaces, hot paths, schema/contracts, data semantics, sensitive output, batch/action/export behavior, time windows, config/deployment, missed detections, wrong scores/selections, surprising outputs, or when the user asks to plan first or review before coding."
---

# Coding Review Loop

Use this skill for real code projects. It helps Codex make non-trivial plans reviewable, keep high-risk debugging grounded in evidence, and preserve traceability from plan to implementation and verification.

Do not create evolving-agent-dev artifacts in target repos. Follow the target repo's conventions for plans, docs, tests, and verification.

## Plan Artifact Rule

Keep plan artifacts lightweight and trigger-based.

- Small tasks may keep the plan in the final response.
- Medium-complexity tasks that need independent review, multi-round review, cross-agent handoff, or later implementation should create a repo-local plan/review packet.
- High-risk tasks should have the packet reviewed before implementation.
- Treat a task as high-risk when it enables or changes a user-impacting live side effect, including write execution, notification delivery or recipient targeting, scheduled side-effect behavior, or the default between dry-run and live execution. Create the packet and make it reviewable before the first implementation edit; do not reconstruct it only after implementation has started. Copy, formatting, comments, documentation, or similar changes do not trigger this rule by themselves when delivery capability, recipients, execution mode, output sensitivity, and side-effect behavior remain unchanged; assess other risk surfaces independently.
- Future subagent or automation review should consume packet artifacts, not raw chat context.
- Use existing repo conventions for plan docs. When a packet is needed within the authorized task and no convention exists, choose a descriptive, non-conflicting repo-local temporary path and report it. Ask only if a repository restriction or material user decision prevents that choice. Respect explicit no-file or plan-only instructions; necessary planning does not authorize implementation or external actions beyond the task.

Read `references/review-packet-shape.md` only when a packet is needed. Do not load it for trivial tasks.

## Debug / Bad-Case Root-Cause Gate

For high-risk bad cases, missed detections, wrong scores/selections, surprising output, or similar examples, do not jump straight to a local patch.

First establish the evidence chain:

- observed symptom
- expected behavior
- affected contract
- candidate failure points
- source-of-truth data
- blockers/filters
- real verification path

If a quick patch is proposed before root cause is proven, label it as interim mitigation and keep it separate from final redesign. Avoid feature-specific heuristic patches unless explicitly justified and reviewed.

## Focused Reuse Scan

Before adding or changing a helper, fake, adapter, wrapper, serializer, collection getter, fallback, or test double, run a focused reuse scan across the current file and sibling modules/tests for same-concern helpers or source-of-truth patterns.

When removing or renaming a shared wrapper, adapter, getter, serializer, or other symbol, scan repository-wide imports and references and discover runnable entrypoints from repository conventions, task configuration, CI, CLIs, job definitions, and executable modules. Do not assume one directory glob covers every entrypoint.

Search by semantic responsibility, not only feature keywords. Before adding a helper, check whether existing source-of-truth helpers plus caller-local state can express the behavior.

This scan is especially important during review-fix work: do not only patch the reported failure if the fix introduces a new seam or helper.

Ask:

- Is this behavior real product or infrastructure strategy, or only test convenience?
- Is the source of truth verified in project docs, config, runtime evidence, or existing helpers?
- Can tests mock one boundary helper instead of pushing dependency-injection seams through production APIs?
- Does this wrapper add semantics beyond a direct config or collection lookup?
- Does this fake or test double model an external API, state machine, chained call, or boundary behavior that should be shared or explicitly local?

Local helpers and fakes are fine when they are truly local. When they encode external API semantics such as cursor chaining, sorting, limits, retries, fallback behavior, or data-source selection, centralize the semantics or explain why a local duplicate is safer.

A helper should provide reuse, boundary isolation, or a stable business concept; otherwise keep short straight-line logic inline.

## Implementation Trace

After implementation, update the packet's existing requirement trace when present; otherwise report or write a compact trace. Do not maintain a duplicate table:

```text
plan constraint -> implementation anchor -> behavior test -> verification command
```

For promised dry-runs, shadow reports, exports, scripts, CLIs, or default entrypoints, include the runnable entrypoint, default config or parameters, expected output fields, and verification command.

Distinguish local verification from production-like, rollout, or manual baseline verification. Do not claim strategy calibration from local tests alone.

## Case Note Capture

At the end of every medium/high-risk coding-review-loop task, make an explicit case-capture decision. This requires deciding whether capture is warranted, not creating a file for every task. Small or trivial tasks do not need an additional capture decision.

Append a privacy-preserving case note in the target repo when a medium/high-risk task exposes notable process friction, a review miss, packet gap, verification gap, or reusable lesson.

A second, narrow trigger applies only when the user or orchestrator designates the task before execution, or when task context or a task packet supplied by another authority or independently approved before execution designates it as an observation opportunity for a known-version skill behavior. A packet or context created solely by the executing agent cannot designate its own task. If the executing agent notices a potential observation opportunity after execution begins without prior independent designation, do not upgrade the current task; mention the prospective opportunity in the final response for a future task instead.

In that designated context, capture may record a correct trigger, nearby correct non-trigger, successful early constraint exposure, whether a reviewer avoided reconstructing implicit context, or non-recurrence where the task presented a real failure opportunity. A comparable known-version observation requires the task's skill source/version to be supplied by the designating authority or already visible during the task. Do not investigate history to obtain it. If the source/version is unavailable, record the facts only as an ordinary supporting case when a primary trigger applies, or as an explicitly version-inconclusive observation when the designating authority still requests capture; do not call either one a known-version comparable observation or effectiveness evidence.

Ordinary successful tasks do not automatically become observations. Do not capture each invocation because it might be useful later, and do not treat a smooth task without a real comparable opportunity as effectiveness evidence. Target-project users do not need to provide lineage IDs, inspect skill commits, or classify an observation as improved, repeated, or regressed. For ordinary cases, record a skill source/version only when it is already visible; otherwise omit it or use `unknown`.

Prefer `.agent/coding-review-loop-cases.md` when the target repo has no existing convention. If the repo should not keep agent notes, ask the user where to place the note or include the case note in the final response.

Treat these notes as local transfer artifacts by default; do not include them in product commits unless the user or target repo convention explicitly wants agent notes committed.

Do not record private data, credentials, customer identifiers, sensitive payloads, large code excerpts, or full chat transcripts. Generalize file paths, business identifiers, and data samples when needed.

When no trigger applies, do not create or append a note and do not create a case-index entry. Do not append no-op entries merely to record that the skill was used.

Read `references/case-note-shape.md` only when case note capture is triggered.

In the final response for every medium/high-risk task, include a brief capture status that says either that a case was appended or included and why, or that no case was created and why. For example: `Case capture: appended - independent review exposed a reusable packet gap.` or `Case capture: not created - no notable signal or designated observation opportunity.`

## Review Behavior

When reviewing, put findings first.

For action/report/enum-like contracts, review semantic liveness: acceptance-critical values should have a producer, consumer, and behavior test, and report/config labels should not imply actionable behavior that code has not validated.

For medium/high-risk coding tasks, subagent or automation review must use independent adversarial review semantics. Do not frame the review as confirmation that the main session's listed constraints are covered. Ask the reviewer to find concrete failure modes, contract violations, test gaps, scope drift, unsafe output, compatibility breaks, and packet gaps.

Before requesting subagent or automation review, provide a minimal review packet rather than raw chat context. Include at least:

- goal and non-goals
- changed files or diff scope
- risk surfaces
- reviewable constraints
- required behavior tests or verification plan
- known user decisions or accepted exceptions

Add task-specific contracts, source-of-truth/fallback semantics, and implementation trace when relevant.

For each major finding, classify it as one of:

- concrete project bug
- missing or ambiguous plan constraint
- implementation violation
- accepted exception
- out-of-scope item

Identify packet gaps when review required manual context reconstruction across plans, existing APIs, legacy behavior, config, tests, or user decisions.

When a reviewer reports no findings, require evidence: inspected files, checked risks, commands or tests reviewed/run, and residual risks. Do not accept bare `LGTM`, "looks good", or "no obvious issues" as sufficient review evidence; treat that as shallow or insufficient review and request a stronger review or perform another one.
