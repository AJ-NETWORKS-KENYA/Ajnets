"""
Phase 5: Rebuild all case study pages to the AJNETWORKS enterprise design system.
Replaces Tailwind/cyber-themed markup with Bootstrap brand components.
"""
import os

BASE = r"c:\My Web Sites\ajnets\portfolio"

# Shared HTML template components
HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="facebook-domain-verification" content="r5liwwbty07nhozk87d1uwkz4fyp70" />
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="{meta_desc}" />
    <meta name="keywords" content="{keywords}" />
    <meta name="author" content="AJNETWORKS" />
    <title>{title} | Case Study — AJNETWORKS</title>

    <link rel="icon" type="image/svg+xml" href="/images/favicon.svg" />
    <link rel="icon" type="image/png" sizes="96x96" href="/images/favicon-96x96.png" />
    <link rel="shortcut icon" href="/images/favicon.ico" />
    <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png" />
    <link rel="manifest" href="/images/site.webmanifest" />

    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/font-awesome.min.css" />
    <link rel="stylesheet" href="/css/flaticon.css" />
    <link rel="stylesheet" href="/css/owl.carousel.min.css" />
    <link rel="stylesheet" href="/css/owl.theme.css" />
    <link rel="stylesheet" href="/css/magnific-popup.css" />
    <link rel="stylesheet" href="/style.css" />
    <link rel="stylesheet" href="/css/logo-ajnetworks.css" />
    <link rel="stylesheet" href="/css/cookie-consent.css" />
    <link rel="stylesheet" href="/css/trust-strip.css" />
    <script src="/js/cookie-consent.js" defer></script>

    <!-- Google Consent Mode v2 -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{ dataLayer.push(arguments); }}
      gtag("consent", "default", {{
        ad_storage: "denied",
        ad_user_data: "denied",
        ad_personalization: "denied",
        analytics_storage: "denied",
      }});
    </script>

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-2E6LLT0TT7"></script>
    <script>
      gtag("js", new Date());
      gtag("config", "G-2E6LLT0TT7");
    </script>

    <!-- LinkedIn Insight Tag -->
    <script type="text/javascript">
      _linkedin_partner_id = "YOUR_LINKEDIN_PID";
      window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
      window._linkedin_data_partner_ids.push(_linkedin_partner_id);
    </script>
    <script type="text/javascript">
      (function (l) {{
        if (!l) {{
          window.lintrk = function (a, b) {{ window.lintrk.q.push([a, b]); }};
          window.lintrk.q = [];
        }}
        var s = document.getElementsByTagName("script")[0];
        var b = document.createElement("script");
        b.type = "text/javascript"; b.async = true;
        b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
        s.parentNode.insertBefore(b, s);
      }})(window.lintrk);
    </script>
    <noscript>
      <img height="1" width="1" style="display: none" alt="" src="https://px.ads.linkedin.com/collect/?pid=YOUR_LINKEDIN_PID&amp;fmt=gif" />
    </noscript>

    <!-- Canonical & Open Graph -->
    <link rel="canonical" href="https://ajnetworkskenya.it.com/portfolio/{slug}" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://ajnetworkskenya.it.com/portfolio/{slug}" />
    <meta property="og:title" content="{title} | Case Study — AJNETWORKS" />
    <meta property="og:description" content="{meta_desc}" />
    <meta property="og:image" content="https://ajnetworkskenya.it.com/images/og-home.jpg" />
    <meta property="og:site_name" content="AJNETWORKS" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title} | Case Study — AJNETWORKS" />
    <meta name="twitter:description" content="{meta_desc}" />

    <!-- BreadcrumbList Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://ajnetworkskenya.it.com/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Client Success", "item": "https://ajnetworkskenya.it.com/portfolio/client-success" }},
        {{ "@type": "ListItem", "position": 3, "name": "{title}", "item": "https://ajnetworkskenya.it.com/portfolio/{slug}" }}
      ]
    }}
    </script>
