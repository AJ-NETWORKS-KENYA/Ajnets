"""
AJNETWORKS Full Static Regression Audit Script
Checks: broken links, SEO tags, tracking scripts, missing assets
"""
import os, re, json
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"c:\My Web Sites\ajnets")
HTML_FILES = sorted(ROOT.glob("*.html"))
LIVE_DOMAIN = "https://ajnetworkskenya.it.com"

# ── Internal nav pages we care most about ──────────────────────────────────────
KEY_PAGES = [
    "index.html", "about-us.html", "services.html", "client-success.html",
    "book-consultation.html", "insights.html",
    "software-engineering.html", "cybersecurity.html",
    "technology-strategy.html", "networking.html", "performance-seo.html",
    "case-study-bada.html", "case-study-sgss.html", "case-study-racnyali.html",
    "case-study-transitflow.html", "case-study-audiophile.html", "case-study-greenremedies.html",
]

results = {
    "broken_links": [],
    "seo_issues": [],
    "tracking_issues": [],
    "asset_issues": [],
    "ok_pages": [],
    "seo_ok": [],
    "tracking_ok": [],
}

# ─── 1. BROKEN INTERNAL LINK CHECKER ─────────────────────────────────────────
print("\n═══ 1. INTERNAL LINK CHECKER ═══")
link_pattern = re.compile(r'href=["\']([^"\'#?]+)["\']', re.I)

for html_path in HTML_FILES:
    with open(html_path, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    links = link_pattern.findall(content)
    for link in links:
        # Skip external, mailto, tel, js
        if link.startswith(("http", "mailto:", "tel:", "javascript", "//")):
            continue
        # Resolve relative path
        target = ROOT / link.split("?")[0].split("#")[0]
        if not target.exists():
            results["broken_links"].append({"source": html_path.name, "target": link})
            print(f"  ✗ BROKEN: {html_path.name} → {link}")

if not results["broken_links"]:
    print("  ✓ No broken internal links detected")

# ─── 2. SEO STRUCTURE AUDIT ───────────────────────────────────────────────────
print("\n═══ 2. SEO STRUCTURE AUDIT ═══")

title_re   = re.compile(r'<title>(.+?)</title>', re.I | re.S)
desc_re    = re.compile(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', re.I | re.S)
h1_re      = re.compile(r'<h1[^>]*>(.*?)</h1>', re.I | re.S)
schema_re  = re.compile(r'"@type"\s*:\s*"(Organization|LocalBusiness)"', re.I)
og_re      = re.compile(r'<meta\s+property=["\']og:title["\']', re.I)
canonical_re = re.compile(r'<link\s+rel=["\']canonical["\']', re.I)

for page in KEY_PAGES:
    path = ROOT / page
    if not path.exists():
        results["seo_issues"].append({"page": page, "issue": "FILE MISSING"})
        print(f"  ✗ MISSING: {page}")
        continue

    with open(path, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    issues = []
    title = title_re.search(html)
    if not title:
        issues.append("Missing <title>")
    elif len(title.group(1)) < 10 or len(title.group(1)) > 70:
        issues.append(f"Title length {len(title.group(1))} chars (ideal: 10-70)")

    desc = desc_re.search(html)
    if not desc:
        issues.append("Missing <meta description>")
    elif len(desc.group(1)) < 50 or len(desc.group(1)) > 160:
        issues.append(f"Meta desc length {len(desc.group(1))} chars (ideal: 50-160)")

    h1s = h1_re.findall(html)
    if not h1s:
        issues.append("Missing <h1>")
    elif len(h1s) > 1:
        issues.append(f"{len(h1s)} <h1> tags (should be exactly 1)")

    if issues:
        for iss in issues:
            results["seo_issues"].append({"page": page, "issue": iss})
            print(f"  ⚠ {page}: {iss}")
    else:
        results["seo_ok"].append(page)

print(f"\n  ✓ {len(results['seo_ok'])} pages passed SEO checks")
print(f"  ✗ {len(results['seo_issues'])} SEO issues found")

# ─── 3. TRACKING SCRIPTS AUDIT ────────────────────────────────────────────────
print("\n═══ 3. TRACKING SCRIPTS AUDIT ═══")

ga_re       = re.compile(r'G-2E6LLT0TT7', re.I)
cookie_re   = re.compile(r'cookie-consent\.js', re.I)
linkedin_re = re.compile(r'linkedin\.com/in/\|partner_id\|_linkedin_partner_id|linkedin\.com/px', re.I)

for page in KEY_PAGES:
    path = ROOT / page
    if not path.exists():
        continue
    with open(path, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    issues = []
    if not ga_re.search(html):
        issues.append("Missing GA4 tag (G-2E6LLT0TT7)")
    if not cookie_re.search(html):
        issues.append("Missing cookie-consent.js")

    if issues:
        for iss in issues:
            results["tracking_issues"].append({"page": page, "issue": iss})
            print(f"  ⚠ {page}: {iss}")
    else:
        results["tracking_ok"].append(page)

print(f"\n  ✓ {len(results['tracking_ok'])} pages have complete tracking")
print(f"  ✗ {len(results['tracking_issues'])} tracking issues found")

# ─── 4. ASSET EXISTENCE CHECK ─────────────────────────────────────────────────
print("\n═══ 4. MISSING ASSET AUDIT ═══")

src_pattern = re.compile(r'(?:src|href)=["\']([^"\'#?]+\.(?:css|js|jpg|jpeg|png|webp|svg|ico))["\']', re.I)

checked_assets = set()
for html_path in HTML_FILES:
    if html_path.name not in KEY_PAGES:
        continue
    with open(html_path, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    assets = src_pattern.findall(content)
    for asset in assets:
        if asset.startswith(("http", "//", "data:")):
            continue
        target = ROOT / asset
        if str(target) not in checked_assets:
            checked_assets.add(str(target))
            if not target.exists():
                results["asset_issues"].append({"source": html_path.name, "asset": asset})
                print(f"  ✗ MISSING ASSET: {html_path.name} → {asset}")

if not results["asset_issues"]:
    print("  ✓ All referenced local assets exist")

# ─── SUMMARY ─────────────────────────────────────────────────────────────────
print("\n═══════════════════════════════════════")
print("STATIC AUDIT SUMMARY")
print("═══════════════════════════════════════")
print(f"  HTML files scanned:       {len(HTML_FILES)}")
print(f"  Broken internal links:    {len(results['broken_links'])}")
print(f"  SEO issues:               {len(results['seo_issues'])}")
print(f"  Tracking issues:          {len(results['tracking_issues'])}")
print(f"  Missing asset references: {len(results['asset_issues'])}")

# Save results as JSON for report generation
import json
with open(ROOT / "_audit_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("\n  Results saved to _audit_results.json")
