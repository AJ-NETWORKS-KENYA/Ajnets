import subprocess
import json
import time
import threading
import http.server
import socketserver
from pathlib import Path

PORT = 8092
ROOT = Path(r"C:\My Web Sites\ajnets")
TMP_DIR = ROOT / ".tmp"
TMP_DIR.mkdir(exist_ok=True)

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, format, *args):
        pass
    def handle(self):
        try:
            super().handle()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            pass

def start_server():
    httpd = ThreadingHTTPServer(("", PORT), QuietHandler)
    httpd.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(1)

print(f"[INFO] Server listening on port {PORT}")

PAGES = [
    {"name": "Home Page", "path": "index.html"},
    {"name": "Contact Page", "path": "company/book-consultation.html"},
    {"name": "Services Page", "path": "services/services.html"},
    {"name": "Client Success Page", "path": "portfolio/client-success.html"},
]

results = []

for page in PAGES:
    url = f"http://localhost:{PORT}/{page['path']}"
    slug = page["path"].replace("/", "_").replace(".html", "")
    report_json_path = TMP_DIR / f"lighthouse_{slug}.json"
    
    print(f"\n[INFO] Running Lighthouse audit on {page['name']} ({url})...")
    
    cmd = [
        "npx.cmd", "lighthouse", url,
        "--output=json",
        f"--output-path={report_json_path}",
        "--chrome-flags=--headless=new --no-sandbox --disable-gpu",
        "--only-categories=performance,accessibility,best-practices,seo",
        "--quiet",
    ]
    
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"[WARN] Lighthouse returned non-zero code {proc.returncode}: {proc.stderr[:200]}")
        
    if report_json_path.exists():
        with open(report_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        cats = data.get("categories", {})
        perf = int((cats.get("performance", {}).get("score") or 0) * 100)
        a11y = int((cats.get("accessibility", {}).get("score") or 0) * 100)
        bp = int((cats.get("best-practices", {}).get("score") or 0) * 100)
        seo = int((cats.get("seo", {}).get("score") or 0) * 100)
        
        audits = data.get("audits", {})
        fcp = audits.get("first-contentful-paint", {}).get("displayValue", "N/A")
        lcp = audits.get("largest-contentful-paint", {}).get("displayValue", "N/A")
        cls = audits.get("cumulative-layout-shift", {}).get("displayValue", "N/A")
        tbt = audits.get("total-blocking-time", {}).get("displayValue", "N/A")
        
        page_res = {
            "page": page["name"],
            "url": url,
            "performance": perf,
            "accessibility": a11y,
            "best_practices": bp,
            "seo": seo,
            "fcp": fcp,
            "lcp": lcp,
            "cls": cls,
            "tbt": tbt,
        }
        results.append(page_res)
        print(f"[RESULT] {page['name']}: Perf={perf} | A11y={a11y} | BestPractices={bp} | SEO={seo} | FCP={fcp} | LCP={lcp} | CLS={cls}")
    else:
        print(f"[ERROR] Lighthouse report not found at {report_json_path}")

# Write Markdown report
summary_md = [
    "# AJNETWORKS — SEO & Performance Regression Audit Summary\n",
    "| Page | Performance | Accessibility | Best Practices | SEO | FCP | LCP | CLS |",
    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
]

for r in results:
    summary_md.append(f"| **{r['page']}** | {r['performance']}/100 | {r['accessibility']}/100 | {r['best_practices']}/100 | {r['seo']}/100 | {r['fcp']} | {r['lcp']} | {r['cls']} |")

summary_text = "\n".join(summary_md)
with open(TMP_DIR / "regression_audit_report.md", "w", encoding="utf-8") as f:
    f.write(summary_text)

print("\n" + "="*60)
print(summary_text)
print("="*60)
