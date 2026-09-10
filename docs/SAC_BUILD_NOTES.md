# AGOS — SAC Build Notes

Working recipe for building the storyboard charts in SAP Analytics Cloud, validated end to end on 2026-09-10.

**Tenant:** `https://aseandse.ap11.hcs.cloud.sap`
**Story:** `AGOS_Storyboard_NaiveBais` (Canvas type)
**Owner:** NAIVEBAIS

---

## Smoke test result — PASSED

Before committing to 13 charts, one chart was built end to end to prove the automation path. It worked, and the result was kept rather than discarded (the P3 chart is real, not a throwaway).

| Step | Result |
|---|---|
| CSV import → dataset | **Works.** SAC auto-typed correctly with zero manual fixing |
| Dataset → story | **Works** |
| Insert chart | **Works** — via Insert toolbar, *not* drag |
| Chart type → Bubble | **Works** |
| Bind measures / dimensions / colour | **Works** |
| Save | **Works** |

**Conclusion: the plan is buildable as specified.** No chart type in the spec is missing from this tenant.

---

## Why Canvas, not Responsive

Canvas gives absolute positioning and fixed page dimensions. Responsive reflows content, which fights a landscape PDF that must land on an exact page count. For a storyboard with a hard 15-page cap, Canvas is the correct choice.

---

## Automation gotchas — read before driving the UI

These cost time to discover. They will recur on every remaining chart.

**1. Drag-and-drop does not work.**
Playwright's `dragTo` does not drive UI5's HTML5 drag implementation — the widget arms but never drops. **Use the Insert toolbar instead:** `button[title="Chart"]`, `button[title="Table"]`, etc.

**2. The toolbar lives in shadow DOM.**
A plain `document.querySelectorAll('button')` finds almost nothing in the toolbar band. Pierce shadow roots:

```js
const walk = (root) => {
  root.querySelectorAll('*').forEach(el => {
    if (el.shadowRoot) walk(el.shadowRoot);
    // ...inspect el
  });
};
walk(document);
```

Buttons are reliably addressable afterwards by `button[title="<Tooltip>"]`.

**3. Two different UI frameworks, and it matters for selectors.**
The Data panel is **UI5** (`.Text_text_*` classes); the measure/dimension pickers are **MUI** (`.MuiTypography-root`, `.MuiListItem-root`). A bare text selector matches both and clicks the wrong one.

Use `.MuiTypography-root:text-is("<FieldName>")` to hit the picker specifically.

**4. Popovers block the next click.**
After choosing a field, a `.uqmMenuBackdrop` or `ui5-li-content` overlay can intercept pointer events, and the next click times out with "subtree intercepts pointer events." **Press `Escape` before clicking anything outside the popover.**

**5. Slot selectors shift as you fill them.**
`text="At least 1 Measure required"` matches every unfilled measure slot. As each is filled, the remaining ones renumber, so `nth=0` walks the list naturally: X-Axis → Y-Axis → Size.

**6. Leaving the dataset editor prompts to save.**
Navigating away raises "You have unsaved changes." Click **Save** in that dialog; it completes the navigation afterwards.

**7. The session expires, and a failed save looks exactly like a successful one.**
This bit us once and cost a rebuild. SAC's session died mid-build; the next `Save` silently
did nothing, and **the breadcrumb showed no unsaved-changes asterisk**, because the page was
stale rather than saved. Everything looked fine until a re-login revealed the story had
reverted to its last genuine save.

- **Never treat the missing asterisk as proof of a save.** On a dead session it means nothing.
- **Verify a save by reloading the page and re-reading the chart**, not by inspecting UI state.
- Save after *every* chart, so a session death costs one chart at most.
- On "Session Ended", clicking **Log On** re-authenticates from the existing SSO cookie
  without re-entering credentials — but everything since the last genuine save is gone.

**8. Reimport requires an exact schema match.**
`Reimport Data` on an existing dataset is far cheaper than a fresh import, because it keeps
the dataset ID and every chart binding pointing at it stays valid. But SAC rejects it with
*"Reimport is allowed only when all columns match in terms of name and data type"* if a
single column has been renamed.

**So: when changing data that is already imported, change values freely but never the column
names.** If a rename is genuinely needed, it is a fresh import plus rebinding every chart.

Also note the **Dependencies** dialog fires before the reimport dialog and blocks the
toolbar; click its OK, then click Reimport again.

**9. Screenshots default to the repo root.**
Always pass `.playwright-mcp/<name>.png`. Root-level images are gitignored as a backstop, but the artifacts belong in the ignored folder, not scattered.

