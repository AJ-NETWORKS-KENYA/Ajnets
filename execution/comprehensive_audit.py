import os, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(r"C:\My Web Sites\ajnets")
html_files = [f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

print(f"Total HTML files found: {len(html_files)}")

all_titles = {}
all_descriptions = {}

for hf in sorted(html_files):
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # Title
    title_tags = soup.find_all("title")
    titles = [t.get_text().strip() for t in title_tags]
    
    # Meta descriptions
    meta_descs = soup.find_all("meta", attrs={"name": re.compile(r"^description$", re.I)})
    descs = [m.get("content", "").strip() for m in meta_descs]
    
    all_titles[rel] = titles
    all_descriptions[rel] = descs
    
    # Check for corrupt characters
    has_corrupt_char = "\ufffd" in content
    
    # Check images
    img_tags = soup.find_all("img")
    missing_alt = [img for img in img_tags if not img.get("alt") or img.get("alt").strip() == ""]
    missing_lazy = [img for img in img_tags if img.get("loading") != "lazy"]
    
    print(f"\n[{rel}]")
    print(f"  Titles ({len(titles)}): {titles}")
    print(f"  Descriptions ({len(descs)}): {descs}")
    if has_corrupt_char:
        print("  WARNING: File contains corrupt/replacement characters ()")
    print(f"  Total Images: {len(img_tags)}, Missing Alt: {len(missing_alt)}, Missing Lazy: {len(missing_lazy)}")

print("\n" + "="*50)
# Check title uniqueness
title_to_pages = {}
for rel, titles in all_titles.items():
    for t in titles:
        title_to_pages.setdefault(t, []).append(rel)

print("DUPLICATE TITLES:")
for t, pages in title_to_pages.items():
    if len(pages) > 1:
        print(f"  Title: '{t}' in {pages}")

desc_to_pages = {}
for rel, descs in all_descriptions.items():
    for d in descs:
        desc_to_pages.setdefault(d, []).append(rel)

print("\nDUPLICATE DESCRIPTIONS:")
for d, pages in desc_to_pages.items():
    if len(pages) > 1:
        print(f"  Desc: '{d}' in {pages}")
