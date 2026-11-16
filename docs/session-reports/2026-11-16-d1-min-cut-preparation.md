# Session Report: D1 Minimum-Cut Preparation

This records the initial preparation checkpoint. Execution subsequently continued
at the user's request; [the Stage 1 report](2026-11-16-d1-min-cut-stage1.md)
supersedes the blocked execution status below and records the reviewed Stage 1
closure on 2026-11-17.

## Goal

Start the user-authorized bounded D1 pilot using F1, F3, F4, F6, F9 and C1.
The user requested optimizing the quoted execution path and proceeding. Apply
its evidence split: fixture observations may support D2 candidates, never
real-task effectiveness, lineage promotion or automatic guidance edits.

Mode: edit task, evolving-agent-process dogfood, post-Stage 0. Stage 0 stays
frozen. This report records experiment preparation, not a behavior observation.

## Changes

- Added a bounded-pilot option to the existing D1 rubric: four-hour total cap,
  C1 first, at most 12 screen runs plus four confirmation runs for one inline
  item, fixed confirmation priority F3 then F6 then F4, no Stage 3 or expansion.
  Unconfirmed eligible items remain screen-only. Original classification
  thresholds and the full-design budget are unchanged.
- Prepared six neutral standard-library Python projects outside the repository
  under a generated `d1-min-cut-2026-11-16-*` temporary directory. The final
  response identifies the concrete local directory. No fixture or runner code
  was added to the repository.
- Extracted verbatim excerpts from committed source `b8da3a3`, with exact
  zero-based UTF-8 byte ranges and SHA-256 in `item-registry.json`. F1 has two
  source excerpts, F3 two paragraphs, F4/F6/F9 one section each; C1 uses F4's
  treatment. Registry SHA-256:
  `692c9c42accbebdd1cada24a4cc06545bb31bb452478a7c3851079ff2a67a347`.
- Prepared criteria, identical A/B message wrappers, message hashes, opaque
  run IDs with a private condition key, judge prompt and a 55-file preparation
  integrity manifest. Original committed design hashes and the modified pilot
  rubric hash are recorded separately. These snapshots are not a completed
  execution preregistration: model, effort, native instructions, actual tool
  inventory and delivery receipts are still missing. No commit was made.

## Verification

Local Docker, Podman and nerdctl executables and the checked default Docker/
Podman sockets were absent. Existing bubblewrap successfully ran fresh mount,
PID and network namespaces with cleared environment, empty HOME, read-only
system runtime and only one writable workload bind at `/work`.

For each fixture, saved commands and full outputs of filesystem discovery,
mount inventory, environment and failed external network connection in private
preflight logs. The final `find` checks completed without errors or matches;
host home and repository paths were absent. These checks establish isolation
for the test subprocess only, not a model runner.

| Fixture | Initial isolated unittest suite | Additional construction check | D1 status |
|---|---|---|---|
| F1 | 3 tests passed | behavior tests do not pin private helper calls | not run |
| F3 | 3 tests passed | supplied diff applies; candidate produces one expected behavior-test failure | not run |
| F4 | 2 tests passed | two date helpers have different boundaries | not run |
| F6 | 4 tests passed | zero denominator returns None, then becomes score 0 | not run |
| F9 | 2 tests passed | changing only library default to 30 leaves CLI at 7 | not run |
| C1 | 2 tests passed | internal rename task has behavior-level tests | not run |

All 16 initial tests passed. Private construction mutations used disposable
copies; prepared source snapshots retained their hashes. Verified source byte
ranges against the committed files, local Markdown links, whitespace, bounded
run-budget arithmetic and stale-wording checks. `git diff --check` passed;
untracked report content was checked separately.

### Verification Failure and Execution Boundary

- First private F3 checker incorrectly expected two failed tests after applying
  the candidate; only the full-page test fails, while the partial-page test
  still passes. Corrected the checker expectation and reran in fresh copies.
  No fixture or criterion was changed to accommodate an agent result.
- Inspected local `codex exec`, `exec-server` and app-server help. CLI version
  is 0.166.0. `codex sandbox linux --help` could not initialize because its
  app-server socket directory failed the ownership/mode check. The separate
  bubblewrap probe succeeded; this is not proof the CLI runner is unusable.
- No existing end-to-end model runner was validated in this task that keeps
  model transport outside the isolated tool environment, prevents all other
  filesystem/tool access, disables skill/memory/resume injection and records
  delivered messages. No model connection was attempted. Help text and a clean
  subprocess cannot establish these properties.
- Alternative verification: isolated fixture tests and construction checks
  above. They are preparation checks, not a substitute for runner admission.
- Remaining risk: model transport/tool isolation, actual message delivery,
  native instruction overlap, F6 ordering trace and blind judge export remain
  unvalidated. Temporary artifacts can disappear and must be rechecked before
  reuse. A runner change requires a new complete freeze before scoring.
- Completion: preparation is verified; D1 execution is blocked at runner
  admission. Zero scored runs, zero judge verdicts, no C1 A/B result, no F4
  sensitivity result and no retirement/retention classification.

## Role Separation

- Plan decision: bound cost before results and stop at unvalidated isolation.
- Test responsibility: verify initial suites, constructed failure paths and
  exact source attribution without scoring their author as an experimental run.
- Implementation responsibility: build only external temporary preparation
  materials and update the existing rubric; do not build an agent runtime.
- Review check: distinguish subprocess isolation from model-agent isolation,
  control readiness from control success, and source snapshots from delivery.

## Good

The stop condition prevented environment integration from becoming an unbounded
infrastructure task. Preparation has useful concrete checks without claiming
that the fixtures discriminate or that any guidance should be retired.

## Friction

The operating system can isolate Python test execution, but the model runner's
transport, native instructions and full tool boundary have not been integrated
and verified. This is a tooling/execution gap, not a rule-effectiveness finding.
It prevented Stage 1; the raw preparation record stays outside the repository.

## Proposed Follow-up

Validate one existing isolated model runner on a neutral unscored smoke task
before investing in further fixtures. Check its full tool inventory and native
instructions, then pin model/effort, delivery, F6 order export and judge exports.
Commit/freeze the final run design before starting C1; resume from verified
snapshots only. If satisfying that boundary requires a new agent runtime,
reconsider D1's cost instead of automatically expanding scope.

No policy, ADR, casebook or evaluation promotion. No CRL outcome changed.
