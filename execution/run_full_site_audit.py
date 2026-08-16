import os
import sys
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl

root = Path(r"C:\My Web Sites\ajnets")
html_files = sorted([f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents", ".git"])])

print(f"Total HTML pages to analyze: {len(html_files)}")

banned_words = [
    "innovative", "cutting-edge", "cutting edge", "world-class", "world class", 
    "revolutionary", "disruptive", "cheap", "affordable", "budget", 
    "best in kenya", "guaranteed", "freelance", "outsourcing"
]

all_pages_data = {}
all_titles = {}
all_descriptions = {}
all_canonicals = {}
all_h1s = {}
all_internal_links = []
all_external_links = []
missing_image_files = []
orphan_check_links = set()

# Live site test map
live_results = {}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for hf in html_files:
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    # Titles
    titles = [t.get_text().strip() for t in soup.find_all("title")]
    all_titles[rel] = titles
    
    # Meta description
    meta_desc = [m.get("content", "").strip() for m in soup.find_all("meta", attrs={"name": re.compile(r"^description$", re.I)})]
    all_descriptions[rel] = meta_desc
    
    # Canonical
    canonicals = [c.get("href", "").strip() for c in soup.find_all("link", attrs={"rel": "canonical"})]
    all_canonicals[rel] = canonicals
    
    # OG Tags
    og_title = [m.get("content", "") for m in soup.find_all("meta", attrs={"property": "og:title"})]
    og_desc = [m.get("content", "") for m in soup.find_all("meta", attrs={"property": "og:description"})]
    og_image = [m.get("content", "") for m in soup.find_all("meta", attrs={"property": "og:image"})]
    og_url = [m.get("content", "") for m in soup.find_all("meta", attrs={"property": "og:url"})]
    og_type = [m.get("content", "") for m in soup.find_all("meta", attrs={"property": "og:type"})]
    og_site_name = [m.get("content", "") for m in soup.find_all("meta", attrs={"property": "og:site_name"})]
    
    # Twitter tags
    tw_card = [m.get("content", "") for m in soup.find_all("meta", attrs={"name": "twitter:card"})]
    tw_title = [m.get("content", "") for m in soup.find_all("meta", attrs={"name": "twitter:title"})]
    tw_desc = [m.get("content", "") for m in soup.find_all("meta", attrs={"name": "twitter:description"})]
    tw_image = [m.get("content", "") for m in soup.find_all("meta", attrs={"name": "twitter:image"})]
    
    # JSON-LD
    json_lds = []
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            parsed = json.loads(s.string) if s.string else {}
            t = parsed.get("@type", "unknown")
            json_lds.append({"type": t, "raw": parsed})
        except Exception as e:
            json_lds.append({"type": "INVALID_JSON", "error": str(e)})
            
    # Headings
    h1s = [h.get_text().strip() for h in soup.find_all("h1")]
    h2s = [h.get_text().strip() for h in soup.find_all("h2")]
    h3s = [h.get_text().strip() for h in soup.find_all("h3")]
    h4s = [h.get_text().strip() for h in soup.find_all("h4")]
    all_h1s[rel] = h1s
    
    # Images
    imgs = soup.find_all("img")
    img_details = []
    for img in imgs:
        src = img.get("src", "")
        alt = img.get("alt", None)
        loading = img.get("loading", None)
        w = img.get("width", None)
        h = img.get("height", None)
        
        # Check if local image exists
        exists_on_disk = True
        file_size_bytes = None
        if src and not src.startswith("http") and not src.startswith("data:"):
            clean_src = src.split("?")[0].split("#")[0]
            if clean_src.startswith("/"):
                img_path = root / clean_src.lstrip("/")
            else:
                img_path = (hf.parent / clean_src).resolve()
            if not img_path.exists():
                exists_on_disk = False
                missing_image_files.append({"page": rel, "src": src, "resolved_path": str(img_path)})
            else:
                file_size_bytes = img_path.stat().st_size
                
        img_details.append({
            "src": src,
            "alt": alt,
            "loading": loading,
            "width": w,
            "height": h,
            "exists_on_disk": exists_on_disk,
            "size_bytes": file_size_bytes
        })
        
    # Links
    links = soup.find_all("a")
    page_links = []
    for a in links:
        href = a.get("href", "").strip()
        text = a.get_text().strip()
        target = a.get("target", "")
        rel_attr = a.get("rel", "")
        if href:
            page_links.append({"href": href, "text": text, "target": target, "rel": rel_attr})
            if href.startswith("http"):
                all_external_links.append({"page": rel, "href": href, "text": text, "rel": rel_attr, "target": target})
            elif not href.startswith("#") and not href.startswith("mailto:") and not href.startswith("tel:") and not href.startswith("javascript:"):
                all_internal_links.append({"page": rel, "href": href, "text": text})
                orphan_check_links.add(href)
                
    # Scripts
    script_tags = soup.find_all("script")
    scripts = [s.get("src", "") for s in script_tags if s.get("src")]
    inline_scripts = [s.string for s in script_tags if not s.get("src") and s.string]
    
    # CSS
    css_links = [c.get("href", "") for c in soup.find_all("link", attrs={"rel": "stylesheet"})]
    inline_styles = [s.string for s in soup.find_all("style") if s.string]
    
    # Forms
    forms = []
    for f_idx, form in enumerate(soup.find_all("form")):
        action = form.get("action", "")
        method = form.get("method", "")
        inputs = [{"name": inp.get("name"), "type": inp.get("type"), "required": inp.has_attr("required")} for inp in form.find_all(["input", "select", "textarea"])]
        forms.append({"action": action, "method": method, "inputs": inputs})
        
    # Buzzwords check in text
    text_content = soup.get_text().lower()
    found_buzzwords = {}
    for bw in banned_words:
        matches = len(re.findall(r"\b" + re.escape(bw) + r"\b", text_content))
        if matches > 0:
            found_buzzwords[bw] = matches
            
    all_pages_data[rel] = {
        "rel_path": rel,
        "html_size_bytes": len(html),
        "titles": titles,
        "meta_desc": meta_desc,
        "canonicals": canonicals,
        "og": {
            "title": og_title,
            "description": og_desc,
            "image": og_image,
            "url": og_url,
            "type": og_type,
            "site_name": og_site_name
        },
        "twitter": {
            "card": tw_card,
            "title": tw_title,
            "description": tw_desc,
            "image": tw_image
        },
        "json_ld": json_lds,
        "headings": {
            "h1": h1s,
            "h2": h2s,
            "h3": h3s,
            "h4": h4s
        },
        "images": {
            "total": len(imgs),
            "missing_alt": [i for i in img_details if i["alt"] is None or i["alt"].strip() == ""],
            "missing_lazy": [i for i in img_details if i["loading"] != "lazy"],
            "missing_dimensions": [i for i in img_details if not i["width"] or not i["height"]],
            "details": img_details
        },
        "links": {
            "total": len(links),
            "internal_count": len([l for l in page_links if not l["href"].startswith("http")]),
            "external_count": len([l for l in page_links if l["href"].startswith("http")]),
            "details": page_links
        },
        "scripts": {
            "external": scripts,
            "inline_count": len(inline_scripts)
        },
        "stylesheets": {
            "external": css_links,
            "inline_count": len(inline_styles)
        },
        "forms": forms,
        "banned_buzzwords": found_buzzwords
    }

# Check live URLs corresponding to clean URLs
print("\n=== TESTING LIVE ENDPOINTS ===")
routes_to_test = [
    ("/", "index.html"),
    ("/about-us", "company/about-us.html"),
    ("/book-consultation", "company/book-consultation.html"),
    ("/faq", "company/faq.html"),
    ("/services", "services/services.html"),
    ("/technology-strategy", "services/technology-strategy.html"),
    ("/software-engineering", "services/software-engineering.html"),
    ("/cybersecurity", "services/cybersecurity.html"),
    ("/networking", "services/networking.html"),
    ("/performance-seo", "services/performance-seo.html"),
    ("/client-success", "portfolio/client-success.html"),
    ("/case-study-audiophile", "portfolio/case-study-audiophile.html"),
    ("/case-study-bada", "portfolio/case-study-bada.html"),
    ("/case-study-crappo", "portfolio/case-study-crappo.html"),
    ("/case-study-greenremedies", "portfolio/case-study-greenremedies.html"),
    ("/case-study-racnyali", "portfolio/case-study-racnyali.html"),
    ("/case-study-sgss", "portfolio/case-study-sgss.html"),
    ("/case-study-transitflow", "portfolio/case-study-transitflow.html"),
    ("/insights", "insights/insights.html"),
    ("/post", "insights/post.html")
]

for route, mapped_file in routes_to_test:
    live_url = f"https://ajnetworks.co{route}"
    try:
        req = urllib.request.Request(live_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AuditBot/1.0"})
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            live_results[route] = {
                "url": live_url,
                "status": resp.status,
                "headers": dict(resp.getheaders()),
                "bytes": len(resp.read())
            }
            print(f"  [OK {resp.status}] {live_url}")
    except urllib.error.HTTPError as he:
        live_results[route] = {"url": live_url, "status": he.code, "error": str(he)}
        print(f"  [HTTP ERROR {he.code}] {live_url}")
    except Exception as e:
        live_results[route] = {"url": live_url, "status": "ERROR", "error": str(e)}
        print(f"  [ERROR] {live_url}: {e}")

# Save full crawl data
output_path = root / "teamwork_audit" / "CRAWL_DATA.json"
final_data = {
    "summary": {
        "total_html_files": len(html_files),
        "total_images_analyzed": sum(d["images"]["total"] for d in all_pages_data.values()),
        "total_links_analyzed": sum(d["links"]["total"] for d in all_pages_data.values()),
        "live_endpoints_tested": len(routes_to_test),
        "live_endpoints_ok": len([r for r in live_results.values() if r.get("status") == 200])
    },
    "pages": all_pages_data,
    "live_site_tests": live_results,
    "missing_images_on_disk": missing_image_files
}

with open(output_path, "w", encoding="utf-8") as out:
    json.dump(final_data, out, indent=2)

print(f"\nSuccessfully wrote crawl data to {output_path}")
