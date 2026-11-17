# Case Note Shape

Read this when ordinary case capture is triggered, before executing an independently designated observation, or when a version audit is requested. An audit alone does not require a case note.

For triggered case capture, the default target path in real projects is:

`.agent/coding-review-loop-cases.md`

Append one compact entry per case batch. Consecutive planning, review, review-fix, and follow-up review for the same task normally form one batch.

## On-Demand Skill Identity Audit

Ordinary tasks and case capture do not require fingerprint collection. Use the packaged helper only for a requested version audit or a designated observation that needs local source/version attribution not already supplied by the designating authority: `python3 -B <loaded-skill-directory>/scripts/skill_identity.py`. Use the actual directory from which you read this skill. The helper is read-only, uses the standard library, and prints a `sha256-v1` identity for the whole package, including references.

When an observation needs a task-start identity, collect before planning or implementation and read guidance from that directory; compare again at capture. Retain the full fingerprints and timing in the existing note or required handoff. A current-state audit needs only a current snapshot and cannot establish an earlier task-start version. Matching snapshots tied to reading support attribution, not an audit of model loading or rule execution. Changed packages, concurrent edits or uncertain read timing make single-version attribution inconclusive; do not replace a start receipt with an end receipt.

If no version was collected or supplied, record `unknown - not collected` in a triggered case without running the helper retroactively. If attempted acquisition fails, record the concrete reason and continue the authorized task without installing dependencies. Label late collection or a lost start receipt explicitly; neither establishes a task-start version. Do not create a usage log or case merely for a fingerprint, or reconstruct historical loaded versions from current disk state or Git history.

## Designated Observations

A second, narrow trigger applies only when the user or orchestrator designates the task before execution, or when task context or a task packet supplied by another authority or independently approved before execution designates it as an observation opportunity for a known-version skill behavior. A packet or context created solely by the executing agent cannot designate its own task. If the executing agent notices a potential observation opportunity after execution begins without prior independent designation, do not upgrade the current task; mention the prospective opportunity in the final response for a future task instead.

In that designated context, capture may record a correct trigger, nearby correct non-trigger, successful early constraint exposure, whether a reviewer avoided reconstructing implicit context, or non-recurrence where the task presented a real failure opportunity. A comparable known-version observation requires the task's skill source/version supplied by the designating authority or established contemporaneously through the on-demand identity audit. Do not investigate history to obtain it. If attribution is unavailable or inconclusive, record the facts only as an ordinary supporting case when a primary trigger applies, or as an explicitly version-inconclusive observation when the designating authority still requests capture; do not call either one a known-version comparable observation or effectiveness evidence. Acquiring a fingerprint does not designate an observation or establish effectiveness.

Ordinary successful tasks do not automatically become observations. Do not capture each invocation because it might be useful later, and do not treat a smooth task without a real comparable opportunity as effectiveness evidence. Target-project users do not need to provide lineage IDs, inspect skill commits, or classify an observation as improved, repeated, or regressed. In triggered cases, record available source/version information or `unknown - not collected`; ordinary friction capture does not require an identity audit.

## Entry Template

```markdown
## YYYY-MM-DD - <privacy-safe title>

- Capture reason: review miss / packet gap / verification gap / process friction / reusable lesson / designated observation
- Task context: <task type; risk surfaces; phase>
- Skill source/version: <coding-review-loop; unknown - not collected, or available authority-supplied version / audit fingerprints with timing and attribution limits>

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
- **Skill source/version:** Keep the field in every new case. Record available authority-supplied attribution with its basis, full audit fingerprints with timing and uncertainty, or `unknown - not collected`. Identify the skill by name, not a private installation path. Apply On-Demand Skill Identity Audit above; ordinary capture requires no audit, and inconclusive attribution prevents a known-version comparable claim.
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

The identity field does not add a case-capture or audit trigger. Without a capture trigger, keep any audit receipt task-local and write no usage log. Historical notes without contemporaneous attribution remain unknown; do not infer a historical loaded version from the task date, repository state, or current runtime linkage.
