import re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")
path = ROOT / "case-study-greenremedies.html"

with open(path, encoding="utf-8") as f:
    html = f.read()

img_block = """
  <section class="pb-16" style="border-bottom:1px solid #1e2d4a; margin-top:-2rem;">
    <div class="max-w-6xl mx-auto px-6 reveal">
      <div class="rounded-xl overflow-hidden shadow-2xl project-hero-img" style="border: 1px solid #1e2d4a; background: #080c18;">
        <img src="images/projects/foodEX.png" alt="Project preview" class="w-full h-auto object-cover" loading="lazy" />
      </div>
    </div>
  </section>
"""

html_new = re.sub(
    r'(</section>)\s*(<section class="py-20 reveal"[^>]*>|<section class="py-20 reveal">)',
    r'\1\n' + img_block + r'  \2',
    html,
    count=1
)

if html_new != html:
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_new)
    print("foodEX.png injected into Green Remedies.")
else:
    print("Failed to inject.")
