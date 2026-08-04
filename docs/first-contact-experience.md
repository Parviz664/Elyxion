# First-contact experience score

This document is the canonical visual-audio direction for Elyxion Phase 1. It
turns deterministic encounter outcomes into a 31-second experience without
moving game rules into a renderer.

The emotional arc is:

`stillness -> unease -> impact -> recognition -> damage -> fragile support -> recovery`

The ending is survival with a changed relationship. It is not a victory,
power-up, or complete shield.

## Timeline

| Time | Beat | World and camera | Sound | Domain event |
| --- | --- | --- | --- | --- |
| 0.0-4.0 s | Ancient stillness | Macro view of the proto planet; suspended matter drifts while the membrane breathes almost imperceptibly. | A quiet subaquatic bed, granular movement, and no melody. | Establish the untouched initial state. |
| 4.0-7.0 s | Node approach | The Red Pressure Node enters through depth rather than a hard cut. Its three inner cores rotate out of phase. | Three soft, detuned throbs establish its identity before it attacks. | The threat becomes readable without UI or exposition. |
| 7.0-10.5 s | Probe | The first core flare precedes a small local membrane ripple. Camera movement is nearly subliminal. | A rounded pressure hit with no metallic edge or explosion tail. | Tick 1: `18/pulse`; the friendly particle remains dormant. |
| 10.5-15.5 s | Recognition | Sustained deformation travels across the membrane. The friendly particle gains a faint internal pulse, but does not connect yet. | The ambient bed tightens; one restrained, glass-like particle tone appears. | Tick 2: `42/sustained`; `dormant -> recognizing`. |
| 15.5-21.5 s | Surge | The strongest strike bends the silhouette, drains color briefly, and creates the first thin connection toward the membrane. Camera impulse remains local to the planet. | The deepest pressure hit loses high frequencies and opens into a short near-silence; a warm harmonic emerges late and quietly. | Tick 3: `78/surge`; real damage occurs and `recognizing -> supporting`, but current-impact support stays weak. |
| 21.5-25.5 s | Support | A subtle green flow is visible before the last pulse. Deformation still occurs, proving the connection is not a shield. | The hit is smaller; the warm partial persists underneath rather than becoming a theme. | Tick 4: `28/pulse`; the already-supporting particle adds limited mitigation. |
| 25.5-31.0 s | Recovery | The Red Pressure Node recedes into depth. The membrane resumes uneven breathing; damage remains visible and the connection stays delicate. | The low bed returns with altered resonance. No fanfare, success sting, or spoken explanation. | End with membrane state `recovery`, not an artificial reset to `stable`. |

## Visual language

- Use a dark blue-gray, prebiotic environment with diffuse broken light and no
  visible horizon.
- Keep the membrane gelatinous and semi-transparent. Pressure must travel
  through it as deformation, not as a rigid-body collision.
- Preserve the enemy's canonical translucent-crimson body and three red-orange
  cores. The core rhythm is the primary pre-attack tell.
- Keep the friendly particle muted green. Awakening is a change in rhythm and
  internal luminance, not sudden scale or saturated glow.
- The first connection is a narrow, unstable transfer path. The membrane must
  still deform after it appears.
- Do not communicate danger only through red/green color. Silhouette change,
  rhythm, motion, and sound must carry the same information.

## Sound language

- Treat every attack as displaced pressure: low, rounded, damp, and physically
  close. Avoid gunshot transients, metallic impacts, and cinematic explosions.
- Give the Red Pressure Node three slightly detuned pulse components so its
  internal anatomy is audible.
- Use short loss of high frequencies to reinforce severe membrane impact and
  visual desaturation.
- Let the friendly particle occupy a small warm/glass-like band. It should be
  audible only after recognition and should never become heroic music.
- Recovery restores breathing and ambience imperfectly. Remaining damage must
  also be audible as an altered resonance.

## Camera and pacing

- Begin with a stable macro composition and slow parallax drift.
- Keep impact impulses centered on the proto planet and proportional to residual
  pressure. Do not shake the whole world equally for every hit.
- Hold long enough after the surge for damage and connection to be understood
  before the final pulse.
- Use no cuts during the four-impact sequence in the first prototype. Continuity
  makes cause and effect easier to read.

## Runtime contract

`src/presentation/first-contact-score.ts` derives the score from the immutable
encounter history. Every cue contains:

- a stable ID and owning emotional beat;
- an absolute start time and duration in milliseconds;
- a normalized strength from 0 to 1;
- a modality (`visual`, `audio`, or `camera`) and semantic target;
- the originating threat-signal ID when the cue comes from an impact.

The score does not name shaders, animation clips, audio files, engine nodes, or
camera APIs. A Unity, Godot, or web adapter may map cue types to implementation
assets, but it must not change encounter outcomes or reorder the domain loop.

## Prototype acceptance criteria

- The full experience lasts 31 seconds and contains seven continuous beats.
- All four threat signals produce synchronized visual, audio, and camera cues.
- Recognition, connection, and active support occur on separate impacts.
- The strongest surge is visibly and audibly stronger than the probe.
- The final pulse still damages and deforms the membrane.
- The scene is understandable in grayscale and remains readable with audio off.
- With visuals hidden, the three-core rhythm and four impacts remain audible.
- Replaying the same simulation produces an identical ordered cue score.
