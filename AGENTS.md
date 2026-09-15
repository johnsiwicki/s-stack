# AGENTS.md

This repository is the source of truth for reusable AI skills and automations.

Capacities, Notion, Zo, Cursor, Claude, Codex, Copilot, ChatGPT, and Gemini should copy from here. They should not become competing sources of the same workflow.

## What belongs where

| Path | Put this here |
| --- | --- |
| `skills/<slug>/SKILL.md` | The portable workflow: when to use it, inputs, steps, output, guardrails |
| `skills/<slug>/references/` | Detail loaded only when needed |
| `skills/<slug>/scripts/` | Deterministic helpers the agent can run |
| `skills/<slug>/assets/` | Templates and other static files |
| `automations/` | Trigger + prompt recipes that call a skill |
| `templates/` | Blank skill and automation files |

Do not store all skills in one note. Each skill is its own folder.

## Skill contract

Follow the [Agent Skills](https://agentskills.io/specification) spec:

- Folder name = `name` frontmatter = lowercase hyphenated slug
- `description` says what it does **and** when to use it
- Body stays under ~500 lines
- No secrets, no hardcoded private paths unless the skill cannot run without them
- External actions need confirmation

Use `templates/SKILL.md` for new skills. Use the `create-skill` skill when adding one.

## Discovery

Canonical files live in `skills/`.

These paths are symlinks to the same folder so tools auto-discover them when this repo is the workspace:

- `.agents/skills` — Cursor, Codex, GitHub Copilot
- `.claude/skills` — Claude Code
- `.cursor/skills` — Cursor

Plugins also load `skills/` via `.cursor-plugin/` and `.claude-plugin/`.

## Automations

Cursor automations are still configured in the product UI (`/automate` or cursor.com/automations). Files in `automations/` are the versioned recipes to paste there, or into Claude scheduled tasks / Zo cron.

An automation should name:

1. The trigger
2. The skill it runs
3. The exact prompt
4. What "do nothing" looks like
5. Confirmation-gated actions

## Guardrails

- Separate the workflow from the tool.
- Prefer one original idea a week over a new agent architecture.
- Tuesday Stack Snacks email is the publishing floor. Do not skip it to build systems.
- If a request is "should I do this?", use `chief-of-staff` before creating a new skill or automation.