---

## Dataset import recipe

1. **Datasets** → *From a CSV or Excel File* → **Select Source File**
2. Upload the CSV; keep **Use first row as column headers** checked; delimiter **Auto-detect**
3. **Create** → wait for "Preparing data import…"
4. Name it `AGOS_<page>_<subject>`; write a description that includes **source and retrieval date**
5. **Save**, then **Save** again if the leave-prompt appears

### Verified: SAC types our CSVs correctly with no intervention

For `asean_inform_multidim_2026.csv` it produced, unprompted:
- **Measures (7):** FloodHazard, HazardExposure, Vulnerability, LackOfCopingCapacity, InformRisk, MedianFloodHazard, MedianLackOfCopingCapacity
- **Dimensions (3):** Country, ISO3, Quadrant

This is why the Phase 1 CSVs were written flat, with plain headers and no thousands separators. It paid off.

### Known configuration item — aggregation

Imported measures default to **SUM**. For 0–10 index scores that is meaningless if anything ever aggregates across countries ("ASEAN total flood hazard = 71.0" is nonsense).

It does not affect the current charts, which are per-country with no aggregation, and the ASEAN medians are precomputed in the CSV rather than derived in SAC. **But if any chart is later changed to aggregate, switch those measures to AVERAGE first.**

---

## Chart build recipe

1. Select the page, click `button[title="Chart"]` in the **Insert** toolbar
2. In **Builder**, set *Currently Selected Chart* to the required type
3. Fill the slots in order; press `Escape` after each picker closes
4. Set the title, axis labels, and data labels
5. **Save the story before starting the next chart** — never hold unsaved work across charts

### Chart types confirmed available in this tenant

Bar/Column · Line · Numeric Point · Gauge · Combination Column & Line · Pareto · Stacked Bar/Column · Combination Stacked Column & Line · Area · Stacked Area · Pie · Donut · Bullet · **Time Series** · **Heat Map** · Waterfall · Tree Map · Box Plot · Marimekko · **Bubble** · Histogram · **Scatterplot** · Cluster Bubble · Radar · Funnel · Sankey

Every type the storyboard plan calls for is present.

---

## Datasets in the tenant

| Dataset | Source CSV | Backs |
|---|---|---|
| `AGOS_ASEAN_INFORM_2026` | `asean_inform_multidim_2026.csv` | P2, P3, P15 |
| `AGOS_PH_vs_ASEAN` | `ph_vs_asean_dimensions.csv` | P4 |
| `AGOS_Olongapo_Rainfall` | `olongapo_rainfall_normals.csv` | P6, P8 |
| `AGOS_Aeta_Isolation` | `aeta_botolan_isolation_sept2026.csv` | P11 |

Still to import: `leadtime_scenarios` (P10), `risk_matrix` (P12), `roadmap_phases` (P14),
`zambales_lahar_share` + `zambales_lahar_dredging` (P13), `olongapo_aug2026_events` (P6 support).

`AGOS_P3_ASEAN_INFORM_2026` is the **superseded** first import, kept only until the P3 chart
is repointed at `AGOS_ASEAN_INFORM_2026`. Delete it after that, or it will confuse whoever
opens the tenant next.

### Import loop, condensed

Datasets nav → *(Save if the unsaved-changes prompt appears)* → CSV tile →
`button:has-text("Select Source File")` → `browser_file_upload` →
`button:has-text("Create")` → wait ~8s → set Name → `button:has-text("Save")` → wait ~8s.

Roughly nine calls per dataset. The Name field ref changes every time, so locate it with a
find on the source filename rather than caching a ref.

---

## P3 — BUILT, SAVED, VERIFIED BY RELOAD

**Chart:** Bubble · **Dataset:** `AGOS_ASEAN_INFORM_2026` · **Size:** default (resize during page assembly)

| Slot | Field |
|---|---|
| X-Axis | `River flood hazard (0-10)` |
| Y-Axis | `Lack of coping capacity (higher = weaker)` |
| Size | `INFORM Risk score (0-10)` |
| Dimension | `Country` |
| Colour | `Quadrant` |

Renders all 10 ASEAN states. Axis titles come through correctly from the column names, so
the "higher = weaker" warning is on the chart without any UI editing — which was the whole
point of moving labels into the data layer.

The legend shows **three** quadrants, not four: no ASEAN member state occupies *High flood
hazard / Stronger capacity*. True property of the data, not a rendering fault.

