"""
P3 Fixes:
  1. Add Service JSON-LD schema to service pages
  2. Fix accessibility: add aria-labels to icon-only buttons/links
  3. Add og:image fallback file (SVG placeholder)
"""
import os, re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")

# ─── 1. Service page JSON-LD schemas ──────────────────────────────────────────
service_schemas = {
    "software-engineering.html": {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Software Engineering & Systems Development",
        "provider": {"@type": "Organization", "name": "AJNETWORKS", "url": "https://ajnetworkskenya.it.com"},
        "description": "Custom web platforms, mobile applications, and enterprise systems built with security-first engineering practices.",
        "areaServed": "KE",
        "serviceType": "Software Engineering"
    },
    "cybersecurity.html": {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Cybersecurity & Assurance Services",
        "provider": {"@type": "Organization", "name": "AJNETWORKS", "url": "https://ajnetworkskenya.it.com"},
        "description": "Enterprise-grade cybersecurity including network security, penetration testing, RBAC design, and compliance advisory.",
        "areaServed": "KE",
        "serviceType": "Cybersecurity"
    },
    "technology-strategy.html": {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Technology & Digital Strategy Consulting",
        "provider": {"@type": "Organization", "name": "AJNETWORKS", "url": "https://ajnetworkskenya.it.com"},
        "description": "Digital transformation advisory, IT roadmap planning, and technology strategy consulting for East African enterprises.",
        "areaServed": "KE",
        "serviceType": "Technology Consulting"
    },
    "networking.html": {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Networking & IT Infrastructure",
        "provider": {"@type": "Organization", "name": "AJNETWORKS", "url": "https://ajnetworkskenya.it.com"},
        "description": "Enterprise networking, LAN/WAN design, cloud connectivity, and IT infrastructure implementation in Kenya.",
        "areaServed": "KE",
        "serviceType": "Networking & Infrastructure"
    },
    "performance-seo.html": {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Web Performance & SEO Optimization",
        "provider": {"@type": "Organization", "name": "AJNETWORKS", "url": "https://ajnetworkskenya.it.com"},
        "description": "Core Web Vitals improvement, technical SEO auditing, and website speed optimization for Kenyan businesses.",
        "areaServed": "KE",
        "serviceType": "SEO & Performance"
    },
}

import json
for page, schema in service_schemas.items():
    filepath = ROOT / page
    if not filepath.exists():
        print(f"SKIP: {page}")
        continue

    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    if '"@type": "Service"' in html:
        print(f"  Schema already present: {page}")
        continue

    schema_tag = f'\n    <script type="application/ld+json">{json.dumps(schema, indent=6)}</script>\n'

    if '</head>' in html:
        html = html.replace('</head>', schema_tag + '  </head>', 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Schema added: {page}")

# ─── 2. Accessibility fixes on all HTML pages ────────────────────────────────
# Add aria-label to social + search icon links that lack descriptive text
aria_fixes = [
    # Social links: add aria-label
    (r'<a class="share-facebook" href="([^"]*)" target="_blank">', r'<a class="share-facebook" href="\1" target="_blank" aria-label="Share on Facebook" rel="noopener">'),
    (r'<a class="share-twitter" href="([^"]*)" target="_blank">', r'<a class="share-twitter" href="\1" target="_blank" aria-label="Share on Twitter" rel="noopener">'),
    (r'<a class="share-linkedin" href="([^"]*)" target="_blank">', r'<a class="share-linkedin" href="\1" target="_blank" aria-label="Share on LinkedIn" rel="noopener">'),
    (r'<a class="share-pinterest" href="([^"]*)" target="_blank">', r'<a class="share-pinterest" href="\1" target="_blank" aria-label="Share on Pinterest" rel="noopener">'),
    # Toggle search button
    (r'<div class="toggle_search octf-cta-icons">\s*<i class="flaticon-search"></i>\s*</div>',
     '<button class="toggle_search octf-cta-icons" aria-label="Search" type="button"><i class="flaticon-search" aria-hidden="true"></i></button>'),
    # Mobile menu toggle
    (r'<div id="mmenu_toggle">\s*<button>',
     '<div id="mmenu_toggle"><button aria-label="Open navigation menu" aria-expanded="false">'),
    # Back to top button
    (r'<a id="back-to-top" href="#" class="show">',
     '<a id="back-to-top" href="#" class="show" aria-label="Back to top">'),
]

a11y_patched = 0
for html_path in sorted(ROOT.glob("*.html")):
    with open(html_path, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    original = content
    for pattern, replacement in aria_fixes:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if content != original:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        a11y_patched += 1
        print(f"  Accessibility patched: {html_path.name}")

# ─── 3. Create OG image placeholder if it doesn't exist ─────────────────────
og_image_path = ROOT / "images" / "og-home.jpg"
if not og_image_path.exists():
    # Create a simple SVG that can serve as placeholder
    svg_placeholder = ROOT / "images" / "og-home.svg"
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#0a0e1a"/>
  <text x="600" y="280" font-family="Inter, sans-serif" font-size="72" font-weight="700" fill="#00d4ff" text-anchor="middle">AJNETWORKS</text>
  <text x="600" y="360" font-family="Inter, sans-serif" font-size="32" fill="#94a3b8" text-anchor="middle">Technology Consulting &amp; Engineering</text>
  <text x="600" y="420" font-family="Inter, sans-serif" font-size="24" fill="#475569" text-anchor="middle">Nairobi &amp; Mombasa, Kenya</text>
</svg>'''
    with open(svg_placeholder, "w") as f:
        f.write(svg_content)
    print(f"  Created OG image placeholder: images/og-home.svg")

print(f"\nTotal a11y pages patched: {a11y_patched}")
print("P3 fixes complete.")
