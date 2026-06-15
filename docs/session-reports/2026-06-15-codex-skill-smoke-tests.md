# Session Report: Codex Skill Smoke Tests

## Goal

Run the four v0.1 smoke tests for the locally installed `evolving-agent-process` Codex skill.

## Evidence Status

- Dogfood: yes.
- Counts as Stage 0 real task: no.
- Reason: this was skill smoke testing. Smoke Test C produced a Stage 0 real task candidate separately in `docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md`, but this summary report is test harness evidence, not an additional real task.

## Changes

- Ran Smoke Test A: review-only process review, no edits.
- Ran Smoke Test B: discussion-only with explicit friction recording, updated `docs/casebook/inbox.md` only.
- Ran Smoke Test C: edit task, updated `docs/policies/testing-policy.md` and created `docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md`.
- Ran Smoke Test D: seed evidence judgment, no edits.

## Verification

```bash
<codex-binary> exec --dangerously-bypass-approvals-and-sandbox -C <repo> -o /tmp/... "Use the evolving-agent-process skill. Review docs/process-v0.2.md for consistency issues only. Do not edit files."
```

Result: passed. Codex loaded the skill, reviewed `docs/process-v0.2.md`, returned findings, and `git status --short` stayed clean.

```bash
<codex-binary> exec --dangerously-bypass-approvals-and-sandbox -C <repo> -o /tmp/... "Use the evolving-agent-process skill. Discussion only: the skill install flow feels unclear. Record this as one micro friction item in docs/casebook/inbox.md only; do not create a session report."
```

Result: passed. Codex updated only `docs/casebook/inbox.md`; no session report was created. The change was committed as `6adce6f`.

```bash
<codex-binary> exec --dangerously-bypass-approvals-and-sandbox -C <repo> -o /tmp/... "Use the evolving-agent-process skill. Smoke Test C edit task: make a small substantive docs change in docs/policies/testing-policy.md by adding one sentence clarifying that implementation-detail tests require a stated requirement. Verify the change and write a minimal session report. The report must state dogfood status and Stage 0 evidence status."
```

Result: passed. Codex updated `docs/policies/testing-policy.md`, created `docs/session-reports/2026-06-15-smoke-test-c-testing-policy.md`, recorded dogfood and Stage 0 evidence status, and verified with `rg`, `git diff --check`, `git diff`, and `sed`. The change was committed as `a391c7d`.

```bash
<codex-binary> exec --dangerously-bypass-approvals-and-sandbox -C <repo> -o /tmp/... "Use the evolving-agent-process skill. Smoke Test D: Do existing seed casebook entries and draft evaluations satisfy Stage 0 exit criteria? Answer only; do not edit files."
```

Result: passed. Codex answered no, cited seed-vs-real evidence, and `git status --short` stayed clean.

## Good

- The installed skill loaded from the symlinked directory and Codex followed the intended task distinctions.
- Review-only and seed-evidence tasks did not write files.
- Discussion-only with explicit friction wrote only the requested inbox artifact.
- Edit task produced a minimal session report and did not expand into casebook, ADR, or evaluation.

## Friction

### Codex workspace sandbox failed before smoke testing

- What happened: The first Smoke Test A attempt with `-s workspace-write` failed before any command could run: `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`.
- Why it felt wrong: Smoke tests need to exercise normal Codex behavior, but the local sandbox could not initialize in this environment.
- Impact: Smoke tests had to be rerun with `--dangerously-bypass-approvals-and-sandbox`, so the smoke result validates skill behavior but not sandboxed execution.
- Category: `tooling`
- Root cause guess: Codex's Linux sandbox requires user namespace/network setup that is unavailable in this runtime.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: not yet; track if Codex sandbox failures recur.
- ADR needed? no.
- Evaluation candidate? no.
- Next: choose the first real low-risk dogfood task. Smoke Test C can be considered one Stage 0 real task candidate if accepted after review.
