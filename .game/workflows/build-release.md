# Build and release workflow

Use for internal, playtest or public-demo artifacts.

## Channels

- `internal`: development baseline; documented non-blockers may remain.
- `playtest`: named audience and hypothesis; unrelated P0/P1 findings block release.
- `public-demo`: no open P0/P1 and required platform/human evidence recorded.

## Flow

1. Confirm `.game/project.json`, release record and requested channel.
2. Record source commit and working-tree state.
3. Run the project's deterministic validation entry point for its actual runtime/toolchain.
4. Package only the requested target/platform using the project's native tooling.
5. Include `CHANGELOG.md`, `KNOWN_ISSUES.md` and `PLAYTEST_BRIEF.md`.
6. Write `BUILD_INFO.json` and checksums when packaging supports artifacts.
7. Report artifact location and validation evidence.

Packaging does not automatically authorize tagging, deploying or publishing.
