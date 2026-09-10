# deck/ — assembly workspace

Where the storyboard gets turned into the submitted PDF. **Nothing image-shaped in here is
committed** — `deck/charts/`, `deck/photos/` and `deck/*.pdf` are gitignored, because they
are screenshots of the SAC story and the project rule is that screenshots stay out of the
repository. This README and the source documents are the tracked part.

```
deck/
  README.md      ← tracked
  index.html     ← tracked — the 15 pages, all copy already in place
  charts/        ← gitignored — chart exports from SAC
  photos/        ← gitignored — cover, pivot and alert imagery
  PHILIPPINES_NAIVE BAIS.pdf   ← gitignored — the submission
```

## Building the PDF

```bash
python scripts/build_deck_pdf.py
```

Drives headless Chromium over `deck/index.html` and writes
`deck/PHILIPPINES_NAIVE BAIS.pdf`, then checks the three pass/fail rules — page
count, document size, and per-image size — and exits non-zero if any fails. It also
lists any referenced asset that is missing, so a placeholder box never reaches the
submission unnoticed.

The 15 pages are already written and laid out. Four assets are still placeholders,
each drawn as a labelled dashed box naming the exact file it wants:

| Page | File | Where it comes from |
|---|---|---|
| P1 | `deck/photos/cover.jpg` | sourced photograph |
| P5 | `deck/photos/pivot.jpg` | sourced photograph |
| P7 | `deck/charts/P7_architecture.png` | screenshot `mockups/agos-architecture.html` |
| P9 | `deck/charts/P9_alerts.png` | screenshot the VOICE states + PATH from `mockups/agos-screens.html` |

Drop each file in and re-run; nothing else needs editing.

## What you need, and where it comes from

| Input | Source |
|---|---|
| Page text — headline, body, source line, for all 15 pages | `docs/PAGE_COPY.md` |
| Chart images ×11 | export from SAC, below |
| P7 architecture diagram | `mockups/agos-architecture.html` |
| P9 alert states and route map | `mockups/agos-screens.html` |
| References page | `docs/REFERENCES.md` (regenerate with `python scripts/build_references.py`) |
| Cover / pivot / alert photography | **not sourced yet — your call, see below** |

## Exporting the charts from SAC

**Do this in your own browser, not through automation.** A chart on the canvas is only
about 370 px wide, and a capture at that size is too soft to print. Full Screen re-renders
it at roughly 1800 px, which is what you want.

Per chart:

1. Open the story, click the chart, then its **⋯ → Full Screen**
2. Screenshot the chart region *(Win+Shift+S)*
3. **Esc** to exit, next chart

Save them into `deck/charts/` using these names — the page copy refers to them in this order:

```
P2_asean_flood.png      P3_quadrant.png       P4_ph_vs_median.png
P6_rainfall_month.png   P8_timeseries.png     P10_leadtime.png
P11_aeta_access.png     P12_risk_matrix.png   P13_lahar.png
P14_roadmap.png         P15_scaling.png
```

A low-resolution preview set may already be sitting in `deck/charts/` — captured straight
off the canvas at 1×, good enough to lay pages out against, **not good enough to submit**.
Overwrite each one as you export it properly.

> **Before exporting, finish the chart styling.** Titles, the validated categorical palette,
> data labels and source notes are still on SAC defaults. `docs/HOW_TO_FINISH_THE_CHARTS.md`
> has the per-chart checklist. Exporting first and styling second means exporting twice.

## Photography — still open

Three images are needed and none is sourced:

| Page | Image | Note |
|---|---|---|
| **P1** cover | Olongapo / Zambales flooding | full-bleed |
| **P5** pivot | river aerial | full-bleed, low opacity behind text |
| **P9** | optional — a real alert or evacuation scene | the mockups can carry this page alone |

**Pick a sourcing route and stay in it:** official agency imagery (PAGASA, NDRRMC, PIA — check
the reuse terms), licensed stock, or the team's own photographs. Whichever you choose,
**credit it on the page**, and keep every image **under 2 MB** — that is a hard ADSE cap per
image, separate from the 20 MB document cap.

## Assembling

Route A from `docs/EXECUTION_SEQUENCE.md`, already agreed: **every chart is genuinely built
in SAC**, then the 15 pages are assembled in a layout tool and exported as one landscape PDF.
ADSE requires the charts to be SAC-generated; it does not require the PDF to come out of SAC.

Page template, consistent across all 15:

```
┌─────────────────────────────────────────────┐
│ SCOPE TAG                                   │  ← ASEAN / PHILIPPINES / ZAMBALES / OLONGAPO
│                                             │
│ Headline                                    │
│ Standfirst                                  │
│                                             │
│   ┌───────────────┐   • body bullet         │
│   │  SAC chart    │   • body bullet         │
│   └───────────────┘   • body bullet         │
│                                             │
│ Source line                                 │  ← 9–10 pt, muted
└─────────────────────────────────────────────┘
```

The scope tag is not decoration. Several August 2026 figures in this deck are **national**
totals that read like local ones, and mislabelling one is the easiest way to lose the deck's
credibility — it is the exact error that was cut from the first draft.

## Export gate — every item is pass/fail

- [ ] **≤ 15 pages** including cover, excluding references
- [ ] **Landscape** orientation
- [ ] **≤ 20 MB** total, each embedded image **≤ 2 MB**
- [ ] Filename **`PHILIPPINES_NAIVE BAIS.pdf`**
- [ ] Cover carries all six required elements — title, team, institution, country, SDGs, description
- [ ] Every chart legible at 100% **and** printed
- [ ] All charts visibly SAC-generated
- [ ] References page present
- [ ] All copy in English
- [ ] Read end to end, aloud, once

A fail on any of these scores zero regardless of what is on the pages. Never compress this
step to buy time somewhere else.
