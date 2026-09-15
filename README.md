# s-stack

Portable **skills** and **automations** used across AI tools.

This repo is the source of truth. Cursor, Claude, Codex, Copilot, ChatGPT, Gemini, and Zo should copy from here instead of each keeping a private fork of the same workflow.

A skill is a folder with a `SKILL.md` file in the [Agent Skills](https://agentskills.io/specification) format. An automation is a trigger plus a prompt that runs a skill.

## Install

Open this repository as a workspace and most agents find `skills/` automatically through the `.agents/skills`, `.claude/skills`, and `.cursor/skills` symlinks.

### Cursor

1. Clone or add this repo as the workspace, **or**
2. Customize → Skills → From GitHub Repository → `johnsiwicki/s-stack`, **or**
3. Copy selected folders into `~/.cursor/skills/`
4. For Cloud Agents, turn on **Sync Skills for Cloud Agents** if you install them as personal skills

Create a Cursor automation from a recipe in `automations/` with `/automate`.

### Claude Code

```text
/plugin marketplace add johnsiwicki/s-stack
/plugin install s-stack@s-stack
```

Or clone the repo; `.claude/skills` points at the same files.

### Codex / ChatGPT

Codex reads `.agents/skills`. ChatGPT can use the same `SKILL.md` files in a plugin or by pasting the skill.

### GitHub Copilot

Copilot discovers `.agents/skills` (and `.claude/skills`). You can also install with `gh skill` when that CLI is available.

### Gemini, Zo, and everyone else

Copy `skills/<slug>/` into the tool's skill directory, or paste `SKILL.md` into the custom instructions / skill box. Keep the GitHub copy canonical.

## Skills

| Skill | Use when |
| --- | --- |
| [`create-skill`](skills/create-skill/SKILL.md) | Adding a new portable skill to this repo |
| [`create-automation`](skills/create-automation/SKILL.md) | Adding a scheduled or event-driven recipe |
| [`chief-of-staff`](skills/chief-of-staff/SKILL.md) | "Should I do this?", prioritization, keep/kill |
| [`stack-snacks-issue`](skills/stack-snacks-issue/SKILL.md) | Writing the Tuesday Stack Snacks email |
| [`keep-or-kill-review`](skills/keep-or-kill-review/SKILL.md) | Honest tool review with a keep / cancel / wait verdict |
| [`content-repurpose`](skills/content-repurpose/SKILL.md) | One project → video, newsletter, X, Notes |
| [`youtube-packaging`](skills/youtube-packaging/SKILL.md) | Titles, thumbnails, hooks, descriptions |
| [`youtube-thumbnail-creator`](skills/youtube-thumbnail-creator/SKILL.md) | Generating thumbnail design concepts |
| [`seo-audit`](skills/seo-audit/SKILL.md) | Practical SEO audits and action plans |
| [`website-qa-audit`](skills/website-qa-audit/SKILL.md) | Lighthouse + visual QA across viewports |
| [`tracking-pixel-audit`](skills/tracking-pixel-audit/SKILL.md) | Checking GTM, GA4, ads, and pixels on a URL |

## Automations

Recipes live in [`automations/`](automations/README.md). They are versioned prompts, not live Cursor config.

| Automation | Trigger | Skill |
| --- | --- | --- |
| [`tuesday-stack-snacks-issue`](automations/tuesday-stack-snacks-issue.md) | Tuesday morning | `stack-snacks-issue` |
| [`sunday-list-count`](automations/sunday-list-count.md) | Sunday, 10 minutes | none — log the subscriber count |

## Layout

```text
skills/<slug>/SKILL.md     canonical workflows
automations/               trigger + prompt recipes
templates/                 blank skill and automation
plugin.json                Agent plugin manifest
.cursor-plugin/            Cursor marketplace + plugin
.claude-plugin/            Claude Code marketplace + plugin
.agents/skills -> skills   Cursor, Codex, Copilot discovery
```

## Add a skill

```text
Use create-skill
```

Or copy `templates/SKILL.md` to `skills/<slug>/SKILL.md` and run:

```bash
python3 scripts/validate_skills.py
```

Rules for portable skills are in [`AGENTS.md`](AGENTS.md). The writing template matches the Capacities **AI Skill Template** and the open Agent Skills spec.

## Related

- Treehouse-only Claude marketplace (historical): [johnsiwicki/skills](https://github.com/johnsiwicki/skills)
- Agent Skills spec: [agentskills.io/specification](https://agentskills.io/specification)
