# AGOS — interface mockups and diagrams

Two self-contained files. No build step, no dependencies — open either in a browser, or
serve the folder:

```bash
python -m http.server 8823
# then http://localhost:8823/agos-screens.html
#      http://localhost:8823/agos-architecture.html
```

| File | Covers |
|---|---|
| `agos-screens.html` | the seven app screens — **P9**, P7/P8 support, **P13**, finals deck |
| `agos-architecture.html` | the system architecture diagram — **P7** |

Both carry the same token block. It is duplicated rather than imported so each file opens
standalone from disk with nothing missing.

## Screens

| # | Screen | Used on |
|---|---|---|
| 1–3 | **VOICE** household alert — Watch / Warning / Evacuate Now | Storyboard **P9**, finals deck |
| 4 | **PATH** barangay-officer road status | Storyboard **P9**, finals deck |
| 5 | **EYE** LGU engineer dashboard | Storyboard **P7/P8**, finals deck |
| 6 | **FUND** provincial treasurer widget | Storyboard **P13**, finals deck |
| 7 | **Home** resident landing | Finals deck |

> **Building or extending these? Read `docs/DESIGN_BRIEF.md` first.** It is written to be
> self-contained — tokens, per-screen specs, the data rules, and a computable acceptance
> checklist — so a fresh session can work from it without reading the rest of the repo.
> What follows here is the summary.

## Design rules these follow

- **Severity colours are PAGASA's own rainfall-warning convention** — Watch amber,
  Warning orange, Evacuate red — so residents don't have to learn a second colour language.
- **Severity is never colour alone.** Every state carries an icon *and* a text label,
  which also keeps it readable for colour-blind users and in greyscale print.
- **Severity reads as a lightness ramp**, not just a hue change — relative luminance
  0.576 → 0.171 → 0.083 across Watch → Warning → Evacuate. The escalation therefore
  survives greyscale printing and colour-blind vision, not only colour perception.
- **All three states share one treatment** (a solid fill) so the tier reads as a single
  ladder. An earlier draft gave Watch a pale background plus a thick left border, which
  made it look like a different component rather than step one of the same scale.
- **Every fill is WCAG AA verified against its own ink:** Watch 6.80:1, Warning 4.75:1,
  Evacuate 7.89:1. The first draft's warning orange was 4.03:1 and would have shipped
  failing AA — worth re-checking with a contrast calculation, not by eye, if these
  colours are ever adjusted.
- **Status colours are reserved.** They never appear as chart-series colours; the
  analytical charts use a separate validated categorical palette.
- One 4px spacing scale, one neutral ramp, one accent (`--accent`, used only for the
  primary action and focus rings). Real inline SVG icons, never emoji.
- All interactive elements have hover and a visible `:focus-visible` ring.

## Figures shown are real

Every number traces to `docs/SOURCES.md`:

- 4.7 bn m³ lahar; Bucao 3.0 bn (63.8%), Santo Tomas 1.6 bn (34.0%) — MGB Central Luzon
- 1.06% dredged in 35 years — the FUND progress bar is *deliberately* almost invisible
- 21 barangays under threat — 6 Bucao, 15 Santo Tomas
- 866 mm August normal — PAGASA ClimGridPh CliMap v2.0

**FUND's revenue rows are dashes on purpose.** Lahar-sand price per m³ and sensor costs
have not been sourced, and inventing them would be the same failure as the misattributed
figures removed from the v1 plan. The screen says so on its face.

**Sensors reporting shows an em dash**, not a number — the pilot isn't deployed. Showing
a fabricated sensor count on a mockup of an unbuilt system would be dishonest.

## `agos-architecture.html` — the P7 diagram

Four stages left to right: **Sense** (EYE, PULSE) → **Integrate & model** (SAP BTP, SAP
Datasphere) → **Analyse** (SAP Analytics Cloud) → **Act & sustain** (VOICE, PATH, FUND).

**The two-state key is the point of the page.** Exactly one card is marked *Demonstrated* —
SAC, the layer every chart in this deck was actually built in. Everything else is marked
*Proposed architecture*, in muted ink, because it is designed and costed but not built.

Claiming a live BTP pipeline that does not exist is the kind of overreach that collapses
under the first question at finals. The honest split is also the stronger one: it shows the
team knows which part of the stack it has proven.

Component tags use the **validated categorical palette** (`#2E6FA8`, `#E0762F`, `#1FA8C4`,
`#8C5BB0`, `#5A9E3E`) — the same five hues as the charts — with SAP layers in brand navy.
No status colour appears anywhere on this diagram; severity red/orange/amber stay reserved
for the alert states.

## Exporting for the deck

Screenshot individual screens at 2× for print clarity. Keep each image under 2 MB
(the ADSE per-image cap). Rendered PNGs are **not** committed — only this source is.
