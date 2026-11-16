# Session Report: D1 Minimum-Cut Stage 1

## Goal and Review Boundary

Complete a reviewable first experiment stage after the user rejected stopping at
preparation. Stage 1 and first-pass blind judging are complete: 12 agent runs,
one A/B pair for F1, F3, F4, F6, F9 and C1. The user-provided independent review
was received on 2026-11-17; this pilot is now closed at Stage 1. No Stage 2/3,
expansion, rule edit, demotion or retirement is authorized by these results.

Mode: evolving-agent-process dogfood, post-Stage 0. This is synthetic screening,
not real-task effectiveness or Stage 0 evidence. No CRL outcome changed. See the
[preparation checkpoint](2026-11-16-d1-min-cut-preparation.md) for construction
and initial isolated tests.

## Result

No aggregate pass/fail A/B difference was observed. C1 passed in both conditions.
F4 also passed in both: sensitivity is unestablished and this pilot cannot be
used to retire guidance. F1's identical failures mask a qualitative difference
that exposes a rubric concern; the reviewed frozen failures remain unchanged.

| Fixture | A | B | Interpretation at this checkpoint |
|---|---|---|---|
| C1 | pass | pass | Screen control satisfied; not a guidance classification |
| F1 | fail | fail | No escalation under the frozen mapping; review criterion fit |
| F3 | pass | pass | Screen-only; confirmation eligible, not internalized |
| F4 | pass | pass | Screen-only; no sensitivity established, no retirement use |
| F6 | pass | pass | Screen-only; both diagnosed before editing |
| F9 | pass | pass | Reference probe only; both changed the actual CLI default |

All 12 post-run test suites passed, totaling 47 tests. Passing those tests does
not override the guidance rubric: F1 fails on test design despite green tests.
There are no confirmed `internalized`, `load-bearing` or `harmful` items. Four
guidance pairs remain unconfirmed and F1 is inconclusive under the literal
criteria; this is not a measured post-confirmation inconclusive rate.

## What Ran

- Model: `gpt-6.1-sol`, requested and response-reported effort `medium`.
- Harness: one temporary standard-library Responses API driver outside the
  repository. Model HTTPS runs in the parent. The sole declared tool is `exec`;
  every command runs in fresh bubblewrap mount/PID/network namespaces with only
  its neutral workload writable at `/work`, empty HOME and cleared environment.
- No skill package, automatic discovery, memory tool, session resume, previous
  response ID, host home or credential file is available to the executing tool.
  There are no model-accessible host tools. Server-internal instructions remain
  unobservable; the API envelope and supplied base instructions are held fixed.
- A receives an empty guidance body; B receives the previously registered
  verbatim excerpts. Source commit is `b8da3a3`; exact current pilot amendment,
  fixtures, source ranges, messages, criteria, model settings and driver are
  captured in the local freeze. This is a minimal API harness, not native Codex
  skill activation or a whole-package experiment.
- C1 was judged before releasing the other fixtures. Three agent requests were
  allowed concurrently across independent work directories. No completed task
  or completed tool was replayed to select a preferred outcome.
- Judges used fresh independent requests of the same model/effort with no tools,
  no executing-session history, no treatment message and no condition mapping.
  They received criterion, before/after files, diff, final response, ordered
  observable trace and post-run tests. Remaining packet order was randomized.
  These are model judgments. The subsequent user-provided independent review
  confirmed all 12 literal verdicts; its statement does not establish a separate
  condition-blind human judging protocol. The main agent's evidence audit was
  not blind.

## Cell Record

Each row is one scored agent run; all are repeat 1. IDs locate the corresponding
`judge/<id>/artifact.json` and `verdict.json`, and the private raw trace/delivery
record in the external experiment directory. Fixture F1 maps to items
`D1-F1-1` and `D1-F1-2`; F3 to `D1-F3-1` and `D1-F3-2`; F4, F6, F9 and
C1 each map to `D1-<fixture>-1`. Exact source hashes remain in the frozen
`item-registry.json`; the table below is a compact view, not the complete
Recording schema. Per-fixture screening summaries are in Result above; no
individual source paragraph has an independently confirmed classification.

