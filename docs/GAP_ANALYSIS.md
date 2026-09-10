# AGOS — Gap Analysis of the v1 Master Plan

**Date:** 2026-09-10
**Reviewed artifact:** `AGOS_Storyboard_Master_Plan.md` (v1)
**Verdict:** Strong narrative instincts, structurally unsubmittable. Two fatal flaws, four serious, three missed opportunities.

This document records *what was wrong and why*, so the reasoning behind v2 is auditable. The corrected plan is `AGOS_Storyboard_Plan_v2.md`.

---

## F1 — FATAL: The plan is ~2.5× over the hard page limit

**Rule (verified):** ASEAN DSE storyboards are capped at **15 pages including the Cover Page, excluding References**, PDF, landscape, ≤20 MB, images ≤2 MB each.
Source: <https://aseandse.org/data-analytics-storyboard-requirement/>

**v1 specified:** 12 pages for Parts 1–2, plus a components hub, 5 feature deep-dives, and ~6 business-model pages ≈ **33–37 pages**.

**Root cause.** v1 reverse-engineered Team Sharksfin's **79-page deck**. A 79-page artifact cannot be an ADSE storyboard — the cap has been 15 pages. That deck is almost certainly Sharksfin's **National/Regional Finals presentation**, which is a *separate, later* deliverable governed by different rules. v1 copied the mechanics of the wrong artifact.

**Consequence if unfixed:** disqualification or forced amputation at submission time.

**Fix:** rebuild to a 15-page budget (see F2 for how the budget is allocated). The discarded material is not wasted — it is re-homed into the Finals deck backlog (`docs/FINALS_DECK_BACKLOG.md`), which is where it always belonged.

---

## F2 — FATAL: Page budget is inverted against the scoring rubric

**Rule (verified):** <https://aseandse.org/judging-criteria/>

| Criterion | Weight | What it actually rewards | v1 page spend |
|---|---|---|---|
| Problem Definition | **10%** | Clear socio-economic issue, SDG + ASEAN priority alignment, regional specificity | **~10 pages** |
| **Analysis & Insights** | **25%** | Data storytelling logic/flow, **visualisation quality, effective use of charts and SAC tools**, source credibility | ~5 charts |
| Relevancy & Impact | **20%** | Scale of change, **replicability across ASEAN member states**, **underrepresented communities** | folded into feature slides |
| Viability | **15%** | Real-world feasibility, stakeholder roles, realistic roadmap | ~4 pages |
| Innovation | **15%** | Originality, root-cause thinking, future resilience, **AI and digital technology integration** | thin / implicit |
| *(Presentation Delivery)* | *15%* | *Finals stage only* | n/a |

v1 spent roughly **two-thirds of the budget on the 10% criterion.** Analysis & Insights is worth **2.5× Problem Definition** and is the single largest line item.

**Compounding error:** several v1 pages carry **no SAC chart at all** — the CTA pivot page (deliberately empty), the Components-vs-Features hub, the win-win-win table, the roadmap table, the partnership table. Under a 15-page cap where 25% of the score is chart quality and SAC tool use, a chartless page is close to a wasted page.

**Fix:** allocate pages in proportion to weight, and impose a hard rule — **every page except the cover and the pivot must carry a SAC-generated visual.** Tables become SAC tables; roadmaps become SAC Gantt/time-series; the win-win-win becomes a SAC comparison chart.

---

## S1 — SERIOUS: Headline figures are misattributed

"Data source credibility" is scored inside the 25% criterion. Three of v1's most prominent numbers do not survive checking.

| v1 claim | What the sources actually say | Status |
|---|---|---|
| "**PHP 690M** in damage" (presented as Olongapo/Zambales flood damage) | **PHP 689M** is the estimated **national agriculture** damage from the August 2026 cyclones + habagat across 10 regions. Infrastructure damage nationally was PHP 3.4B. | **Misattributed by ~3 orders of scope.** Nationwide agriculture figure relabelled as one city's total damage. |
| "**8.4M** people / **2.4M** families affected" | **8.1M people** affected across 10 regions (Philstar, 30 Aug 2026), from TCs Luis, Maymay, Neneng **and** habagat combined. Earlier NDRRMC counts: 3.65M people / 1.06M families, rising to ~5M / 1.43M. | **Inflated and mismatched.** The people/family ratio in v1 is internally inconsistent with every NDRRMC report. |
| Escalation ladder "**172 → 534 → 2,876 → 17,317**" evacuated, presented at Olongapo scale | Olongapo-level reporting gives **517 evacuated (10 Aug, 165 families)** and **1,076 individuals / 336 families (18 Aug)**. No Olongapo source produces 17,317. | **Unverifiable at the stated scope.** May be province- or region-wide; cannot be presented as Olongapo's without a citation. |