</head>
"""

HEADER = """
<body>

    <!-- Skip to main content link for accessibility -->
    <a href="#content" class="skip-link">Skip to main content</a>

    <header
      id="site-header"
      class="site-header header-style-2 header-fullwidth sticky-header header-static"
    >
      <div class="header-topbar">
        <div class="octf-area-wrap">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-6">
                <ul class="topbar-info">
                  <li><i class="fas fa-envelope"></i><a href="mailto:hello@ajnetworkskenya.it.com">hello&#64;ajnetworkskenya.it.com</a></li>
                  <li><i class="fas fa-clock"></i> Mon - Sat: 8.00 am - 7.00 pm</li>
                </ul>
              </div>
              <div class="col-md-6 text-right">
                <div class="topbar-right">
                  <ul class="extra-text">
                    <li>We are creative, ambitious and ready for challenges! <a href="/company/book-consultation">Book Advisory Session</a></li>
                  </ul>
                  <ul class="social-list">
                    <li><a href="https://twitter.com/ajnetworks" target="_blank" rel="noopener" aria-label="Twitter"><i class="fab fa-twitter"></i></a></li>
                    <li><a href="https://facebook.com/ajnetworks" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                    <li><a href="https://linkedin.com/company/ajnetworks" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a></li>
                    <li><a href="https://instagram.com/ajnetworks" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="octf-main-header">
        <div class="octf-area-wrap">
          <div class="container-fluid octf-mainbar-container">
            <div class="octf-mainbar">
              <div class="octf-mainbar-row octf-row">
                <div class="octf-col logo-col">
                  <div id="site-logo" class="site-logo">
                    <a href="/"><img src="/images/logo.svg" alt="AJNETWORKS" /></a>
                  </div>
                </div>
                <div class="octf-col menu-col">
                  <nav id="site-navigation" class="main-navigation" role="navigation" aria-label="Main Menu">
                    <ul class="menu">
                      <li><a href="/">Home</a></li>
                      <li><a href="/company/about-us">Who We Are</a></li>
                      <li class="menu-item-has-children">
                        <a href="/services/services">Services</a>
                        <ul class="sub-menu">
                          <li><a href="/services/technology-strategy">Technology &amp; Digital Strategy</a></li>
                          <li><a href="/services/software-engineering">Software Engineering</a></li>
                          <li><a href="/services/cybersecurity">Cybersecurity &amp; Assurance</a></li>
                          <li><a href="/services/networking">Networking &amp; IT Infrastructure</a></li>
                          <li><a href="/services/performance-seo">Performance &amp; SEO</a></li>
                        </ul>
                      </li>
                      <li class="current-menu-item"><a href="/portfolio/client-success">Client Success</a></li>
                      <li><a href="/insights/insights">Insights</a></li>
                      <li><a href="/company/book-consultation">Book Consultation</a></li>
                    </ul>
                  </nav>
                </div>
                <div class="octf-col cta-col text-right">
                  <div class="octf-btn-cta">
                    <div class="octf-header-module">
                      <div class="btn-cta-group btn-cta-header">
                        <a class="octf-btn octf-btn-third" href="/company/book-consultation">Request Consultation</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="header_mobile">
        <div class="container">
          <div class="mlogo_wrapper clearfix">
            <div class="mobile_logo">
              <a href="/"><img src="/images/logo.svg" alt="AJNETWORKS" /></a>
            </div>
            <div id="mmenu_toggle">
              <button aria-label="Open navigation menu" aria-expanded="false"></button>
            </div>
          </div>
          <div class="mmenu_wrapper">
            <div class="mobile_nav collapse">
              <ul id="menu-main-menu" class="mobile_mainmenu">
                <li><a href="/">Home</a></li>
                <li><a href="/company/about-us">Who We Are</a></li>
                <li class="menu-item-has-children">
                  <a href="/services/services">Services</a>
                  <ul class="sub-menu">
                    <li><a href="/services/technology-strategy">Technology &amp; Digital Strategy</a></li>
                    <li><a href="/services/software-engineering">Software Engineering</a></li>
                    <li><a href="/services/cybersecurity">Cybersecurity &amp; Assurance</a></li>
                    <li><a href="/services/networking">Networking &amp; IT Infrastructure</a></li>
                    <li><a href="/services/performance-seo">Performance &amp; SEO</a></li>
                  </ul>
                </li>
                <li><a href="/portfolio/client-success">Client Success</a></li>
                <li><a href="/insights/insights">Insights</a></li>
                <li><a href="/company/book-consultation">Book Consultation</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div id="content" class="page-wrap">
