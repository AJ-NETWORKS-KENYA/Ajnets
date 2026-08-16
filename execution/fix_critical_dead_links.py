import os
import re

def fix_dead_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Remove Status and Documentation links from footer
    new_content = re.sub(r'<li class="list-item"><a href="#">Status</a></li>\s*', '', new_content)
    new_content = re.sub(r'<li class="list-item"><a href="#">Documentation</a></li>\s*', '', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    root_dir = r"c:\My Web Sites\ajnets"
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root or ".vercel" in root or ".tmp" in root:
            continue
        for file in files:
            if file.endswith('.html'):
                fix_dead_links(os.path.join(root, file))

if __name__ == "__main__":
    main()
