# Minimal game agent contract

Before substantial work:

1. Read `.game/project.json`.
2. Read the relevant living documentation under `docs/`.
3. Check Git status and preserve unrelated changes.

Rules:

- Repository state is durable shared memory.
- One writer owns a file or tightly coupled subsystem at a time.
- Automated checks do not prove gameplay feel or usability.
- `FIXED` is not `VERIFIED`.
- Deployment requires explicit authorization.
- Non-trivial tasks must record documentation impact.
