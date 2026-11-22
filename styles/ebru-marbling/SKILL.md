---
name: ebru-marbling
description: "Use for craft, stationery, cultural and hospitality sites in a 16th-century Ottoman ebru (marbled paper) direction: a living, interactive marbling tray built from the real fluid model (drops, stylus, comb), calm book-plate typography, procedurally marbled section rules and pattern cards, and an unhurried booking flow."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "16th-century Ottoman ebru"
  version: 4.0.0
  tier: living
---

# Ebru Marbling — Living Style

> **Living style.** This skill does not stop at colours and fonts. It gives you a signature interaction, a motion language, a section library and working code. The result should feel *alive* in a way no generic AI template does, because the movement comes from the craft itself.

## 1. Design philosophy
Ebru is paint floated on thickened water (*kitre*), pushed by new drops (*damla*), drawn with a stylus (*biz*) and pulled with a comb (*tarak*), then lifted onto a single sheet (*kâğıt*). No two prints repeat.

The interface borrows that tension: **one fluid, living surface** against an **orderly, bookish reading column**. The marbling is the only ornament. Everything around it is quiet, set like a book plate in a bindery.

The test for every decision: *would an ebru master recognise this as their process?* If a motion, texture or shape cannot be explained by drops, stylus, comb or paper, leave it out.

## 2. Colour tokens
```css
:root {
  --color-bg: #F4EEE1;        /* page: unbleached paper */
  --color-surface: #FBF7EE;   /* book plates, forms */
  --color-ink: #1E2340;       /* text = indigo pigment */
  --color-muted: #585467;
  --color-accent: #A8362B;    /* madder: primary action, scarcity, emphasis */
  --color-border: #2B3159;
  /* pigments — for marbling only, never for body text */
  --pigment-indigo: #1E2340;
  --pigment-madder: #A8362B;
  --pigment-ochre: #C99A3B;
  --pigment-verdigris: #2F6B6A;
  --stone: #F3ECDC;           /* "stone" drops and battal spots */
  --size-paper: #EDE3CC;      /* the water/size colour behind the marbling */
}
```
- Pigments are mineral and earth tones. Never neon, never purple–blue gradients.
- Madder is precious: the primary CTA, "1 seat left", an italic emphasis word. At most one madder element per view besides the marbling.

## 3. Typography
- **Display:** a humanist book serif (`'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif`), regular weight, 44–70px, tight leading (0.98–1.05). Italic carries emphasis in madder: *Lift* it onto paper.
- **Body and UI:** a calm humanist sans (`'Segoe UI', Candara, Arial, sans-serif`), 15–18px, leading 1.6.
- **Kickers and labels:** 11–12px uppercase, 0.2em tracking.
- **Craft terms** stay in Turkish with a gloss: *gelgit* (come-and-go), *biz* (stylus), *tarak* (comb), *kitre* (gum tragacanth). Never translate them away; they are the brand's authenticity.

## 4. Layout and geometry
- **Hero split:** the living tray takes 40–46% of the width at full height; the reading column takes the rest. On mobile the copy comes first and the tray follows at ~70vh.
- **Book plate:** cream label, 1px border plus an inner outline (`outline-offset: -6px`) placed on the marbling to hold one sentence. It fades once the visitor starts playing.
- **Ruled rows, not cards,** for schedules and lists: date · title + detail · action.
- **Marbled rules** (22px tall canvas strips) separate major sections instead of plain hairlines.
- Square corners everywhere. Shadows only to suggest a sheet of paper (2px hard offset), never soft glows.

## 5. Signature interaction — the tray (*tekne*)
The hero is a real marbling tray the visitor can use. This is what makes the page memorable; do not replace it with a static image or a looping video.

| Gesture | What happens | Craft meaning |
|---|---|---|
| Click / tap | A drop lands and pushes all existing paint outward | *damla* |
| Press and hold | The drop keeps growing while held (cap ≈150 units) | more paint from the brush |
| Stylus mode + drag | Paint is pulled along the path, decaying with distance | *biz* |
| Comb button | Parallel tines pass up and down → gelgit waves (animated ~0.5s) | *tarak* |
| Lift onto paper | A paper sheet lowers, the image is saved to "Your sheets" (downloadable), the tray empties | *kâğıda almak* |
| New ground | Lays a fresh combed ground with stone drops | preparing the tray |

Keyboard: the canvas is focusable; arrows move a visible ring cursor (Shift = bigger steps), Space/Enter drops; in stylus mode arrows draw. A polite live region announces combing, new ground and lifted sheets.

## 6. Motion language
| Moment | Motion | Duration / easing |
|---|---|---|
| Drop | concentric ring expands from the drop point and fades | 0.9s, `cubic-bezier(.2,.7,.2,1)` ("water") |
| Comb | the actual paint deforms, frame by frame | ~28 frames |
| Lift | cream sheet lowers over the tray, prints, lifts away | 0.7s down, 1.5s total |
| Link hover | a wavy underline flows sideways | 1.2s linear loop, only while hovered |
| Pattern card "Replay" | the card rebuilds its pattern step by step | 30–90ms per step |

Rules:
- **Motion is always the craft, never decoration.** No fade-up-on-scroll cards, no parallax, no floating blobs, no shimmer.
- Nothing moves on its own except in direct response to the visitor (or a Replay they pressed).
- `prefers-reduced-motion: reduce`: rings off, comb/lift/replay jump to the final state, hover flow off. The tray still works.

## 7. Section library
Compose pages from these, in roughly this order. Each has a defined job; do not add a generic "features" grid.

