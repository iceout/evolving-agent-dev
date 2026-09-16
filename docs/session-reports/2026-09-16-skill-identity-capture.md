# Session Report: Task-Time Skill Identity Capture

## Goal

Connect the existing package fingerprint to actual `coding-review-loop` use
and triggered case capture so future cases need not repeatedly lack version
information. The user authorized implementation after investigation identified
the gap. This is a skill/tooling edit, not conditional record-only distillation.

Status: evolving-agent-process dogfood, post-Stage 0 implementation evidence.
Skills used: evolving-agent-process and skill-creator. No external source note
is edited or backfilled; no CRL lineage outcome or Stage 0 count changes.

## Root Cause And Decision

The existing inspection command could identify package content, but ordinary
cases explicitly allowed omitting the version and first use did not acquire
one. Thus a current installed package could still produce an unversioned note.
Default inspection also looked only under the configured Codex directory,
while the observed skill was linked under the agent skills directory. Explicit
inspection of that actual location matched repository content; installation
drift was not the cause of missing historical attribution.

Use the existing `sha256-v1` content identity, including references, rather
than introduce a manually maintained release number. Acquire it at first use
from the actual skill directory, retain it in task context, read guidance from
that directory, and check again at triggered case capture. A new case requires
the receipt or a concrete acquisition/attribution limitation. Changes during
the task, late snapshots, and lost start receipts remain explicit uncertainty.

## Changes

- `skills/coding-review-loop/scripts/skill_identity.py`: package-local,
  standard-library, read-only CLI; works with copies and symlinks and prints
  identity/status without private paths. It contains the existing fingerprint
  implementation, which the installer reuses instead of duplicating.
- `skills/coding-review-loop/SKILL.md` and `references/case-note-shape.md`:
  first-use acquisition, capture-time comparison, required identity field,
  change/late/failure handling, and continuity through existing handoffs.
- `scripts/install-skill.py`: read-only inspection discovers existing configured,
  agent, and legacy Codex installation locations, reporting multiple locations
  separately. An explicit runtime root and installation destinations retain
  their previous semantics. No location is asserted to be the loaded one.
- `tests/test_install_skill.py`: regression checks for discovery, multiple
  copies, explicit overrides, unchanged install defaults, and standalone
  package identity/change detection without repository access or new files.
- `README.md` and `docs/skill-design/local-evidence-ledger.md`: synchronize
  acquisition, persistence, inspection, and attribution semantics.
- This report records the implementation and its limits.

Other skills retain their current capture behavior. No dependency, runtime
installation, telemetry, usage ledger, policy, evaluation, new lineage, or
process version is introduced. The existing runtime symlink exposes the
updated package without a separate installation step.

## Role Separation

- Plan decision: fix acquisition and capture at the source, preserving case
  triggers, privacy boundaries, historical uncertainty, and designation rules.
- Test responsibility: exercise observable CLI behavior and content changes,
  including copied packages; do not equate an identity with rule execution.
- Implementation responsibility: share the existing fingerprint algorithm and
  extend current guidance and artifacts within the eight-file allowlist.
- Review check: parent reviews the complete diff and new files; a separate
  no-turn subagent exercises the skill in a temporary copy without changing
  repository files. This is bounded forward-testing, not a CRL efficacy pilot.

## Verification

- `python3 -B -m unittest discover -s tests -v`: all 11 tests passed, none
  skipped. Existing fingerprint, link, permission, and preservation checks
  remain covered alongside the new acquisition/discovery cases.
- Canonical skill-creator `quick_validate.py` on `skills/coding-review-loop`:
  `Skill is valid!`; no dependency installation required.
- Default `python3 -B scripts/install-skill.py --inspect coding-review-loop`
  discovers the actual agent skills location and reports `matches repository`.
  Running the installed package's identity helper returns the same fingerprint.
- Independent forward test: a temporary copied skill produced equal start/end
  fingerprints, then a different end fingerprint after a reference edit. The
  example changed-version case retained both identities; the resumed-task case
  marked the missing start receipt and current-only observation explicitly.
  The no-trigger case produced no case/log/index. The child reported no concrete
  failure; temporary test resources were cleaned up. These are controlled
  implementation checks, not natural real-task effectiveness observations.
- Complete diff/new-file review, `git diff --check`, new-file whitespace checks,
  linked-file checks, and the eight-file allowlist check passed. Negative search
  found no obsolete optional-version or omit-field guidance in the changed
  current documents. Historical reports and all lineage states are unchanged.

## Good

Version identity is acquired by the agent during use and travels with a case
only when capture is warranted. Copies work without a central checkout, and
the installer and skill use one fingerprint algorithm.

## Friction

The previous implementation exposed identity through an optional inspection
tool without connecting it to ordinary task capture. The permissive case field
and single-directory inspection left a repeatable process/tooling gap. This
report records that existing gap and its authorized repair; it is not another
independent external evidence batch.

## Limits And Follow-Up

Hashing is not atomic and does not attest to model loading or execution.
Matching snapshots plus contemporaneous reading support task-local attribution;
visible concurrent edits or uncertain loading remain inconclusive. Agents must
execute the instructions; this is not a runtime-enforced hook. Real future use
must still show whether receipts survive handoffs and appear in triggered
cases. Acquiring a fingerprint does not designate an observation, establish a
comparable failure opportunity, or promote a skill outcome. Historical tasks
without contemporaneous receipts remain unknown.

Leave all changes uncommitted. No external operation or further permission is
required to inspect the reviewable result.
