---
name: new-wave-1980s
description: "Use for design schools, studios and culture sites in a 1980s new-wave typography direction: layered and rotated type, pastel planes, halftone dot fields, stepped rules and crosshair marks, balanced by one strictly structured information panel."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "1980s new wave typography"
  version: 3.1.0
---

# New Wave Typography (1980s Basel / LA)

## 1. Design Philosophy
New wave typography took the Swiss grid and deliberately broke it: type layered, rotated, outlined, overprinted with dots and pastel planes. The trick is controlled chaos. One half of the page is an expressive collage; the other half is a calm, perfectly aligned panel where people actually read and act.

## 2. Color Tokens & Surface Rules
```css
:root {
  --color-bg: #EEE8DC;
  --color-surface: #FAF7F0;
  --color-ink: #1A1A1A;
  --color-muted: #524E47;
  --color-accent: #E2492F;
  --color-border: #1A1A1A;
  --plane-pink: #F3B3C3;
  --plane-teal: #4FA9A2;
  --plane-yellow: #F2CF4A;
}
```
- **Rule:** `--color-accent` (#E2492F) is reserved for the primary action, the current state and one focal detail per view. Additional pigment tokens are for illustration and ornament; verify contrast before using any of them for text.

## 3. Typography & Hierarchy
- **Display font stack:** `'Bahnschrift', 'Arial Narrow', Arial, sans-serif`
- **Body font stack:** `'Segoe UI', Arial, sans-serif`
- Display: a geometric/DIN-like sans (Bahnschrift) at 150–250px, mixing solid, outlined (`-webkit-text-stroke`) and rotated (−6° to −10°) words.
- Use letter-spaced small display (0.18em) for codes like season or issue numbers.
- Vertical micro-text (writing-mode) along one edge for a manifesto line.
- Body and panels: 13–16px Segoe UI/Arial, never rotated.

## 4. Layout, Grid & Geometry
- Left 60%: collage of pastel rectangles, a halftone dot field (radial-gradient pattern), a circle, a stair-step rule and registration crosshairs.
- Right 30–35%: a bordered panel with numbered rows and a full-width black CTA; aligned to a strict baseline.
- Overlaps are deliberate: type crosses planes, but never crosses the panel.
- Below 768px, stack: compact collage strip (max 40vh) → panel → description.

## 5. Component Specifications
- **Crosshair marks:** 22px plus-signs drawn with pseudo-elements at plane corners.
- **Halftone field:** `radial-gradient(var(--color-ink) 1.6px, transparent 1.8px)` at 9px spacing.
- **Course rows:** big numeral, title + meta, outlined status tag (dashed when waitlisted).
- **CTA bar:** black full-width bar with yellow arrow.

## 6. Strict Forbidden Patterns (Anti-Slop Checklist)
- NEVER rotate or layer interactive text, form labels or prices.
- NEVER use neon or synthwave gradients; this is print-derived pastel + black.
- NEVER apply the collage to every page; use it on landing/section openers only.
- NEVER centre the composition symmetrically.

---

## 7. Distinctive art direction and page anatomy

**Reference era:** 1980s new wave typography. This is a contemporary interpretation, not a reproduction of a historical artefact or a trademarked brand. Make work that feels designed by a person with a point of view.

- **Reference composition:** `collage half + strict panel`. Lead with a purposeful hierarchy, a real content block, and the signature `layered rotated type and halftone planes` treatment; do not assume every product needs a dashboard.
- **Sample editorial voice:** “new wave” / “Layer · rotate · break the grid · then rebuild it.”. Replace sample copy with authentic project copy; do not ship the preview's fictional brand or made-up details.
- **Use cases:** Design schools, studios, music, culture programmes, portfolios. Develop other applications only when the visual language matches their audience and task.
- **Key visual device:** `layered rotated type and halftone planes`; create it with original vector or CSS geometry, real user-provided photography, or properly licensed assets.
- **Minimum component vocabulary:** header/navigation, primary action, secondary action, content grouping, form/input, an item or list row, and visible feedback state.
- **Repeatable signature:** keep the typographic proportion and materiality on subsequent pages; vary composition based on content so the site is not one repeated hero template.

## Required semantic-token interface
The implementation MUST use these shared CSS custom properties (the palette layer may override them later):

```css
:root {
  --color-bg: #EEE8DC;
  --color-surface: #FAF7F0;
  --color-ink: #1A1A1A;
  --color-muted: #524E47;
  --color-accent: #E2492F;
  --color-border: #1A1A1A;
  --font-display: 'Bahnschrift', 'Arial Narrow', Arial, sans-serif;
  --font-body: 'Segoe UI', Arial, sans-serif;
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
Use the new-wave-1980s design skill. Identify the product's core workflow, map its content hierarchy, apply its tokens and signature composition, and build a usable responsive page with real content states. Do not mimic the sample preview's fictional brand; do not introduce generic AI gradient/card patterns. Explain design choices in 5 concise sentences after implementation.
```

## 12. Visual reference

![new-wave-1980s original design preview](./preview.png)

`demo.html` is the local, self-contained composition used to generate this preview. It illustrates a style direction, not a production-ready application.
