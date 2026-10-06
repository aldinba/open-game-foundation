# Optional modules

The shared core should stay small. Add these modules only when a project actually needs them.

## Performance budget

Track project-specific thresholds such as:

- web bundle size;
- startup time;
- memory budget;
- frame-time target;
- export/package size.

Store the chosen thresholds in project documentation and report regressions during validation.

## Asset provenance

For asset-heavy games, maintain a simple ledger with:

- source/creator;
- license;
- modification notes;
- generated-vs-original status;
- shipping eligibility.

This is especially useful when mixing generated, commissioned and downloaded assets.

## Save migration policy

Once players can accumulate meaningful progress, document:

- current save schema/version;
- forward migration behavior;
- corruption/fallback behavior;
- compatibility guarantees.

## Telemetry/privacy note

If analytics or crash reporting is added, document exactly what is collected, where it goes and how it is disabled.

## Accessibility checklist

As the project matures, consider explicit checks for:

- remappable controls;
- text size/readability;
- color dependence;
- subtitles/captions;
- reduced motion;
- input alternatives.

## Release rollback

For projects with public distribution, document how to restore the previous known-good build and which state must be preserved.
