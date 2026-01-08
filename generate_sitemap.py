import os
import glob
from datetime import datetime

# Domain name
DOMAIN = "https://www.ajnetworkskenya.it.com"
DIRECTORY = r"c:\My Web Sites\ajnets"

# Template for sitemap
SITEMAP_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
SITEMAP_FOOTER = '</urlset>'

# Files to exclude
EXCLUDE_FILES = [
    "services-backup.html",
    "elements.html",  # Usually a style guide
]

def generate_sitemap():
    urls = []
    
    # Get all HTML files
    files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    
    for filepath in files:
        filename = os.path.basename(filepath)
        
        if filename in EXCLUDE_FILES:
            continue
            
        # Modify URL structure (remove .html for clean URLs)
        if filename == "index.html":
            url_path = ""
        else:
            url_path = filename.replace(".html", "")
            
        full_url = f"{DOMAIN}/{url_path}"
        
        # Get last modified time
        mod_time = os.path.getmtime(filepath)
        last_mod = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
        
        url_entry = f"""
  <url>
    <loc>{full_url}</loc>
    <lastmod>{last_mod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if filename == 'index.html' else '0.8'}</priority>
  </url>"""
        urls.append(url_entry)

    # Write sitemap.xml
    with open(os.path.join(DIRECTORY, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(SITEMAP_HEADER)
        f.write("".join(urls))
        f.write(SITEMAP_FOOTER)
        
    print(f"Sitemap generated with {len(urls)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
