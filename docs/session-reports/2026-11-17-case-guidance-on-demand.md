# Session Report: Case Guidance on Demand

## Goal

Implement the authorized first D5 slice: move low-frequency audit and designated
observation procedures into the existing case-note reference. Mode:
evolving-agent-process dogfood, post-Stage 0. Skills: evolving-agent-process and
skill-creator. This is guidance maintenance, not effectiveness evidence.

## Changes

- Removed the leading identity audit section from `SKILL.md` and shortened
  Case Note Capture to triggers, routing, placement, privacy and final status.
- Moved all three audit paragraphs and all three designated-observation
  paragraphs verbatim into `references/case-note-shape.md`. Its introduction
  now explicitly supports audits without requiring a note; the version field
  delegates procedural detail to the local audit section rather than repeating it.
- The main entry still requires reading the reference before a designated
  observation, so task-start collection is discoverable before execution.
  Ordinary tasks and friction cases still need no fingerprint. No-trigger
  tasks still create no note, index or usage record.
- Recorded only this completed D5 slice in v0.4. Broader skill merging and other
  D5 work remain separate. Core planning, root-cause, reuse, implementation trace
  and review guidance are byte-identical to the prior version.

The main file shrank from 136 to 116 lines and by about 28% in UTF-8 bytes.
This measures entry-point size, not proven attention savings. Details remain
available on demand. The helper, installer and capture/attribution boundaries
are unchanged. Git history provides recovery. The existing runtime symlink
exposes these edits without a separate installation command.

## Verification

- Compared old/new sections: exact paragraph migration, unchanged core sections
  and frontmatter; checked ordinary/no-trigger tasks, ordinary friction,
  independently designated observations and audit-only navigation paths.
- `python3 -B -m unittest discover -s tests -p test_install_skill.py`: 11/11
  passed, including standalone audit and reference-drift behavior.
- Read the complete diff and this report; checked packaged references, local
  links, EOF/whitespace, v0.4 status and absence of the old capture-only reference
  loading instruction. `git diff --check` passed.

### Verification Failure

Skill-creator `quick_validate.py skills/coding-review-loop` again could not start
because Python lacks `yaml` (`ModuleNotFoundError`). No dependency was installed.
Alternative checks cover unchanged frontmatter, name/description, reference
existence and unfinished placeholders; they are not the canonical validator.
That unavailable check remains a limitation, but the migration checks and
existing tests support submitting this bounded edit for review.

## Friction and Review Boundary

Keeping the old reference-loading instruction would defer task-start audit
instructions until capture, too late for designated observations. Routing now
explicitly covers the pre-execution and audit-only paths.

No A/B run, historical evidence change, new ledger or effectiveness claim.
No commit requested. Stop for user review; no further D5 changes in this batch.
