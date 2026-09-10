# How to Finish the AGOS Charts — step by step

Written to be followed click-by-click in your own browser. No prior context needed.

**Tenant:** <https://aseandse.ap11.hcs.cloud.sap>
**Story:** `AGOS_Storyboard_NaiveBais` (open it from **Stories**)
**Working in your own browser is much faster than automation** — sessions stay alive and clicks don't get swallowed.

---

## Every dataset is imported. Nothing left to import.

| Dataset | Backs |
|---|---|
| `AGOS_ASEAN_INFORM_2026` | P2, P3, P15 |
| `AGOS_PH_vs_ASEAN` | P4 |
| `AGOS_Olongapo_Rainfall` | P6 |
| `AGOS_Olongapo_Rainfall_v2` | P8 — has the `Date` column Time Series needs |
| `AGOS_Aeta_Isolation_v2` | P11 — has the `Communities` count column |
| `AGOS_LeadTime_v3` | P10 — minutes written as text so they type as a dimension |
| `AGOS_Risk_Matrix_v2` | P12 — ordered text labels; `Risk score` aggregates as MAX |
| `AGOS_Roadmap` | P14 |
| `AGOS_Lahar_Dredging` | P13 fallback |

**Always take the highest version suffix.** The unsuffixed twins are superseded imports
kept only so nothing breaks; binding a chart to one will give you the wrong field types.

---

## Already done — 11 of 13. Don't rebuild these.

All eleven were saved and re-checked after a page reload.

| Page | Chart | What it shows |
|---|---|---|
| **P2** | Bar | ASEAN-10 river flood hazard, Viet Nam 9.90 → Singapore 0.00 |
| **P3** | Bubble | ASEAN-10, flood hazard × coping capacity, sized by risk, coloured by quadrant |
| **P4** | Bar | Philippines gap vs ASEAN median — the −1.6 / +2.25 inversion |
| **P6** | Bar | Olongapo rainfall by month, **August auto-highlighted** |
| **P8** | Time Series | Rainfall normals across the year |
| **P10** | Line | Reactive warning vs AGOS lead time, 0 → 120 min, both on one axis |
| **P11** | Bar | Aeta access during cutoff — helicopter 9, carabao cart 2 |
| **P12** | Heat Map | Risk score over Likelihood × Impact, single-hue ramp |
| **P14** | Bar | Roadmap phases, ordered by End month |
| **P13** | Bar | Lahar dredged 50 vs remaining 4,650 million m³ — **1.06% in 35 years** |
| **P15** | Bubble | Where AGOS scales next |

They all sit on **Page_1** for now; rearrange during page assembly.

## The two recipes you'll repeat

### Recipe A — import a CSV as a dataset

1. Left nav → **Datasets**
2. Tile: **From a CSV or Excel File**
3. **Select Source File** → pick the CSV from `data/processed/`
4. Leave *Use first row as column headers* ticked, delimiter **Auto-detect**
5. **Create** → wait for "Preparing data import…"
6. Set the **Name** (given per chart below) → **Save**
7. If it asks again on leaving, click **Save**

> The column names are already written to be presentation-ready, so **axis titles come out correct automatically**. Don't rename anything.

### Recipe B — add a chart to the story

1. Open the story → **Insert** toolbar → **Chart** *(don't drag from the left panel — it doesn't work)*
2. New chart binds to whichever dataset was last used. To change it:
   **Builder** panel → pencil ✏️ beside **Data Source** →
   - dataset already in the story? pick it from the dropdown → **OK**
   - not yet? **Select other model…** → search → double-click it
3. Set **Currently Selected Chart** to the type listed
4. Fill each slot from the table
5. **Save** (Ctrl+S), then **reload the page** and check the chart is still there

> **Why reload:** if the SAC session has quietly expired, Save does nothing and the UI still looks fine. Reloading is the only reliable check. This cost me a rebuild — don't skip it.

---

## What is actually left

### 1. Polish the eleven built charts ⭐ this is where the marks are now

Every chart renders correct numbers. None of them has been styled. Per chart:

