---
name: iznik-ceramic
description: "Use for hospitality, restaurant and cultural sites in a 16th-century İznik tile direction: cobalt and bole-red repeating tile panels framing a white-slip ogee-arch content area with a clear reservation or booking form."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "16th-century İznik tilework"
  version: 3.1.0
---

# İznik Ceramic (Cobalt & Bole Tilework)

## 1. Design Philosophy
İznik ware pairs a dense, rhythmic tile field with clear white slip. The page works the same way: patterned panels at the edges, a calm white arch at the centre where the task happens. Cobalt is the ink colour; the raised bole red is precious and reserved for the single most important action.

## 2. Color Tokens & Surface Rules
```css
:root {
  --color-bg: #F7F3EA;
  --color-surface: #FFFFFF;
  --color-ink: #14295A;
  --color-muted: #4B5873;
  --color-accent: #B8322A;
  --color-border: #1F3F8A;
  --tile-turquoise: #2A8C8C;
  --tile-sage: #3E7A4F;
  --tile-slip: #F7F3EA;
}
```
- **Rule:** `--color-accent` (#B8322A) is reserved for the primary action, the current state and one focal detail per view. Additional pigment tokens are for illustration and ornament; verify contrast before using any of them for text.

## 3. Typography & Hierarchy
- **Display font stack:** `'Palatino Linotype', 'Book Antiqua', Georgia, serif`
- **Body font stack:** `'Segoe UI', Corbel, Arial, sans-serif`
- Display: a classical book serif (Palatino) at 44–56px, centred inside the arch only.
- Body and form labels: a humanist sans; labels are 11px uppercase with 0.16em tracking.
- Cobalt (#14295A) for all text; never set body text in turquoise or red.

## 4. Layout, Grid & Geometry
- Three columns on desktop: tile panel · white arch content · tile panel. The arch is the only centred element on the page.
- Draw the arch with a half-ellipse cap (`border-radius: 50% 50% 0 0 / 100% 100% 0 0`) and a small finial on the axis.
- Finish the page with a narrow repeating border band (cartouche motif) along one edge.
- On mobile, collapse the side panels into a 56px tile band at top and bottom; keep the arch full width.

## 5. Component Specifications
- **Tile pattern:** an original SVG `<pattern>` with mirrored saz-style leaves, a central rosette and corner fragments that complete when tiled; outline leaves in cobalt.
- **Reservation form:** date and guest inputs on slip background, time chips (selected = filled cobalt, unavailable = dashed + strike-through), one full-width bole-red submit.
- **Label card:** white card with a 2px cobalt border for small specials or notices placed over the tile panel.

## 6. Strict Forbidden Patterns (Anti-Slop Checklist)
- NEVER set text directly on the tile pattern.
- NEVER use more than one red element per view; bole red is the primary action only.
- NEVER copy a specific museum tile or mosque panel; design original repeats.
- NEVER round the form controls into pills or add soft shadows.

---

## 7. Distinctive art direction and page anatomy

**Reference era:** 16th-century İznik tilework. This is a contemporary interpretation, not a reproduction of a historical artefact or a trademarked brand. Make work that feels designed by a person with a point of view.

- **Reference composition:** `centred arch with tiled flanks`. Lead with a purposeful hierarchy, a real content block, and the signature `repeating tile panels` treatment; do not assume every product needs a dashboard.
- **Sample editorial voice:** “A table under the cobalt tiles.”. Replace sample copy with authentic project copy; do not ship the preview's fictional brand or made-up details.
- **Use cases:** Restaurants, tea rooms, hotels, museum shops, ceramic studios. Develop other applications only when the visual language matches their audience and task.
- **Key visual device:** `repeating tile panels`; create it with original vector or CSS geometry, real user-provided photography, or properly licensed assets.
- **Minimum component vocabulary:** header/navigation, primary action, secondary action, content grouping, form/input, an item or list row, and visible feedback state.
- **Repeatable signature:** keep the typographic proportion and materiality on subsequent pages; vary composition based on content so the site is not one repeated hero template.

## Required semantic-token interface
The implementation MUST use these shared CSS custom properties (the palette layer may override them later):

```css
:root {
  --color-bg: #F7F3EA;
  --color-surface: #FFFFFF;
  --color-ink: #14295A;
  --color-muted: #4B5873;
  --color-accent: #B8322A;
  --color-border: #1F3F8A;
  --font-display: 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
  --font-body: 'Segoe UI', Corbel, Arial, sans-serif;
  --radius-control: 0px;
  --focus-ring: 3px solid var(--color-accent);
}
```

Use `var(--color-bg)` rather than hardcoding background colors throughout components. When combining a palette, **load style tokens first, then palette tokens** (the later palette overrides the six `--color-*` values). A palette changes color only, not the style's spatial or typographic DNA.

## 8. Responsive behavior (do not skip)

- At `>= 1200px`, use the full composition described above. At `768–1199px`, reduce columns and proportionally scale headlines. Below `768px`, collapse to a single deliberate reading path; keep the primary action visible without floating overlays.
- Typography: scale the display size with `clamp()` (for example `clamp(2.5rem, 6vw, 4rem)`), keep body text between 16px and 18px.
- Use `minmax(0, 1fr)` for long content, `overflow-wrap: anywhere` for technical tokens, and a horizontal overflow wrapper for necessary data tables.
- All interactive controls have touch targets around 44×44 CSS pixels. Do not hide access to important workflows on mobile.
- Offer low-motion alternatives; respect `prefers-reduced-motion: reduce`.

## 9. Accessible components and states

- Text contrast: normal text at least WCAG AA 4.5:1 and large text at least 3:1, including muted labels. Decorative pigments and pattern colours are **not** automatically safe for foreground copy; test the actual pair.
- Keyboard: visible `:focus-visible` ring, logical tab order, Escape on dismissible overlays, proper native controls; hover is never the only feedback.
- Supply designed states: default, hover, focus, pressed, disabled, loading, empty, error, success, and selected where applicable. Announce async outcomes in a polite live region, not by color alone.
- Use semantic landmarks (`header`, `nav`, `main`, `aside`, `footer`) and ordered heading levels. Ornamental SVG uses `aria-hidden="true"`; meaningful illustrations get a short `role="img"` label.

## 10. Anti-clone quality gate

Before delivery, check: (1) Could the result be mistaken for another skill in this library? If so, change the **composition**, not merely its colors. (2) Are the content and controls plausible for the product? (3) Are there illegible labels or invented statistics? (4) Do mobile, keyboard and reduced-motion states work? (5) Has AI-default hero/card/glow styling slipped back in?

## 11. Invocation example

```text
Use the iznik-ceramic design skill. Identify the product's core workflow, map its content hierarchy, apply its tokens and signature composition, and build a usable responsive page with real content states. Do not mimic the sample preview's fictional brand; do not introduce generic AI gradient/card patterns. Explain design choices in 5 concise sentences after implementation.
```

## 12. Visual reference

![iznik-ceramic original design preview](./preview.png)

`demo.html` is the local, self-contained composition used to generate this preview. It illustrates a style direction, not a production-ready application.
