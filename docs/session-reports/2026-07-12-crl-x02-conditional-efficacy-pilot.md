# Session Report: CRL-X02 Conditional-Efficacy Pilot

## Goal

Run one narrow, paired pilot to test whether the CRL-X02 removal/rename clarification changes behavior after `coding-review-loop` has already been selected and loaded. Compare known old/new full skill-package snapshots on the same privacy-safe synthetic shared-wrapper-removal task without exposing the hidden rubric, traps, pair mapping, or expected failure modes to either executor.

This pilot does not test automatic skill selection, packet-first behavior, X01/X03, repeated-run stability, real-project improvement, natural generalization, or formal evaluation promotion.

## Status

- Dogfood: yes; the pilot orchestration and evidence update used the repo-tracked `evolving-agent-process` skill.
- Evidence level: synthetic `fixture-conformant` behavior only.
- Pilot result: `no incremental signal`.
- CRL-X02 lineage outcome: remains `awaiting evidence`.
- Stage 0 evidence status: not accepted Stage 0 evidence; frozen counts remain unchanged.

## Experimental Controls

- Run A loaded the full `coding-review-loop` package from `a90e36684370e6e681cc4ec351759e01e2256b20`; Run B loaded the full package from `3a0f4bf4a99b7ac21ac2248faf03a7e97519f780`.
- The actual `SKILL.md` read by each executor matched its assigned source commit byte-for-byte. The package source trees contained the same three paths, and the new tree added the CRL-X02 rule plus orthogonal X01/X03 and case-note changes.
- Both fresh/no-context executors received the same natural task prompt and fixture-level `AGENTS.md`. The prompt explicitly selected `coding-review-loop` because selection efficacy was out of scope, but did not mention repository-wide scanning, entrypoint discovery, mock boundaries, replacement indirection, traces, or the paired experiment.
- `--ignore-rules` was not used. A preflight confirmed normal fixture instruction discovery, and both execution transcripts show `AGENTS.md` was loaded.
- Runs used separate fresh runtime state, the same provider/config source, sequentially reset fixture workspaces, and no shared run artifacts. Agent-issued command transcripts had no access to the repository under test control, the other run, evaluator material, or staged artifacts.
- Isolation was audited logical isolation, not filesystem-level non-visibility. Fresh contexts, snapshot-local runtime directories, sequential staging, forbidden-path command audits, and post-run artifact collection reduced contamination risk; absolute inability to read arbitrary host paths was not claimed.
- Raw bundles were held outside executor workspaces. Reviewer bundles used the same deterministic redaction: remove command events that loaded the skill text, replace run-specific runtime/workspace paths with neutral placeholders, and preserve ordinary task search, plans, edits, diff, tests, and final responses. Raw and redacted bundles were hashed before review and intentionally were not committed.

## Frozen Rubric

Acceptance-critical behavior was fixed before execution:

1. repository-wide impact discovery;
2. repository-native runnable-entrypoint discovery;
3. complete caller migration;
4. direct lookup without equivalent lambda, partial, alias, or thin-wrapper indirection;
5. verification at the real lookup/routing boundary, including the entrypoint.

Rule incorporation and traceability were diagnostic. Fixture validity, snapshot/config consistency, fresh context/runtime, artifact completeness, contamination, and X01/X03 non-interference were validity gates. Pair outcomes were frozen as `supported`, `partial support`, `no incremental signal`, `unsupported`, `regression/variance signal`, or `invalid/inconclusive`.

## Result and Attribution

An independent fresh/no-context reviewer received anonymous Run A/Run B bundles and the frozen rubric, but not the version mapping. It marked all five critical and both diagnostic items `PASS` for both runs and froze the pair result as `no incremental signal`. The reviewer found no visible contamination or artifact-completeness failure. Only after that judgment was recorded did the orchestrator unblind A as new and B as old.

Both runs:

- searched the repository and found both production callers;
- used task configuration and operations documentation to identify the maintenance entrypoint;
- removed the shared wrapper and migrated all callers to the direct named lookup;
- changed tests from permissive wrapper mocks to caller-local lookup mocks with routing assertions;
- passed all four fixture tests and the dry-run entrypoint check;
- left no stale symbol references or replacement indirection;
- produced byte-identical final patches.

The fixture therefore demonstrates that both snapshots can conform on this task. It does not show that the new rule caused an improvement. Plausible explanations include sufficient behavior from the old Focused Reuse Scan plus the base agent, or a fixture that is valid but not discriminating enough. This result neither disproves the clarification nor supports changing CRL-X02 to `improved` or `repeated`.

## Changes

