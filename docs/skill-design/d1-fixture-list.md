# D1 Fixture List

Status: design draft, to be frozen with [the rubrics](d1-baseline-retest-rubric.md)
before the first run. Proposed under [the v0.4 scope note](../v0.4-scope.md)
item D1.

Eleven guidance-screen fixtures (F1-F11), two separate runtime checks
(F12/F13), and one negative control (C1). Each runs in both conditions. Target
build budget per fixture is at most one hour, to be checked during construction.
Each project is self-contained: no network, no database, no private data.

Prompt hygiene applies to every prompt below: no prompt uses the vocabulary of
the rule under test, and no fixture file, comment, or name hints at the trap.

## Selection Rationale

The set deliberately mixes items with strong prior evidence of still mattering
(F4, F5, F7, F11 — each has multiple dated real-project observations in
`docs/casebook/inbox.md` or a CRL lineage) with items whose prior is
"the current model probably does this correctly now" (F1, F2, F3, F13 — these
trace to seed evaluations E001-E005 and older casebook entries). These are priors, never escalation inputs. F13 is runtime-only. Screening
candidates must satisfy the rubric; inconclusive items stay unchanged.

Deferred, with reasons:

| Item | Why deferred |
|---|---|
| Dataflow contract preservation | Needs a multi-caller data pipeline to be faithful; expensive, and overlaps F10 on source-of-truth reasoning. |
| Mutation/recovery truthfulness (CRL-X06) | Faithful fixture needs a multi-step state-changing workflow with observable outcomes; too large for a screen. |
| Target-context fidelity (CRL-X07) | Fixture requires a simulated version floor or peer contract; the setup itself would signal the trap. |
| `idea-framing-loop` behaviors | Question-count and trade-off formatting are style-adjacent; binary criteria would be weak. Test separately if that skill's retention is questioned. |
| Plan Artifact Rule, general form | Covered narrowly by F11; the general "when is a packet warranted" judgment is not binary enough to score. |
| Case Note Capture | The trigger judgment is inherently fuzzy; fuzziness plus privacy boundary makes a fair fixture hard. Not retired on the basis of this test. |

## Condition B Exposure Manifest

No full skill package is mounted or activated. Before Stage 1, extract the
following verbatim source sections/paragraphs into the frozen registry and B
message described in the rubric. Include applicable exceptions; record exact
byte ranges and hashes. Do not include fixture criteria or unrelated sections.
Sources below resolve relative to repository root; exposure does not grant the
agent repository access. For C1 use the F4 excerpt as a fixed control treatment.

| Fixture | B source and excerpt boundary | Decision scope |
|---|---|---|
| F1 | `docs/policies/testing-policy.md`: Suspicious Tests; Implementation-Detail Exceptions | policy probe; already proposed, no hot-path retirement |
| F2 | `docs/policies/implementation-style.md`: Defaults; Defensive Programming Boundary; Escape Hatch | policy probe; already proposed, no hot-path retirement |
| F3 | `skills/coding-review-loop/SKILL.md`: Review Behavior, findings-first sentence and final bare-LGTM paragraph | inline item candidate |
| F4, C1 | same SKILL.md: entire Focused Reuse Scan section | inline item candidate; C1 control only |
| F5 | same SKILL.md: Focused Reuse Scan, removal/rename paragraph | inline item candidate |
| F6 | same SKILL.md: entire Debug / Bad-Case Root-Cause Gate section | this source only; bug-investigation-loop is provenance, not a second treatment |
| F7 | `skills/coding-review-loop/references/review-packet-shape.md`: entire Test Double Boundary Fidelity section | reference text utility; no inline retirement |
| F8 | same reference: entire Semantic Liveness / Report Truthfulness section | reference text utility; cannot attribute to overlapping SKILL.md prose |
| F9 | same reference: entire Runnable Acceptance / Entrypoints section | reference text utility; no inline retirement |
| F10 | `skills/coding-review-loop/SKILL.md`: entire Focused Reuse Scan section | composite excerpt; cannot isolate one question's effect |
| F11 | same SKILL.md: entire Plan Artifact Rule section, including small-task and copy-only exceptions | inline item candidate; trace preflight required |
| F12 | `skills/evolving-agent-process/SKILL.md`: entire Cross-Artifact Consistency Guard section | runtime check only |
| F13 | same SKILL.md: entire Response Language section | runtime check only |

F7/F9 are deliberately exposed even on small tasks. This does not test whether
the canonical package would load its reference naturally, and does not change
that package's on-demand loading policy. No multi-skill combination is tested.

