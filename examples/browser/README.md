# Browser game example

Typical project evidence:

- runtime: `browser`;
- implementation root: `src`;
- deterministic validation: typecheck + tests + production build;
- optional smoke test in a real browser;
- deployment artifact: static build directory plus any explicitly documented server-side helpers.

Good additional checks:

- bundle-size regression;
- startup error smoke;
- keyboard/touch/gamepad input paths;
- server-preserved config/state if deploying through rsync/FTP/cPanel.
