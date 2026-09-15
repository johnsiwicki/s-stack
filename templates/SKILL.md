---
name: skill-slug
description: What this skill does and when an AI should use it. Include trigger keywords.
license: MIT
metadata:
  author: johnsiwicki
  category: content
  status: draft
  version: "0.1.0"
---

# Skill Name

Use this skill when the user asks for X, needs Y, or the workflow repeats often enough to standardize.

## Do not use when

- The task is a one-off and does not need a reusable workflow.
- Required inputs are missing and cannot be inferred.
- The workflow would trigger external actions without confirmation.

## Inputs

- Input 1
- Input 2

## Workflow

1. Clarify the goal only if a wrong assumption would change the output.
2. Gather the required context.
3. Execute the steps.
4. Verify the output against the quality bar.
5. Report back with files, links, or next steps.

## Output

Describe the finished result.

## Guardrails

- Do not perform external sends, publishes, purchases, or deletions without explicit confirmation.
- Do not invent metrics, quotes, or client claims.
- Do not put secrets in files, logs, or chat.
- Keep the reusable workflow in `skills/<slug>/SKILL.md`. Tool-specific glue belongs in `automations/` or a skill `scripts/` folder.

## Example prompts

- Run this skill for...
- Use this workflow to...
