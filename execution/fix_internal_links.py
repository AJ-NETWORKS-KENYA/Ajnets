"""
Phase 8: Fix internal links.
Replaces obsolete links with the consolidated service/portfolio links.
"""
import os
import re

ROOT = r"c:\My Web Sites\ajnets"

REPLACEMENTS = {
    r'"/services/web-development"': '"/services/software-engineering"',
    r'"/services/mobile-development"': '"/services/software-engineering"',
    r'"/services/solutions"': '"/services/services"',
    r'"/portfolio/portfolio-details-1"': '"/portfolio/client-success"',
    r'"/portfolio/portfolio-details-2"': '"/portfolio/client-success"',
}

def fix_links(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    for old, new in REPLACEMENTS.items():
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
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
                if fix_links(fpath):
                    print(f"  [FIXED] {os.path.relpath(fpath, ROOT)}")
                    fixed += 1

    print(f"\nDone - {fixed} files fixed.")

if __name__ == "__main__":
    print("Phase 8: Fixing internal links...")
    main()
