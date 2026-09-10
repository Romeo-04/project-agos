#!/usr/bin/env python3
"""
Build the ASEAN-10 INFORM Risk datasets that back storyboard pages P2, P3, P4 and P15.

Source: INFORM Risk Mid 2026, European Commission Joint Research Centre.
        Public REST API, workflow 515.

Outputs are written flat, with plain headers and no thousands separators, so they
import into SAP Analytics Cloud without manual type fixing.

Usage:  python scripts/build_asean_inform.py
"""

import csv
import json
import statistics
import urllib.request
from pathlib import Path

API = "https://drmkc.jrc.ec.europa.eu/inform-index/API/InformAPI"
WORKFLOW = 515  # INFORM Risk Mid 2026

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "inform_2026"
PROC = ROOT / "data" / "processed"

# ASEAN member states, ISO3 -> display name used across the storyboard
ASEAN = {
    "BRN": "Brunei Darussalam",
    "KHM": "Cambodia",
    "IDN": "Indonesia",
    "LAO": "Lao PDR",
    "MYS": "Malaysia",
    "MMR": "Myanmar",
    "PHL": "Philippines",
    "SGP": "Singapore",
    "THA": "Thailand",
    "VNM": "Viet Nam",
}

# INFORM indicator -> the column name used in the storyboard
INDICATORS = {
    "HA.NAT.FL": "FloodHazard",       # river flood hazard & exposure, 0-10
    "HA": "HazardExposure",           # overall Hazard & Exposure dimension
    "VU": "Vulnerability",            # Vulnerability dimension
    "CC": "LackOfCopingCapacity",     # Lack of Coping Capacity dimension
    "INFORM": "InformRisk",           # composite INFORM Risk score
}


def fetch(indicator: str) -> dict:
    """Fetch one indicator for every country, return {iso3: score} for ASEAN only."""
    url = f"{API}/countries/Scores/?WorkflowId={WORKFLOW}&IndicatorId={indicator}"
    with urllib.request.urlopen(url, timeout=120) as r:
        payload = json.loads(r.read().decode("utf-8"))

    RAW.mkdir(parents=True, exist_ok=True)
    safe = indicator.replace(".", "_")
    (RAW / f"{safe}.json").write_text(
        json.dumps(payload, indent=1), encoding="utf-8"
    )

    return {
        row["Iso3"]: row["IndicatorScore"]
        for row in payload
        if row["Iso3"] in ASEAN
    }


def write_csv(path: Path, fieldnames: list, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path.relative_to(ROOT)}  ({len(rows)} rows)")


def main() -> None:
    print(f"INFORM Risk Mid 2026 (workflow {WORKFLOW}) -> ASEAN-10")

    scores = {}
    for indicator, column in INDICATORS.items():
        print(f"  fetching {indicator} ...")
        for iso3, value in fetch(indicator).items():
            scores.setdefault(iso3, {})[column] = value

    missing = set(ASEAN) - set(scores)
    if missing:
        raise SystemExit(f"ERROR: no data returned for {sorted(missing)}")

    cols = list(INDICATORS.values())

    # ---- P3 / P15: full multi-dimensional table, plus the quadrant flag -------
    # Quadrant lines are the ASEAN medians, so the split is defined by the region
    # itself rather than by an arbitrary threshold.
    med_flood = statistics.median(scores[i]["FloodHazard"] for i in ASEAN)
    med_cc = statistics.median(scores[i]["LackOfCopingCapacity"] for i in ASEAN)
    print(f"  ASEAN medians -> FloodHazard {med_flood}, LackOfCopingCapacity {med_cc}")

    multidim = []
    for iso3, name in ASEAN.items():
        row = {"Country": name, "ISO3": iso3}
        row.update({c: scores[iso3][c] for c in cols})
        # Note on direction: LackOfCopingCapacity is scored so that HIGHER means
        # WORSE. "Weak capacity" is therefore >= the median, not <=.
        high_hazard = row["FloodHazard"] >= med_flood
        weak_capacity = row["LackOfCopingCapacity"] >= med_cc
        row["Quadrant"] = (
            "High flood hazard / Weak capacity" if high_hazard and weak_capacity
            else "High flood hazard / Stronger capacity" if high_hazard
            else "Lower flood hazard / Weak capacity" if weak_capacity
            else "Lower flood hazard / Stronger capacity"
        )
        # Carried on every row so SAC can draw the quadrant lines straight from
        # the dataset rather than from a hardcoded value in the chart definition.
        row["MedianFloodHazard"] = med_flood
        row["MedianLackOfCopingCapacity"] = med_cc
        multidim.append(row)

    multidim.sort(key=lambda r: -r["FloodHazard"])
    write_csv(
        PROC / "asean_inform_multidim_2026.csv",
        ["Country", "ISO3"] + cols
        + ["Quadrant", "MedianFloodHazard", "MedianLackOfCopingCapacity"],
        multidim,
    )

    # ---- P2: single-measure flood hazard bar chart ---------------------------
    write_csv(
        PROC / "asean_flood_inform2026.csv",
        ["Country", "ISO3", "FloodHazard", "SevereThreshold"],
        [
            {
                "Country": r["Country"],
                "ISO3": r["ISO3"],
                "FloodHazard": r["FloodHazard"],
                # 8.0 = the "severe" reference line drawn on P2
                "SevereThreshold": 8.0,
            }
            for r in multidim
        ],
    )

    # ---- P4: Philippines against the ASEAN median, by dimension --------------
    # Readable axis labels; the raw indicator names are not presentation-grade.
    LABELS = {
        "FloodHazard": "River flood hazard",
        "HazardExposure": "Hazard & exposure (all hazards)",
        "Vulnerability": "Vulnerability",
        "LackOfCopingCapacity": "Lack of coping capacity",
        "InformRisk": "INFORM Risk (composite)",
    }
    ph_rows = []
    for column in cols:
        median = round(statistics.median(scores[i][column] for i in ASEAN), 2)
        ph = scores["PHL"][column]
        rank = sorted(
            (scores[i][column] for i in ASEAN), reverse=True
        ).index(ph) + 1
        ph_rows.append(
            {
                "Dimension": LABELS[column],
                "Philippines": ph,
                "ASEANMedian": median,
                "GapVsMedian": round(ph - median, 2),
                "PhilippinesRank": rank,
            }
        )
    write_csv(
        PROC / "ph_vs_asean_dimensions.csv",
        ["Dimension", "Philippines", "ASEANMedian", "GapVsMedian", "PhilippinesRank"],
        ph_rows,
    )

    # ---- console summary, for the citation register --------------------------
    print("\n  Findings for SOURCES.md:")
    ranked = sorted(multidim, key=lambda r: -r["FloodHazard"])
    ph_rank = [r["ISO3"] for r in ranked].index("PHL") + 1
    severe = [r["Country"] for r in ranked if r["FloodHazard"] >= 8.0]
    print(f"    Philippines river flood hazard rank: {ph_rank} of {len(ranked)}")
    print(f"    States at or above 8.0: {len(severe)} -> {', '.join(severe)}")
    worst_cc = sorted(multidim, key=lambda r: -r["LackOfCopingCapacity"])[:3]
    print(
        "    Weakest coping capacity: "
        + ", ".join(f"{r['Country']} {r['LackOfCopingCapacity']}" for r in worst_cc)
    )


if __name__ == "__main__":
    main()
