# AGOS — Final Page Copy

Paste-ready text for all 15 pages. Nothing here needs rewriting; drop it into the layout
and place the SAC chart beside it.

**Every number below traces to a row in `SOURCES.md`.** The bracketed IDs are those rows.
If a figure gets challenged, that register has the source, the publication date and — the
part that matters most here — the **geographic scope**.

**House rules for the layout**

- **Scope tag** goes top-left of every page, small caps, muted ink: `ASEAN` / `PHILIPPINES` /
  `ZAMBALES` / `OLONGAPO`. Several figures in circulation about August 2026 are national
  totals that read like local ones. The tag is what stops a judge mis-reading them.
- **Source line** goes bottom-left, one line, 9–10 pt, muted.
- Headline ≤ 12 words. Standfirst is one sentence. Body is bullets, never paragraphs.
- Numbers in body copy are **bold**; units are not.

---

## P1 — Cover

**No chart.** Full-bleed Olongapo/Zambales flood photograph, ≤ 2 MB.

> # AGOS
> ### The flood warning that reaches the last house on the river.

**Required block — all six ADSE elements, bottom third of the page:**

| | |
|---|---|
| **Team** | Naive Bais |
| **Institution** | FEU – Institute of Technology |
| **Country** | Philippines |
| **SDGs** | SDG 11 — Sustainable Cities and Communities · SDG 13 — Climate Action |
| **Members** | Jhezra A. Tolentino · Sean Matthew L. Viacrusis |

**Description (one sentence, must name the solution):**

> AGOS is a river-sensing and community-verified flood warning system for Zambales,
> Philippines — turning rainfall into hours of warning for the households that regional
> flood indices under-count and existing alerts reach last.

*Two words carry weight here.* **Under-count**, not "cannot see": an index is a
country-level scoring instrument with no detection function, and what P4 proves is that it
scores the hazard too low. And the word **predictive** was removed — it was the first
adjective a judge read, and P8 ships as a plain time series because SAC's Predictive
Forecast is licence-gated on this tenant. "Turning rainfall into hours of warning" makes the
same claim as an outcome, which the deck can actually show.

**Export as** `PHILIPPINES_NAIVE BAIS.pdf`

---

## P2 — Flood exposure is an ASEAN condition

`ASEAN` · Chart: **bar** — river flood hazard, 10 states

> ## Six of ten ASEAN states face severe river flood hazard.
> ### This is not one country's problem, and it is not one country's solution.

- Viet Nam **9.9**, Thailand **9.8**, Myanmar **8.8**, Cambodia **8.6**, Indonesia **8.4**,
  Lao PDR **8.2** all sit at or above 8 on a 0–10 scale. [S1]
- The Philippines sits **8th of ten**, at **6.7**. [S1]
- Singapore scores **0.0** — the one member state the monsoon does not reach this way. [S1]

> **Leave the Philippines where the data puts it.** Eighth looks like the wrong country to
> build in. The next two pages are about why that reading is wrong, and the argument only
> lands if the rank is shown honestly first.

*Source: INFORM Risk Index, Mid 2026 (workflow 515), indicator HA.NAT.FL — European
Commission, Joint Research Centre. Scope: national, ASEAN-10.*

---

## P3 — Hazard is not the differentiator; coping capacity is

`ASEAN` · Chart: **bubble** — hazard × coping capacity, sized by INFORM Risk

> ## Hazard and capacity are independent.
> ### Where they diverge, a flood becomes a disaster.

- The x-axis is what the weather does. The y-axis is what happens next — **higher means
  weaker** capacity to respond.
- Quadrant lines are drawn at the **ASEAN medians**, not at round numbers: flood hazard
  **8.3**, lack of coping capacity **3.9**. Both ship as columns in the dataset, so the
  lines come from the data. [S14]
- The legend shows **three** quadrants, not four. **No ASEAN state combines high flood
  hazard with strong coping capacity.** That empty quadrant is a real property of the
  region, not a rendering fault.

*Source: INFORM Risk Index, Mid 2026 — EC JRC. Medians derived; see `scripts/build_asean_inform.py`.*