"""

FOOTER = """
    </div>

    <footer id="site-footer" class="site-footer footer-v1">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-sm-6 col-12">
            <div class="widget-footer">
              <h5 class="text-white">Services</h5>
              <ul class="list-items">
                <li class="list-item"><a href="/services/technology-strategy">Technology &amp; Strategy</a></li>
                <li class="list-item"><a href="/services/software-engineering">Software Engineering</a></li>
                <li class="list-item"><a href="/services/cybersecurity">Cybersecurity &amp; Assurance</a></li>
                <li class="list-item"><a href="/services/networking">Networking &amp; Infrastructure</a></li>
                <li class="list-item"><a href="/services/performance-seo">Performance &amp; SEO</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 col-12">
            <div class="widget-footer">
              <h5 class="text-white">Quick Links</h5>
              <ul class="list-items">
                <li class="list-item"><a href="/company/about-us">Who We Are</a></li>
                <li class="list-item"><a href="/portfolio/client-success">Client Success</a></li>
                <li class="list-item"><a href="/insights/insights">Insights</a></li>
                <li class="list-item"><a href="/company/book-consultation">Book Consultation</a></li>
                <li class="list-item"><a href="/company/faq">FAQ</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 col-12">
            <div class="widget-footer">
              <h5 class="text-white">Operations</h5>
              <p>AJNETWORKS is a technology consulting firm delivering secure, scalable digital systems across East Africa.</p>
              <p><strong>HQ:</strong> Nairobi, Kenya<br /><strong>Operations:</strong> Kigali, Rwanda</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6 col-12">
            <div class="widget-footer">
              <h5 class="text-white">Get In Touch</h5>
              <div class="footer-contact-info">
                <p><i class="fas fa-envelope"></i> <a href="mailto:hello@ajnetworkskenya.it.com">hello&#64;ajnetworkskenya.it.com</a></p>
                <p><i class="fas fa-phone-alt"></i> +254 758 238 617</p>
                <p><i class="fas fa-clock"></i> Mon - Sat: 8:00 AM - 7:00 PM</p>
                <a href="/company/book-consultation" class="octf-btn octf-btn-primary mt-3">Book Strategy Call</a>
              </div>
            </div>
          </div>
        </div>
        <div class="row mt-65">
          <div class="col-md-6 mb-4 mb-md-0">
            <img src="/images/logo.svg" alt="AJNETWORKS Logo" />
          </div>
          <div class="col-md-6 text-left text-md-right align-self-center">
            <p class="copyright-text">Copyright &copy; 2026 AJNETWORKS. All Rights Reserved.</p>
          </div>
        </div>
      </div>
    </footer>

    <script src="/js/jquery.min.js"></script>
    <script src="/js/jquery.magnific-popup.min.js" defer></script>
    <script src="/js/jquery.isotope.min.js" defer></script>
    <script src="/js/owl.carousel.min.js" defer></script>
    <script src="/js/easypiechart.min.js" defer></script>
    <script src="/js/jquery.countdown.min.js" defer></script>
    <script src="/js/scripts.js" defer></script>
    <script src="/js/header-mobile.js" defer></script>

    <!-- Cookie Consent Banner -->
    <div id="cookie-consent-banner">
      <div class="cookie-content">
        <div class="cookie-text">
          <h3>We value your privacy</h3>
          <p>We use cookies to enhance your browsing experience, serve personalized content, and analyze our traffic. By clicking "Accept", you consent to our use of cookies.</p>
        </div>
        <div class="cookie-buttons">
          <button id="btn-reject-cookies" class="cookie-btn reject">Decline</button>
          <button id="btn-accept-cookies" class="cookie-btn accept">Accept</button>
        </div>
      </div>
    </div>

