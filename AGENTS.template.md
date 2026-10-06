# Game agent contract

This repository supports Claude, Codex, local coding agents and future provider-neutral agents.

The project may use any engine or runtime. Do not assume web, Godot, Unity or another stack unless repository evidence says so.

Before substantial work:

1. Read `.game/project.json`.
2. Read the smallest applicable workflow under `.game/workflows/`.
3. Check active task records under `.game/agents/tasks/`.
4. Read the relevant living documentation under `docs/` before changing architecture, gameplay rules, controls, build/test, deployment or platform strategy.
5. Inspect current Git status and preserve unrelated working-tree changes.

Operational rules:

- Repository state is durable shared memory; do not depend on hidden chat history.
- Assign one writer per file or tightly coupled subsystem.
- Use independent branches/worktrees for non-trivial parallel implementation.
- Read-only reviews may run in parallel with implementation.
- Never reset, clean or overwrite another agent's work.
- Deterministic failures cannot be waived by an agent.
- Automated tests do not prove gameplay feel, fun, comprehension or external validation.
- `FIXED` is not `VERIFIED`; verification requires a later named build/retest.
- Tagging, deployment, publishing and public release remain separate actions.
- On handoff, record `RESULT / CHANGES / VALIDATION / BLOCKERS / NEXT`.
- A non-trivial task is not `DONE` until the owner has checked documentation impact and updated relevant living docs or recorded why no documentation change is needed.
- New durable architecture/product tradeoffs belong in `docs/decisions/` rather than only in chat or commit messages.
