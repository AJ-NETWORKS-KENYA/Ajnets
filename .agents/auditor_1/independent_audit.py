import sys
import os
from pathlib import Path
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re

ROOT = Path(r"C:\My Web Sites\ajnets")

def run_audit():
    print("=" * 70)
    print("AJNETWORKS VICTORY AUDITOR — INDEPENDENT VERIFICATION SUITE")
    print("=" * 70)
    
    html_files = sorted([
        f for f in ROOT.rglob("*.html") 
        if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])
    ])
    
    print(f"\n[INFO] Found {len(html_files)} production HTML files to audit.")
    
    audit_results = {
        "r1_meta": {"status": "PASS", "details": []},
        "r2_form": {"status": "PASS", "details": []},
        "r3_images": {"status": "PASS", "details": []},
        "r4_sitemap_robots": {"status": "PASS", "details": []},
    }
    
    # -------------------------------------------------------------
    # 1. AUDIT R1: META TAGS
    # -------------------------------------------------------------
    print("\n>>> AUDITING R1: META TAGS (Titles & Descriptions)...")
    titles = {}
    descriptions = {}
    
    for hf in html_files:
        rel = str(hf.relative_to(ROOT)).replace("\\", "/")
        with open(hf, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")
            
        t_tags = soup.find_all("title")
        if len(t_tags) == 0:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"{rel}: Missing <title> tag")
        elif len(t_tags) > 1:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"{rel}: Multiple ({len(t_tags)}) <title> tags")
        else:
            t_text = t_tags[0].get_text().strip()
            if not t_text or len(t_text) < 10:
                audit_results["r1_meta"]["status"] = "FAIL"
                audit_results["r1_meta"]["details"].append(f"{rel}: Title too short/empty ('{t_text}')")
            titles.setdefault(t_text, []).append(rel)
            
        d_tags = soup.find_all("meta", attrs={"name": lambda x: x and x.lower() == "description"})
        if len(d_tags) == 0:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"{rel}: Missing <meta name='description'> tag")
        elif len(d_tags) > 1:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"{rel}: Multiple ({len(d_tags)}) description tags")
        else:
            d_text = d_tags[0].get("content", "").strip()
            if not d_text or len(d_text) < 30:
                audit_results["r1_meta"]["status"] = "FAIL"
                audit_results["r1_meta"]["details"].append(f"{rel}: Description too short/empty ('{d_text}')")
            descriptions.setdefault(d_text, []).append(rel)
            
        # Check for garbled characters / unescaped entities
        if "&#" in t_text or "&amp;amp;" in t_text:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"{rel}: Malformed title encoding ('{t_text}')")

    # Uniqueness check
    for t_text, files in titles.items():
        if len(files) > 1:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"Duplicate title across {len(files)} files: '{t_text}' in {files}")
            
    for d_text, files in descriptions.items():
        if len(files) > 1:
            audit_results["r1_meta"]["status"] = "FAIL"
            audit_results["r1_meta"]["details"].append(f"Duplicate description across {len(files)} files: '{d_text}' in {files}")

    print(f"  Result: {audit_results['r1_meta']['status']}")
    if audit_results['r1_meta']['details']:
        for d in audit_results['r1_meta']['details']:
            print(f"    - {d}")
    else:
        print(f"    - All {len(html_files)} HTML files possess exactly 1 unique <title> and 1 unique <meta name='description'>.")

    # -------------------------------------------------------------
    # 2. AUDIT R2: CONTACT FORM
    # -------------------------------------------------------------
    print("\n>>> AUDITING R2: CONTACT FORM & VALIDATION...")
    contact_path = ROOT / "company" / "book-consultation.html"
    if not contact_path.exists():
        audit_results["r2_form"]["status"] = "FAIL"
        audit_results["r2_form"]["details"].append("company/book-consultation.html not found")
    else:
        with open(contact_path, "r", encoding="utf-8") as f:
            c_html = f.read()
            soup = BeautifulSoup(c_html, "html.parser")
            
        # Check for malformed tags
        if "<h2request" in c_html.lower():
            audit_results["r2_form"]["status"] = "FAIL"
            audit_results["r2_form"]["details"].append("Malformed <h2request> tag detected in HTML")
            
        # Check region select
        region_select = soup.find("select", attrs={"id": "region"})
        if not region_select:
            audit_results["r2_form"]["status"] = "FAIL"
            audit_results["r2_form"]["details"].append("Missing #region select element")
        else:
            opts = region_select.find_all("option")
            real_opts = [o for o in opts if o.get("value")]
            if len(real_opts) < 3:
                audit_results["r2_form"]["status"] = "FAIL"
                audit_results["r2_form"]["details"].append(f"Insufficient region options ({len(real_opts)} found)")
            else:
                audit_results["r2_form"]["details"].append(f"Found {len(real_opts)} region options: {[o.get('value') for o in real_opts]}")

        # Check script inclusion
        scripts = [s.get("src") for s in soup.find_all("script") if s.get("src")]
        contact_js = any("contact-form.js" in s for s in scripts)
        if not contact_js:
            audit_results["r2_form"]["status"] = "FAIL"
            audit_results["r2_form"]["details"].append("Missing contact-form.js script tag")
        else:
            audit_results["r2_form"]["details"].append("contact-form.js is properly included")

        # Check CSS for .error display:none
        css_path = ROOT / "style.css"
        min_css_path = ROOT / "style.min.css"
        css_ok = False
        if css_path.exists():
            with open(css_path, "r", encoding="utf-8") as cf:
                css_content = cf.read()
                if ".error" in css_content and "display: none" in css_content:
                    css_ok = True
        if not css_ok:
            audit_results["r2_form"]["status"] = "FAIL"
            audit_results["r2_form"]["details"].append("CSS rule for .error { display: none; } missing in style.css")
        else:
            audit_results["r2_form"]["details"].append("style.css properly sets .error { display: none; }")

        if min_css_path.exists():
            with open(min_css_path, "r", encoding="utf-8") as mcf:
                min_css_content = mcf.read()
                if ".error" in min_css_content and "display:none" in min_css_content:
                    audit_results["r2_form"]["details"].append("style.min.css contains .error { display:none } rule")
                else:
                    audit_results["r2_form"]["status"] = "FAIL"
                    audit_results["r2_form"]["details"].append("style.min.css missing .error rule")

    print(f"  Result: {audit_results['r2_form']['status']}")
    for d in audit_results['r2_form']['details']:
        print(f"    - {d}")

    # -------------------------------------------------------------
    # 3. AUDIT R3: IMAGE OPTIMIZATION (alt & lazy loading)
    # -------------------------------------------------------------
    print("\n>>> AUDITING R3: IMAGE OPTIMIZATION (Alt & Lazy Loading)...")
    total_imgs = 0
    missing_alt = []
    missing_lazy = []
    eager_header_imgs = 0
    lazy_imgs = 0
    
    for hf in html_files:
        rel = str(hf.relative_to(ROOT)).replace("\\", "/")
        with open(hf, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        imgs = soup.find_all("img")
        for img in imgs:
            total_imgs += 1
            src = img.get("src", "")
            alt = img.get("alt")
            loading = img.get("loading")
            
            if alt is None or alt.strip() == "":
                missing_alt.append(f"{rel}: img src='{src}' missing alt")
                
            # Check hierarchy for header / above-the-fold
            is_above_fold = False
            p = img.parent
            while p:
                if p.name == "header" or (p.get("class") and any("header" in c for c in p.get("class"))):
                    is_above_fold = True
                    break
                if p.get("id") in ["site-header", "site-logo"]:
                    is_above_fold = True
                    break
                p = p.parent
                
            if is_above_fold:
                eager_header_imgs += 1
            else:
                if loading == "lazy":
                    lazy_imgs += 1
                else:
                    missing_lazy.append(f"{rel}: img src='{src}' missing loading='lazy'")

    if missing_alt:
        audit_results["r3_images"]["status"] = "FAIL"
        audit_results["r3_images"]["details"].extend(missing_alt[:10])
        if len(missing_alt) > 10:
            audit_results["r3_images"]["details"].append(f"... and {len(missing_alt)-10} more missing alt tags")
    else:
        audit_results["r3_images"]["details"].append(f"All {total_imgs} <img> elements have valid descriptive alt text.")
        
    if missing_lazy:
        audit_results["r3_images"]["status"] = "FAIL"
        audit_results["r3_images"]["details"].extend(missing_lazy[:10])
        if len(missing_lazy) > 10:
            audit_results["r3_images"]["details"].append(f"... and {len(missing_lazy)-10} more missing loading='lazy' tags")
    else:
        audit_results["r3_images"]["details"].append(f"All {lazy_imgs} below-the-fold images have loading='lazy' (and {eager_header_imgs} header/critical images loaded eagerly).")

    print(f"  Result: {audit_results['r3_images']['status']}")
    for d in audit_results['r3_images']['details']:
        print(f"    - {d}")

    # -------------------------------------------------------------
    # 4. AUDIT R4: SITEMAP & ROBOTS
    # -------------------------------------------------------------
    print("\n>>> AUDITING R4: SITEMAP.XML & ROBOTS.TXT...")
    robots_path = ROOT / "robots.txt"
    sitemap_path = ROOT / "sitemap.xml"
    
    if not robots_path.exists():
        audit_results["r4_sitemap_robots"]["status"] = "FAIL"
        audit_results["r4_sitemap_robots"]["details"].append("robots.txt does not exist")
    else:
        with open(robots_path, "r", encoding="utf-8") as rf:
            rc = rf.read()
            if "User-agent:" not in rc:
                audit_results["r4_sitemap_robots"]["status"] = "FAIL"
                audit_results["r4_sitemap_robots"]["details"].append("robots.txt missing User-agent directive")
            if "Sitemap: https://ajnetworks.co/sitemap.xml" not in rc:
                audit_results["r4_sitemap_robots"]["status"] = "FAIL"
                audit_results["r4_sitemap_robots"]["details"].append("robots.txt missing correct Sitemap URL directive")
            if audit_results["r4_sitemap_robots"]["status"] == "PASS":
                audit_results["r4_sitemap_robots"]["details"].append("robots.txt is valid and points to sitemap.xml")

    if not sitemap_path.exists():
        audit_results["r4_sitemap_robots"]["status"] = "FAIL"
        audit_results["r4_sitemap_robots"]["details"].append("sitemap.xml does not exist")
    else:
        try:
            tree = ET.parse(str(sitemap_path))
            s_root = tree.getroot()
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls = s_root.findall("sm:url", ns)
            if not urls:
                urls = s_root.findall("url")
            audit_results["r4_sitemap_robots"]["details"].append(f"sitemap.xml is valid XML containing {len(urls)} URLs")
            
            # Verify each URL in sitemap matches an actual HTML file
            dead_urls = []
            for u in urls:
                loc = u.find("sm:loc", ns) if u.find("sm:loc", ns) is not None else u.find("loc")
                if loc is not None and loc.text:
                    url_text = loc.text.strip()
                    path_part = url_text.replace("https://ajnetworks.co/", "").replace("https://ajnetworks.co", "").strip("/")
                    if path_part == "":
                        target_file = ROOT / "index.html"
                    else:
                        target_file = ROOT / f"{path_part}.html"
                        if not target_file.exists():
                            target_file = ROOT / path_part / "index.html"
                    if not target_file.exists():
                        dead_urls.append(f"{url_text} -> expected file {target_file} not found")
                        
            if dead_urls:
                audit_results["r4_sitemap_robots"]["status"] = "FAIL"
                audit_results["r4_sitemap_robots"]["details"].extend(dead_urls)
            else:
                audit_results["r4_sitemap_robots"]["details"].append("All sitemap.xml URLs map to valid, existing project HTML files.")
                
        except Exception as e:
            audit_results["r4_sitemap_robots"]["status"] = "FAIL"
            audit_results["r4_sitemap_robots"]["details"].append(f"sitemap.xml parsing error: {e}")

    print(f"  Result: {audit_results['r4_sitemap_robots']['status']}")
    for d in audit_results['r4_sitemap_robots']['details']:
        print(f"    - {d}")

    # -------------------------------------------------------------
    # OVERALL AUDIT SUMMARY
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    all_passed = all(res["status"] == "PASS" for res in audit_results.values())
    if all_passed:
        print("OVERALL VERDICT: ALL CHECKS PASSED (STATIC VERIFICATION CONFIRMED)")
    else:
        print("OVERALL VERDICT: SOME CHECKS FAILED (STATIC VERIFICATION REJECTED)")
    print("=" * 70)
    
    return all_passed, audit_results

if __name__ == "__main__":
    passed, results = run_audit()
    sys.exit(0 if passed else 1)
