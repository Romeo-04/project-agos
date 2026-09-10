# Source — MODELLED datasets (P10, P12, P13, P14)

Covers `leadtime_scenarios.csv`, `risk_matrix.csv`, `roadmap_phases.csv`,
and `model_assumptions.csv`.

**These are not measurements.** Every other dataset in this repository is an observation
with a citation. These four are models built on stated assumptions, and the storyboard
prints those assumptions on the page.

- **Built by:** `scripts/build_models.py`
- **Assumption register:** `model_assumptions.csv` — 10 assumptions, each tagged
  `SOURCED`, `ESTIMATE`, or `UNSOURCED - BLOCKING`
- **Date:** 2026-09-10

## Why the assumptions ship as data

A transparent model with visible assumptions is credible; a confident number with hidden
ones is not. Carrying the assumptions in a CSV rather than in prose means they cannot be
lost between this repo and the chart, and P10/P13 can render them directly onto the page.

## Status

| Status | Count | Meaning |
|---|---|---|
| `SOURCED` | 4 | Traceable to a row in `SOURCES.md` |
| `ESTIMATE` | 4 | Reasoned assumption, owned by the team, printed on the page |
| `UNSOURCED - BLOCKING` | **2** | **P13 cannot ship until these have real values** |

### The two blocking items

- **A7 — lahar-sand sale price per m³.** Needs a figure from the Zambales Provincial
  Treasurer's Office. Without it the FUND revenue loop is decorative.
- **A8 — sensor unit cost, installation cost, annual platform subscription per LGU.**
  Needs vendor quotes.

**No placeholder pricing has been invented for these.** Fabricating a revenue projection
would be the same failure mode as v1's misattributed figures, and it would collapse under
the first Viability question at finals.

## Per-dataset notes

**`leadtime_scenarios.csv` (P10)** — cumulative % of at-risk households evacuated against
minutes from first alert, for two scenarios. Both series share one x-axis and one y-unit,
so this charts on a **single axis**. The 2-hour AGOS lead time (A3) is an estimate the team
must validate against actual Bucao-to-Olongapo channel travel time; it is the number a judge
is most likely to challenge.

**`risk_matrix.csv` (P12)** — v1's failure/mitigation content, scored 1–5 on likelihood and
impact so it renders as a SAC heat map instead of a table. Scores are qualitative team
judgement (A10), not measured frequencies. `RiskScore` is likelihood × impact.

**`roadmap_phases.csv` (P14)** — four phases over 24 months, carried from v1 §4.4.
**`KpiTarget` is deliberately empty.** Baselines are real where one exists (notably
`1.06% in 35 years` for dredging, from S21); targets are the team's call and must not be
invented here. A KPI without a baseline is not measurable — a target without a team
decision is not a commitment.
