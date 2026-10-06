# Open Game Foundation

[![Release](https://img.shields.io/github/v/release/aldinba/open-game-foundation)](https://github.com/aldinba/open-game-foundation/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Runtime-agnostic project foundation for small and medium game teams working with humans and coding agents.

It gives a game repository a durable operating system for:

- project identity and release records;
- multi-agent collaboration;
- deterministic validation;
- playtest evidence and finding lifecycle;
- living technical/product documentation;
- safer deployment and platform evolution.

It does **not** prescribe an engine. Browser-native games, Godot, Unity and future runtimes can use the same operating contract.

## Quick start

Fastest path:

```bash
python3 scripts/init_foundation.py ../my-game \
  --slug my-game \
  --title "My Game" \
  --runtime browser \
  --implementation-root src
```

Then:

1. Read `ADOPTION.md`.
2. Replace generic documentation with repository-specific facts.
3. Expose one deterministic validation command for the actual engine/runtime.
4. Run `python3 scripts/validate_foundation.py ../my-game`.
5. Use `AGENTS.template.md` as `AGENTS.md` only if your repo does not already have stronger instructions.

Recommended target structure:

```text
.game/
  project.json
  agents/
  workflows/
  schemas/
docs/
  ARCHITECTURE.md
  GAMEPLAY.md
  CONTROLS.md
  BUILD_AND_TESTING.md
  DEPLOYMENT.md
  PLATFORM_STRATEGY.md
  decisions/
playtests/
  templates/
releases/
AGENTS.md
```

## Why this exists

The same problems repeat across game projects regardless of engine:

- contributors lose architectural context;
- chat history becomes undocumented project memory;
- parallel agents overwrite each other;
- builds pass while gameplay is still broken;
- fixes are called done before anybody retests them;
- deployment knowledge lives in one person's head;
- platform/runtime decisions are forgotten or silently reversed.

This foundation turns those concerns into repository state.

## Core principles

- Repository state is durable shared memory.
- One writer owns a file or tightly coupled subsystem at a time.
- Parallel work uses isolated scopes or branches/worktrees.
- Automation proves deterministic properties, not fun, feel or comprehension.
- `FIXED` is not `VERIFIED`.
- Deployment and publishing are separate from packaging/validation.
- Living documentation is part of Definition of Done.
- Runtime-specific details belong in project-local adapters and commands.

## What to add only when useful

This repository intentionally avoids forcing heavyweight process. Small prototypes can start with only:

- `.game/project.json`
- one validation command
- `AGENTS.md`
- `docs/BUILD_AND_TESTING.md`
- one release record

Add the rest as the project grows.

For larger or more uncertain projects, OGF also includes an optional advanced layer for assumptions, risks, experiments, role-based reviews, performance benchmarks, milestone retros and fast agent discovery. See `docs/OPTIONAL_MODULES.md`.

## Example

See `examples/minimal-game/` for a complete small adoption and `examples/browser/`, `examples/godot/`, and `examples/unity/` for runtime-specific notes.

## Languages

The reusable templates are written in English for broad reuse. `README.bs.md` explains the same model in Bosnian/BHS and can be shared directly with local teams.

## License

MIT. See `LICENSE`.
