---
name: sunday-list-count
description: Ten-minute Sunday log of the Stack Snacks subscriber count and whether Tuesday shipped. Nothing else.
status: reusable
skill: none
---

# Sunday list count

This is the whole automation. Do not turn it into a weekly review, a new dashboard, or a plan.

## Trigger

| Field | Value |
| --- | --- |
| Type | schedule |
| When | `0 18 * * 0` (Sunday 18:00) |
| Timezone | `America/New_York` |
| Repository | none |

## Prompt

```text
Log this week's Stack Snacks scoreboard. Ten minutes of work, then stop.

Write:
1. Today's date
2. Subscriber count (look it up if you have Substack/Notion access; otherwise ask)
3. Did Tuesday's email ship? Yes/No
4. One line on whether the week stayed inside the 90-day contract

Do not propose new systems, brands, tools, or automations.
Do not draft next week's email unless asked.
If you cannot see the count, output the four-line template with COUNT and TUESDAY marked missing.
```

## Success criteria

- Four lines, then stop
- No new pages, no new skills, no "while I was here"

## Install notes

Cursor: `/automate` → paste the prompt → Sunday schedule → no repository. Prefer a Slack DM or a Notion append if those tools are connected; otherwise leave the four lines in the run output.
