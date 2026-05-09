import os
import re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")
src_path = ROOT / "case-study-audiophile.html"
dst_path = ROOT / "case-study-crappo.html"

with open(src_path, "r", encoding="utf-8") as f:
    html = f.read()

# Make replacements for Crappo
replacements = {
    "Audiophile E-Commerce Architecture": "Crappo Crypto Platform",
    "case-study-audiophile.html": "case-study-crappo.html",
    "Online Retail Platform": "Crypto Investment Platform",
    "Retail E-Commerce": "FinTech / Cryptocurrency",
    "A premium e-commerce web application for a consumer electronics retailer featuring advanced state management, dynamic routing, and fluid Framer Motion animations.": "A modern, high-performance cryptocurrency investment platform featuring live market data integration, secure wallet connections, and sleek dark-mode UI components.",
    "https://audiophile-estore.netlify.app": "#",
    "E-commerce platforms must balance visual richness with technical performance. The challenge was delivering a premium product browsing and checkout experience that rivalled market leaders — without compromising load times or accessibility.": "Building trust in Web3 requires a flawless, professional user interface. The challenge was designing and engineering a crypto platform that felt secure, fast, and accessible to both novice investors and experienced traders.",
    "We engineered a fully featured React e-commerce frontend with context-based global state management. Framer Motion was implemented for smooth page transitions and micro-interaction animations. The cart system maintains persistent state through session storage with optimistic UI updates.": "We built a specialized React frontend using TailwindCSS for rapid, responsive styling. The architecture includes modular dashboard components, animated data visualizations, and a secure authentication flow designed for financial applications.",
    "Enterprise-Grade Frontend Architecture": "Secure FinTech Architecture",
    "Modular component system with clear separation of concerns for maintainability at scale.": "Built with strict component boundaries and immutable state patterns suitable for financial data handling.",
    "Fluid Interaction Design": "Data Visualization & UI",
    "Framer Motion animations deliver a premium perceived performance without impacting real LCP.": "Integrated modern chart libraries and smooth transitions to make complex market data easily digestible.",
    "Complete Checkout Flow": "Wallet Integration Flow",
    "Full add-to-cart, quantity management, and order summary flow implemented with no backend dependency.": "Engineered the frontend flows for wallet connectivity, securely guiding users through the exchange process.",
    "React, TailwindCSS, Framer Motion, Figma": "React, TailwindCSS, Figma",
    "images/projects/Audiophile.png": "images/projects/Crappo.png",
    "/audiophile-ecommerce": "/crappo-crypto-platform"
}

# Replace colors
# Audiophile uses purple #7c3aed and pink #ec4899 in the card (wait, the card is in client-success.html)
# The case study uses cyber-blue / cyber-green standard colors. 

for old, new in replacements.items():
    html = html.replace(old, new)


with open(dst_path, "w", encoding="utf-8") as f:
    f.write(html)

print("case-study-crappo.html created successfully.")
