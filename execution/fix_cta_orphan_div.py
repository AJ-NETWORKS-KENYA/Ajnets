"""
fix_cta_orphan_div.py  --  Fix the orphaned </div> inside .octf-btn-cta.

After previous cleanup, there is a stray </div> that prematurely closes
.octf-btn-cta before the Request Consultation button module.

This script fixes all HTML files by:
1. Finding the malformed structure inside .octf-btn-cta
2. Removing the stray </div> that prematurely closes it
"""

import os
import re


def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The broken pattern: inside octf-btn-cta there is an orphaned comment + </div>
    # before the octf-header-module that contains the CTA button.
    # Pattern:
    #   <div class="octf-btn-cta">
    #     ...  <!-- Form Search on Header -->  ...  </div>   <-- STRAY </div>
    #     <div class="octf-header-module">
    #       ... Request Consultation ...
    #     </div>
    #   </div>
    #
    # Fix: remove the stray </div> that appears between the comment and the module

    old_pattern = (
        r'(<div class="octf-btn-cta">)'
        r'(\s*\r?\n\s*\r?\n?\s*\r?\n\s*<!-- Form Search on Header -->)'
        r'(\s*\r?\n\s*\r?\n?\s*</div>)'
        r'(\s*\r?\n\s*\r?\n?\s*\r?\n\s*)'
        r'(<div class="octf-header-module">)'
    )

    replacement = r'\1\2\4\5'

    new_content, count = re.subn(old_pattern, replacement, content, flags=re.MULTILINE)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  Fixed ({count} replacement): {filepath}')
    else:
        print(f'  No match found: {filepath}')


def run():
    skip = {'.git', 'node_modules', '.tmp', '.vercel', 'execution'}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in skip]
        for fname in files:
            if fname.endswith('.html'):
                fix_file(os.path.join(root, fname))
    print('\nDone.')


if __name__ == '__main__':
    run()
