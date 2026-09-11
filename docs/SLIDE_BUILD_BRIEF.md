# AGOS — Slide Build Brief

Everything needed to build the AGOS storyboard as a slide deck, assuming no other context.
Hand this to a fresh session and it should be able to work without reading the rest of the
repository.

**What this is not:** the National Finals presentation. That is a separate, later deliverable
with its own rules, and its material is parked in `docs/FINALS_DECK_BACKLOG.md`. Do not mix
them.

---

## 1. The deliverable in one paragraph

A **17-slide landscape deck** for the ASEAN Data Science Explorers 2026 competition: 15
content slides plus 2 reference slides. It is read, not presented — a judge opens the PDF
and reads it alone, so every slide must stand up without a speaker. Team **Naive Bais**,
FEU – Institute of Technology, Philippines.

A working reference implementation already exists at `deck/index.html` (HTML, prints to PDF
via `scripts/build_deck_pdf.py`). **Read it before building anything.** This brief exists so
the same deck can be rebuilt in a slide tool — PowerPoint, Google Slides, Canva — not to
replace it.

---

## 2. Hard rules. Each is pass/fail, and a miss scores zero.

| Rule | Value |
|---|---|
| Content slides | **≤ 15**, including the cover |
| Reference slides | **Not counted** against that cap. Currently 2, at slides 16–17. |
| Orientation | **Landscape** |
| Page size | **297 × 210 mm** (A4 landscape). In Canva: Custom size, 297 × 210 mm. |
| Format | PDF |
| Document size | **≤ 20 MB** |
| Each embedded image | **≤ 2 MB** — a separate cap, easy to miss |
| Filename | **`PHILIPPINES_NAIVE BAIS.pdf`** — exact, including the space |
| Language | English throughout |
| Charts | Must be **generated in SAP Analytics Cloud**. They are, and they are exported to `deck/charts/`. Do not redraw them in the slide tool — that breaks the requirement. |

**The cover must carry all six:** storyboard title · team name · institution · country ·
SDG(s) · a one-sentence description naming the solution.

---

## 3. Where every piece of content comes from

Do not write new copy. It is finished and fact-checked.

| Need | File |
|---|---|
| **All slide text** — headline, standfirst, bullets, callouts, source line, per slide | **`docs/PAGE_COPY.md`** |
| Chart images ×11, architecture diagram, alert screens | `deck/charts/` |
| Reference slide content | `docs/REFERENCES.md`, regenerate with `python scripts/build_references.py` |
| Cover and pivot photographs | `deck/photos/` — **not sourced yet, see §7** |
| Working layout to copy from | `deck/index.html` |

---

## 4. Slide inventory

| # | Slide | Scope tag | Figure |
|---|---|---|---|
| 1 | Cover — AGOS | — | full-bleed photo *(missing)* |
| 2 | Six of ten ASEAN states face severe river flood hazard | ASEAN | `P2_asean_flood.png` |
| 3 | Hazard and capacity are independent | ASEAN | `P3_quadrant.png` |
| 4 | 8th for river floods, 1st for hazard exposure | PHILIPPINES | `P4_ph_vs_median.png` |
| 5 | The Pivot — no chart, deliberately | ZAMBALES | full-bleed photo *(missing)* |
| 6 | August was already Olongapo's wettest month | OLONGAPO | `P6_rainfall_month.png` |
| 7 | Where SAP sits in the system | System | `P7_architecture.png` |
| 8 | From rainfall to river level | OLONGAPO | `P8_timeseries.png` |
| 9 | A warning that arrives on the channel people have | OLONGAPO | `P9_alerts.png` |
| 10 | What one hour of warning is worth | ZAMBALES | `P10_leadtime.png` |
| 11 | Nine of eleven could only be reached by helicopter | ZAMBALES | `P11_aeta_access.png` |
| 12 | What breaks, and what we do about it | System | `P12_risk_matrix.png` |
| 13 | Funded by the sand the floods leave behind | Business model | `P13_lahar.png` |
| 14 | Twenty-four months, four phases | Roadmap | `P14_roadmap.png` |
| 15 | The countries that need this most | ASEAN | `P15_scaling.png` |
| 16–17 | References | References | — |

**Slide 5 has no chart on purpose.** It is the one slide permitted to hold no data; the
restraint is the rhetorical move. Do not "fix" it by adding a graphic.

---

## 5. The layout

One template, used on all 13 chart slides. Consistency is the point — a judge should stop
noticing the layout by slide 4.

```
┌─────────────────────────────────────────────────────────┐
│ SCOPE TAG                                               │ ← 7.5pt, caps, letterspaced, muted
│                                                         │
│ Headline, up to two lines                               │ ← 26pt bold navy, max 24ch
│ Standfirst, one sentence                                │ ← 12pt, muted
│                                                         │
│  ┌──────────────────┐   • body bullet                   │
│  │                  │   • body bullet                   │
│  │   SAC chart      │   • body bullet                   │
│  │                  │                                   │
│  └──────────────────┘   ┌───────────────────────────┐   │
│                         │ callout — the argument    │   │
│                         └───────────────────────────┘   │
│                                                         │
│ ──────────────────────────────────────────────────────  │
│ Source line                                          15 │ ← 7.5pt muted, rule above
└─────────────────────────────────────────────────────────┘
```

