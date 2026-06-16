# Friction Inbox

Append-only log for lightweight friction from micro tasks or scattered observations.

## Template

```markdown
### YYYY-MM-DD - <short title>

- Context:
- What happened:
- Why it felt wrong:
- Category:
- Follow-up:
```

### 2026-06-15 - Skill install flow unclear

- Context: Using the evolving-agent-process skill and its installation notes.
- What happened: The skill install flow felt unclear.
- Why it felt wrong: It was not immediately obvious what the expected install path, copy-vs-symlink choice, or verification step should be.
- Category: `tooling`
- Follow-up: Clarify the install flow in the skill docs or installation notes before treating it as a stable default.

### 2026-06-16 - External pilot cross-artifact drift

- Context: External Stage 0 real-code pilot in an external private code project.
- What happened: The agent found and fixed cross-artifact consistency drift where the same runtime path was scattered across a template and multiple docs. Verification had mild tooling friction because the project has tests, but `pip-req.txt` did not declare `pytest`, so the local test command was not directly runnable.
- Why it felt wrong: The target repo had real consistency drift, but the pilot evidence is external and not traceable enough under the current tracker rules to count as an accepted internal dogfood task.
- Category: `process` / `cross-artifact consistency`; secondary: `tooling` / `missing test dependency`
- Follow-up: Current routing decision: friction evidence only. No evolving-agent-dev process artifacts were loaded or written inside the target repo; do not promote to casebook or evaluation-candidate evidence unless similar external real-code pilots repeat the pattern.

### 2026-06-16 - External README onboarding review gaps

- Context: Follow-up review of a README/onboarding documentation task in an external private code project.
- What happened: Setup docs did not state the Python version prerequisite even though the code uses syntax requiring Python 3.10+. The settings section told users to copy and edit the settings file, but documented only runtime path settings while the template also contained operational/deployment-specific values such as instance identity, notification endpoint, and external config path.
- Why it felt wrong: A fresh clone on an older Python could install dependencies and then fail on import or tests. A local clone could also keep unsuitable copied settings unless the README tells users to review all settings in the template.
- Verified clean points: No hard-coded fixed deployment path issue remained in README; the run command matched current server entrypoint/host/port behavior; the test command matched declared dependencies; tests require a local settings file and README documents copying it before running tests.
- Category: `setup` / `runtime prerequisite`; secondary: `process` / `cross-artifact consistency` / `config-template semantics`
- Follow-up: Privacy-preserving external friction evidence only. Do not count as an accepted internal Stage 0 dogfood task or create E008 unless the setup/runtime prerequisite gap repeats with enough judgeable evidence.
