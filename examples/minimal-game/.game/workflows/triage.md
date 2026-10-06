# Finding triage workflow

1. Preserve the original observation.
2. Reproduce on the named build where possible.
3. Create a finding matching `.game/schemas/finding.schema.json`.
4. Assign type, priority, area and status independently.
5. Separate expected behavior, observed behavior and proposed solution.
6. Add deterministic regression coverage when useful and practical.
7. Set `FIXED` in the implementation build and `VERIFIED` only after later retest.

Priority model:

- `P0`: stop release work.
- `P1`: blocks normal playtest/public release.
- `P2`: may enter internal builds when documented.
- `P3`: backlog/polish.
