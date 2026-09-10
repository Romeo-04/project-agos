# AGOS — National Finals Deck Backlog

Material cut from the 15-page storyboard, preserved for the **National Finals presentation** — a separate, later deliverable with its own rules and far more room.

This file exists so the compression in `AGOS_Storyboard_Plan_v2.md` is a *deferral*, not a deletion. v1 reverse-engineered a 79-page reference deck; that page count is impossible for an ADSE storyboard but entirely normal for a finals presentation. Everything below belongs there.

**Finals context:** shortlisted teams present slides and optionally an app prototype, with three to four weeks to prepare. Presentation Delivery carries **15%** and is judged on speaker confidence, handling technical questions, and professionalism of visuals.

---

## Cut from the storyboard — ready to reinstate

| Item | Original v1 home | Why it was cut | Finals value |
|---|---|---|---|
| **Per-feature deep dives** — EYE, PULSE, VOICE, PATH, FUND, one page each with mockup, synergies, SDG codes, ASEAN target | Part 3 §3.4 | Five pages against a 15-page cap; folded into P8, P9, P13 | **High.** This is the natural spine of a 15-minute talk — one feature per beat |
| **Country-by-country "when communities are left out" strip** — Vietnam Mekong, Indonesia Jakarta subsidence, Myanmar/Cambodia/Thailand | Part 1, slide 4 | Needed research and pages the storyboard did not have | **Medium.** Good for the regional-relevance question |
| **Five-year institutional report timeline** — IPCC AR6 / AHA Centre annual reports | Part 1, slide 6 | Proves "known and unacted" but costs a page for one rhetorical beat | **Medium.** Strong answer to "why hasn't this been solved already?" |
| **Components vs. Features hub diagram** | Part 3 §3.3 | No chart, and P7's architecture diagram covers the same ground better | **Low.** Superseded |
| **Win-win-win stakeholder table** | Part 4 §4.3 | Chartless page under a chart-scored rubric | **High.** Judges ask who pays and who benefits — this answers it directly |
| **Name-reveal bridge page** | Part 2, slide 12 | Pure pacing; unaffordable at 15 pages | **High.** Pacing is exactly what a live presentation needs |
| **Full ASEAN institutional partnership table** — AHA Centre, ACDM, NDRRMC-OCD, DELSA/JAIF, World Bank/ADB | Part 4 §4.2 | Compressed to a named list on P14 | **High.** The most credible section for a Viability question |

---

## Ambitious features — deferred, not dropped

Strong ideas with no room in the storyboard. All three are excellent Q&A material, and each answers a predictable judge question.

- **Cross-border Region III data sharing** (Bataan, Tarlac, Pampanga) — the same August 2026 monsoon warning covered all of them, so a shared regional dashboard multiplies value without multiplying cost.
  *Answers:* "Does this only work in one city?"

- **AHA Centre / ADInet integration** — push Zambales data into ASEAN's own regional situational-awareness feed.
  *Answers:* "How does this connect to ASEAN institutions?" Retained in compressed form on P15, worth full treatment at finals.

- **Parametric micro-insurance trigger** — a PULSE threshold crossing auto-initiates claims for enrolled households, removing the weeks-long adjustment delay after a flood.
  *Answers:* "What happens after the flood?" — the one part of the disaster cycle AGOS otherwise does not touch.

---

## App prototype — if the team builds one

The finals permit an app prototype. v1 §3.6 already specifies five screens, and they remain the right five:

1. Household alert (VOICE) — three states: Watch / Warning / Evacuate Now
2. Barangay officer route status (PATH) — map, tap to set status
3. LGU engineer dashboard (EYE) — river map, lahar risk colour coding
4. Provincial treasurer widget (FUND) — revenue vs. cost
5. Home / onboarding — barangay status summary, links to the other four

**Design tokens** carry over from `AGOS_Storyboard_Plan_v2.md` §4. Two rules that matter:

- Alert severity uses the **reserved status palette** — Watch `#F2C14E`, Warning `#C74A1A`, Evacuate Now `#9E1F17` — aligned to PAGASA's own rainfall-warning convention so residents do not have to learn a second colour language. Always paired with an icon and a text label, never colour alone. These are the contrast-corrected values (6.80:1 / 4.75:1 / 7.89:1); the earlier `#D9531E` failed AA at 4.03:1. Full rationale in `docs/DESIGN_BRIEF.md`.
- The categorical chart palette (`#2E6FA8`, `#E0762F`, `#1FA8C4`, `#8C5BB0`, `#5A9E3E`) is for **analytical charts only** and must not appear as alert states.

Keep each screen to a single task. This is a tool for people who may be evacuating.

---

## Anticipated judge questions

Prepared answers matter more at finals than more slides. The hardest questions, and where the answer already lives:

| Question | Where the answer is |
|---|---|
| "The Philippines is only 8th of 10 on flood hazard — why here?" | **Storyboard P4.** PH is 1st on all-hazard exposure; river-flood indices under-count compound, lahar-amplified flooding. Rehearse this one — it looks like a trap and is actually the strongest answer in the deck. |
| "What happens when the sensor is destroyed?" | Storyboard P12 — non-contact sensors above historical max, replacement budgeted as a consumable |
| "Why will people trust another alert system?" | P12 — three-tier alert language against documented alert fatigue; barangay captains retained as the verified relay |
| "Who pays after the grant runs out?" | P13 — lahar-sand revenue as a reserve fund, plus subscription and licensing |
| "Does this work outside the Philippines?" | P15 — Myanmar, Lao PDR, Cambodia by lack-of-coping-capacity score |
| "What about communities with no phone signal?" | **P11** — this is the strongest answer available. On 6 Sept 2026 nine of eleven Aeta communities in Botolan could only be reached by helicopter. The solar siren is the primary channel for that population, not a fallback. |

---

## Rule check before building the finals deck

The 15-page cap, the 20 MB limit, and the landscape requirement are **storyboard rules**. Do not assume they carry over. Re-read the finals requirements on aseandse.org when the shortlist is announced, and confirm the page/time limits before building.
