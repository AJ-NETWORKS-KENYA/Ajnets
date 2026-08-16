import os
import re
from PIL import Image

def process_html_file(filepath, base_dir):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def img_replacer(match):
        img_tag = match.group(0)
        
        src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
        if not src_match:
            return img_tag
            
        src = src_match.group(1)
        
        if src.startswith('/'):
            img_path = os.path.join(base_dir, src.lstrip('/'))
        else:
            img_path = os.path.join(os.path.dirname(filepath), src)
            
        img_path = os.path.normpath(img_path)
        
        size = None
        if os.path.exists(img_path):
            try:
                with Image.open(img_path) as img:
                    size = img.size
            except:
                pass
                
        new_tag = img_tag
        
        if size:
            # Check if width/height already exists
            has_width = bool(re.search(r'\bwidth=["\']\d+', new_tag, re.IGNORECASE))
            has_height = bool(re.search(r'\bheight=["\']\d+', new_tag, re.IGNORECASE))
            
            if not has_width and not has_height:
                if new_tag.endswith('/>'):
                    new_tag = new_tag[:-2] + f' width="{size[0]}" height="{size[1]}"/>'
                elif new_tag.endswith('>'):
                    new_tag = new_tag[:-1] + f' width="{size[0]}" height="{size[1]}">'
                
        # Handle lazy loading
        if 'logo' in src.lower():
            # Logo should load eagerly
            new_tag = re.sub(r'\s*loading=["\']lazy["\']', '', new_tag, flags=re.IGNORECASE)
            new_tag = re.sub(r'\s*fetchpriority=["\'][^"\']+["\']', '', new_tag, flags=re.IGNORECASE)
            if 'fetchpriority' not in new_tag:
                 if new_tag.endswith('/>'):
                     new_tag = new_tag[:-2] + ' fetchpriority="high"/>'
                 else:
                     new_tag = new_tag[:-1] + ' fetchpriority="high">'
        else:
            if 'loading=' not in new_tag.lower() and 'fetchpriority=' not in new_tag.lower():
                if new_tag.endswith('/>'):
                    new_tag = new_tag[:-2] + ' loading="lazy"/>'
                elif new_tag.endswith('>'):
                    new_tag = new_tag[:-1] + ' loading="lazy">'
                
        return new_tag

    new_content = re.sub(r'<img\s+[^>]*>', img_replacer, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated images in {filepath}")

def main():
    base_dir = r"c:\My Web Sites\ajnets"
    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file), base_dir)

if __name__ == "__main__":
    main()
