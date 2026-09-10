#!/usr/bin/env python3
"""
Generate the storyboard's References page from the citation register.

ADSE requires a references section, and it does not count against the 15-page cap.
Generating it from SOURCES.md rather than maintaining it by hand means the page can
never drift out of sync with the figures actually used.

Reads   docs/SOURCES.md   (the "Verified" and "Competition rules" tables)
Writes  docs/REFERENCES.md

Usage:  python scripts/build_references.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "SOURCES.md"
OUT = ROOT / "docs" / "REFERENCES.md"


def split_row(line: str) -> list:
    """Split a markdown table row into its cells."""
    return [c.strip() for c in line.strip().strip("|").split("|")]


def strip_md(text: str) -> str:
    """Remove markdown emphasis and inline code so the output reads as plain prose."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1 (\2)", text)
    return text.strip()


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"ERROR: {SRC} not found")

    lines = SRC.read_text(encoding="utf-8").splitlines()

    sources, rules = [], []
    section = None
    for line in lines:
        s = line.strip()
        if s.startswith("## "):
            head = s[3:].lower()
            if "verified" in head and "cleared" in head:
                section = "sources"
            elif "competition rules" in head:
                section = "rules"
            else:
                section = None
            continue
        if not s.startswith("|") or set(s) <= set("|- "):
            continue
        cells = split_row(s)
        if not cells or cells[0] in ("#", "") or cells[0].startswith("---"):
            continue

        if section == "sources" and len(cells) >= 6:
            sources.append({
                "id": cells[0],
                "figure": strip_md(cells[1]),
                "scope": strip_md(cells[2]),
                "source": strip_md(cells[3]),
                "published": strip_md(cells[4]),
                "retrieved": strip_md(cells[5]),
            })
        elif section == "rules" and len(cells) >= 4:
            rules.append({
                "id": cells[0],
                "rule": strip_md(cells[1]),
                "source": strip_md(cells[2]),
                "retrieved": strip_md(cells[3]),
            })

    # Group by the publishing organisation so the page reads like a reference list
    # rather than a dump of the internal register.
    def org_of(src: str) -> str:
        low = src.lower()
        if "inform risk" in low or "jrc" in low:
            return "INFORM Risk Index — European Commission, Joint Research Centre"
        if "pagasa" in low or "climgridph" in low:
            return "PAGASA — Philippine Atmospheric, Geophysical and Astronomical Services Administration"
        if "ndrrmc" in low:
            return "NDRRMC — National Disaster Risk Reduction and Management Council"
        if "mgb" in low:
            return "MGB — Mines and Geosciences Bureau, Central Luzon"
        if "derived" in low:
            return "Derived in this project (reproducible from scripts/)"
        return "News reporting (contemporaneous)"

    grouped = {}
    for s in sources:
        grouped.setdefault(org_of(s["source"]), []).append(s)

    out = []
    out.append("# AGOS — References\n")
    out.append("Storyboard: **AGOS**, Team **Naive Bais**, FEU – Institute of Technology, Philippines.\n")
    out.append(
        "Every figure used in the storyboard appears below with its **geographic scope** "
        "stated explicitly, because several figures in circulation about the August 2026 "
        "floods are national totals that are easily mistaken for local ones.\n"
    )
    out.append("---\n")

    order = [
        "INFORM Risk Index — European Commission, Joint Research Centre",
        "PAGASA — Philippine Atmospheric, Geophysical and Astronomical Services Administration",
        "MGB — Mines and Geosciences Bureau, Central Luzon",
        "NDRRMC — National Disaster Risk Reduction and Management Council",
        "News reporting (contemporaneous)",
        "Derived in this project (reproducible from scripts/)",
    ]
    for org in order:
        if org not in grouped:
            continue
        out.append(f"## {org}\n")
        for s in grouped[org]:
            out.append(f"- **[{s['id']}]** {s['figure']}")
            out.append(f"  - Scope: {s['scope']}")
            bits = [f"Source: {s['source']}"]
            if s["published"] and s["published"] != "—":
                bits.append(f"Published: {s['published']}")
            bits.append(f"Retrieved: {s['retrieved']}")
            out.append("  - " + " · ".join(bits))
        out.append("")

    if rules:
        out.append("---\n")
        out.append("## Competition rules consulted\n")
        for r in rules:
            out.append(f"- **[{r['id']}]** {r['rule']}")
            out.append(f"  - {r['source']} · Retrieved: {r['retrieved']}")
        out.append("")

    out.append("---\n")
    out.append(
        "All datasets and the scripts that build them are in the project repository. "
        "Every derived figure regenerates from source with a single command, so any number "
        "on any page can be traced back to the data it came from.\n"
    )

    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"  wrote {OUT.relative_to(ROOT)}")
    print(f"  {len(sources)} sourced figures across {len(grouped)} organisations")
    print(f"  {len(rules)} competition rules")


if __name__ == "__main__":
    main()
