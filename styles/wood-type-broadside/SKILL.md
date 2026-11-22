---
name: wood-type-broadside
description: "Use for markets, fairs, breweries, community events and local shops in an 1870s wood-type broadside direction: a living print shop where visitors set their own poster lines (each auto-sized to fill the measure), ink the forme with a roller and pull unique prints with real ink texture, framed by handbill columns, slab labels and a two-colour discipline."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "1870s wood type broadsides"
  version: 4.0.0
  tier: living
---

# Wood Type Broadside — Living Style

> **Living style.** The poster is set, inked and printed in the browser. Every behaviour comes from the job printer's workflow: set · ink · pull.

## 1. Design philosophy
A broadside was set line by line from whatever wood type the shop had: a huge condensed word, a spaced slab line, an italic connective, a second colour for the key word. Each line is sized to **fill the measure**. Ink is never perfect; every pull differs slightly.

The page lets visitors do exactly that with their own words, and keeps practical information (schedule, booking) in plain handbill columns beside the poster.

Test: *could a jobbing printer with one case of wood type and two inks have made this?*

## 2. Colour tokens
```css
:root {
  --color-bg: #EDE0C4;       /* shop paper */
  --color-surface: #F6EDD6;
  --color-ink: #221A14;      /* black ink */
  --color-muted: #5A4838;
  --color-accent: #A82820;   /* the second ink: red */
  --color-border: #221A14;
  --metal: #7A746B;          /* un-inked type in the forme */
  --paper: #F4EAD2;          /* the printing sheet */
}
```
Two inks plus paper. Never a third ink.

## 3. Typography
| Face | Stack | Use |
|---|---|---|
| Gothic (condensed) | `Impact, Haettenschweiler, 'Arial Narrow Bold'` | the big word |
| Wide | same, `letter-spacing: .16em` | secondary big word |
| Slab | `Rockwell, 'Rockwell Extra Bold', 'Courier New'`, uppercase, `.42em` tracking | small spaced lines, labels, buttons |
| Italic | `Georgia` italic | connectives (&, at, and) |
| Band | slab on a solid ink band, reversed | the date / call to action line |
| Reading | `Georgia` 15–16px | handbills, forms |

Letter-spaced faces get matching `padding-left` so the trailing spacing does not push the line off centre.

## 4. Layout
- **Desktop:** handbill column (≈260px) · poster · composing stick (≈360px), divided by 3px ink rules.
- **Tablet:** the handbill becomes a three-column strip above; poster and stick side by side.
- **Phone:** handbill → poster (≥72vh) → stick.
- Printer's ornament rule (line · dot · diamond · dot · line) after the fourth line.
- Paper grain overlay (`feTurbulence`, multiply, ~45%) is fixed and `pointer-events:none`.

## 5. Signature interaction — set · ink · pull
| Step | Visitor does | What happens |
|---|---|---|
| Set | edits five lines; picks Gothic / Wide / Slab / Italic / Band and black or red per line | each line re-fits to the measure; the forme shows **bare grey metal** |
| Ink | presses "Ink the forme" | a roller passes top to bottom; each line darkens as the roller reaches it |
| Pull | presses "Pull a print" | the platen comes down and lifts; the sheet shows a print with ink speckle, a slight wobble, and red slightly out of register; the print number joins "Pulled prints" |
| Order | "Order 10" | the current text is ordered for collection |

**Fit algorithm:** set each line to 100px, measure its width, scale to `min(maxFor(face), 100 × measure / width)`; if the stack is taller than the sheet, scale all lines down by the same factor. Lines use `display: table` so they shrink-wrap and centre.

## 6. Motion language
| Moment | Motion | Timing |
|---|---|---|
| Ink | roller (dark cylinder) travels down the sheet; lines turn from metal to ink as it passes | 0.9s, delay per line by its vertical position |
| Pull | platen down, hold, up | 1.0s total, print swaps at the midpoint |
| Button press | the red button's hard 4px shadow collapses (it is "pressed") | 0.08s |
| Everything else | none | — |

`prefers-reduced-motion`: no roller or platen; states switch instantly.

## 7. Section library
1. **Print shop hero** — handbill (mark, nav, "This Saturday" schedule, access note) · poster sheet with status line · composing stick (five lines, face chips, ink toggle, Ink / Pull, pulled-print pile, order box).
2. **Set · Ink · Pull** — three woodcut-style SVG illustrations between heavy rules.
3. **Book a stall** — pitch choice as large radio cards with prices, date select, produce, name, email; inline validation; confirmation in a dashed box.
4. **Footer** — double rule and a colophon.

## 8. Code recipes
```html
<filter id="ink">
  <feTurbulence id="speck" type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3" result="n"/>
  <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -6 4.15" result="m"/>
  <feComposite in="SourceGraphic" in2="m" operator="in" result="s"/>
  <feTurbulence id="wobble" type="fractalNoise" baseFrequency=".05" seed="9" result="w"/>
  <feDisplacementMap in="s" in2="w" scale="2.4"/>
</filter>
```
- The alpha matrix (`−6·A + 4.15`) keeps most of the ink and removes small specks where the noise is high — a worn wood-type look rather than a dirty overlay.
- New seed per pull (`speck.setAttribute('seed', …)`) makes every print unique; red lines get a random 0–1.5px offset (`--mx`, `--my`) for misregistration.
- States are classes on the sheet: `.forme` (metal grey) → `.inked` → `.printed` (filter on). Editing any line returns to `.forme`.

## 9. Content rules
- Real schedule times, prices and dates; the printed bill shows only what the visitor typed.
- Always offer large-print / plain-text versions of event information; the poster is an image for assistive tech (`role="img"` with a label).

## 10. Forbidden patterns (anti-slop)
- NEVER more than two inks; NEVER gradients on type.
- NEVER use distressed "western" novelty fonts for reading text.
- NEVER centre the handbill columns; only the poster is centred.
- NEVER add idle animation, hover zooms or glow; the press moves only when used.
- NEVER let grain or texture reduce form or body-text contrast below AA.

## 11. Accessibility
- Composing controls: labelled inputs, face chips as a `radiogroup`, ink toggle with `aria-pressed`; focus stays on the control after re-render.
- Ink/Pull buttons are disabled when not applicable; a `role=status` line explains the next step after every action.
- Stall form: real radio inputs inside large labels (`:has(:focus-visible)` shows focus), `aria-invalid`, one combined `role=alert` message.

## 12. Quality gate
(1) Does every line still fill the measure after any edit and at every viewport? (2) Do Ink and Pull follow the workflow (no pulling un-inked type)? (3) Are two consecutive prints visibly different? (4) Reduced motion and keyboard pass? (5) Only two inks?

## Required semantic-token interface
```css
:root {
  --color-bg: #EDE0C4;
  --color-surface: #F6EDD6;
  --color-ink: #221A14;
  --color-muted: #5A4838;
  --color-accent: #A82820;
  --color-border: #221A14;
  --font-display: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  --font-body: Georgia, 'Times New Roman', serif;
  --radius-control: 0px;
  --focus-ring: 3px solid var(--color-accent);
}
```

## Invocation example
```text
Use the wood-type-broadside living style. Build a print-shop hero: five editable
poster lines, each auto-fitted to the measure in a chosen wood-type face and one of
two inks; "Ink the forme" runs a roller that darkens lines as it passes; "Pull a
print" lowers the platen and shows a unique print (new turbulence seed, slight red
misregistration). Keep schedule and booking in plain handbill columns.
```

![wood-type-broadside living preview](./preview.png)

`demo.html` is a complete, interactive single-file page; the preview shows its first screen.
