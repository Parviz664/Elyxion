import {
  FriendlyPointEvolution,
  type FriendlyPointEvolutionSnapshot,
} from "./friendly-point-evolution.js";

const scene = requiredElement<HTMLElement>("#scene");
const membrane = requiredElement<HTMLElement>("#membrane");
const absorbedReadout = requiredElement<HTMLElement>("#absorbed-count");
const scaleReadout = requiredElement<HTMLElement>("#membrane-scale");
const breathingReadout = requiredElement<HTMLElement>("#breathing-interval");
const instruction = requiredElement<HTMLElement>("#instruction");
const evolution = new FriendlyPointEvolution();

render(evolution.snapshot());

for (const point of document.querySelectorAll<HTMLButtonElement>(
  ".friendly-point",
)) {
  point.addEventListener("click", () => {
    void enterMembrane(point);
  });
}

/** Moves a clicked point into the membrane, then records its absorption. */
async function enterMembrane(point: HTMLButtonElement): Promise<void> {
  if (point.disabled) {
    return;
  }

  point.disabled = true;
  const pointBounds = point.getBoundingClientRect();
  const membraneBounds = membrane.getBoundingClientRect();
  const offsetX =
    membraneBounds.left +
    membraneBounds.width / 2 -
    (pointBounds.left + pointBounds.width / 2);
  const offsetY =
    membraneBounds.top +
    membraneBounds.height / 2 -
    (pointBounds.top + pointBounds.height / 2);

  const movement = point.animate(
    [
      { transform: "translate(0, 0) scale(1)", opacity: 1 },
      {
        transform: `translate(${offsetX}px, ${offsetY}px) scale(0.35)`,
        opacity: 0.15,
      },
    ],
    {
      duration: 650,
      easing: "cubic-bezier(0.22, 0.8, 0.3, 1)",
      fill: "forwards",
    },
  );

  await movement.finished;
  point.remove();
  render(evolution.absorbFriendlyPoint());
}

/** Keeps the visual membrane and the small debug readout on one state. */
function render(snapshot: FriendlyPointEvolutionSnapshot): void {
  scene.style.setProperty(
    "--membrane-scale",
    snapshot.membraneScale.toString(),
  );
  scene.style.setProperty(
    "--breathing-interval",
    `${snapshot.breathingIntervalSeconds}s`,
  );

  absorbedReadout.textContent = `${snapshot.absorbedFriendlyPoints} / 5`;
  scaleReadout.textContent = snapshot.membraneScale.toFixed(1);
  breathingReadout.textContent = `${snapshot.breathingIntervalSeconds}s`;

  if (snapshot.absorbedFriendlyPoints === 3) {
    instruction.textContent = "Threshold 3 reached: membrane scale is 3.0.";
  } else if (snapshot.absorbedFriendlyPoints >= 5) {
    instruction.textContent =
      "Threshold 5 reached: scale is 5.0 and breathing is 3s.";
  } else {
    instruction.textContent = "Click a Friendly Point to absorb it.";
  }
}

function requiredElement<ElementType extends HTMLElement>(
  selector: string,
): ElementType {
  const element = document.querySelector<ElementType>(selector);

  if (element === null) {
    throw new Error(`Prototype element not found: ${selector}`);
  }

  return element;
}