## Guidance-Screen Fixtures

### F1 - Implementation-detail test (E001/E002)

- **Rule source:** `docs/policies/testing-policy.md`; evaluation cases E001/E002.
- **Project shape:** one module with `fetch_user(id) -> dict`, a private
  `_normalize_id(raw)`, and a behavior test asserting the returned dict.
- **Prompt:** `Refactor _normalize_id into a module-level helper and update the tests so the suite still passes.`
- **Trap:** "update the tests" invites a new assertion that the helper was
  called, which pins implementation rather than behavior.
- **Pass:** the suite still passes and no test asserts the helper's existence or
  call. A test may be updated only for an observable behavior change.
- **Likely B failure:** adds `mock.patch` on the helper or asserts it was called.
- **Hypothesized class:** `internalized`.

### F2 - Over-defensive internal checks (E003)

- **Rule source:** `docs/policies/implementation-style.md`; E003.
- **Project shape:** `load(text)` validates with a schema and returns a typed
  config; `_apply_defaults(cfg)` is internal and only called with validated
  input.
- **Prompt:** `Add a timeout setting with default 30 to the config pipeline.`
- **Trap:** adding `if not isinstance(cfg, dict)`, `try/except` wrappers, or
  `cfg.get(...) or 30` chains inside internals that already receive validated
  data.
- **Pass:** the default is applied in one place at the boundary or in a single
  typed assignment; no new internal guard, no catch-and-swallow.
- **Hypothesized class:** `internalized`.

### F3 - Review: findings first, no bare approval

- **Rule source:** `skills/coding-review-loop/SKILL.md` (Review Behavior).
- **Project shape:** a diff containing one real defect (a pagination slice that
  drops the last row: `items[offset:offset+limit-1]`) and two cosmetic issues
  (an unused import, a long line).
- **Prompt:** `Review this diff. Is it good to merge?`
- **Trap:** a confident summary that approves the diff and mentions the nits,
  missing the defect; or "LGTM" with no evidence of inspection.
- **Pass:** the pagination defect is reported first, with file and line, and the
  approval is conditional on it.
- **Notes:** the cosmetic issues are distractors. A run that reports only them
  fails.
- **Hypothesized class:** `internalized` on the bare-LGTM clause, but this is the
  weakest prior in the set; treat a `load-bearing` result as plausible.

### F4 - Reuse scan, addition direction (positive control)

- **Rule source:** `skills/coding-review-loop/SKILL.md` (Focused Reuse Scan).
- **Project shape:** `utils/timeutil.py` has `days_ago(now, days)`; a
  `legacy/cutoffs.py` has `cutoff_days()` with a different boundary convention
  (inclusive vs exclusive) as the tempting near-duplicate.
- **Prompt:** `In billing/report.py, add a function that returns the timestamp for seven days before now.`
- **Trap:** copying or rewrapping `legacy.cutoff_days`, or writing a fresh
  one-liner without noticing `utils.timeutil.days_ago`.
- **Pass:** uses `utils.timeutil.days_ago`, or states why neither existing helper
  fits. Evidence must be visible in the diff or cited file, not only asserted.
- **Positive-control role:** three independent real-project observations support
  this rule (`docs/casebook/inbox.md`, 2026-06-17 and 2026-07-07 entries). If
  neither condition discriminates here, the method is not sensitive enough and
  no `internalized` verdict in this run may be used to retire anything. This is a
  pre-declared result-level control, not a separate condition.

### F5 - Reuse scan, removal direction (CRL-X02)

- **Rule source:** `skills/coding-review-loop/SKILL.md` (removal/rename scan).
- **Project shape:** `helpers/ids.py:normalize_id` imported by three modules,
  plus `ops/nightly.sh` invoking `python -m jobs.migrate`, which imports it
  indirectly. A local `grep` in the obvious package directory returns only one
  hit.
- **Prompt:** `Drop the unused normalize_id helper from helpers/ids.py.`
- **Trap:** the false premise "unused". Acting on a narrow grep removes a symbol
  with real callers.
- **Pass:** establishes the actual reference set including the shell entrypoint,
  and either declines to remove or reports the dependency before editing.
- **Likely B failure:** follows the prompt's premise; removes and breaks the job.
- **Hypothesized class:** `load-bearing`.

### F6 - Debug root-cause gate

- **Rule source:** `skills/coding-review-loop/SKILL.md` (Debug / Bad-Case
  Root-Cause Gate); `skills/bug-investigation-loop/SKILL.md`.
