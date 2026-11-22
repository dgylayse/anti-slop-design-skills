---
name: oxblood-parchment
description: Use this color palette for interfaces requiring bookbinder reds and parchment
  for literary or heritage brands. Provides normalized semantic colors and contrast
  guidance.
license: MIT
metadata:
  category: palettes
  preview: preview.png
  era: palette
  version: 2.0.0
---

# Palette: Oxblood Parchment

Bookbinder reds and parchment for literary or heritage brands.

## Canonical palette contract (authoritative)

Apply this **after** a style's core tokens. The style owns its grid and typography. This palette only overrides semantic colors:

```css
:root {
  --color-bg: #F4E8D6;
  --color-surface: #FFF8EB;
  --color-ink: #33272A;
  --color-muted: #6C585A;
  --color-accent: #7D2639;
  --color-border: #C8ADA5;
}
```

**Contrast and application:** use `--color-ink` for body copy and `--color-muted` for secondary labels on the canvas. Do not assume `--color-accent` can be used as small text: run a contrast check and use it for larger labels, thick rules or backgrounds as needed. For buttons, verify contrast in both default and hover states. Error and success require distinct icons/text, not color alone.

## Composition rule

1. Style tokens first, then this palette. Use its accent sparingly on selected controls, key numbers, or strong editorial rules; do not turn each container into a colored block.
2. No gradient is introduced by choosing this palette. Solid surfaces and contrast do the work.
3. Ensure accessible dark/light differentiation and preserve focus outlines.

![Oxblood Parchment palette preview](./preview.png)
