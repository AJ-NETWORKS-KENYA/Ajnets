import os, re

directory = r"c:\My Web Sites\ajnets"

case_studies = [
    {
        "file": "case-study-sgss.html",
        "title": "Siri Guru Singh Sabha Mombasa",
        "subtitle": "Community Portal",
        "breadcrumb": "sgss-mombasa",
        "tags": ["Community / Religious", "Client / Organization"],
        "tag_colors": ["amber", "green"],
        "stack": ["React", "TypeScript", "TailwindCSS", "Vercel"],
        "url": "https://sirigurusinghsabha.vercel.app/",
        "emoji": "🛕",
        "description": "A comprehensive community portal for a Sikh temple providing real-time information about temple events, prayer services, and community activities.",
        "challenge": "The Gurdwara required a centralized digital presence to communicate daily services, events, and community programs to its congregation — replacing fragmented WhatsApp group notifications and physical notice boards.",
        "approach": "We built a high-performance React and TypeScript application deployed on Vercel's global edge network. The architecture prioritises speed, accessibility, and content currency — featuring a dynamic event system and a responsive UI system with strong cultural design sensitivity.",
        "outcomes": [
            ("Digitized Congregation Management", "Real-time event listings and service announcements replaced informal communication channels."),
            ("Performance-Optimized Frontend", "Core Web Vitals achieving 95+ scores across LCP, FID, and CLS metrics."),
            ("Scalable Architecture", "TypeScript-first codebase designed for maintainability and future feature additions by any developer."),
        ]
    },
    {
        "file": "case-study-racnyali.html",
        "title": "Rotaract Club of Nyali",
        "subtitle": "Non-Profit Web Platform",
        "breadcrumb": "rotaract-nyali",
        "tags": ["Non-Profit / NGO", "Client / Organization"],
        "tag_colors": ["green", "blue"],
        "stack": ["React", "TypeScript", "TailwindCSS"],
        "url": "https://rotaractnyali.org/",
        "emoji": "🤝",
        "description": "A polished web presence for the Rotaract Nyali chapter showcasing community projects, team profiles, and event highlights.",
        "challenge": "The chapter needed a professional online identity to increase donor visibility, attract new members, and clearly communicate ongoing community programmes to a wider Mombasa audience.",
        "approach": "A TypeScript React application engineered for maximum performance and accessibility. The layout prioritises visual impact for project showcases, creating a compelling narrative of the chapter's community impact with a mobile-first, accessibility-compliant design system.",
        "outcomes": [
            ("100 Lighthouse Performance Score", "Achieved perfect Core Web Vitals scores — one of the fastest-loading non-profit sites in the region."),
            ("Enhanced Donor Transparency", "Clear project showcases directly communicate community impact, supporting fundraising and membership growth."),
            ("Digital Brand Credibility", "A polished online presence elevating the chapter's authority and community standing."),
        ]
    },
    {
        "file": "case-study-transitflow.html",
        "title": "Transit Flow Logistics",
        "subtitle": "Business Landing Page",
        "breadcrumb": "transit-flow",
        "tags": ["Logistics & Supply Chain", "Internal Engineering Project"],
        "tag_colors": ["blue", "green"],
        "stack": ["React", "TailwindCSS", "Figma"],
        "url": "https://transit-flow-logistics.netlify.app",
        "emoji": "🚛",
        "description": "A fully responsive, high-performance business landing page engineered for a modern logistics and transit company from Figma designs to production deployment.",
        "challenge": "Modern logistics companies require digital presence that communicates reliability, operational scale, and professionalism. The challenge was designing and deploying a conversion-optimized site that worked flawlessly across all device breakpoints.",
        "approach": "This internal engineering project demonstrates our full design-to-code delivery pipeline. Starting from Figma wireframes, we built a component-driven React architecture with TailwindCSS utility classes, implementing mobile-first CSS Grid and Flexbox layouts.",
        "outcomes": [
            ("Fully Responsive Across All Breakpoints", "Pixel-perfect fidelity from Figma designs on mobile, tablet, and desktop."),
            ("Production-Grade Component Architecture", "Reusable React components with clean prop interfaces for rapid future extension."),
            ("Conversion-Optimized Design", "Hero sections, service listings, and CTA placements designed to maximize engagement."),
        ]
    },
    {
        "file": "case-study-audiophile.html",
        "title": "Audiophile E-Commerce Architecture",
        "subtitle": "Online Retail Platform",
        "breadcrumb": "audiophile-ecommerce",
        "tags": ["Retail E-Commerce", "Internal Engineering Project"],
        "tag_colors": ["purple", "green"],
        "stack": ["React", "TailwindCSS", "Framer Motion", "Figma"],
        "url": "https://audiophile-estore.netlify.app",
        "emoji": "🎧",
        "description": "A premium e-commerce web application for a consumer electronics retailer featuring advanced state management, dynamic routing, and fluid Framer Motion animations.",
        "challenge": "E-commerce platforms must balance visual richness with technical performance. The challenge was delivering a premium product browsing and checkout experience that rivalled market leaders — without compromising load times or accessibility.",
        "approach": "We engineered a fully featured React e-commerce frontend with context-based global state management. Framer Motion was implemented for smooth page transitions and micro-interaction animations. The cart system maintains persistent state through session storage with optimistic UI updates.",
        "outcomes": [
            ("Enterprise-Grade Frontend Architecture", "Modular component system with clear separation of concerns for maintainability at scale."),
            ("Fluid Interaction Design", "Framer Motion animations deliver a premium perceived performance without impacting real LCP."),
            ("Complete Checkout Flow", "Full add-to-cart, quantity management, and order summary flow implemented with no backend dependency."),
        ]
    },
    {
        "file": "case-study-greenremedies.html",
        "title": "Green Remedies Marketplace",
        "subtitle": "E-Commerce with Auth",
        "breadcrumb": "green-remedies",
        "tags": ["Health & Wellness", "Internal Engineering Project"],
        "tag_colors": ["green", "blue"],
        "stack": ["React", "TailwindCSS", "Kinde Auth", "Figma"],
        "url": "https://thegreenremedies.com",
        "emoji": "🌿",
        "description": "An open-source authenticated e-commerce platform for herbal products, built collaboratively with a cross-functional product team including PMs, designers, and developers.",
        "challenge": "Building a secure, role-based e-commerce platform in a team environment requires disciplined architecture and clean authentication boundaries. The challenge was integrating modern identity management without coupling auth logic to business components.",
        "approach": "We integrated Kinde Auth for enterprise-quality SSO and role-based access control, decoupling identity management from product business logic. The React codebase follows strict component separation with centralized auth context, ensuring protected routes and session management work reliably across all user states.",
        "outcomes": [
            ("Secure Authentication Layer", "Kinde Auth integration delivers enterprise-grade identity management, SSO support, and role-based access."),
            ("Cross-Functional Collaboration", "Successfully shipped with a distributed team of product managers, UX designers, and frontend engineers."),
            ("Production-Ready Security Architecture", "Auth-aware routing, protected API calls, and secure session management implemented from day one."),
        ]
    },
]

