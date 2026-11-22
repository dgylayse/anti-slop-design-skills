---
name: thermal-receipt
description: "Use for cafés, food ordering, checkout and order-tracking flows in a thermal-receipt direction: a living receipt printer that prints each line as items are added (and void lines when removed), a paid stamp, a tear-off, and honest step-by-step pickup status, all in one monospace face on counter-grey and paper-white."
license: MIT
metadata:
  category: styles
  preview: preview.png
  era: "1990s point-of-sale receipts"
  version: 4.0.0
  tier: living
---

# Thermal Receipt — Living Style

> **Living style.** The receipt is not a picture of a receipt. It is the order itself, printed line by line as the visitor acts, with the same rules a real till follows.

## 1. Design philosophy
A receipt is the most honest document in commerce: every item, every modifier, every correction, the time, the total. A till never erases; it prints a **void** line. The interface adopts that honesty. The slip is an **append-only log** of what happened, and the page around it stays plain and functional, like a counter.

Test: *would this line, this state or this motion exist on a real till?*

## 2. Colour tokens
```css
:root {
  --color-bg: #E2DFD8;       /* the counter */
  --color-surface: #FBFAF6;  /* thermal paper */
  --color-ink: #1B1B1B;
  --color-muted: #4F4D49;
  --color-accent: #B5172B;   /* second print colour: current step, PAID stamp, pay button */
  --color-border: #1B1B1B;
  --slot: #2A2A28;           /* printer body */
}
```
One extra signal colour is allowed for state: open/ready green (#2E7D4F) as text only.

## 3. Typography
- **One monospace family** for everything (`Consolas, 'Lucida Console', 'Courier New', monospace`), weights 400 and 700.
- Headline 40–58px bold, negative tracking; the status word in red.
- Receipt lines 15px; modifiers lowercase, indented, muted; totals 22px bold; the order number 76px+.
- Labels 11–13px uppercase with 0.1–0.2em tracking.

## 4. Layout
- **Desktop:** three columns — menu · printer (≈440px, sticky) · total, pickup steps, shelf.
- **Tablet:** menu + printer; the right column moves below as two panels.
- **Phone:** menu → printer → status. The receipt is never hidden behind a drawer.
- The printer is a dark head with an LED and a slot; paper feeds from the slot with a zigzag tear edge at the bottom.
- No rounded cards, no shadows except the paper's 1px edge.

## 5. Signature interaction — the printer
| Visitor action | Printed on the slip |
|---|---|
| Page opens | header: shop, address, date/time, order number (printed instantly so first paint is complete) |
| Add an item (with chosen modifiers) | `1 × ITEM    3.40` and indented `+ oat milk    0.40` |
| Remove an item | `VOID ITEM    −3.80`, struck through, muted. **Never delete printed lines.** |
| Pay & print | dashed rule, TOTAL, VAT line, `CARD ···· APPROVED`, big order number, barcode, thank-you line; then the red **PAID** stamp lands |
| Tear off | the slip tears and drops away; the number joins "torn-off slips"; the printer starts a fresh order |

Status steps (Ordering → Paid → Brewing → Ready on shelf) advance with real events and timestamps; "Ready" reveals the shelf letter. The LED lights while the head is printing.

## 6. Motion language
| Moment | Motion | Timing |
|---|---|---|
| Each printed line | feeds out of the slot (clip from the top, height grows) | 0.32s, 95ms between lines, `cubic-bezier(.4,0,.2,1)` |
| PAID | stamp drops from 1.8× scale and settles at −14° | 0.35s overshoot |
| Tear off | small jerk, then the slip falls and rotates away | 0.8s ease-in |
| Everything else | none | — |

`prefers-reduced-motion`: lines appear instantly, no stamp bounce, the slip vanishes without falling.

## 7. Section library
1. **Order hero** — kicker, headline with red status word, honest lede, menu rows (name, description, price, + / − buttons, modifier toggles), printer with Pay and Tear buttons, running total, pickup steps, shelf card, live status line.
2. **How pickup works** — three receipt stubs (zigzag bottom edges) with big numerals.
3. **Hours + stamp card** — a ruled hours table with today highlighted; a punch card with punched holes and a red FREE hole.
4. **Footer** — address and payment notes in one line.

## 8. Code recipes
```js
// append-only print queue; instant while building the header so screenshots are complete
function print(cls, left = '', right = '') { /* push {cls,left,right}; feed() unless instant */ }
function feed() { /* take one job, append .ln.new, light the LED, setTimeout(feed, 95) */ }
// adding prints item + modifiers; removing prints a VOID line with a negative amount
print('', '1 × FLAT WHITE', '3.40'); print('sub', '+ oat milk', '0.40');
print('void', 'VOID FLAT WHITE', '−3.80');
// CSS
.ln.new { animation: feed .32s cubic-bezier(.4,0,.2,1) both }
@keyframes feed { from { clip-path: inset(0 0 100% 0); max-height: 0 } to { clip-path: inset(0); max-height: 120px } }
.paper:after { /* zigzag tear: two 45° linear-gradients, 14px × 10px */ }
.ln.bar { background: repeating-linear-gradient(90deg, ink 0 2px, transparent 2px 4px, ...) } /* decorative barcode */
```
Keep the receipt scrolled to the newest line (`wrap.scrollTop = wrap.scrollHeight`) and switch the wrapper to scrollable only when the slip is taller than the viewport.

## 9. Content rules
- Real prices, VAT line, payment method masked to `····`. Never print full card numbers, names or emails on the slip.
- The order number is the only identifier shown at pickup.
- A barcode or QR that is not scannable must be `aria-hidden` and described as decorative.

## 10. Forbidden patterns (anti-slop)
- NEVER delete or edit printed lines; corrections are void lines.
- NEVER rely on the red stamp alone to signal payment; the status text says it too.
- NEVER add rounded cards, gradients, glassmorphism or floating shadows around the receipt.
- NEVER animate anything idle (no blinking cursor, no pulsing buttons).
- NEVER use a second font family.

## 11. Accessibility
- The receipt is an `article` with `aria-live="polite"` for additions; a separate `role=status` line summarises each event in a sentence.
- Steps use `aria-current="step"`; buttons have explicit labels ("Remove one chai"); focus returns to the related control after each action.
- Contrast: ink and muted pass AA on paper and on the counter grey.
- Touch targets 44px for + / −, 34px for modifier toggles.

## 12. Quality gate
(1) Does every add, remove and pay produce the correct printed lines? (2) Is anything ever erased from the slip? (3) Does the page work with motion reduced? (4) On a phone, is the receipt directly after the menu? (5) Is any personal data printed?

## Required semantic-token interface
```css
:root {
  --color-bg: #E2DFD8;
  --color-surface: #FBFAF6;
  --color-ink: #1B1B1B;
  --color-muted: #4F4D49;
  --color-accent: #B5172B;
  --color-border: #1B1B1B;
  --font-display: Consolas, 'Lucida Console', 'Courier New', monospace;
  --font-body: Consolas, 'Lucida Console', 'Courier New', monospace;
  --radius-control: 0px;
  --focus-ring: 3px solid var(--color-accent);
}
```

## Invocation example
```text
Use the thermal-receipt living style for this ordering flow. Build a printer whose
slip is an append-only log: items and modifiers print as they are added, removals
print VOID lines, paying prints the totals and a PAID stamp, tearing off starts a
new order and advances honest pickup steps. One monospace font, motion only from
printing, reduced-motion safe, no personal data on the slip.
```

![thermal-receipt living preview](./preview.png)

`demo.html` is a complete, interactive single-file page; the preview shows its first screen.
