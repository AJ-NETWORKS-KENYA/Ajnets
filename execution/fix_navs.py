import os
import glob
import re

directory = r"c:\My Web Sites\ajnets"
html_files = glob.glob(os.path.join(directory, "*.html"))

desktop_nav_replacement = """<nav id="site-navigation" class="main-navigation">
                      <ul class="menu">
                                        <li><a href="./">Home</a></li>
                                        <li><a href="about-us.html">Who We Are</a></li>
                                        <li class="menu-item-has-children"><a href="services.html">Services</a>
                                            <ul class="sub-menu">
                                                <li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                                                <li><a href="software-engineering.html">Software Engineering</a></li>
                                                <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                                                <li><a href="networking.html">Networking & Infrastructure</a></li>
                                                <li><a href="performance-seo.html">Performance & SEO</a></li>
                                            </ul>
                                        </li>
                                        <li><a href="client-success.html">Client Success</a></li>
                                        <li><a href="insights.html">Insights</a></li>
                                        <li><a href="book-consultation.html">Book Consultation</a></li>
                                    </ul>
                    </nav>"""

mobile_nav_replacement = """<ul id="menu-main-menu" class="mobile_mainmenu">
                                        <li><a href="./">Home</a></li>
                                        <li><a href="about-us.html">Who We Are</a></li>
                                        <li class="menu-item-has-children"><a href="services.html">Services</a>
                                            <ul class="sub-menu">
                                                <li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                                                <li><a href="software-engineering.html">Software Engineering</a></li>
                                                <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                                                <li><a href="networking.html">Networking & Infrastructure</a></li>
                                                <li><a href="performance-seo.html">Performance & SEO</a></li>
                                            </ul>
                                        </li>
                                        <li><a href="client-success.html">Client Success</a></li>
                                        <li><a href="insights.html">Insights</a></li>
                                        <li><a href="book-consultation.html">Book Consultation</a></li>
                                    </ul>"""

PATTERN_DESKTOP = re.compile(r'<nav id="site-navigation" class="main-navigation">.*?</nav>', re.DOTALL)
PATTERN_MOBILE = re.compile(r'<ul id="menu-main-menu" class="mobile_mainmenu">.*?</ul>', re.DOTALL)

for file_path in html_files:
    if file_path.endswith("index.html"):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop Nav
    content = re.sub(PATTERN_DESKTOP, desktop_nav_replacement, content)

    # Mobile Nav
    content = re.sub(PATTERN_MOBILE, mobile_nav_replacement, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated navigation headers globally across {len(html_files)} files.")
