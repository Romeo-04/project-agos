# AGOS — Design Brief

Everything needed to build or extend the AGOS interface mockups, assuming no other context.
Hand this file to a fresh session and it should be able to work without reading the rest of
the repository.

**Deliverable:** self-contained HTML files in `mockups/`. No build step, no dependencies, no
framework. Each file opens from disk in a browser.

**Already built — read before adding anything:**

| File | Contains |
|---|---|
| `mockups/agos-screens.html` | seven app screens |
| `mockups/agos-architecture.html` | the P7 system diagram |

---

## 1. What AGOS is, in one paragraph

AGOS is a flood early-warning system for Zambales, Philippines. River sensors and satellite
radar feed a forecast; the forecast becomes an alert that reaches households through the
channel they actually have — including a solar-powered barangay siren for communities with
no phone signal. It is an entry for the ASEAN Data Science Explorers competition, so the
mockups appear inside a PDF storyboard rather than shipping as software.

**Who uses each screen matters more than how it looks.** In order of how much the design
owes them:

1. **A resident deciding whether to leave the house, possibly at night, possibly on a phone
   with one bar.** Every VOICE screen is for this person.
2. **A barangay officer** marking a road impassable while standing in the rain.
3. **An LGU engineer** watching river levels across the city.
4. **A provincial treasurer** checking whether the funding loop is working.

---

## 2. The three constraints that outrank aesthetics

### 2.1 This is a tool for people who may be evacuating

One task per screen. The primary action is the largest thing on it. Nothing decorative
competes with the thing the person came to do. If a screen has two plausible primary
actions, it is two screens.

### 2.2 Severity is never carried by colour alone

Every alert state ships with **a colour, an icon, and a text label**, all three. This is not
only an accessibility rule — colour-blind users, greyscale printing in the PDF, and a phone
screen in direct sun all break colour-only encoding.

The three states also form a **lightness ramp**, not just a hue change:

| State | Fill | Ink | Relative luminance | Contrast |
|---|---|---|---|---|
| Watch | `#F2C14E` | `#4a3708` | 0.576 | **6.80:1** |
| Warning | `#C74A1A` | `#ffffff` | 0.171 | **4.75:1** |
| Evacuate Now | `#9E1F17` | `#ffffff` | 0.083 | **7.89:1** |

Because luminance descends 0.576 → 0.171 → 0.083, the escalation survives greyscale print
and colour-blind vision. A hue-only ramp would not.

> **These exact values are load-bearing.** An earlier draft used `#D9531E` for Warning,
> which gives white text **4.03:1** — below AA, and it would have shipped failing. If you
> change any of these, recompute the contrast; do not eyeball it. The check is in §7.

All three states use **one treatment: a solid fill.** An earlier draft gave Watch a pale
background plus a thick left border, which made it read as a different component rather
than as step one of the same ladder.

### 2.3 Status colours are reserved

Amber, orange and red mean severity. They never appear as a chart series, a brand accent, a
button, or decoration. Analytical charts use a separate validated palette (§3.3), and the
two systems **never appear on the same page** — status colours live only on the alert
screens.

---

## 3. Tokens

Define these once, use nothing outside them. Both existing mockup files carry this block
verbatim; it is duplicated rather than imported so each file opens standalone from disk with
nothing missing. Keep doing that.

```css
:root {
  /* spacing — 4px base scale, no value outside it */
  --s1:4px;  --s2:8px;  --s3:12px; --s4:16px;
  --s5:24px; --s6:32px; --s7:48px; --s8:64px;

  /* radius */
  --r-ctl:8px; --r-card:14px; --r-pill:999px;

  /* type scale */
  --t-xs:11px; --t-sm:13px; --t-md:15px;
  --t-lg:19px; --t-xl:25px; --t-2xl:33px;

  /* neutral ramp — this does most of the work */
  --n0:#ffffff; --n50:#f7f8fa; --n100:#eef1f5; --n200:#dfe4ea;
  --n300:#c3ccd6; --n500:#7b8794; --n700:#48525e; --n900:#1b2129;

  /* brand — deck chrome only, never a data mark */
  --navy:#10344C; --teal:#1C7293;

  /* accent — one hue, primary action and focus ring only */
  --accent:#1C7293; --accent-press:#155b76;

  /* RESERVED status palette — severity only. See §2.2. */
  --watch:#F2C14E;    --watch-ink:#4a3708;   --watch-bg:#fdf5e2;
  --warning:#C74A1A;  --warning-ink:#ffffff; --warning-bg:#fdeee7;
  --evacuate:#9E1F17; --evacuate-ink:#ffffff;--evacuate-bg:#fbeae9;
  --ok:#2F7D4F;       --ok-bg:#eaf4ee;

  --border:1px solid var(--n200);
  --shadow-card:0 1px 2px rgba(16,52,76,.06), 0 1px 3px rgba(16,52,76,.04);
  --shadow-float:0 8px 24px rgba(16,52,76,.14);
}
```