**Root cause:** figures were carried over from an earlier working session without a citation register, so scope labels drifted from their sources.

**Fix:** a mandatory citation register (`docs/SOURCES.md`). **No number enters the storyboard without a row in that register naming source, publication date, geographic scope, and retrieval date.** Every CSV in `data/` gets a matching `.source.md` sidecar.

---

## S2 — SERIOUS: The required datasets do not exist

v1's SAC build notes depend on four files. Only one exists.

| File | Status |
|---|---|
| `Olongapo_City_municipal_monthly.csv` | **EXISTS** — PAGASA/ClimGridPh CliMap v2.0, now in repo. Verified: 12 rows, rainfall + temp normals. |
| `zambales_flood_history_multiyear.csv` | **MISSING** — not in repo or anywhere on the machine |
| `zambales_lahar_share.csv` | **MISSING** |
| `zambales_evacuation_escalation.csv` | **MISSING** |

**Fix:** rebuild all three from primary sources with full citation, per the approved data strategy. Primary sources identified and confirmed reachable:
- **INFORM Risk Mid 2026** (JRC European Commission) — live REST API, workflow `515`, all 10 ASEAN states, multi-dimensional. Confirmed working.
- **NDRRMC Monitoring Dashboard** situational reports for the SW monsoon
- **AHA Centre** weekly disaster updates / ADInet
- **PAGASA ClimGridPh CliMap v2.0** — already in hand
- Contemporaneous **Inquirer / GMA / PNA / Philstar** reporting for city-level evacuation counts

---

## S3 — SERIOUS: The ASEAN framing is contradicted by the best available data

v1 planned a bar chart implying Philippine flood exceptionalism, then a line reading *"flood exposure is not a Philippine problem. It is an ASEAN condition."*

**Retrieved data (INFORM Risk Mid 2026, river flood hazard & exposure, 0–10):**

| Country | Flood | Hazard & Exposure | Vulnerability | Lack of Coping Capacity | INFORM Risk |
|---|---|---|---|---|---|
| Viet Nam | 9.9 | 5.2 | 2.6 | 4.3 | 3.9 |
| Thailand | 9.8 | 7.4 | 4.1 | 3.9 | 4.9 |
| Myanmar | 8.8 | 8.3 | 6.6 | 5.6 | 6.7 |
| Cambodia | 8.6 | 6.9 | 6.0 | 5.5 | 6.1 |
| Indonesia | 8.4 | 8.0 | 3.0 | 3.9 | 4.5 |
| Lao PDR | 8.2 | 2.6 | 3.4 | 5.6 | 3.7 |
| Malaysia | 6.8 | 3.0 | 3.4 | 3.2 | 3.2 |
| **Philippines** | **6.7** | **8.3** | **4.7** | **3.8** | **5.3** |
| Brunei Darussalam | 4.7 | 1.5 | 2.9 | 2.8 | 2.3 |
| Singapore | 0.0 | 0.7 | 0.5 | 0.8 | 0.7 |

**The Philippines ranks 8th of 10 on river flood hazard.** A chart built to imply Philippine exceptionalism would be *refuted by its own axis* — the worst possible outcome on a credibility-scored criterion.

**This is a gift, not a problem.** The data proves v1's own thesis line *literally*: six ASEAN states score ≥8.0. Flood exposure genuinely **is** an ASEAN condition. And the Philippines' real distinction is visible in a different column — **overall Hazard & Exposure 8.3, tied highest in ASEAN with Myanmar; INFORM Risk 5.3, second highest.**

