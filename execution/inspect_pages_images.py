import os, re
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(r"C:\My Web Sites\ajnets")
pages_to_check = [
    "index.html",
    "company/about-us.html",
    "company/faq.html",
    "company/book-consultation.html",
    "elements/elements.html",
    "insights/insights.html",
    "insights/post.html",
]

for p in pages_to_check:
    hf = root / p
    rel = p
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
        print(f"  [{idx+1}] src='{src}' | alt='{alt}' | loading='{loading}' | parent=<{parent_tag} class='{' '.join(parent_class)}'>")
