#!/usr/bin/env python3
"""
Print deck/index.html to the submission PDF.

ADSE requires a landscape PDF of at most 15 pages and 20 MB, named
PHILIPPINES_<TEAM NAME>.pdf. This drives headless Chromium so the output
matches what the browser renders, and then checks the result against the
rules that are pass/fail — because an unsubmittable PDF scores zero no
matter what is on the pages.

Usage:
    pip install playwright && playwright install chromium
    python scripts/build_deck_pdf.py

Writes  deck/PHILIPPINES_NAIVE BAIS.pdf  (gitignored)
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "deck" / "index.html"
OUT = ROOT / "deck" / "PHILIPPINES_NAIVE BAIS.pdf"

MAX_PAGES = 15
MAX_MB = 20.0
MAX_IMAGE_MB = 2.0


def check_images() -> list:
    """Each embedded image has its own 2 MB cap, separate from the document cap."""
    problems = []
    for d in (ROOT / "deck" / "charts", ROOT / "deck" / "photos"):
        if not d.exists():
            continue
        for f in sorted(d.iterdir()):
            if f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                mb = f.stat().st_size / 1_048_576
                if mb > MAX_IMAGE_MB:
                    problems.append(f"{f.relative_to(ROOT)} is {mb:.1f} MB (cap {MAX_IMAGE_MB} MB)")
    return problems


def missing_assets() -> list:
    """Report referenced files that do not exist, so a blank box is never a surprise."""
    import re
    html = SRC.read_text(encoding="utf-8")
    missing = []
    for m in re.finditer(r'src="([^"]+)"', html):
        p = (SRC.parent / m.group(1)).resolve()
        if not p.exists():
            missing.append(m.group(1))
    # placeholders the page itself declares
    for m in re.finditer(r'<span class="f">([^<]+)</span>', html):
        rel = m.group(1).strip()
        if not (ROOT / rel).exists():
            missing.append(rel + "  (placeholder box shown)")
    return missing


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"ERROR: {SRC} not found")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise SystemExit(
            "Playwright is not installed.\n"
            "  pip install playwright\n"
            "  playwright install chromium"
        )

    for note in missing_assets():
        print(f"  MISSING  {note}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(SRC.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUT),
            width="297mm",
            height="210mm",
            landscape=False,      # the page box is already landscape-shaped
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        browser.close()

    size_mb = OUT.stat().st_size / 1_048_576

    # page count, read straight out of the PDF
    raw = OUT.read_bytes()
    pages = raw.count(b"/Type /Page") - raw.count(b"/Type /Pages")
    if pages <= 0:
        pages = raw.count(b"/Type/Page") - raw.count(b"/Type/Pages")

    # References are required, and explicitly exempt from the page cap, so
    # they are counted apart from the pages that must fit inside it.
    ref_pages = SRC.read_text(encoding="utf-8").count('data-refs="1"')
    content_pages = pages - ref_pages

    print(f"\n  wrote {OUT.relative_to(ROOT)}")
    plural = "" if ref_pages == 1 else "s"
    print(f"  {content_pages} content pages + {ref_pages} reference page{plural}"
          f" = {pages} total · {size_mb:.2f} MB")

    fails = []
    if content_pages > MAX_PAGES:
        fails.append(f"{content_pages} content pages exceeds the {MAX_PAGES}-page cap")
    if ref_pages == 0:
        fails.append("no references page, and ADSE requires one")
    if size_mb > MAX_MB:
        fails.append(f"{size_mb:.1f} MB exceeds the {MAX_MB} MB cap")
    fails += check_images()

    print()
    if fails:
        for f in fails:
            print(f"  FAIL  {f}")
        sys.exit(1)
    print("  PASS  page count, file size, per-image size and the references page")
    print("        all satisfy the ADSE rules.")
    print("  Still to check by eye: every chart legible at 100% and in print,")
    print("  and the cover's six required elements.")


if __name__ == "__main__":
    main()
