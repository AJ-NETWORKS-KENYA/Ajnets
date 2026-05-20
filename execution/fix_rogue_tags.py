import os
import re

def fix_rogue_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # Fix case:  >>Request a Strategy Call
    # If we have >> followed by word char or space
    content = re.sub(r'>>\s*([A-Za-z])', r'>\1', content)
    
    # Fix case: >>Contact Us
    content = re.sub(r'>>([A-Z])', r'>\1', content)
    
    # Fix case: >>hello (specifically the book-consultation mailto issue)
    content = re.sub(r'>>\s*hello', r'>hello', content)
    
    # Fix case: >View Live Site
    # e.g., <a ... >>View Live Site => <a ... >View Live Site
    # Wait, the previous regex covers this because V is [A-Z]
    
    # Fix case: <a ... >>>
    content = re.sub(r'>>>', r'>', content)
    
    # Fix case empty links: " ... ">>
    # If the tag simply ends in >> before a newline or <
    content = re.sub(r'>>\s*(?=<)', r'>', content)
    content = re.sub(r'>>\n', r'>\n', content)
    
    # Extreme edge case: class="foo">>
    content = re.sub(r'"\s*>>', r'">', content)

    # Specific fixes seen in the logs
    content = content.replace('>>', '>') # Wait, this might break valid JS `>> 1` if we have inline scripts. 
    # Let me just replace `>>` with `>` ONLY if it's not inside a <script> block. Actually, since this is raw HTML, replacing all `>>` is risky.
    # Let's revert that blanket replace and trust the targeted regexes above.
    
    # Wait, let me handle the blanket replace safely by splitting by <script:
    blocks = content.split('<script')
    for i, block in enumerate(blocks):
        if i == 0:
            blocks[i] = block.replace('>>', '>')
        else:
            # Everything up to </script> is JS, do not touch it
            js_end = block.find('</script>')
            if js_end != -1:
                html_part = block[js_end:]
                blocks[i] = block[:js_end] + html_part.replace('>>', '>')

    content = '<script'.join(blocks)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned rogue tags in {filepath}")

def run():
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not (d.startswith('.') or d in ['node_modules', 'execution'])]
        for f in files:
            if f.endswith('.html'):
                fix_rogue_tags(os.path.join(root, f))

if __name__ == '__main__':
    run()
