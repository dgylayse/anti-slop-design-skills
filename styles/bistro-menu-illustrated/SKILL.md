---
name: bistro-menu-illustrated
description: Use this 1950s hand-illustrated bistro menus visual system for restaurant
  websites. Distinct menu composition with original bistro motif; accessible responsive
  implementation.
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: 1950s hand-illustrated bistro menus
  version: 3.0.0
---

# Bistro Menu Illustrated — Art Direction Skill

## Creative rationale

- **Historical / editorial DNA:** 1950s hand-illustrated bistro menus. This is a contemporary interpretation, not a reproduction of an identifiable historical work.
- **Ideal audience:** Restaurant and adjacent use cases requiring this visual character.
- **Signature composition:** menu — Printed menu hierarchy, sketchbook illustration and visible opening/booking details.
- **Illustration device:** bistro; create it with original CSS/SVG or licensed, project-specific visual material.
- **Typography:** Georgia, Times New Roman, serif. Use this to distinguish headings from reading copy, never as an excuse to shrink normal text.

## Semantic CSS foundations

```css
:root {
  --color-bg: #F6ECD8;
  --color-surface: #FFF8EB;
  --color-ink: #332F27;
  --color-muted: #675847;
  --color-accent: #B54E36;
  --color-border: #B7A38A;
  --font-display: Georgia, Times New Roman, serif;
  --font-body: Arial, Helvetica, sans-serif;
  --radius-control: 0px;
  --focus-ring: 3px solid var(--color-accent);
}
```

## Specific page blueprint

1. Navigation carries 4–6 useful destinations and a clear current-page state; styling echoes the print/period source but remains usable.
2. Hero uses a purposeful statement and a **menu** composition; its art element reinforces the message, not merely decorates.
3. First content section proves the premise with genuine photos, descriptions, inventory or process, depending on product.
4. Primary CTA reflects a real task for restaurant; secondary CTA should be a helpful alternative rather than a redundant button.
5. Supporting content adopts the historical graphic vocabulary without repeating the same composition on every page.

## Specific anti-patterns

- No photos of fake dishes presented as real.
- No purple-blue generative gradients, repeated floating feature cards, generic sparkle symbols or indistinguishable pill-button hero.
- Avoid using historical ornament as a substitute for accessible information or functional UI.

## Implementation contract

- Use the six shared color tokens (`--color-bg`, `--color-surface`, `--color-ink`, `--color-muted`, `--color-accent`, `--color-border`) so palettes can override color **only**; preserve the style’s independent typographic and spatial identity.
- Provide clear semantic `header`, `nav`, `main`, and `footer` landmarks. Use native links and buttons; no decorative-only CTAs.
- Under 768px, recast the information hierarchy into a single intentional reading path; do not simply shrink the desktop canvas. At 768–1199px use a measured two-column adaptation and at larger sizes use the complete art-directed composition.
- Use visible focus styles (`:focus-visible` with `--focus-ring`), proper text alternatives, logical tab order and touch targets around 44px. Honor `prefers-reduced-motion`.
- Check actual text/background pairs against WCAG AA (4.5:1 for ordinary copy); an accent that is decorative may not be suitable for text.
- Create genuine hover, focus, selected, disabled, loading, error, empty and success states when applicable. Make success/errors perceivable without color alone.
- Do not invent statistics, testimonials, inventory, services, safety information, legal outcomes or product capabilities. Placeholder brand names in previews are fictional demonstrations, not ready-made content.
- Do not copy SITE123 customer templates, third-party logos, photographs or artwork. All examples here use original abstract HTML/SVG illustration.

## QA before delivery

1. Does the structure look different when viewed in grayscale, rather than just swapping colors? 2. Is the user’s primary task obvious? 3. Do keyboard, mobile and error states work? 4. Does the content sound like the real brand and avoid made-up proof? 5. Does the output remain coherent across a second screen?

## Demo composition

![Original art-direction study](./preview.png)

Open [the self-contained source HTML](./demo.html). Its sample words and imagery are fictional and illustrative.
