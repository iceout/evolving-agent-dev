# Session Report: CLI Review Context Validation and Fallback

## Goal

First commit the previously reviewed external-evidence record, then test CLI
conversation separation and, if supported, add the user-requested automatic
review fallback to existing orchestration guidance.

The earlier evidence record was committed separately as `3abb5f3`; the worktree
was clean before this validation. This task is capability validation and a
user-authorized guidance change, not external evidence promotion or Stage 0
evidence. Existing CRL-X01-X07 states and historical reports remain unchanged.
Skills used: `evolving-agent-process`, `openai-docs`, and `skill-creator`.

## Test Boundary

The question is whether a new `codex review` session automatically inherits
messages from an existing CLI conversation. It is not whether all model inputs,
configuration, memory, hooks, or accessible files are isolated.

The probe used Codex CLI 0.153.4 with the existing provider configuration and
no model override, in a fresh temporary Git repository with no task files.
All four prompts prohibited tools and file/history reads. CLI initialization
and session persistence were authorized outside the parent filesystem sandbox;
the agent's execution sandbox remained read-only. Seeded session persistence
was necessary for the explicit resume control. No external project was used.

The acceptance conditions were frozen in the temporary probe runner before
execution: seed acknowledgment; exact marker recovery on resume; `NONE` in a
new review; exact marker recovery when supplied to a new review; unchanged
seed identity on resume; distinct new-review identity; no observed tool calls;
and an unchanged temporary worktree. No missing result counted as a pass.

## Prompts and Commands

The randomly generated, non-sensitive marker was
`CLI-CONTEXT-ad5c6aa4574b4b7accc460321bcc876a`.

Seed prompt, passed to `codex exec --json --sandbox read-only -`:

```text
This is a context-boundary test. PROBE_TOKEN=CLI-CONTEXT-ad5c6aa4574b4b7accc460321bcc876a. Keep this value in this conversation. Do not use tools or inspect files. Reply exactly READY.
```

The same query was passed to the explicit resumed-session control and the
fresh review. Its SHA-256 is
`717737c3dde4633be08c67e397a8096f67a4562ff1f390a510c25f12080a8a36`:

```text
Read-only context-boundary probe. Do not use tools, inspect files, search, or read session history. From conversation messages already available to you, report the exact value of PROBE_TOKEN if present; otherwise report NONE. Do not guess. Output exactly one line: probe_token: <value>.
```

The control resumed the exact seed session with
`codex exec resume --json -c 'sandbox_mode="read-only"' <seed-session> -`.
The fresh review used `codex review -c 'sandbox_mode="read-only"' -`, without
resume, fork, session identifier, or supplied transcript. A second fresh review
used the same command and query, preceded by exactly
`PROBE_TOKEN=CLI-CONTEXT-ad5c6aa4574b4b7accc460321bcc876a` and a newline.
This last control checks that the review surface can report the marker when it
is actually supplied, rather than returning `NONE` unconditionally.

## Observed Results

| Run | Final answer | Conversation identity | Observed tool use |
|---|---|---|---|
| Seed | `READY` | New seed session | None |
| Resumed control | `probe_token: CLI-CONTEXT-ad5c6aa4574b4b7accc460321bcc876a` | Same seed session | None |
| Fresh review | `probe_token: NONE` | Different new session | None |
| Supplied-marker review control | `probe_token: CLI-CONTEXT-ad5c6aa4574b4b7accc460321bcc876a` | Another new session | None |

All four processes exited 0 and all eight predeclared assertions passed.
The seed/resume JSONL contained only thread/turn and agent-message events,
with no command, file-change, MCP, or web item. Review stderr showed read-only
sandbox headers and no tool execution headers. The temporary repository stayed
clean. Complete raw stdout/stderr and the temporary runner were retained
locally for this task's review; they are not a new repository harness or ledger.

Fresh-review stdout SHA-256:
`4a82726f79b21b8facb2fbbcd27f419bc7b93a940215173391507c48ba4efc1d`.
Supplied-marker review stdout SHA-256:
`1b1b94c3bba868bd9b7bb6ecc851a392a1a1776d39c05b1ec231148da6cb8023`.

