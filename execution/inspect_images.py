import os, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(r"C:\My Web Sites\ajnets")
html_files = [f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

for hf in sorted(html_files):
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    img_tags = soup.find_all("img")
    
    print(f"\n==========================================")
    print(f"FILE: {rel} ({len(img_tags)} images)")
    print(f"==========================================")
    
    for idx, img in enumerate(img_tags):
        src = img.get("src", "")
        alt = img.get("alt", "")
        loading = img.get("loading", "")
        parent_tag = img.parent.name if img.parent else ""
        parent_class = img.parent.get("class", []) if img.parent else []
        
        # Check if alt is missing or empty
        is_alt_missing = (alt is None or alt.strip() == "")
        is_lazy = (loading == "lazy")
        
        print(f"  [{idx+1}] src='{src}' | alt='{alt}' | loading='{loading}' | parent=<{parent_tag} class='{' '.join(parent_class)}'>")
