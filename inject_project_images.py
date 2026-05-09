import os
import re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")

# Map case study files to their uploaded image
page_image_map = {
    "case-study-audiophile.html": "images/projects/Audiophile.png",
    "case-study-transitflow.html": "images/projects/transit flow.png",
    "case-study-bada.html": "images/projects/bli.png",
    "case-study-racnyali.html": "images/projects/rotaract nyali.png",
}

for page, img_src in page_image_map.items():
    html_path = ROOT / page
    if not html_path.exists():
        print(f"File not found: {page}")
        continue
        
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    # Check if we already injected it
    if 'class="rounded-xl overflow-hidden shadow-2xl project-hero-img"' in html:
        print(f"Image already injected in {page}")
        continue
        
    # We want to inject the image right after the hero section, before <section class="py-20 reveal">
    # The hero section ends with </section>\n\n  <section class="py-20 reveal">
    
    img_block = f"""
  <section class="pb-16" style="border-bottom:1px solid #1e2d4a; margin-top:-2rem;">
    <div class="max-w-6xl mx-auto px-6 reveal">
      <div class="rounded-xl overflow-hidden shadow-2xl project-hero-img" style="border: 1px solid #1e2d4a; background: #080c18;">
        <img src="{img_src}" alt="Project preview" class="w-full h-auto object-cover" loading="lazy" />
      </div>
    </div>
  </section>

"""
    
    # regex to find the boundary between hero and content sections
    pattern = r'(</section>)\s*(<section class="py-20 reveal"|<section class="py-20 reveal">)'
    html_new = re.sub(pattern, r'\1\n' + img_block + r'  \2', html, count=1)
    
    if html_new != html:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_new)
        print(f"Injected image into {page}")
    else:
        print(f"Could not find insertion point in {page}")

print("Done.")
