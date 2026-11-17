# Session Report: On-Demand Skill Identity

## Goal

Implement the user-authorized D4 identity change under principle 11: remove
default fingerprint collection, keep a usable audit command and honest source
attribution. Mode: evolving-agent-process dogfood, post-Stage 0. Skills used:
evolving-agent-process and skill-creator. No effectiveness claim or CRL outcome
change follows from this maintenance decision.

## Changes and Trade-off

- `SKILL.md` now invokes the existing helper only for a requested version audit
  or a designated observation needing local attribution. Ordinary tasks and
  friction capture may omit collection and record `unknown - not collected`.
- A current-state audit uses a current snapshot. An observation relying on a
  local task-start version still collects before planning/implementation, reads
  from that package and compares at capture. Authority-supplied versions retain
  their separate attribution basis. Late/lost receipts, drift and failed
  acquisition remain explicit limitations; history cannot backfill loading.
- Updated case-note guidance, README and local-evidence-ledger so none silently
  reintroduces mandatory collection. Updated v0.4 diagnosis/current state and
  the completed identity portion of D4; other D4 proposals remain open.
- Accepted trade-off: fewer ordinary cases will have fingerprints, reducing
  later known-version comparability. Their factual friction still transfers.
  Git can restore the guidance if this trade-off proves unacceptable.

The helper, installer, capture triggers, independent designation requirements,
privacy rules and final capture-status requirement are unchanged. D5 prose
relocation is deferred. No installation command was run; the existing runtime
symlink points to the tracked package, so its guidance reflects these edits
without a separate installation. No historical evidence is rewritten.

## Verification

- `python3 -B -m unittest discover -s tests -p test_install_skill.py`: all 11
  tests passed. This covers existing inspection, standalone copied-package
  identity, deterministic receipts and reference-drift detection.
- Reviewed ordinary-task, ordinary-friction, authority-version, local designated
  observation and late/current-only audit paths across the changed guidance.
  Ordinary cases need no helper; known-version claims still need attribution.
  This is a document consistency review, not an execution/effectiveness trial.
- Read the complete diff and new report; checked relative links, old mandatory
  wording, unchanged helper/installer bytes, frontmatter and whitespace/EOFs.
  `git diff --check` passed. Frozen D1 inputs and v0.3 lineage states are unchanged.

### Verification Failure

Canonical skill-creator `quick_validate.py skills/coding-review-loop` could not
start: the current Python lacks `yaml` (`ModuleNotFoundError`). No dependencies
were installed. Alternative checks confirm unchanged frontmatter bytes/name/
description, existing packaged references and absence of unfinished placeholders.
These checks are not a canonical validator pass. Remaining risk is limited to
checks the unavailable validator would perform; the narrow guidance edit and
11 passing existing tests are sufficient to submit for review.

## Role Separation

- Plan decision: remove routine collection while preserving audit attribution.
- Test responsibility: existing tool behavior and cross-document consistency.
- Implementation responsibility: guidance only, without D5 or helper changes.
- Review check: user review is the next checkpoint; no independent forward
  test or behavioral benefit is claimed.

## Friction and Follow-up

The case template and ledger carried the old mandatory requirement as well as
the skill entry point; changing only the entry point would leave a contradiction.
No new ledger, ADR, evaluation, runtime installation or commit was added.
Stop for review before considering the separate D5 simplification.
