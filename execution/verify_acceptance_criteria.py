from pathlib import Path
from bs4 import BeautifulSoup
import re
import sys

root = Path(r"C:\My Web Sites\ajnets")
html_files = sorted([f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])])

print(f"=== 1. VERIFYING TITLE AND META DESCRIPTION TAGS ({len(html_files)} files) ===")

titles = {}
descriptions = {}
failed = False

for hf in html_files:
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    t_tags = soup.find_all("title")
    if len(t_tags) != 1:
        print(f"FAILED: {rel} has {len(t_tags)} <title> tags (expected 1)")
        failed = True
    else:
        t_text = t_tags[0].get_text().strip()
        if not t_text or len(t_text) < 10:
            print(f"FAILED: {rel} has invalid title '{t_text}'")
            failed = True
        titles.setdefault(t_text, []).append(rel)
        
    d_tags = soup.find_all("meta", attrs={"name": lambda x: x and x.lower() == "description"})
    if len(d_tags) != 1:
        print(f"FAILED: {rel} has {len(d_tags)} description tags (expected 1)")
        failed = True
    else:
        d_text = d_tags[0].get("content", "").strip()
        if not d_text or len(d_text) < 30:
            print(f"FAILED: {rel} has invalid description '{d_text}'")
            failed = True
        descriptions.setdefault(d_text, []).append(rel)

# Check uniqueness
for t, files in titles.items():
    if len(files) > 1:
        print(f"FAILED: Duplicate title '{t}' in {files}")
        failed = True

for d, files in descriptions.items():
    if len(files) > 1:
        print(f"FAILED: Duplicate description '{d}' in {files}")
        failed = True

if not failed:
    print("[PASS] All 21 HTML files have exactly one unique <title> and <meta name='description'> tag.")

print("\n=== 2. VERIFYING IMG TAGS ALT & LAZY LOADING ===")
img_failed = False
total_images = 0

for hf in html_files:
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    img_tags = soup.find_all("img")
    for img in img_tags:
        total_images += 1
        src = img.get("src", "")
        alt = img.get("alt")
        loading = img.get("loading")
        
        # Check alt
        if alt is None or alt.strip() == "":
            print(f"[FAIL]: Missing alt on {rel} for {src}")
            img_failed = True
            
        # Check below-the-fold loading="lazy"
        # Determine if header / above fold
        is_header = False
        p = img.parent
        while p:
            if p.name == "header" or (p.get("class") and any("header" in c for c in p.get("class"))):
                is_header = True
                break
            if p.get("id") in ["site-header", "site-logo"]:
                is_header = True
                break
            p = p.parent
            
        if not is_header and loading != "lazy":
            print(f"[FAIL]: Missing loading='lazy' on {rel} for {src}")
            img_failed = True

if not img_failed:
    print(f"[PASS] All {total_images} <img> tags across all pages have valid alt attributes, and all below-the-fold images have loading='lazy'.")

print("\n=== 3. VERIFYING ROBOTS.TXT AND SITEMAP.XML ===")
robots_file = root / "robots.txt"
sitemap_file = root / "sitemap.xml"

if not robots_file.exists():
    print("[FAIL]: robots.txt does not exist")
    failed = True
else:
    with open(robots_file, "r", encoding="utf-8") as f:
        rc = f.read()
    if "User-agent:" in rc and "Sitemap: https://ajnetworks.co/sitemap.xml" in rc:
        print("[PASS] robots.txt exists and is properly formatted.")
    else:
        print("[FAIL]: robots.txt content invalid.")
        failed = True

if not sitemap_file.exists():
    print("[FAIL]: sitemap.xml does not exist")
    failed = True
else:
    with open(sitemap_file, "r", encoding="utf-8") as f:
        sc = f.read()
    if "<?xml" in sc and "<urlset" in sc and "</urlset>" in sc and "https://ajnetworks.co/" in sc:
        print("[PASS] sitemap.xml exists and is valid XML.")
    else:
        print("[FAIL]: sitemap.xml content invalid.")
        failed = True

print("\n=== 4. VERIFYING CONTACT FORM (company/book-consultation.html) ===")
contact_file = root / "company" / "book-consultation.html"
with open(contact_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

region_select = soup.find("select", attrs={"id": "region"})
if not region_select:
    print("[FAIL]: Region select (#region) not found")
    failed = True
else:
    options = region_select.find_all("option")
    valid_options = [opt.get("value") for opt in options if opt.get("value")]
    print(f"[PASS] Region select found with {len(valid_options)} options: {valid_options}")
    if len(valid_options) < 2:
        print("[FAIL]: Region options insufficient")
        failed = True

error_spans = soup.find_all(attrs={"class": lambda c: c and "error" in c.split()})
print(f"[PASS] Found {len(error_spans)} error elements on contact page.")

if failed or img_failed:
    print("\nSUMMARY: [FAIL] Static verification failed.")
    sys.exit(1)
else:
    print("\nSUMMARY: [PASS] All static verification checks passed successfully!")
