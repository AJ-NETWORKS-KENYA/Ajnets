"""
fix_search_block.py  --  Remove the loose search button+form from octf-btn-cta.

The previous fix removed the <div class="octf-header-module"> wrapper around
the search, but the button/form itself (toggle_search) was left behind as a
bare element inside .octf-btn-cta. That orphan block hides the CTA button.

This script:
1. Removes the solo <button class="toggle_search ..."> tag
2. Removes the <div class="h-search-form-field collapse"> block that follows it
"""

import os
import re


def remove_tag(content, tag_open, tag_close):
    """Generic removal of the first matching open+close tag pair."""
    start = content.find(tag_open)
    if start == -1:
        return content, False
    end_marker = content.find(tag_close, start)
    if end_marker == -1:
        return content, False
    end = end_marker + len(tag_close)
    return content[:start] + content[end:], True


def remove_search_button(content):
    """Remove <button class="toggle_search ...">...</button>"""
    # Find start
    start = content.find('<button\n                          class="toggle_search')
    if start == -1:
        start = content.find('<button class="toggle_search')
    if start == -1:
        start = content.find('"toggle_search')
        if start != -1:
            # Walk back to find the <button tag
            tag_start = content.rfind('<button', 0, start)
            if tag_start != -1:
                start = tag_start

    if start == -1:
        return content, False

    end = content.find('</button>', start) + len('</button>')
    return content[:start] + content[end:], True


def remove_search_form_div(content):
    """Remove <div class="h-search-form-field collapse">...</div>"""
    open_tag_variants = [
        '<div class="h-search-form-field collapse">',
        '<div class="h-search-form-field collapse" >',
    ]
    start = -1
    for v in open_tag_variants:
        idx = content.find(v)
        if idx != -1:
            start = idx
            break

    if start == -1:
        return content, False

    # Count divs to find closing tag
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

    content, ok1 = remove_search_button(content)
    changed = changed or ok1

    content, ok2 = remove_search_form_div(content)
    changed = changed or ok2

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
