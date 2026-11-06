import os
import re

directory = "c:\\My Web Sites\\ajnets"

VIEWPORT_REGEX = re.compile(
    r'(<meta\s+name="viewport"\s+content="[^"]*)(\s*,\s*maximum-scale=1)(\s*[^"]*"\s*/?>)',
    flags=re.IGNORECASE
)
DOUBLE_COMMA_REGEX = re.compile(r',\s*,')
TRAILING_COMMA_QUOTE_REGEX = re.compile(r',\s*"')
REL_REGEX = re.compile(r'rel="([^"]*)"')
TARGET_BLANK_REGEX = re.compile(r'<a\s+[^>]*target="_blank"[^>]*>', flags=re.IGNORECASE)

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix viewport: Remove 'maximum-scale=1'
    content = VIEWPORT_REGEX.sub(r'\1\3', content)

    # Clean up double commas if any (e.g. initial-scale=1,,)
    content = DOUBLE_COMMA_REGEX.sub(',', content)
    # Clean up trailing comma before quote
    content = TRAILING_COMMA_QUOTE_REGEX.sub('"', content)

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
            return REL_REGEX.sub(r'rel="\1 noopener"', a_tag)
        return a_tag
    
    content = TARGET_BLANK_REGEX.sub(add_noopener, content)

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
