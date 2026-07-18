import os
import re

ROOT_DIR = r"c:\My Web Sites\ajnets"

SOCIAL_TOPBAR_HTML = """<ul class="social-list">
<li><a aria-label="Facebook" href="https://facebook.com/ajnetworks" rel="noopener" target="_blank"><i class="fab fa-facebook-f"></i></a></li>
<li><a aria-label="LinkedIn" href="https://linkedin.com/company/ajnetworks" rel="noopener" target="_blank"><i class="fab fa-linkedin-in"></i></a></li>
<li><a aria-label="YouTube" href="https://www.youtube.com/@ajnets" rel="noopener" target="_blank"><i class="fab fa-youtube"></i></a></li>
<li><a aria-label="Pinterest" href="https://pinterest.com/ajnetworks" rel="noopener" target="_blank"><i class="fab fa-pinterest-p"></i></a></li>
</ul>"""

SOCIAL_FOOTER_HTML = """<ul class="social-list footer-social-list mt-3">
<li><a aria-label="Facebook" href="https://facebook.com/ajnetworks" rel="noopener" target="_blank"><i class="fab fa-facebook-f"></i></a></li>
<li><a aria-label="LinkedIn" href="https://linkedin.com/company/ajnetworks" rel="noopener" target="_blank"><i class="fab fa-linkedin-in"></i></a></li>
<li><a aria-label="YouTube" href="https://www.youtube.com/@ajnets" rel="noopener" target="_blank"><i class="fab fa-youtube"></i></a></li>
<li><a aria-label="Pinterest" href="https://pinterest.com/ajnetworks" rel="noopener" target="_blank"><i class="fab fa-pinterest-p"></i></a></li>
</ul>"""

SCHEMA_LD_JSON = """<!-- Schema.org Organization JSON-LD -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AJNETWORKS",
  "url": "https://ajnetworks.co",
  "logo": "https://ajnetworks.co/images/logo.svg",
  "description": "AJNETWORKS is an enterprise technology consultancy delivering strategic advisory, software engineering, cybersecurity, and IT infrastructure solutions across East Africa.",
  "email": "hello@ajnetworks.co",
  "telephone": "+254758238617",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Nairobi",
    "addressCountry": "KE"
  },
  "sameAs": [
    "https://facebook.com/ajnetworks",
    "https://linkedin.com/company/ajnetworks",
    "https://www.youtube.com/@ajnets",
    "https://pinterest.com/ajnetworks"
  ]
}
</script>"""

def get_all_html_files(root):
    html_files = []
    for dirpath, _, filenames in os.walk(root):
        if "node_modules" in dirpath or ".git" in dirpath:
            continue
        for f in filenames:
            if f.endswith(".html"):
                html_files.append(os.path.join(dirpath, f))
    return html_files

def update_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Update topbar social list
    if '<ul class="social-list">' in content:
        content = re.sub(r'<ul class="social-list">.*?</ul>', SOCIAL_TOPBAR_HTML, content, flags=re.DOTALL)
        modified = True

    # 2. Update/Inject Schema.org JSON-LD in <head>
    if "application/ld+json" in content:
        content = re.sub(r'<!-- Schema\.org Organization JSON-LD -->\s*<script type="application/ld\+json">.*?</script>', SCHEMA_LD_JSON, content, flags=re.DOTALL)
        content = re.sub(r'<script type="application/ld\+json">.*?</script>', SCHEMA_LD_JSON, content, flags=re.DOTALL)
        modified = True
    else:
        if "</head>" in content:
            content = content.replace("</head>", f"{SCHEMA_LD_JSON}\n</head>", 1)
            modified = True

    # 3. Update footer contact info to include social icons if not present
    if 'footer-contact-info' in content:
        if 'footer-social-list' in content:
            content = re.sub(r'<ul class="social-list footer-social-list.*?</ul>', SOCIAL_FOOTER_HTML, content, flags=re.DOTALL)
            modified = True
        else:
            # Inject right before Book Strategy Call button in footer
            content = re.sub(
                r'(<a [^>]*class="octf-btn octf-btn-primary[^"]*"[^>]*>Book Strategy Call</a>)',
                f'{SOCIAL_FOOTER_HTML}\n\\1',
                content
            )
            modified = True

    # 4. Replace any old email domain or non-canonical URLs
    if "ajnetworkskenya.it.com" in content:
        content = content.replace("ajnetworkskenya.it.com", "ajnetworks.co")
        modified = True
    if "hello&#64;ajnetworkskenya.it.com" in content:
        content = content.replace("hello&#64;ajnetworkskenya.it.com", "hello@ajnetworks.co")
        modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {file_path}")

