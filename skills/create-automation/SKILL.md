---
name: create-automation
description: Create a portable automation recipe that runs a skill on a schedule or event. Use when the user wants a cron job, GitHub/Slack/Linear trigger, Cursor automation, Claude scheduled task, or Zo cron that should live in this repo.
license: MIT
metadata:
  author: johnsiwicki
  category: meta
  status: reusable
  version: "0.1.0"
---

# Create an automation

Record the trigger, prompt, and success criteria in `automations/`. Cursor automations are still configured in the product UI; this file is what you paste into `/automate` or another scheduler.

## Do not use when

- There is no skill yet. Create the skill first.
- The user wants a one-off run in the current chat.
- The job is a deterministic GitHub Action with no agent. Put that under `.github/workflows/` instead.

## Inputs

- Name and slug
- Trigger (schedule, GitHub, Slack, webhook, Linear, manual)
- Skill to run
- What a good run produces
- What "do nothing" looks like
- Confirmation-gated actions

## Workflow

1. Confirm the skill exists in `skills/`. If the workflow is new, run `create-skill` first.
2. Copy [templates/AUTOMATION.md](../../templates/AUTOMATION.md) to `automations/<slug>.md`.
3. Fill trigger, timezone (`America/New_York` unless told otherwise), tools, and the exact prompt.
4. The prompt must tell the agent which `SKILL.md` to load, what inputs to gather, and when to stop without acting.
5. Default to **draft then confirm** for anything that sends, publishes, comments publicly, or opens a PR.
6. Add a row to `automations/README.md` and the README automations table.
7. If the user wants it live in Cursor, give them the `/automate` paste, not a claim that committing the file enabled it.

## Prompt pattern

```text
Load skills/<slug>/SKILL.md and follow it.

Goal: <one sentence>
Inputs: <where to read them>
Output: <file, draft, or message>
Do not send, publish, or open a PR unless the recipe says the user already confirmed that.
If the inputs are missing, stop and report what is missing.
```

## Guardrails

- Do not invent a live Cursor YAML schema. Product automations are UI-configured; this repo stores the recipe.
- Do not put webhook secrets or API keys in the recipe.
- Prefer no-repo automations when the job is mail, research, or a digest. Attach a repo only when code must change.

## Example prompts

- Make a Tuesday morning automation that drafts the Stack Snacks email.
- Add a Sunday automation that only logs the subscriber count.
- Turn website-qa-audit into a weekly Lighthouse watch for a client URL.