---

## P4 — The Philippines at the sharp end

`PHILIPPINES` · Chart: **diverging bar** — gap vs ASEAN median, five dimensions

> ## 8th for river floods. 1st for hazard exposure.
> ### The index is measuring the wrong thing.

Against the ASEAN median, the Philippines scores: [S13]

- **−1.6** on river flood hazard — **rank 8 of 10**
- **+2.25** on all-hazard Hazard & Exposure — **rank 1 of 10**
- **+1.1** on composite INFORM Risk (5.3) — **rank 3 of 10**

> **This inversion is the problem statement.** Philippine flooding is *compound* —
> typhoon-driven, and in Zambales lahar-amplified — so a single-hazard river-flood index
> systematically under-counts it. If regional indices score the hazard Zambales faces too
> low, local sensing and community verification are not a convenience. They are the only
> instruments that measure it directly.

**Stat band — August 2026, national scope:** **8.1 million** people affected across
**10 regions** · **PHP 3.4 billion** infrastructure damage · **PHP 689 million** agriculture
damage · **437** road sections and **27** bridges affected. [S8, S9, S10]

> ⚠ **Label these as national.** They are national totals. Presenting the agriculture figure
> as one city's flood damage is exactly the error removed from the first draft of this deck.

*Sources: INFORM Risk Index Mid 2026 — EC JRC · NDRRMC situational reports, August 2026.
Scope: Philippines, national.*

---

## P5 — The Pivot

`ZAMBALES` · **No chart.** The restraint is the point — this is the only page in the deck
permitted to hold no data.

Full-bleed river aerial, low opacity. One icon. Two lines, centred:

> *There is an opportunity to give every flood-prone community in Zambales the same warning
> a scientist would have — hours before the water arrives.*

> One way to do this is via a **predictive**, **community-connected** early-warning system.

---

## P6 — Olongapo: the mechanism, and the proof it was foreseeable

`OLONGAPO` · Chart: **bar** — 12-month rainfall normals, August highlighted

> ## August was already Olongapo's wettest month.
> ### For thirty years running.

- August normal **865.97 mm**, ahead of July's **788.38** and September's **632.31** —
  August leads by **78 mm**. [S4]
- August alone carries **25.6%** of Olongapo's annual rainfall. June–September together
  carry **82.5%** of an annual normal of **3,385.75 mm**. [S19]
- The city's entire flood exposure is compressed into four months, and one of them
  dominates. **That concentration is what makes a seasonal warning system tractable**
  rather than a year-round burden.

**The August 2026 sequence, and the mechanism:** three bridges — Del Rosario, Sta. Rita,
Kalaklan — carry the Olongapo river crossings. **10 Aug: 517 individuals / 165 families
evacuated, 11 barangays affected [S5] → 18 Aug: 1,076 individuals / 336 families
evacuated [S6] → 28–29 Aug: renewed flooding, major roads impassable, erosion in Barangay
Kalaklan [S7].**

> **Three evacuations in one month, on a river whose wettest month has been known for thirty
> years.** Foreseeable is not the same as forecast — and that gap is what the next page is for.

> The highlight on August is **driven by the data**, not hand-picked: the dataset carries a
> `Wettest month` flag, so the emphasis survives a refresh.

*Sources: PAGASA ClimGridPh CliMap v2.0 — Olongapo City municipal monthly normals
(rainfall 2001–2020) · Inquirer and GMA News reporting, August 2026. Scope: Olongapo City.*

---

## P7 — AGOS: the system, and where SAP sits in it

`—` · **Architecture diagram** + one small SAC tile

> ## AGOS: river sensing joined to community-verified alerting.
> ### Knowing that August floods is climatology. It does not tell a household on a Tuesday night whether to leave. Converting a season into hours is the whole job.

**Flow, left to right:**

`EYE` satellite + `PULSE` river sensors → **SAP BTP** integration → **SAP Datasphere**
modelling → **SAP Analytics Cloud** → `VOICE` alerting + `PATH` route status → `FUND`

**The five components:**

