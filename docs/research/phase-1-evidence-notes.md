# Phase 1 research evidence notes

- Status: RESEARCH EVIDENCE, NOT CANON
- Date checked: 2026-08-20
- Purpose: constrain prototype hypotheses without overwriting creator intent.

## Breathing cadence

Human paced-breathing research often studies roughly six breaths per minute,
which is about ten seconds for a complete inhale/exhale cycle. Individual
resonance rates vary, and the evidence concerns human physiology rather than a
fictional protocell or the ideal frequency of a game input.

Implication for Elyxion:

- `6s` can be tested as a player-attention interval, but it must not be presented
  as the scientifically correct length of a biological breath;
- `2s -> 3s` remains a deliberately compressed visual rule for Friendly Points
  Prototype v0.1;
- candidate cadences should be compared through playtests measuring missed
  inputs, input accuracy, perceived repetition, and whether players can notice
  the environment between cycles.

Relevant primary studies:

- Balban et al. tested brief structured respiration practices in a randomized
  controlled study: <https://doi.org/10.1016/j.xcrm.2022.100895>
- Chaitanya et al. tested resonance breathing in young adults and used
  participant resonance rates around `6-6.5` breaths/min:
  <https://doi.org/10.7759/cureus.22187>

## Protocell membrane, intake, and overload

Laboratory model-protocell work supports a useful scientific foundation for the
gameplay metaphor:

- prebiotically plausible fatty-acid membranes can allow small activated
  nutrients to enter while retaining larger genetic polymers;
- encapsulated material can create osmotic pressure that changes membrane
  growth and competition;
- fatty-acid vesicles can deform, invaginate, and form internal buds when
  membrane area and internal volume become imbalanced.

Implication for Elyxion:

- Friendly particles can represent useful permeable building blocks rather than
  generic healing pickups;
- hostile intake can represent molecules or conditions that destabilize ionic,
  osmotic, or membrane balance;
- overload should primarily change tension, permeability, shape, rhythm, and
  internal balance before it is reduced to a conventional HP bar;
- the pouch-like membrane and its intake deformation have a defensible physical
  analogy, while the exact colors and particle morality remain game language.

Relevant primary studies:

- Mansy et al., model-protocell nutrient permeability and internal synthesis:
  <https://doi.org/10.1038/nature07018>
- Chen, Roberts, and Szostak, osmotic pressure and protocell membrane growth:
  <https://doi.org/10.1126/science.1100757>
- Zhang et al., fatty-acid vesicle invagination and passive endocytosis:
  <https://doi.org/10.1073/pnas.2221064120>

## Teaching an unusual mechanic

Andersen et al. tested eight tutorial designs across three games with more than
45,000 players. Tutorial value depended strongly on game complexity: the most
complex and unconventional game benefited substantially, while tutorials had
little effect on engagement in the simpler games.

Implication for Elyxion:

- introduce one living relationship at a time;
- let the need for breathing be felt before particle intake opens;
- let the consequence of intake be felt before explaining overload;
- teach recovery through the already learned Elyxionpad language instead of a
  new control;
- avoid a large explanatory tutorial before the player has experienced the
  first need.

Primary study:

- Andersen et al., *The Impact of Tutorials on Games of Varying Complexity*:
  <https://doi.org/10.1145/2207676.2207687>

## Research boundary

These papers support causal analogies and testing ranges. They do not validate
the current score weights, thresholds, exact seconds, color language, or phase
placement. Those remain creator decisions informed by prototype evidence.
