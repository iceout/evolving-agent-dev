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
- Skill source/version (optional for ordinary cases; required for a comparable designated observation and supplied by the designating authority or already visible):

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
- **Skill source/version:** For ordinary friction, miss, gap, or lesson cases, omit the field or use `unknown` when the value is not already visible. For a comparable designated observation, record the task's source/version supplied by the designating authority or already visible during the task. Do not investigate history. If unavailable, use a primary-trigger supporting case when applicable or label the requested observation `version inconclusive`; do not call it a known-version comparable observation or effectiveness evidence.
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

The skill source/version field remains optional for ordinary cases and may be omitted or set to `unknown`. A comparable designated observation requires the task's source/version from the designating authority or information already visible during the task. Do not investigate commit history or infer a historical loaded version from the task date, repository state, or current runtime linkage.
