import os
import re

# The folders that are internal routing implementation details
INTERNAL_FOLDERS = ['company/', 'services/', 'portfolio/', 'insights/', 'elements/']

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # We want to replace things like:
    # <link href="https://ajnetworks.co/company/about-us" rel="canonical"/>
    # with:
    # <link href="https://ajnetworks.co/about-us" rel="canonical"/>
    
    for folder in INTERNAL_FOLDERS:
        # Fix canonical
        new_content = re.sub(
            f'href="https://ajnetworks.co/{folder}',
            'href="https://ajnetworks.co/',
            new_content
        )
        # Fix og:url
        new_content = re.sub(
            f'content="https://ajnetworks.co/{folder}',
            'content="https://ajnetworks.co/',
            new_content
        )

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    root_dir = r"c:\My Web Sites\ajnets"
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root or ".vercel" in root:
            continue
        for file in files:
            if file.endswith('.html'):
                fix_html_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
