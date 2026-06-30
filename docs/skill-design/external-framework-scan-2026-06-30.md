# External Framework Scan: 2026-06-30

Status: selected scan.

## Scope

This was a selective scan, not a comprehensive review of gstack or superpowers. External frameworks were treated as design inputs, not authorities or accepted evidence for this project.

Read from this project:

- `README.md`
- `docs/process-v0.2.md`
- `docs/v0.3-scope.md`
- `docs/skill-design/external-framework-scan.md`
- `skills/coding-review-loop/SKILL.md`
- `skills/idea-framing-loop/SKILL.md`

Selected external sources read:

- gstack: `README.md`, `ETHOS.md`, selected relevant sections from `office-hours/SKILL.md`, `plan-eng-review/SKILL.md`, `review/SKILL.md`, `investigate/SKILL.md`, and `qa-only/SKILL.md`.
- superpowers: `README.md`, `skills/brainstorming/SKILL.md`, selected relevant sections from `skills/writing-plans/SKILL.md`, full `skills/requesting-code-review/SKILL.md`, full `skills/receiving-code-review/SKILL.md`, selected relevant sections from `skills/subagent-driven-development/SKILL.md`, full `skills/systematic-debugging/SKILL.md`, and full `skills/verification-before-completion/SKILL.md`.

These sources were chosen because they map to current v0.3 themes: idea framing, planning, review, subagent handoff, root-cause debugging, verification, QA, search-before-build, and external-framework scan boundaries.

## Executive Summary

- Strongest borrowable pattern: make review-fix work more disciplined. Superpowers' review reception pattern and gstack's verification-of-claims rule both reinforce this project's recent fake cursor friction: do not blindly implement review feedback; verify codebase reality, fix one item at a time, and re-check the result.
- Already covered: `skills/coding-review-loop/SKILL.md` already contains plan packet behavior, adversarial review semantics, debug root-cause gate, implementation trace, and focused reuse scan. gstack and superpowers mostly validate those directions rather than requiring immediate skill edits.
- Useful backlog refinement: add future watchlist language around two-stage review, distinguishing spec/plan compliance from code quality. This could reduce plan-to-implementation drift without adopting a full subagent framework now.
- Continue observing: verification-before-completion and source-of-truth/fallback semantics remain promising evaluation candidates, but need privacy-safe fixtures and pass/fail rubrics before promotion.
- Do not copy yet: hard mandatory design gates, TDD-always, broad autonomous subagent pipelines, browser QA infrastructure, release automation, telemetry, memory systems, or full product-factory workflows.

## Pattern Map

| External pattern | Source | Problem it solves | Fit for this project | Action |
|---|---|---|---|---|
| Staged idea/spec approval before implementation | superpowers `brainstorming`; gstack `office-hours` | Prevents agents from coding from vague ideas or hidden assumptions. | Partly covered by `idea-framing-loop`, but this project intentionally keeps it lightweight and trigger-based. | Continue observing; possible future refinement for non-trivial agent behavior changes, not a hard gate for every task. |
| Written plan before execution with explicit task slices | superpowers `writing-plans`; gstack `plan-eng-review` | Makes implementation handoff concrete enough for a fresh agent and exposes test/verification gaps before coding. | Covered in lighter form by `coding-review-loop` plan/review packet. | Future skill refinement candidate for high-risk multi-step tasks: optional task-slice checklist, not always-on complete code plans. |
| Search before building / what already exists | gstack `ETHOS` and `plan-eng-review` | Reduces duplicated helpers, parallel implementations, and custom solutions where built-ins or existing flows exist. | Directly maps to focused reuse scan and recent Mongo helper/fake friction. | Already absorbed by `coding-review-loop` Focused Reuse Scan; continue collecting evaluation-quality fixtures. |
| Independent/adversarial review | gstack `review`; superpowers `requesting-code-review` | Finds production risks and plan drift that the implementation agent misses. | Already covered by `coding-review-loop` Review Behavior. | No change now; use as support for future review-packet fixture design. |
| Review feedback reception discipline | superpowers `receiving-code-review`; gstack `review` verification-of-claims | Prevents blind review-fix patches, performative agreement, and unverified claims that feedback is handled. | Strong fit for the recent review-fix fake cursor miss. | Future skill refinement candidate: review-fix should verify codebase reality and run focused reuse/source-of-truth scans before patching. |
| Two-stage review: spec compliance then code quality | superpowers `subagent-driven-development` | Separates "did we build the requested thing?" from "is the implementation good?" | Fits current plan-to-implementation traceability friction, but full subagent loop is too heavy now. | Add to watchlist; consider evaluation fixture before changing skills. |
| Systematic debugging / root-cause gate | gstack `investigate`; superpowers `systematic-debugging` | Stops quick patches and symptom fixes before root cause is proven. | Already covered by `coding-review-loop` Debug / Bad-Case Root-Cause Gate. | No change now; possible future fixture around 3 failed hypotheses or fallback-as-mitigation boundary. |
| Verification before completion | superpowers `verification-before-completion`; gstack review/QA verification rules | Prevents false completion claims and requires fresh evidence. | Already covered in `evolving-agent-process` verification rules and `coding-review-loop` implementation trace. | Continue observing; possible evaluation candidate when fixture-quality failures appear. |
| Browser/manual QA loop with evidence | gstack `qa-only` | Tests user-visible behavior with screenshots, console checks, repro steps, and report-only output. | Useful for future real-code QA, but outside current process-doc v0.3 scope. | Do not copy now; possible future external coding skill or QA note if real tasks demand it. |
| Hard gates and full autonomous workflow | superpowers basic workflow; gstack sprint pipeline | Provides consistency across full product delivery. | Mismatched with this repo's current lightweight, evidence-first v0.3 scope. | Do not copy yet. Preserve low-noise triggered checks. |