</body>
</html>
"""


def build_case_study_body(d):
    """Build the page-specific body content for a case study."""
    # Build tech badges HTML
    tech_html = "".join(f'<span class="tech-badge">{t}</span> ' for t in d["tech"])

    # Live site link
    live_link = ""
    if d.get("live_url"):
        live_link = f'<a href="{d["live_url"]}" target="_blank" rel="noopener" class="octf-btn octf-btn-primary mt-3"><i class="fas fa-external-link-alt"></i> View Live Site</a>'

    # Build outcomes HTML
    outcomes_html = ""
    for o in d["outcomes"]:
        outcomes_html += f"""
                  <li>
                    <strong>{o["label"]}</strong><br />
                    {o["detail"]}
                  </li>"""

    # Build sidebar meta
    sidebar_meta = ""
    for item in d["sidebar"]:
        sidebar_meta += f"""
                  <li class="sidebar-meta-item">
                    <div class="sidebar-meta-label">{item["label"]}</div>
                    <div class="sidebar-meta-value">{item["value"]}</div>
                  </li>"""

    # Build prev/next nav
    nav_prev = ""
    nav_next = ""
    if d.get("prev"):
        nav_prev = f"""
              <a href="/portfolio/{d['prev']['slug']}" class="case-study-nav-item prev">
                <span class="case-nav-label"><i class="fas fa-arrow-left"></i> Previous</span>
                <span class="case-nav-title">{d['prev']['title']}</span>
              </a>"""
    if d.get("next"):
        nav_next = f"""
              <a href="/portfolio/{d['next']['slug']}" class="case-study-nav-item next">
                <span class="case-nav-label">Next <i class="fas fa-arrow-right"></i></span>
                <span class="case-nav-title">{d['next']['title']}</span>
              </a>"""

    return f"""
      <!-- Page Hero -->
      <div class="page-hero" style="background-image: url('{d["hero_img"]}');">
        <div class="container">
          <nav class="breadcrumb-nav" aria-label="Breadcrumb">
            <a href="/">Home</a>
            <span class="separator">/</span>
            <a href="/portfolio/client-success">Client Success</a>
            <span class="separator">/</span>
            <span class="current">{d["title"]}</span>
          </nav>
          <h1>{d["title"]}</h1>
          <p style="color: rgba(255,255,255,0.75); font-size: 17px; max-width: 600px; margin-top: 15px;">
            {d["subtitle"]}
          </p>
          <div class="mt-4">
            {tech_html}
          </div>
        </div>
      </div>

      <!-- Case Study Content -->
      <section class="section-padd">
        <div class="container">
          <div class="row">

            <!-- Main Content Column -->
            <div class="col-lg-8">

              <!-- Business Challenge -->
              <div class="mb-5">
                <div class="ot-heading">
                  <span>// the challenge</span>
                  <h2 class="main-heading">Business Challenge</h2>
                </div>
                <p>{d["challenge"]}</p>
              </div>

              <!-- Engineering Approach -->
              <div class="mb-5">
                <div class="ot-heading">
                  <span>// our approach</span>
                  <h2 class="main-heading">Engineering Approach</h2>
                </div>
                <p>{d["approach"]}</p>
              </div>

              <!-- Measurable Outcomes -->
              <div class="outcome-box">
                <h3>Measurable Outcomes</h3>
                <ul class="outcome-list">{outcomes_html}
                </ul>
              </div>

              {live_link}

              <!-- Case Study Navigation -->
              <nav class="case-study-nav" aria-label="Case study navigation">
                {nav_prev}
                {nav_next}
              </nav>

            </div>

            <!-- Sidebar -->
            <div class="col-lg-4">
              <div class="case-study-sidebar">
                <h4>Project Details</h4>
                <ul class="sidebar-meta-list">{sidebar_meta}
                </ul>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- CTA Section -->
      <section class="section-padd" style="background: var(--light-bg);">
        <div class="container">
          <div class="cta">
            <div class="row">
              <div class="col-md-8 text-md-left text-center mb-4 mb-md-0">
                <div class="ot-heading">
                  <span>// your challenge, our expertise</span>
                  <h2 class="main-heading">Your business challenge could be our next success story.</h2>
                </div>
              </div>
              <div class="col-md-4 text-md-right text-center align-self-end">
                <a href="/company/book-consultation" class="octf-btn octf-btn-primary">Book Advisory Session</a>
              </div>
            </div>
          </div>
        </div>
      </section>
