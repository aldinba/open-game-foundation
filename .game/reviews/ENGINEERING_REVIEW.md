# Engineering review perspective

Optional technical review after product/gameplay/UX intent is clear.

Ask:

- What subsystem owns the change?
- What dependencies or state contracts are affected?
- What can be validated deterministically?
- What regression paths need tests or smoke checks?
- Is there unnecessary architecture churn?
- Are runtime/platform constraints respected?
- Does the change require an ADR?

Prefer the smallest implementation that preserves current working behavior.

