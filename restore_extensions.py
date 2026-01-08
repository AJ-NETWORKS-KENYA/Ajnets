import os
import re

def restore_extensions():
    # Get all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Map of "clean name" -> "file name"
    # e.g., "about-us" -> "about-us.html"
    file_map = {f[:-5]: f for f in html_files}
    
    print(f"Found {len(html_files)} HTML files to scan.")
    
    count_files_changed = 0

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # For each known HTML file, check if it's referenced without extension
        for clean_name, full_name in file_map.items():
            # Regex to find href="clean_name"
            # We use strict matching to avoid replacing "about-us-services" when looking for "about-us"
            # Look for href="clean_name" or href="./clean_name"
            
            # Pattern 1: href="clean_name"
            pattern1 = r'href="' + re.escape(clean_name) + r'"'
            replacement1 = f'href="{full_name}"'
            content = re.sub(pattern1, replacement1, content)
            
            # Pattern 2: href="./clean_name"
            pattern2 = r'href="\./' + re.escape(clean_name) + r'"'
            replacement2 = f'href="./{full_name}"'
            content = re.sub(pattern2, replacement2, content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated links in: {file_path}")
            count_files_changed += 1
            
    print(f"Finished. Updated {count_files_changed} files.")

if __name__ == "__main__":
    restore_extensions()
