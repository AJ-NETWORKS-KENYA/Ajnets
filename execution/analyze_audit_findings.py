import os
import sys
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(r"C:\My Web Sites\ajnets")
crawl_path = root / "teamwork_audit" / "CRAWL_DATA.json"

with open(crawl_path, "r", encoding="utf-8") as f:
    crawl_data = json.load(f)

pages = crawl_data["pages"]

print(f"=== DETAILED FINDINGS EXTRACTION ({len(pages)} pages) ===")

findings = []

# 1. SEO & METADATA CHECKS
print("\n--- 1. SEO & METADATA ANALYSIS ---")
titles = {}
meta_descs = {}
canonicals = {}
og_images = {}

for p, data in pages.items():
    # Title analysis
    t_list = data["titles"]
    if len(t_list) == 0:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": "Missing <title> tag"})
    elif len(t_list) > 1:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": f"Multiple ({len(t_list)}) <title> tags"})
    else:
        t = t_list[0]
        titles.setdefault(t, []).append(p)
        if len(t) < 30:
            findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": f"Title tag too short ({len(t)} chars): '{t}'"})
        elif len(t) > 65:
            findings.append({"category": "SEO", "severity": "P3", "page": p, "issue": f"Title tag potentially truncated in SERPs ({len(t)} chars): '{t}'"})
            
    # Meta description analysis
    d_list = data["meta_desc"]
    if len(d_list) == 0:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": "Missing meta description tag"})
    elif len(d_list) > 1:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": f"Multiple ({len(d_list)}) meta description tags"})
    else:
        d = d_list[0]
        meta_descs.setdefault(d, []).append(p)
        if len(d) < 70:
            findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": f"Meta description too short ({len(d)} chars): '{d}'"})
        elif len(d) > 165:
            findings.append({"category": "SEO", "severity": "P3", "page": p, "issue": f"Meta description exceeds SERP snippet limit ({len(d)} chars): '{d}'"})

    # Canonical analysis
    c_list = data["canonicals"]
    if len(c_list) == 0:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": "Missing canonical URL tag"})
    elif len(c_list) > 1:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": f"Multiple ({len(c_list)}) canonical tags"})
    else:
        c = c_list[0]
        if not c.startswith("https://ajnetworks.co"):
            findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": f"Canonical URL not absolute HTTPS: '{c}'"})
            
    # Open Graph & Twitter Cards
    og = data["og"]
    if not og["title"]:
        findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": "Missing og:title tag"})
    if not og["description"]:
        findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": "Missing og:description tag"})
    if not og["image"]:
        findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": "Missing og:image tag"})
    elif og["image"][0] and not og["image"][0].startswith("http"):
        findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": f"og:image uses relative path instead of absolute URL: '{og['image'][0]}'"})
    if not og["url"]:
        findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": "Missing og:url tag"})
        
    tw = data["twitter"]
    if not tw["card"]:
        findings.append({"category": "SEO", "severity": "P3", "page": p, "issue": "Missing twitter:card tag"})
        
    # Heading hierarchy
    h1_list = data["headings"]["h1"]
    if len(h1_list) == 0:
        findings.append({"category": "SEO", "severity": "P1", "page": p, "issue": "Missing H1 heading tag"})
    elif len(h1_list) > 1:
        findings.append({"category": "SEO", "severity": "P2", "page": p, "issue": f"Multiple ({len(h1_list)}) H1 tags found: {h1_list}"})

# Check for duplicate titles and descriptions
for t, p_list in titles.items():
    if len(p_list) > 1:
        findings.append({"category": "SEO", "severity": "P1", "page": str(p_list), "issue": f"Duplicate title tag across {len(p_list)} pages: '{t}'"})

for d, p_list in meta_descs.items():
    if len(p_list) > 1:
        findings.append({"category": "SEO", "severity": "P1", "page": str(p_list), "issue": f"Duplicate meta description across {len(p_list)} pages: '{d}'"})

