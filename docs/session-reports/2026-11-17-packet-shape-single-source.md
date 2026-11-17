# Session Report: Packet Shape Single Source

## Goal

Complete v0.4 backlog item 1 using the user-approved pointer-only option.
Mode: evolving-agent-process dogfood, post-Stage 0. This is documentation
maintenance, not effectiveness evidence; no CRL outcome changes.

## Changes

- Replaced `docs/v0.3-review-packet-shape.md` with a compatibility pointer to
  `skills/coding-review-loop/references/review-packet-shape.md`, the sole
  maintained packet shape. Keep future field edits in that reference.
- Updated v0.4 D-4 and backlog item 1 to distinguish historical duplication from
  current state. The separate oversized-inline-guidance concern remains open.
- Preserved existing skill instructions and historical reports. The active
  process-skill consumer continues through the stable repository entry point.
  No skill package or runtime installation changed.

## Verification

- Read both full templates before replacement. All 13 legacy Shape sections
  have corresponding sections in the canonical reference; common minimum
  content and conditional section guidance are also present. The reference
  additionally contains the five specialized sections and explicit conditional
  mutation/recovery and target-context exclusions.
- Checked Implementation Trace specifically: the reference delegates to one
  evolving Requirement Traceability Checklist, retains planned versus actual
  results and cross-artifact checks, and forbids a duplicate table. This covers
  the old requirement/artifact/verification/cross-artifact chain.
- Searched repository references to both paths. No legacy heading-anchor
  consumers were found. The active process-skill instruction still names the
  preserved path; following its Markdown pointer reaches the existing reference.
- Checked the pointer contains no section templates, local Markdown links
  resolve, the canonical reference and process skill are unchanged, and v0.4
  no longer describes the two files as currently divergent maintained copies.
- Read the final diff and this new report; checked whitespace and EOFs,
  including the untracked report, and ran `git diff --check`.

## Good

One maintained source removes a known divergence path while preserving existing
file-path consumers. Git history retains the old template for recovery.

## Friction

The reference is framed for real code projects and contains additional
conditional checks. Process consumers now reach that same reference through
the pointer; this consolidates guidance rather than claiming byte-equivalent
templates. Its existing applicability rules remain in the sole source.

## Proposed Follow-up

No A/B experiment or new consistency automation is needed for this bounded
change. Future packet-field changes belong in the canonical reference.
No ADR, evaluation promotion, skill installation or commit was requested.
