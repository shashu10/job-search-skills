#!/usr/bin/env python3
"""Create a new private workspace from blank templates; never overwrite one."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = SKILL_ROOT / "assets" / "workspace"


def create_workspace(destination: Path, skills_dir: Path | None = None) -> Path:
    requested = destination.expanduser()
    if requested.exists() or requested.is_symlink():
        raise ValueError("Destination already exists; map or migrate it deliberately instead.")
    target = requested.resolve()
    package = SKILL_ROOT
    if SKILL_ROOT.parent.name == "skills" and (SKILL_ROOT.parent.parent / "plugin.json").is_file():
        package = SKILL_ROOT.parent.parent
    protected = [package.resolve()]
    skills: list[Path] = []
    if skills_dir is not None:
        catalog = skills_dir.expanduser().resolve(strict=True)
        if not catalog.is_dir():
            raise ValueError("The skills directory must be a directory.")
        protected.append(catalog)
        skills = sorted(p for p in catalog.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
        if not skills:
            raise ValueError("No skill folders found in the supplied directory.")
        for skill in skills:
            if skill.is_symlink() or any(p.is_symlink() for p in skill.rglob("*")):
                raise ValueError("Skill sources must contain ordinary files, not symbolic links.")
    if any(target == root or root in target.parents for root in protected):
        raise ValueError("Create the private workspace outside the public package and skill catalog.")
    if not (TEMPLATES / "AGENTS.md").is_file():
        raise ValueError("Workspace templates are unavailable.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir()  # Atomic refusal if another process created the destination.
    shutil.copytree(TEMPLATES, target, dirs_exist_ok=True)
    (target / "gitignore.template").rename(target / ".gitignore")
    if skills:
        installed = target / ".agents" / "skills"
        installed.mkdir(parents=True)
        for skill in skills:
            shutil.copytree(skill, installed / skill.name,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", ".git"))
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New private directory outside this package")
    parser.add_argument("--skills-dir", type=Path, help="Optional catalog to copy into .agents/skills")
    args = parser.parse_args()
    try:
        target = create_workspace(args.destination, args.skills_dir)
    except (ValueError, OSError) as exc:
        print(f"Workspace not completed: {exc}", file=sys.stderr)
        return 1
    print(f"Created private workspace: {target}")
    print("Open it in your agent and run job-search-setup to fill in your own facts and preferences.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
