# D1 Baseline Re-Test Rubric

Status: design draft, frozen on first use. Proposed under
[the v0.4 scope note](../v0.4-scope.md) item D1. Authorizes no change on its own.

## Purpose

Decide, per rule item, whether current models still need it in the per-task read
path. Produce a `load-bearing` / `internalized` / `harmful` classification that a
later retirement proposal can cite only if the scope note's two-tier evidence
decision is accepted. Otherwise results are instrument observations only.

## What This Measures

At fixture level, whether explicitly supplied canonical guidance text changes an observable
outcome on a small, self-contained task.

## What This Does Not Establish

- Not real-task evidence. Not Stage 0 or v0.3 evidence.
- No CRL lineage outcome. It cannot mark anything `improved`, `repeated`, or
  `regression`, and it does not touch CRL-X01 through CRL-X07.
- Not a quality measurement of the skill overall, and not a claim that a
  `load-bearing` item prevents harm in real tasks.
- Detection here is detection of a constructed trap, which is deliberately
  easier than prevention in a real project. Per `AGENTS.md`, review detection is
  not prevention.
- A fixture the baseline passes does not prove the model would pass an unknown
  variant. It only shows this trap did not discriminate.

## Preregistration

Freeze before the first run:

1. This file and the fixture list, committed as-is.
2. `sha256` of both files, recorded in the run log.
3. The classification table and Stage 1-to-2 mapping below, exact fixture
   contents, prompts, judge template, harness instructions, and isolation recipe.
4. A run-local item registry in the existing run log: `item id | source file |
   section heading | paragraph ordinal/range | SHA-256 of exact UTF-8 source
   bytes | fixture ids`. Include every paragraph needed for a composite item
   (including reference and policy sources), with captured source text in the
   frozen snapshot. IDs remain stable; changed hashes are new item versions,
   never silently inherit old verdicts. Build this before Stage 1, not at
   retirement time. This is an experiment manifest, not a central lineage ledger.

Any post-hoc change to a pass criterion after seeing a result invalidates that
item's result and must be recorded as `inconclusive` for the original version. A
revised criterion may be tried in a later, separately preregistered pass.

## Conditions

- **A (baseline):** no skill package present on any load path.
- **B (text exposure):** the exact registered source excerpts for that fixture
  supplied in a dedicated harness guidance message before the task prompt.

D1 tests conditional text utility, not normal package discovery, reference
triggering, or the effect of the whole skill. Neither condition loads a skill
package. B receives only verbatim registered paragraphs, including their trigger
and exception clauses, without editorial strengthening or pass-criterion hints.
The fixture exposure table defines the sources. A receives the same message
wrapper with an empty guidance body; task prompts and all other instructions
match. Freeze the rendered messages and their hashes. Record delivery receipts
privately before the first task action; missing or mismatched delivery makes the
comparison invalid. Delivery proves supplied context, not attention or obedience.
F1/F2 are policy-text probes, not candidates for removal from a mandatory read
path. F7/F9 bypass reference discovery deliberately; results cannot establish
whether normal skill invocation would expose that guidance.

Pin and record per run: model id, reasoning effort, harness version, date, and
working directory. Results are only meaningful for the pinned model. A model
change makes prior results stale; do not compare across models in one table.

Only two conditions in the first pass. A natural whole-package activation arm
is out of scope and would require separate preregistration and budget.

## Isolation and Leakage Controls

These are the main ways this experiment produces a false `internalized`.

- **No repository access in condition A.** The agent must not be able to read
  `evolving-agent-dev`, the runtime skill directory, or a cached copy. A passing
  baseline that found the rule file is not a baseline.
- **Clean working directory per run.** Fresh copy of the fixture, no leftover
  artifacts from a prior run, no `.agent/` directory, no prior transcript.
- **No cross-run context.** Each run starts with no history. Do not run both
  conditions in one session.
- **Prompt hygiene.** The task prompt must not use the rule's vocabulary. If the
  item is about reuse scans, the prompt must not say "reuse", "existing helper",
  "search first", or "DRY". The fixture list specifies the exact prompt per item.
