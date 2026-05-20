import os
import re

directory = "c:\\My Web Sites\\ajnets"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original_content = content

    # 1. Search submit buttons -> title="Submit search"
    content = re.sub(
        r'(<button\s+[^>]*class="[^"]*search-submit[^"]*"[^>]*)>',
        lambda m: m.group(1) + ' title="Submit search">' if 'title=' not in m.group(1) else m.group(0),
        content,
        flags=re.IGNORECASE
    )

    # 2. Cart buttons
    content = re.sub(
        r'(<button\s+[^>]*class="[^"]*toggle_search[^"]*"[^>]*)>',
        lambda m: m.group(1) + ' title="Toggle search">' if 'title=' not in m.group(1) else m.group(0),
        content,
        flags=re.IGNORECASE
    )

    # 3. All a-tags containing an 'fa-' or 'flaticon-' icon -> assign dynamic title
    # We'll match <a ...> ... <i class="...fa-X..."> ... </a> using a robust pattern
    def repl_icon_link(match):
        a_tag_full = match.group(0)
        # Check if the a-tag has visible text other than the icon/whitespace
        # (This is approximate, but good enough for these templates)
        inside_a = match.group(2)
        if 'title=' in match.group(1):
            return a_tag_full

        icon_match = re.search(r'(?:fa|flaticon)-([a-z0-9-]+)', inside_a, re.IGNORECASE)
        if icon_match:
            label = icon_match.group(1).replace('-', ' ').title()
            return f'<a title="{label}" ' + match.group(1)[3:] + '>' + inside_a + '</a>'
        return a_tag_full

    # Match <a ...> ... </a>
    content = re.sub(
        r'(<a\s+[^>]*>)(.*?)(</a>)',
        repl_icon_link,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 4. Same for generic <button> ... </button>
    def repl_icon_button(match):
        b_tag_full = match.group(0)
        inside_b = match.group(2)
        if 'title=' in match.group(1):
            return b_tag_full

        icon_match = re.search(r'(?:fa|flaticon)-([a-z0-9-]+)', inside_b, re.IGNORECASE)
        if icon_match:
            label = icon_match.group(1).replace('-', ' ').title()
            return f'<button title="{label}" ' + match.group(1)[8:] + '>' + inside_b + '</button>'
        return b_tag_full

    content = re.sub(
        r'(<button\s+[^>]*>)(.*?)(</button>)',
        repl_icon_button,
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed titles in {os.path.basename(filepath)}")

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        fix_file(os.path.join(directory, filename))

print("Lint fix 3 completed.")