### 3.1 Type

System stack: `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. Two weights carry
everything — 400/500 for body, 600/700 for emphasis. Body line-height ~1.5, headings ~1.2,
measure 45–75 characters.

### 3.2 Layout

- Constrain width: body text and forms ~560–720px; dashboards ~1100–1400px, centred.
- Responsive side padding so content never touches the edge:
  `padding-inline: clamp(16px, 4vw, 56px)`.
- Prefer `gap` on flex/grid over margins.
- Space *within* a component is smaller than space *between* components. Proximity
  communicates grouping better than borders do.
- Tap targets ≥ 44px on the resident-facing screens. Assume wet hands.

### 3.3 The categorical palette — analytical charts only

Fixed order, **never cycled**. Do not use these on alert screens.

| Slot | Hex | Role |
|---|---|---|
| 1 | `#2E6FA8` | primary series / Philippines |
| 2 | `#E0762F` | second series / highlight |
| 3 | `#1FA8C4` | third series |
| 4 | `#8C5BB0` | fourth series |
| 5 | `#5A9E3E` | fifth series |

The brand navy and teal **fail** as data marks — navy sits outside the lightness band and
both fall below the chroma floor, so they read as grey. They stay as deck chrome.

`#1FA8C4` carries a contrast WARN at 2.74:1. That is **not dismissable**: it obligates
visible data labels on any chart using it. The competition's readability rule demands the
same thing, so the two constraints resolve to one action.

---

## 4. The screens

`agos-screens.html` renders all seven in one scrollable page, each in a phone or desktop
frame with a caption naming its user and its job.

| # | Screen | User | The one job |
|---|---|---|---|
| 1 | **VOICE — Watch** | resident | "the river is rising, prepare" |
| 2 | **VOICE — Warning** | resident | "flooding likely within hours, be ready to leave" |
| 3 | **VOICE — Evacuate Now** | resident | "leave for the evacuation centre now" |
| 4 | **PATH — road status** | barangay officer | mark a route open / impassable, see the rest |
| 5 | **EYE — river dashboard** | LGU engineer | river levels and lahar risk across the city |
| 6 | **FUND — treasurer widget** | provincial treasurer | is the self-funding loop working |
| 7 | **Home** | resident | barangay status, and a way into the other four |

### 4.1 VOICE, screens 1–3

The same component in three states. What changes is the fill, the icon, the label and the
instruction — never the layout. A resident who has seen Watch should recognise Evacuate Now
instantly as the same thing, escalated.

Each carries, in this order: **state label · what is happening · what to do · when it was
issued · which barangay**. The "what to do" line is the largest text on the screen after the
state label.

### 4.2 PATH, screen 4

A route list with status chips, plus one map. Status is set by tap. Anything older than
**two hours** auto-downgrades to *Unconfirmed — proceed with caution*, and the UI must show
that downgrade happening rather than silently ageing — a stale green road that still reads
as safe is the failure mode this screen exists to prevent.

### 4.3 EYE, screen 5

River gauges against threshold lines, and lahar risk by barangay. This is the only screen
where a chart-like element appears; it uses the categorical palette, not status colours.

### 4.4 FUND, screen 6

Revenue against operating cost, and dredging progress.

### 4.5 Home, screen 7

Current barangay status, then links to the other four. Nothing else.

---

## 5. Data rules — the part most likely to go wrong

**Every number shown must be real and traceable to `docs/SOURCES.md`.** The figures already
used in the mockups:

- **4.7 bn m³** of Pinatubo lahar in the Zambales rivers — Bucao **3.0 bn (63.8%)**,
  Santo Tomas **1.6 bn (34.0%)**
- **1.06%** dredged in 35 years — the FUND progress bar is *deliberately* almost invisible
- **21 barangays** under threat — 6 Bucao, 15 Santo Tomas
- **866 mm** August rainfall normal

### Where a number does not exist, show that it does not exist

Two places in the current build do this, and both are correct:

- **FUND's revenue rows are em dashes.** Lahar-sand price per m³ and sensor costs have not
  been sourced. The screen says so on its face.
- **Sensors reporting shows an em dash**, not a count. The pilot is not deployed.

Inventing a plausible-looking number for a mockup of an unbuilt system is the same failure
as the misattributed figures that were cut from the first draft of this project. **Use an em
dash and a short note.** A judge who spots one invented number stops trusting all of them.

---

## 6. States — a component without them is unfinished

Never ship one of these missing:

**hover** · **:focus-visible** (always a visible ring; never `outline:none` without a
replacement) · **active/pressed** · **disabled** (reduced opacity, `cursor:not-allowed`, no
hover) · **loading** (skeleton or spinner, trigger disabled) · **empty** (a helpful message,
not a blank void) · **error** (specific, and next to its cause).

**Motion:** 120–250ms, `ease-out` on enter, animate `opacity`/`transform` only. Respect
`@media (prefers-reduced-motion: reduce)`.

**Icons:** real inline SVG at consistent size and stroke. **Never emoji** — they render
differently on every platform and cannot be recoloured.

---

## 7. How to verify, rather than judge by eye

Two checks are computable. Run them; do not reason about them.

**Contrast.** For any new colour pairing:

```python
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    c = [(v/12.92 if v <= 0.04045 else ((v+0.055)/1.055)**2.4) for v in c]
    return 0.2126*c[0] + 0.7152*c[1] + 0.0722*c[2]

def contrast(a, b):
    l1, l2 = sorted([lum(a), lum(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)
```

Body text ≥ **4.5:1**. Large text and UI borders ≥ **3:1**.

**Categorical palette.** If you change any chart hue, run the dataviz skill's validator
rather than judging colour-blind safety by eye:

```bash
node scripts/validate_palette.js "#2E6FA8,#E0762F,#1FA8C4,#8C5BB0,#5A9E3E" --mode light
```

**Layout.** Render the file and look at it. The validators check colour, not collisions,
overflow or geometry.

---

## 8. Anti-patterns — check every screen against this list

Many almost-equal spacings or greys instead of the scale · accent colour sprinkled beyond
the primary action and focus · **status colours used as a series or a decoration** · emoji as
icons · mixed icon sets or sizes · `outline:none` with no replacement · placeholder used as
the only label · everything shadowed · centre-aligned long paragraphs · full-width text with
no max-width · pure `#000` on `#fff` · low-contrast grey-on-grey · **a number on the screen
that no source supports**.

---

## 9. Acceptance checklist

- [ ] Every spacing and size value comes from the scale; every colour is a token
- [ ] One accent, used only for primary action and focus
- [ ] Text contrast passes AA — **computed, not judged**
- [ ] All three alert states: solid fill, colour **and** icon **and** text label
- [ ] Alert states form a descending lightness ramp and survive greyscale
- [ ] Status colours appear on alert screens only, never as a series or accent
- [ ] Consistent radius; hairline borders with restrained shadow
- [ ] Every interactive element has hover **and** visible focus-visible
- [ ] Empty, loading and error states exist
- [ ] Real inline SVG icons, consistent size and stroke
- [ ] Tap targets ≥ 44px on resident-facing screens
- [ ] Motion ≤ 250ms and respects reduced-motion
- [ ] **Every number traces to `docs/SOURCES.md`; anything unsourced is an em dash**
- [ ] File opens standalone from disk with no missing asset
- [ ] Rendered and looked at, not just written

---

## 10. Exporting for the storyboard

Screenshot individual screens at 2× for print clarity. Each image must stay under **2 MB** —
a hard competition cap, separate from the 20 MB document cap.

**Rendered PNGs are never committed.** Only the HTML source is. See `deck/README.md` for
where exported images go and how the pages are assembled.
