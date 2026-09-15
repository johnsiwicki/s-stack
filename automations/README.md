# Automations

Versioned recipes. They do not turn themselves on.

Cursor still configures automations in `/automate` or [cursor.com/automations](https://cursor.com/automations). Claude uses scheduled tasks. Zo uses cron. Paste the prompt from the recipe, set the trigger, then activate.

Each file should name the trigger, the skill, the exact prompt, and what "do nothing" looks like.

| Recipe | Trigger | Skill |
| --- | --- | --- |
| [tuesday-stack-snacks-issue](tuesday-stack-snacks-issue.md) | Tuesday morning | `stack-snacks-issue` |
| [sunday-list-count](sunday-list-count.md) | Sunday | none |

Add new recipes with `create-automation`.
