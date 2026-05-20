"""
fix_header_cta.py  –  Clean up the header CTA column.

Removes from ALL html files:
  1. The search icon module (toggle_search + h-search-form-field)
  2. The secondary contact-header phone block (already in topbar)

Leaves only the Request Consultation CTA button.
"""

import os
import re


def remove_module_by_content(content, search_for):
    """
    Removes the nearest wrapping <div class="octf-header-module"> that
    contains 'search_for'.  Handles nested divs via depth counting.
    """
    idx = content.find(search_for)
    if idx == -1:
        return content, False

    # Walk backwards to find the opening <div class="octf-header-module">
    open_tag = '<div class="octf-header-module">'
    start = content.rfind(open_tag, 0, idx)
    if start == -1:
        return content, False

    # Walk forward counting div depth to find matching </div>
    depth = 0
    i = start
    while i < len(content):
        next_open  = content.find('<div', i)
        next_close = content.find('</div', i)

        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + 4
        elif next_close != -1:
            depth -= 1
            end = content.find('>', next_close) + 1
            i = end
            if depth == 0:
                return content[:start] + content[end:], True
        else:
            break
    return content, False


def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changed = False

    # 1. Remove search module
    content, ok = remove_module_by_content(content, 'toggle_search')
    if ok:
        changed = True

    # 2. Remove secondary contact-header (phone) module
    content, ok = remove_module_by_content(content, 'contact-header')
    if ok:
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Updated: {filepath}')
    else:
        print(f'  No change: {filepath}')


def run():
    skip = {'.git', 'node_modules', '.tmp', '.vercel', 'execution'}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in skip]
        for fname in files:
            if fname.endswith('.html'):
                clean_file(os.path.join(root, fname))

    print('\nDone.')


if __name__ == '__main__':
    run()
