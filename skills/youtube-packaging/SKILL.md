---
name: youtube-packaging
description: Generate and pressure-test YouTube packaging for Stack Snacks videos: title variants, thumbnail concepts, first-30-second hooks, and description/timestamps. Use when writing or improving a video title, thumbnail, cold open, Short, or upload package, or when a video underperformed.
license: MIT
metadata:
  author: johnsiwicki
  category: content
  status: reusable
  version: "0.1.0"
---

# YouTube packaging

Produce title, thumbnail, hook, and description as **one promise**. They must agree without repeating the same words.

For rendered thumbnail art, also use `youtube-thumbnail-creator`.

## Inputs

Ask only for what changes the output:

- Topic / angle (required)
- Type: tool review, build/tutorial, comparison, news, opinion, Short
- Transcript, outline, or script if it exists
- Tool(s) and the on-screen proof
- Optional: past performers, keyword, available thumbnail assets

If only a topic is given, proceed and mark assumptions.

## Brand constraints

- Snack-sized. Completable. Not "the ultimate guide."
- Teach: imply a takeaway, not just a reaction.
- Honest. Curiosity is fine. Bait is not.
- No ALL CAPS, "INSANE," "BROKEN," "GAME CHANGER," or fake urgency.
- First person: "I built / I tested / I replaced" beats "you need to."
- If a metaphor lands in the title, do not reuse it in thumbnail text and the hook.

## Workflow

1. Extract the promise in one sentence: who + what they can do after watching. If that sentence is weak, stop and say so.
2. Identify the single most visual proof. That drives the thumbnail.
3. Generate **5 titles** from different patterns below, not five riffs on one pattern.
4. Generate **3 thumbnail concepts**, each with ≤4 words of overlay that does not repeat the title.
5. Write **3 hooks** (15–30 seconds): result cold open, problem statement, contrarian claim.
6. Score the package.
7. Draft description, timestamps, tags.
8. Recommend one default plus the strongest alternative.

## Title patterns

| Pattern | Shape | Example |
| --- | --- | --- |
| Build-instead-of-buy | I Built X to Avoid Y | I Built an X Scheduler With Zo to Avoid Another Subscription |
| Head-to-head | A vs B: the honest verdict | Claude Cowork vs Zo: Which One Actually Ships Work |
| Outcome-first | Result, then tool | This Report Writes Itself Every Monday (Zo + Claude) |
| Cost / waste | Money or time reclaimed | I Cut 4 AI Subscriptions and Lost Nothing |
| Time-boxed teach | Skill in a bounded window | Set Up Your First AI Agent in 20 Minutes |
| Contrarian | Reverse the consensus | Stop Using Agents for This |

Front-load distinct words. Keep the hook readable at ~55 characters. Do not stack a colon and parentheses.

## Thumbnail concepts

For each concept specify focal point (face, screen, or object — pick one), overlay text, visual proof, and what must read at 320px wide.

Defaults: real screen output, one arrow or circle max, high contrast, curious not shocked.

## Hooks

Write speakable lines, 40–80 words. Pay off the title in 30 seconds. No greeting or housekeeping in the first 30 seconds.

Every video also needs the spoken CTA in the first 20 seconds and at the end: one email a week at stack-snacks.com.

## Scorecard (1–5, flag under 4)

| Criterion | Question |
| --- | --- |
| Clarity | Can a stranger tell what they get in under 2 seconds? |
| Specificity | Concrete tool, number, or outcome? |
| Curiosity | Open loop worth clicking? |
| Honesty | Does the video deliver the promise? |
| Title/thumb fit | One idea, not a duplicate? |
| Searchability | Would anyone type this? |
| Brand fit | Snack-sized, teaching, first-person, non-hyped? |

## Output

Recommended package, title table, three thumbnail concepts, three hooks, description + timestamps + 5–10 tags, scorecard, and the one change that would most improve it.

## Edge cases

- No transcript: label hooks as drafts.
- Underperforming video: diagnose promise, readability, redundancy, hook delay. Swap title/thumb before re-editing.
- Comparison: do not declare a winner in the title unless the video commits to one.
- Shorts: first frame is the thumbnail. Hook in under 3 seconds.