- **Fixture neutrality.** No comment, filename, or doc in the fixture may hint at
  the trap.
- **Record leakage checks.** State in the run log that A had no skill access, and
  how that was verified.

### Executable isolation preflight (required before Stage 1)

Use a fresh container per run, with a separate HOME and no host HOME, repository,
`.git`, session-cache, global-memory, or socket mounts. Changing HOME alone is
insufficient. Freeze the actual image, launch command, mount allowlist, and
harness configuration in the run log; inability to enforce this blocks the run.

1. Mount only the neutral fixture at `/work`. Supply B's frozen excerpt through
   the harness message, not a repository or package mount. The host-side private
   manifest stores source snapshots, message hashes and delivery receipts.
2. Set HOME, CODEX_HOME, and XDG cache/config/data paths to fresh container-local
   directories; disable all skill discovery in both conditions.
3. Disable memory tools, persistent memory injection, session resume, network,
   and host integration in **both** A and B. Pin identical non-treatment harness instructions
   and record any native instructions overlapping the tested rule.
4. In the agent's execution context run `find /work /root /home /opt -name
   SKILL.md -o -name .git -o -name .agents -o -name .codex`; expected: no hits
   except declared fresh harness configuration directories; no SKILL.md or .git. Inspect `/proc/self/mountinfo`:
   expected only the frozen mount allowlist, no host source/cache/home mounts.
   Also record harness discovery/tool inventory: both have no skills and no
   memory or resume tools. Filesystem probes alone cannot prove injection absent.
5. Save commands, full outputs, configuration and inventory in the private run
   log before execution. Unexpected access or undisclosed injected instructions
   invalidate affected comparisons; do not infer isolation from a passing task.

Before F11 is admitted, run an unscored harness smoke fixture that creates a
packet then edits code. Export the harness tool-event stream with monotonic
sequence numbers, tool arguments, and write targets; verify it distinguishes
packet creation from the first implementation edit. Preserve raw trace privately
and a sanitized order-preserving judge copy. If export fails, omit F11 runs and
record it as constructively `inconclusive`; do not spend two scored runs on it.

## Run Protocol

Staged, with a rule frozen in advance:

**Stage 1 — screen.** One run per condition for F1-F11 plus C1: 24 runs.
F12/F13 are separate runtime checks (4 runs), excluded from retirement classes.
If F11 fails trace preflight, the screen is 22 runs and F11 is inconclusive.

**Stage 2 — escalate.** Apply observed Stage 1 results, never fixture priors:

| Stage 1 A / B | Stage 2 action |
|---|---|
| pass / pass | observed as potentially `internalized`; add 2 runs per condition |
| fail / pass | potentially `load-bearing`; add 2 runs per condition |
| pass / fail | potentially `harmful`; add 2 runs per condition |
| fail / fail | keep unchanged, `inconclusive`; no escalation |
| invalid or unjudgeable / any (or reverse) | `inconclusive`; no classification |

Rationale for escalating pass/pass: retention is the cheap, reversible default;
retirement is not. Asymmetric evidence is deliberate. An item may leave the read
path only on 3/3, never on a single lucky pair.

**Stage 3 — negative pairs.** Trigger-based items get a matched non-trigger
fixture. Run only after Stage 2, and only for items that were classified
`load-bearing` or `harmful`, because a non-trigger fixture is only interesting for
a rule that actually fires. Run one A/B pair per eligible non-trigger (at most five pairs). A failure
is a specificity warning, not a confirmed harmful verdict: retain `inconclusive`
for that decision until a separately authorized confirmation. This is the specificity check; the CRL-X01 pilot
found over-triggering here and the same risk applies.

Do not exceed 3 runs per condition per cell. If 3 runs disagree, the answer is
`inconclusive`, not "run more until it agrees".

## Judging

- **Blind carrier.** Before runs, assign random opaque `case-<hash>` IDs not
  derived from condition. Keep the ID-to-condition key, raw logs and labels in
  `private/`, inaccessible to judges. Export only allowlisted diff, final response,
  criterion and sanitized trace into `judge/<opaque-id>/`; normalize directory
  names, absolute paths, timestamps and prompt metadata while preserving trace
  order. Audit exports for condition/path leakage before randomized judging.
  Freeze a per-fixture redaction allowlist before runs: remove standalone
  `Case capture:` status lines and unrelated administrative trace tables only
  when they contain no evidence for that fixture's criterion. Apply the same
  content-based rule to A and B, never condition-based filtering. Preserve raw
  originals and an edit manifest privately; a non-judging auditor checks that
  no criterion evidence was removed. Keep root-cause evidence (F6), producer/
  consumer reasoning (F8), source conflict reasoning (F10), and ordering evidence
  (F11), even inside a trace table. If content cannot be separated safely, retain
  it and flag unblinding. Excerpt-only B should not request unrelated capture
  rituals, but unexpected signatures still require this export policy.
  Do not erase substantive behavior that itself suggests the condition; record
  residual unblinding as a limit. Freeze this judge prompt: "Using only the
  supplied criterion and artifacts, return pass/fail/unjudgeable, cite the
  evidence location, and state missing evidence. Do not infer the condition."
- **Blind.** The judge sees the run's outcome artifacts and diff, stripped of the
  condition label, in randomized order. No condition name in the artifact, path,
  or prompt metadata.
- **Binary per criterion.** Each fixture has one substantive criterion with a
  pass/fail. Secondary observations (`extra artifacts created`, `ritual wording
  present`) are recorded but do not change the verdict.
- **Evidence requirement.** A pass requires the behavior to be visible in the
  artifact or diff, not merely asserted in the response. A response claiming
  "I scanned for existing helpers" with no evidence of the scan, no reference to
  the helper, and a duplicated helper is a fail. This is the repository's own
  known failure mode, recorded in `docs/casebook/inbox.md` (2026-06-18, planning
  scan false confidence).
- **Two judges on disagreement.** A human audit challenges unclear first verdicts;
  record audited counts and disputes. A second blind judge scores disputed cells without
  seeing the first verdict. Persistent disagreement is `inconclusive`. Report the
  disagreement rate; a high rate means the criteria are unclear and the rubric,
  not the rule, needs work.
- **Ordering-sensitive items.** For rules whose claim is about *when* something
  happened (packet before first edit), the run must produce a tool-call or edit
  order trace. Without a trace the item is `inconclusive` by construction, not a
  guess.

## Classification

| Class | Rule |
|---|---|
| `load-bearing` | A fails the substantive criterion and B passes, consistently (3/3 each direction). |
| `internalized` | A and B both pass, 3/3 each. |
| `harmful` | A passes 3/3 and B fails 3/3 on the substantive criterion. A Stage 3 non-trigger failure is only a warning pending confirmation. |
| `ritual-only` | B produces the rule's vocabulary or artifact but fails the substantive criterion, where A passes 3/3 and B fails 3/3. Counted as `harmful` for decision purposes: it adds cost with no benefit. |
| `inconclusive` | Any other outcome, including high variance, judge disagreement, missing ordering trace, or a failed leakage check. |

`internalized` is not a criticism of the rule's history. It means both conditions passed this fixture under the pinned runtime. It does
not distinguish model defaults from native harness guidance or prove learning.

### Asymmetric and mixed outcomes

Always report A/B pass counts, not only the class. A=3/3, B=2/3 remains
`inconclusive` with mandatory flag `baseline-pass / treatment-shortfall` and a
review note: possible variance or treatment interference, not established harm.
Other mixed results carry `mixed-outcome`. Do not silently count either as
positive retention evidence. Any follow-up needs a separately frozen question,
variant and budget, not additional runs until a preferred answer appears.
A=3/3 does not prove the rule unnecessary; this design cannot distinguish a
small effect from sampling noise. No threshold is relaxed after observing data.

## Decision Mapping

This table proposes; it does not authorize.

| Class | Proposed action | Needs user decision |
|---|---|---|
| `load-bearing` | Keep at current source location, no change | no |
| `internalized` | For mandatory-path items, propose demotion. For existing policy/reference items, record no detected need for extra exposure; no path removal implied | yes for any source edit |
| `harmful` | Remove, or narrow the trigger and re-test | yes |
| `ritual-only` | Treat as `harmful`; remove the wording, keep any substantive part | yes |
| `inconclusive` | Keep source unchanged; record counts and required warning flags; no automatic favorable retention claim | no |

A retirement decision records: frozen registry item ID and source hash, cited fixture and result, date, model,
prior location, new location (if demoted), and what would bring it back.

## Cost

Costs below are incremental runs, not cumulative totals; excluded F11 reduces
Stage 1 by 2 and Stage 2 maximum by 4. Invalid controls stop decision use.

| Stage | Runs minimum | Runs maximum | Notes |
|---|---:|---:|---|
| Trace preflight | 1 | 1 | unscored smoke run; fix harness before admission |
| 1 screen | 22 | 24 | F1-F11 + C1, A/B; F11 conditional |
| Separate runtime checks | 4 | 4 | F12/F13 A/B, no retirement classification |
| 2 escalation | 0 | 44 | +4 per eligible item; total 6 per item including Stage 1 |
| 3 non-trigger pairs | 0 | 10 | F4/F5/F6/F9/F11, one A/B pair each |

Full planned maximum: 83 runs including preflight, runtime checks and control.
This excludes reruns after invalidation, which require a new budget decision.
Building 14 base fixtures at up to one hour each budgets up to 14 person-hours
(roughly two working days), plus up to five non-trigger variants. This estimate
is unverified. Blinding/export setup and judge work are additional costs: budget
5-15 minutes per scored run (up to 82 first-pass judgments, roughly 7-21 hours),
plus second judgments on disputes. Record actual build and judge time separately
from model execution cost; parallel runs do not remove human review cost.

**Minimum useful cut** if the full design is too expensive: run only F1, F3, F6,
F9, and C1, plus F4 as the sensitivity control. That set covers a likely-internalized item, two
likely-load-bearing items, a pure-detection task, and the method's own validity
check. It cannot support a retirement decision for the untested items, and the
report must say so.

## Recording

One table, one row per cell:

```text
item id + source hash | fixture | condition | run # | model | effort | date | verdict | evidence path | notes
```

Then one summary row per item: classification, runs, disagreement count, leak
check result. Keep artifacts (fixture copy, diff, final response) under a single
dated directory so a later reviewer can re-judge blind.

## Limits

- Fixture-level results do not transfer to real tasks and cannot justify an
  effectiveness claim of any kind.
- The fixtures are written by the same project that wrote the rules, so they
  encode that project's theory of what the failure looks like. A fixture that
  discriminates may be discriminating on style rather than substance.
- The model under test may have been trained on public discussion of similar
  guidance; `internalized` may be memorization of phrasing rather than stable
  behavior. This cannot be separated here.
- Judging quality is bounded by the criteria. Binary criteria hide partial
  compliance, which is why `ritual-only` exists as its own class.

- Three repetitions have low power: for independent runs with true pass
  probability p, one condition passes 3/3 with probability p^3. At p=0.6 this
  is 21.6%, so 3/3 is not proof of reliable behavior. Both-condition classification
  has a different probability (p_A^3 p_B^3 only under independence); shared
  prompts and runtime can correlate runs. Explicitly accept this uncertainty in
  any demotion decision, with a reversible return trigger.
- The strict two-sided gate also misses stable-looking candidates: under
  independent runs with p_A=p_B=0.85, probability of 6/6 is 0.85^6 = 37.7%.
  The remaining 62.3% do not reach `internalized` (mostly inconclusive; some
  other strict outcomes are possible). This is an illustrative unconditional
  probability, not measured power or a posterior error rate; Stage 1 selection
  and correlated runs complicate interpretation. The design favors avoiding
  unsupported demotion over maximizing retirements and may be too conservative
  for D-1. Report the inconclusive rate and decide whether the instrument is
  useful before any larger run; do not interpret retention-by-default as benefit.
- A minimum useful cut cannot support decisions for untested items. F12/F13
  measure behavior under native harness instructions and cannot attribute it to
  repository rules; report their results separately.
