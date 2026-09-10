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

**7. Screenshots default to the repo root.**
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

## P3 — built

**Chart:** Bubble
**Dataset:** `AGOS_P3_ASEAN_INFORM_2026`

| Slot | Field |
|---|---|
| X-Axis | `FloodHazard` |
| Y-Axis | `LackOfCopingCapacity` |
| Size | `InformRisk` |
| Dimension | `Country` |
| Colour | `Quadrant` |

Renders all 10 ASEAN states. The legend shows **three** quadrants, not four — no ASEAN member state occupies *High flood hazard / Stronger capacity*. That is a true property of the data, not a rendering fault.

### Outstanding refinements for P3

- [ ] Title → *"Hazard and capacity are independent. Where they diverge, floods become disasters."*
- [ ] **Y-axis label must read "Lack of coping capacity (higher = weaker)"** — without it the chart reads backwards
- [ ] X-axis label → "River flood hazard (INFORM, 0–10)"
- [ ] Apply the validated categorical palette; the default `sapColorfulPalette` has not been colour-validated
- [ ] Data labels on (required — resolves the contrast WARN and ADSE's readability rule)
- [ ] Source note on chart: *INFORM Risk Mid 2026, EC JRC*
- [ ] Annotate the high-hazard / weak-capacity quadrant