tag_color_map = {
    "blue": ("#00d4ff", "rgba(0,212,255,0.1)"),
    "green": ("#00ff88", "rgba(0,255,136,0.1)"),
    "amber": ("#fbbf24", "rgba(245,158,11,0.1)"),
    "purple": ("#a78bfa", "rgba(124,58,237,0.1)"),
}

for cs in case_studies:
    tag_el = ""
    for tag, color_key in zip(cs["tags"], cs["tag_colors"]):
        c_text, c_bg = tag_color_map.get(color_key, ("#00d4ff","rgba(0,212,255,0.1)"))
        tag_el += f'<span class="px-3 py-1 rounded-full text-xs font-mono font-semibold" style="background:{c_bg};color:{c_text};">{tag}</span>'

    tech_el = "".join(f'<span class="tech-badge">{t}</span>' for t in cs["stack"])

    outcome_items = "".join(f"""
              <div class="flex items-start gap-3 p-4 rounded-xl" style="background:#0f1628;border:1px solid #1e2d4a;">
                <i class="fas fa-check-circle text-cyber-green mt-0.5"></i>
                <div>
                  <div class="text-sm font-semibold text-white">{o[0]}</div>
                  <div class="text-xs text-slate-500 mt-1">{o[1]}</div>
                </div>
              </div>""" for o in cs["outcomes"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Case Study: {cs['title']} - AJ Networks" />
  <title>{cs['title']} | Case Study — AJ Networks</title>
  <link rel="icon" type="image/svg+xml" href="images/favicon.svg" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{ 'cyber-blue':'#00d4ff','cyber-green':'#00ff88','cyber-dark':'#0a0e1a','cyber-card':'#0f1628','cyber-border':'#1e2d4a' }},
          fontFamily: {{ sans:['Inter','system-ui','sans-serif'], mono:['JetBrains Mono','monospace'] }},
        }},
      }},
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <style>
    body {{ background:#0a0e1a; color:#e2e8f0; font-family:'Inter',sans-serif; margin:0; }}
    .grid-bg {{ background-image: linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px); background-size:40px 40px; }}
    .gradient-text {{ background:linear-gradient(135deg,#00d4ff 0%,#00ff88 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }}
    .tech-badge {{ background:rgba(0,212,255,0.08); border:1px solid rgba(0,212,255,0.2); color:#00d4ff; font-family:'JetBrains Mono',monospace; font-size:.75rem; padding:4px 12px; border-radius:4px; display:inline-flex; align-items:center; gap:4px; }}
    .reveal {{ opacity:0; transform:translateY(20px); transition:opacity .6s,transform .6s; }}
    .reveal.visible {{ opacity:1; transform:translateY(0); }}
    ::-webkit-scrollbar{{width:6px}} ::-webkit-scrollbar-track{{background:#0a0e1a}} ::-webkit-scrollbar-thumb{{background:#1e2d4a;border-radius:3px}}
  </style>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('consent','default',{{'analytics_storage':'denied'}});</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-2E6LLT0TT7"></script>
  <script>gtag('js',new Date());gtag('config','G-2E6LLT0TT7');</script>
</head>
<body class="grid-bg">

  <nav class="fixed top-0 left-0 w-full z-50" style="background:rgba(10,14,26,0.9);backdrop-filter:blur(16px);border-bottom:1px solid #1e2d4a;">
    <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
      <a href="./" class="flex items-center gap-2">
        <img src="images/logo.svg" alt="AJ Networks" class="h-8" onerror="this.style.display='none'" />
        <span class="font-mono text-sm font-bold gradient-text hidden sm:block">AJ<span class="text-slate-300">NETWORKS</span></span>
      </a>
      <div class="hidden md:flex items-center gap-6 text-sm">
        <a href="./" class="text-slate-400 hover:text-cyber-blue transition">Home</a>
        <a href="about-us.html" class="text-slate-400 hover:text-cyber-blue transition">Who We Are</a>
        <a href="services.html" class="text-slate-400 hover:text-cyber-blue transition">Services</a>
        <a href="client-success.html" class="text-cyber-blue font-semibold">Client Success</a>
        <a href="insights.html" class="text-slate-400 hover:text-cyber-blue transition">Insights</a>
      </div>
      <a href="book-consultation.html" class="px-5 py-2 text-sm font-semibold rounded-lg text-cyber-dark hidden md:block" style="background:linear-gradient(135deg,#00d4ff,#00ff88);">Book Consultation</a>
    </div>
  </nav>

  <section class="pt-36 pb-16" style="border-bottom:1px solid #1e2d4a;">
    <div class="max-w-5xl mx-auto px-6">
      <nav class="flex items-center gap-2 text-xs font-mono text-slate-500 mb-8">
        <a href="./" class="hover:text-cyber-blue transition">~/home</a>
        <span class="text-cyber-blue">/</span>
        <a href="client-success.html" class="hover:text-cyber-blue transition">work</a>
        <span class="text-cyber-blue">/</span>
        <span class="text-cyber-blue">{cs['breadcrumb']}</span>
      </nav>
      <div class="flex items-center gap-4 mb-5 flex-wrap">{tag_el}</div>
      <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-4">{cs['title']}<br/><span class="gradient-text">{cs['subtitle']}</span></h1>
      <p class="text-slate-400 text-lg max-w-2xl mb-8">{cs['description']}</p>
      <div class="flex flex-wrap gap-3">
        {tech_el}
        <a href="{cs['url']}" target="_blank" rel="noopener" class="flex items-center gap-2 px-4 py-1.5 rounded-lg text-sm font-semibold text-cyber-dark ml-2" style="background:linear-gradient(135deg,#00d4ff,#00ff88);">
          <i class="fas fa-external-link-alt"></i> View Live Site
        </a>
      </div>
    </div>
  </section>

  <section class="py-20 reveal">
    <div class="max-w-5xl mx-auto px-6">
      <div class="grid lg:grid-cols-3 gap-12">
        <div class="lg:col-span-2 space-y-10">
          <div>
            <h2 class="text-2xl font-bold text-white mb-4 flex items-center gap-3">
              <span class="w-6 h-6 rounded flex items-center justify-center text-xs" style="background:#00d4ff;color:#000;font-weight:700;">01</span>
              Business Challenge
            </h2>
            <p class="text-slate-400 leading-relaxed">{cs['challenge']}</p>
          </div>
          <div>
            <h2 class="text-2xl font-bold text-white mb-4 flex items-center gap-3">
              <span class="w-6 h-6 rounded flex items-center justify-center text-xs" style="background:#00ff88;color:#000;font-weight:700;">02</span>
              Engineering Approach
            </h2>
            <p class="text-slate-400 leading-relaxed">{cs['approach']}</p>
          </div>
          <div>
            <h2 class="text-2xl font-bold text-white mb-5 flex items-center gap-3">
              <span class="w-6 h-6 rounded flex items-center justify-center text-xs" style="background:#7c3aed;color:#fff;font-weight:700;">03</span>
              Measurable Outcomes
            </h2>
            <div class="space-y-3">{outcome_items}</div>
          </div>
        </div>
        <div class="space-y-6">
          <div class="p-6 rounded-xl" style="background:#0f1628;border:1px solid #1e2d4a;">
            <h4 class="text-sm font-semibold text-slate-300 mb-4 font-mono uppercase tracking-wider">Project Details</h4>
            <div class="space-y-4">
              <div>
                <div class="text-xs text-slate-500 font-mono mb-1">CLIENT</div>
                <div class="text-sm text-white font-semibold">{cs['title']}</div>
              </div>
              <div>
                <div class="text-xs text-slate-500 font-mono mb-1">INDUSTRY</div>
                <div class="text-sm text-white">{cs['tags'][0]}</div>
              </div>
              <div>
                <div class="text-xs text-slate-500 font-mono mb-1">TYPE</div>
                <div class="text-sm font-semibold" style="color:#00d4ff;">{cs['tags'][1]}</div>
              </div>
              <div>
                <div class="text-xs text-slate-500 font-mono mb-1">TECH STACK</div>
                <div class="text-sm text-white">{', '.join(cs['stack'])}</div>
              </div>
              <div>
                <div class="text-xs text-slate-500 font-mono mb-1">STATUS</div>
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-cyber-green animate-pulse"></span>
                  <span class="text-sm text-cyber-green font-mono">LIVE</span>
                </div>
              </div>
            </div>
          </div>
          <a href="{cs['url']}" target="_blank" rel="noopener" class="block w-full py-3 text-sm font-semibold text-center rounded-lg text-cyber-dark" style="background:linear-gradient(135deg,#00d4ff,#00ff88);">View Live Site <i class="fas fa-external-link-alt ml-1"></i></a>
          <a href="client-success.html" class="block w-full py-3 text-sm font-semibold text-center rounded-lg text-slate-300" style="border:1px solid #1e2d4a;background:rgba(255,255,255,0.03);">← All Case Studies</a>
        </div>
      </div>
    </div>
  </section>

  <section class="py-20 reveal" style="border-top:1px solid #1e2d4a;">
    <div class="max-w-2xl mx-auto px-6 text-center">
      <h2 class="text-3xl font-bold text-white mb-4">Ready to build your platform?</h2>
      <p class="text-slate-400 mb-8">Let AJ Networks engineer your next business-critical digital system.</p>
      <a href="book-consultation.html" class="inline-block px-8 py-3 rounded-lg font-semibold text-cyber-dark" style="background:linear-gradient(135deg,#00d4ff,#00ff88);">Book Consultation</a>
    </div>
  </section>

  <footer style="background:#080c18;border-top:1px solid #1e2d4a;" class="py-8">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-4">
      <p class="text-sm text-slate-500 font-mono">© 2026 AJNETWORKS. All Rights Reserved.</p>
      <nav class="flex gap-6 text-sm">
        <a href="./" class="text-slate-500 hover:text-cyber-blue transition">Home</a>
        <a href="services.html" class="text-slate-500 hover:text-cyber-blue transition">Services</a>
        <a href="client-success.html" class="text-cyber-blue">Client Success</a>
        <a href="book-consultation.html" class="text-slate-500 hover:text-cyber-blue transition">Book Consultation</a>
      </nav>
    </div>
  </footer>

  <script>
    const reveals = document.querySelectorAll('.reveal');
    reveals.forEach(el => {{
      new IntersectionObserver((entries) => entries.forEach(e => {{ if(e.isIntersecting) e.target.classList.add('visible'); }}), {{threshold:0.1}}).observe(el);
    }});
  </script>
  <link rel="stylesheet" href="css/cookie-consent.css" />
  <script src="js/cookie-consent.js" defer></script>
</body>
</html>
"""

    filepath = os.path.join(directory, cs["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written {cs['file']}")

print("All case study pages rebuilt.")