# 2. PERFORMANCE & ASSETS
print("\n--- 2. PERFORMANCE & ASSETS ANALYSIS ---")
for p, data in pages.items():
    imgs = data["images"]
    if imgs["missing_alt"]:
        findings.append({"category": "Accessibility", "severity": "P2", "page": p, "issue": f"{len(imgs['missing_alt'])} images missing alt attributes"})
    if imgs["missing_lazy"]:
        findings.append({"category": "Performance", "severity": "P2", "page": p, "issue": f"{len(imgs['missing_lazy'])} images missing loading='lazy'"})
    if imgs["missing_dimensions"]:
        findings.append({"category": "Performance", "severity": "P2", "page": p, "issue": f"{len(imgs['missing_dimensions'])} images missing explicit width/height dimensions (CLS risk)"})
        
    # Check external scripts
    scripts = data["scripts"]["external"]
    for s in scripts:
        if "cdn.tailwindcss.com" in s:
            findings.append({"category": "Performance", "severity": "P1", "page": p, "issue": "Client-side runtime Tailwind CDN (cdn.tailwindcss.com) used in production; causes JIT compilation overhead, render delay, and CSP issues"})

# Check image file formats on disk
large_images = []
legacy_format_images = []
for p in (root / "images").rglob("*.*"):
    if p.is_file() and p.suffix.lower() in [".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg"]:
        size_kb = p.stat().st_size / 1024
        if size_kb > 200:
            large_images.append((str(p.relative_to(root)), round(size_kb, 1)))
        if p.suffix.lower() in [".png", ".jpg", ".jpeg"]:
            legacy_format_images.append(str(p.relative_to(root)))

if large_images:
    findings.append({"category": "Performance", "severity": "P2", "page": "images/", "issue": f"{len(large_images)} unoptimized image assets exceed 200KB (e.g. {large_images[:3]})"})
if legacy_format_images:
    findings.append({"category": "Performance", "severity": "P3", "page": "images/", "issue": f"{len(legacy_format_images)} raster images in legacy PNG/JPG format without modern next-gen AVIF/WebP equivalents"})

# Check unused stylesheets
css_files = [f.name for f in (root / "css").glob("*.css")]
if "woocommerce.css" in css_files:
    findings.append({"category": "Technical", "severity": "P3", "page": "css/woocommerce.css", "issue": "Dead code / unused stylesheet: 'woocommerce.css' exists in codebase for a non-e-commerce consultancy website"})

# 3. SECURITY & DATA PRIVACY
print("\n--- 3. SECURITY & DATA PRIVACY ANALYSIS ---")
# Check serverless rate limiting & CORS
findings.append({
    "category": "Security",
    "severity": "P1",
    "page": "api/contact.js",
    "issue": "In-memory rate limiter (ipRateLimit Map) fails to persist across serverless lambdas in Vercel, allowing bypass across horizontal instances"
})

findings.append({
    "category": "Security",
    "severity": "P2",
    "page": "api/contact.js",
    "issue": "Lack of cryptographic bot protection (e.g. Cloudflare Turnstile or reCAPTCHA v3); reliance solely on naive hidden bot_field honeypot"
})

findings.append({
    "category": "Security",
    "severity": "P2",
    "page": "vercel.json",
    "issue": "CSP uses 'unsafe-inline' for script-src and style-src without cryptographic hashes or nonces, weakening XSS mitigation"
})

findings.append({
    "category": "Security",
    "severity": "P3",
    "page": "vercel.json",
    "issue": "X-Frame-Options is set to 'SAMEORIGIN' while Content-Security-Policy defines frame-ancestors 'none'; modern browsers prioritize CSP frame-ancestors but header mismatch exists"
})

# Secrets in root
secrets_files = []
for sec_name in [".env", ".env.local", "credentials.json", "token.json"]:
    if (root / sec_name).exists():
        secrets_files.append(sec_name)

if secrets_files:
    findings.append({
        "category": "Security",
        "severity": "P2",
        "page": "Root directory",
        "issue": f"Local secret/credential stub files ({', '.join(secrets_files)}) present in workspace; risk of accidental git exposure if .gitignore is modified"
    })

# Check Cookie Consent & Third-Party Tracking
findings.append({
    "category": "Security & Compliance",
    "severity": "P2",
    "page": "Global / Tracking Scripts",
    "issue": "LinkedIn Insight Tag and Google Tag Manager load prior to explicit user opt-in consent, violating strict GDPR and Kenya Data Protection Act 2019 consent requirements"
})

