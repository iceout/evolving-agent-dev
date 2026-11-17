# Session Report: Rule Maintenance as Engineering

## Goal

Record the user-approved principle that prompt and process rule maintenance is
ordinary engineering work, not an effectiveness claim. Mode: evolving-agent-process
dogfood, post-Stage 0. This documentation change is not effectiveness evidence.

## Changes

- Added principle 11: maintainer review, risk-proportionate verification and a
  recovery path suffice for rule maintenance without prior A/B evidence.
- Clarified principle 9 so evaluation supports behavior hypotheses and claims
  without becoming a prerequisite for every maintenance change.
- Updated v0.4 D1/D2/D5 and backlog dependencies: experiments are optional
  diagnostic tools; D-4 and D3/D4/D5 maintenance need not wait for them.
  Individual implementations still require an authorized scope.
- Linked the closed first pilot. Its frozen rubric, criteria, verdicts and
  evidence remain unchanged; its retirement restriction still applies to
  claims based on that experiment.

## Verification

Read the full changed-file diff and this report. Checked Markdown file links
and the new principle anchor, whitespace and EOFs, and ran `git diff --check`.
Searched the scope note for the former mandatory D1 sequencing and the
principles for the unconditional evaluation requirement; neither remains.
No runtime package changed, so no skill validation or A/B run was needed.

## Good

Review can accept either equivalent behavior or an explicit behavior change;
missing effectiveness evidence no longer implies retaining every rule.

## Friction

The former evaluation principle and v0.4 ordering could turn evidence standards
for claims into prerequisites for reversible maintenance. The linked wording
was corrected together to avoid preserving that conflict.

## Proposed Follow-up

Select a bounded maintenance change separately. No canonical skill, policy
status, CRL outcome or frozen experimental result changed. No ADR or evaluation
artifact is needed for this principle clarification; no commit was requested.
