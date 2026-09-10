#!/usr/bin/env python3
"""
Build the Olongapo datasets backing storyboard page P6.

Two outputs:
  olongapo_rainfall_normals.csv  - PAGASA 30-year normals, SAC-ready
  olongapo_aug2026_events.csv    - the August 2026 flood sequence, correctly scoped

Source for the normals: PAGASA ClimGridPh / CliMap v2.0 municipal climate normals
(rainfall 2001-2020, temperature 1991-2020), supplied by the team.

Source for the events: contemporaneous Inquirer / GMA reporting. Every row is
scoped to Olongapo City and carries its own citation - see SOURCES.md S5-S7.

Usage:  python scripts/build_olongapo.py
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "raw" / "pagasa_climgridph" / "olongapo_city_municipal_monthly.csv"
PROC = ROOT / "data" / "processed"

MONTH_ORDER = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# The August 2026 sequence, at Olongapo City scope only.
# Deliberately excludes the national figures (8.1M affected, PHP 3.4B) - those
# belong on P4 and are labelled national there. Mixing scopes is what broke v1.
AUG_2026_EVENTS = [
    {
        "Date": "2026-08-10",
        "EventLabel": "First evacuation",
        "Individuals": 517,
        "Families": 165,
        "BarangaysAffected": 11,
        "Scope": "Olongapo City",
        "Source": "Inquirer / GMA News, 2026-08-10",
    },
    {
        "Date": "2026-08-17",
        "EventLabel": "Bridges reach evacuation level",
        "Individuals": "",       # reported qualitatively, no count given
        "Families": "",
        "BarangaysAffected": "",
        "Scope": "Olongapo City",
        "Source": "Inquirer, 2026-08-17",
    },
    {
        "Date": "2026-08-18",
        "EventLabel": "Second evacuation",
        "Individuals": 1076,
        "Families": 336,
        "BarangaysAffected": "",
        "Scope": "Olongapo City",
        "Source": "Inquirer, 2026-08-18",
    },
    {
        "Date": "2026-08-28",
        "EventLabel": "Flooding and soil erosion; roads impassable",
        "Individuals": "",
        "Families": "",
        "BarangaysAffected": "",
        "Scope": "Olongapo City",
        "Source": "Inquirer, 2026-08-28/29",
    },
]


def write_csv(path: Path, fieldnames: list, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path.relative_to(ROOT)}  ({len(rows)} rows)")


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"ERROR: missing source file {SRC}")

    with SRC.open(encoding="utf-8") as f:
        raw = list(csv.DictReader(f))

    rows = []
    for r in raw:
        month = r["Month"].strip()
        rows.append(
            {
                "MonthNumber": MONTH_ORDER.index(month) + 1,
                "Month": month,
                "MonthShort": month[:3],
                "RainfallMm": float(r["Rainfall"]),
                "MeanTempC": float(r["MeanTemp"]),
                "Municipality": r["Municipality"].strip(),
                "Province": r["Province"].strip(),
            }
        )
    rows.sort(key=lambda r: r["MonthNumber"])

    wettest = max(rows, key=lambda r: r["RainfallMm"])
    annual = sum(r["RainfallMm"] for r in rows)

    # Flags SAC uses for conditional highlighting on P6, so the emphasis is
    # driven by the data rather than by hand-picking a bar in the chart editor.
    for r in rows:
        r["IsWettestMonth"] = "Yes" if r["Month"] == wettest["Month"] else "No"
        r["ShareOfAnnualPct"] = round(r["RainfallMm"] / annual * 100, 1)

    write_csv(
        PROC / "olongapo_rainfall_normals.csv",
        ["MonthNumber", "Month", "MonthShort", "RainfallMm", "MeanTempC",
         "ShareOfAnnualPct", "IsWettestMonth", "Municipality", "Province"],
        rows,
    )

    write_csv(
        PROC / "olongapo_aug2026_events.csv",
        ["Date", "EventLabel", "Individuals", "Families",
         "BarangaysAffected", "Scope", "Source"],
        AUG_2026_EVENTS,
    )

    # ---- console summary, for the citation register --------------------------
    runner_up = sorted(rows, key=lambda r: -r["RainfallMm"])[1]
    jja_son = [r for r in rows if r["Month"] in ("June", "July", "August", "September")]
    print("\n  Findings for SOURCES.md:")
    print(f"    Wettest month: {wettest['Month']} at {wettest['RainfallMm']} mm")
    print(
        f"    Margin over {runner_up['Month']}: "
        f"{round(wettest['RainfallMm'] - runner_up['RainfallMm'], 2)} mm"
    )
    print(f"    August share of annual rainfall: {wettest['ShareOfAnnualPct']}%")
    print(f"    Annual total (normals): {round(annual, 2)} mm")
    print(
        "    Jun-Sep share of annual: "
        f"{round(sum(r['RainfallMm'] for r in jja_son) / annual * 100, 1)}%"
    )


if __name__ == "__main__":
    main()
