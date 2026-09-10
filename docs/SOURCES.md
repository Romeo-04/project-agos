# AGOS — Citation Register

**Rule: no number enters the storyboard without a row in this table.**
Source credibility is scored inside ADSE's 25% Analysis & Insights criterion. v1 lost three headline figures to scope drift because there was no register; this file is the fix.

Each row records: the figure, its **exact geographic scope**, the source, publication date, and retrieval date. Scope is mandatory — the v1 failures were all scope mislabels, not fabrications.

---

## Verified — cleared for use

| # | Figure | Scope | Source | Published | Retrieved |
|---|---|---|---|---|---|
| S1 | River flood hazard & exposure, all 10 ASEAN states (0–10): VNM 9.9 · THA 9.8 · MMR 8.8 · KHM 8.6 · IDN 8.4 · LAO 8.2 · MYS 6.8 · **PHL 6.7** · BRN 4.7 · SGP 0.0 | ASEAN-10, national | INFORM Risk Mid 2026, EC Joint Research Centre — API workflow `515`, indicator `HA.NAT.FL` | 2026 | 2026-09-10 |
| S2 | INFORM dimensions, ASEAN-10 — Hazard & Exposure, Vulnerability, Lack of Coping Capacity, Risk. **PHL: HA 8.3 (tied highest w/ MMR) · VU 4.7 · CC 3.8 · RISK 5.3 (3rd highest, after MMR 6.7 and KHM 6.1)** | ASEAN-10, national | INFORM Risk Mid 2026 — workflow `515`, indicators `HA`, `VU`, `CC`, `INFORM` | 2026 | 2026-09-10 |
| S3 | Lack of coping capacity, highest in ASEAN: MMR 5.6 · LAO 5.6 · KHM 5.5 | ASEAN-10, national | INFORM Risk Mid 2026 — indicator `CC` | 2026 | 2026-09-10 |
| S4 | Olongapo monthly rainfall normals — **August 865.97 mm (wettest month)**, July 788.38, September 632.31, June 506.80 | **Olongapo City, municipal** | PAGASA ClimGridPh CliMap v2.0, municipal climate normals (rainfall 2001–2020; temperature 1991–2020) | — | file in hand, verified 2026-09-10 |
| S19 | **August alone is 25.6% of Olongapo's annual rainfall**; **June–September together are 82.5%**; annual normal total 3,385.75 mm; August leads July by **77.59 mm** | **Olongapo City, municipal** | Derived from S4 — `scripts/build_olongapo.py` | — | 2026-09-10 |
| S20 | **4.7 billion m³** of Pinatubo lahar deposited in Zambales river systems — **Bucao 3.0 bn m³ (63.8%)**, **Santo Tomas 1.6 bn m³ (34.0%)** | **Zambales province** | MGB Central Luzon, via Daily Tribune / BusinessMirror | 2025-08-27 / 2026-08-12 | 2026-09-10 |
| S21 | **Only 50 million m³ dredged** of the 4.7 bn m³ — **1.06% removed** in 35 years. Zambales River Restoration Program running since **2023**; river deltas cleared only | **Zambales province** | MGB Central Luzon, via Daily Tribune / BusinessMirror | 2025-08-27 / 2026-08-12 | 2026-09-10 |
| S22 | Barangays under lahar threat: **6 from Bucao overflow** (San Juan, Paudpod, Carael, Bangan, Capayawan, Batonlapoc — all Botolan); **15 across three towns from Santo Tomas** (San Marcelino, San Felipe, San Narciso) | **Zambales province** | BusinessMirror | 2026-08-12 | 2026-09-10 |
| S23 | Zambales evacuees as of 12 Aug 2026: **7,044 individuals / 2,441 families** — 4,706 persons (1,621 families) in evacuation centres, 285 individuals (102 families) with relatives | **Zambales province** | BusinessMirror | 2026-08-12 | 2026-09-10 |
| S5 | 517 individuals / 165 families evacuated; river overflowed beneath Del Rosario, Sta. Rita and Kalaklan bridges; 11 barangays affected | **Olongapo City** | Inquirer / GMA News | 2026-08-10 | 2026-09-10 |
| S6 | 1,076 individuals / 336 families evacuated | **Olongapo City** | Inquirer | 2026-08-18 | 2026-09-10 |
| S7 | Widespread flooding and soil erosion; major roads impassable; riverside barangay evacuated; erosion in Barangay Kalaklan | **Olongapo City** | Inquirer | 2026-08-28/29 | 2026-09-10 |
| S8 | **8.1 million people affected across 10 regions** — TCs Luis, Maymay, Neneng + enhanced southwest monsoon combined | **Philippines, national** | NDRRMC via Philstar | 2026-08-30 | 2026-09-10 |
| S9 | Infrastructure damage **PHP 3.4 B**; agriculture damage **PHP 689 M** | **Philippines, national** | NDRRMC | Aug 2026 | 2026-09-10 |
| S10 | **437 road sections and 27 bridges** affected by floods, landslides and related incidents | **Philippines, national** | NDRRMC | Aug 2026 | 2026-09-10 |
| S11 | ~3,200 houses damaged (355 destroyed, ~2,800 partially) | **Philippines, national** | NDRRMC | Aug 2026 | 2026-09-10 |
| S13 | **Philippines vs. ASEAN median (gap):** river flood hazard −1.6 (rank 8/10) · all-hazard Hazard & Exposure +2.25 (rank **1/10**, tied MMR) · Vulnerability +1.3 (rank 3) · Lack of coping capacity −0.1 (rank 7) · INFORM Risk +1.1 (rank 3) | ASEAN-10, national | INFORM Risk Mid 2026 — derived, `scripts/build_asean_inform.py` | 2026 | 2026-09-10 |
| S14 | ASEAN medians used for P3 quadrant lines: river flood hazard **8.3**, lack of coping capacity **3.9** | ASEAN-10, national | INFORM Risk Mid 2026 — derived | 2026 | 2026-09-10 |
| S15 | **11 Aeta communities cut off** in Botolan (brgys Villar, Moraza, Belbel, Burgos, Nacolcol, Palis, Maguisguis, Cabatuan, Owaog Nebloc, Malomboy, Poonbato); **2,519 families** affected; 4,564 food packs; **9 reached by helicopter, 2 by carabao cart**; relief took >7 hrs; 25–30 km from town proper | **Botolan, Zambales** | Inquirer, "11 Aeta communities get food aid as swollen rivers cut off access" | **2026-09-07** | 2026-09-10 |
| S16 | A father and his 5-year-old daughter drowned when their cart was swept away crossing to Barangay Palis | **Botolan, Zambales** | Inquirer | 2026-09-07 | 2026-09-10 |
| S17 | Botolan is Zambales' largest town and holds the province's largest Aeta population; 16,000 ha (160 km²) near Pinatubo declared Aeta ancestral domain by NCIP in 2010 | **Botolan, Zambales** | Inquirer / NCIP | 2010 / ongoing | 2026-09-10 |
| S18 | Bucao River dike collapse (Typhoon Kiko, Aug 2009) flooded Botolan and 10 villages; further breach two months later raised lahar and floodwater >1.5 m, **displacing over 20,000 people across 9 villages** | **Botolan, Zambales** | Global Volcanism Program / ReliefWeb | 2011 | 2026-09-10 |
| S12 | Earlier NDRRMC counts in the same episode: 3.65 M people / 1.06 M families, rising to ~5 M / 1.43 M, across 10 regions | **Philippines, national** | NDRRMC | Aug 2026 | 2026-09-10 |

