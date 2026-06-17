# Case 0005: Planning Impact Analysis Gaps

## Status

Open

## Evidence Type

`real external friction` - repeated privacy-preserving observations from external private code projects. This is not an accepted internal Stage 0 dogfood task and not an evaluation candidate.

## Category

- process / planning impact analysis
- requirements / retention semantics
- requirements / contract boundary
- context / internal consumer impact
- context / missed tool capability
- testing / behavior-level regression gap
- testing / contract regression coverage
- process / cross-artifact consistency

## Privacy Boundary

This case omits private repository names, local absolute paths, private commit hashes, private code contents, user identifiers, exact tool names, exact dates, and sensitive operational details. Evidence is recorded only as behavior-level planning and verification patterns.

## Scenario

A planning task can acknowledge uncertainty but still miss the impact of source-location accuracy, tool capability boundaries, runtime semantics, downstream callers, reusable shared logic, contract boundaries, authoritative specs/runbooks, and behavior-level performance verification.

## Observed Behavior

Three external planning reviews showed a repeated planning-impact pattern:

- A performance-oriented plan noted that real profiling and a current timing baseline were still needed, but human review found missed source-location accuracy, user-visible metadata semantics, downstream batch/scoring callers, reuse of shared aggregation logic, and real indexed-query verification.
- A tool-selection repair plan for overlapping log-query capabilities initially considered only the recent-window capability for an out-of-window lookup. Later review found premature assumptions about recent-window semantics before clarifying the rolling-hour window, overreliance on prompt/tool descriptions, lack of a runtime guard for wrong capability use, weak prompt/schema-oriented tests, missed linked tool docs and metadata artifacts, a rejected calendar-day boundary check after rolling-window semantics were clarified, and remaining lack of real LLM tool-selection dogfood.
- An API-contract simplification plan adapted after learning the interfaces were pre-adoption, but still conflated public payload cleanup with the internal rich computation contract. Later review found that the safer plan would preserve internal machine-readable facts behind a dedicated public serializer unless internal consumers were explicitly migrated, and would update or supersede authoritative specs/runbooks that still described old output fields or export contracts.

## Why It Feels Wrong

The agent can produce a plausible plan that names uncertainty but still fails to turn that uncertainty into concrete impact checks, linked-artifact searches, behavior-level tests, or runtime verification requirements.

## Impact

- Plans may point to the wrong implementation or setup location.
- Visible debug or metadata semantics can change without being called out.
- Downstream callers can be missed when a hot path changes.
- Existing shared builders or aggregation logic can be duplicated.
- Prompt/schema tests can pass without proving behavior-level regressions or real indexed/tool-selection behavior.
- Documentation, runtime schema visibility, and metadata can drift around tool capability boundaries.
- Public-facing payload simplification can accidentally become an internal contract migration.
- Specs or runbooks can keep describing obsolete fields or export contracts after implementation changes.

## Root Cause Guess

The recurring issue is incomplete planning impact analysis: the agent treats descriptions and local code paths as enough, instead of explicitly checking semantics, linked callers, existing shared logic, runtime guards, behavior-level regression tests, and real environment verification paths. For retention-sensitive tool selection, the plan should clarify calendar-day vs rolling-hour window semantics, data-source retention, start-time vs full-window rules, and boundary splitting.

## Current Handling

Keep this as privacy-preserving casebook evidence. Do not count external planning observations as accepted internal Stage 0 dogfood tasks. Do not create E008 until the pattern has a judgeable, reproducible fixture that can evaluate planning impact analysis without private project details.

## Related Documents

- `docs/casebook/inbox.md`
