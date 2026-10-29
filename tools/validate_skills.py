#!/usr/bin/env python3
"""Validate repository skill bundles without executing their scripts."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate_skill(skill: Path) -> list[str]:
    errors: list[str] = []
    main = skill / "SKILL.md"
    if not main.is_file():
        return [f"{skill.name}: missing SKILL.md"]

    text = main.read_text(encoding="utf-8-sig")
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not front:
        errors.append(f"{skill.name}: missing YAML frontmatter")
    else:
        # This is a lightweight contract check, not a complete YAML parser.
        name = re.search(r"^name:\s*['\"]?([a-z0-9-]+)['\"]?\s*$", front[1], re.M)
        if not name or name[1] != skill.name:
            errors.append(f"{skill.name}: name must match its directory")
        if not re.search(r"^description:\s*\S", front[1], re.M):
            errors.append(f"{skill.name}: missing description")

    for path in sorted(skill.rglob("*")):
        if path.is_symlink():
            errors.append(f"{path.relative_to(skill)}: symlinks are not portable bundles")
            continue
        if not path.is_file():
            continue
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
            except (SyntaxError, UnicodeError) as exc:
                errors.append(f"{path.relative_to(skill)}: {exc}")
        if path.suffix != ".md":
            continue

        content = path.read_text(encoding="utf-8-sig")
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", content):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = (path.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(skill.resolve()):
                errors.append(f"{path.relative_to(skill)}: reference escapes skill: {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(skill)}: missing reference: {target}")

        for target in re.findall(r"(?<!\w)@(references/[^\s`]+)", content):
            if not (skill / target).is_file():
                errors.append(f"{path.relative_to(skill)}: missing resource: {target}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skills = sorted(path for path in (root / "skills").iterdir() if path.is_dir())
    if not skills:
        print("No skills found", file=sys.stderr)
        return 1
    errors = [error for skill in skills for error in validate_skill(skill)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skills)} skill(s): " + ", ".join(path.name for path in skills))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
