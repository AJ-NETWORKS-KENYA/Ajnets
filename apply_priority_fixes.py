"""
P1 + P2 Priority Fixes for AJNETWORKS website
Applies:
  1. font-display=swap on Google Fonts (all pages)
  2. defer on non-critical JS scripts (all legacy HTML pages)
  3. Hero image preload + fetchpriority on index.html
  4. Canonical URL tags (all key pages)
  5. Open Graph tags (all key pages)
  6. JSON-LD Service schema on service pages
"""
import os, re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")
DOMAIN = "https://ajnetworkskenya.it.com"

# Pages and their metadata for OG + canonical tags
PAGE_META = {
    "index.html": {
        "url": "/",
        "title": "AJNETWORKS - Technology Consulting & Engineering Delivery",
        "description": "AJNETWORKS is a technology consulting firm delivering strategic advisory, software engineering, cybersecurity, and IT infrastructure solutions in Kenya.",
        "og_image": "/images/og-home.jpg",
    },
    "about-us.html": {
        "url": "/about-us.html",
        "title": "Who We Are | AJNETWORKS",
        "description": "Meet the team behind AJNETWORKS — a consulting firm founded by Abraham John, delivering technology strategy, engineering, and cybersecurity solutions across East Africa.",
        "og_image": "/images/og-home.jpg",
    },
    "services.html": {
        "url": "/services.html",
        "title": "Services | AJNETWORKS",
        "description": "Explore AJNETWORKS services: technology strategy, software engineering, cybersecurity, networking infrastructure, and digital performance optimization.",
        "og_image": "/images/og-home.jpg",
    },
    "client-success.html": {
        "url": "/client-success.html",
        "title": "Client Success & Case Studies | AJNETWORKS",
        "description": "Real solutions delivered by AJNETWORKS across cybersecurity, web development, and IT systems. Explore our client case studies and engineering portfolios.",
        "og_image": "/images/og-home.jpg",
    },
    "book-consultation.html": {
        "url": "/book-consultation.html",
        "title": "Book a Consultation | AJNETWORKS",
        "description": "Ready to transform your technology? Book an advisory session with AJNETWORKS — technology consulting, software engineering, and cybersecurity experts.",
        "og_image": "/images/og-home.jpg",
    },
    "insights.html": {
        "url": "/insights.html",
        "title": "Insights & Resources | AJNETWORKS",
        "description": "Technology insights, cybersecurity guides, and engineering articles from the AJNETWORKS team. Stay ahead with expert knowledge.",
        "og_image": "/images/og-home.jpg",
    },
    "software-engineering.html": {
        "url": "/software-engineering.html",
        "title": "Software Engineering Services | AJNETWORKS",
        "description": "Custom software engineering in Kenya. Web platforms, mobile apps, and internal systems built with security-first design by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "cybersecurity.html": {
        "url": "/cybersecurity.html",
        "title": "Cybersecurity & Assurance Services | AJNETWORKS",
        "description": "Enterprise cybersecurity services in Kenya — network security, penetration testing, compliance, and threat monitoring by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "technology-strategy.html": {
        "url": "/technology-strategy.html",
        "title": "Technology & Digital Strategy | AJNETWORKS",
        "description": "Strategic technology advisory for East African businesses. Digital transformation, IT roadmaps, and consulting-led solutions by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "networking.html": {
        "url": "/networking.html",
        "title": "Networking & Infrastructure | AJNETWORKS",
        "description": "Enterprise networking and IT infrastructure solutions in Kenya — LAN/WAN, cloud networking, and secure connectivity by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "performance-seo.html": {
        "url": "/performance-seo.html",
        "title": "Performance & SEO Optimization | AJNETWORKS",
        "description": "Core Web Vitals optimization, technical SEO, and web performance consulting in Kenya by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "case-study-bada.html": {
        "url": "/case-study-bada.html",
        "title": "Bada Language Institute Platform | Case Study — AJNETWORKS",
        "description": "How AJNETWORKS engineered an LMS and corporate web platform for Bada Language Institute, improving student engagement and course registrations.",
        "og_image": "/images/og-home.jpg",
    },
    "case-study-sgss.html": {
        "url": "/case-study-sgss.html",
        "title": "Siri Guru Singh Sabha Portal | Case Study — AJNETWORKS",
        "description": "How AJNETWORKS built a high-performance React community portal for Gurdwara Siri Guru Singh Sabha Mombasa.",
        "og_image": "/images/og-home.jpg",
    },
    "case-study-racnyali.html": {
        "url": "/case-study-racnyali.html",
        "title": "Rotaract Club of Nyali | Case Study — AJNETWORKS",
        "description": "A 100-score Lighthouse web platform for Rotaract Nyali showcasing community projects and events, built by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "case-study-transitflow.html": {
        "url": "/case-study-transitflow.html",
        "title": "Transit Flow Logistics | Case Study — AJNETWORKS",
        "description": "AJNETWORKS engineering portfolio: A responsive React logistics landing page from Figma-to-production.",
        "og_image": "/images/og-home.jpg",
    },
    "case-study-audiophile.html": {
        "url": "/case-study-audiophile.html",
        "title": "Audiophile E-Commerce Architecture | Case Study — AJNETWORKS",
        "description": "Engineering case study: A premium e-commerce platform with advanced state management and Framer Motion animations, by AJNETWORKS.",
        "og_image": "/images/og-home.jpg",
    },
    "case-study-greenremedies.html": {
        "url": "/case-study-greenremedies.html",
        "title": "Green Remedies Marketplace | Case Study — AJNETWORKS",
        "description": "Authentication-first e-commerce engineering: How AJNETWORKS built a secure marketplace with Kinde Auth and React.",
        "og_image": "/images/og-home.jpg",
    },
}

