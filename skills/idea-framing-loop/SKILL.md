---
name: idea-framing-loop
description: "Use when the user proposes a new idea, feature concept, product/process/tool improvement, agent behavior change, or asks whether something is worth doing before planning or coding. Helps clarify goal, evidence, current workaround, target user/workflow, constraints, non-goals, smallest useful version, risks, and success criteria through one-question-at-a-time dialogue, then proposes 2-3 approaches with trade-offs and a recommendation or produces a concise idea brief. Trigger for brainstorming, office-hours-style discussion, help thinking before planning or implementation, unclear goal, scope, non-goals, success criteria, evidence, or smallest useful version."
---

# Idea Framing Loop

Use this skill to frame ideas before planning, coding, or changing a skill. It is for clarification and direction-setting, not implementation.

Do not write code while using this skill. If the idea becomes a non-trivial coding plan, hand off to `coding-review-loop` after the idea is framed.

Small ideas can stay in conversation. Create a repo-local idea brief only when it helps with review, handoff, future planning, or later implementation.

## Workflow

1. Context skim
   - When in a repo, inspect only the minimal project context needed to understand the idea.
   - Do not turn the skim into implementation planning.

2. Classify idea mode
   - product/user idea
   - developer tool idea
   - process/agent behavior idea
   - code feature idea
   - research/exploration idea

3. Ask one question at a time
   - Smart-skip questions the user already answered.
   - Ask at most 2-5 high-value questions unless the user wants deeper exploration.
   - Prefer concrete questions over broad questionnaires.

4. Clarify the useful shape
   - goal / pain
   - evidence / examples
   - current workaround
   - target user or workflow
   - constraints and non-goals
   - smallest useful version
   - risks / what would make it too heavy
   - success criteria

5. Propose 2-3 approaches
   - minimal / low-risk
   - stronger / more structured
   - too-heavy / not recommended, when useful
   - Include a recommendation and why.

6. Produce output
   - For small ideas, provide a concise conversation summary and recommendation.
   - For ideas needing review, handoff, future planning, or implementation, create a lightweight idea brief using `references/idea-brief-shape.md`.
   - Hand off to `coding-review-loop` when the framed idea becomes a non-trivial coding plan.

## Escape Hatches

- If the user says "just give me a proposal" or resists questioning, ask only the 1-2 most critical questions, then propose approaches.
- If the user already supplied a fully formed idea with evidence, skip most questions and produce the brief or recommendation.

## Idea Note Capture

At the end of an idea-framing-loop session, capture a privacy-preserving idea note in the target repo only when the discussion produced a reusable process lesson, future skill idea, non-trivial product/process decision, or handoff candidate.

Prefer `.agent/idea-framing-notes.md` when the target repo has no existing convention. If the repo should not keep agent notes, ask the user where to place the note or include the idea note in the final response.

Treat these notes as local transfer artifacts by default; do not include them in product commits unless the user or target repo convention explicitly wants agent notes committed.

Idea notes are lighter than idea briefs. Use `references/idea-brief-shape.md` when the idea needs review, handoff, future planning, or implementation. Use `references/idea-note-shape.md` only when capturing a reusable lesson or future idea without creating a full brief.

Do not record private data, credentials, customer identifiers, sensitive payloads, large code excerpts, or full chat transcripts. Generalize file paths, business identifiers, and data samples when needed.

No reusable lesson or handoff candidate does not require an idea note.

## Reference

Read `references/idea-brief-shape.md` only when creating an idea brief. Do not load it for trivial discussion.
