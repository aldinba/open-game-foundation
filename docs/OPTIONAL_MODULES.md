# Optional modules

The shared core should stay small. Add these modules only when a project actually needs them.

## Evidence-driven discovery

For uncertain or high-impact work, optionally add:

- `docs/ASSUMPTIONS.md` for beliefs not yet confirmed;
- `docs/RISKS.md` for material technical/product/platform risks;
- `docs/experiments/` for hypothesis-driven POCs, benchmarks and discovery work.

Keep facts, assumptions and decisions separate. Experiments should produce evidence that either updates an assumption/risk or leads to a durable ADR/product decision.

## Role-based review perspectives

`.game/reviews/` provides optional perspectives for product, game design, UX/input, engineering, QA and release readiness.

These are review lenses, not required team roles and not AI-provider-specific skills. One person or agent may execute several perspectives. Use them only when the task complexity justifies it.

For larger features a useful order is:

`product -> game design -> UX/input -> engineering -> QA/validation plan`

Engineering review comes after intent is clear so implementation decisions do not prematurely constrain the product/gameplay review.

## Agent discovery index

Keep `AGENT_INDEX.md` as the low-cost map of project truth. It helps humans and agents locate the smallest relevant documents without crawling the entire repository.

## Performance budget

Track project-specific thresholds such as:

- web bundle size;
- startup time;
- memory budget;
- frame-time target;
- export/package size.

Store the chosen thresholds in project documentation and report regressions during validation.

When performance becomes material, adopt `docs/PERFORMANCE.md` and `.game/workflows/benchmark.md` rather than relying on informal measurements.

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

## Milestone retro

For meaningful milestones, copy `releases/template/RETRO.md` into the release record. Capture what worked, what failed, surprises and lessons worth carrying into the next milestone or back into the shared foundation.
