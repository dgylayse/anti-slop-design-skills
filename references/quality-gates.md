# Art Direction Quality Gates

## Craft
- A distinct visual motif and **distinct composition**; merely changing palette on identical SaaS cards does not count.
- Information order matches the product's real use; no fabricated testimonials or fake financial/security metrics.
- Crop, text scale, spacing and density are intentional across mobile/tablet/desktop.
- Avoid generic AI tropes: giant center hero, random neon gradients, purple/cyan/blue radiance, floating pill tags, cards-inside-cards, sparkles everywhere, unusable low-contrast glass.

## Accessibility and functionality
- Normal text >= 4.5:1 contrast; large text >= 3:1; non-text UI component boundaries >= 3:1 where applicable; verify against actual backdrop.
- Keyboard reachable, focus visible, semantic headings/landmarks, form labels, errors explained in text, not color only.
- Functional success, loading, empty, selected, disabled and error states; no icon-only ambiguous action without a label.
- Touch targets approximately 44×44px; reduced-motion preferences respected; meaningful navigation, no overlapping sticky bars.

## Provenance and delivery
- Images local or appropriately licensed and credited where needed. Original CSS and vector illustrations preferred for ornamental studies.
- Do not ship the catalog demo's fictional names, dates or metrics as user facts.
- Review design at 390×844, 768×1024 and 1440×900. Avoid overflow and truncated menus.
- `preview.png` is a **representative, illustrative screenshot** made from `demo.html`, not a promise that pasting a prompt yields pixel-perfect output.