| | |
|---|---|
| **EYE** | Sentinel-1 SAR satellite scanning — penetrates monsoon cloud |
| **PULSE** | Non-contact ultrasonic river sensors on the three existing bridges |
| **VOICE** | Three-tier alerts: Watch · Warning · Evacuate Now |
| **PATH** | Barangay-verified road and route status |
| **FUND** | Lahar-sand revenue recycled into operating cost |

> **Scope honestly.** The SAP stack beyond SAC is **proposed architecture** and is labelled
> as such on the diagram. What this entry **demonstrates** is SAC. Claiming a built BTP
> pipeline that does not exist is the kind of overreach that collapses under the first
> finals question.

---

## P8 — PREDICT: rainfall to river level, with lead time

`OLONGAPO` · Chart: **time series** — monthly rainfall normals

> ## From rainfall to river level: converting data into hours.

- **EYE** — Sentinel-1 **SAR** imagery, which sees through monsoon cloud cover. Optical
  satellite is blind exactly when the flood is happening; radar is not.
- **PULSE** — non-contact ultrasonic sensors mounted **above the historical maximum flood
  line** on Del Rosario, Sta. Rita and Kalaklan. **No new civil works at the pilot site.**
- Antecedent rainfall drives a river-stage forecast; the lead-time interval is what the
  next page prices.

> ⚠ **Say this on the page:** the series is **PAGASA 30-year monthly normals**, not one
> season's observations. The year in the date column is nominal. Nobody should read this
> chart as August 2026.

*Source: PAGASA ClimGridPh CliMap v2.0 — Olongapo City. Scope: Olongapo City.*

---

## P9 — DELIVER: VOICE and PATH

`OLONGAPO` · **Alert mockups** + route-status map *(static graphics — see `mockups/`)*

> ## A warning that arrives, on the channel people already have.

**Three severity states, PAGASA-aligned.** Colour never carries the meaning alone — every
state ships with an icon **and** a text label:

| State | Meaning |
|---|---|
| **Watch** | River rising. Prepare. |
| **Warning** | Flooding likely within hours. Move valuables, be ready to leave. |
| **Evacuate Now** | Leave for the evacuation centre immediately. |

**PATH** carries road and route status from barangay-verified officer accounts. Status older
than **2 hours** auto-downgrades to *Unconfirmed — proceed with caution*, so a stale green
road never reads as a safe one.

**Why route status is not optional:** **437** road sections and **27** bridges were affected
nationally in August 2026. [S10] A warning that does not say which way out is still open is
half a warning.

*Source: NDRRMC situational reports, August 2026. Scope: Philippines, national.*

---

## P10 — The lead-time impact model

`ZAMBALES` · Chart: **line** — evacuation completion, reactive vs AGOS

> ## What one hour of warning is worth.

- Under **current reactive warning**, evacuation reaches **30%** at one hour and **79%** at
  two hours.
- With **AGOS lead time**, the same curve reaches **80%** at one hour and **100%** at two.
- The gap is not the technology. It is the head start.

> ### This is a model. Here are its assumptions.
>
> **A1 · sourced** — anchored to the Olongapo evacuation of 18 Aug 2026: 1,076 individuals
> / 336 families. [S6]
> **A2 · sourced** — current warning is reactive: the alert is issued when the river reaches
> evacuation level *at the bridge*. [S5–S7]
> **A3 · estimate** — **AGOS gives 2 hours of lead time**, from upstream sensor threshold to
> downstream evacuation level. *Team to validate against Bucao-to-Olongapo channel travel time.*
> **A4 · estimate** — evacuation completion follows an S-curve; households move faster once
> neighbours do.
>
> **A3 is the number a judge is most likely to challenge. Say it is an estimate before they
> ask.** A transparent model is credible; a confident number with hidden assumptions is not.

*Source: modelled in this project. Assumptions and their status are in
`data/processed/model_assumptions.csv`; the curve regenerates from `scripts/build_models.py`.*

---

## P11 — Who this reaches: the Aeta communities

`ZAMBALES` · Chart: **bar** — communities by access method during the cutoff