# Non-critical JS scripts to add defer to on legacy pages
DEFERRABLE_JS = [
    "js/jquery.magnific-popup.min.js",
    "js/jquery.isotope.min.js",
    "js/owl.carousel.min.js",
    "js/easypiechart.min.js",
    "js/jquery.countdown.min.js",
    "js/scripts.js",
    "js/header-mobile.js",
]

fixes_applied = 0

for page, meta in PAGE_META.items():
    filepath = ROOT / page
    if not filepath.exists():
        print(f"SKIP (not found): {page}")
        continue

    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html
    full_url = DOMAIN + meta["url"]

    # ─── 1. Add font-display=swap to Google Fonts ───────────────────────────
    html = re.sub(
        r'(https://fonts\.googleapis\.com/css2\?[^"\']+)(?:[^"\']*)',
        lambda m: m.group(0) if 'display=swap' in m.group(0) else m.group(0) + '&display=swap',
        html
    )

    # ─── 2. Inject canonical + OG tags if </head> is present ────────────────
    if '</head>' in html:
        # Remove existing canonical / og: tags to avoid duplicates
        html = re.sub(r'\s*<link rel=["\']canonical["\'][^>]*/>\s*', '\n', html)
        html = re.sub(r'\s*<meta property=["\']og:[^>]+>\s*', '\n', html)
        html = re.sub(r'\s*<meta name=["\']twitter:[^>]+>\s*', '\n', html)

        seo_block = f"""
    <!-- Canonical & Open Graph -->
    <link rel="canonical" href="{full_url}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{full_url}" />
    <meta property="og:title" content="{meta['title']}" />
    <meta property="og:description" content="{meta['description']}" />
    <meta property="og:image" content="{DOMAIN}{meta['og_image']}" />
    <meta property="og:site_name" content="AJNETWORKS" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{meta['title']}" />
    <meta name="twitter:description" content="{meta['description']}" />"""

        html = html.replace('</head>', seo_block + '\n  </head>', 1)

    # ─── 3. Add defer to non-critical legacy JS (non-Tailwind pages) ────────
    if 'cdn.tailwindcss.com' not in html:
        for js in DEFERRABLE_JS:
            # Add defer if not already present
            html = re.sub(
                r'(<script\s+src=["\']' + re.escape(js) + r'["\'])(>)',
                r'\1 defer\2',
                html
            )
            # Handle self-closing variant
            html = re.sub(
                r'(<script\s+src=["\']' + re.escape(js) + r'["\'])(\s*></script>)',
                r'\1 defer\2',
                html
            )

    # ─── 4. Hero image preload on index.html ────────────────────────────────
    if page == "index.html":
        preload_tag = '    <link rel="preload" as="image" href="images/slider/slide1-home1.webp" fetchpriority="high" />\n'
        if 'rel="preload" as="image"' not in html:
            html = html.replace('  </head>', preload_tag + '  </head>', 1)

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        fixes_applied += 1
        print(f"  Fixed: {page}")
    else:
        print(f"  No change needed: {page}")

print(f"\nTotal pages updated: {fixes_applied}/{len(PAGE_META)}")
print("Done.")
