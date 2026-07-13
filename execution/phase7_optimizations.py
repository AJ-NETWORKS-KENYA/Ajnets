"""
Phase 7: Accessibility & Performance
- Adds loading="lazy" to all below-the-fold images.
- Ensures all img tags have an alt attribute.
"""
import os
from bs4 import BeautifulSoup

ROOT = r"c:\My Web Sites\ajnets"

def optimize_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    modified = False

    # 1. Image optimizations
    for img in soup.find_all("img"):
        src = img.get("src", "").lower()
        
        # Ensure alt attribute exists
        if not img.has_attr("alt"):
            img["alt"] = ""
            modified = True
            
        # Add lazy loading to below-fold images
        # Exclude logos, hero images, slider images
        if "logo" not in src and "slide" not in src and "hero" not in src:
            if not img.has_attr("loading"):
                img["loading"] = "lazy"
                modified = True

    if modified:
        # Convert bs4 object back to string
        new_html = str(soup)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        return True

    return False

def main():
    optimized = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip execution and node_modules
        dirnames[:] = [d for d in dirnames if d not in ("execution", "node_modules", ".git", ".tmp")]
        for fname in filenames:
            if fname.endswith(".html"):
                fpath = os.path.join(dirpath, fname)
                if optimize_file(fpath):
                    print(f"  [OPTIMIZED] {os.path.relpath(fpath, ROOT)}")
                    optimized += 1

    print(f"\nDone - {optimized} files optimized.")

if __name__ == "__main__":
    print("Phase 7: Running accessibility and performance optimizations...")
    main()
