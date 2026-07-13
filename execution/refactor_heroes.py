"""
Phase 6: Standardize service page heroes.
Replaces inline-styled heroes with the page-hero component class.
"""
import os
import re
from bs4 import BeautifulSoup

ROOT = r"c:\My Web Sites\ajnets\services"

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the Hero Section comment
    if "<!-- Hero Section -->" not in content:
        return False
        
    soup = BeautifulSoup(content, "html.parser")
    
    # We are looking for the section with padding 120px...
    sections = soup.find_all("section")
    hero_section = None
    for sec in sections:
        style = sec.get("style", "")
        if "120px 0 80px 0" in style or "linear-gradient" in style:
            hero_section = sec
            break
            
    if not hero_section:
        return False
        
    # Extract data
    subtitle_span = hero_section.find("span")
    subtitle = subtitle_span.text.strip().replace("//", "").strip() if subtitle_span else ""
    
    h1 = hero_section.find("h1")
    title = h1.text.strip() if h1 else ""
    
    p = hero_section.find("p")
    desc = p.text.strip() if p else ""
    
    # If it's services.html, Breadcrumb is "Home / Services"
    # Else "Home / Services / [TITLE]"
    filename = os.path.basename(filepath)
    if filename == "services.html":
        breadcrumb = f'''
          <nav class="breadcrumb-nav" aria-label="Breadcrumb">
            <a href="/">Home</a>
            <span class="separator">/</span>
            <span class="current">Services</span>
          </nav>'''
        current = "Services"
    else:
        breadcrumb = f'''
          <nav class="breadcrumb-nav" aria-label="Breadcrumb">
            <a href="/">Home</a>
            <span class="separator">/</span>
            <a href="/services/services">Services</a>
            <span class="separator">/</span>
            <span class="current">{title}</span>
          </nav>'''
          
    new_hero = f'''
      <!-- Page Hero -->
      <div class="page-hero bg-dark-primary">
        <div class="container">{breadcrumb}
          <h1 class="text-white mt-3">{title}</h1>
          <p style="color: rgba(255,255,255,0.75); font-size: 17px; max-width: 600px; margin-top: 15px;">
            {desc}
          </p>
        </div>
      </div>
'''

    # Replace the old section with the new hero
    new_html = str(soup)
    old_section_html = str(hero_section)
    
    # Find the old section in the original string to preserve formatting where possible
    # bs4 can mess up some formatting
    
    start_idx = content.find("<!-- Hero Section -->")
    if start_idx != -1:
        # Find the end of the section tag
        # We know it's a section, so let's find the closing tag
        # Since bs4 parsed it, we can use regex to replace
        pattern = r'<!-- Hero Section -->\s*<section.*?style="[^"]*120px.*?</section>'
        new_content = re.sub(pattern, new_hero.strip(), content, flags=re.DOTALL)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
        
    return False

def main():
    fixed = 0
    for fname in os.listdir(ROOT):
        if fname.endswith(".html"):
            fpath = os.path.join(ROOT, fname)
            if process_file(fpath):
                print(f"  [FIXED] {fname}")
                fixed += 1

    print(f"\nDone - {fixed} files fixed.")

if __name__ == "__main__":
    print("Phase 6: Standardizing heroes...")
    main()