> ## Nine of eleven could only be reached by helicopter.

**On 6 September 2026, five days before this storyboard was submitted, 11 Aeta communities
in Botolan, Zambales, totalling 2,519 families, were cut off** by swollen rivers and impassable roads
along the **Bucao River** and two tributaries draining Mount Pinatubo. [S15]

- Relief took **over seven hours**.
- **Nine** communities were reached by Philippine Air Force helicopter. **Two** by
  carabao-drawn cart. [S15]
- Earlier that week a father and his **5-year-old daughter** drowned when their cart was
  swept away crossing to Barangay Palis. [S16]

**This is the same river system AGOS targets.** Not an anecdote borrowed from elsewhere —
the pilot site, this monsoon season, with a named human cost.

**Standing context:** Botolan holds Zambales' largest Aeta population; **16,000 ha** near
Pinatubo was declared Aeta ancestral domain in 2010; the 2009 Bucao dike collapse displaced
over **20,000** people across nine villages. The exposure is structural, not a one-off. [S17, S18]

> ### The design consequence — this is the point of the page
> Because the most exposed users are the least connected, the **solar-powered barangay
> siren is not a fallback. It is the primary channel for the highest-risk population.**

> ⚠ **Do not chart distance.** The source gives one range for the whole group, **25–30 km
> from the town proper**, stored as a midpoint so the file loads. Charting it per barangay
> would invent precision the source does not have. Use it as text.

*Sources: contemporaneous news reporting, 6–7 September 2026 [S15, S16]; NCIP ancestral
domain declaration 2010 [S17]; Bucao dike collapse, August 2009 [S18]. Scope: Botolan, Zambales.*

---

## P12 — Failure and mitigation

`—` · Chart: **heat map** — risk score over likelihood × impact

> ## What breaks, and what we do about it.

Ten identified risks, scored 1–5 on likelihood and impact. The two worst, both scoring
**20**, are communications failures rather than sensor failures:

| Risk | Score | Mitigation |
|---|---|---|
| Cellular signal lost during the storm | **20** | Dual uplink — LoRaWAN mesh between sensors as primary, cellular as backup |
| Power or cell outage cuts off the highest-risk households | **20** | Solar-charged barangay siren on the same PULSE threshold; no phone required |
| Sensor destroyed or swept away | **16** | Non-contact sensors above historical max; replacement budgeted as a consumable, not capex |
| Alert fatigue erodes trust after false alarms | **16** | Three-tier language instead of binary alerting |
| Monsoon cloud blocks optical imagery | **15** | Sentinel-1 SAR penetrates cloud; primary feed during active monsoon |
| Crowd-sourced road status goes stale | **12** | Status older than 2 hours auto-downgrades to *Unconfirmed* |
| Lahar-sand revenue fluctuates with demand | **12** | Reserve-fund structure — bank surplus quarters against lean ones |
| LGU turnover ends sponsorship mid-rollout | **12** | MOU at provincial PDRRMO level, not city administration alone |

> Most entries present a frictionless solution. Naming the failure modes — and showing that
> the two worst are already designed around — is worth more than claiming there aren't any.

*Source: qualitative assessment by the team (assumption A10, `model_assumptions.csv`).
Likelihood and impact are scored, not measured, and the page says so.*

---

## P13 — Business model: B2B2G

`—` · Chart: **bar** — lahar dredged vs remaining

> ## Funded by the sand the floods leave behind.

- Mount Pinatubo left **4.7 billion m³** of lahar in the Zambales river systems — Bucao
  **3.0 bn (63.8%)**, Santo Tomas **1.6 bn (34.0%)**. [S20]
- **50 million m³** has been dredged. That is **1.06% in 35 years.** [S21]
- The Zambales River Restoration Program has only been running since 2023, and only river
  deltas have been cleared.

> **At the current rate the backlog is permanent.** That is the strongest available argument
> that the constraint is **financing cadence, not engineering** — and therefore that a
> self-funding loop is the right intervention, not a larger one-off budget request.

