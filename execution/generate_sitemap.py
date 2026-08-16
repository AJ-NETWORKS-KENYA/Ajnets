from pathlib import Path
from datetime import datetime

root = Path(r"C:\My Web Sites\ajnets")
today = datetime.utcnow().strftime("%Y-%m-%d")

# Define sitemap entries with priority and changefreq
SITEMAP_ENTRIES = [
    {"loc": "https://ajnetworks.co/", "priority": "1.0", "changefreq": "weekly"},
    {"loc": "https://ajnetworks.co/company/about-us", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/company/book-consultation", "priority": "0.9", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/company/faq", "priority": "0.7", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/services/services", "priority": "0.9", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/services/technology-strategy", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/services/software-engineering", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/services/cybersecurity", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/services/networking", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/services/performance-seo", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/client-success", "priority": "0.9", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-audiophile", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-bada", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-crappo", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-greenremedies", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-racnyali", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-sgss", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/portfolio/case-study-transitflow", "priority": "0.8", "changefreq": "monthly"},
    {"loc": "https://ajnetworks.co/insights/insights", "priority": "0.8", "changefreq": "weekly"},
    {"loc": "https://ajnetworks.co/insights/post", "priority": "0.7", "changefreq": "monthly"},
]

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]

for entry in SITEMAP_ENTRIES:
    xml_lines.append("  <url>")
    xml_lines.append(f"    <loc>{entry['loc']}</loc>")
    xml_lines.append(f"    <lastmod>{today}</lastmod>")
    xml_lines.append(f"    <changefreq>{entry['changefreq']}</changefreq>")
    xml_lines.append(f"    <priority>{entry['priority']}</priority>")
    xml_lines.append("  </url>")

xml_lines.append("</urlset>\n")

sitemap_content = "\n".join(xml_lines)
with open(root / "sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Generated sitemap.xml with {len(SITEMAP_ENTRIES)} verified URLs.")

# Robots.txt
robots_content = """User-agent: *
Allow: /

Sitemap: https://ajnetworks.co/sitemap.xml
"""

with open(root / "robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

print("Generated robots.txt.")
