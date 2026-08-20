import {
  ManualRhythmCycle,
  type ManualRhythmCycleSnapshot,
  type ManualRhythmStage,
} from "./manual-rhythm-cycle.js";

type DragKind = "inhale" | "exhale";

interface DragSession {
  readonly kind: DragKind;
  readonly pointerId: number;
  readonly control: HTMLButtonElement;
  readonly startY: number;
  readonly targetDistance: number;
  readonly direction: -1 | 1;
  progress: number;
}

const cycle = new ManualRhythmCycle();
const scene = requiredElement<HTMLElement>("#rhythm-scene");
const membrane = requiredElement<HTMLElement>("#rhythm-membrane");
const lowerControl = requiredElement<HTMLButtonElement>("#lower-control");
const centerControl = requiredElement<HTMLButtonElement>("#center-control");
const upperControl = requiredElement<HTMLButtonElement>("#upper-control");
const resetButton = requiredElement<HTMLButtonElement>("#reset-cycle");
const instruction = requiredElement<HTMLElement>("#rhythm-instruction");
const stageReadout = requiredElement<HTMLElement>("#rhythm-stage");
const inhaleReadout = requiredElement<HTMLElement>("#inhale-time");
const holdReadout = requiredElement<HTMLElement>("#hold-time");
const exhaleReadout = requiredElement<HTMLElement>("#exhale-time");
const totalReadout = requiredElement<HTMLElement>("#total-time");

let activeDrag: DragSession | null = null;
let holdPointerId: number | null = null;
let instructionOverride: string | null = null;

lowerControl.addEventListener("pointerdown", (event) => {
  if (cycle.snapshot().stage !== "awaiting-inhale") {
    return;
  }

  cycle.beginInhale(performance.now());
  beginDrag(event, "inhale", lowerControl, -1);
});

upperControl.addEventListener("pointerdown", (event) => {
  if (cycle.snapshot().stage !== "awaiting-exhale") {
    return;
  }

  cycle.beginExhale(performance.now());
  beginDrag(event, "exhale", upperControl, 1);
});

scene.addEventListener("pointermove", (event) => {
  if (activeDrag?.pointerId === event.pointerId) {
    event.preventDefault();
    updateDrag(event.clientY);
  }
});

scene.addEventListener("pointerup", (event) => {
  if (activeDrag?.pointerId !== event.pointerId) {
    return;
  }

  event.preventDefault();
  updateDrag(event.clientY);
  finishDrag();
});

scene.addEventListener("pointercancel", (event) => {
  if (activeDrag?.pointerId === event.pointerId) {
    cancelCurrentCycle("Gesture interrupted. Start the cycle again.");
  }
});

centerControl.addEventListener("pointerdown", (event) => {
  if (cycle.snapshot().stage !== "awaiting-hold" || !isPrimaryPointer(event)) {
    return;
  }

  event.preventDefault();
  instructionOverride = null;
  holdPointerId = event.pointerId;
  centerControl.setPointerCapture(event.pointerId);
  render(cycle.beginHold(performance.now()));
});

centerControl.addEventListener("pointerup", (event) => {
  if (
    holdPointerId !== event.pointerId ||
    cycle.snapshot().stage !== "holding"
  ) {
    return;
  }

  event.preventDefault();
  releasePointer(centerControl, event.pointerId);
  holdPointerId = null;
  render(cycle.completeHold(performance.now()));
});

centerControl.addEventListener("pointercancel", (event) => {
  if (holdPointerId === event.pointerId) {
    holdPointerId = null;
    cancelCurrentCycle("Center hold interrupted. Start the cycle again.");
  }
});

resetButton.addEventListener("click", () => {
  resetVisualControls();
  instructionOverride = null;
  render(cycle.reset());
  lowerControl.focus({ preventScroll: true });
});

render(cycle.snapshot());

function beginDrag(
  event: PointerEvent,
  kind: DragKind,
  control: HTMLButtonElement,
  direction: -1 | 1,
): void {
  if (!isPrimaryPointer(event)) {
    cycle.reset();
    return;
  }

  event.preventDefault();
  instructionOverride = null;
  const controlBounds = control.getBoundingClientRect();
  const centerBounds = centerControl.getBoundingClientRect();
  const controlCenterY = controlBounds.top + controlBounds.height / 2;
  const centerY = centerBounds.top + centerBounds.height / 2;
  const targetDistance = Math.max(1, Math.abs(centerY - controlCenterY));

  activeDrag = {
    kind,
    pointerId: event.pointerId,
    control,
    startY: event.clientY,
    targetDistance,
    direction,
    progress: 0,
  };
  control.setPointerCapture(event.pointerId);
  render(cycle.snapshot());
}

