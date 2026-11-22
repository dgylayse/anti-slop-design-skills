---
name: solarpunk-commons
description: "Use for cooperatives, climate, energy and civic projects in a solarpunk direction: an arched window illustration of gardens, solar roofs and turbines, leaf-cut card corners, rounded civic controls and plain-language community data."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "2020s solarpunk"
  version: 3.1.0
---

# Solarpunk Commons (Hopeful Ecological Futurism)

## 1. Design Philosophy
Solarpunk imagines a future that is green, local and repaired rather than chrome and dystopian. Visually that means hand-drawn warmth plus practical technology: solar panels on terraced houses, wind turbines beside vegetable beds. The interface is optimistic but civic: clear schedules, shared resources and plain language instead of hype.

## 2. Color Tokens & Surface Rules
```css
:root {
  --color-bg: #F3F0E2;
  --color-surface: #FFFDF3;
  --color-ink: #1E2D22;
  --color-muted: #4B5A4D;
  --color-accent: #C8691C;
  --color-border: #2F4A35;
  --leaf: #5E9A5A;
  --moss: #2F6B45;
  --sun: #F0B43C;
  --sky: #BFDCD6;
}
```
- **Rule:** `--color-accent` (#C8691C) is reserved for the primary action, the current state and one focal detail per view. Additional pigment tokens are for illustration and ornament; verify contrast before using any of them for text.

## 3. Typography & Hierarchy
- **Display font stack:** `'Constantia', 'Palatino Linotype', Georgia, serif`
- **Body font stack:** `'Candara', 'Segoe UI', sans-serif`
- Display: a warm transitional serif (Constantia) at 50–58px; italic moss-green words for the two key nouns.
- Body: a humanist sans (Candara) at 16–17px.
- Labels: 12–13px uppercase tracked, terracotta for kickers.

## 4. Layout, Grid & Geometry
- Three columns: message · tall arched illustration window (top radius ≈ half its width) · live community cards.
- Illustration uses flat shapes: sun disc, turbine, green hills, houses with patterned solar roofs, arched windows, garden beds.
- Cards use asymmetrical 'leaf' corners (`border-radius: 22px 4px 22px 4px`).
- Mobile: the arch becomes a 4:3 rounded-top banner above the text.

## 5. Component Specifications
- **Pill nav and buttons:** 40–48px tall, rounded; selected nav = filled moss.
- **Resource meter:** native `role=meter` with aria values, green bar, a plain-language takeaway sentence underneath.
- **Task list:** dashed separators, day labels in moss caps, a visible 'need N more' call for volunteers.
- **Mark:** sun disc with a leaf sprout.

## 6. Strict Forbidden Patterns (Anti-Slop Checklist)
- NEVER use dystopian neon, chrome or glassmorphism.
- NEVER invent impact statistics (CO₂ saved, households served) in production; use real data or omit.
- NEVER use stock photos of wind farms with lens flare instead of the illustrated world.
- NEVER apply terracotta to body text on cream unless contrast is verified.

---

## 7. Distinctive art direction and page anatomy

**Reference era:** 2020s solarpunk. This is a contemporary interpretation, not a reproduction of a historical artefact or a trademarked brand. Make work that feels designed by a person with a point of view.

- **Reference composition:** `message · arch window · community cards`. Lead with a purposeful hierarchy, a real content block, and the signature `arched illustration window` treatment; do not assume every product needs a dashboard.
- **Sample editorial voice:** “A street that grows its food and makes its power.”. Replace sample copy with authentic project copy; do not ship the preview's fictional brand or made-up details.
- **Use cases:** Community energy, cooperatives, urban farms, climate organisations, civic tech. Develop other applications only when the visual language matches their audience and task.
- **Key visual device:** `arched illustration window`; create it with original vector or CSS geometry, real user-provided photography, or properly licensed assets.
- **Minimum component vocabulary:** header/navigation, primary action, secondary action, content grouping, form/input, an item or list row, and visible feedback state.
- **Repeatable signature:** keep the typographic proportion and materiality on subsequent pages; vary composition based on content so the site is not one repeated hero template.

## Required semantic-token interface
The implementation MUST use these shared CSS custom properties (the palette layer may override them later):

```css
:root {
  --color-bg: #F3F0E2;
  --color-surface: #FFFDF3;
  --color-ink: #1E2D22;
  --color-muted: #4B5A4D;
  --color-accent: #C8691C;
  --color-border: #2F4A35;
  --font-display: 'Constantia', 'Palatino Linotype', Georgia, serif;
  --font-body: 'Candara', 'Segoe UI', sans-serif;
  --radius-control: 24px;
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
Use the solarpunk-commons design skill. Identify the product's core workflow, map its content hierarchy, apply its tokens and signature composition, and build a usable responsive page with real content states. Do not mimic the sample preview's fictional brand; do not introduce generic AI gradient/card patterns. Explain design choices in 5 concise sentences after implementation.
```

## 12. Visual reference

![solarpunk-commons original design preview](./preview.png)

`demo.html` is the local, self-contained composition used to generate this preview. It illustrates a style direction, not a production-ready application.
