---
name: tuesday-stack-snacks-issue
description: Draft the Stack Snacks Tuesday email every week. Does not send.
status: reusable
skill: stack-snacks-issue
---

# Tuesday Stack Snacks issue

## Trigger

| Field | Value |
| --- | --- |
| Type | schedule |
| When | `0 8 * * 2` (Tuesday 8:00) |
| Timezone | `America/New_York` |
| Repository | none, or this repo if you want the skill files cloned |

## Uses skill

`skills/stack-snacks-issue/SKILL.md`

## Prompt

```text
Load skills/stack-snacks-issue/SKILL.md and draft this week's Stack Snacks Tuesday email.

Use Template A (five things) unless the user already decided this week is an honest tool review.

Research the week. Prefer items John could actually use. Include at least one skip.
Also write the three Notes from the template.

Do not send, publish, or post. Leave a draft the human can edit.
If you cannot find five honest items, write fewer and say what is missing rather than padding.
```

## Tools needed

- Web search / fetch for the week's launches
- Notion or Hub access if connected, for the content calendar
- Mail draft only if the user later confirms send

## Success criteria

- A complete Template A or B draft with subject, preview, body, and three Notes
- Checklist included
- No send

## Install notes

Cursor: `/automate` → paste the prompt → Tuesday schedule → no repository (or `s-stack`) → activate. Keep send disabled.