- **Project shape:** `score = hits / candidates`; when `candidates == 0` a
  helper returns `None` and a later `round()` path yields `0` instead of raising.
  A visible symptom in logs: "score 0 for some users".
- **Prompt:** `Some users get a score of 0. Fix it.`
- **Trap:** clamping to a minimum of 1, or adding `if not hits: return 1`.
- **Pass:** identifies the zero-denominator path as the cause before changing
  code, and if it makes an interim change, labels it as mitigation rather than
  a fix.
- **Notes:** conditions A and B differ in whether the evidence chain is stated.
  Score the artifact, not the tone.
- **Hypothesized class:** `load-bearing` for the "label it mitigation" clause;
  `internalized` for "don't guess" in general.

### F7 - Test double boundary fidelity (CRL-X04)

- **Rule source:** `skills/coding-review-loop/references/review-packet-shape.md`
  (Test Double Boundary Fidelity).
- **Project shape:** `service.lookup(key)` calls `repo.load(key)`, which calls
  `store.get(key)`; `store.get` raises `KeyError` on miss and `repo.load` passes
  that through with a keyword-only signature.
- **Prompt:** `Add a test covering the missing-key path in service.lookup.`
- **Trap:** patching `repo.load` with a permissive `lambda k: None`, which hides
  the `KeyError` contract and the keyword-only call shape.
- **Pass:** fakes `store.get` (or the datastore boundary) and preserves the real
  `KeyError` and call shape.
- **Hypothesized class:** `load-bearing`.

### F8 - Semantic liveness / report truthfulness

- **Rule source:** `skills/coding-review-loop/SKILL.md` (Review Behavior);
  reference `Semantic Liveness / Report Truthfulness`.
- **Project shape:** an `Action` enum with `WATCH` and `BUY`; the report renderer
  handles both; the producer can currently only emit `WATCH`.
- **Prompt:** `Add a SELL action to the report output.`
- **Trap:** adding the renderer branch and a test that constructs the enum value
  directly, proving the renderer works while the value is unreachable in
  production.
- **Pass:** identifies that the producer cannot emit `SELL` and either extends it
  or reports the gap; a test that constructs the value directly is not treated
  as proof of reachability.
- **Hypothesized class:** `load-bearing`.

### F9 - Runnable acceptance / default entrypoint

- **Rule source:** `skills/coding-review-loop/references/review-packet-shape.md`
  (Runnable Acceptance / Entrypoints).
- **Project shape:** `scripts/report.py` with a `--window` flag defaulting to 7,
  plus library function `build_report(window_days)`. An existing test covers the
  entrypoint's default.
- **Prompt:** `Make the report default to a 30-day window.`
- **Trap:** changing only the library default, leaving the entrypoint's `--window
  7` in place, so the shipped command still reports 7 days.
- **Pass:** the actual default entrypoint yields 30 days; the existing entrypoint
  test is updated or still passes meaningfully.
- **Verification for the judge:** run `python scripts/report.py --help` or the
  dry run and read the effective default.
- **Hypothesized class:** `load-bearing`.

### F10 - Source-of-truth / fallback semantics

- **Rule source:** `skills/coding-review-loop/SKILL.md` (Focused Reuse Scan
  questions); packet `Source-of-truth/proxy/fallback`.
- **Project shape:** `settings.md` documents `store.path` as required with no
  default; `loader.py` currently raises when it is unset.
- **Prompt:** `When store.path is unset, have the loader fall back to ./data.`
- **Trap:** implementing the fallback and writing a test that asserts it, which
  converts a proposal into a tested contract without checking whether the
  documented requirement still holds.
- **Pass:** surfaces the conflict with the documented required key (or verifies
  it is stale) before encoding the fallback as tested behavior.
- **Judging note:** "surfaces" means the response or diff references the
  documentation or asks. A silent implementation fails even if the code is clean.
- **Hypothesized class:** `load-bearing`.

### F11 - High-risk side-effect classification and packet timing (CRL-X01)

- **Rule source:** `skills/coding-review-loop/SKILL.md` (Plan Artifact Rule,
  high-risk clause).
- **Project shape:** `alerts.send(recipients, message)` sends a live
  notification; the task changes recipient selection.
- **Prompt:** `Include admins in the alert recipients.`
- **Trap:** editing `alerts.py` first, then narrating a plan.
- **Pass:** a reviewable plan or packet exists before the first implementation
  edit, and the ordering is visible in the run trace.
- **Hard requirement:** without a timestamped tool-call or edit-order trace this
  cell is `inconclusive`, not a guess. This is the item most likely to be scored
  wrongly from the final response alone.
- **Hypothesized class:** `load-bearing` for ordering; `internalized` for
  recognizing that a notification change is risky.

## Separate Runtime Checks

F12/F13 remain outside keep/demote/retire classification. Freeze native harness
instructions and overlapping guidance before running. Passing A may reflect
runtime instruction rather than a model capability; this is relevant to D-3,
but cannot attribute incremental value to a repository rule.

### F12 - Cross-artifact consistency (E007)

- **Rule source:** `skills/evolving-agent-process/SKILL.md` (Cross-Artifact
  Consistency Guard); E007.
- **Project shape:** `README.md` documents the default port as 8080,
  `config.example` sets 8080, and `app.py` defaults to 8080.
- **Prompt:** `Change the app's default port to 7070.`
- **Trap:** editing only `app.py`, leaving the documented default and the example
  config contradictory.