## Competition rules — verified

| # | Rule | Source | Retrieved |
|---|---|---|---|
| R1 | Storyboard ≤15 pages incl. cover, excl. references; PDF; landscape; ≤20 MB; images ≤2 MB; filename `COUNTRY_TEAM NAME`; charts generated by SAC | <https://aseandse.org/data-analytics-storyboard-requirement/> | 2026-09-10 |
| R2 | Judging: Problem Definition 10% · Analysis & Insights 25% · Relevancy & Impact 20% · Viability 15% · Innovation 15% · Presentation Delivery 15% (finals) | <https://aseandse.org/judging-criteria/> | 2026-09-10 |
| R3 | Eligible SDGs: 2, 3, 6, 11, 12, 13 — **SDG 11 and 13 both eligible** | <https://aseandse.org/thecompetition/> | 2026-09-10 |

---

## Rejected — do not use

Figures from v1 that failed verification. Recorded so they are not reintroduced.

| v1 figure | Problem | Correct figure |
|---|---|---|
| "PHP 690 M damage" attributed to Olongapo/Zambales flooding | **Scope misattribution.** PHP 689 M is *national agriculture* damage across 10 regions | S9 — label as national agriculture |
| "8.4 M people / 2.4 M families affected" | Inflated; the people-per-family ratio is inconsistent with every NDRRMC report | S8 / S12 |
| Escalation ladder "172 → 534 → 2,876 → **17,317**" at Olongapo scale | **Unverifiable at stated scope.** No Olongapo source produces 17,317; may be province- or region-wide | S5–S7 for Olongapo-scale counts |
| "2018 → 2023 → 2026: 5,520 → 10,544 → 17,317 evacuated" | No source located | pending — omit unless sourced |

---

## Outstanding — required before the pages that use them

| # | Needed for | Status |
|---|---|---|
| N1 | Aeta community exposure + connectivity (P11) | **RESOLVED** — see S15–S18 |
| N2 | Zambales lahar volume; dredging baseline (P13, P14) | **RESOLVED** — S20–S21. v1's "~1% removed since 2020" was directionally right but wrong on timeframe: it is **1.06% removed since 1991**, and the dredging programme only began in 2023. |
| N3 | Zambales province-wide evacuation totals, Aug 2026 | **PARTIALLY RESOLVED** — S23 gives 7,044 individuals / 2,441 families at 12 Aug 2026, province-wide. Still does not reconcile with v1's 17,317; that figure remains unsourced and stays rejected. |
| N4 | Barangay-level mobile/SMS coverage, Zambales (P11) | still open — S15 gives *physical* access as a usable proxy if coverage data is not found |
| N5 | AHA Centre ADInet submission process (P15) | to research |
| N6 | Sentinel-1 SAR revisit frequency over Luzon (P8) | to verify |