**Fix:** replace the single-bar "who's worst" chart with a **two-axis analysis** (flood hazard × lack of coping capacity). This is a stronger analytical move, it is honest, and it hands the solution its replication argument for free: the countries where hazard is high *and* coping capacity is weakest (Myanmar 5.6, Lao PDR 5.6, Cambodia 5.5) are precisely where a low-cost early-warning system transfers best. That argument is worth points under Relevancy & Impact (20%, "replication across ASEAN member states").

---

## S4 — SERIOUS: SAP stack claimed at the wrong altitude

v1 maps AGOS onto SAP Build Apps → BTP → Datasphere → SAC. The architecture is plausible, but **the competition's storyboard criterion rewards "effective use of charts and SAC tools" — the tool the team actually uses — not the breadth of SAP products named in a diagram.** A four-product architecture diagram scores under Viability/Innovation at best; it earns nothing under the 25% criterion.

**Fix:** keep the architecture diagram (one page, it does real Viability work), but make the *demonstrated* SAC capability visible in the charts themselves. Concretely, use SAC features that show fluency rather than a bar chart anyone could draw in Excel: calculated measures, a forecast/predictive layer, geo-map visualisation, variance/threshold formatting, and linked-dimension filtering. Named-but-unbuilt SAP products are a claim; a SAC forecast chart is evidence.

---

## M1 — MISSED: No affected population is ever named

Relevancy & Impact (20%) explicitly scores **"consideration of underrepresented communities."** v1 names DENR-MGB, DPWH, PAGASA, SBMA, treasurers, and barangay captains — every *institution* — and not one affected community.

The Zambales lahar story has an obvious and real protagonist that v1 omits entirely: the **Aeta indigenous communities** displaced by the 1991 Pinatubo eruption, whose resettlement areas sit in and beside the lahar channels of the Bucao and Santo Tomas river systems. They are simultaneously the most exposed, the least connected (lowest mobile/SMS coverage), and the least represented in formal DRRM planning.

**Fix:** promote them to a named beneficiary with a dedicated analytical page, and let it drive a design consequence — the zero-connectivity fallback (solar siren/beacon) stops being a nice-to-have footnote and becomes the *reason* the system reaches its most vulnerable users. Design justified by an equity finding scores far better than design justified by completeness.

---

## M2 — MISSED: Innovation is under-claimed

Innovation (15%) explicitly rewards **"integration of AI and digital technologies."** v1 says "predictive" repeatedly but never names a method, so a judge cannot award the points.

**Fix:** name the technique and show it. A rainfall→river-level lead-time model, surfaced as a **SAC predictive forecast** on a time series, converts an unscoreable adjective into visible, scoreable evidence. Add the SAR (Sentinel-1) cloud-penetration point from v1 §3.4 — it is a genuinely sophisticated detail already in the plan but buried in a mitigation bullet.

---

## M3 — MISSED: The strongest single insight is buried on page 9

v1's best line is that PAGASA's own 30-year normals already show **August as Olongapo's wettest month at 865.97 mm** — before the 2026 record year. *(Verified against the ClimGridPh file: Aug 865.97 mm vs. Jul 788.38, Sep 632.31; the wettest month by a 78 mm margin.)*

That is the "the data already told us this was coming" moment, and it is the cleanest available proof that the problem is *predictable* — which is the entire premise of the solution. In v1 it appears on slide 9 of 12, after the reader's attention is spent.

**Fix:** move it into the problem section's climax position, where it functions as the hinge between "this happened" and "this was foreseeable, therefore preventable."

---

## Retained from v1 without change

Not everything needs fixing. These are v1's genuine strengths and v2 keeps them:

- The **deductive scope ladder** (ASEAN → Philippines → Zambales → Olongapo) with persistent scope tags — legible, judge-friendly, keeps a compressed deck oriented
- The **Failure & Mitigation layer** — a real differentiator; most student entries present solutions as frictionless, and this one pre-empts the hardest judge question
- **Naming ASEAN institutions specifically** (AHA Centre, ACDM, ADInet, DELSA/JAIF) rather than "regional partners"
- The **self-funding lahar-sand revenue loop** — the most original idea in the plan and the strongest Viability asset
- **PAGASA colour-convention reuse** for alert severity — sharp human-factors reasoning
- The **B2B2G** correction over Sharksfin's B2B2C
- **SDG 11 + 13** — both confirmed eligible under ADSE's six permitted SDGs