function updateDrag(pointerY: number): void {
  if (activeDrag === null) {
    return;
  }

  const rawDistance =
    activeDrag.direction === -1
      ? activeDrag.startY - pointerY
      : pointerY - activeDrag.startY;
  activeDrag.progress = clamp(rawDistance / activeDrag.targetDistance, 0, 1);
  const offset =
    activeDrag.direction * activeDrag.progress * activeDrag.targetDistance;
  activeDrag.control.style.setProperty("--drag-offset", `${offset}px`);
}

function finishDrag(): void {
  if (activeDrag === null) {
    return;
  }

  const finishedDrag = activeDrag;
  releasePointer(finishedDrag.control, finishedDrag.pointerId);
  activeDrag = null;

  // This threshold is only the control's geometric hit area, not a rhythm score.
  if (finishedDrag.progress < 0.78) {
    cancelCurrentCycle("Bring the point fully into the center, then release.");
    return;
  }

  finishedDrag.control.style.setProperty(
    "--drag-offset",
    `${finishedDrag.direction * finishedDrag.targetDistance}px`,
  );

  const snapshot =
    finishedDrag.kind === "inhale"
      ? cycle.completeInhale(performance.now())
      : cycle.completeExhale(performance.now());
  render(snapshot);
}

function cancelCurrentCycle(message: string): void {
  if (activeDrag !== null) {
    releasePointer(activeDrag.control, activeDrag.pointerId);
  }

  activeDrag = null;
  holdPointerId = null;
  resetVisualControls();
  instructionOverride = message;
  render(cycle.reset());
}

function resetVisualControls(): void {
  lowerControl.style.removeProperty("--drag-offset");
  upperControl.style.removeProperty("--drag-offset");
}

function render(snapshot: ManualRhythmCycleSnapshot): void {
  scene.dataset.stage = snapshot.stage;
  membrane.dataset.stage = snapshot.stage;

  lowerControl.disabled = ![
    "awaiting-inhale",
    "inhaling",
  ].includes(snapshot.stage);
  centerControl.disabled = !["awaiting-hold", "holding"].includes(
    snapshot.stage,
  );
  upperControl.disabled = ![
    "awaiting-exhale",
    "exhaling",
  ].includes(snapshot.stage);

  lowerControl.classList.toggle(
    "is-complete",
    !["awaiting-inhale", "inhaling"].includes(snapshot.stage),
  );
  centerControl.classList.toggle(
    "is-complete",
    ["awaiting-exhale", "exhaling", "complete"].includes(snapshot.stage),
  );
  upperControl.classList.toggle("is-complete", snapshot.stage === "complete");

  stageReadout.textContent = stageLabel(snapshot.stage);
  inhaleReadout.textContent = formatMilliseconds(snapshot.inhaleTravelMs);
  holdReadout.textContent = formatMilliseconds(snapshot.centerHoldMs);
  exhaleReadout.textContent = formatMilliseconds(snapshot.exhaleTravelMs);
  totalReadout.textContent = formatMilliseconds(snapshot.totalCycleMs);
  instruction.textContent =
    instructionOverride ?? instructionForStage(snapshot.stage);
}

function stageLabel(stage: ManualRhythmStage): string {
  const labels: Readonly<Record<ManualRhythmStage, string>> = {
    "awaiting-inhale": "Ready",
    inhaling: "Inhale gesture",
    "awaiting-hold": "Center ready",
    holding: "Holding center",
    "awaiting-exhale": "Exhale ready",
    exhaling: "Exhale gesture",
    complete: "Cycle recorded",
  };

  return labels[stage];
}

function instructionForStage(stage: ManualRhythmStage): string {
  const instructions: Readonly<Record<ManualRhythmStage, string>> = {
    "awaiting-inhale": "Drag the lower point upward into the center.",
    inhaling: "Continue upward until the lower point reaches the center.",
    "awaiting-hold": "Press and hold the center.",
    holding: "Keep holding; release when the hold feels complete.",
    "awaiting-exhale": "Drag the upper split downward into the center.",
    exhaling: "Continue downward until the upper split reaches the center.",
    complete: "One full rhythm cycle recorded. No score was assigned.",
  };

  return instructions[stage];
}

function formatMilliseconds(value: number | null): string {
  return value === null ? "—" : `${Math.round(value)} ms`;
}

function releasePointer(control: HTMLElement, pointerId: number): void {
  if (control.hasPointerCapture(pointerId)) {
    control.releasePointerCapture(pointerId);
  }
}

function isPrimaryPointer(event: PointerEvent): boolean {
  return event.isPrimary && (event.pointerType !== "mouse" || event.button === 0);
}

function clamp(value: number, minimum: number, maximum: number): number {
  return Math.min(maximum, Math.max(minimum, value));
}

function requiredElement<ElementType extends HTMLElement>(
  selector: string,
): ElementType {
  const element = document.querySelector<ElementType>(selector);

  if (element === null) {
    throw new Error(`Manual rhythm prototype element not found: ${selector}`);
  }

  return element;
}
