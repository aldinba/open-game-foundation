# Lessons learned from multiple game projects

These practices earned their place here because the same failure modes repeated across different projects and runtimes.

## 1. Separate process from engine

Build identity, release gates, playtest evidence and agent coordination should not depend on whether the game uses a browser stack, Godot or Unity.

Engine-specific checks belong behind the project's own validation command.

## 2. Keep one deterministic validation entry point

Every project should expose one command or script that answers: "is this repository mechanically healthy enough to hand to somebody else?"

That command can internally call type checks, engine import, unit tests, smoke tests or packaging checks.

## 3. Preserve human evidence as a separate layer

Automated checks cannot answer whether:

- movement feels good;
- controls are understandable;
- a level is fun;
- mobile layout is usable;
- network play works on real networks;
- performance is acceptable on target hardware.

Use named playtest sessions and record the exact build/commit/device/input.

## 4. Do not collapse FIXED and VERIFIED

`FIXED` means implementation changed.

`VERIFIED` means a later named build or retest demonstrated the issue no longer reproduces.

This distinction prevents optimistic closure of regressions.

## 5. Treat agent context as ephemeral

Claude, Codex, local models and future agents may not share chat history.

Project truth must live in manifests, tasks, docs, ADRs, tests and release records.

## 6. Protect parallel work with ownership

Two agents editing the same tightly coupled area produce more merge cost than speed.

Assign one writer per file/subsystem. Parallelize independent work and use one integrator for synthesis.

## 7. Do not refactor a working game just to fit the framework

Adoption should first document and validate the current architecture.

Extraction of shared runtime code should happen only after the same need appears in at least two real projects.

## 8. Separate deploy authorization from technical readiness

A clean build or packaged artifact does not imply permission to publish it.

Keep build/package, deploy and public release as distinct steps.

## 9. Document server-preserved state

Web games often have files that must survive deploys: config, uploaded data, generated state or secrets.

Explicitly document what deployment tooling must not overwrite.

## 10. Track performance budgets before they become emergencies

For browser games, record bundle/build size and startup/runtime constraints. For engine builds, record export size and target hardware expectations.

Do not enforce one universal number; use project-defined budgets and make regressions visible.

## 11. Make input semantic before device-specific

Define actions such as move, aim, jump, interact and pause first. Then map keyboard, touch, gamepad or phone-controller paths.

This makes platform expansion and controller prompts much easier.

## 12. Preserve superseded decisions

Do not delete ADRs because a decision changed. Mark them superseded and link the replacement.

Future contributors need to know why an apparently obvious alternative was rejected earlier.
