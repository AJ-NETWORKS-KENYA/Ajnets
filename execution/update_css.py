import os

filepath = r"c:\My Web Sites\ajnets\style.css"

css_to_append = """
/* ==========================================================================
   AJNETWORKS VERSION 2.5 - ENTERPRISE DESIGN SYSTEM OVERRIDES
   ========================================================================== */

:root {
    /* Brand Colors */
    --ajn-navy: #1A1A2E;
    --ajn-blue: #2B3B85;
    --ajn-accent: #43D9AD;
    --ajn-light: #E0E0E0;
    --ajn-white: #FFFFFF;
    
    /* Spacing Scale (No arbitrary spacing) */
    --spacing-16: 16px;
    --spacing-24: 24px;
    --spacing-32: 32px;
    --spacing-48: 48px;
    --spacing-64: 64px;
    --spacing-96: 96px;
    --spacing-128: 128px;
    
    /* Typography */
    --font-display: 'Montserrat', sans-serif;
    --font-body: 'Nunito Sans', sans-serif;
}

/* Typography Overrides */
h1, h2, h3, h4, h5, h6, .main-heading {
    font-family: var(--font-display) !important;
}

body, p, a, span, div {
    font-family: var(--font-body);
}

/* Global Backgrounds & Colors */
.bg-dark-primary {
    background-color: var(--ajn-navy) !important;
}

.bg-gradient {
    background: linear-gradient(135deg, var(--ajn-navy) 0%, var(--ajn-blue) 100%) !important;
}

/* Standardized Padding */
.section-padd {
    padding: var(--spacing-96) 0 !important;
}

.padding-half {
    padding: var(--spacing-48) 0 !important;
}

/* Hero Heights & Layouts */
.page-hero {
    padding: var(--spacing-128) 0 var(--spacing-96) 0 !important;
    text-align: left;
}

/* Standardized Buttons */
.octf-btn-primary {
    background-color: var(--ajn-accent) !important;
    color: var(--ajn-navy) !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
}

.octf-btn-primary:hover {
    background-color: #38bfa0 !important;
    color: var(--ajn-navy) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(67, 217, 173, 0.3);
}

/* Standardized Cards */
.icon-box-s2, .outcome-box, .case-study-cta, .widget-footer {
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    border: 1px solid rgba(0,0,0,0.05);
}

.icon-box-s2:hover, .outcome-box:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08) !important;
}

/* Trust Signals / Technologies Bar */
.tech-badge {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #fff;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 600;
    margin-right: 8px;
    display: inline-block;
    margin-bottom: 8px;
}

/* Ensure no neon / glassmorphism */
.glass-effect, .neon-text {
    display: none !important;
}
"""

try:
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(css_to_append)
    print("Appended V2.5 Design System overrides to style.css")
except Exception as e:
    print(f"Error updating style.css: {e}")
