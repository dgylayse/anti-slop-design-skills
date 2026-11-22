---
name: illuminated-manuscript
description: "Use for archives, libraries, heritage and long-form reading sites in an illuminated manuscript direction: vellum ground, ruled two-column justified text, a painted initial, red rubrics, vine marginalia and folio navigation."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "13th–15th-century illuminated manuscripts"
  version: 3.1.0
---

# Illuminated Manuscript (Medieval Book Hand)

## 1. Design Philosophy
A manuscript page is an interface designed over centuries: ruling lines for rhythm, red rubrics for wayfinding, painted initials to mark where a text begins, marginal vines to frame. Use those devices as navigation and hierarchy, not as fantasy decoration, and keep the reading experience generous and calm.

## 2. Color Tokens & Surface Rules
```css
:root {
  --color-bg: #F2E8D0;
  --color-surface: #F8F1DF;
  --color-ink: #2A1D14;
  --color-muted: #5C4A39;
  --color-accent: #9B2A1F;
  --color-border: #6B4E2E;
  --gold: #C79A2E;
  --lapis: #26437A;
  --verdigris: #3F6B4A;
}
```
- **Rule:** `--color-accent` (#9B2A1F) is reserved for the primary action, the current state and one focal detail per view. Additional pigment tokens are for illustration and ornament; verify contrast before using any of them for text.

## 3. Typography & Hierarchy
- **Display font stack:** `'Palatino Linotype', 'Book Antiqua', Georgia, serif`
- **Body font stack:** `'Palatino Linotype', 'Book Antiqua', Georgia, serif`
- One old-style serif family (Palatino) for everything; hierarchy through size, small caps and colour.
- Rubrics (section openers, nav, buttons) in small caps, 0.06–0.14em tracking, vermilion.
- Body 18px on a 32px baseline, justified with hyphenation, in two columns with a thin column rule.
- One painted initial (≈ 3.5 lines tall) per page, lapis ground, gold letter, small vine and dots.

## 4. Layout, Grid & Geometry
- Grid: a 150px decorated margin (vine, leaves, gold and vermilion dots) · reading block · a surface-coloured sidebar for indexes.
- Faint ruling lines repeat at the text baseline across the reading block.
- Header uses a double rule below; a catchword at the end of a column or sidebar hints at what comes next.
- Mobile: drop to a single column, move the vine to a 24px top border strip.

## 5. Component Specifications
- **Search:** bordered field on surface with a vermilion 'Seek' button in small caps.
- **Folio list:** square thumbnail with a symbol (✠ ❦ ¶), title with folio number, italic note.
- **Folio pager:** previous/next folio in small caps with a keyboard hint.
- **Uncertain text:** mark editorial doubt with [square brackets], never guess.

## 6. Strict Forbidden Patterns (Anti-Slop Checklist)
- NEVER use blackletter for body text or UI; it fails readability.
- NEVER use gold for text; it is ornament only.
- NEVER fake parchment with heavy noise or burnt edges.
- NEVER put more than one painted initial in a viewport.

---

## 7. Distinctive art direction and page anatomy

**Reference era:** 13th–15th-century illuminated manuscripts. This is a contemporary interpretation, not a reproduction of a historical artefact or a trademarked brand. Make work that feels designed by a person with a point of view.

- **Reference composition:** `margin vine · ruled two-column text · index sidebar`. Lead with a purposeful hierarchy, a real content block, and the signature `painted initial and vine margin` treatment; do not assume every product needs a dashboard.
- **Sample editorial voice:** “Two hundred leaves of vellum, read closely.”. Replace sample copy with authentic project copy; do not ship the preview's fictional brand or made-up details.
- **Use cases:** Archives, libraries, rare books, heritage, wineries, long-form reading, fantasy games. Develop other applications only when the visual language matches their audience and task.
- **Key visual device:** `painted initial and vine margin`; create it with original vector or CSS geometry, real user-provided photography, or properly licensed assets.
- **Minimum component vocabulary:** header/navigation, primary action, secondary action, content grouping, form/input, an item or list row, and visible feedback state.
- **Repeatable signature:** keep the typographic proportion and materiality on subsequent pages; vary composition based on content so the site is not one repeated hero template.

## Required semantic-token interface
The implementation MUST use these shared CSS custom properties (the palette layer may override them later):

```css
:root {
  --color-bg: #F2E8D0;
  --color-surface: #F8F1DF;
  --color-ink: #2A1D14;
  --color-muted: #5C4A39;
  --color-accent: #9B2A1F;
  --color-border: #6B4E2E;
  --font-display: 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
  --font-body: 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
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
Use the illuminated-manuscript design skill. Identify the product's core workflow, map its content hierarchy, apply its tokens and signature composition, and build a usable responsive page with real content states. Do not mimic the sample preview's fictional brand; do not introduce generic AI gradient/card patterns. Explain design choices in 5 concise sentences after implementation.
```

## 12. Visual reference

![illuminated-manuscript original design preview](./preview.png)

`demo.html` is the local, self-contained composition used to generate this preview. It illustrates a style direction, not a production-ready application.
