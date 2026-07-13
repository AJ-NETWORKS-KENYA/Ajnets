import os
import re

HEADER_MARKUP = """      <!-- Skip to main content link for accessibility -->
      <a href="#content" class="skip-link">Skip to main content</a>

      <header
        id="site-header"
        class="site-header header-style-2 header-fullwidth sticky-header header-static"
      >
        <!-- Main Header start -->
        <div class="header-topbar">
          <div class="octf-area-wrap">
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-6">
                  <ul class="topbar-info">
                    <li>
                      <i class="fas fa-envelope"></i><a href="mailto:hello@ajnetworkskenya.it.com">hello&#64;ajnetworkskenya.it.com</a>
                    </li>
                    <li>
                      <i class="fas fa-clock"></i> Mon - Sat: 8.00 am - 7.00 pm
                    </li>
                  </ul>
                </div>
                <div class="col-md-6 text-right">
                  <div class="topbar-right">
                    <ul class="extra-text">
                      <li>
                        We are creative, ambitious and ready for challenges!
                        <a href="/company/book-consultation">Book Advisory Session</a>
                      </li>
                    </ul>
                    <ul class="social-list">
                      <li>
                        <a href="https://twitter.com/ajnetworks" target="_blank" rel="noopener" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                      </li>
                      <li>
                        <a href="https://facebook.com/ajnetworks" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/company/ajnetworks" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                      </li>
                      <li>
                        <a href="https://instagram.com/ajnetworks" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                      </li>
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
                      <a href="/">
                        <img src="/images/logo.svg" alt="AJNETWORKS" />
                      </a>
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
                            <li>
                              <a href="/services/technology-strategy">Technology &amp; Digital Strategy</a>
                            </li>
                            <li>
                              <a href="/services/software-engineering">Software Engineering</a>
                            </li>
                            <li>
                              <a href="/services/cybersecurity">Cybersecurity &amp; Assurance</a>
                            </li>
                            <li>
                              <a href="/services/networking">Networking &amp; IT Infrastructure</a>
                            </li>
                            <li>
                              <a href="/services/performance-seo">Performance &amp; SEO</a>
                            </li>
                          </ul>
                        </li>
                        <li>
                          <a href="/portfolio/client-success">Client Success</a>
                        </li>
                        <li><a href="/insights/insights">Insights</a></li>
                        <li>
                          <a href="/company/book-consultation">Book Consultation</a>
                        </li>
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
                <a href="/">
                  <img src="/images/logo.svg" alt="AJNETWORKS" />
                </a>
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
                      <li>
                        <a href="/services/technology-strategy">Technology &amp; Digital Strategy</a>
                      </li>
                      <li>
                        <a href="/services/software-engineering">Software Engineering</a>
                      </li>
                      <li>
                        <a href="/services/cybersecurity">Cybersecurity &amp; Assurance</a>
                      </li>
                      <li>
                        <a href="/services/networking">Networking &amp; IT Infrastructure</a>
                      </li>
                      <li>
                        <a href="/services/performance-seo">Performance &amp; SEO</a>
                      </li>
                    </ul>
                  </li>
                  <li><a href="/portfolio/client-success">Client Success</a></li>
                  <li><a href="/insights/insights">Insights</a></li>
                  <li>
                    <a href="/company/book-consultation">Book Consultation</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </header>"""

