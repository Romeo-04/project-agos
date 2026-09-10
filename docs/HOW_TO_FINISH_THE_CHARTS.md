# How to Finish the AGOS Charts — step by step

Written to be followed click-by-click in your own browser. No prior context needed.

**Tenant:** <https://aseandse.ap11.hcs.cloud.sap>
**Story:** `AGOS_Storyboard_NaiveBais` (open it from **Stories**)
**Working in your own browser is much faster than automation** — sessions stay alive and clicks don't get swallowed.

---

## Datasets already in the tenant — nothing to import for the next three charts

| Dataset | Use for |
|---|---|
| `AGOS_ASEAN_INFORM_2026` | P2 ✅, P3 ✅, **P15** |
| `AGOS_Olongapo_Rainfall_v2` | **P8** — has the `Date` column Time Series needs |
| `AGOS_Aeta_Isolation_v2` | **P11** — has the `Communities` count column |
| `AGOS_PH_vs_ASEAN` | P4 ✅ |

Only P10, P12, P14 and the P13 fallback still need a CSV imported (Recipe A).

---

## Already done — don't rebuild these

| Page | Chart | What it shows |
|---|---|---|
| **P3** | Bubble | ASEAN-10, flood hazard × coping capacity, sized by risk, coloured by quadrant |
| **P6** | Bar | Olongapo rainfall by month, **August auto-highlighted** |
| **P2** | Bar | ASEAN-10 river flood hazard, Viet Nam 9.90 → Singapore 0.00 |
| **P4** | Bar | Philippines gap vs ASEAN median — the −1.6 / +2.25 inversion |

All four are on **Page_1** of the story. Leave them; you'll rearrange during page assembly.

---

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

## Build these, in this order

### 1. P11 — Aeta community isolation ⭐ highest value

**Dataset is already imported** as **`AGOS_Aeta_Isolation_v2`** — skip Recipe A, go straight to Recipe B.

| Setting | Value |
|---|---|
| Chart type | **Bar/Column** |
| Measure | `Communities` |
| Dimension | `Access method during cutoff` |
| Colour | `Access method during cutoff` |

**Expected: Helicopter airlift 9, Carabao-drawn cart 2.** If you see 11 and 11, the measure is wrong.

Page text to go beside it: on **6 September 2026**, 11 Aeta communities in Botolan — **2,519 families** — were cut off by the swollen Bucao. Nine reached by Air Force helicopter, two by carabao cart. A father and his 5-year-old daughter drowned that week crossing to Barangay Palis.

> Do **not** chart `Distance from town proper (km)`. The source gives one range for the whole group (25–30 km), stored as a midpoint so the file loads. Charting it per barangay would invent precision that isn't in the source. Use "25–30 km from the town proper" as text on the page.

---

### 2. P15 — Where AGOS scales next

No import needed — reuses `AGOS_ASEAN_INFORM_2026`.

Build it exactly like P3 (copy/paste the P3 chart if easier: select it → **More Actions → Copy**, then paste):

| Setting | Value |
|---|---|
| Chart type | **Bubble** |
| X-Axis | `River flood hazard (0-10)` |
| Y-Axis | `Lack of coping capacity (higher = weaker)` |
| Size | `INFORM Risk score (0-10)` |
| Dimension | `Country` |
| Colour | `Quadrant` |

Then annotate the weak-capacity corner: **Myanmar 5.6 · Lao PDR 5.6 · Cambodia 5.5**. Those are the scaling targets.

---

### 3. P8 — Rainfall forecast ⭐ this one earns the Innovation marks

**Dataset is already imported** as **`AGOS_Olongapo_Rainfall_v2`**, with a real `Date` column
that SAC types as a date — verified. Skip Recipe A, go straight to Recipe B.

| Setting | Value |
|---|---|
| Chart type | **Time Series** |
| Measure | `Rainfall (mm)` |
| Time dimension | **`Date`** (not `Month` — Time Series rejects text dimensions) |

The year 2026 in the `Date` column is nominal: these are 30-year normals, not one year's
observations. Say so on the page — "PAGASA 30-year monthly normals" — so nobody reads it as
a single season.

Then: **Chart Add-Ons → Predictive Forecast**.

Innovation is 15% and explicitly rewards *"integration of AI and digital technologies."* A visible forecast band scores; the word "predictive" in a sentence does not. **If you build only one more chart, build this one.**

---

### 4. P10 — What one hour of warning is worth

- Recipe A with `leadtime_scenarios.csv` → name **`AGOS_LeadTime`**

| Setting | Value |
|---|---|
| Chart type | **Line** |
| Measures | `Current reactive warning (% evacuated)` **and** `With AGOS lead time (% evacuated)` |
| Dimension | `Minutes from first alert` |

Both measures go on the **same axis** — they share a unit. Never make this a dual-axis chart.

**Print the assumptions on the page.** They're in `data/processed/model_assumptions.csv`, rows A1–A4. A model with visible assumptions is credible; one with hidden assumptions gets taken apart in Q&A. The 2-hour lead time (A3) is the number a judge is most likely to challenge — be ready to say it's an estimate pending channel travel-time validation.

---

### 5. P12 — Risk matrix

- Recipe A with `risk_matrix.csv` → name **`AGOS_Risk_Matrix`**

| Setting | Value |
|---|---|
| Chart type | **Heat Map** |
| Measure | `Risk score` |
| Dimensions | `Likelihood (1-5)` and `Impact (1-5)` |

Single-hue ramp, light → dark. Not a rainbow.

---

### 6. P14 — Roadmap

- Recipe A with `roadmap_phases.csv` → name **`AGOS_Roadmap`**

| Setting | Value |
|---|---|
| Chart type | **Bar/Column**, Horizontal |
| Measure | `End month` |
| Dimension | `Phase name` |

`KPI target` is deliberately blank — those numbers are your team's commitment to make, not mine to invent.

---

### 7. P13 — FUND 🔒 blocked on you

Needs two figures nobody has yet:

- **Lahar-sand sale price per m³** — Zambales Provincial Treasurer's Office
- **Sensor unit cost, installation, annual LGU subscription** — vendor quotes

**If you get them:** build revenue vs cost over the roadmap horizon.

**If you don't:** ship the page without a revenue chart. Use the sourced lahar figures instead, which are strong on their own:

- Recipe A with `zambales_lahar_dredging.csv` → **Bar/Column**, Measure `Volume (million m3)`, Dimension `Status`
- That single chart says **1.06% dredged in 35 years** — the best argument in the deck that the constraint is financing cadence, not engineering

I deliberately didn't invent placeholder pricing. A made-up revenue projection is the same mistake as the misattributed figures we removed from v1, and it would fall apart under the first Viability question.

---

### 8. P9 and P7 — build last, or not at all

Lowest value. P9 (alert reach by channel) needs a dataset that doesn't exist yet; P7 only wants a small tile beside the architecture diagram. **Both pages work fine as static graphics.** If you're short on time, these are the two cheapest things to drop.

---

## Traps that will cost you time

| Trap | What to do |
|---|---|
| A save seems to work but nothing persisted | The session expired. **Always reload and re-check after saving.** |
| "Change Language" popup keeps blocking things | Tick *Do not ask me again*, or click **Change** |
| Reimporting an existing dataset gets rejected | Reimport needs **identical column names**. Changed a column? Import as a new dataset instead. |
| A chart shows old values after you fix the data | The story caches the dataset. Remove it from the story's Data panel and re-add it. |
| P6's months are out of calendar order | Same cache. Same fix. Cosmetic — no figure is wrong. |

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
