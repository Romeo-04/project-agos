# AGOS — Per-Chart Build Sheet

Exact specification for every storyboard chart, so any of us can build them in SAC without re-deriving anything. Follow `SAC_BUILD_NOTES.md` for the mechanics and gotchas.

**Story:** `AGOS_Storyboard_NaiveBais` (Canvas) · **Tenant:** `https://aseandse.ap11.hcs.cloud.sap`

**Status:** ✅ built · ⬜ not built · 🔒 blocked
**11 of 13 built and verified by reload: P2, P3, P4, P6, P8, P10, P11, P12, P13-fallback, P14, P15.**
Only P9 and P7 remain, and both are planned as static graphics. P13's *revenue* chart is
still blocked on pricing; the lahar-dredging chart stands in for it and is built.

**Reliable way to change chart type** (the scripted approaches silently fail):
click the *value* text in the Currently Selected Chart combobox, then click the type inside
`[data-testid="custom-select-popper"]`. Clicking the combobox wrapper toggles it shut again.

**Do not use the Delete key to remove a chart** — selection is easy to misjudge and it acts
on whatever SAC thinks is focused. Use the chart's own **More Actions → Delete**.

**Charts scroll horizontally off-canvas and SAC virtualises them.** A DOM text scan will
report a chart as missing when it is only off-screen. Verify by screenshot, not by scanning.

**Repointing a chart's dataset:** the Select Model dropdown will not accept a scripted
`.click()` on an option. Click the combobox, press **ArrowDown** to select, **Enter** to
commit, then **OK**. That sequence works reliably.

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

## ✅ P2 — ASEAN flood exposure

**Bar/Column, orientation Horizontal** · `AGOS_ASEAN_INFORM_2026`

Renders all 10 states with data labels: Viet Nam 9.90 · Thailand 9.80 · Myanmar 8.80 ·
Cambodia 8.60 · Indonesia 8.40 · Lao PDR 8.20 · Malaysia 6.80 · **Philippines 6.70** ·
Brunei 4.70 · Singapore 0.00. Currently ordered alphabetically; sort descending by measure
during polish.

| Slot | Field |
|---|---|
| Measure | `River flood hazard (0-10)` |
| Dimension | `Country` |

Sort descending by measure. The Philippines lands **8th of 10** — leave it there. That rank is the setup for P4, and hiding it would cost more than it gains.

---

## ✅ P4 — Philippines vs ASEAN median

**Bar/Column, orientation Horizontal** · `AGOS_PH_vs_ASEAN`

| Slot | Field |
|---|---|
| Measure | `Gap vs ASEAN median` |
| Dimension | `Dimension` |

Renders diverging around zero, and the inversion reads in one glance:
**all-hazard exposure +2.25** and **INFORM Risk +1.10** to the right, **river flood hazard
−1.6** to the left, vulnerability +1.30, coping capacity −0.10.

Still to polish: two hues with a neutral grey at zero — never a hue at the midpoint.

---

## ✅ P11 — Aeta community isolation

**Bar/Column** · `AGOS_Aeta_Isolation_v2`

| Slot | Field |
|---|---|
| Measure | `Communities` |
| Dimension | `Access method during cutoff` |

Renders **Helicopter airlift 9, Carabao-drawn cart 2** — verified. Do **not** chart `Distance from town proper (km)` per barangay — it is a single group range (25–30 km) from the source, carried as a midpoint so the file is loadable. Charting it per barangay would invent precision. Use it as a page annotation instead.

---

## ✅ P15 — Scaling priority

**Bubble** · `AGOS_ASEAN_INFORM_2026` — built, same bindings as P3. Still to do: annotate the
high-hazard / weak-capacity corner and call out **Myanmar 5.6, Lao PDR 5.6, Cambodia 5.5**.

---

## ✅ P8 — Rainfall to river level

**Time Series** · `AGOS_Olongapo_Rainfall`

| Slot | Field |
|---|---|
| Measure | `Rainfall (mm)` |
| Time dimension | `Month` |

Renders the seasonal curve in correct calendar order.

> **Forecast is not available on this tenant.** Chart Add-Ons offers only Reference Line,
> Tooltip, Hyperlink and Structure — no Predictive Forecast. Likely licence-gated. If it
> cannot be enabled, the Innovation claim rests on the SAR/Sentinel-1 cloud-penetration
> reasoning and the sensor architecture instead, both already written up in the plan.

---

## ✅ P10 — Lead-time scenarios

**Line** · `AGOS_LeadTime_v3`

| Slot | Field |
|---|---|
| Left Y-Axis | `Current reactive warning (% evacuated)` **and** `With AGOS lead time (% evacuated)` |
| Dimension | `Minutes from first alert` |

