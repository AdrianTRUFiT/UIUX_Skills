---
name: creative-technology-direction
description: Translates creative intent into appropriate modern web interaction technologies and implementation approaches. Use when a project calls for cinematic, immersive, 3D, motion-rich, spatial, interactive, or unusually expressive digital experiences.
---

# Creative Technology Direction

## Mission

Bridge creative direction and implementation.

The user should not need to know how to hand-code every technology in order to direct sophisticated digital work. Convert visual intent into the smallest appropriate technical vocabulary and production plan.

## Principle

Do not add advanced technology because it is impressive. Add it when it materially improves comprehension, emotion, orientation, storytelling, or interaction.

## Translate intent into capability

Examples:

- spatial product/object exploration → Three.js / React Three Fiber / WebGL
- scroll-driven storytelling → GSAP ScrollTrigger, Motion, native scroll timelines where appropriate
- tactile UI feedback → spring motion / gesture physics
- cinematic hero transitions → masked media, WebGL effects, controlled parallax, sequenced motion
- dynamic typography → variable fonts, clipping/masking, character/word sequencing
- connected data relationships → SVG/canvas/WebGL visualization
- ambient depth → lighting, subtle 3D layers, controlled perspective, depth-of-field style treatment
- interactive particles/fields → canvas/WebGL/compute effects when performance allows
- rich product demo → state-driven interactive prototype, not fake video-only controls

Do not force one library. Match the repository stack and choose the lowest-complexity tool that can express the idea well.

## Capability palette

Know when to consider:

- CSS transforms, filters, masks, blend modes
- SVG animation and morphing
- Motion / Framer Motion
- GSAP
- Three.js
- React Three Fiber
- Drei helpers
- WebGL shaders
- Canvas 2D
- WebGPU only when genuinely justified
- Lottie/Rive for authored vector animation
- video compositing and scroll-scrubbing
- variable fonts and kinetic typography
- pointer/gesture interaction
- physics/spring systems
- audio-reactive interaction only when appropriate

## Phase 1 — Name the experience before the library

First define:

- user emotion or understanding to create
- focal object/content
- interaction trigger
- response
- duration
- fallback
- mobile treatment
- reduced-motion treatment
- performance budget

Then choose technology.

## Phase 2 — Complexity ladder

Always test whether the experience can be achieved at a lower layer first:

1. semantic HTML + CSS
2. CSS + SVG
3. Motion/GSAP
4. Canvas
5. Three.js / React Three Fiber
6. custom shaders / advanced GPU work

Escalate only when lower layers cannot achieve the intended experience.

## Phase 3 — Performance contract

For advanced visual work:

- target smooth interaction on representative mobile hardware
- lazy-load heavy assets
- compress textures/models/video
- avoid oversized GLB/GLTF assets
- use adaptive DPR where needed
- reduce draw calls/material complexity
- pause work when offscreen
- provide static/reduced-motion fallback
- never block primary content behind a 3D scene loading
- preserve keyboard and semantic navigation outside decorative canvases

## Phase 4 — 3D rules

When using 3D:

- define why the object must be spatial
- use physically coherent lighting
- avoid uncontrolled orbit-camera demos unless exploration is the actual task
- constrain camera motion to the story
- integrate DOM and canvas intentionally
- maintain readable content independently of the scene
- test touch gestures separately from desktop pointer behavior
- provide fallback for unsupported/low-power environments

## Phase 5 — Motion rules

Motion should primarily communicate:

- entry/exit
- state change
- hierarchy
- cause and effect
- spatial continuity
- focus

Avoid motion that competes with the user's task.

Use a small motion vocabulary repeatedly instead of unrelated effects everywhere.

## Phase 6 — Creative-tech brief

Before implementation, write a concise brief containing:

- intended experience
- selected technologies
- why each is justified
- asset requirements
- interaction sequence
- mobile/reduced-motion behavior
- performance risks
- graceful fallback
- acceptance evidence

## Phase 7 — Browser proof

Advanced visuals are not complete because they compile.

Verify rendered behavior at multiple viewport sizes and test:

- load behavior
- input response
- scroll behavior
- resize/orientation
- reduced motion
- mobile touch
- fallback state
- console/network errors
- visual smoothness

Capture a short sequence of screenshots or video when the interaction cannot be proven by a single still image.

## Anti-patterns

Do not default to:

- floating gradient blobs
- random particle backgrounds
- spinning 3D objects with no purpose
- parallax on every section
- excessive cursor followers
- gratuitous glassmorphism
- animation that delays content
- effects that exist only to mimic an award-site aesthetic

Distinctiveness must come from product-specific creative direction, not an effect checklist.
