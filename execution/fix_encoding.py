"""
Phase 6: Standardize service page heroes and fix encoding issues.
Replaces inline-styled heroes with the page-hero component class.
"""
import os
import re

ROOT = "."

# Fix encoding artifacts (replacement character)
def fix_encoding(content):
    # Replace common encoding artifacts
    content = content.replace("\ufffd", "—")
    content = content.replace("\u00e2\u0080\u0094", "—")
    content = content.replace("\u00e2\u0080\u0093", "–")
    content = content.replace("\u00e2\u0080\u0099", "'")
    content = content.replace("\u00e2\u0080\u009c", '"')
    content = content.replace("\u00e2\u0080\u009d", '"')
    return content


def fix_all_html():
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ("execution", "node_modules", ".git", ".tmp")]
        for fname in filenames:
            if fname.endswith(".html"):
                fpath = os.path.join(dirpath, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()

                original = content
                content = fix_encoding(content)

                if content != original:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  [FIXED] {os.path.relpath(fpath, ROOT)}")
                    fixed += 1

    return fixed


if __name__ == "__main__":
    print("Phase 6: Fixing encoding issues across all pages...")
    count = fix_all_html()
    print(f"\nDone - {count} files fixed.")
