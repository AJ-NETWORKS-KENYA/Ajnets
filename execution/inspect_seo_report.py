import json

with open(r".tmp\lighthouse_index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

seo_audits = data["categories"]["seo"]["auditRefs"]
print("Non-perfect SEO audits on Index:")
for ref in seo_audits:
    audit_id = ref["id"]
    audit_res = data["audits"].get(audit_id, {})
    score = audit_res.get("score")
    if score is not None and score < 1:
        title = audit_res.get("title")
        desc = audit_res.get("description")
        explanation = audit_res.get("explanation")
        print(f"  - {audit_id} (score={score}): {title}")
        print(f"    Details: {explanation or audit_res.get('displayValue')}")