## Candidate Borrowings

### Review-Fix Reception Discipline

- Pattern: Treat review feedback as technical input to verify, not instructions to blindly implement.
- Why it fits: Recent `_FakeMongoCursor` duplication happened after a subagent finding because the fix narrowed to the reported failure and did not re-run a focused reuse scan.
- Where to route: future `coding-review-loop` refinement candidate; possible evaluation watchlist if a privacy-safe review-fix fixture can be built.
- Risk/noise: Too much ceremony could slow small review comments. Keep it triggered by review fixes that introduce or modify helpers, fakes, adapters, wrappers, fallbacks, serializers, or test doubles.

### Spec Compliance vs Code Quality Review Split

- Pattern: Review first for whether implementation matches the accepted plan/spec, then separately for code quality.
- Why it fits: This project has repeated plan-to-implementation traceability and review packet friction.
- Where to route: v0.3 backlog / evaluation watchlist, not skill edit yet.
- Risk/noise: A mandatory two-stage review for every task would be too heavy. Use only for medium/high-risk tasks, subagent handoff, or review-packet tasks.

### What Already Exists / Search Before Building Output

- Pattern: Make reuse scan findings visible as an output, not just an internal thought.
- Why it fits: Thin Mongo wrappers and duplicated fake cursors show that saying "reuse scan" is not enough when helpers encode external API or source-of-truth semantics.
- Where to route: already partly in `coding-review-loop` Focused Reuse Scan; continue observing for fixture-quality evidence.
- Risk/noise: Requiring a written reuse section for every tiny helper would be noisy. Trigger only for production API seams, data-source/fallback behavior, adapters, wrappers, fakes, and test doubles.

### Verification Evidence Before Completion Claims

- Pattern: Identify the verification command, run it freshly, read output, and only then state status.
- Why it fits: This matches existing verification failure rules and supports future evaluation of false-completion behavior.
- Where to route: continue observing; possible evaluation candidate when a privacy-safe fixture can test success-claim discipline.
- Risk/noise: The principle is already present; over-restating it in every skill could create duplication.

### External Pattern Search During Debugging

- Pattern: After local root-cause evidence is gathered, search external references for known framework/library failure modes using sanitized generic errors.
- Why it fits: Complements source-of-truth/fallback semantics and failure-driven external framework scan.
- Where to route: v0.3 backlog / continue observing.
- Risk/noise: Web search can leak sensitive details or distract from local evidence. Keep it sanitized and secondary to local root-cause investigation.

## Patterns Not To Copy Yet

- Hard mandatory brainstorming/design approval for every task. This would conflict with this project's lightweight micro-task routing and likely over-trigger on small process edits.
- TDD-always and delete-code-before-tests rules. This project values behavior-level verification, but current evidence does not justify a universal TDD gate.
- Full subagent-driven development loop with implementer plus spec reviewer plus code-quality reviewer per task. The split is useful, but the full workflow is too heavy before this project has a runtime or judgeable fixtures.
- gstack's full sprint/product factory pipeline, release automation, telemetry, memory system, review dashboard, and browser QA infrastructure. These are useful product ideas, not current v0.3 scope.
- Always-on cross-model review. Independent adversarial review is valuable, but this project should keep it triggered by risk and review-packet needs until it has low-noise evidence.

## Relationship To Current Project

- `skills/coding-review-loop/SKILL.md`: The scan mostly validates current direction: review packets, adversarial review semantics, debug root-cause gate, implementation trace, and Focused Reuse Scan. The strongest future refinement is review-fix reception discipline: verify feedback against codebase reality before patching, especially when adding helpers/fakes/wrappers.
- `skills/idea-framing-loop/SKILL.md`: Superpowers and gstack both support idea framing before implementation, but their hard gates are heavier than this project's current skill. Keep the current one-question-at-a-time, trigger-based framing model.
- `docs/v0.3-scope.md`: The scan supports existing carryovers: planning impact analysis, reuse scan, source-of-truth/fallback semantics, and lightweight executable behavior. It does not justify creating `docs/process-v0.3.md`.
- Existing watchlist: Focused reuse scan and source-of-truth/fallback semantics remain watchlist items. External sources make the patterns clearer but do not provide accepted internal evidence.

## Proposed Follow-up

- No skill changes in this task.
- Future skill refinement candidate: add a narrow review-fix reception rule to `coding-review-loop` only if another real review-fix task repeats the blind-patch pattern.
- Future evaluation candidate: construct a privacy-safe review-fix fixture where an agent must resolve review feedback without duplicating a test double or encoding an unverified fallback.
- Future casebook/policy candidate: only if the same review-fix / source-of-truth / reuse-scan pattern repeats with enough replayable context.
- Continue treating gstack and superpowers as design inputs, not authorities or accepted evidence.
