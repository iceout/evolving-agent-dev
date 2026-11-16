# Session Report: D1 Baseline Re-Test Design

## Goal

Draft the rubric and fixture list for v0.4 item D1, as requested after the scope
draft: "把 D1 的 rubric 和 fixture 清单也起草出来". Design only; no run was
attempted and no rule is changed by this work.

Mode: documentation design task. evolving-agent-process dogfood, post-Stage 0.
Stage 0 counts frozen and unchanged. No CRL-X01 through CRL-X07 outcome,
evaluation watchlist item, policy, ADR, or skill file is touched.

## Changes

- `docs/skill-design/d1-baseline-retest-rubric.md` (new): what the test measures
  and explicitly does not establish, preregistration and hashing, two conditions,
  leakage controls, a three-stage run protocol with an asymmetric escalation rule,
  blind binary judging with an evidence requirement, a five-class verdict scheme
  including `ritual-only`, a proposed decision mapping, cost and a minimum useful
  cut, the recording table, and limits.
- `docs/skill-design/d1-fixture-list.md` (new): eleven guidance-screen fixtures, two
  separate runtime checks, and one negative control, with rule sources, project
  shapes, exact prompts, traps and pass criteria. Some include likely B failures
  or prior classes; runtime checks carry no retirement class. Six deferred
  items with reasons, five non-trigger pairs for Stage 3, build/run notes, limits.
- `docs/v0.4-scope.md`: the D1 item now links both design documents and states
  the current fixture grouping and its evidence boundaries.
- `docs/session-reports/2026-11-13-v0.4-scope-draft.md`: addendum recording that
  the earlier verification gap was closed once the tooling problem cleared.

No fixture directory, no test, no script, and no runtime file was created.

## Role Separation

Not triggered. Documentation-only change. The design does describe a future
experiment, but drafting an experiment is not the experiment.

## Verification

Bash was available in this session; the earlier tooling block had cleared.

- `git diff --check`: passed.
- Whitespace scan of all four new/changed files: no trailing whitespace.
- Relative-link resolution check for `docs/v0.4-scope.md`,
  `docs/skill-design/d1-baseline-retest-rubric.md`, and
  `docs/skill-design/d1-fixture-list.md`: every markdown link resolves to an
  existing file. Checked with a loop over the extracted link targets.
- `git status --short` at the start of this task showed only the three expected
  files from the previous task: `README.md` modified, and the two untracked
  documents. No unrelated change was present or touched.
- Source check before drafting: read `skills/idea-framing-loop/SKILL.md` in full,
  the last skill file not yet read, to decide whether it belongs in the fixture
  set. It is deferred, with the reason recorded in the fixture list rather than
  silently omitted.
- Fixture prompts were written against the hygiene rule the rubric imposes: no
  prompt uses the vocabulary of the rule under test. Checked F4 (no "reuse",
  "existing", or "scan"), F5 (no "unused reference"), F6 (no "root cause"),
  F9 (no "entrypoint" or "acceptance"), F10 (no "source of truth"), F11 (no
  "packet" or "high-risk").
- One cross-document consistency fix during writing: F4 was originally going to
  be a separate condition, which would have doubled the run count for a question
  classification already answers. It is now a pre-declared result-level control
  inside the existing two conditions, and the rubric states the consequence when
  it fails.

Not verified: whether any fixture actually discriminates. That is the experiment,
and it has not run. The hypothesized classes in the fixture list are priors from
`docs/casebook/inbox.md` and the v0.3 lineages, not measurements.

## Good

The design makes retirement harder to reach than retention, on purpose: an item
may leave the read path only on 3/3 in both conditions, while keeping it needs
nothing. That matches how the asymmetry actually costs — a wrongly kept rule is
cheap and reversible, a wrongly removed rule is neither.

`ritual-only` was added as a distinct class because the repository's own most
frequent recorded failure is producing the vocabulary of a check without its
substance (`docs/casebook/inbox.md`, 2026-06-18). A two-class scheme would have
scored that as a pass.

F11 requires an ordering trace and is `inconclusive` without one, rather than
letting the final response stand in for the timing claim.

## Friction

- What happened: while drafting, the ten-item count in the v0.4 scope draft and
  the fixture set pulled in opposite directions. Ten most-used items would have
  left several retirement candidates untested, which would make their retirement
  undecidable; thirteen plus a control tests the candidates but costs more.
- Why it felt wrong: the scope draft named a number before the measurement
  design existed.
- Impact: the scope draft's D1 wording was amended and the discrepancy is stated
  in that section rather than quietly reconciled.
- Category: `process` / `requirements`
- Root cause guess: writing a direction item with a count attached before
  designing the measurement. The count was a placeholder that read as a
  specification.

