import os
import re

def strip_div_by_class(html_str, class_name):
    """
    Robustly removes a div and all its children by class name by counting open/close tags.
    """
    target = f'<div class="{class_name}">'
    idx = html_str.find(target)
    if idx == -1:
        # Some might have extra spacing
        match = re.search(r'<div\s+class="(?:[^"]*\s)?' + re.escape(class_name) + r'(?:\s[^"]*)?">', html_str)
        if not match:
            return html_str
        idx = match.start()
    
    # We found the start of the div
    div_depth = 0
    i = idx
    while i < len(html_str):
        # Find next <div or </div
        next_open = html_str.find('<div', i)
        next_close = html_str.find('</div', i)
        
        if next_open != -1 and next_open < next_close:
            div_depth += 1
            i = next_open + 4
        elif next_close != -1:
            div_depth -= 1
            i = next_close + 6
            if div_depth == 0:
                # We found the closing div for our target
                # Now close the tag completely `</div>`
                tag_close_idx = html_str.find('>', i)
                if tag_close_idx != -1:
                    # Return substring before target + substring after target
                    return html_str[:idx] + html_str[tag_close_idx+1:]
                break
        else:
            break
            
    return html_str

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_length = len(content)
    
    # 1. Remove the shopping cart module
    content = strip_div_by_class(content, "octf-header-module cart-btn-hover")
    
    # 2. Fix rogue duplicated closing angle brackets: >><i
    content = content.replace('>><i', '><i')
    content = content.replace('>> <i', '> <i')
    content = content.replace('>>\n<i', '>\n<i')
    
    # 3. Fix broken self-hosted flaticons by falling back to FontAwesome
    content = content.replace('flaticon-search', 'fas fa-search')
    # If shopper is still there anywhere (e.g. mobile menu), replace it just in case
    content = content.replace('flaticon-shopper', 'fas fa-shopping-cart')
    
    # 4. Search form placeholder weird character fix (placeholder="Search ")
    # Actually just replace the bad char if it exists
    content = content.replace('placeholder="Search "', 'placeholder="Search..."')
    
    if len(content) != old_length or True: # Force write in case replacement was 1:1 length
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def run():
    print("Fixing UI anomalies across all HTML files...")
    # Walk all folders that could contain HTML
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                # Ignore node_modules, .tmp, etc.
                if '.git' in root or 'node_modules' in root or '.tmp' in root or '.vercel' in root or 'execution' in root:
                    continue
                filepath = os.path.join(root, f)
                process_file(filepath)

if __name__ == '__main__':
    run()
    print("Done!")
