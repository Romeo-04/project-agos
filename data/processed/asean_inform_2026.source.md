# Source — ASEAN-10 INFORM Risk datasets

Covers `asean_flood_inform2026.csv`, `asean_inform_multidim_2026.csv`,
and `ph_vs_asean_dimensions.csv`.

- **Provider:** European Commission, Joint Research Centre (JRC) — Disaster Risk Management Knowledge Centre
- **Product:** INFORM Risk, **Mid 2026** release
- **Access:** public REST API, `https://drmkc.jrc.ec.europa.eu/inform-index/API/InformAPI`, workflow `515`
- **Indicators:** `HA.NAT.FL` (river flood hazard & exposure), `HA` (Hazard & Exposure dimension), `VU` (Vulnerability), `CC` (Lack of Coping Capacity), `INFORM` (composite Risk)
- **Scale:** all indicators 0–10; **higher is worse on every one, including coping capacity**
- **Scope:** national, all 10 ASEAN member states
- **Retrieved:** 2026-09-10
- **Reproduce:** `python scripts/build_asean_inform.py` (raw API responses land in `data/raw/inform_2026/`)

## Key findings

- **Six of ten** ASEAN states score ≥8.0 on river flood hazard: Viet Nam 9.9, Thailand 9.8,
  Myanmar 8.8, Cambodia 8.6, Indonesia 8.4, Lao PDR 8.2.
- **Philippines ranks 8th of 10** on river flood hazard (6.7) — below the ASEAN median of 8.3.
- **But 1st of 10 on all-hazard Hazard & Exposure** (8.3, tied with Myanmar; ASEAN median 6.05),
  and **3rd on composite INFORM Risk** (5.3, after Myanmar 6.7 and Cambodia 6.1).
- **Weakest coping capacity in ASEAN:** Myanmar 5.6, Lao PDR 5.6, Cambodia 5.5 — the
  scaling targets identified on P15.

## Interpretation note

The river-flood/all-hazard inversion is the analytical spine of pages P3–P4. It is a real
property of the index, not an artifact: INFORM's `HA.NAT.FL` measures *riverine* flood
exposure only, so it does not capture typhoon-driven or lahar-amplified flooding. The
storyboard states this openly rather than selecting the flattering measure.

## Caveats

- Quadrant assignment in `asean_inform_multidim_2026.csv` uses **ASEAN medians**, not global
  or absolute thresholds. Medians are carried as columns so the split is reproducible.
- The 8.0 reference line on P2 is a *severity* annotation and is deliberately different from
  the 8.3 median used for P3's quadrant split. Both are labelled on their respective pages.
- Singapore scores 0.0 on river flood hazard — a true index value reflecting no significant
  riverine system, not missing data.
