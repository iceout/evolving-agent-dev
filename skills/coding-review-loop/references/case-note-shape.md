# Case Note Shape

Use this only when a coding-review-loop task triggers case capture through notable process friction, a review miss, packet gap, verification gap, reusable lesson, or an explicitly designated observation opportunity.

Default target path in real projects:

`.agent/coding-review-loop-cases.md`

Append one compact entry per case batch. Consecutive planning, review, review-fix, and follow-up review for the same task normally form one batch.

## Entry Template

```markdown
## YYYY-MM-DD - <privacy-safe title>

- Capture reason: review miss / packet gap / verification gap / process friction / reusable lesson / designated observation
- Task context: <task type; risk surfaces; phase>
- Skill source/version: <coding-review-loop; start sha256-v1:...; end sha256-v1:...; captured at first use before planning; unchanged / changed / inconclusive, or unknown with reason>

### Expected And Observed

- Expected:
- Observed:
- Detection:

### Action And Evidence

- Action:
- Verification:
- Remaining gap:

### Transfer Signal

- Reusable signal:
- Comparable opportunity (only for designated observations):
- Privacy boundary:
```

## Field Semantics

- **Capture reason:** State why the entry is worth creating. Keep `designated observation` distinct from friction, misses, and gaps; do not enter a central lineage outcome.
- **Task context:** Compress task type, risk surfaces, and phase into one line or short paragraph. Do not copy the full packet.
- **Skill source/version:** Required in every new case. Use the Task-Start Skill Identity receipt from `SKILL.md` and the check at capture; record full fingerprints, acquisition timing, and any change or uncertainty. Identify the skill by name, not a private installation path. An authority-supplied version may also be recorded with its basis; distinguish it from locally observed content. If acquisition failed, record `unknown` and why. A late snapshot or lost start receipt cannot establish a task-start version. Do not investigate history or backfill older entries from current disk state. Attribution alone does not designate an observation or prove execution/effectiveness; inconclusive attribution prevents a known-version comparable claim.
- **Expected:** Record the factual plan, contract, or skill behavior that can be compared with what happened.
- **Observed:** Record the actual execution or review observation. A successful designated observation may state that expected behavior occurred; do not record model-internal reasoning.
- **Detection:** Name the packet review, independent reviewer, test, command, runtime check, or user observation without copying full logs.
- **Action:** Record only the target project's local correction, decision, or no-change. Do not require an evolving-agent-dev skill proposal.
- **Verification:** Record completed tests, commands, artifact review, or manual checks, preserving the distinction between local, target, and production-like verification.
- **Remaining gap:** State what was not run or could not be established. Do not present a plan, proposed gate, or review suggestion as verified.
- **Reusable signal:** Give one privacy-safe, factual, transferable observation. Do not require root-cause classification, lineage mapping, or a promotion decision.
- **Comparable opportunity:** Use only for an independently designated observation. State who or what designated it before execution and the real opportunity for the target behavior to fail, trigger correctly, or correctly not trigger. Without prior independent designation, a known source/version, and a real opportunity, absence of a problem is not known-version improvement evidence. Omit this field for ordinary friction cases and version-inconclusive observations.
- **Privacy boundary:** State which identities, paths, payloads, endpoints, credentials, recipients, or user/customer data were omitted or generalized.

## Lightweight Boundary

Keep each field to one or two sentences. A note is normally about 100-200 English words or 150-300 Chinese characters. Do not copy a full chat, packet, diff, command output, review transcript, or large code excerpt. Omit inapplicable conditional fields instead of accumulating `N/A` values.

This note is a factual transfer artifact, not a complete retrospective, session report, or central lineage record. Target-project users record local facts only; evolving-agent-dev owns inbox/casebook routing, skill refinement, evaluation decisions, lineage, regression classification, root-cause classification, promotion, and later outcomes.

## Batch Transfer

When several entries accumulate, the user can copy this file back to evolving-agent-dev for batch distillation. Treat transferred entries as external privacy-preserving evidence, not accepted internal Stage 0 dogfood evidence.

Treat these notes as local transfer artifacts by default; do not include them in product commits unless the user or target repo convention explicitly wants agent notes committed.

The identity field does not add a case-capture trigger. Without a capture trigger, keep the receipt task-local and write no usage log. Historical notes without receipts remain unknown; do not infer a historical loaded version from the task date, repository state, or current runtime linkage.