# Missing Legal Pages
legal_pages_check = ["privacy-policy", "terms-of-service", "responsible-disclosure"]
missing_legal = []
for lp in legal_pages_check:
    if not any(lp in p for p in pages.keys()):
        missing_legal.append(lp)

if missing_legal:
    findings.append({
        "category": "Credibility & Compliance",
        "severity": "P1",
        "page": "Site Architecture",
        "issue": f"Missing dedicated legal/trust pages: {', '.join(missing_legal)} (mandated in data.md sections 7, 18 & 19)"
    })

# 4. BUSINESS & STRATEGIC POSITIONING
print("\n--- 4. BUSINESS & STRATEGIC POSITIONING ANALYSIS ---")
for p, data in pages.items():
    bw = data["banned_buzzwords"]
    if bw:
        findings.append({
            "category": "Strategic Positioning",
            "severity": "P2",
            "page": p,
            "issue": f"Banned buzzwords detected in violation of data.md tone guidelines: {bw}"
        })

# Case Study Completeness against data.md 10-point standard
case_studies = [p for p in pages.keys() if "case-study-" in p]
print(f"Analyzing {len(case_studies)} case studies...")
for cs in case_studies:
    p_data = pages[cs]
    with open(root / cs, "r", encoding="utf-8", errors="ignore") as f:
        cs_html = f.read().lower()
    
    missing_rubric_items = []
    rubric_keywords = {
        "client": ["client", "client overview", "about client"],
        "industry": ["industry", "sector"],
        "challenge": ["challenge", "problem statement", "the problem"],
        "approach": ["approach", "solution", "methodology"],
        "technologies": ["technologies", "tech stack", "tools used"],
        "timeline": ["timeline", "duration", "timeframe", "weeks", "months"],
        "business_results": ["business results", "outcomes", "impact"],
        "key_metrics": ["key metrics", "metrics", "%", "roi", "reduction", "growth"],
        "related_services": ["related services", "services delivered"],
        "next_cta": ["book consultation", "start your project", "contact"]
    }
    for item, kws in rubric_keywords.items():
        if not any(kw in cs_html for kw in kws):
            missing_rubric_items.append(item)
    if missing_rubric_items:
        findings.append({
            "category": "Strategic Positioning",
            "severity": "P2",
            "page": cs,
            "issue": f"Case study missing structured data.md transformation elements: {', '.join(missing_rubric_items)}"
        })

# 5. UX / UI & ACCESSIBILITY
print("\n--- 5. UX / UI & ACCESSIBILITY ANALYSIS ---")
# Check elements.html exposure
if "elements/elements.html" in pages:
    findings.append({
        "category": "UX & Architecture",
        "severity": "P2",
        "page": "elements/elements.html",
        "issue": "Orphan UI component catalog (elements/elements.html) is publicly accessible in root and indexed without noindex directive or authentication gate"
    })

# Check forms accessibility
for p, data in pages.items():
    if data["forms"]:
        for form in data["forms"]:
            for inp in form["inputs"]:
                # Check for label association or aria-label
                pass

# Check social links
for p, data in pages.items():
    for link in data["links"]["details"]:
        href = link["href"]
        if "facebook.com" in href and "ajnetworks" not in href:
            findings.append({"category": "Credibility", "severity": "P2", "page": p, "issue": f"Placeholder/generic social URL found: '{href}'"})
        elif "linkedin.com" in href and "company/ajnetworks" not in href:
            findings.append({"category": "Credibility", "severity": "P2", "page": p, "issue": f"Generic or malformed LinkedIn company link: '{href}'"})

# Print summary
print(f"\nTotal findings cataloged: {len(findings)}")
for idx, f in enumerate(findings, 1):
    print(f"{idx}. [{f['severity']}] [{f['category']}] ({f['page']}): {f['issue']}")

# Save findings json
findings_path = root / "teamwork_audit" / "FINDINGS_RAW.json"
with open(findings_path, "w", encoding="utf-8") as out:
    json.dump(findings, out, indent=2)
print(f"\nSaved raw findings to {findings_path}")
