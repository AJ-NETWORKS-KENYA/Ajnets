import json

d = json.load(open('_audit_results.json'))

print('=== BROKEN LINKS ===')
for x in d['broken_links']:
    print('  ' + x['source'] + ' -> ' + x['target'])

print()
print('=== SEO ISSUES ===')
for x in d['seo_issues']:
    print('  ' + x['page'] + ': ' + x['issue'])

print()
print('=== TRACKING ISSUES ===')
for x in d['tracking_issues']:
    print('  ' + x['page'] + ': ' + x['issue'])

print()
print('=== ASSET ISSUES ===')
for x in d['asset_issues']:
    print('  ' + x['source'] + ' -> ' + x['asset'])

print()
print('SEO OK count: ' + str(len(d['seo_ok'])))
print('Tracking OK count: ' + str(len(d['tracking_ok'])))
