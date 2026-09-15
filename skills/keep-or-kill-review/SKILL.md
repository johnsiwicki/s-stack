---
name: keep-or-kill-review
description: Research an AI tool and write an honest keep / cancel / wait verdict from real use. Use when reviewing a product for Stack Snacks, deciding whether to keep a subscription, drafting Template B, or answering "is this worth $X/month?"
license: MIT
metadata:
  author: johnsiwicki
  category: content
  status: reusable
  version: "0.1.0"
---

# Keep or kill review

Produce a verdict John can stand behind: **keep**, **cancel**, or **wait**. Demo tours are not reviews.

## Do not use when

- The tool was not used on real work and the user wants a shipping newsletter anyway. Say so, then either wait or write Template A instead.
- The question is "should I add another tool to the stack?" with no use case. Use `chief-of-staff`.
- The user only wants packaging for a video. Use `youtube-packaging` after the verdict exists.

## Inputs

- Tool name
- Time used and the real project it was used on
- Price, if known
- What it is supposed to replace or stack with

If time-used is missing, research publicly, then label the verdict **wait** unless the user confirms hands-on use.

## Workflow

1. Collect public facts: pricing, limits, main job, obvious competitors.
2. Separate **used** evidence from **researched** evidence.
3. Write three wins and two failures, or say there are not enough of either.
4. Answer the money question in one line: worth $X/month vs the thing it replaces?
5. Force a status: Keeping it / canceling / waiting. No "it depends" without the deciding variable.
6. Write the screenshot line: one sentence a busy person can steal.

## Output

```markdown
# {{Tool}} — {{verdict in 6 words}}

**Used on:** {{project}} for {{time}}
**Status:** Keeping it / canceling / waiting

## What it actually does
3–5 sentences. No marketing copy.

## Where it earned its keep
- win
- win
- win

## Where it failed
- miss
- miss

## What it costs
{{price}} vs {{replacement or adjacent tool}}

## Screenshot line
{{one sentence}}
```

If this is going in the Tuesday email, hand the block to `stack-snacks-issue` Template B.

## Guardrails

- Do not write "I used it" unless that is true.
- Do not treat affiliate potential as a keep reason.
- A tool that is only good content is a video topic, not a subscription.