- What happened: `skills/idea-framing-loop` could not be scored with a binary
  criterion without inventing one. Its stated behaviors are dialogue shape and
  trade-off presentation.
- Why it felt wrong: leaving it out of the fixture list could read as an implicit
  "not worth testing" verdict.
- Impact: it is listed as deferred with an explicit reason and an explicit
  statement that this test cannot retire it.
- Category: `review`
- Root cause guess: the method suits decision-like rules and interacts poorly
  with style-adjacent ones. That is a limit of the instrument, not of the skill.

## Proposed Follow-up

- Policy note candidate: none.
- Casebook candidate: none.
- ADR needed? Only if D2 (retirement becomes a required decision) is accepted.
  Not from this design work.
- Evaluation candidate? No. These are experiment fixtures, deliberately not in
  `docs/evaluations/`; promoting them would cross the v0.3 evidence boundary.
- Next step needs explicit authorization and a run environment: build the
  fixtures, freeze both files with hashes, then run Stage 1. The minimum useful
  cut (now F1, F3, F4, F6, F9, C1) is the bounded way to check that the instrument
  discriminates before spending on the full set.

## Review Revision (2026-11-13)

The user requested checking review comments 2-9 and fixing supported findings.
They were substantially supported by the draft text. The source identity issue
also applies to policy/reference paragraphs, not only SKILL.md. The p^3 example
is a one-condition probability under independence, not the final classifier's
false-positive rate.

- Scope: replaced the claim that D1 tests D-2 with a mandatory evidence-tier
  decision before execution; fixture outcomes remain candidates, not effectiveness.
  Proposed the skill packet reference as sole source and repository copy as a
  checked pointer, without implementing that separate backlog item.
- Rubric: requires a frozen run-local item registry with paragraph hashes before
  Stage 1, observed-result escalation mapping, explicit incremental cost table,
  construction/judging estimates, opaque judge exports and frozen prompt,
  container isolation preflight, memory off in both conditions, and trace smoke
  validation before F11. The registry itself belongs to experiment preparation;
  no source snapshot or historical attribution is invented in this design edit.
- Fixture list: F12/F13 are separate runtime checks excluded from retirement;
  neutral agent copies exclude criteria. C1 failure in either condition invalidates
  decision use. Minimum cut includes both C1 and the F4 sensitivity control.
- Related correction: a single Stage 3 non-trigger pair only raises a warning;
  it cannot establish confirmed harmful behavior for removal.

Verification: read the full final design files and README diff, checked local
Markdown links and whitespace (including untracked files), asserted run-budget
arithmetic and required sections, and searched for the obsolete count, escalation,
D-2 and automatic-internalization language. `git diff --check` passed.
No experiment ran; isolation, trace export, fixture build time and judgment cost
remain unvalidated design requirements/estimates. Completion here means the
documentation revision, not an operationally validated harness. No skill package,
central lineage, runtime install or Stage 0 count changed; no commit made.

Role separation: plan decision was to fix the draft's gates and reproducibility
without executing D1; verification checked arithmetic, links and cross-document
semantics; implementation was limited to the three design docs and this report;
review checked evidence boundaries and stale claims. No new process rule or
formal evaluation was promoted. No separate friction artifact is needed: the
review findings and their resolution are recorded here.

## Second Review Revision (2026-11-16)

Documentation edit, evolving-agent-process dogfood; Stage 0 frozen, no outcome
or effectiveness claim. Review findings 1, 2 and 4 were supported. Finding 3's
0.85^6 calculation is valid under independence; A=3/3 is not proof that guidance
is unnecessary. Preserved the strict threshold, documented its low yield, and
added a mandatory baseline-pass/treatment-shortfall warning for A=3/3, B=2/3.

Changed the experimental treatment explicitly from normal package loading to
frozen per-fixture text exposure. The fixture manifest specifies source boundaries
for every B treatment and C1; policy/reference probes cannot imply inline
retirement. This intentionally excludes natural activation, multi-skill behavior
and whole-package overhead from D1's claims. Such tests need a separate design.
Added symmetric, preregistered removal of irrelevant output signatures with raw
originals, edit manifest and evidence-preservation audit. Updated the opening
Changes summary; the earlier dated revision sections retain their historical
context, superseded by this section where treatment semantics differ.

Plan: resolve treatment delivery without touching canonical skills. Verification:
check exact source headings, fixture coverage, links, stale treatment wording,
probability arithmetic, full final files and whitespace. Implementation: only
scope, rubric, fixture list and this report. Review: preserve conservative
classification without hiding asymmetric warnings or claiming native loading.
Checks passed; no harness/fixtures ran, so delivery, isolation and redaction
remain unvalidated execution requirements. No new policy, evaluation, casebook,
runtime install or commit. The review and resolution stay in this report.
