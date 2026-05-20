import os

css_fix = """

/* --- UI HOTFIX: Responsive Header Overlap --- */
/* Hide the second contact-header on smaller screens because it overlaps the Request Consultation CTA */
/* The phone number is already visible in the topbar, so it is safe to collapse here. */
@media (max-width: 1366px) {
    .octf-btn-cta .contact-header {
        display: none !important;
    }
}
"""

def apply_css_fix(style_path):
    # Check if fix already applied
    with open(style_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* --- UI HOTFIX: Responsive Header Overlap --- */" not in content:
        with open(style_path, 'a', encoding='utf-8') as f:
            f.write(css_fix)
        print(f"Applied responsive header overlap fix to {style_path}")
    else:
        print(f"Responsive fix already exists in {style_path}")

def run():
    style_path = os.path.join('.', 'style.css')
    if os.path.exists(style_path):
        apply_css_fix(style_path)
    else:
        print("style.css not found!")

if __name__ == "__main__":
    run()
