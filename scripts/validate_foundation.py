#!/usr/bin/env python3
"""Validate an Open Game Foundation adoption without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_DOCS = [
    "ARCHITECTURE.md",
    "BUILD_AND_TESTING.md",
]

REQUIRED_RELEASE_FILES = ["CHANGELOG.md", "KNOWN_ISSUES.md", "PLAYTEST_BRIEF.md"]
PLACEHOLDER_RE = re.compile(r"REPLACE_ME|TODO_FILL|CHANGEME", re.IGNORECASE)
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d{3}$")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Open Game Foundation repository structure.")
    parser.add_argument("target", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    root = args.target.resolve()
    foundation_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    warnings: list[str] = []

    project_path = root / ".game" / "project.json"
    if not project_path.exists():
        errors.append("missing .game/project.json")
        project = None
    else:
        try:
            project = json.loads(project_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid .game/project.json: {exc}")
            project = None

    if project:
        required = [
            "slug",
            "title",
            "phase",
            "milestone",
            "buildSequence",
            "displayVersion",
            "defaultChannel",
            "primaryRuntime",
            "implementationRoot",
            "releaseRecordRoot",
            "localArtifactRoot",
        ]
        for key in required:
            if key not in project or project[key] in (None, ""):
                errors.append(f"project.json missing required value: {key}")
        serialized = json.dumps(project)
        if PLACEHOLDER_RE.search(serialized):
            errors.append("project.json still contains placeholder values")
        version = project.get("displayVersion", "")
        if version and not VERSION_RE.match(version):
            errors.append(f"displayVersion must match vX.Y.NNN: {version}")
        if project.get("defaultChannel") not in {"internal", "playtest", "public-demo"}:
            errors.append("defaultChannel must be internal, playtest, or public-demo")

        if version:
            release_dir = root / project.get("releaseRecordRoot", "releases") / version
            for name in REQUIRED_RELEASE_FILES:
                if not (release_dir / name).exists():
                    errors.append(f"missing release file: {release_dir.relative_to(root) / name}")

    required_paths = [
        root / ".game" / "agents" / "contract.md",
        root / ".game" / "agents" / "tasks" / "TASK.template.md",
        root / ".game" / "agents" / "handoffs" / "HANDOFF.template.md",
        root / ".game" / "workflows" / "build-release.md",
        root / ".game" / "workflows" / "playtest.md",
        root / ".game" / "workflows" / "triage.md",
        root / "AGENTS.md",
    ]
    for path in required_paths:
        if not path.exists():
            errors.append(f"missing required foundation file: {path.relative_to(root)}")

    for schema_name in ("project.schema.json", "build.schema.json", "finding.schema.json"):
        schema_path = root / ".game" / "schemas" / schema_name
        if not schema_path.exists():
            source_schema = foundation_root / ".game" / "schemas" / schema_name
            if source_schema.exists():
                warnings.append(f"schema not copied into adoption: .game/schemas/{schema_name}")
            else:
                errors.append(f"missing schema: .game/schemas/{schema_name}")

    for name in REQUIRED_DOCS:
        if not (root / "docs" / name).exists():
            errors.append(f"missing required living doc: docs/{name}")

    optional_docs = ["GAMEPLAY.md", "CONTROLS.md", "DEPLOYMENT.md", "PLATFORM_STRATEGY.md"]
    for name in optional_docs:
        if not (root / "docs" / name).exists():
            warnings.append(f"optional doc not present: docs/{name}")

    if not (root / "playtests" / "templates" / "SESSION.md").exists():
        warnings.append("playtest session template not present")

    if not (root / "AGENT_INDEX.md").exists():
        warnings.append("agent discovery index not present: AGENT_INDEX.md")

    if errors:
        print("Foundation validation: FAILED")
        for err in errors:
            print(f"ERROR: {err}")
    else:
        print("Foundation validation: PASSED")

    for warning in warnings:
        print(f"WARN: {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
