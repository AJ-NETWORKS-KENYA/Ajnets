import re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")
path = ROOT / "client-success.html"

with open(path, encoding="utf-8") as f:
    html = f.read()

crappo_card = """
        <!-- Crappo -->
        <div class="card-glow rounded-xl overflow-hidden" style="background: #0f1628;">
          <div class="h-2" style="background: linear-gradient(90deg,#0052ff,#00d4ff);"></div>
          <div class="p-6">
            <div class="flex items-start justify-between mb-4">
              <div class="w-10 h-10 rounded-lg flex items-center justify-center text-lg" style="background: rgba(0,82,255,0.12); color: #0084ff;">
                <i class="fab fa-bitcoin"></i>
              </div>
              <span class="tag-pill" style="background: rgba(0,82,255,0.1); color: #0084ff;">FinTech / Crypto</span>
            </div>
            <h3 class="text-lg font-bold text-white mb-2">Crappo Crypto Platform</h3>
            <p class="text-sm text-slate-400 mb-4 leading-relaxed">A modern, high-performance cryptocurrency investment platform featuring live market data integration, secure wallet connections, and sleek dark-mode UI components.</p>
            <div class="flex flex-wrap gap-2 mb-5">
              <span class="tech-badge"><i class="fab fa-react"></i> React</span>
              <span class="tech-badge">TailwindCSS</span>
              <span class="tech-badge">Figma</span>
            </div>
            <div class="flex items-center justify-between pt-4" style="border-top: 1px solid #1e2d4a;">
              <a href="case-study-crappo.html" class="text-xs font-semibold text-cyber-blue hover:text-white transition">Read Case Study →</a>
              <span class="text-xs font-mono text-slate-500">Internal Engineering</span>
            </div>
          </div>
        </div>
"""

# Insert it before Green Remedies
# We can look for `<!-- Green Remedies -->`
html_new = html.replace('<!-- Green Remedies -->', crappo_card + '\n        <!-- Green Remedies -->', 1)

if html_new != html:
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_new)
    print("Crappo added to client-success.html")
else:
    print("Failed to add Crappo.")
