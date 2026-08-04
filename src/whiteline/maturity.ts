import type { MaturityTier } from "../core/contracts.js";

export const MATURITY_BANDS = [
  { tier: "M0", minimum: 0, maximum: 24 },
  { tier: "M1", minimum: 25, maximum: 49 },
  { tier: "M2", minimum: 50, maximum: 74 },
  { tier: "M3", minimum: 75, maximum: 100 },
] as const satisfies ReadonlyArray<{
  readonly tier: MaturityTier;
  readonly minimum: number;
  readonly maximum: number;
}>;

export function maturityTierFor(score: number): MaturityTier {
  const band = MATURITY_BANDS.find(
    ({ minimum, maximum }) => score >= minimum && score <= maximum,
  );

  if (!band) {
    throw new RangeError("WhiteLine score must be between 0 and 100.");
  }

  return band.tier;
}