## Interpretation and Decision

The resumed control proves the marker was available in prior conversation
history; the supplied-marker control proves the review query is sensitive to
visible input. The new review's absence result and distinct session identity
therefore support non-inheritance of this existing CLI conversation under the
tested configuration. This is stronger than the earlier negative-only CLI
self-report, whose historical inconclusive result is preserved.

This evidence supports the narrow operational review boundary when a new CLI
process receives only permitted source/repository/diff/rubric inputs, with no
parent transcript, Card, resume/fork, or history-reading instruction. It does
not audit the complete model request or prove separation from every possible
parent context, global memory/configuration injection, filesystem visibility,
model/evidence independence, or reviewer correctness. The no-tools constraint
applies to the probe; real reviewers may read the permitted evidence files.

Per the user's conditional authorization, accept a reviewer-start fallback to
this validated new-session CLI surface. A thread-limit error is an execution
failure on one surface, not evidence that all reviewers are unavailable.
Automatically try the applicable alternative within scope, while respecting
platform permissions. Do not use it to retry substantive findings, replace
analysis, broaden evidence routes, or reset correction/re-review limits.

This task does not claim skill effectiveness, reduced user effort, or new
external evidence outcomes. The preceding CLI content review demonstrated
execution on real documents; this controlled probe addresses a narrower
conversation boundary, not an end-to-end effectiveness evaluation.

## Changes

- `skills/evolving-agent-process/SKILL.md`: route reviewer-start failures to
  the validated CLI fallback in the existing reference.
- `skills/evolving-agent-process/references/external-evidence-distillation-orchestration.md`:
  define the bounded CLI fallback, allowed inputs, read-only execution,
  capability/capacity distinction, and unchanged stop/correction constraints.
- `docs/decisions/ADR-0002-external-evidence-distillation-orchestration.md`:
  align condition 7 and current capability evidence with the user-authorized
  fallback, retaining the prior probe's historical limitations.
- This report: controlled evidence, decision boundary, and verification.

The change has four allowed files. No new agent framework, persistent probe
script, dependency, runtime installation, external-project change, or additional
commit is included. The existing runtime symlink exposes tracked guidance;
no separate installation or copy is performed.

## Verification

- Controlled probe: all four runs and eight assertions passed; raw event/log
  readback confirmed the observed results and tool-use limits above.
- Local help and official CLI reference confirmed custom prompts are mutually
  exclusive with `--uncommitted`, `--base`, and `--commit`; the fallback uses
  custom stdin instructions that explicitly cover the required worktree layers.
- Canonical `skill-creator/scripts/quick_validate.py` on the complete
  `skills/evolving-agent-process` package returned `Skill is valid!`; no
  dependency installation was needed.
- Full diff/new-report readback, `git diff --check`, and separate new-report
  whitespace checking passed. The latter emitted no warnings and exited 1
  solely because the new file differs from `/dev/null`.
- Exact four-file scope, empty staging, local links, probe/report trace, and
  stale direct-only capability wording checks passed. Lineage/Stage 0 state,
  the prior capability report, and the committed external record stayed
  byte-identical. The reference uses a repository-root evidence path so a copied
  skill does not depend on an installation-relative link outside its package.
- Independent read-only CLI review exited 0 after reading all four changed
  files, the complete report, and raw probe inputs/outputs. It returned no
  findings and confirmed that controls support the narrow stated boundary and
  that permissions, input separation, substantive-finding handling, correction
  caps, and outcome limits remain intact. This final documentary update records
  that result without changing guidance or the experimental interpretation.

## Good

Positive controls distinguish lack of inherited conversation from an insensitive
query. Capacity failure and context capability now have separate evidence.

## Friction

Earlier collaboration thread exhaustion was generalized too broadly until the
user suggested CLI review. The new fallback addresses that execution gap without
claiming stronger isolation than the controlled observation supports.

## Proposed Follow-up

Use the validated fallback on future eligible reviewer-start failures, preserving
the same rubric and limits. Revalidate if the relevant CLI surface/configuration
or context semantics materially change. Do not retrofit historical records into
known-version effectiveness evidence, and do not commit these guidance changes
without a separate user request.
