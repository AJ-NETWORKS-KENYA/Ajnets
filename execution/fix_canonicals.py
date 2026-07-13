"""
Phase 6: Fix broken canonical URLs and duplicate skip-links across all HTML pages.
The standardization script erroneously used Windows file paths in canonical/OG URLs.
"""
import os
import re

ROOT = r"c:\My Web Sites\ajnets"
DOMAIN = "https://ajnetworkskenya.it.com"

# Build map of file paths to correct URL paths
def get_url_path(filepath):
    """Convert a file path to a URL path relative to site root."""
    rel = os.path.relpath(filepath, ROOT).replace("\\", "/")
    # Remove .html extension for clean URLs
    if rel.endswith(".html"):
        rel = rel[:-5]
    # index becomes /
    if rel == "index":
        return "/"
    return "/" + rel


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    url_path = get_url_path(filepath)

    # 1. Fix broken canonical URLs containing Windows paths
    # Pattern: https://ajnetworkskenya.it.com/c:/My Web Sites/ajnets/some/path
    content = re.sub(
        r'(https://ajnetworkskenya\.it\.com/)c:/My Web Sites/ajnets/([^"\']+)',
        lambda m: DOMAIN + "/" + m.group(2),
        content
    )

    # 2. Remove duplicate skip-links (keep only the first one)
    skip_pattern = r'(\s*<!-- Skip to main content link for accessibility -->\s*<a href="#content" class="skip-link">Skip to main content</a>\s*)'
    matches = list(re.finditer(skip_pattern, content))
    if len(matches) > 1:
        # Remove all but the first occurrence
        for match in reversed(matches[1:]):
            content = content[:match.start()] + "\n" + content[match.end():]

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip execution and node_modules
        dirnames[:] = [d for d in dirnames if d not in ("execution", "node_modules", ".git", ".tmp")]
        for fname in filenames:
            if fname.endswith(".html"):
                fpath = os.path.join(dirpath, fname)
                if fix_file(fpath):
                    print(f"  [FIXED] {os.path.relpath(fpath, ROOT)}")
                    fixed += 1

    print(f"\nDone - {fixed} files fixed.")


if __name__ == "__main__":
    print("Phase 6: Fixing canonical URLs and duplicate skip-links...")
    main()
