---
name: newsletter-to-tweet
description: Turn a finished newsletter or Tuesday email into X posts — a primary tweet, two alternates, and an optional short thread. Use when converting a Stack Snacks issue, Substack post, or newsletter draft into tweets, an X thread, or same-day social posts.
license: MIT
metadata:
  author: johnsiwicki
  category: content
  status: reusable
  version: "0.1.0"
---

# Newsletter to tweet

The email already exists. This skill pulls one or two ideas out of it and writes posts that can start a conversation on X. It is not a recap of the issue.

Default account job: **@siwicadilly starts a conversation.** Teach lives in the email. The post should make someone reply, quote, or click — not summarize five items.

## Do not use when

- There is no newsletter yet. Write it with `stack-snacks-issue` first.
- The user wants the full weekly package (email + video + Notes + site). Use `content-repurpose`.
- The user only wants Substack Notes. `stack-snacks-issue` already outputs those.
- The user is asking whether to skip Tuesday to post more on X. Use `chief-of-staff`. The answer is no.

## Inputs

- The newsletter: paste, file, or URL
- Optional live URL to point at (Substack / archive link)
- Optional: which item to feature, or "thread the five things"
- Optional format: `single` (default), `three-standalone`, or `thread`

If the source is a URL, fetch it. If fetch fails (paywall, login), ask for a paste. Do not invent issue contents.

## Voice

- Direct. Specific. One idea per post.
- Name the product, the price, or the skip. Vague "AI is moving fast" is a miss.
- First person: "I skipped this" / "I used this on real work" beats "you need to."
- No ALL CAPS, "INSANE," "GAME CHANGER," hashtag soup, or emoji filler.
- A skip or unpopular take outperforms a recommendation.
- The post must make sense if the reader never opens the email.

## Workflow

1. **Read the issue.** List the candidate ideas in one line each (max five). Mark which are skips, which were used on real work, and which are just news.
2. **Pick the hook.** Prefer, in order: a skip / don't-bother, a concrete verdict with a number or price, a lesson from real use, a sharp question. If nothing is specific enough, say so and quote the weakest line instead of padding.
3. **Write the primary post** (default ≤280 characters, including the link if it must live in the post). One job. No "new issue is live 🦉" as the whole tweet.
4. **Write two alternates** with different jobs from the table below. Do not riff on the same sentence three times.
5. **If the user asked for a thread,** write 3–5 posts. Tweet 1 must stand alone. Each later post is one item with a *do this* or a skip — not a paste of the email. Last post may carry the issue URL. Never thread all five items unless each has a punchline.
6. **Count characters.** Shorten until they fit. Prefer cutting throat-clearing ("Happy Tuesday," "in this week's issue") over cutting the specific noun.
7. **Place the link.** Default: primary post has no URL; issue URL is a reply. If the user wants the URL in the post, put it at the end. The URL is not the joke.
8. **Do not post** unless the user explicitly says to publish.

## Post jobs

Use three different jobs. Steal this split from `content-repurpose` when writing standalone posts:

| Job | Shape |
| --- | --- |
| Problem | Plain number, cost, or broken workflow |
| Lesson | What you kept, skipped, or would change |
| Question | Invites a reply from marketers, developers, or solo operators |

## Quality bar

A post is ready when:

- A stranger knows the product or the take in one read
- It would still be useful with the link stripped
- It does not repeat the subject line of the email
- It does not use the same metaphor as a video title/thumb if those exist (`youtube-packaging`)

## Output

Labeled drafts the user can paste:

1. **Primary** — text, character count, job
2. **Alternate A** — different job
3. **Alternate B** — different job
4. **Optional thread** — numbered, each with a character count
5. **Reply / link line** — issue URL, or this pin if no issue URL exists: `One email a week on the tools I actually keep, skip, or try. stack-snacks.com`
6. **Recommended order** — what to post now vs later the same day
7. **Assumptions** — paywalled source, missing URL, or which item you featured

If the week is crowded, ship the primary post only. The rest can wait.

## Guardrails

- Do not invent that John used a tool he did not use. Drop that item or label it "not tested."
- Do not turn the five-things email into five promotional tweets.
- Do not create a new brand, handle, or newsletter to distribute the same idea.
- Do not send, schedule, or publish without explicit confirmation.

## Example prompts

- Turn this week's Stack Snacks issue into three tweets.
- Convert this Substack URL into a primary tweet and a short thread.
- Pull the skip from this newsletter and make that the post.
- I already wrote the Tuesday email. Give me the X posts. Do not post them.
