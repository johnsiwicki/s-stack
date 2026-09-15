#!/usr/bin/env python3
"""Validate Agent Skills in this repo against the portable SKILL.md contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter delimited by ---")
    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line or line.startswith(" ") or line.startswith("\t") or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key:
            data[key] = value
    return data


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    try:
        meta = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]

    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        errors.append(f"{skill_dir.name}: frontmatter is missing name")
    elif name != skill_dir.name:
        errors.append(
            f"{skill_dir.name}: name '{name}' must match the folder name"
        )
    elif not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(
            f"{skill_dir.name}: name must be 1-64 chars of lowercase, numbers, and single hyphens"
        )

    if not description:
        errors.append(f"{skill_dir.name}: frontmatter is missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_dir.name}: description exceeds 1024 characters")

    if len(text.splitlines()) > 500:
        errors.append(
            f"{skill_dir.name}: SKILL.md is over 500 lines; move detail into references/"
        )

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("skills/ directory is missing", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("no skill directories found under skills/", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    for skill_dir in skill_dirs:
        print(f"  ok  {skill_dir.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
