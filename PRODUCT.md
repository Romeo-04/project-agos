# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Plain static HTML/CSS in single self-contained files, no build step and no dependencies.
Established by the existing codebase (`mockups/agos-screens.html`,
`mockups/agos-architecture.html`), not a fresh decision. Each file must open from disk in a
browser with nothing missing, because the files are handed to teammates and screenshotted
for a PDF rather than deployed.

Design tokens are duplicated into each file rather than imported, deliberately, for the same
reason.

## Users

Four, ordered by how much the design owes them.

1. **A resident deciding whether to leave the house.** Possibly at night, possibly in rain,
   possibly on a phone with one bar of signal. Every VOICE alert screen is for this person.
   In Botolan, the most exposed residents are Aeta community members who may have no phone
   signal at all — for them the solar-powered barangay siren is the primary channel, not a
   fallback.
2. **A barangay officer** marking a road impassable while standing in the weather.
3. **An LGU engineer** watching river levels and lahar risk across the city.
4. **A provincial treasurer** checking whether the self-funding loop is working.

## Product Purpose

AGOS is a flood early-warning system for Zambales, Philippines. River sensors and satellite
radar feed a river-stage forecast; the forecast becomes an alert delivered on the channel a
household actually has. Success is a household leaving earlier than it otherwise would have.

The project's modelled claim is that lead time is the variable that matters: under current
reactive warning, evacuation reaches 30% at one hour, against 80% with AGOS lead time.

## Positioning

Regional flood indices under-count Philippine flood risk because Philippine flooding is
*compound* — typhoon-driven, and in Zambales lahar-amplified. Against the ASEAN median the
Philippines scores −1.6 on river flood hazard (rank 8 of 10) yet +2.25 on all-hazard
exposure (rank 1 of 10). **That measurement gap is the product's reason to exist:** if
regional indices cannot see the hazard Zambales faces, local sensing plus community
verification is the only instrument that can.

The funding mechanism is the second differentiator: lahar-sand dredging revenue recycled
into operating cost as a reserve fund. Only 1.06% of the 4.7 bn m³ Pinatubo lahar backlog
has been dredged in 35 years, which argues the constraint is financing cadence rather than
engineering.

## Operating Context

- **Competition deliverable.** ASEAN Data Science Explorers 2026. Team **Naive Bais**,
  FEU – Institute of Technology, Philippines. Members Jhezra A. Tolentino and
  Sean Matthew L. Viacrusis. Submission deadline **2026-09-11, 11:59 PM**.
- The mockups appear as static images inside a 15-page landscape PDF storyboard
  (pages P9 and P13), and — confirmed by the user — must **also** work as a clickable
  prototype for the national finals, which permit an app prototype.
- Every analytical chart in the storyboard is built in SAP Analytics Cloud. The mockups are
  interface design, not charts, and the two do not share a palette.
- Pilot site: Olongapo City (three bridges — Del Rosario, Sta. Rita, Kalaklan) and Botolan,
  Zambales (Bucao River).

## Capabilities and Constraints

**Five named components.** EYE (Sentinel-1 SAR satellite scanning) · PULSE (non-contact
ultrasonic river sensors) · VOICE (three-tier alerting) · PATH (barangay-verified route
status) · FUND (the self-funding loop).

**Alert copy is English only** — confirmed by the user. Filipino-primary copy was offered
and declined.

**Ten screens exist.** The original seven plus an SMS-only fallback, the solar siren's
physical indicator, and an offline/last-known state. They ship as one file in two modes:
a gallery for screenshotting into the PDF, and a click-through prototype for the finals.

**Hard design constraints, all load-bearing:**

- Severity is never carried by colour alone — colour **and** icon **and** text label.
- The three alert states descend in relative luminance (0.576 → 0.171 → 0.083) so the
  escalation survives greyscale print and colour-blind vision.
- Status colours are reserved for severity and never appear as a chart series or accent.
- Every number shown is one of three things, never a bare invented value: **sourced** and
  cited on the screen; **simulated** device telemetry, dot-underlined via `.sim` and
  explained once in the header; or **absent**, shown as an em dash with a note naming who
  supplies it. No sensor exists, so a live river level can only ever be the second kind.

**Undecided product facts, deliberately not invented:** lahar-sand sale price per m³;
sensor unit, installation and annual subscription costs; the roadmap's KPI targets. These
are marked BLOCKING in `data/processed/model_assumptions.csv` and must stay em dashes until
the team supplies real figures.

**Not built.** No sensor is deployed and no pipeline is running. The SAP stack beyond SAC is
proposed architecture and is labelled as such wherever it appears.

## Brand Commitments

- **Name:** AGOS. Filipino for *flow* or *current*.
- **Deck chrome:** navy `#10344C`, teal `#1C7293`. These are chrome only — both fail as
  data marks (outside the lightness band, below the chroma floor) and read as grey.
- **Reserved status palette, contrast-verified:** Watch `#F2C14E` on `#4a3708` (6.80:1) ·
  Warning `#C74A1A` on white (4.75:1) · Evacuate Now `#9E1F17` on white (7.89:1). Aligned to
  PAGASA's own rainfall-warning convention so residents do not have to learn a second colour
  language.
- **Voice:** plain, direct, no marketing register. The product tells someone what is
  happening and what to do.
- Governing design spec: `docs/DESIGN_BRIEF.md`.

## Evidence on Hand

All figures are registered in `docs/SOURCES.md` with source, publication date and — the
field that matters most here — **geographic scope**, because several August 2026 figures in
circulation are national totals that read like local ones.

- INFORM Risk Index Mid 2026 (EC JRC, workflow 515) — ASEAN-10 hazard and capacity scores
- PAGASA ClimGridPh CliMap v2.0 — Olongapo monthly rainfall normals, August 865.97 mm
- MGB Central Luzon — 4.7 bn m³ lahar; Bucao 3.0 bn (63.8%), Santo Tomas 1.6 bn (34.0%)
- NDRRMC situational reports, August 2026 — national totals, labelled as such
- Contemporaneous reporting, 6–7 September 2026 — 11 Aeta communities in Botolan cut off,
  2,519 families, nine reached by helicopter and two by carabao cart

## Accessibility

WCAG AA is a floor, not an aspiration, and the reasons are situational rather than
compliance-driven: this interface is read in rain, at night, in direct sun, on cheap phones,
and printed in greyscale inside a PDF.

- Body text ≥ 4.5:1; large text and UI borders ≥ 3:1. **Computed, never judged by eye.**
- Severity encoded three ways — hue, luminance, and an icon plus text label.
- Tap targets ≥ 44px on resident-facing screens. Assume wet hands.
- Visible `:focus-visible` on every interactive element.
- Motion 120–250ms, and `prefers-reduced-motion` respected.

## Open Decisions

- Cover, pivot and alert photography for the storyboard is unsourced; route not yet chosen
  (official agency imagery, licensed stock, or the team's own photographs).
- Whether ADSE can enable SAC's Predictive Forecast on this tenant — it is licence-gated,
  so P8 currently ships as a plain time series.
