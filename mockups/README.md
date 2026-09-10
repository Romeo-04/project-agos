# AGOS — interface mockups

`agos-screens.html` — a single self-contained file rendering every AGOS screen.
No build step, no dependencies. Open it in a browser, or serve the folder:

```bash
python -m http.server 8823
# then http://localhost:8823/agos-screens.html
```

## Screens

| # | Screen | Used on |
|---|---|---|
| 1–3 | **VOICE** household alert — Watch / Warning / Evacuate Now | Storyboard **P9**, finals deck |
| 4 | **PATH** barangay-officer road status | Storyboard **P9**, finals deck |
| 5 | **EYE** LGU engineer dashboard | Storyboard **P7/P8**, finals deck |
| 6 | **FUND** provincial treasurer widget | Storyboard **P13**, finals deck |
| 7 | **Home** resident landing | Finals deck |

## Design rules these follow

- **Severity colours are PAGASA's own rainfall-warning convention** — Watch amber,
  Warning orange, Evacuate red — so residents don't have to learn a second colour language.
- **Severity is never colour alone.** Every state carries an icon *and* a text label,
  which also keeps it readable for colour-blind users and in greyscale print.
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

## Exporting for the deck

Screenshot individual screens at 2× for print clarity. Keep each image under 2 MB
(the ADSE per-image cap). Rendered PNGs are **not** committed — only this source is.
