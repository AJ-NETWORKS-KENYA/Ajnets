import os
import re

directory = "c:\\My Web Sites\\ajnets"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix viewport: Remove 'maximum-scale=1'
    content = re.sub(
        r'(<meta\s+name="viewport"\s+content="[^"]*)(\s*,\s*maximum-scale=1)(\s*[^"]*"\s*/?>)',
        r'\1\3',
        content,
        flags=re.IGNORECASE
    )

    # Clean up double commas if any (e.g. initial-scale=1,,)
    content = re.sub(r',\s*,', ',', content)
    # Clean up trailing comma before quote
    content = re.sub(r',\s*"', '"', content)

    # 2. Add rel="noopener" to target="_blank" links
    # This is a bit tricky since some might have rel already.
    # To be safe, we selectively add rel="noopener" if it doesn't already have a rel attribute.
    # regex: <a [^>]*target="_blank"[^>]*>
    def add_noopener(match):
        a_tag = match.group(0)
        if 'rel=' not in a_tag:
            return a_tag.replace('target="_blank"', 'target="_blank" rel="noopener"')
        elif 'noopener' not in a_tag:
            # Append noopener to existing rel
            return re.sub(r'rel="([^"]*)"', r'rel="\1 noopener"', a_tag)
        return a_tag
    
    content = re.sub(r'<a\s+[^>]*target="_blank"[^>]*>', add_noopener, content, flags=re.IGNORECASE)

    # 3. Add title/aria-label to common icon buttons
    # e.g. <span class="search-submit">...<i class="flaticon-search"></i></span>
    # We will let the IDE handle empty links specifically if we still need to.

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed lint errors in {os.path.basename(filepath)}")

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        fix_file(os.path.join(directory, filename))

print("Lint fix script completed.")
