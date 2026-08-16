import os
import re

def fix_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    new_content = new_content.replace('href="/faq">Privacy Policy</a>', 'href="/privacy">Privacy Policy</a>')
    new_content = new_content.replace('href="/faq">Terms</a>', 'href="/terms">Terms</a>')
    new_content = new_content.replace('href="/faq">Responsible Disclosure</a>', 'href="/responsible-disclosure">Responsible Disclosure</a>')

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
                fix_footer(os.path.join(root, file))

if __name__ == "__main__":
    main()
