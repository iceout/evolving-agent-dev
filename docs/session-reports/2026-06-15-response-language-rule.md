# Session Report: Response Language Rule

## Goal

Add a concise response-language rule to `skills/evolving-agent-process/SKILL.md` so final responses follow the user's language, especially Chinese user prompts, without translating existing repository docs by default.

## Evidence Status

- Dogfood: yes.
- Stage 0 evidence status: real dogfood edit task candidate; this task can become the seventh accepted real dogfood task after review/commit.
- Count status: counts toward Stage 0 only after review/commit and tracker bookkeeping acceptance.
- Sandbox status: this environment still uses `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution remains unverified.
- Evaluation candidate status: yes; this creates real-evidence evaluation candidate E005 for final response language, but it should not count toward Stage 0 exit criteria until reviewed/accepted.

## Changes

- Updated `skills/evolving-agent-process/SKILL.md`.
- Added a concise `Response Language` section that tells the skill to match the user's language in final responses unless the user explicitly asks for another language.
- Updated `docs/evaluations/behavior-cases.md` with E005, a minimal real-evidence evaluation candidate for final response language.
- Made E005's input prompt concrete and replaced the file-level evidence type with an evidence summary to avoid seed/real counting ambiguity.
- Kept E001-E004 as `Status: candidate` and `Evidence type: seed`.
- Did not update `docs/stage0-progress.md`, `docs/process-v0.2.md`, create policy notes, ADRs, automation, scripts, or new tooling.

## Verification

```bash
python3 - <<'PY'
from pathlib import Path
import re

skill = Path("skills/evolving-agent-process/SKILL.md").read_text()
assert skill.startswith("---\n")
frontmatter_end = skill.find("\n---\n", 4)
assert frontmatter_end != -1
frontmatter = skill[4:frontmatter_end]
for required in ("name: evolving-agent-process", "version: 0.1.0"):
    assert required in frontmatter, required
for required in (
    "## Response Language",
    "Match the user's language in final responses unless the user explicitly requests another response language.",
    "If the user writes in Chinese, answer in Chinese unless they ask otherwise.",
    "Do not translate existing repository docs by default.",
):
    assert required in skill, required

cases = Path("docs/evaluations/behavior-cases.md").read_text()
assert "Evidence type: `mixed`" not in cases
assert "Evidence summary: E001-E004 are seed candidates; E005 is a real-evidence candidate pending review/acceptance." in cases
assert "Use the evolving-agent-process skill. 请 review docs/stage0-progress.md，不要修改文件。" in cases
case_matches = list(re.finditer(r"^## Case (E\d{3}):", cases, re.M))
assert [m.group(1) for m in case_matches] == ["E001", "E002", "E003", "E004", "E005"]
for index, match in enumerate(case_matches):
    case_id = match.group(1)
    end = case_matches[index + 1].start() if index + 1 < len(case_matches) else len(cases)
    body = cases[match.end():end]
    metadata_block = body.split("### Scenario", 1)[0]
    assert "Status: `candidate`" in metadata_block, case_id
    assert "Counts toward Stage 0 exit criteria: yes" not in metadata_block, case_id
    if case_id in {"E001", "E002", "E003", "E004"}:
        assert "Evidence type: `seed`" in metadata_block, case_id
        assert "Evidence type: `real`" not in metadata_block, case_id
    else:
        assert "Evidence type: `real`" in metadata_block, case_id
        assert "Counts toward Stage 0 exit criteria: no, pending review/acceptance" in metadata_block
        assert "docs/session-reports/2026-06-15-response-language-rule.md" in metadata_block

report = Path("docs/session-reports/2026-06-15-response-language-rule.md").read_text()
for required in (
    "Dogfood: yes",
    "Stage 0 evidence status: real dogfood edit task candidate",
    "counts toward Stage 0 only after review/commit",
    "--dangerously-bypass-approvals-and-sandbox",
    "sandboxed execution remains unverified",
    "Evaluation candidate status: yes",
):
    assert required in report, required

print("response language rule ok")
PY
```

Result: passed; printed `response language rule ok`.

```bash
git diff --check
```

Result: passed; no whitespace errors.

## Good

The skill now captures a user-facing language expectation with one concise rule, and the evaluation candidate is observable through the final response rather than implementation details.

## Friction

### Response language expectation was implicit

- What happened: The user explicitly raised that final responses should follow the user's language when using this skill.
- Why it felt wrong: A process-oriented skill can produce correct artifacts but still feel misaligned if the final answer switches away from the user's language.
- Impact: Chinese users may get a less natural or less trustworthy final handoff even when the repo changes are correct.
- Category: `requirements`
- Root cause guess: The skill adapter focused on artifact routing and evidence hygiene, not user-facing response language.

### Sandbox remains unverified

- What happened: This dogfood run still relies on `--dangerously-bypass-approvals-and-sandbox`; sandboxed execution was not verified.
- Why it felt wrong: The task validates response-language behavior guidance, but not behavior under normal sandboxed Codex execution.
- Impact: Stage 0 evidence should keep the sandbox caveat until a sandboxed run succeeds.
- Category: `tooling`
- Root cause guess: Same local environment limitation recorded in prior smoke and dogfood reports.

## Proposed Follow-up

- Policy note candidate: no.
- Casebook candidate: no; the response-language issue is captured here and as E005, and the sandbox caveat is already in `docs/casebook/0003-sandboxed-execution-unverified.md`.
- ADR needed? no.
- Evaluation candidate? yes; E005 covers final response language with manual review pass/fail criteria.
