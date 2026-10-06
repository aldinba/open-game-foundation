#!/usr/bin/env python3
"""Initialize Open Game Foundation files in an existing game repository."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def copy_tree(src: Path, dst: Path) -> None:
    for path in src.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            continue
        shutil.copy2(path, target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Adopt Open Game Foundation into a game repository.")
    parser.add_argument("target", type=Path, help="Target game repository")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--runtime", required=True, help="browser, godot, unity, or project-defined runtime")
    parser.add_argument("--implementation-root", required=True)
    parser.add_argument("--phase", default="PRE_ALPHA")
    parser.add_argument("--milestone", default="0.1")
    parser.add_argument("--build-sequence", type=int, default=1)
    parser.add_argument("--channel", default="internal", choices=["internal", "playtest", "public-demo"])
    args = parser.parse_args()

    target = args.target.resolve()
    target.mkdir(parents=True, exist_ok=True)

    copy_tree(ROOT / ".game", target / ".game")
    copy_tree(ROOT / "playtests" / "templates", target / "playtests" / "templates")
    copy_tree(ROOT / "releases" / "template", target / "releases" / "template")
    copy_tree(ROOT / "docs", target / "docs")

    agents_target = target / "AGENTS.md"
    if not agents_target.exists():
        shutil.copy2(ROOT / "AGENTS.template.md", agents_target)

    project_path = target / ".game" / "project.json"
    project = json.loads(project_path.read_text(encoding="utf-8"))
    project.update(
        {
            "slug": args.slug,
            "title": args.title,
            "phase": args.phase,
            "milestone": args.milestone,
            "buildSequence": args.build_sequence,
            "displayVersion": f"v{args.milestone}.{args.build_sequence:03d}",
            "defaultChannel": args.channel,
            "primaryRuntime": args.runtime,
            "implementationRoot": args.implementation_root,
        }
    )
    project_path.write_text(json.dumps(project, indent=2) + "\n", encoding="utf-8")

    release_dir = target / "releases" / project["displayVersion"]
    release_dir.mkdir(parents=True, exist_ok=True)
    for name in ("CHANGELOG.md", "KNOWN_ISSUES.md", "PLAYTEST_BRIEF.md"):
        src = ROOT / "releases" / "template" / name
        dst = release_dir / name
        if not dst.exists():
            shutil.copy2(src, dst)

    print(f"Initialized Open Game Foundation in {target}")
    print(f"Project: {project['title']} ({project['displayVersion']}, {project['primaryRuntime']})")
    print("Next: customize docs, configure one deterministic validation command, then run scripts/validate_foundation.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