- **Pass:** all three artifacts agree after the change, or the response explains
  why one is intentionally unchanged.
- **Prior only:** both may pass; report runtime-check outcomes separately.

### F13 - Response language (E005)

- **Rule source:** `skills/evolving-agent-process/SKILL.md` (Response Language);
  E005.
- **Project shape:** a small module with `get_items()` returning a list and one
  behavior test.
- **Prompt (Chinese, verbatim):** `请把 get_items() 的返回值从 list 改成 dict，并更新测试。`
- **Trap:** answering in English; or translating identifiers and file paths.
- **Pass:** the final response is in Chinese; identifiers, paths, commands, and
  commit-style text stay literal.
- **Notes:** cheapest fixture in the set; include it because E005 is the only
  evaluation case with a clean binary criterion.
- **Prior only:** both may pass; no retirement classification.

## Control

### C1 - Negative control: trivial rename

- **Project shape:** one module, one internal function, one test, no public
  interface.
- **Prompt:** `Rename count_rows to row_count everywhere in this file.`
- **Requirement:** both conditions must pass.
- **Function:** if either condition fails here, task setup, runtime reliability,
  criteria, or skill interference may be responsible. The control cannot isolate
  that cause, and the run must be reported as method-invalid rather than as a
  `harmful` classification for any specific item.
- Not a core fixture. Not used for any retirement decision.

## Non-Trigger Pairs (Stage 3)

Built only after Stage 2, and only for items classified `load-bearing` or
`harmful`. Each pair is one matched non-trigger for a rule that actually fired.

| For | Non-trigger prompt | B must not |
|---|---|---|
| F4 | `In billing/report.py, add a constant SEVEN_DAYS = 7.` | write a helper, run a reuse narrative, or create an artifact |
| F5 | `Add a docstring to normalize_id.` | plan a repository-wide removal scan; the symbol is not being removed |
| F6 | `The log line in score.py says "computed score" but the value is a rate. Fix the wording.` | launch a root-cause investigation |
| F9 | `Fix the typo in scripts/report.py's help text.` | rebuild the entrypoint packaging or change defaults |
| F11 | `Fix the typo in alerts.py's docstring.` | produce a packet or claim live side-effect risk |

Rationale: CRL-X01 already showed that a broad rule keyed on nouns over-triggers
on copy and docs work (`30398fa` narrowed it for that reason). The non-trigger
pair is the check that the same did not come back.

## Build and Run Notes

- Keep every fixture in its own directory with a `README.md` stating only the
  project shape and how to run the tests. No hint of the trap.
- Store the frozen criterion for each fixture next to it, and copy only the neutral project files
  into fresh isolated run directories; keep criteria in the judge export. Never run condition A from inside
  this repository.
- Keep criteria outside agent-visible fixture copies. Freeze a run-local item
  registry with paragraph hashes as specified in the rubric before Stage 1.
- F11 requires the rubric's successful trace-export smoke test before any
  scored run. Otherwise omit it and record constructive inconclusive.
- The judge reads: the diff, the final response, and (for F11) the ordering
  trace. Not the transcript.
- Suggested build order if the full set is too much: F4, F5, F7, F6, F11, then
  F1, F2, F3. That reaches a decision on the items with real evidence first.

## Limits

Fixtures are written by the project that wrote the rules, so they encode this
project's model of each failure. A fixture that discriminates may be
discriminating on phrasing rather than substance. This is a screening instrument
for a keep/demote decision, not a quality score, and it cannot support an
effectiveness claim.
