from pathlib import Path
from bs4 import BeautifulSoup

root = Path(r"C:\My Web Sites\ajnets")
html_files = [f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

for hf in sorted(html_files):
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    title = soup.find("title")
    meta_desc = soup.find("meta", attrs={"name": lambda x: x and x.lower() == "description"})
    og_title = soup.find("meta", attrs={"property": "og:title"})
    og_desc = soup.find("meta", attrs={"property": "og:description"})
    tw_title = soup.find("meta", attrs={"name": "twitter:title"})
    tw_desc = soup.find("meta", attrs={"name": "twitter:description"})
    
    print(f"{rel}:")
    print(f"  title:    {title.get_text() if title else 'MISSING'}")
    print(f"  desc:     {meta_desc.get('content') if meta_desc else 'MISSING'}")
    print(f"  og:title: {og_title.get('content') if og_title else 'MISSING'}")
    print(f"  og:desc:  {og_desc.get('content') if og_desc else 'MISSING'}")
    print(f"  tw:title: {tw_title.get('content') if tw_title else 'MISSING'}")
    print(f"  tw:desc:  {tw_desc.get('content') if tw_desc else 'MISSING'}")
