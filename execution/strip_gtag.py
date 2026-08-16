import os
import re

def strip_gtag_script(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The string to look for (using regex to handle possible whitespace changes)
    pattern = re.compile(r'<script async(?:="")? src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*')
    
    new_content, count = pattern.subn('', content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Stripped {count} gtag.js tag(s) from: {filepath}")
    else:
        print(f"No gtag.js tag found: {filepath}")

def main():
    root_dir = r"c:\My Web Sites\ajnets"
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root or ".vercel" in root or ".tmp" in root:
            continue
        for file in files:
            if file.endswith('.html'):
                strip_gtag_script(os.path.join(root, file))

if __name__ == "__main__":
    main()