**Four revenue streams:** hardware sales · platform subscription · anonymised data-insights
licensing · grant and development finance.

**The FUND loop:** lahar-sand dredging revenue is recycled into system operating cost,
structured as a **reserve fund** — banking surplus in high-demand construction quarters
against lean ones — rather than passed straight through.

> 🔒 **Two figures are deliberately missing from this page:** the lahar-sand sale price per
> m³ (Provincial Treasurer's Office) and the sensor, installation and subscription costs
> (vendor quotes). Until those exist there is no revenue projection here. A fabricated one
> is the same failure as the misattributed figures cut from the first draft, and it would
> not survive the first Viability question.

*Source: MGB Central Luzon lahar volume estimates; Zambales River Restoration Program.
Scope: Zambales province.*

---

## P14 — Roadmap and KPIs

`—` · Chart: **bar** — phases by end month

> ## Twenty-four months, four phases, one monsoon to prove it.

| Phase | Months | What happens |
|---|---|---|
| **1 · Engagement & Planning** | 1–3 | Co-design with Olongapo LGU and Botolan barangays; MOU at provincial PDRRMO level |
| **2 · Deployment & Set-up** | 4–9 | Sensors on the three bridges; barangay officer accounts; SAC dashboards live |
| **3 · Operation & Monsoon Stress Test** | 10–15 | First full monsoon under AGOS — the phase that either proves this or doesn't |
| **4 · Scaling & Reporting** | 16–24 | Expand to Region III; annual Flood Resilience report; ADInet feed |

**KPIs, each with a baseline — a KPI without one is not measurable:**

- Sensor uptime in monsoon season *(baseline: 0 — no sensors exist)*
- Alert lead time in minutes *(baseline: 0 — warning currently begins at visible flooding)*
- Barangays with an active PATH officer account *(baseline: 0)*
- Lahar volume dredged per quarter *(baseline: 1.06% removed in 35 years)*
- LGU subscription renewal rate *(baseline: n/a — first cycle)*

> 🔒 **Targets are blank on purpose.** Those are the team's numbers to commit to, and a
> target invented to fill a column is worse than an empty one.

**Named institutional partners:** AHA Centre / ADInet · ACDM · NDRRMC-OCD · DELSA-JAIF ·
World Bank / ADB · DENR-MGB · DPWH · PAGASA.

*Source: programme design by the team. Phase boundaries are planning assumptions.*

---

## P15 — Scaling across ASEAN

`ASEAN` · Chart: **bubble** — the P3 quadrant, with deployment priority overlaid

> ## The countries that need this most are the ones we can reach next.

- The weak-capacity corner names its own targets: **Myanmar 5.6**, **Lao PDR 5.6**,
  **Cambodia 5.5** on lack of coping capacity — all three also above the ASEAN median for
  river flood hazard. [S1]
- Same monsoon, same river-basin geometry, same gap between hazard and the ability to
  respond to it.

**The closing move:** push Zambales data into the **AHA Centre's ADInet**, so a Zambales
flood appears in ASEAN's own regional situational-awareness feed rather than only in a
national one.

> The deck opened at ASEAN scale and closes there — having earned the generalisation
> rather than assumed it.

*Source: INFORM Risk Index Mid 2026 — EC JRC. Scope: national, ASEAN-10.*

---

## References — does not count against the 15-page cap

Generate with `python scripts/build_references.py`, which reads `docs/SOURCES.md` and writes
`docs/REFERENCES.md`. Regenerate it **after** any figure changes, so the page can never
drift out of sync with the numbers actually used.

---

## Before you export

- [ ] **≤ 15 pages** including cover, excluding references
- [ ] **Landscape**, PDF, **≤ 20 MB**, each image **≤ 2 MB**
- [ ] Filename **`PHILIPPINES_NAIVE BAIS.pdf`**
- [ ] Cover carries all six required elements
- [ ] Every chart legible at 100% **and** in print
- [ ] Every scope tag present — this is the one that stops a national figure reading as local
- [ ] Every number traces to a row in `SOURCES.md`
- [ ] Read it end to end, aloud, once
