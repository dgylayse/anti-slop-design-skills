---
name: plum-marigold
description: Use this color palette for interfaces requiring expressive purple-plum
  without the generic neon gradient look. Provides normalized semantic colors and
  contrast guidance.
license: MIT
metadata:
  category: palettes
  preview: preview.png
  era: palette
  version: 2.0.0
---

# Palette: Plum & Marigold

Expressive purple-plum without the generic neon gradient look.

## Canonical palette contract (authoritative)

Apply this **after** a style's core tokens. The style owns its grid and typography. This palette only overrides semantic colors:

```css
:root {
  --color-bg: #F4EDEB;
  --color-surface: #FFF9F2;
  --color-ink: #392A42;
  --color-muted: #65566B;
  --color-accent: #963F77;
  --color-border: #D0BDCF;
}
```

**Contrast and application:** use `--color-ink` for body copy and `--color-muted` for secondary labels on the canvas. Do not assume `--color-accent` can be used as small text: run a contrast check and use it for larger labels, thick rules or backgrounds as needed. For buttons, verify contrast in both default and hover states. Error and success require distinct icons/text, not color alone.

## Composition rule

1. Style tokens first, then this palette. Use its accent sparingly on selected controls, key numbers, or strong editorial rules; do not turn each container into a colored block.
2. No gradient is introduced by choosing this palette. Solid surfaces and contrast do the work.
3. Ensure accessible dark/light differentiation and preserve focus outlines.

![Plum & Marigold palette preview](./preview.png)
