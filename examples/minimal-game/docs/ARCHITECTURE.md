# Architecture

The game is a small browser-native application.

- Runtime: browser
- Implementation root: `src/`
- Entry point: `src/main.js`
- Rendering/input/game state are intentionally kept in one small module for the prototype.

If the project grows, this document should be updated before splitting major subsystem ownership.
