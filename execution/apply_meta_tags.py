from pathlib import Path
from bs4 import BeautifulSoup

root = Path(r"C:\My Web Sites\ajnets")

META_CONFIG = {
    "index.html": {
        "title": "AJNETWORKS - Technology Consulting & Engineering Delivery",
        "description": "AJNETWORKS is an enterprise technology consultancy in Nairobi, Kenya delivering strategic advisory, custom software engineering, cybersecurity, and cloud infrastructure solutions across East Africa.",
    },
    "company/about-us.html": {
        "title": "About Us | AJNETWORKS - Enterprise Technology Consulting",
        "description": "Learn about AJNETWORKS — a technology consulting partner combining strategic insight with hands-on software engineering, cybersecurity, and cloud infrastructure across Kenya and East Africa.",
    },
    "company/book-consultation.html": {
        "title": "Contact Us & Book Consultation | AJNETWORKS",
        "description": "Schedule a technology strategy consultation with AJNETWORKS in Nairobi & Mombasa. Connect with our engineering and cybersecurity advisors today.",
    },
    "company/faq.html": {
        "title": "Frequently Asked Questions | AJNETWORKS",
        "description": "Find answers to frequently asked questions about AJNETWORKS technology consulting services, software development, cybersecurity assurance, pricing, and project delivery.",
    },
    "elements/elements.html": {
        "title": "UI Elements & Design Components | AJNETWORKS",
        "description": "Explore the UI components, design tokens, and frontend elements powering the AJNETWORKS enterprise digital platform.",
    },
    "insights/insights.html": {
        "title": "Insights & Technology Articles | AJNETWORKS",
        "description": "Read industry perspectives, architecture blueprints, and technology strategy insights from senior consultants and engineers at AJNETWORKS.",
    },
    "insights/post.html": {
        "title": "The Importance of Strategic Technology Consulting | AJNETWORKS",
        "description": "Discover why strategic technology consulting is critical for sustainable digital transformation, ROI alignment, and scalable software architecture.",
    },
    "portfolio/client-success.html": {
        "title": "Client Success & Case Studies | AJNETWORKS",
        "description": "Explore AJNETWORKS client engagements across software engineering, cybersecurity, and IT infrastructure delivering measurable business impact.",
    },
    "portfolio/case-study-audiophile.html": {
        "title": "Audiophile E-Commerce Case Study | AJNETWORKS",
        "description": "Case study on engineering a high-performance e-commerce platform with multi-step checkout, responsive galleries, and state persistence by AJNETWORKS.",
    },
    "portfolio/case-study-bada.html": {
        "title": "Bada Language Institute Case Study | AJNETWORKS",
        "description": "How AJNETWORKS engineered an LMS and corporate web platform for Bada Language Institute with course management and digital enrolment.",
    },
    "portfolio/case-study-crappo.html": {
        "title": "Crappo Crypto Platform Case Study | AJNETWORKS",
        "description": "Case study on developing a modern cryptocurrency platform with live market data integration and responsive UI by AJNETWORKS.",
    },
    "portfolio/case-study-greenremedies.html": {
        "title": "Green Remedies E-Commerce Case Study | AJNETWORKS",
        "description": "Case study on building an authenticated e-commerce application for herbal products with Kinde Auth, secure checkout, and inventory tracking.",
    },
    "portfolio/case-study-racnyali.html": {
        "title": "Rotaract Club Nyali Portal Case Study | AJNETWORKS",
        "description": "How AJNETWORKS delivered a community engagement portal for Rotaract Club of Nyali with membership management and event registration.",
    },
    "portfolio/case-study-sgss.html": {
        "title": "SGSS Mombasa Medical Fund Case Study | AJNETWORKS",
        "description": "How AJNETWORKS built a secure medical fund management portal for SGSS Mombasa with donor tracking and patient record security.",
    },
    "portfolio/case-study-transitflow.html": {
        "title": "Transit Flow Logistics Case Study | AJNETWORKS",
        "description": "Case study on creating a high-performance, responsive logistics landing platform engineered with modular web architecture by AJNETWORKS.",
    },
    "services/services.html": {
        "title": "Our Services - Consulting & Engineering | AJNETWORKS",
        "description": "Explore AJNETWORKS consulting practices: Technology Strategy, Software Engineering, Cybersecurity, Infrastructure, and Performance SEO across East Africa.",
    },
    "services/technology-strategy.html": {
        "title": "Technology & Digital Strategy Consulting | AJNETWORKS",
        "description": "Technology and digital strategy consulting in Kenya. Business analysis, systems audits, IT roadmaps, and vendor advisory from AJNETWORKS.",
    },
    "services/software-engineering.html": {
        "title": "Custom Software Engineering Services | AJNETWORKS",
        "description": "Custom software engineering in Kenya. Web applications, enterprise systems, and mobile platforms built with security-first architecture by AJNETWORKS.",
    },
    "services/cybersecurity.html": {
        "title": "Cybersecurity & Infrastructure Assurance | AJNETWORKS",
        "description": "Cybersecurity and infrastructure assurance in Kenya. Vulnerability assessments, secure architecture, and compliance readiness by AJNETWORKS.",
    },
    "services/networking.html": {
        "title": "Networking & IT Infrastructure Solutions | AJNETWORKS",
        "description": "Enterprise networking and IT infrastructure services in Kenya. Network design, server management, VPNs, and infrastructure monitoring from AJNETWORKS.",
    },
    "services/performance-seo.html": {
        "title": "Performance Engineering & Technical SEO | AJNETWORKS",
        "description": "Performance optimization and technical SEO in Kenya. Core Web Vitals optimization, search visibility, and speed engineering by AJNETWORKS.",
    },
}

for rel_path, config in META_CONFIG.items():
    file_path = root / rel_path
    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    # 1. Update <title>
    title_tag = soup.find("title")
    if title_tag:
        title_tag.string = config["title"]
    else:
        new_title = soup.new_tag("title")
        new_title.string = config["title"]
        if soup.head:
            soup.head.append(new_title)
            
    # 2. Update <meta name="description">
    desc_tag = soup.find("meta", attrs={"name": lambda x: x and x.lower() == "description"})
    if desc_tag:
        desc_tag["content"] = config["description"]
    else:
        new_desc = soup.new_tag("meta", attrs={"name": "description", "content": config["description"]})
        if soup.head:
            soup.head.append(new_desc)
            
    # 3. Update og:title and og:description if present
    og_title = soup.find("meta", attrs={"property": "og:title"})
    if og_title:
        og_title["content"] = config["title"]
    og_desc = soup.find("meta", attrs={"property": "og:description"})
    if og_desc:
        og_desc["content"] = config["description"]
        
    # 4. Update twitter:title and twitter:description if present
    tw_title = soup.find("meta", attrs={"name": "twitter:title"})
    if tw_title:
        tw_title["content"] = config["title"]
    tw_desc = soup.find("meta", attrs={"name": "twitter:description"})
    if tw_desc:
        tw_desc["content"] = config["description"]
        
    # Save back preserving utf-8
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Updated meta tags for {rel_path}")

print("\nDone updating all meta tags.")
