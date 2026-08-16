import os, re
from pathlib import Path

root = Path(r"C:\My Web Sites\ajnets")
html_files = [f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

print(f"Total HTML files found: {len(html_files)}")

all_titles = {}
all_descriptions = {}
title_counts = {}
desc_counts = {}

for hf in sorted(html_files):
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    titles = re.findall(r"<title>(.*?)</title>", content, re.I | re.S)
    
    # regex for meta description
    # matches <meta ... name="description" ... content="..." ...> or <meta ... content="..." ... name="description" ...>
    desc_matches = re.findall(r'<meta\s+[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']|<meta\s+[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', content, re.I | re.S)
    descs = [m[0] or m[1] for m in desc_matches]
    
    all_titles[rel] = titles
    all_descriptions[rel] = descs
    
    print(f"\n[{rel}]")
    print(f"  Count titles: {len(titles)}")
    for t in titles:
        print(f"    Title: {t.strip()}")
        title_counts[t.strip()] = title_counts.get(t.strip(), 0) + 1
        
    print(f"  Count descriptions: {len(descs)}")
    for d in descs:
        print(f"    Desc: {d.strip()}")
        desc_counts[d.strip()] = desc_counts.get(d.strip(), 0) + 1

print("\n" + "="*50)
print("DUPLICATE TITLES:")
for t, c in title_counts.items():
    if c > 1:
        print(f"  ({c}x) {t}")

print("\nDUPLICATE DESCRIPTIONS:")
for d, c in desc_counts.items():
    if c > 1:
        print(f"  ({c}x) {d}")