1. **Hero tray + promise** — tray, kicker, two-line display headline, one paragraph, primary + secondary action, a three-column "how to play" strip (Damla / Biz / Tarak).
2. **Method** — four square marbled canvases showing the stages (empty size with faint ripples → drops → combed → lifted sheet in a paper frame), each with a numbered serif title.
3. **Booking rows** — date / title / seat status / action; the action expands an inline form (name, email, seat stepper capped at seats left) with inline validation and a success note in a `role=status` region. Full sessions become a waitlist form.
4. **Pattern families** — cards with procedurally marbled previews (Battal, Gelgit, Şal, Bülbül yuvası, Lale, Taraklı battal), price, and a **Replay** button that rebuilds the pattern.
5. **Atelier note** — a round marbled tulip (*lale*) beside a large serif quote. Quote the workshop's own words; do not invent a named master.
6. **Footer** — indigo ground, visit hours, access info, a one-field newsletter.

## 8. Code recipes
The full, working engine is in `demo.html` (`class Marbler`, ~60 lines). Copy it rather than inventing a new one. The core maths:

```js
// DROP at c with radius r: every existing point p moves outward
// p' = c + (p - c) * sqrt(1 + r² / |p - c|²)
push(cx, cy, r) { /* apply to all points */ }
drop(cx, cy, r, color) { push(cx, cy, r); addCircle(cx, cy, r, color); refine(); }

// COMB tooth: infinite line through P with direction M; perpendicular distance d
// p' = p + M * z * u^d,  u = 0.5^(1/c)         (sharp, classic)
// p' = p + M * z * exp(-d²/c²)                  (smooth = rounder gelgit waves)

// STYLUS: same as a tooth, but d = distance to the dragged segment
// SWIRL (bülbül yuvası): rotate p around a centre by θ = a * exp(-|p - c| / c)

// REFINE: after every operation subdivide polygon edges longer than ~7 units
// (only near the visible area) so stretched paint stays smooth.
```
Recipes are lists of steps so they can be replayed:
- **Battal:** ~70 drops cycling indigo / ochre / madder / verdigris / stone, shrinking in size, then a few small stone drops.
- **Gelgit:** horizontal colour bands of random height → a few broad smooth vertical tines and gentle swirls for organic wobble → a comb of alternating smooth tines every ~50 units (`z ≈ 30–44`, `c ≈ 0.42 × spacing`).
- **Şal:** gelgit, then a finer horizontal comb.
- **Bülbül yuvası:** gelgit, then strong swirls (`a ≈ 7`, `c ≈ 48`) on an offset grid.
- **Lale:** concentric drops (madder → stone → madder → ochre), a stylus pulled down through the centre, two verdigris leaves pulled inward, a thin stem.

Performance budget: work in a fixed logical space (e.g. 1000 × 1100) scaled to the canvas with "cover" fit; cap DPR at 2; cap shapes (~500) and points per shape (~5000); redraw with one `requestAnimationFrame` per change. Initial patterns are computed synchronously so screenshots and first paint are never blank.

## 9. Imagery and texture
- The marbling **is** the imagery. Generate it with the engine, or use real scans of marbled paper the client owns.
- Real photography, if used, shows hands, trays, combs and drying sheets: close, natural light, unstyled tables.
- **Never** use AI-generated "marble texture", stock fluid-art gradients, or blurred colour blobs. They are exactly the slop this style exists to avoid.

## 10. Forbidden patterns (anti-slop)
- NEVER put body text, form fields or navigation directly on marbling (only the book plate may sit on it).
- NEVER loop an ambient animation on the tray; the paint moves only when touched.
- NEVER substitute a gradient or noise texture for real marbling.
- NEVER use generic "oriental" clichés (lanterns, random arabesques, domes) to signal Turkishness; the paper technique is enough.
- NEVER round controls into pills, add glassmorphism, or float cards with soft shadows.

## 11. Accessibility
- Text contrast AA: ink and muted pass on bg and surface; pigments are not text colours.
- The tray is an enhancement: every task (booking, buying, reading) works without touching it.
- Canvas has a descriptive `aria-label`, keyboard control and visible focus; decorative canvases are `aria-hidden`.
- Toolbar uses `role=toolbar`, pigments and tools are `radiogroup`s with `aria-checked`. Touch targets ≥ 34px in the toolbar, 44px elsewhere.
- Forms: labels, `aria-invalid`, one combined error message in `role=alert`, focus moved to the first invalid field.

## 12. Quality gate
Before delivery check: (1) Does the hero tray respond to click, hold, drag and keyboard? (2) Does anything move that the visitor did not cause? (3) Would the page still be recognisable as ebru in greyscale? (4) Is any section a generic three-card feature grid? Replace it with a section from §7. (5) Reduced-motion and mobile pass?

## Required semantic-token interface
```css
:root {
  --color-bg: #F4EEE1;
  --color-surface: #FBF7EE;
  --color-ink: #1E2340;
  --color-muted: #585467;
  --color-accent: #A8362B;
  --color-border: #2B3159;
  --font-display: 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif;
  --font-body: 'Segoe UI', Candara, Arial, sans-serif;
  --radius-control: 0px;
  --focus-ring: 3px solid var(--color-accent);
}
```
Load style tokens first, then palette tokens; a palette may recolour the six `--color-*` values and the pigments, but not the tray, the motion language or the layout.

## Invocation example
```text
Use the ebru-marbling living style. Build the hero as a working marbling tray
(drop, hold to grow, stylus, comb, lift onto paper) using the Marbler engine
from demo.html, then compose the page from the section library. Motion only
in response to the visitor; respect reduced motion. No gradients, no generic
feature grids, no invented testimonials.
```

![ebru-marbling living preview](./preview.png)

`demo.html` is a complete, interactive single-file page: open it in a browser and use the tray. The preview shows its first screen.