- [ ] Replace the auto-generated title with the page headline
- [ ] Apply the validated categorical palette — `#2E6FA8, #E0762F, #1FA8C4, #8C5BB0, #5A9E3E`
      *(the heat map keeps its own single-hue ramp; don't put categorical hues on it)*
- [ ] Data labels on — required by ADSE readability and by the contrast check
- [ ] Unit and source stated on the chart
- [ ] Legend for ≥2 series; direct labels where ≤4

### 2. P13 — the real revenue chart 🔒 blocked on you

Needs two figures nobody has yet:

- **Lahar-sand sale price per m³** — Zambales Provincial Treasurer's Office
- **Sensor unit cost, installation, annual LGU subscription** — vendor quotes

**If you get them:** build revenue vs cost over the roadmap horizon, and put both numbers
into `data/processed/model_assumptions.csv` rows A7 and A8 first, so they are cited.

**If you don't:** ship the fallback that is already built. `Volume (million m3)` by `Status`
says **1.06% dredged in 35 years** — 50 million m³ moved against 4,650 million m³ remaining.
It is the best argument in the deck that the constraint is financing cadence, not engineering.

I deliberately didn't invent placeholder pricing. A made-up revenue projection is the same
mistake as the misattributed figures we removed from v1, and it would fall apart under the
first Viability question.

### 3. P9 and P7 — build last, or not at all

Lowest value. P9 (alert reach by channel) needs a dataset that doesn't exist yet; P7 only
wants a small tile beside the architecture diagram. **Both pages work fine as static
graphics** — the mockups in `mockups/agos-screens.html` cover them. If you're short on time,
these are the two cheapest things to drop.

### 4. Predictive Forecast on P8 — not available here

Chart Add-Ons on this tenant offers only Reference Line, Tooltip, Hyperlink and Structure.
Predictive Forecast appears to be licence-gated. P8 ships as a plain time series, and the
Innovation claim rests on the SAR/Sentinel-1 reasoning plus the sensor architecture instead.
Worth one email to ADSE asking whether the licence can be switched on.

## Traps that will cost you time

| Trap | What to do |
|---|---|
| A save seems to work but nothing persisted | The session expired. **Always reload and re-check after saving.** |
| "Change Language" popup keeps blocking things | Tick *Do not ask me again*, or click **Change** |
| Reimporting an existing dataset gets rejected | Reimport needs **identical column names**. Changed a column? Import as a new dataset instead. |
| A chart shows old values after you fix the data | The story caches the dataset. Remove it from the story's Data panel and re-add it. |
| P6's months are out of calendar order | Same cache. Same fix. Cosmetic — no figure is wrong. |
| A column you expect as a measure isn't in the picker | SAC won't accept an all-numeric dataset and demotes the **last** column to a dimension. Fix the CSV, don't fight the UI. |
| A heat map cell shows a number bigger than any row | It's SUM-ing the rows in that cell. Change the measure's **Aggregation Type** on the *dataset* (Details tab) — the story Builder has no aggregation control, and there is no AVERAGE. |
| A light→dark gradient renders dark→light | Gradient position 0 maps to the **highest** value. Use the ⇄ swap button in *Edit Story Gradient Palette*. |
| Bars are in alphabetical order when order is inherent | Chart `...` → **Sort** → the measure → *Lowest to Highest*. |

---

## Exporting the charts

**Do this in your own browser.** A chart on the canvas is only about 370 px wide, and a
capture at that size is too soft to print. **⋯ → Full Screen** re-renders the chart at
roughly 1800 px, which is the version you want.

Per chart: click it → **⋯ → Full Screen** → screenshot *(Win+Shift+S)* → **Esc** → next.

Save into `deck/charts/` with these names:

```
P2_asean_flood.png      P3_quadrant.png       P4_ph_vs_median.png
P6_rainfall_month.png   P8_timeseries.png     P10_leadtime.png
P11_aeta_access.png     P12_risk_matrix.png   P13_lahar.png
P14_roadmap.png         P15_scaling.png
```

A 1× preview set may already be there — fine to lay pages out against, **not good enough to
submit**. Overwrite each as you export it properly.

**Style before you export, not after.** Otherwise you export twice.

Assembly instructions, the page template and the photography that is still unsourced are in
`deck/README.md`. The page text is finished and waiting in `docs/PAGE_COPY.md`.

---

## Before you export

Hard rules from ADSE. Any miss is fatal.

- [ ] **≤15 pages** including cover, excluding references
- [ ] **Landscape**, PDF, **≤20 MB**, each image **≤2 MB**
- [ ] Filename **`PHILIPPINES_NAIVE BAIS.pdf`**
- [ ] Cover has all six: title · team name · institution · country · SDGs · description
- [ ] Every chart legible at 100% and in print
- [ ] References page included *(generate from `docs/SOURCES.md`)*
- [ ] Every number on every page traces to a row in `SOURCES.md`

Cover block, confirmed: **Naive Bais** · FEU – Institute of Technology · Philippines · SDG 11 + SDG 13 · Jhezra A. Tolentino, Sean Matthew L. Viacrusis.

---

## If a number gets questioned

`docs/SOURCES.md` has every figure with its source, date and **geographic scope**. It also has a *Rejected* table listing three figures from the original plan that didn't survive checking — including the PHP 690M that was actually national agriculture damage, not Olongapo flood damage. Don't let those back in.
