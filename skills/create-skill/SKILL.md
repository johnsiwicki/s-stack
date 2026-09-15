---
name: create-skill
description: Create a new portable Agent Skill in this repository. Use when adding a skill, converting a Notion/Capacities/Zo workflow into SKILL.md, or when the user wants a reusable workflow that works in Cursor, Claude, Codex, Copilot, ChatGPT, Gemini, or Zo.
license: MIT
metadata:
  author: johnsiwicki
  category: meta
  status: reusable
  version: "0.1.0"
---

# Create a skill

Add one folder under `skills/` that any Agent Skills client can load.

## Do not use when

- The request is a one-off task.
- The user is asking whether to pursue an idea. Use `chief-of-staff` first.
- The work is only a trigger and prompt. Use `create-automation` and point it at an existing skill.

## Inputs

- Skill slug (lowercase hyphenated)
- What it does and when to use it
- Required inputs and expected output
- Tools or integrations, described generically
- Status: `draft`, `tested`, or `reusable`

If the slug is missing, propose one from the job to be done (`seo-title-meta-audit`, not `My SEO Skill`).

## Workflow

1. Check `skills/` so you do not duplicate an existing skill. Update the existing one if the job is the same.
2. Copy [templates/SKILL.md](../../templates/SKILL.md) to `skills/<slug>/SKILL.md`.
3. Set frontmatter:
   - `name` must match the folder
   - `description` must include trigger keywords
   - `metadata.category` one of `meta`, `content`, `client`, `ops`
   - `metadata.status` starts at `draft` unless the workflow is already proven
4. Write the body in this order: when to use, when not to, inputs, workflow, output, guardrails, example prompts.
5. Move long reference material into `references/`. Keep `SKILL.md` under 500 lines.
6. Put deterministic helpers in `scripts/` and templates in `assets/`.
7. Run `python3 scripts/validate_skills.py`.
8. Add a row to the skills table in `README.md`.

## Portability rules

- Separate the workflow from the tool.
- Prefer generic capability names: web fetch, browser, filesystem, calendar, mail draft.
- Replace secrets with environment variable names.
- Do not hardcode private file paths unless the skill cannot run without them. If you must, put them under **Compatible environments** and say what to change for other tools.
- Do not perform sends, publishes, purchases, or deletions without confirmation.
- Include failure modes: missing inputs, blocked pages, inconclusive evidence.

## Quality bar

A reusable skill tells another AI:

1. What problem it solves
2. When to use it and when not to
3. What inputs it needs
4. What output to produce
5. Which actions need confirmation
6. Where the source of truth lives (`skills/<slug>/SKILL.md`)

## Example prompts

- Add a skill for auditing title tags and meta descriptions.
- Turn my Tuesday newsletter template into a portable skill.
- Convert the Notion seo-audit page into a SKILL.md in this repo.
