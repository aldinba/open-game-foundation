# Adopt the Freebit Game Foundation

Use this as an incremental repository-operations adoption. Do not refactor gameplay simply to match the template.

## 1. Inspect the target repository

Determine:

- project title and slug;
- current runtime/engine, if any;
- implementation root;
- existing version/build identity;
- build, lint and test commands;
- deployment/release mechanism;
- existing agent/repository instructions;
- existing save/settings/input/application-shell services.

Preserve existing working behavior and deployment. Do not change engine/runtime merely to adopt the foundation.

## 2. Copy the neutral structure

Copy `.game/`, `docs/`, `playtests/templates/`, `releases/template/` and `AGENTS.template.md` into the target repository.

Rename `AGENTS.template.md` to `AGENTS.md` only if an existing `AGENTS.md` is absent. If one exists, merge the Freebit requirements into it without removing project-specific instructions.

## 3. Configure `.game/project.json`

Replace every placeholder using repository evidence. Do not invent supported platforms, validation claims or release maturity.

## 4. Configure validation

The project must expose one documented deterministic validation entry point. Reuse existing commands rather than replacing mature tooling. The implementation may use npm/Vite/Three.js, Godot, Unity, native tooling or another stack.

At minimum validate:

1. project manifest;
2. build/compile/import or equivalent runtime check;
3. existing tests where present;
4. startup/smoke path where available.

## 5. Multi-agent readiness

Create an active task record for any non-trivial adoption work. Assign one writer per file/subsystem. If multiple agents implement in parallel, use isolated branches/worktrees and one integrator.

## 6. Release/playtest records

Create the first current release record from the template. Unknowns must be stated as unknown rather than promoted to passed/supported.

## 7. Runtime candidate inventory

Identify reusable candidates for settings, save/progress, input routing, controller prompts, application shell and platform adapters. Document them only during initial adoption unless extraction is already low-risk and clearly isolated.

## 8. Living documentation baseline

Adopt the smallest useful set of living documents from `docs/`:

- `ARCHITECTURE.md` for system boundaries and major data/runtime flows;
- `GAMEPLAY.md` for authoritative gameplay rules and core loops;
- `CONTROLS.md` for supported input semantics and device-specific differences;
- `BUILD_AND_TESTING.md` for deterministic local validation and what automation does not prove;
- `DEPLOYMENT.md` for release/deploy topology and operational constraints;
- `PLATFORM_STRATEGY.md` for supported/target platforms and runtime choices;
- `docs/decisions/` for durable architecture/product ADRs.

Do not duplicate the README mechanically. Link to existing authoritative documentation where it is already stronger. The goal is to make future agents able to reconstruct current project intent without relying on chat history.

## 9. Documentation completion gate

A non-trivial task is not `DONE` until the task owner has checked whether it changes any living documentation. If it does, update the relevant document in the same change or record why the documentation is intentionally unchanged.

Typical mapping:

- architecture/runtime boundary change -> `ARCHITECTURE.md`;
- gameplay rule/state/content contract change -> `GAMEPLAY.md`;
- input/control change -> `CONTROLS.md`;
- validation/build/test change -> `BUILD_AND_TESTING.md`;
- deployment/hosting/release-process change -> `DEPLOYMENT.md`;
- platform/runtime support decision -> `PLATFORM_STRATEGY.md`;
- durable tradeoff/decision -> new ADR.

## 10. Completion report

Report:

- files added/changed;
- existing tooling reused;
- current validation command and result;
- project-specific systems that remain local;
- candidate shared runtime services;
- documentation added/updated or intentionally unchanged;
- blockers or uncertain assumptions.
