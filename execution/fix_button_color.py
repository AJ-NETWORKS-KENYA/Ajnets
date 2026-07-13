import os

css_path = r"c:\My Web Sites\ajnets\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace the previous var(--ajn-blue) in .octf-btn-primary with the bright blue from the image
old_btn = """/* Standardized Buttons */
.octf-btn-primary {
    background-color: var(--ajn-blue) !important;
    color: var(--ajn-white) !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
}

.octf-btn-primary:hover {
    background-color: var(--ajn-navy) !important;
    color: var(--ajn-white) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(43, 59, 133, 0.3);
}"""

new_btn = """/* Standardized Buttons */
.octf-btn-primary, .octf-btn-third {
    background-color: #4DB5FF !important; /* Bright sky blue from reference */
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase;
}

.octf-btn-primary:hover, .octf-btn-third:hover {
    background-color: #3AA3F0 !important;
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(77, 181, 255, 0.4);
}"""

if old_btn in css_content:
    css_content = css_content.replace(old_btn, new_btn)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated button color to reference bright blue.")
else:
    print("Could not find the exact old button CSS block.")
