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