Data spot-checked against source via the chart tooltip — Brunei Darussalam reads 4.70 /
2.80 / 2.30, matching `asean_inform_multidim_2026.csv` exactly.

**Persistence confirmed the hard way.** The first attempt at this rebuild was lost to a
silent save failure on an expired session. This version was re-verified by reloading the
page and re-reading the chart: title, both axis labels, legend and all 10 bubbles came back.

**A working save route when the toolbar menu misbehaves:** click `button[title="Save"]` to
open the File menu, then press **Enter** — the menu opens with *Save* already highlighted,
and the menu items sit in shadow DOM where text selectors cannot reach them.

**Superseded dataset removed.** On save, SAC offered to drop the now-unused
`AGOS_P3_ASEAN_INFORM_2026` from the story ("Remove Models"); accepted, so only the
re-headered dataset remains attached.

### Still to do on P3

- [ ] Replace the auto-generated title with the page headline
- [ ] Apply the validated categorical palette (still on default `sapColorfulPalette`)
- [ ] Turn on data labels — required by the contrast WARN *and* ADSE's readability rule
- [ ] Source note on chart: *INFORM Risk Mid 2026, EC JRC*
- [ ] Annotate the high-hazard / weak-capacity quadrant

---

## P6 — BUILT, one open issue

**Chart:** Bar/Column (horizontal) · **Dataset:** `AGOS_Olongapo_Rainfall`

| Slot | Field |
|---|---|
| Measure | `Rainfall (mm)` |
| Dimension | `Month` |
| Colour | `Wettest month` |

Renders all 12 months with data labels on, and the **August bar is highlighted automatically**
because `Wettest month = Yes` drives the colour. That part works exactly as designed — the
emphasis is data-driven, not hand-picked.

### Open issue: month order (cosmetic, one chart)

SAC sorts the dimension alphabetically, so the months render out of calendar sequence. The
data fix is done and verified — the dataset holds `01 Jan` … `12 Dec` — but the **story keeps
its own cached copy of the model's dimension members**, and none of these clears it:

- reloading the story page
- deleting the chart and building a brand-new one
- `Data Refresh` from the File toolbar

So this is a story-level model cache, not a chart-level one. Untried options, cheapest first:
1. Remove `AGOS_Olongapo_Rainfall` from the story's Data panel entirely, then re-add it
2. Build the affected pages in a **new story** (a fresh story reads members fresh)
3. Leave it and fix the order during page assembly, since the export is an image anyway

**This is cosmetic and affects one chart.** It does not touch any figure: August is still
865.97 mm, still highlighted automatically off the `Wettest month` flag, still 25.6% of annual.
Deprioritised in favour of building the remaining charts.

---

## Remaining build queue

Pages in score order, per `EXECUTION_SEQUENCE.md`. Datasets marked ✅ are already in the tenant.

| # | Page | Chart | Dataset |
|---|---|---|---|
| ~~1~~ | ~~P3~~ | ~~Bubble quadrant~~ | ✅ **DONE** |
| 2 | P6 | Column, August highlighted | ✅ `AGOS_Olongapo_Rainfall` |
| 3 | P8 | Time series + SAC forecast | ✅ `AGOS_Olongapo_Rainfall` |
| 4 | P2 | Horizontal bar, 10 states | ✅ `AGOS_ASEAN_INFORM_2026` |
| 5 | P4 | Diverging bar, gap vs median | ✅ `AGOS_PH_vs_ASEAN` |
| 6 | P11 | Access method by barangay | ✅ `AGOS_Aeta_Isolation` |
| 7 | P15 | Quadrant + deployment priority | ✅ `AGOS_ASEAN_INFORM_2026` |
| 8 | P10 | Lead-time scenarios | ⬜ import `leadtime_scenarios.csv` |
| 9 | P13 | Revenue vs cost | ⬜ **blocked on pricing inputs** |
| 10 | P12 | Risk heat map | ⬜ import `risk_matrix.csv` |
| 11 | P14 | Roadmap timeline | ⬜ import `roadmap_phases.csv` |
| 12 | P9 | Alert reach by channel | ⬜ |
| 13 | P7 | Architecture data tile | ⬜ |

**Pace observed:** roughly 12–15 tool calls per chart once the dataset is in, plus about 9
per dataset import. The first chart cost far more because of the UI discovery recorded above;
that cost is now paid and does not recur.

### Page creation

`+` next to the page tab → **Add Canvas Page** / Add Responsive Page / Import Story Pages.
Use **Add Canvas Page** for every storyboard page, to match Page_1.