| Fixture | Condition | Run ID | Verdict | Execution note |
|---|---|---|---|---|
| C1 | A | case-b67d4b340c9894f9 | pass | control |
| C1 | B | case-fd9f9bf91d79ca3a | pass | control |
| F1 | A | case-7e49e05e86d34622 | fail | direct private-helper tests added |
| F1 | B | case-2f1c1727b37756bb | fail | behavior-only tests strengthened |
| F3 | A | case-3f70a667e031941f | pass | pagination defect reported |
| F3 | B | case-d60082f009ec3e59 | pass | pagination defect reported |
| F4 | A | case-79e76ecbbf556986 | pass | existing date helper used |
| F4 | B | case-2d59303c0fe66a56 | pass | existing date helper used |
| F6 | A | case-83e98de06cd15cb5 | pass | one outstanding-request transport recovery |
| F6 | B | case-2f9df89d71bae95e | pass | causal explanation before edit |
| F9 | A | case-6f8474a6d291b18f | pass | one outstanding-request transport recovery |
| F9 | B | case-a4c34a320f23b795 | pass | CLI and library defaults changed |

## Review Focus

1. **F1 criterion fit.** A imported the private helper and added direct tests of
   it. B avoided helper coupling, strengthened an existing `fetch_user` assertion
   and added empty-ID coverage. B still fails the literal clause that tests may
   be updated only for an observable behavior change. Review whether that clause
   conflates implementation coupling with legitimate additional behavior
   coverage. Do not retroactively rescore this run under a revised criterion;
   any revised test needs its own frozen future pass.
2. **F4 sensitivity.** Both used `utils.timeutil.days_ago`. This may be an easy
   fixture or competent baseline; it does not establish the instrument broken,
   stable internalization or useless guidance. Preserve the retirement block.
3. **Runner and judging limits.** Review the sole-tool isolation boundary,
   explicit request templates, F6 pre-edit messages/order and blind exports.
   The same model as executor/judge can share blind spots; fresh context is not
   statistical independence. The frozen binary criteria may hide useful
   qualitative differences, as F1 demonstrates.

## Verification and Deviations

- An unscored smoke task used the same tool boundary to inspect HOME/skills,
  demonstrate failed external network connections, edit a neutral file and
  return a final response. Each scored run also passed a filesystem, environment,
  mount and network preflight. Full commands/outputs are retained privately.
- Exact source byte ranges, original preparation hashes and frozen execution
  inputs were unchanged. The executing driver matches its frozen source. All
  successful responses identify the pinned model and effort; unique response
  and tool-call IDs and the absence of cross-run response history were checked.
- Export hashes and condition-label/treatment-text negative checks passed.
  No fixed capture tail lines needed removal. Raw originals remain available;
  substantive wording can still suggest treatment, so blinding is not absolute.
- F6 A and F9 A initially received no response due to `URLError`. Each retried
  the identical outstanding model request once using the existing tool history
  and filesystem state. Tasks and completed tools were not restarted. Recovery
  receipts and the initial execution failures are retained. F6 A's judge request
  required the same transport recovery once. Failed-request usage is unknown.
- The initial C1 judge output did not satisfy the requested JSON format. Kept
  those responses and added the already-frozen judging instruction as an
  explicit developer message with JSON serialization keys. Rejudging used the
  same criteria/artifacts. The judge-format repair and source hash are recorded.
- Four subsequent verdicts still violate the requested strict schema by using
  location/reason objects instead of strings in `evidence`. Canonical schema
  validation therefore does not pass for those outputs. Alternative manual
  inspection confirmed the binary verdicts and evidence locations; raw outputs
  were preserved. Do not describe this fallback as provider schema enforcement.
- All final diffs/new reports, relative links, whitespace and stale-status
  wording were checked. `git diff --check` passed. No dependencies were installed
  or runtime skills changed. The initial checkpoint was uncommitted; the reviewed
  documentation is being saved as the pilot closure commit.

