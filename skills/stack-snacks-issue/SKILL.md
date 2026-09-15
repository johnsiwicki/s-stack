---
name: stack-snacks-issue
description: Draft the weekly Stack Snacks Tuesday email using Template A (five things) or Template B (honest tool review). Use when writing this week's issue, the newsletter, Substack, "Happy Tuesday Snackers," Notes, or the five-things roundup.
license: MIT
metadata:
  author: johnsiwicki
  category: content
  status: reusable
  version: "0.1.0"
---

# Stack Snacks Tuesday issue

Write the email that ships every Tuesday. Short is allowed. Skipping is not.

Default to **Template A**. Use **Template B** only when this issue is an honest tool review (about once a month). Template C is a section, or a full issue only if the week is thin.

## Do not use when

- The user wants tweets or an X thread from an issue that already exists. Use `newsletter-to-tweet`.
- The user wants video titles and thumbnails. Use `youtube-packaging`.
- The user wants a keep/cancel/wait research brief before writing. Use `keep-or-kill-review`, then come back here.
- The user is asking whether to skip Tuesday for a video or a new system. Use `chief-of-staff`. The answer is no.

## Inputs

- Template: A (default), B, or C-as-section
- The week's items, URLs, or a research dump
- Optional: last week's link, subscriber count, a tool already used on real work

If items are missing, research the week, then draft. Mark anything not personally verified as "not yet used."

## Voice

- Direct. Coffee-length. No 47-link roundups.
- Name the product and the date.
- At least one skip or "don't bother."
- At least one item that belongs in John's own stack this week.
- Subject line is specific (a product, a price, an outage), not "AI news this week."

## Template A — Tuesday five-things

**Subject:** This week in AI: {{hook in 6–8 words}}

**Preview text:** Five things that actually belong in your stack. Not 47 links.

**Notes (same day, one at a time):**

- {{steal item 1's "what it means" line}}
- {{steal item 2 or 3 as a question to readers}}
- {{one skip / unpopular take from item 5}}

Body:

```text
Happy Tuesday, Snackers 👋

{{One sentence on the week. Mood, not a recap.}} Five things that matter. Coffee-length.

**1. {{Short headline}}**
{{What happened, in 1–2 sentences. Name the product and the date.}}
*What it means:* {{Why a marketer, developer, or solo operator should care.}}
*Do this:* {{One action, or "skip."}}

**2–5.** Same shape. Item 5 can be the "not this" item. *Do this:* Skip is allowed.

That's five. Not 47.

{{Optional closer, one sentence, with a link.}}

If this was useful, forward it to one person who pays for AI tools. That's how this list grows.

See you next Tuesday.
```

Fill-this-first checklist (delete before send):

- [ ] 5 items, not 6
- [ ] At least one skip or don't bother
- [ ] At least one item John would use this week
- [ ] Every item has a *Do this*
- [ ] Subject is specific
- [ ] 3 Notes copied out before publish

## Template B — Honest tool review

Use `keep-or-kill-review` for the research, then format:

**Subject:** {{Tool}}: {{verdict in 6 words}}

**Preview text:** I used it on real work. Here's the keep / cancel / wait.

Include: what it actually does, where it earned its keep, where it failed, what it costs, **Current status:** Keeping it / canceling / waiting.

## Template C — Prompt stack

Section header: `Prompt stack: {{job to be done}}`

Include the full prompt, when to use, when not to, model used, and the one variable to change.

## Output

1. Subject, preview, full email with brackets filled
2. Three Notes, ready to paste
3. The checklist, still checked so the user can uncheck while editing
4. Do **not** send unless the user explicitly says to publish
5. For X posts from this draft, point at `newsletter-to-tweet` — do not invent a second recap thread here

## Guardrails

- Do not invent that John used a tool he did not use. Say "not tested" or pick another item.
- Do not skip the skip. A five-things with five recommendations is a listicle.
- CTA for growth is the forward line and stack-snacks.com, not a new brand.
