# Source — Aeta community isolation, Botolan, September 2026

- **Event:** 11 Aeta communities in Botolan, Zambales cut off from the town proper by swollen
  rivers and impassable roads; relief delivered 6 September 2026
- **Source:** Philippine Daily Inquirer, "11 Aeta communities get food aid as swollen rivers cut
  off access," published **2026-09-07**
- **Scope:** **Botolan municipality, Zambales** — eastern section locally known as Baytan
- **Retrieved:** 2026-09-10

## Figures as reported

| Figure | Value |
|---|---|
| Aeta communities cut off | **11** |
| Affected families | **2,519** |
| Family food packs delivered | **4,564** |
| Distance from Botolan town proper | **25–30 km** |
| Duration of the relief operation | **more than 7 hours** |
| Communities reached by helicopter | **9** |
| Communities reached by carabao-drawn cart | **2** |
| River system | **Bucao River** and two tributaries draining Mount Pinatubo |
| Responding agencies | Zambales PDRRMO · Philippine Air Force · Botolan LGU |

**Human cost:** a father and his 5-year-old daughter drowned earlier that week when their cart
was swept away by river currents while travelling to Barangay Palis.

## Data note — read before charting

`DistanceFromTownProperKm` is recorded as **27.5 for every row**: the source gives a single
range ("about 25 to 30 kilometres") for the group, not a per-barangay distance. The midpoint is
carried on each row so the dataset is chartable, **but it must not be presented as a
per-barangay measurement.** Chart it as a group annotation, or replace it with per-barangay
distances if a survey source is found. This is exactly the scope-drift failure that put three
wrong numbers into v1.

`AccessMethodDuringCutoff` is reported per-community and is reliable: 9 airlift, 2 cart.

## Why this anchors P11

The Bucao River is the same system AGOS's EYE and PULSE components target. These communities
are simultaneously the most lahar-exposed population in Zambales, the furthest from response
capacity, and the least connected — and in September 2026 the fastest available way to reach
nine of them was a military helicopter.

This is the evidentiary basis for the design decision on P11: for this population, a
solar-powered barangay siren triggered by an upstream sensor is not a fallback channel.
It is the only channel that works.