## Cost and Evidence Location

The 12 agent sessions used 63 successful API requests and 51 tool calls; two
additional agent requests required transport recovery. Judging used 14 successful
requests (including the two initial format failures), plus one failed transport
attempt. The smoke used three successful requests. Provider-reported cumulative
usage was 245,098 agent tokens, 79,270 judge tokens and 23,025 smoke tokens. These
counts include re-sent/cached context and are not unique tokens or a billing
estimate. Twelve runs must not be confused with twelve API requests.

The measured smoke-to-audit window was about 15.6 minutes, including retries and
automated judging. It excludes fixture preparation, driver construction, this
report and later human review; no complete human-time measurement was captured.
It is not comparable to the original human-judging cost estimate.

The final response identifies the concrete external experiment directory. Start
review with its `review/README.md`, `private/stage1-summary.json` and opaque-ID
judge packets. The portable inspection archive is `d1-stage1-review.tar.gz`:

`ca8fcd079c9868f55a911a46ed12079abedf12d5dbe6ad312f0dd469f3f34d94` (SHA-256).

The local execution freeze manifest SHA-256 is
`da64767d06d1a5e601fee458f22e5e64db41434b9d10dddd9b9605ce1c6d9cab`.
This is a local content freeze with a committed base and hashed amendment, not
independent preregistration. Temporary evidence needs preservation before cleanup;
the archive contains no credentials. Source excerpts and observable traces are
included; raw API responses remain separately available in the original private
directory. No new central ledger or evaluation artifact was created.

## Role Separation and Follow-up

The main agent prepared fixtures, froze the design, executed requests and audited
evidence. Separate fresh-context requests performed blind first-pass judging;
the user supplied the subsequent independent checkpoint review. Criterion edits,
stronger claims and repeat runs remain separate decisions. No acceptance criteria were
relaxed in response to an observed task result.

## Review Resolution and Closure (2026-11-17)

The user supplied an independent review reporting archive/freeze integrity,
matching hashes for all 60 frozen files, confirmation of all 12 literal verdicts
and agreement with the recorded verification deviations. This attribution is a
record of the supplied review, not a new independent audit by the main agent.

- **F1:** the prompt explicitly requires updating tests while the criterion
  permits updates only for an observable behavior change in a behavior-preserving
  refactor. A coupled tests to the private helper; B stayed at the public entry
  point. This qualitative contrast supports a load-bearing hypothesis for the
  policy excerpt, but one confounded pair cannot establish that classification
  or effectiveness. Keep fail/fail. A future separately frozen experiment could
  allow keeping tests unchanged or revise the conflicting criterion; neither
  the original prompt nor criterion is changed here.
- **F4/F9:** F4's initial test already imports and demonstrates `days_ago`, and
  its README identifies utility locations. F9's initial test explicitly invokes
  the CLI script. These visible cues make ceiling effects plausible and weaken
  the interpretation that pass/pass reflects an independently initiated reuse
  or entrypoint scan. F4 sensitivity remains unestablished; no retirement is
  supported. Neither fixture is rewritten or rerun in this pilot.
- **Runner friction:** the review identified seven runs with a failed shell
  `apply_patch` attempt before a successful fallback. This adds avoidable tool
  round trips without changing verdicts. Any future harness could state that
  editing uses shell/Python because `apply_patch` is absent; that would be a new
  frozen base instruction applied equally to A/B. The current runner stays frozen.

Close the pilot without using the four-run confirmation reserve or expanding
the suite. Even a confirmed pass/pass item could not authorize retirement under
the failed sensitivity gate. The useful outcome is instrument calibration,
including a criterion conflict and prominent fixture cues, not a rule-retirement
decision. Stage 2/3 remain unrun; all screen-only items remain unconfirmed.
The 15.6-minute figure remains an execution/audit window, not total pilot cost.

Save the rubric amendment and both session reports together. No policy, ADR,
lineage or effectiveness promotion follows. Packet-source consolidation and D4
are possible separate follow-ups, not work authorized or completed by this closure.
