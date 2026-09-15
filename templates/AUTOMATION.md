---
name: automation-slug
description: What this automation does and when it should fire.
status: draft
skill: skill-slug
---

# Automation Name

Portable recipe. Cursor does not yet treat repo files as live automation config, so install this by pasting it into `/automate`, a Claude scheduled task, a Zo cron, or another scheduler.

## Trigger

| Field | Value |
| --- | --- |
| Type | `schedule` / `github` / `slack` / `webhook` / `linear` |
| When | cron, event, or human instruction |
| Timezone | `America/New_York` |
| Repository | none / this repo / another repo |

## Uses skill

`skills/<slug>/SKILL.md`

## Prompt

Paste this as the automation prompt:

```text
Load skills/<slug>/SKILL.md and run it.

Goal:
Inputs:
Done when:
Do not:
```

## Tools needed

- List generic capabilities (web fetch, browser, calendar, mail draft).
- Name confirmation-gated actions separately.

## Success criteria

- What "did nothing" looks like.
- What a good run produces.
- Where the output should land.

## Install notes

- **Cursor:** `/automate` → paste the prompt → set the trigger → activate.
- **Claude:** scheduled task or Claude Code plugin with the same prompt.
- **Zo:** cron against this skill path.
- **GitHub Actions:** only if the job is deterministic scripts, not an LLM agent.