"""


# ======================================================================
# CASE STUDY DATA
# ======================================================================

CASE_STUDIES = [
    {
        "slug": "case-study-bada",
        "title": "Bada Language Institute",
        "meta_desc": "AJNETWORKS engineered a comprehensive LMS and corporate web platform for Bada Language Institute, delivering structured course management, event scheduling, and digital enrolment.",
        "keywords": "Bada Language Institute, LMS platform, education technology, Wix Studio, course management",
        "subtitle": "LMS and corporate web platform delivering structured course management, event scheduling, and digital enrolment for a regional education provider.",
        "hero_img": "/images/projects/project7-720x520.jpg",
        "tech": ["Wix Studio", "CMS", "SEO Optimization", "LMS Design"],
        "challenge": "The Bada Language Institute required a professional digital presence capable of centralising course listings, student communication, and event scheduling. Their legacy operations relied on manual processes and informal channels, limiting enrolment reach and brand credibility in the regional education market.",
        "approach": "We selected Wix Studio as the platform of choice to deliver maximum flexibility and maintainability without imposing custom code overhead on a non-technical team. The architecture structured the LMS into clearly separated content modules — Courses, Events, and Enrolment — ensuring each area could be independently updated. A robust SEO foundation was implemented across all pages including structured data markup, canonical links, and optimised meta descriptions, ensuring the institute ranked for competitive education keywords in Mombasa and the wider East African region.",
        "outcomes": [
            {"label": "Streamlined Course Registrations", "detail": "Students can browse, register, and pay for courses fully online — eliminating manual enrolment paperwork."},
            {"label": "Increased Student Engagement", "detail": "Dynamic event listings and real-time notifications increased community engagement with institute activities."},
            {"label": "Fortified Brand Presence", "detail": "A polished, professional digital identity elevating the institute's authority in the regional education sector."},
        ],
        "live_url": "https://www.badaglobal-bli.com/",
        "sidebar": [
            {"label": "Client", "value": "Bada Language Institute"},
            {"label": "Industry", "value": "Education / E-Learning"},
            {"label": "Type", "value": "Client Engagement"},
            {"label": "Platform", "value": "Wix Studio"},
            {"label": "Status", "value": "Live"},
        ],
        "prev": None,
        "next": {"slug": "case-study-sgss", "title": "SGSS Mombasa Medical Fund"},
    },
    {
        "slug": "case-study-sgss",
        "title": "SGSS Mombasa Medical Fund",
        "meta_desc": "AJNETWORKS built a secure medical fund management portal for SGSS Mombasa with donor tracking, patient records security, and real-time community health reporting.",
        "keywords": "SGSS Mombasa, medical fund portal, healthcare technology, community health, secure records",
        "subtitle": "Secure medical fund management portal with donor tracking, patient records security, and real-time reporting for a community healthcare organisation.",
        "hero_img": "/images/projects/project3-720x520.jpg",
        "tech": ["WordPress", "PHP", "MySQL", "Security Hardening"],
        "challenge": "SGSS Mombasa needed a centralised digital platform to manage their community medical fund — replacing spreadsheet-based tracking of donor contributions, patient records, and fund disbursements. Data integrity and patient privacy were paramount concerns.",
        "approach": "We engineered a WordPress-based portal with custom post types for donor management, patient records, and fund allocation tracking. Security hardening was applied at every layer: SSL enforcement, role-based access control, and encrypted data storage for sensitive patient information. Real-time dashboards were built to give administrators immediate visibility into fund balances and disbursement patterns.",
        "outcomes": [
            {"label": "Secured Patient Records", "detail": "All sensitive patient data encrypted at rest and in transit, with role-based access ensuring only authorised staff can view records."},
            {"label": "Transparent Fund Management", "detail": "Real-time dashboards replaced manual spreadsheets, providing instant visibility into contributions and disbursements."},
            {"label": "Community Trust", "detail": "A professional digital presence strengthened donor confidence and community trust in the fund's operations."},
        ],
        "live_url": None,
        "sidebar": [
            {"label": "Client", "value": "SGSS Mombasa"},
            {"label": "Industry", "value": "Healthcare / Community"},
            {"label": "Type", "value": "Client Engagement"},
            {"label": "Platform", "value": "WordPress / PHP"},
            {"label": "Status", "value": "Deployed"},
        ],
        "prev": {"slug": "case-study-bada", "title": "Bada Language Institute"},
        "next": {"slug": "case-study-racnyali", "title": "Rotaract Club Nyali"},
    },
    {
        "slug": "case-study-racnyali",
        "title": "Rotaract Club Nyali",
        "meta_desc": "AJNETWORKS delivered a community engagement portal for the Rotaract Club of Nyali with membership management, event registration, and project tracking.",
        "keywords": "Rotaract Nyali, community portal, membership management, event registration, NGO technology",
        "subtitle": "Community engagement portal with membership management, event registration, and project tracking for a Rotary-affiliated service organisation.",
        "hero_img": "/images/projects/project-720x520.jpg",
        "tech": ["WordPress", "Custom Theme", "Event Management", "Responsive Design"],
        "challenge": "The Rotaract Club of Nyali needed a digital platform to coordinate membership, track community service projects, and manage event registrations. All activities were previously coordinated through fragmented WhatsApp groups and manual spreadsheets.",
        "approach": "We built a custom WordPress-based portal with integrated membership management, event registration forms, and project tracking dashboards. The design was mobile-first to ensure accessibility for members primarily using smartphones. Custom taxonomies organised projects by service area, enabling leadership to generate impact reports across different community initiatives.",
        "outcomes": [
            {"label": "Streamlined Member Operations", "detail": "Centralised membership records replaced fragmented communication channels, improving coordination and reducing administrative overhead."},
            {"label": "Event Registration Automation", "detail": "Online event registration eliminated manual sign-ups, providing real-time attendee counts and automated confirmation emails."},
            {"label": "Project Impact Visibility", "detail": "Structured project tracking enabled leadership to generate service area reports and demonstrate community impact to Rotary International."},
        ],
        "live_url": None,
        "sidebar": [
            {"label": "Client", "value": "Rotaract Club of Nyali"},
            {"label": "Industry", "value": "NGO / Community"},
            {"label": "Type", "value": "Client Engagement"},
            {"label": "Platform", "value": "WordPress"},
            {"label": "Status", "value": "Deployed"},
        ],
        "prev": {"slug": "case-study-sgss", "title": "SGSS Mombasa Medical Fund"},
        "next": {"slug": "case-study-crappo", "title": "Crappo Crypto Platform"},
    },
    {
        "slug": "case-study-crappo",
        "title": "Crappo Crypto Platform",
        "meta_desc": "Engineering showcase: Modern cryptocurrency investment platform with live market data integration, secure wallet connections, and a sleek dark-mode UI built by AJNETWORKS.",
        "keywords": "crypto platform, fintech UI, dark mode design, cryptocurrency, engineering showcase",
        "subtitle": "Modern cryptocurrency investment platform featuring live market data, secure wallet connections, and sleek dark-mode UI components.",
        "hero_img": "/images/projects/project4-720x520.jpg",
        "tech": ["React", "REST API", "Chart.js", "Dark Mode UI"],
        "challenge": "This internal engineering project explored real-time data integration challenges common in fintech applications — specifically, rendering live cryptocurrency market data with responsive chart visualisations while maintaining sub-second UI responsiveness.",
        "approach": "Built as a single-page React application with Chart.js for real-time market visualisations. The architecture implemented efficient WebSocket-based data streams for live price updates, lazy-loaded component modules for performance, and a comprehensive dark-mode design system with accessible contrast ratios throughout.",
        "outcomes": [
            {"label": "Real-Time Data Rendering", "detail": "Live market data visualisation with sub-second updates demonstrating efficient WebSocket integration patterns."},
            {"label": "Accessible Dark-Mode System", "detail": "Complete dark-mode design system meeting WCAG 2.1 AA contrast requirements across all interactive elements."},
            {"label": "Component Architecture", "detail": "Modular React component library with documented props, enabling rapid prototyping of fintech-grade interfaces."},
        ],
        "live_url": None,
        "sidebar": [
            {"label": "Project", "value": "Crappo Crypto Platform"},
            {"label": "Industry", "value": "FinTech / Crypto"},
            {"label": "Type", "value": "Internal Engineering"},
            {"label": "Stack", "value": "React / Chart.js"},
            {"label": "Status", "value": "Showcase"},
        ],
        "prev": {"slug": "case-study-racnyali", "title": "Rotaract Club Nyali"},
        "next": {"slug": "case-study-audiophile", "title": "Audiophile E-Commerce"},
    },
    {
        "slug": "case-study-audiophile",
        "title": "Audiophile E-Commerce",
        "meta_desc": "Engineering showcase: Premium audio equipment e-commerce platform with multi-step checkout, product filtering, responsive galleries, and cart persistence built by AJNETWORKS.",
        "keywords": "e-commerce platform, audiophile, product catalogue, checkout flow, engineering showcase",
        "subtitle": "Premium audio equipment e-commerce platform with multi-step checkout, product filtering, responsive image galleries, and cart persistence.",
        "hero_img": "/images/projects/project8-720x520.jpg",
        "tech": ["React", "Redux", "Stripe API", "Responsive Design"],
        "challenge": "This internal project explored the full complexity of e-commerce user flows — product discovery, filtering, cart management, and multi-step checkout — with particular focus on cart state persistence and responsive product image galleries.",
        "approach": "Engineered as a React/Redux application with a normalised product data store. The checkout flow implements a multi-step form with validation at each stage, address autocomplete, and Stripe payment integration. Product galleries use progressive image loading with responsive srcset definitions, ensuring fast load times across device sizes. Cart state persists via localStorage with optimistic UI updates.",
        "outcomes": [
            {"label": "Multi-Step Checkout Flow", "detail": "Complete checkout pipeline with form validation, address autocomplete, and payment processing — demonstrating production-grade e-commerce patterns."},
            {"label": "Cart State Persistence", "detail": "localStorage-backed cart with optimistic updates, surviving page refreshes and browser sessions."},
            {"label": "Responsive Product Galleries", "detail": "Progressive image loading with srcset/sizes attributes, delivering optimal image resolution across all viewports."},
        ],
        "live_url": None,
        "sidebar": [
            {"label": "Project", "value": "Audiophile E-Commerce"},
            {"label": "Industry", "value": "Retail / E-Commerce"},
            {"label": "Type", "value": "Internal Engineering"},
            {"label": "Stack", "value": "React / Redux"},
            {"label": "Status", "value": "Showcase"},
        ],
        "prev": {"slug": "case-study-crappo", "title": "Crappo Crypto Platform"},
        "next": {"slug": "case-study-greenremedies", "title": "Green Remedies"},
    },
    {
        "slug": "case-study-greenremedies",
        "title": "Green Remedies",
        "meta_desc": "Open-source team project: Fully authenticated e-commerce application for herbal products with Kinde Auth, secure checkout, and real-time inventory management.",
        "keywords": "green remedies, herbal e-commerce, open source, Kinde Auth, team project",
        "subtitle": "Open-source team project — a fully authenticated e-commerce application for herbal products with Kinde Auth, secure checkout, and real-time inventory.",
        "hero_img": "/images/projects/project7-720x520.jpg",
        "tech": ["Next.js", "Kinde Auth", "Prisma", "PostgreSQL", "Open Source"],
        "challenge": "This collaborative open-source project addressed the challenge of building a secure, fully authenticated e-commerce platform from the ground up — with particular emphasis on OAuth-based authentication, role-based access control, and real-time inventory synchronisation.",
        "approach": "Built with Next.js and Prisma ORM, the application uses Kinde Auth for passwordless authentication and social login. A PostgreSQL database with Prisma migrations manages product catalogue, inventory, and order state. Role-based middleware controls access to admin dashboards, order management, and inventory tools. Real-time inventory updates prevent overselling through optimistic locking patterns.",
        "outcomes": [
            {"label": "Secure Authentication", "detail": "Passwordless and social login via Kinde Auth, with role-based access control for admin and customer user types."},
            {"label": "Real-Time Inventory", "detail": "Optimistic locking prevents overselling, with inventory counts updating in real time across concurrent sessions."},
            {"label": "Open-Source Collaboration", "detail": "Published as an open-source project with documented API contracts, enabling community contributions and code review."},
        ],
        "live_url": None,
        "sidebar": [
            {"label": "Project", "value": "Green Remedies"},
            {"label": "Industry", "value": "E-Commerce / Health"},
            {"label": "Type", "value": "Open Source"},
            {"label": "Stack", "value": "Next.js / Prisma"},
            {"label": "Status", "value": "Published"},
        ],
        "prev": {"slug": "case-study-audiophile", "title": "Audiophile E-Commerce"},
        "next": {"slug": "case-study-transitflow", "title": "Transit Flow Logistics"},
    },
    {
        "slug": "case-study-transitflow",
        "title": "Transit Flow Logistics",
        "meta_desc": "Engineering showcase: High-performance, fully responsive business landing page for a modern logistics provider, designed in Figma and built as production-quality React components.",
        "keywords": "logistics landing page, Figma to React, responsive design, performance optimization, engineering showcase",
        "subtitle": "High-performance, fully responsive business landing page for a modern logistics provider. Designed in Figma, converted to production-quality React components.",
        "hero_img": "/images/projects/project3-720x520.jpg",
        "tech": ["React", "Figma", "CSS Modules", "Performance Optimization"],
        "challenge": "This internal project explored the full Figma-to-production pipeline — converting a designer's pixel-perfect Figma mockups into production-grade React components with zero visual regression, sub-2-second load times, and full responsive coverage from 320px to 2560px viewports.",
        "approach": "Starting from a detailed Figma design file, every component was built as an isolated React module with CSS Modules for scoped styling. The build pipeline includes automated Lighthouse CI checks to enforce performance budgets. Image assets were optimised through responsive srcset definitions with AVIF/WebP fallbacks. Layout was implemented using CSS Grid with carefully calibrated breakpoints matching the Figma artboard sizes.",
        "outcomes": [
            {"label": "Pixel-Perfect Figma Parity", "detail": "Zero visual regression between Figma designs and deployed components across all responsive breakpoints."},
            {"label": "Sub-2-Second Load Time", "detail": "Automated Lighthouse CI enforcement maintaining 95+ performance scores across mobile and desktop audits."},
            {"label": "Full Responsive Coverage", "detail": "Seamless layout adaptation from 320px mobile to 2560px ultrawide viewports with no horizontal scrolling or layout breaks."},
        ],
        "live_url": None,
        "sidebar": [
            {"label": "Project", "value": "Transit Flow Logistics"},
            {"label": "Industry", "value": "Logistics / Transport"},
            {"label": "Type", "value": "Internal Engineering"},
            {"label": "Stack", "value": "React / CSS Modules"},
            {"label": "Status", "value": "Showcase"},
        ],
        "prev": {"slug": "case-study-greenremedies", "title": "Green Remedies"},
        "next": None,
    },
]


def generate_page(data):
    head = HEAD_TEMPLATE.format(
        title=data["title"],
        meta_desc=data["meta_desc"],
        keywords=data["keywords"],
        slug=data["slug"],
    )
    body = build_case_study_body(data)
    html = head + HEADER + body + FOOTER
    path = os.path.join(BASE, f"{data['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] {data['slug']}.html")


if __name__ == "__main__":
    print("Phase 5: Generating case study pages...")
    for cs in CASE_STUDIES:
        generate_page(cs)
    print(f"\nDone — {len(CASE_STUDIES)} case study pages rebuilt.")