def update_sitemap():
    sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace("https://www.ajnetworks.co", "https://ajnetworks.co")
        if new_content != content:
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated sitemap.xml: normalize domain to https://ajnetworks.co")

def update_robots():
    robots_path = os.path.join(ROOT_DIR, "robots.txt")
    if os.path.exists(robots_path):
        with open(robots_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace("https://www.ajnetworks.co/sitemap.xml", "https://ajnetworks.co/sitemap.xml")
        if new_content != content:
            with open(robots_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated robots.txt: normalize sitemap URL to https://ajnetworks.co/sitemap.xml")

def update_docs():
    data_md = os.path.join(ROOT_DIR, "data.md")
    if os.path.exists(data_md):
        with open(data_md, "r", encoding="utf-8") as f:
            content = f.read()
        if "Official Social Media Channels" not in content:
            content += """

---

# 24. Official Online Presence & Social Links

- **Official Website:** https://ajnetworks.co
- **Facebook:** https://facebook.com/ajnetworks
- **LinkedIn:** https://linkedin.com/company/ajnetworks
- **YouTube:** https://www.youtube.com/@ajnets
- **Pinterest:** https://pinterest.com/ajnetworks
"""
            with open(data_md, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated data.md with Official Social Links")

    design_md = os.path.join(ROOT_DIR, "design.md")
    if os.path.exists(design_md):
        with open(design_md, "r", encoding="utf-8") as f:
            content = f.read()
        if "https://facebook.com/ajnetworks" not in content:
            content += """

## Social Media & Brand Links
- **Website:** https://ajnetworks.co
- **Facebook:** https://facebook.com/ajnetworks
- **LinkedIn:** https://linkedin.com/company/ajnetworks
- **YouTube:** https://www.youtube.com/@ajnets
- **Pinterest:** https://pinterest.com/ajnetworks
"""
            with open(design_md, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated design.md with Official Social Links")

def update_python_scripts():
    standardize_nav = os.path.join(ROOT_DIR, "execution", "standardize_nav.py")
    if os.path.exists(standardize_nav):
        with open(standardize_nav, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("https://ajnetworkskenya.it.com", "https://ajnetworks.co")
        content = content.replace("hello&#64;ajnetworkskenya.it.com", "hello@ajnetworks.co")
        content = content.replace("hello@ajnetworkskenya.it.com", "hello@ajnetworks.co")
        with open(standardize_nav, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated execution/standardize_nav.py")

    rebuild_case_studies = os.path.join(ROOT_DIR, "execution", "rebuild_case_studies.py")
    if os.path.exists(rebuild_case_studies):
        with open(rebuild_case_studies, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("https://ajnetworkskenya.it.com", "https://ajnetworks.co")
        content = content.replace("hello&#64;ajnetworkskenya.it.com", "hello@ajnetworks.co")
        content = content.replace("hello@ajnetworkskenya.it.com", "hello@ajnetworks.co")
        with open(rebuild_case_studies, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated execution/rebuild_case_studies.py")

if __name__ == "__main__":
    html_files = get_all_html_files(ROOT_DIR)
    print(f"Found {len(html_files)} HTML files.")
    for f in html_files:
        update_html_file(f)
    update_sitemap()
    update_robots()
    update_docs()
    update_python_scripts()
    print("Done updating brand links across project.")
