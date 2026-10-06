# Prompt for Claude, Codex or a local coding agent

Adopt the Freebit Game Foundation into this game repository.

Read `FREEBIT_FOUNDATION/README.md`, `FREEBIT_FOUNDATION/ADOPTION.md` and the templates under `FREEBIT_FOUNDATION/` first.

Your objective is to add the project/process foundation while preserving the game's current gameplay, visuals, deployment and user-visible behavior.

The foundation is runtime-agnostic. Do not assume web, Godot, Unity or any other stack. Detect the repository's actual runtime/toolchain and adapt the integration to it.

Requirements:

1. Inspect the repository before changing files. Reuse existing build, test, lint and deploy conventions where possible.
2. Add/configure `.game/project.json`, agent coordination, workflows, schemas, playtest template and current release record.
3. Add or merge the repository-level `AGENTS.md` contract.
4. Configure one deterministic validation entry point using the repository's existing tooling.
5. Do not invent quality, platform-support or human-playtest claims.
6. Preserve `FIXED` versus `VERIFIED` as separate states.
7. Multi-agent support is mandatory: one writer per file/tightly-coupled subsystem, isolated branches/worktrees for parallel implementation, durable task/handoff records, one final integrator.
8. For the first adoption pass, inspect runtime services such as settings, saves, input, controller prompts, application shell and platform helpers; document reusable candidates without broad refactoring.
9. Do not change hosting, production deployment, secrets, release publication or URLs unless explicitly requested.
10. Run appropriate validation and provide a final report with changes, reused tooling, validation results, remaining game-specific systems and candidate shared modules.

If repository-specific instructions conflict with generic template examples, preserve the repository's explicit product constraints and adapt the foundation around them.
