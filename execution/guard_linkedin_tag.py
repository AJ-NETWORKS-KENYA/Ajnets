import re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")
HTML_FILES = [f for f in ROOT.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

old_pattern = re.compile(
    r'<!--\s*LinkedIn\s*Insight\s*Tag\s*-->\s*<script[^>]*>\s*_linkedin_partner_id\s*=\s*"YOUR_LINKEDIN_PID";[\s\S]*?<\/noscript>',
    re.I
)

guarded_tag = '''<!-- LinkedIn Insight Tag -->
<script type="text/javascript">
      _linkedin_partner_id = "YOUR_LINKEDIN_PID";
      if (_linkedin_partner_id && _linkedin_partner_id !== "YOUR_LINKEDIN_PID") {
        window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
        window._linkedin_data_partner_ids.push(_linkedin_partner_id);
        (function (l) {
          if (!l) {
            window.lintrk = function (a, b) {
              window.lintrk.q.push([a, b]);
            };
            window.lintrk.q = [];
          }
          var s = document.getElementsByTagName("script")[0];
          var b = document.createElement("script");
          b.type = "text/javascript";
          b.async = true;
          b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
          s.parentNode.insertBefore(b, s);
        })(window.lintrk);
      }
    </script>'''

for hf in HTML_FILES:
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    if old_pattern.search(content):
        content = old_pattern.sub(guarded_tag, content)
        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [GUARDED]: {hf.relative_to(ROOT)}")
    else:
        print(f"  [SKIPPED]: {hf.relative_to(ROOT)}")

print("\nLinkedIn tag guard completed.")
