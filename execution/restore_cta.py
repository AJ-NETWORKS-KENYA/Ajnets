import os

files_to_fix = []
for root, dirs, files in os.walk('.'):
    # filter out hidden/execution dirs
    dirs[:] = [d for d in dirs if not (d.startswith('.') or d in ['node_modules', 'execution'])]
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            content = open(path, 'r', encoding='utf-8').read()
            if 'Request Consultation' not in content and 'Free Quote' not in content:
                files_to_fix.append(path)

print('Files missing CTA:')
for f in files_to_fix: print('  ' + f)

cta_html = '''
                      <div class="octf-header-module">
                        <div class="btn-cta-group btn-cta-header">
                          <a
                            class="octf-btn octf-btn-third"
                            href="/company/book-consultation"
                            >Request Consultation</a
                          >
                        </div>
                      </div>
'''

for path in files_to_fix:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert CTA button at the end of <div class="octf-btn-cta">
    target = '<div class="octf-btn-cta">'
    idx = content.find(target)
    if idx != -1:
        insert_pos = idx + len(target)
        new_content = content[:insert_pos] + cta_html + content[insert_pos:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Restored CTA in {path}')
    else:
        print(f'Could not find insertion point in {path}')
