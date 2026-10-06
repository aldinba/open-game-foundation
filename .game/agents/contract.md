# Multi-agent development contract

This project supports multiple independent coding agents.

## Rules

- Repository files are shared memory.
- One writer owns a file or tightly coupled subsystem at a time.
- Parallel implementation uses independent scopes or isolated branches/worktrees.
- One orchestrator/integrator owns final synthesis and combined validation.
- Provider identity is metadata only and carries no technical authority.
- Preserve unrelated working-tree changes.
- Do not waive deterministic failures.
- Human/playtest evidence remains separate from automated evidence.

## Task lifecycle

Use `.game/agents/tasks/TASK-YYYYMMDD-NNN.md` for non-trivial work.

Use `.game/agents/handoffs/` when ownership changes or durable continuation context is needed.
