from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path(r"C:\My Web Sites\ajnets")
html_files = [f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

# Dictionary mapping image src filenames / patterns to descriptive alt text
ALT_MAP = {
    "logo.svg": "AJNETWORKS Logo",
    "favicon.svg": "AJNETWORKS Favicon",
    "favicon-96x96.png": "AJNETWORKS Icon",
    "apple-touch-icon.png": "AJNETWORKS Apple Touch Icon",
    "Rotaract Club of Nyali Logo(Cranberry)_EN21.png": "Rotaract Club of Nyali Logo",
    "BLI logoo.png": "Bada Language Institute Logo",
    "sgss-mombasa-logo.png": "Siri Guru Singh Sabha Mombasa Logo",
    "sgss-medical-fund-logo.png": "SGSS Medical Fund Logo",
    "client3.svg": "Enterprise Client Partner Logo",
    "client4.png": "Corporate Technology Partner Logo",
    "client5.svg": "Strategic Industry Partner Logo",
    "client6.svg": "Global Infrastructure Partner Logo",
    "support1.jpg": "Strategic Partner Collaboration Support",
    "support2.jpg": "Customer Operations and Support",
    "support3.jpg": "Startup Incubation and Technology Enablement",
    "testi1.png": "Client Testimonial Avatar",
    "testi2.png": "Enterprise Client Testimonial Avatar",
    "blog4.jpg": "Strategic Technology Consulting Insights",
    "blog-single-1.jpg": "Strategic Planning and Digital Architecture",
    "AJ-widget.jpg": "Abraham John - Technology Consultant",
    "recent-img-1.jpg": "Recent Technology Strategy Insight",
    "recent-img-2.jpg": "Cloud Infrastructure Architecture Insight",
    "recent-img-3.jpg": "Cybersecurity & Assurance Insight",
    "relate-img-1.jpg": "Related Insight on Enterprise Systems",
    "relate-img-2.jpg": "Related Insight on Digital Transformation",
    "comment-1.jpg": "Michael Ross - Commenter Avatar",
    "comment-2.jpg": "Sarah Jenkins - Commenter Avatar",
    "ft-gallery-1.jpg": "AJNETWORKS Engineering Gallery 1",
    "ft-gallery-2.jpg": "AJNETWORKS Engineering Gallery 2",
    "ft-gallery-3.jpg": "AJNETWORKS Engineering Gallery 3",
    "ft-gallery-4.jpg": "AJNETWORKS Engineering Gallery 4",
    "ft-gallery-5.jpg": "AJNETWORKS Engineering Gallery 5",
    "ft-gallery-6.jpg": "AJNETWORKS Engineering Gallery 6",
    "project-720x520.jpg": "Rotaract Club of Nyali Community Portal Showcase",
    "project3-720x520.jpg": "SGSS Mombasa Medical Fund Portal Showcase",
    "project4-720x520.jpg": "Crappo Crypto Investment Platform Showcase",
    "project7-720x520.jpg": "Bada Language Institute LMS Showcase",
    "project8-720x520.jpg": "Audiophile E-Commerce Platform Showcase",
    "project1-720x720.jpg": "Technology Strategy Case Study Showcase",
    "project2-720x720.jpg": "Digital Transformation Case Study Showcase",
    "project3-720x720.jpg": "AI & Process Automation Case Study Showcase",
}

for hf in sorted(html_files):
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    img_tags = soup.find_all("img")
    
    modified = False
    for img in img_tags:
        src = img.get("src", "")
        alt = img.get("alt", "")
        
        # Determine if image is in header / above the fold
        is_in_header = False
        p = img.parent
        while p:
            if p.name == "header" or (p.get("class") and any("header" in c for c in p.get("class"))):
                is_in_header = True
                break
            if p.get("id") in ["site-header", "site-logo"]:
                is_in_header = True
                break
            p = p.parent
            
        # 1. Alt tag handling
        filename = src.split("/")[-1].split("?")[0]
        if not alt or alt.strip() == "":
            if filename in ALT_MAP:
                img["alt"] = ALT_MAP[filename]
                modified = True
            elif "linkedin" in src.lower():
                img["alt"] = "LinkedIn Tracking Pixel"
                modified = True
            else:
                clean_name = filename.rsplit(".", 1)[0].replace("-", " ").replace("_", " ").title()
                img["alt"] = f"AJNETWORKS {clean_name}"
                modified = True
        elif is_in_header and (alt == "Engitech" or alt == ""):
            img["alt"] = "AJNETWORKS"
            modified = True
            
        # 2. Loading="lazy" handling for below-the-fold images
        if not is_in_header:
            if img.get("loading") != "lazy":
                img["loading"] = "lazy"
                modified = True
                
    if modified:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Updated images in {rel}")
    else:
        print(f"No image changes needed in {rel}")

print("\nImage optimization complete.")
