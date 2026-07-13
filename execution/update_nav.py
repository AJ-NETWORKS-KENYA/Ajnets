import os
from bs4 import BeautifulSoup

ROOT = r"c:\My Web Sites\ajnets"

HEADER_MENU_HTML = """
<ul class="menu">
    <li><a href="/index.html">Home</a></li>
    <li class="menu-item-has-children">
        <a href="/services/services.html">Services</a>
        <ul class="sub-menu">
            <li><a href="/services/technology-strategy.html">Technology &amp; Digital Strategy</a></li>
            <li><a href="/services/software-engineering.html">Software Engineering</a></li>
            <li><a href="/services/cybersecurity.html">Cybersecurity &amp; Assurance</a></li>
            <li><a href="/services/networking.html">Infrastructure &amp; Networking</a></li>
            <li><a href="/services/performance-seo.html">Performance &amp; SEO</a></li>
        </ul>
    </li>
    <li><a href="/portfolio/client-success.html">Client Success</a></li>
    <li><a href="/insights/insights.html">Insights</a></li>
    <li><a href="/company/about-us.html">About</a></li>
    <li><a href="/company/book-consultation.html">Contact</a></li>
    <li><a href="/company/book-consultation.html">Book Consultation</a></li>
</ul>
"""

MOBILE_MENU_HTML = """
<ul id="menu-main-menu" class="mobile_mainmenu">
    <li><a href="/index.html">Home</a></li>
    <li class="menu-item-has-children">
        <a href="/services/services.html">Services</a>
        <ul class="sub-menu">
            <li><a href="/services/technology-strategy.html">Technology &amp; Digital Strategy</a></li>
            <li><a href="/services/software-engineering.html">Software Engineering</a></li>
            <li><a href="/services/cybersecurity.html">Cybersecurity &amp; Assurance</a></li>
            <li><a href="/services/networking.html">Infrastructure &amp; Networking</a></li>
            <li><a href="/services/performance-seo.html">Performance &amp; SEO</a></li>
        </ul>
    </li>
    <li><a href="/portfolio/client-success.html">Client Success</a></li>
    <li><a href="/insights/insights.html">Insights</a></li>
    <li><a href="/company/about-us.html">About</a></li>
    <li><a href="/company/book-consultation.html">Contact</a></li>
    <li><a href="/company/book-consultation.html">Book Consultation</a></li>
</ul>
"""

FOOTER_HTML = """
<footer id="site-footer" class="site-footer bg-gradient">
    <div class="container">
        <div class="row">
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                <div class="widget-footer">
                    <h5 class="text-white">Company</h5>
                    <ul class="list-items">
                        <li class="list-item"><a href="/company/about-us.html">About</a></li>
                        <li class="list-item"><a href="/portfolio/client-success.html">Client Success</a></li>
                        <li class="list-item"><a href="/insights/insights.html">Insights</a></li>
                        <li class="list-item"><a href="/company/about-us.html">Careers</a></li>
                        <li class="list-item"><a href="/company/book-consultation.html">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                <div class="widget-footer">
                    <h5 class="text-white">Services</h5>
                    <ul class="list-items">
                        <li class="list-item"><a href="/services/technology-strategy.html">Technology Strategy</a></li>
                        <li class="list-item"><a href="/services/software-engineering.html">Software Engineering</a></li>
                        <li class="list-item"><a href="/services/cybersecurity.html">Cybersecurity</a></li>
                        <li class="list-item"><a href="/services/networking.html">Infrastructure</a></li>
                        <li class="list-item"><a href="/services/performance-seo.html">Performance</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                <div class="widget-footer">
                    <h5 class="text-white">Resources</h5>
                    <ul class="list-items">
                        <li class="list-item"><a href="/company/faq.html">Privacy Policy</a></li>
                        <li class="list-item"><a href="/company/faq.html">Terms</a></li>
                        <li class="list-item"><a href="/company/faq.html">Responsible Disclosure</a></li>
                        <li class="list-item"><a href="#">Status</a></li>
                        <li class="list-item"><a href="#">Documentation</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-sm-6 col-12">
                <div class="widget-footer">
                    <h5 class="text-white">Get In Touch</h5>
                    <div class="footer-contact-info">
                        <p><i class="fas fa-envelope"></i><a href="mailto:hello@ajnetworks.co">hello@ajnetworks.co</a></p>
                        <p><i class="fas fa-map-marker-alt"></i> HQ: Nairobi, Kenya</p>
                        <p><i class="fas fa-clock"></i> Mon - Sat: 8:00 AM - 7:00 PM</p>
                        <a href="/company/book-consultation.html" class="octf-btn octf-btn-primary mt-3">Book Strategy Call</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-65">
            <div class="col-md-6 mb-4 mb-md-0">
                <img src="/images/logo.svg" alt="AJNETWORKS Logo">
            </div>
            <div class="col-md-6 text-left text-md-right align-self-center">
                <p class="copyright-text">Copyright © 2026 AJNETWORKS. All Rights Reserved.</p>
            </div>
        </div>
    </div>
</footer>
"""

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
    except Exception as e:
        return False

    changed = False

    # 1. Main Navigation
    nav = soup.find("nav", id="site-navigation")
    if nav:
        old_menu = nav.find("ul", class_="menu")
        if old_menu:
            new_menu_soup = BeautifulSoup(HEADER_MENU_HTML, "html.parser").ul
            old_menu.replace_with(new_menu_soup)
            changed = True

    # 2. Mobile Navigation
    mobile_nav = soup.find("div", class_="mobile_nav")
    if mobile_nav:
        old_mobile = mobile_nav.find("ul", class_="mobile_mainmenu")
        if old_mobile:
            new_mobile_soup = BeautifulSoup(MOBILE_MENU_HTML, "html.parser").ul
            old_mobile.replace_with(new_mobile_soup)
            changed = True
            
    # 3. Footer
    old_footer = soup.find("footer", id="site-footer")
    if old_footer:
        new_footer_soup = BeautifulSoup(FOOTER_HTML, "html.parser").footer
        old_footer.replace_with(new_footer_soup)
        changed = True

    if changed:
        # Save file with the same formatting
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        return True

    return False

def main():
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "execution", ".tmp")]
        for fname in filenames:
            if fname.endswith(".html"):
                fpath = os.path.join(dirpath, fname)
                if process_file(fpath):
                    print(f"  [UPDATED] {os.path.relpath(fpath, ROOT)}")
                    fixed += 1

    print(f"\nDone - {fixed} files updated.")

if __name__ == "__main__":
    main()
