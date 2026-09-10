# AGOS — Per-Chart Build Sheet

Exact specification for every storyboard chart, so any of us can build them in SAC without re-deriving anything. Follow `SAC_BUILD_NOTES.md` for the mechanics and gotchas.

**Story:** `AGOS_Storyboard_NaiveBais` (Canvas) · **Tenant:** `https://aseandse.ap11.hcs.cloud.sap`

**Status:** ✅ built and verified · ⬜ not built · 🔒 blocked

---

## The loop, per chart

1. `button[title="Chart"]` in the **Insert** toolbar (never drag — UI5 drag is not automatable)
2. If the dataset isn't in the story yet: Builder → the pencil beside **Data Source** → *Select other model…* → search → double-click
3. Set **Currently Selected Chart**
4. Fill each slot; press **Escape** after every picker or the next click is swallowed
5. Save: click `button[title="Save"]`, then press **Enter** (menu items are in shadow DOM)
6. **Verify by reloading the page** — a dead session makes a failed save look identical to a good one

---

## ✅ P3 — Hazard × coping capacity

**Bubble** · `AGOS_ASEAN_INFORM_2026`

| Slot | Field |
|---|---|
| X-Axis | `River flood hazard (0-10)` |
| Y-Axis | `Lack of coping capacity (higher = weaker)` |
| Size | `INFORM Risk score (0-10)` |
| Dimension | `Country` |
| Colour | `Quadrant` |

Legend shows three quadrants, not four — no ASEAN state sits in high-hazard/strong-capacity. That is real.

---

## ✅ P6 — Olongapo rainfall normals

**Bar/Column** · `AGOS_Olongapo_Rainfall`

| Slot | Field |
|---|---|
| Measure | `Rainfall (mm)` |
| Dimension | `Month` |
| Colour | `Wettest month` |

August auto-highlights off the `Wettest month` flag. Month order is alphabetical — see the open issue in `SAC_BUILD_NOTES.md`.

---

## ⬜ P2 — ASEAN flood exposure

**Bar/Column, orientation Horizontal** · `AGOS_ASEAN_INFORM_2026` *(already in the story)*

| Slot | Field |
|---|---|
| Measure | `River flood hazard (0-10)` |
| Dimension | `Country` |

Sort descending by measure. The Philippines lands **8th of 10** — leave it there. That rank is the setup for P4, and hiding it would cost more than it gains.

---

## ⬜ P4 — Philippines vs ASEAN median

**Bar/Column, orientation Horizontal** · `AGOS_PH_vs_ASEAN` *(import needed)*

| Slot | Field |
|---|---|
| Measure | `Gap vs ASEAN median` |
| Dimension | `Dimension` |

Diverging around zero: negative on river flood hazard (−1.6), strongly positive on all-hazard exposure (+2.25). Two hues with a neutral grey at zero — never a hue at the midpoint.

---

## ⬜ P11 — Aeta community isolation

**Bar/Column** · `AGOS_Aeta_Isolation` *(already imported)*

| Slot | Field |
|---|---|
| Measure | `Barangay` (count) |
| Dimension | `Access method during cutoff` |
| Colour | `Access method during cutoff` |

Result: **9 helicopter airlift, 2 carabao cart.** Do **not** chart `Distance from town proper (km)` per barangay — it is a single group range (25–30 km) from the source, carried as a midpoint so the file is loadable. Charting it per barangay would invent precision. Use it as a page annotation instead.

---

## ⬜ P15 — Scaling priority

**Bubble** · `AGOS_ASEAN_INFORM_2026` — same build as P3, then filter or annotate the high-hazard / weak-capacity quadrant. Call out **Myanmar 5.6, Lao PDR 5.6, Cambodia 5.5** on lack of coping capacity.

---

## ⬜ P8 — Rainfall to river level (forecast)

**Time Series** · `AGOS_Olongapo_Rainfall`

| Slot | Field |
|---|---|
| Measure | `Rainfall (mm)` |
| Time dimension | `Month` |

Then **Chart Add-Ons → Predictive Forecast**. This page is the whole Innovation claim (15%): a visible forecast band is scoreable, the adjective "predictive" is not.

---

## ⬜ P10 — Lead-time scenarios

**Line** · import `leadtime_scenarios.csv`

| Slot | Field |
|---|---|
| Measures | `Current reactive warning (% evacuated)` **and** `With AGOS lead time (% evacuated)` |
| Dimension | `Minutes from first alert` |

Both series share one unit and one axis — **never a dual axis**. Print assumptions A1–A4 from `model_assumptions.csv` on the page.

---

## ⬜ P12 — Risk matrix

**Heat Map** · import `risk_matrix.csv`

| Slot | Field |
|---|---|
| Measure | `Risk score` |
| Dimensions | `Likelihood (1-5)` × `Impact (1-5)` |

Sequential single-hue ramp, light → dark. Never a rainbow.

---

## ⬜ P14 — Roadmap

**Bar/Column, Horizontal** · import `roadmap_phases.csv`

| Slot | Field |
|---|---|
| Measure | `End month` |
| Dimension | `Phase name` |

`KPI target` is intentionally empty — those are the team's numbers to set, not ours to invent.

---

## 🔒 P13 — FUND revenue vs cost

**BLOCKED.** Needs two figures that do not exist yet:

- **A7** — lahar-sand sale price per m³ (Zambales Provincial Treasurer's Office)
- **A8** — sensor unit cost, installation cost, annual LGU subscription (vendor quotes)

No placeholder pricing will be invented. A fabricated revenue projection is the same failure mode as v1's misattributed figures and would not survive the first Viability question at finals.

**If they don't arrive:** ship P13 as the self-funding loop shown structurally, plus the *sourced* lahar baseline — **4.7 bn m³ deposited, 50 m m³ dredged, 1.06% in 35 years** — and no revenue chart. That still makes the argument honestly.

Charts available if wanted: `zambales_lahar_share.csv` (Bucao 63.8% / Santo Tomas 34.0%) and `zambales_lahar_dredging.csv` (1.06% vs 98.94%). Both are fully sourced and could carry the page on their own.

---

## ⬜ P9 — Alert reach by channel · ⬜ P7 — Architecture tile

Lowest value, build last. P9 needs a small channel-reach dataset; P7 needs only a sparkline beside the architecture diagram. If time runs out, both pages work as static graphics — they are the two cheapest things to lose.

---

## Datasets

| Dataset | Status |
|---|---|
| `AGOS_ASEAN_INFORM_2026` | ✅ imported, in story |
| `AGOS_Olongapo_Rainfall` | ✅ imported, in story |
| `AGOS_PH_vs_ASEAN` | ✅ imported, not yet in story |
| `AGOS_Aeta_Isolation` | ✅ imported, not yet in story |
| `leadtime_scenarios` · `risk_matrix` · `roadmap_phases` · `zambales_lahar_*` | ⬜ to import |

All source CSVs are in `data/processed/`, all regenerate from `scripts/`, all columns are already named so **axis titles come out right with no chart-editor work**.
