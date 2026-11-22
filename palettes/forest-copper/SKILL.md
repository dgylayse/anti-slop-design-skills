---
name: forest-copper
description: Use this color palette for interfaces requiring leafy greens with oxidized
  copper for physical-product storytelling. Provides normalized semantic colors and
  contrast guidance.
license: MIT
metadata:
  category: palettes
  preview: preview.png
  era: palette
  version: 2.0.0
---

# Palette: Forest & Copper

Leafy greens with oxidized copper for physical-product storytelling.

## Canonical palette contract (authoritative)

Apply this **after** a style's core tokens. The style owns its grid and typography. This palette only overrides semantic colors:

```css
:root {
  --color-bg: #E6E9DD;
  --color-surface: #F7F4E8;
  --color-ink: #213930;
  --color-muted: #53685C;
  --color-accent: #965A3E;
  --color-border: #B9C4B7;
}
```

**Contrast and application:** use `--color-ink` for body copy and `--color-muted` for secondary labels on the canvas. Do not assume `--color-accent` can be used as small text: run a contrast check and use it for larger labels, thick rules or backgrounds as needed. For buttons, verify contrast in both default and hover states. Error and success require distinct icons/text, not color alone.

## Composition rule

1. Style tokens first, then this palette. Use its accent sparingly on selected controls, key numbers, or strong editorial rules; do not turn each container into a colored block.
2. No gradient is introduced by choosing this palette. Solid surfaces and contrast do the work.
3. Ensure accessible dark/light differentiation and preserve focus outlines.

![Forest & Copper palette preview](./preview.png)
