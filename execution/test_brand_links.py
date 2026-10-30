import os
import re
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIST_DIR = os.path.join(ROOT_DIR, "dist")
SCAN_DIR = DIST_DIR if os.path.isdir(DIST_DIR) else ROOT_DIR

EXPECTED_SOCIAL_LINKS = [
    "https://facebook.com/ajnetworks",
    "https://linkedin.com/company/ajnetworks",
    "https://www.youtube.com/@ajnets",
    "https://pinterest.com/ajnetworks"
]

def get_all_html_files(root):
    html_files = []
    for dirpath, _, filenames in os.walk(root):
        if any(x in dirpath for x in ("node_modules", ".git", ".tmp", ".astro", ".agent", ".agents")):
            continue
        for f in filenames:
            if f.endswith(".html"):
                html_files.append(os.path.join(dirpath, f))
    return html_files

def test_html_files():
    html_files = get_all_html_files(SCAN_DIR)
    assert len(html_files) > 0, f"No HTML files found in {SCAN_DIR}!"

    failures = []
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        rel_path = os.path.relpath(filepath, SCAN_DIR)

        # Check social links
        for link in EXPECTED_SOCIAL_LINKS:
            if link not in content:
                failures.append(f"[{rel_path}] Missing social link: {link}")

        # Check Schema.org JSON-LD
        match = re.search(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', content, re.DOTALL)
        if not match:
            failures.append(f"[{rel_path}] Missing <script type='application/ld+json'>")
        else:
            try:
                data = json.loads(match.group(1).strip())
                same_as = data.get("sameAs", [])
                for link in EXPECTED_SOCIAL_LINKS:
                    if link not in same_as:
                        failures.append(f"[{rel_path}] JSON-LD sameAs missing: {link}")
            except json.JSONDecodeError as e:
                failures.append(f"[{rel_path}] Invalid JSON-LD syntax: {e}")

        # Check canonical domain
        if "ajnetworkskenya.it.com" in content:
            failures.append(f"[{rel_path}] Contains legacy domain ajnetworkskenya.it.com")

    return failures

def test_sitemap_and_robots():
    failures = []
    sitemap = os.path.join(SCAN_DIR, "sitemap.xml")
    if not os.path.exists(sitemap):
        sitemap = os.path.join(ROOT_DIR, "public", "sitemap.xml")
    if os.path.exists(sitemap):
        with open(sitemap, "r", encoding="utf-8") as f:
            content = f.read()
        if "https://www.ajnetworks.co" in content:
            failures.append("[sitemap.xml] Contains www. prefix instead of https://ajnetworks.co")

    robots = os.path.join(SCAN_DIR, "robots.txt")
    if not os.path.exists(robots):
        robots = os.path.join(ROOT_DIR, "public", "robots.txt")
    if os.path.exists(robots):
        with open(robots, "r", encoding="utf-8") as f:
            content = f.read()
        if "https://ajnetworks.co/sitemap.xml" not in content:
            failures.append("[robots.txt] Missing https://ajnetworks.co/sitemap.xml")

    return failures

if __name__ == "__main__":
    print(f"Running Gate Tests: test_brand_links.py (target: {os.path.relpath(SCAN_DIR, ROOT_DIR)})")
    failures = test_html_files() + test_sitemap_and_robots()

    if failures:
        print(f"FAILED with {len(failures)} errors:")
        for err in failures:
            print(f" - {err}")
        exit(1)
    else:
        print("ALL GATE TESTS PASSED SUCCESSFULLY! (0 errors)")
        exit(0)
