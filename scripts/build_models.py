#!/usr/bin/env python3
"""
Build the four MODELLED datasets: P10 lead time, P12 risk matrix, P13 FUND, P14 roadmap.

These differ from every other dataset in this repo. The others are measurements with a
citation. These are models built on stated assumptions, and the storyboard prints those
assumptions on the page.

A transparent model with visible assumptions is credible. A confident number with hidden
ones is not - and it is exactly how v1 ended up with three figures that did not survive
checking. Every assumption below is carried in the output as data, so it cannot be lost
between here and the chart.

Usage:  python scripts/build_models.py
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "data" / "processed"

# ---------------------------------------------------------------------------
# ASSUMPTIONS - every one of these must appear on its page.
# Sourced values are marked SOURCED; the rest are ESTIMATES the team should own.
# ---------------------------------------------------------------------------
ASSUMPTIONS = [
    ("A1", "P10", "Olongapo evacuation, 18 Aug 2026: 1,076 individuals / 336 families",
     "SOURCED", "SOURCES.md S6"),
    ("A2", "P10", "Current warning is reactive: alert issued when river reaches evacuation level at the bridge",
     "SOURCED", "Reported practice, SOURCES.md S5-S7"),
    ("A3", "P10", "AGOS lead time of 2 hours from upstream sensor threshold to downstream evacuation level",
     "ESTIMATE", "Team to validate against Bucao-to-Olongapo channel travel time"),
    ("A4", "P10", "Evacuation completion follows an S-curve; households move faster once neighbours do",
     "ESTIMATE", "Standard evacuation-behaviour assumption"),
    ("A5", "P13", "4.7 bn m3 lahar in Zambales rivers; 50 m m3 dredged to date (1.06%)",
     "SOURCED", "SOURCES.md S20-S21"),
    ("A6", "P13", "Zambales River Restoration Program operating since 2023, deltas only",
     "SOURCED", "SOURCES.md S21"),
    ("A7", "P13", "Lahar-sand sale price per m3",
     "UNSOURCED - BLOCKING", "Team must supply a Provincial Treasurer figure before P13 ships"),
    ("A8", "P13", "Sensor unit cost, installation cost, annual platform subscription per LGU",
     "UNSOURCED - BLOCKING", "Team to set from vendor quotes"),
    ("A9", "P14", "24-month roadmap across 4 phases",
     "ESTIMATE", "Carried from v1 plan section 4.4"),
    ("A10", "P12", "Likelihood and impact scored 1-5 by the team, not measured",
     "ESTIMATE", "Qualitative risk assessment"),
]

# ---------------------------------------------------------------------------
# P10 - lead-time scenario comparison
# Cumulative % of at-risk households evacuated, by minutes from first alert.
# Two scenarios over a common timeline so this charts on ONE axis, never two.
# ---------------------------------------------------------------------------
LEADTIME = [
    # minutes, reactive %, AGOS %
    (0, 0, 0), (15, 3, 18), (30, 9, 41), (45, 18, 63), (60, 30, 80),
    (75, 44, 91), (90, 58, 96), (105, 70, 99), (120, 79, 100),
]

# ---------------------------------------------------------------------------
# P12 - risk matrix. Content is v1's failure/mitigation set, scored for charting.
# ---------------------------------------------------------------------------
RISKS = [
    ("R1", "PULSE", "Sensor destroyed or swept away in extreme flow", 4, 4,
     "Non-contact ultrasonic/radar sensors mounted above historical maximum flood line; replacement budgeted as a consumable, not capex"),
    ("R2", "PULSE", "Cellular signal lost during the storm, when it matters most", 4, 5,
     "Dual uplink - LoRaWAN mesh between sensors as primary, cellular as backup"),
    ("R3", "EYE", "Monsoon cloud cover blocks optical satellite imagery", 5, 3,
     "Sentinel-1 SAR imagery penetrates cloud; primary feed during active monsoon"),
    ("R4", "EYE", "Satellite revisit too slow to catch fast lahar shifts after one storm", 3, 3,
     "Drone flyover auto-triggered when a PULSE sensor crosses its warning threshold"),
    ("R5", "VOICE", "Alert fatigue erodes trust after false alarms", 4, 4,
     "Three-tier language - Watch / Warning / Evacuate Now - instead of binary alerting"),
    ("R6", "VOICE", "Power or cell outage cuts off the highest-risk households", 4, 5,
     "Solar-charged barangay siren/beacon on the same PULSE threshold; no phone required"),
    ("R7", "PATH", "Crowd-sourced road status goes stale", 4, 3,
     "Status older than 2 hours auto-downgrades to 'Unconfirmed - proceed with caution'"),
    ("R8", "PATH", "Malicious or mistaken false reports", 2, 4,
     "Only barangay-verified officer accounts can set status; residents may flag for review"),
    ("R9", "FUND", "Lahar-sand revenue fluctuates with construction demand", 4, 3,
     "Reserve-fund structure - bank surplus in high-demand quarters against low ones"),
    ("R10", "Programme", "LGU turnover ends political sponsorship mid-rollout", 3, 4,
     "MOU at provincial PDRRMO level, not city administration alone; data stays with the LGU"),
]

# ---------------------------------------------------------------------------
# P14 - roadmap. Baselines are real; TARGETS ARE DELIBERATELY BLANK.
# A KPI without a baseline is not measurable; a target is the team's call.
# ---------------------------------------------------------------------------
ROADMAP = [
    (1, "Engagement & Planning", 1, 3,
     "Co-design with Olongapo OCDRRMO and Zambales PDRRMO",
     "Formal MOU signed", "Barangays with signed participation", "0", ""),
    (2, "Deployment & Set-up", 4, 9,
     "Convert 3 manual Olongapo bridge gauges to PULSE; install upstream Bucao/Santo Tomas sensors",
     "Devices reporting into the platform", "Sensors live and reporting", "0", ""),
    (3, "Operation & Monsoon Stress Test", 10, 15,
     "VOICE alerts and PATH live; SAC dashboard live for LGU engineers",
     "First full monsoon season monitored", "Sensor uptime in monsoon season (%)", "n/a", ""),
    (4, "Scaling & Reporting", 16, 24,
     "Expand to Region III neighbours; first submission to AHA Centre ADInet",
     "Annual Flood Resilience Report published", "Lahar dredged per quarter vs. baseline", "1.06% in 35 years", ""),
]


def write_csv(path: Path, fieldnames: list, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(fieldnames)
        w.writerows(rows)
    print(f"  wrote {path.relative_to(ROOT)}  ({len(rows)} rows)")


def main() -> None:
    write_csv(
        PROC / "model_assumptions.csv",
        ["AssumptionId", "Page", "Assumption", "Status", "Basis"],
        ASSUMPTIONS,
    )

    write_csv(
        PROC / "leadtime_scenarios.csv",
        ["MinutesFromFirstAlert", "ReactiveWarningPct", "AgosLeadTimePct"],
        LEADTIME,
    )

    risk_rows = [
        (rid, comp, desc, lik, imp, lik * imp, mit)
        for rid, comp, desc, lik, imp, mit in RISKS
    ]
    write_csv(
        PROC / "risk_matrix.csv",
        ["RiskId", "Component", "Risk", "Likelihood1to5", "Impact1to5",
         "RiskScore", "Mitigation"],
        risk_rows,
    )

    write_csv(
        PROC / "roadmap_phases.csv",
        ["Phase", "PhaseName", "StartMonth", "EndMonth", "Step", "Action",
         "KpiName", "KpiBaseline", "KpiTarget"],
        ROADMAP,
    )

    # ---- gate report ---------------------------------------------------------
    blocking = [a for a in ASSUMPTIONS if "BLOCKING" in a[3]]
    print("\n  Assumption status:")
    print(f"    SOURCED:   {sum(1 for a in ASSUMPTIONS if a[3] == 'SOURCED')}")
    print(f"    ESTIMATE:  {sum(1 for a in ASSUMPTIONS if a[3] == 'ESTIMATE')}")
    print(f"    BLOCKING:  {len(blocking)}")
    for a in blocking:
        print(f"      [{a[0]}] {a[1]}: {a[2]}")
    print("\n  P13 cannot ship until the BLOCKING assumptions have team-supplied values.")
    print("  P14 KpiTarget is intentionally blank - targets are the team's call.")


if __name__ == "__main__":
    main()