FOOTER_MARKUP = """      <footer id="site-footer" class="site-footer footer-v1">
        <div class="container">
          <div class="row">
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
              <div class="widget-footer">
                <h5 class="text-white">Services</h5>
                <ul class="list-items">
                  <li class="list-item">
                    <a href="/services/technology-strategy">Technology &amp; Strategy</a>
                  </li>
                  <li class="list-item">
                    <a href="/services/software-engineering">Software Engineering</a>
                  </li>
                  <li class="list-item">
                    <a href="/services/cybersecurity">Cybersecurity &amp; Assurance</a>
                  </li>
                  <li class="list-item">
                    <a href="/services/networking">Networking &amp; Infrastructure</a>
                  </li>
                  <li class="list-item">
                    <a href="/services/performance-seo">Performance &amp; SEO</a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
              <div class="widget-footer">
                <h5 class="text-white">Quick Links</h5>
                <ul class="list-items">
                  <li class="list-item">
                    <a href="/company/about-us">Who We Are</a>
                  </li>
                  <li class="list-item">
                    <a href="/portfolio/client-success">Client Success</a>
                  </li>
                  <li class="list-item">
                    <a href="/insights/insights">Insights</a>
                  </li>
                  <li class="list-item">
                    <a href="/company/book-consultation">Book Consultation</a>
                  </li>
                  <li class="list-item">
                    <a href="/company/faq">FAQ</a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
              <div class="widget-footer">
                <h5 class="text-white">Operations</h5>
                <p>
                  AJNETWORKS is a technology consulting firm delivering secure, scalable digital systems across East Africa.
                </p>
                <p>
                  <strong>HQ:</strong> Nairobi, Kenya<br />
                  <strong>Operations:</strong> Kigali, Rwanda
                </p>
              </div>
            </div>
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
              <div class="widget-footer">
                <h5 class="text-white">Get In Touch</h5>
                <div class="footer-contact-info">
                  <p>
                    <i class="fas fa-envelope"></i>
                    <a href="mailto:hello@ajnetworkskenya.it.com">hello&#64;ajnetworkskenya.it.com</a>
                  </p>
                  <p><i class="fas fa-phone-alt"></i> +254 758 238 617</p>
                  <p>
                    <i class="fas fa-clock"></i> Mon - Sat: 8:00 AM - 7:00 PM
                  </p>
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
              <p class="copyright-text">
                Copyright &copy; 2026 AJNETWORKS. All Rights Reserved.
              </p>
            </div>
          </div>
        </div>
      </footer>"""

SCRIPTS_MARKUP = """    <script src="/js/jquery.min.js"></script>
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
          <p>
            We use cookies to enhance your browsing experience, serve
            personalized content, and analyze our traffic. By clicking "Accept",
            you consent to our use of cookies.
          </p>
        </div>
        <div class="cookie-buttons">
          <button id="btn-reject-cookies" class="cookie-btn reject">
            Decline
          </button>
          <button id="btn-accept-cookies" class="cookie-btn accept">
            Accept
          </button>
        </div>
      </div>
    </div>"""

