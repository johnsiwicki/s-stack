This repository is the source of truth for John's portable AI skills and automations.

When working in this repo:

- Put reusable workflows in `skills/<slug>/SKILL.md` using the Agent Skills format.
- Put scheduled or event-driven recipes in `automations/`.
- Keep the workflow tool-agnostic. Name capabilities generically (web fetch, browser, calendar) instead of assuming one product.
- Do not invent secrets, client claims, rankings, or traffic numbers.
- Do not send, publish, purchase, or delete without explicit confirmation.
- After adding or editing a skill, run `python3 scripts/validate_skills.py`.
- Discovery folders `.agents/skills`, `.claude/skills`, and `.cursor/skills` are symlinks to `skills/`. Edit the canonical files only.
