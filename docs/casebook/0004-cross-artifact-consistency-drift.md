# Case 0004: Cross-Artifact Consistency Drift

## Status

Open

## Evidence Type

`real external/internal friction` - repeated observations from privacy-preserving external pilots and internal stale verification evidence. This is not an accepted internal Stage 0 dogfood task. It supports E007 as an accepted privacy-preserving real-evidence evaluation candidate.

## Category

- process / cross-artifact consistency

## Privacy Boundary

This case intentionally omits private repository names, local absolute paths, commit hashes, private file contents, and sensitive deployment paths. The external pilot evidence below is recorded only at the artifact-type and behavior level.

## Scenario

Documentation and configuration artifacts can drift when the same deployment or runtime path assumption is repeated across multiple files instead of being updated from one coherent source of truth.

## Observed Behavior

Two external real-code pilots exposed cross-artifact consistency drift:

- An external pilot found the same runtime path scattered across a template and multiple docs. The agent fixed the drift and routed the observation back as friction evidence only.
- A private external pilot found deployment-specific path assumptions spread across runtime data layout documentation, download security documentation, and a settings template. No active runtime code changed.

The private pilot also found stale documentation: a download/security doc described old static-file configuration behavior while current code used a different configuration approach.

A later privacy-preserving README/onboarding review found a related config-template semantics gap: the README told users to copy and edit the settings file, but documented only runtime path settings while the template also contained operational/deployment-specific values such as instance identity, notification endpoint, and external config path. The same review found clean points too: no fixed deployment path issue remained in README, the run command matched current server behavior, the test command matched declared dependencies, and the README documented copying a local settings file before tests.

Internal stale-verification evidence showed a related maintenance pattern: `docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md` contained a verification command that became stale after tracker bookkeeping changed the current friction count, requiring a follow-up correction to keep the report reproducible at HEAD.

## Verification Friction Observed

The private pilot had tests, and docs referenced `pytest`, but `pytest` was unavailable and not declared in the project dependency file. Verification still included searching for old hard-coded paths, checking configurable path docs, Python doc assertions, `git diff --check`, syntax parse checks, and an attempted `pytest` run blocked by the missing dependency.

## Why It Feels Wrong

The agent can make a locally correct edit while leaving sibling docs, templates, or verification snippets stale. That makes future readers trust outdated deployment assumptions or non-reproducible verification instructions.

## Impact

- Deployment instructions can contradict templates or current configuration behavior.
- Security or download documentation can describe obsolete behavior.
- Verification becomes less trustworthy when commands rely on undeclared dependencies.
- External pilot evidence must be sanitized before being recorded in a potentially public process repo.

## Root Cause Guess

The recurring issue is not one file being wrong; it is that related docs, templates, and verification commands are coupled but easy to update independently. Agents need to search for sibling artifacts and stale references when changing deployment/configuration assumptions.

## Current Handling

Keep this as casebook evidence and accepted E007 candidate evidence. Do not count the external pilots as accepted internal Stage 0 dogfood tasks under the current tracker rules. E007 counts as an accepted real-evidence evaluation candidate after tracker acceptance.

## Related Documents

- `docs/casebook/inbox.md`
- `docs/session-reports/2026-06-16-cross-artifact-consistency-casebook.md`
- `docs/session-reports/2026-06-16-stage0-exit-blocker-summary.md`
- `docs/stage0-progress.md`