Both series share one unit and sit on the **left axis only** — the Right Y-Axis slot is
deliberately empty. Never make this a dual axis.

Reads `000 min` → `120 min` in order because the minutes are stored as zero-padded text;
SAC sorts dimension members as strings. Reactive tops out at 79%, AGOS reaches 100%.

**Print assumptions A1–A4 from `model_assumptions.csv` on the page.** A3 — the two-hour lead
time — is the number a judge is most likely to challenge; be ready to say it is an estimate
pending channel travel-time validation.

---

## ✅ P12 — Risk matrix

**Heat Map** · `AGOS_Risk_Matrix_v2`

| Slot | Field |
|---|---|
| X-Axis | `Likelihood` *(text: `2 Unlikely` … `5 Almost certain`)* |
| Y-Axis | `Impact` *(text: `3 Moderate` … `5 Severe`)* |
| Colour | `Risk score` |

Use the **text** `Likelihood` / `Impact` columns, not the numeric `(1-5)` ones — SAC types
bare integers as measures, and a heat map needs a dimension on each axis. The number prefix
keeps the scale in order.

`Risk score` aggregates as **MAX**, set on the dataset (Details → Aggregation Type). On SUM
the 4×5 cell read 40 instead of 20, because two risks share it. Every risk in a cell has the
same likelihood and impact, so MAX *is* the cell's score. There is no AVERAGE option.

Colour is a **Story Palette** gradient, `9E1F17` → `FBE0DD`: one hue, light → dark, using the
evacuate red from the design tokens. Not a rainbow, and not `sapColorfulGradientPalette`.
Gradient stop 0 maps to the *highest* value, so the ramp needs swapping — the ⇄ button.

Cells read 8, 9, 12, 12, 15, 16, 20 — exactly likelihood × impact.

---

## ✅ P14 — Roadmap

**Bar/Column, Horizontal** · `AGOS_Roadmap`

| Slot | Field |
|---|---|
| Measure | `End month` |
| Dimension | `Phase name` |

Sorted **End month, Lowest to Highest** (chart `...` → Sort), which puts the phases in
chronological order: Engagement & Planning 3 → Deployment & Set-up 9 → Operation & Monsoon
Stress Test 15 → Scaling & Reporting 24. Left on the default order it sorts alphabetically
and the roadmap reads out of sequence.

`KPI target` is intentionally empty — those are the team's numbers to set, not ours to invent.

---

## 🔒 P13 — FUND revenue vs cost

**BLOCKED.** Needs two figures that do not exist yet:

- **A7** — lahar-sand sale price per m³ (Zambales Provincial Treasurer's Office)
- **A8** — sensor unit cost, installation cost, annual LGU subscription (vendor quotes)

No placeholder pricing will be invented. A fabricated revenue projection is the same failure mode as v1's misattributed figures and would not survive the first Viability question at finals.

### ✅ The fallback is built

**Bar/Column** · `AGOS_Lahar_Dredging`

| Slot | Field |
|---|---|
| Measure | `Volume (million m3)` |
| Dimension | `Status` |

Reads **Dredged since 1991 = 50** against **Remaining in river systems = 4,650**. That single
pair is **1.06% in 35 years** and makes the financing-cadence argument honestly, with no
invented numbers. If the pricing never arrives, ship this and drop the revenue chart.

Still available if a second visual is wanted: `zambales_lahar_share.csv` (Bucao 63.8% /
Santo Tomas 34.0%), fully sourced.

---

## ⬜ P9 — Alert reach by channel · ⬜ P7 — Architecture tile

Lowest value, build last. P9 needs a small channel-reach dataset; P7 needs only a sparkline beside the architecture diagram. If time runs out, both pages work as static graphics — they are the two cheapest things to lose.

---

## Datasets

All imported and bound. Take the highest version suffix — the unsuffixed twins are
superseded imports, kept only so nothing breaks, and they have the wrong field types.

| Dataset | Backs |
|---|---|
| `AGOS_ASEAN_INFORM_2026` | P2, P3, P15 |
| `AGOS_PH_vs_ASEAN` | P4 |
| `AGOS_Olongapo_Rainfall` | P6 |
| `AGOS_Olongapo_Rainfall_v2` | P8 |
| `AGOS_Aeta_Isolation_v2` | P11 |
| `AGOS_LeadTime_v3` | P10 |
| `AGOS_Risk_Matrix_v2` | P12 |
| `AGOS_Roadmap` | P14 |
| `AGOS_Lahar_Dredging` | P13 fallback |

All source CSVs are in `data/processed/`, all regenerate from `scripts/`, all columns are already named so **axis titles come out right with no chart-editor work**.
