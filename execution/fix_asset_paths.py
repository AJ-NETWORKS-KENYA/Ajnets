"""
fix_asset_paths.py -- Fix remaining relative asset paths missed by previous scripts.

Specifically looks for:
- href="style.css" -> href="/style.css"
- src="images/" -> src="/images/"
- logo: "images/logo.svg" -> logo: "/images/logo.svg"
- href="./" -> href="/" (Optional but cleaner for root routing)
"""

import os
import re

STYLE_CSS_RE = re.compile(r'href="(style(?:\.min)?\.css)')
IMAGES_SRC_RE = re.compile(r'src="images/')
LOGO_IMAGES_RE = re.compile(r'logo:\s*"images/')

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix style.css mapping
    content = STYLE_CSS_RE.sub(r'href="/\1', content)
    
    # 2. Fix images prefix (and make sure we don't duplicate slashes)
    content = IMAGES_SRC_RE.sub('src="/images/', content)
    content = LOGO_IMAGES_RE.sub('logo: "/images/', content)
    
    # fix edge case: src="//images"
    content = content.replace('src="//images', 'src="/images')

    # 3. Fix fonts / typography if linked relatively 
    content = content.replace('href="fonts/', 'href="/fonts/')
    content = content.replace('href="js/', 'href="/js/')
    content = content.replace('src="js/', 'src="/js/')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Fixed paths: {filepath}')

def run():
    skip = {'.git', 'node_modules', '.tmp', '.vercel', 'execution'}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in skip]
        for fname in files:
            if fname.endswith('.html'):
                fix_file(os.path.join(root, fname))
    print('\nDone.')

if __name__ == '__main__':
    run()
