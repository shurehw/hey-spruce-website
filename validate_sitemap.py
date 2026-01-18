from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(".")
SITEMAP = ROOT / "sitemap.xml"


def url_to_expected_file(path: str) -> Path | None:
    """
    Map a canonical URL path (cleanUrls + trailingSlash:false) to its expected HTML file.
    """
    if not path.startswith("/"):
        return None

    # Homepage
    if path == "/":
        return ROOT / "index.html"

    # Hub pages
    if path == "/blog":
        return ROOT / "blog.html"
    if path == "/case-studies":
        return ROOT / "case-studies.html"

    # Nested content
    if path.startswith("/blog/"):
        slug = path.removeprefix("/blog/").strip("/")
        if not slug:
            return ROOT / "blog.html"
        return ROOT / "blog" / f"{slug}.html"

    if path.startswith("/case-studies/"):
        slug = path.removeprefix("/case-studies/").strip("/")
        if not slug:
            return ROOT / "case-studies.html"
        return ROOT / "case-studies" / f"{slug}.html"

    # Root-level clean URLs map to root HTML files
    slug = path.strip("/")
    if not slug:
        return ROOT / "index.html"
    return ROOT / f"{slug}.html"


def main() -> int:
    if not SITEMAP.exists():
        print("ERROR: sitemap.xml not found", file=sys.stderr)
        return 2

    xml = SITEMAP.read_text(encoding="utf-8", errors="ignore")
    root = ET.fromstring(xml)

    # Namespace agnostic: find all <loc> tags
    locs: list[str] = []
    for el in root.iter():
        if el.tag.endswith("loc") and el.text:
            locs.append(el.text.strip())

    missing: list[tuple[str, str]] = []
    checked = 0

    for loc in locs:
        u = urlparse(loc)
        expected = url_to_expected_file(u.path)
        if expected is None:
            continue
        checked += 1
        if not expected.exists():
            missing.append((loc, expected.as_posix()))

    print(f"checked_urls: {checked}")
    print(f"missing_files: {len(missing)}")
    for loc, expected in missing[:50]:
        print(f"- {loc} -> expected file missing: {expected}")
    if len(missing) > 50:
        print("... (truncated)")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

