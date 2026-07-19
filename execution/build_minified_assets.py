import os
import re

ROOT_DIR = r"c:\My Web Sites\ajnets"
CSS_FILE = os.path.join(ROOT_DIR, "style.css")
MIN_CSS_FILE = os.path.join(ROOT_DIR, "style.min.css")

def minify_css(css_content):
    css_content = re.sub(r'/\*[\s\S]*?\*/', '', css_content)
    css_content = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css_content)
    css_content = re.sub(r'\s+', ' ', css_content)
    css_content = re.sub(r';\}', '}', css_content)
    return css_content.strip()

def update_html_references():
    updated = 0
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        if "node_modules" in dirpath or ".git" in dirpath or ".tmp" in dirpath:
            continue
        for f in filenames:
            if f.endswith(".html"):
                filepath = os.path.join(dirpath, f)
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()
                if 'href="/style.css"' in content:
                    new_content = content.replace('href="/style.css"', 'href="/style.min.css"')
                    with open(filepath, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    updated += 1
    print(f"Updated {updated} HTML files to load /style.min.css")

def build():
    print("Building minified assets...")
    if not os.path.exists(CSS_FILE):
        print(f"Error: {CSS_FILE} does not exist.")
        return False

    with open(CSS_FILE, "r", encoding="utf-8") as f:
        original_content = f.read()

    original_size = len(original_content.encode("utf-8"))
    minified = minify_css(original_content)
    minified_size = len(minified.encode("utf-8"))

    with open(MIN_CSS_FILE, "w", encoding="utf-8") as f:
        f.write(minified)

    savings = (1 - minified_size / original_size) * 100
    print(f"Original size: {original_size / 1024:.2f} KB")
    print(f"Minified size: {minified_size / 1024:.2f} KB")
    print(f"Compression ratio: {savings:.2f}% savings")
    print(f"Minified CSS written to: {MIN_CSS_FILE}")

    update_html_references()
    return True

if __name__ == "__main__":
    build()
