import os
from bs4 import BeautifulSoup

# 1. Update style.css
css_path = r"c:\My Web Sites\ajnets\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace the accent colors in octf-btn-primary
old_btn = """/* Standardized Buttons */
.octf-btn-primary {
    background-color: var(--ajn-accent) !important;
    color: var(--ajn-navy) !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
}

.octf-btn-primary:hover {
    background-color: #38bfa0 !important;
    color: var(--ajn-navy) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(67, 217, 173, 0.3);
}"""

new_btn = """/* Standardized Buttons */
.octf-btn-primary {
    background-color: var(--ajn-blue) !important;
    color: var(--ajn-white) !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
}

.octf-btn-primary:hover {
    background-color: var(--ajn-navy) !important;
    color: var(--ajn-white) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(43, 59, 133, 0.3);
}"""

if old_btn in css_content:
    css_content = css_content.replace(old_btn, new_btn)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated style.css button colors")

# 2. Update index.html
index_path = r"c:\My Web Sites\ajnets\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the Trusted Technologies section
# It has text "Trusted Technologies & Platforms"
trusted_section = None
for div in soup.find_all("div", class_="padding-half bg-light-1"):
    if "Trusted Technologies & Platforms" in div.get_text():
        trusted_section = div
        break

if trusted_section:
    trusted_section.extract()
    # Insert it before footer
    footer = soup.find("footer", id="site-footer")
    if footer:
        footer.insert_before(trusted_section)
        print("Moved Trusted Technologies section to bottom")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

# 3. Fix CTA links across all HTML files
root_dir = r"c:\My Web Sites\ajnets"
count = 0
for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "execution", ".tmp")]
    for fname in filenames:
        if fname.endswith(".html"):
            fpath = os.path.join(dirpath, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            # Ensure proper links on CTA buttons
            new_content = new_content.replace('href="/company/book-consultation"', 'href="/company/book-consultation.html"')
            new_content = new_content.replace('href="/services/services"', 'href="/services/services.html"')
            new_content = new_content.replace('href="/portfolio/client-success"', 'href="/portfolio/client-success.html"')
            
            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1

print(f"Fixed CTA links in {count} files.")