- Margins **14mm top, 16mm sides, 12mm bottom**. Source line pinned to the bottom.
- Text column **88mm**; the figure takes the rest. **Alternate which side the chart sits on**
  between consecutive slides so the deck has rhythm — `deck/index.html` uses a `flip` class.
- Bullets: 10.5pt, one small teal dot, no nesting, never more than four.
- Callout: light tint, **1px full border, no thick side tab** — see §6.

### The scope tag is not decoration

Every slide names its geography: `ASEAN` / `PHILIPPINES` / `ZAMBALES` / `OLONGAPO`.

Several August 2026 figures in this deck are **national totals that read like local ones**.
Slide 4's stat band — 8.1 M people, PHP 3.4 B, PHP 689 M, 437 roads — is national, and its
source line says so explicitly. Presenting one of those as Olongapo's flood damage is the
exact error that was cut from the first draft. The tag is what stops a judge mis-reading it.

---

## 6. Design tokens

Slide chrome only. **The charts carry their own colours** — never restyle a chart to match
the deck.

```
navy    #10344C   headlines, emphasis, bold text
teal    #1C7293   bullet dots, rules, the single accent
ink     #1b2129   body text
muted   #646e7b   scope tag, source line, standfirst, slide number
hairline#dfe4ea   rules and callout borders
surface #ffffff   slide background
tint    #f7f8fa   callout background
```

Two callout variants, used sparingly:
- **Caution** — background `#fdf5e2`, border `#e8d49a`. Used on slide 8 for the
  "these are normals, not one season" warning.
- **Blocked** — background `#fbeae9`, border `#e9b9b5`. Used on 11 and 13 where a figure is
  deliberately absent.

**Type:** one family. Segoe UI, or system sans. Weights 400 and 700 only.
Sizes: 26pt headline · 12pt standfirst · 10.5pt body · 9pt table · 7.5pt scope and source.

**Alert colours** — `#F2C14E` watch, `#C74A1A` warning, `#9E1F17` evacuate — appear **only**
inside the slide 9 alert graphic. They are reserved for severity and must never be used as
a slide accent, a chart series, or decoration.

### Two things not to do, both learned here

- **No thick coloured border on one side of a callout.** A 3px left tab was tried and removed:
  it is the most recognisable tell of a generated layout, and this project had already
  rejected the same pattern once in its app mockups.
- **Slide numbers must be readable.** They were set in `#c3ccd6` at 1.6:1 and were effectively
  invisible. Muted `#646e7b` at 5.17:1 is the floor. A reader told to turn to slide 12 needs
  to find slide 12.

---

## 7. What is missing, and what to do about it

**Two photographs are not sourced.** In the reference build they render as labelled dashed
boxes naming the exact file each wants — a deliberate choice, so a placeholder can never be
mistaken for a finished slide.

| Slide | File | Needs |
|---|---|---|
| 1 | `deck/photos/cover.jpg` | Olongapo or Zambales flooding, full bleed, under 2 MB |
| 5 | `deck/photos/pivot.jpg` | river aerial, sits behind text at low opacity, under 2 MB |

Pick one sourcing route and stay in it — official agency imagery (check reuse terms),
licensed stock, or the team's own photographs — and **credit it on the slide**.

Cover treatment: photo full-bleed, a navy veil over it at ~0.94 alpha on the text side
falling to ~0.55 on the far side, white text. The veil is what makes the text legible over
an unknown photo; do not drop it.

**Chart resolution.** The exports in `deck/charts/` are roughly 370px — about 190 DPI at
slide size. Acceptable, not crisp. Better versions come from SAC: open the story, click a
chart, **⋯ → Full Screen**, screenshot, Esc. Overwrite the file, keep the name.

---

## 8. Numbers are not editable copy

Every figure on every slide traces to a row in `docs/SOURCES.md`, which records its source,
date and **geographic scope**.

- **Do not round, re-phrase, or "tidy" a number.** 865.97 mm is not 866 mm on slide 6.
- **Do not fill a blank.** Slides 13 and 14 show em dashes where lahar-sand pricing, sensor
  costs and KPI targets would go. Those are unsourced, and the slides say so on their face.
  An invented figure is the failure this project has already corrected once.
- If a figure changes, update `SOURCES.md`, re-run `python scripts/build_references.py`, and
  rebuild the reference slides. They are generated, so they cannot drift out of step.

---

## 9. Acceptance checklist

- [ ] **15 content slides**, references extra
- [ ] Landscape, 297 × 210 mm, PDF
- [ ] **≤ 20 MB** total, every image **≤ 2 MB**
- [ ] Filename `PHILIPPINES_NAIVE BAIS.pdf`
- [ ] Cover carries all six required elements
- [ ] Scope tag on every content slide
- [ ] Every chart is the SAC export, not redrawn
- [ ] Every chart legible at 100% **and** printed
- [ ] Reference slides present, and **no citation clipped off the edge** — count them
- [ ] Slide numbers legible
- [ ] No thick side-tab callouts; no alert colours outside slide 9
- [ ] Every number matches `SOURCES.md`; blanks left blank
- [ ] Read end to end, aloud, once

The clipped-citation check is on the list because it happened: at one reference page in two
columns, **10 of 26 citations flowed past the page edge and were silently dropped**. The page
looked complete. Count what renders, do not trust that it fits.
