---
name: op-art-optical
description: "Use for galleries, events and campaigns in a 1960s optical-art direction: black-and-white stripe fields and concentric vibrating circles, heavy grotesque type in solid boxes, one red point, with explicit pattern-sensitivity safeguards."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "1960s optical art"
  version: 3.1.0
---

# Op-Art Optical (1960s Retinal Art)

## 1. Design Philosophy
Op-art makes the eye do the work: regular stripes and offset circles appear to bulge and shimmer. On the web this is powerful and risky. Use the optical field as a single hero object, then lock every piece of text into solid, opaque boxes so reading is never disturbed by the pattern.

## 2. Color Tokens & Surface Rules
```css
:root {
  --color-bg: #F2F0EA;
  --color-surface: #FFFFFF;
  --color-ink: #0B0B0B;
  --color-muted: #4A4A47;
  --color-accent: #D62E1F;
  --color-border: #0B0B0B;
}
```
- **Rule:** `--color-accent` (#D62E1F) is reserved for the primary action, the current state and one focal detail per view. Additional pigment tokens are for illustration and ornament; verify contrast before using any of them for text.

## 3. Typography & Hierarchy
- **Display font stack:** `'Arial Black', 'Franklin Gothic Heavy', Impact, sans-serif`
- **Body font stack:** `Arial, Helvetica, sans-serif`
- Display: a heavy grotesque at 110–140px, uppercase, tight leading (0.84), set inside solid white or black boxes that sit on top of the pattern.
- Body: 15–16px Arial/Helvetica on solid white; never on stripes.
- Labels: 12px bold uppercase with 0.14–0.16em tracking.

## 4. Layout, Grid & Geometry
- The optical field (stripes + offset concentric circle) fills the viewport behind content; content blocks are opaque rectangles with 3px black borders.
- Anchor content to the left and bottom edges; the circle sits right-of-centre so the eye travels from headline to target.
- Exactly one red accent: the centre of the target or the status label.
- On mobile, replace the full field with a static square tile of the pattern above the content.

## 5. Component Specifications
- **Optical field:** SVG stripe pattern (12px on / 12px off) plus a stack of concentric circles whose centres shift slightly, so the rings converge to one side; a red centre point.
- **Text boxes:** inline white (or inverted black) spans behind each headline line.
- **Split action bar:** two equal buttons in one 3px-bordered bar; primary is inverted.
- **Accessibility stamp:** a solid black block naming opening hours and a low-stimulus alternative.

## 6. Strict Forbidden Patterns (Anti-Slop Checklist)
- NEVER animate the pattern (no scrolling stripes, no rotating rings); respect `prefers-reduced-motion` and offer a 'calm' toggle that swaps the field for flat colour.
- NEVER put body text, form fields or links over stripes.
- NEVER add gradients, shadows or a second accent colour.
- NEVER use fine stripes under 6px; they cause moiré on screens and in screenshots.

---

## 7. Distinctive art direction and page anatomy

**Reference era:** 1960s optical art. This is a contemporary interpretation, not a reproduction of a historical artefact or a trademarked brand. Make work that feels designed by a person with a point of view.

- **Reference composition:** `full-bleed optical field with boxed type`. Lead with a purposeful hierarchy, a real content block, and the signature `stripe and concentric-ring field` treatment; do not assume every product needs a dashboard.
- **Sample editorial voice:** “LOOK AGAIN.”. Replace sample copy with authentic project copy; do not ship the preview's fictional brand or made-up details.
- **Use cases:** Galleries, exhibitions, music events, design festivals, campaign landing pages. Develop other applications only when the visual language matches their audience and task.
- **Key visual device:** `stripe and concentric-ring field`; create it with original vector or CSS geometry, real user-provided photography, or properly licensed assets.
- **Minimum component vocabulary:** header/navigation, primary action, secondary action, content grouping, form/input, an item or list row, and visible feedback state.
- **Repeatable signature:** keep the typographic proportion and materiality on subsequent pages; vary composition based on content so the site is not one repeated hero template.

## Required semantic-token interface
The implementation MUST use these shared CSS custom properties (the palette layer may override them later):

```css
:root {
  --color-bg: #F2F0EA;
  --color-surface: #FFFFFF;
  --color-ink: #0B0B0B;
  --color-muted: #4A4A47;
  --color-accent: #D62E1F;
  --color-border: #0B0B0B;
  --font-display: 'Arial Black', 'Franklin Gothic Heavy', Impact, sans-serif;
  --font-body: Arial, Helvetica, sans-serif;
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
Use the op-art-optical design skill. Identify the product's core workflow, map its content hierarchy, apply its tokens and signature composition, and build a usable responsive page with real content states. Do not mimic the sample preview's fictional brand; do not introduce generic AI gradient/card patterns. Explain design choices in 5 concise sentences after implementation.
```

## 12. Visual reference

![op-art-optical original design preview](./preview.png)

`demo.html` is the local, self-contained composition used to generate this preview. It illustrates a style direction, not a production-ready application.
