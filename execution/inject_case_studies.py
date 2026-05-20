import os
import re

projects = {
    "case-study-bada.html": {
        "title": "Bada Language Institute Platform",
        "type": "Client / Organization",
        "industry": "Education / E-Learning",
        "stack": "Wix Studio",
        "url": "https://www.badaglobal-bli.com/",
        "desc": "A Learning Management System and corporate website for the Bada Language Institute, providing structured information about the institute, courses, and events.",
        "approach": "We engineered a robust digital platform to centralize the institute's course offerings and event schedules. The focus was on creating a highly accessible, user-centric interface that could scale with the institute's growing student base.",
        "outcomes": "The deployment resulted in increased student engagement, streamlined course registrations, and a fortified brand presence in the regional education sector."
    },
    "case-study-sgss.html": {
        "title": "Gurdwara Siri Guru Singh Sabha",
        "type": "Client / Organization",
        "industry": "Community / Religious",
        "stack": "React, TailwindCSS, TypeScript",
        "url": "https://sirigurusinghsabha.vercel.app/",
        "desc": "A comprehensive community portal for a Sikh temple, providing real-time information about the temple, events, services, and community activities.",
        "approach": "Built from the ground up using a modern React and TypeScript architecture, the platform was designed for high performance and maintainability. TailwindCSS was utilized to construct a responsive, culturally appropriate UI system.",
        "outcomes": "The secure, scalable platform successfully digitized community engagement, providing a reliable single source of truth for congregation updates and event coordination."
    },
    "case-study-racnyali.html": {
        "title": "Rotaract Club of Nyali Portal",
        "type": "Client / Organization",
        "industry": "Non-Profit / NGO",
        "stack": "React, TailwindCSS, TypeScript",
        "url": "https://rotaractnyali.org/",
        "desc": "A dedicated nonprofit organization website for the Rotaract Nyali group, designed to showcase ongoing community projects and manage organizational visibility.",
        "approach": "Our engineering team deployed a scalable TypeScript React application. The architecture prioritizes speed, accessibility, and content manageability to ensure volunteers and donors can easily navigate projects and initiatives.",
        "outcomes": "Enhanced digital credibility, improved donor transparency, and a high-performance web presence that scores perfectly on Core Web Vitals."
    },
    "case-study-transitflow.html": {
        "title": "Transit Flow Logistics",
        "type": "Internal Engineering Project",
        "industry": "Logistics & Supply Chain",
        "stack": "React, TailwindCSS, Figma",
        "url": "https://transit-flow-logistics.netlify.app",
        "desc": "A fully responsive, high-performance landing page system engineered for a modern logistics and transit company.",
        "approach": "This internal engineering project demonstrates our capability to rapidly prototype and deploy sector-specific landing pages. The development lifecycle moved seamlessly from Figma UX/UI design to a component-driven React frontend.",
        "outcomes": "A highly tuned digital asset demonstrating best practices in CSS Grid/Flexbox layouts, mobile-first responsiveness, and component reusability."
    },
    "case-study-audiophile.html": {
        "title": "Audiophile E-Commerce Architecture",
        "type": "Internal Engineering Project",
        "industry": "Retail E-Commerce",
        "stack": "React, TailwindCSS, Framer Motion",
        "url": "https://audiophile-estore.netlify.app",
        "desc": "A fully functional, deeply responsive e-commerce web application architecture designed for a premium consumer electronics retailer.",
        "approach": "This project showcases advanced state management, dynamic routing, and complex UI animations using Framer Motion. The engineering focus was on creating a friction-free checkout flow and a premium brand aesthetic.",
        "outcomes": "Proof of capability in delivering enterprise-grade modular e-commerce frontends with fluid state transitions and rigorous accessibility compliance."
    },
    "case-study-greenremedies.html": {
        "title": "Green Remedies Marketplace",
        "type": "Internal Engineering Project",
        "industry": "Health & Wellness E-Commerce",
        "stack": "React, TailwindCSS, Kinde Auth",
        "url": "https://thegreenremedies.com",
        "desc": "An open-source full-stack platform built in collaboration with product managers, designers, and developers to deploy an e-commerce web app for herbal products.",
        "approach": "We integrated Kinde Auth for robust identity and access management, while maintaining a strict component hierarchy in React. The codebase demonstrates cross-functional collaboration and enterprise security best practices.",
        "outcomes": "A secure, authenticated e-commerce environment featuring seamless UX, secure data flow, and highly optimized frontend painting."
    }
}

directory = r"c:\My Web Sites\ajnets"

for filename, data in projects.items():
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Page titles and breadcrumbs
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | AJNETWORKS Case Study</title>', html, flags=re.DOTALL)
    html = re.sub(r'<h1 class="page-title">.*?</h1>', f'<h1 class="page-title">{data["title"]}</h1>', html, flags=re.DOTALL)
    html = re.sub(r'<li class="active">.*?</li>', f'<li class="active">{data["title"]}</li>', html, flags=re.DOTALL)
    
    # 2. Main Title
    html = re.sub(r'<h2>.*?</h2>', f'<h2>{data["title"]}</h2>', html, flags=re.DOTALL, count=1)
    
    # 3. Breadcrumb parent update
    html = html.replace('<li><a href="./">Home</a></li>', '<li><a href="./">Home</a></li>\n                <li><a href="client-success.html">Client Success</a></li>')

    # 4. Project Details Blocks
    detail_blocks = re.findall(r'<div class="project-detail">.*?</div>', html, flags=re.DOTALL)
    if len(detail_blocks) >= 3:
        # Block 1: Type
        b1 = f'<div class="project-detail">\n                  <span>PROJECT TYPE:</span>\n                  <strong style="color: {"#0056b3" if "Internal" in data["type"] else "#28a745"}">{data["type"]}</strong>\n                </div>'
        html = html.replace(detail_blocks[0], b1)
        
        # Block 2: Tech Stack
        b2 = f'<div class="project-detail">\n                  <span>TECH STACK:</span>\n                  <strong>{data["stack"]}</strong>\n                </div>'
        html = html.replace(detail_blocks[1], b2)

        # Block 3: Live URL
        b3 = f'<div class="project-detail">\n                  <span>LIVE ENVIRONMENT:</span>\n                  <strong><a href="{data["url"]}" target="_blank" style="text-decoration: underline;">View Project</a></strong>\n                </div>'
        html = html.replace(detail_blocks[2], b3)

    # 5. Content Replacement
    # We will replace everything from <h3>How it Works</h3> down to <div class="blog-post projects-meta">
    # using a robust regex.
    content_pattern = re.compile(r'<h3>How it Works</h3>.*?(?=<div class="blog-post projects-meta">)', re.DOTALL)
    
    first_letter = data["desc"][0]
    rest_desc = data["desc"][1:]
    
    new_content = f"""<h3>Business Challenge & Engineering Approach</h3>
                <p>
                  <span class="drop-cap"><span class="drop-cap-letter">{first_letter}</span></span>{rest_desc}
                </p>
                <p>{data["approach"]}</p>
                <div class="space-20"></div>
                <h3>Measurable Outcomes & Impact</h3>
                <p style="border-left: 4px solid #0056b3; padding-left: 15px; font-style: italic;">
                  {data["outcomes"]}
                </p>
                <div class="space-40"></div>
                """
    
    html = re.sub(content_pattern, new_content, html)
    
    # 6. Remove Comments section completely (from <div id="comments"> to </form></div>)
    html = re.sub(r'<div id="comments".*?</form>\s*</div>', '', html, flags=re.DOTALL)
    
    # Write back
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Injected content into the 6 targeted case study files.")
