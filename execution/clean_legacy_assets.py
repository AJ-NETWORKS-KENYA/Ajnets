import os
import re

def clean_legacy_assets(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Remove Tailwind CDN
    new_content = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>\s*', '', new_content)
    
    # Remove WooCommerce CSS
    new_content = re.sub(r'<link.*?href="/css/woocommerce\.css".*?>\s*', '', new_content)
    # also handle without leading slash if present
    new_content = re.sub(r'<link.*?href="css/woocommerce\.css".*?>\s*', '', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned legacy assets in: {filepath}")

def main():
    root_dir = r"c:\My Web Sites\ajnets"
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root or ".vercel" in root or ".tmp" in root:
            continue
        for file in files:
            if file.endswith('.html'):
                clean_legacy_assets(os.path.join(root, file))

if __name__ == "__main__":
    main()
