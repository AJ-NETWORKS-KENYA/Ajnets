import os, re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")
HTML_FILES = [f for f in ROOT.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

print(f"Processing {len(HTML_FILES)} HTML files...")

# Regex to find placeholder G-XXXXXXXXXX block
gtag_placeholder_re = re.compile(
    r'<!--\s*Google\s*tag\s*\(gtag\.js\)\s*-->\s*<script[^>]*src="https://www\.googletagmanager\.com/gtag/js\?id=G-XXXXXXXXXX"[^>]*></script>\s*<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*function\s*gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\(\'js\',\s*new\s*Date\(\)\);\s*gtag\(\'config\',\s*\'G-XXXXXXXXXX\'\);\s*</script>\s*',
    re.I | re.S
)

for hf in HTML_FILES:
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    original = content
    
    # 1. Remove duplicate G-XXXXXXXXXX block
    content = gtag_placeholder_re.sub("", content)
    
    # Fallback pattern if spacing varies
    content = re.sub(r'<!-- Google tag \(gtag\.js\) -->\s*<script[^>]*G-XXXXXXXXXX[^<]*</script>\s*<script>[\s\S]*?gtag\(\'config\',\s*\'G-XXXXXXXXXX\'\);\s*</script>', '', content)
    
    # 2. Remove unused scripts from HTML footer
    content = re.sub(r'\s*<script[^>]*src="/js/easypiechart\.min\.js"[^>]*></script>', '', content)
    content = re.sub(r'\s*<script[^>]*src="/js/jquery\.countdown\.min\.js"[^>]*></script>', '', content)
    content = re.sub(r'\s*<script[^>]*src="/js/Drift\.min\.js"[^>]*></script>', '', content)
    content = re.sub(r'\s*<script[^>]*src="/js/royal_preloader\.min\.js"[^>]*></script>', '', content)
    
    if content != original:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [CLEANED]: {hf.relative_to(ROOT)}")
    else:
        print(f"  [NO CHANGE]: {hf.relative_to(ROOT)}")

# Delete unreferenced script files from js/
UNUSED_JS = [
    ROOT / "js" / "easypiechart.min.js",
    ROOT / "js" / "jquery.countdown.min.js",
    ROOT / "js" / "jquery.singlePageNav.js",
    ROOT / "js" / "rev-script-2.js",
    ROOT / "js" / "rev-script-3.js",
    ROOT / "js" / "royal_preloader.min.js",
    ROOT / "js" / "Drift.min.js"
]

print("\nCleaning unused JS files...")
for js_file in UNUSED_JS:
    if js_file.exists():
        js_file.unlink()
        print(f"  [DELETED]: {js_file.name}")
    else:
        print(f"  [ALREADY REMOVED]: {js_file.name}")

print("\nOptimization and cleanup complete.")