def standardize_head(html_content, file_path):
    head_match = re.search(r'<head>(.*?)</head>', html_content, re.DOTALL)
    if not head_match:
        return html_content

    head_inner = head_match.group(1)
    
    title_match = re.search(r'<title>(.*?)</title>', head_inner, re.IGNORECASE)
    title = title_match.group(1) if title_match else "AJNETWORKS - Technology Consulting & Engineering Delivery"
    
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"\s*/?>', head_inner, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content="(.*?)"\s+name="description"\s*/?>', head_inner, re.IGNORECASE)
    description = desc_match.group(1) if desc_match else "AJNETWORKS is a technology consulting firm delivering strategic advisory, software engineering, cybersecurity, and IT infrastructure solutions."

    keywords_match = re.search(r'<meta\s+name="keywords"\s+content="(.*?)"\s*/?>', head_inner, re.IGNORECASE)
    keywords = keywords_match.group(1) if keywords_match else "technology consulting Kenya, software engineering Nairobi, cybersecurity services, IT infrastructure"

    rel_path = file_path.replace("c:\\\\My Web Sites\\\\ajnets\\\\", "").replace("c:/My Web Sites/ajnets/", "").replace("\\\\", "/").replace("\\", "/")
    if rel_path == "index.html" or rel_path == "./index.html":
        canonical_path = ""
    else:
        canonical_path = rel_path.replace(".html", "")
    
    canonical_url = f"https://ajnetworkskenya.it.com/{canonical_path}"

    new_head = f"""    <meta name="facebook-domain-verification" content="r5liwwbty07nhozk87d1uwkz4fyp70" />
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="{description}" />
    <meta name="keywords" content="{keywords}" />
    <meta name="author" content="AJNETWORKS" />
    <title>{title}</title>
    
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
      function gtag() {{
        dataLayer.push(arguments);
      }}
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
          window.lintrk = function (a, b) {{
            window.lintrk.q.push([a, b]);
          }};
          window.lintrk.q = [];
        }}
        var s = document.getElementsByTagName("script")[0];
        var b = document.createElement("script");
        b.type = "text/javascript";
        b.async = true;
        b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
        s.parentNode.insertBefore(b, s);
      }})(window.lintrk);
    </script>
    <noscript>
      <img height="1" width="1" style="display: none" alt="" src="https://px.ads.linkedin.com/collect/?pid=YOUR_LINKEDIN_PID&amp;fmt=gif" />
    </noscript>

    <!-- Canonical & Open Graph -->
    <link rel="canonical" href="{canonical_url}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:image" content="https://ajnetworkskenya.it.com/images/og-home.jpg" />
    <meta property="og:site_name" content="AJNETWORKS" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />"""
    
    if rel_path.endswith("index.html"):
        new_head += '\n    <link rel="preload" as="image" href="/images/slider/slide1-home1.webp" fetchpriority="high" />'
        
    return html_content.replace(head_inner, new_head)

def process_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Standardize Head
    content = standardize_head(content, file_path)

    # 2. Standardize Header
    content = re.sub(r'<header.*?</header>', HEADER_MARKUP, content, flags=re.DOTALL)
    
    if "case-study" in file_path or "client-success" in file_path:
        content = re.sub(r'<!-- ═══════════════════════════════ NAVBAR ═══════════════════════════════ -->.*?<!-- ═══════════════════════════════ HERO', lambda m: HEADER_MARKUP + '\n  <!-- ═══════════════════════════════ HERO', content, flags=re.DOTALL)
        content = re.sub(r'<!-- Navbar -->.*?<!-- Hero', lambda m: HEADER_MARKUP + '\n  <!-- Hero', content, flags=re.DOTALL)
        content = content.replace('<body class="grid-bg">', '<body>')

    # 3. Standardize Footer
    content = re.sub(r'<footer.*?</footer>', FOOTER_MARKUP, content, flags=re.DOTALL)

    # 4. Standardize Scripts
    footer_match = list(re.finditer(r'</footer>', content))
    if footer_match:
        last_footer_pos = footer_match[-1].end()
        body_end_match = re.search(r'</body>', content)
        if body_end_match:
            body_end_pos = body_end_match.start()
            content = content[:last_footer_pos] + "\n" + SCRIPTS_MARKUP + "\n  " + content[body_end_pos:]

    # 5. Fix Typos & Encodings
    content = content.replace("worlds", "world's")
    content = content.replace("Well", "We'll")
    content = content.replace("Weve", "We've")
    content = content.replace("dont", "don't")
    content = content.replace("clients", "client's")
    content = content.replace("IT Counsultancy", "IT Consultancy")
    content = content.replace("LEANR MORE", "LEARN MORE")
    content = content.replace("..", ".")
    content = content.replace("`n Consulting Partner", "Consulting Partner")
    content = content.replace("Intellectsofts", "AJNETWORKS'")
    content = content.replace("Intellectsoft", "AJNETWORKS")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def walk_and_process():
    html_files = []
    for root, dirs, files in os.walk("c:\\\\My Web Sites\\\\ajnets"):
        if any(p in root for p in ["node_modules", ".git", ".vercel", ".agent", ".tmp"]):
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                
    for file_path in html_files:
        process_file(file_path)

if __name__ == "__main__":
    walk_and_process()