- Updated the CRL-X02 current-state record in `docs/v0.3-scope.md` with the pilot link, result, evidence level, and unchanged lineage outcome.
- Added this immutable pilot report.
- Made no skill, packet, case-note, policy, ADR, evaluation, Stage 0, automation, or process-version change.

## Role Separation

### Plan Decision

The orchestrator fixed the experiment boundary, snapshots, prompt, rubric categories, validity gates, redaction, outcome vocabulary, and lineage interpretation before running the pair.

### Test Responsibility

Control-side checks established fixture validity, normal repository-instruction loading, source-snapshot differences, command-path isolation, artifact completeness, and direct fixture verification.

### Implementation Responsibility

Fresh executors changed isolated copies of the fixture only. They did not receive the hidden rubric or modify evolving-agent-dev.

### Review Check

A separate fresh reviewer judged anonymous artifacts. The orchestrator froze that judgment before revealing the old/new mapping, then verified snapshot loading and contamination from raw control artifacts.

## Verification

- Fixture preflight: four baseline unit tests passed; the documented dry-run module entrypoint printed the expected event count.
- Independent fixture-validity review: confirmed a real runnable entrypoint with two repository clues, discoverable callers, a semantically empty wrapper, a plausible permissive-mock failure, a plausible replacement-indirection temptation, no hidden evaluator knowledge, and no rubric leakage.
- Prompt identity: both runs used the same prompt; its SHA-256 was `d933007f9baba79be7d94daf7781c2e9b3636afa63ccf71166b8de264059d159`.
- Snapshot verification: repository tree comparison confirmed the removal rule is absent from `3a0f4bf` and present in `a90e366`; extracted runtime skill text matched the assigned commits byte-for-byte.
- Executor verification: each isolated run passed `python -m unittest discover -s tests -v`, the dry-run module entrypoint, stale-reference checks, and `git diff --check`.
- Control verification: reran the four-test suite and dry-run entrypoint for each collected worktree; both passed. Both forbidden-path audit outputs were empty.
- Blind review: fresh read-only review marked every critical and diagnostic item `PASS` for both anonymous runs and froze `no incremental signal`; its command audit showed no path access outside the review workspace.
- Ephemeral artifact integrity (SHA-256): raw A `0c9c8211c7dcebdfc93aab684867bb11a105fceeb70c98c2c3b4b5944a3a53c4`, raw B `04d8379453d8e3f1e0200b339bc0f71309f765c90ed7ab32acbee14d91eba356`, reviewer A `425d3ec32f14cfe5be8f2938f9f0bf7bf16f8dd97cad6653948841643eab19de`, reviewer B `c97e9d72c64c47ffbd2a11a8d2d714dda1854b2ab9d6c9922f291d442fe575a5`, and frozen review `45d9f3df5b1a872243df52d7ae708cf5c8ce7e607abbeba4f2f23f1758e525fb`. Raw artifacts remained local and temporary rather than becoming repository fixtures.
- Artifact comparison: final patches were byte-identical; each changed the same five intended files with no untracked files.
- Repository verification and privacy/boundary checks are recorded in the final task handoff after the tracked diff is complete.

## Good

- Blinding prevented the reviewer from rewarding the known-new snapshot.
- The result vocabulary preserved useful negative information without relabeling a synthetic pass as real improvement.
- The fixture and artifact protocol were executable with lightweight local tools; no telemetry, database, background job, or permanent benchmark system was needed.

## Friction

- What happened: The valid fixture did not discriminate between snapshots; the old snapshot independently performed the target repository-wide scan and full migration.
- Why it felt wrong: A successful pair run produced no causal signal about the new rule, despite both implementations being correct.
- Impact: The pilot cannot justify an effectiveness claim or a skill edit. Repeating the same fixture would add cost without information.
- Category: `process` / `testing`.
- Root cause guess: Existing general guidance and base-agent behavior were enough for the visible repository clues, so the fixture tested conformance more strongly than incremental rule value.

## Proposed Follow-up

- Do not change the skill from this result and do not rerun the unchanged fixture.
- Keep CRL-X02 `awaiting evidence`; seek one known-version real task, or at most one redesigned paired fixture whose discriminating opportunity is independently validated without making discovery depend on evaluator-only knowledge.
- Before a redesigned fixture, decide whether the removal line is intended mainly as low-cost clarification. If so, lack of synthetic incremental signal may be acceptable and natural evidence should take priority over benchmark escalation.
- Policy note candidate: no.
- Casebook candidate: no.
- ADR needed? no; the pilot applies already-approved experimental boundaries.
- Formal evaluation candidate? not promoted; one non-discriminating synthetic fixture is insufficient.
