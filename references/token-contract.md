# Shared Design Token Contract

All new implementations use the following canonical CSS variables:

```css
:root {
  --color-bg: #f5f3ee;          /* canvas */
  --color-surface: #fff;        /* raised/contrast region */
  --color-ink: #171717;         /* readable body and headings */
  --color-muted: #525252;       /* labels, tested for contrast */
  --color-accent: #b4342a;      /* selected action/mark */
  --color-border: #c9c2b7;      /* separators */
  --font-display: Georgia, serif;
  --font-body: Arial, sans-serif;
  --radius-control: 0px;
  --focus-ring: 3px solid var(--color-accent);
}}
```

**Layer order:** `style → palette → layout-specific structure → component states`. In CSS, import the palette after the style; if the selectors differ in specificity, ensure equal specificity or use a single deliberate variable override root. Preserve readable contrast and font hierarchy even after combining layers. Style-specific legacy variables in inherited specs are historical notes; canonical `--color-*` variables are implementation truth.

**Usage:** background `var(--color-bg)`; text `var(--color-ink)`; muted `var(--color-muted)`; separators `var(--color-border)`; accent `var(--color-accent)`. Never use `--color-accent` as body text without checking contrast. A palette must not smuggle in gradients, typefaces, shadows or layout changes.
