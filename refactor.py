import os
import glob
import re

directory = r"c:\My Web Sites\ajnets"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove Royal Preloader
    content = content.replace('class="royal_preloader"', '')
    content = content.replace('<link rel="stylesheet" href="css/royal-preload.css" />\n', '')
    content = content.replace('<link rel="stylesheet" href="css/royal-preload.css">\n', '')
    content = content.replace('<script src="js/royal_preloader.min.js"></script>\n', '')
    
    # Remove the Royal Preloader init script
    preloader_script_pattern = re.compile(r'<script>\s*window\.jQuery = window\.\$ = jQuery;\s*\(function\(\$\)\s*\{\s*"use strict";\s*//Preloader[\s\S]*?\}\)\(jQuery\);\s*</script>', re.IGNORECASE)
    content = re.sub(preloader_script_pattern, '<script>\n        window.jQuery = window.$ = jQuery;\n    </script>', content)

    # 2. Update CTAs
    content = content.replace('>Hire Us<', '>Book Advisory Session<')
    content = content.replace('>Free Quote<', '>Request Consultation<')

    # 3. Update Link references for renamed pages
    content = content.replace('href="portfolio-grid.html"', 'href="client-success.html"')
    content = content.replace('href="blog.html"', 'href="insights.html"')
    content = content.replace('href="contact.html"', 'href="book-consultation.html"')

    # 4. Flatten Desktop Navigation
    old_nav = """<ul class="menu">
                                        <li><a href="./">Home</a></li>
                                        <li class="menu-item-has-children"><a href="about-us.html">Company</a>
                                            <ul class="sub-menu">
                                                <li><a href="about-us.html">About Us</a></li>
                                            </ul>
                                        </li>
                                        <li class="menu-item-has-children"><a href="services.html">Services</a>
                                            <ul class="sub-menu">
                                                <li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                                                <li><a href="software-engineering.html">Software Engineering</a></li>
                                                <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                                                <li><a href="networking.html">Networking & Infrastructure</a></li>
                                                <li><a href="performance-seo.html">Performance & SEO</a></li>
                                            </ul>
                                        </li>
                                        <li><a href="solutions.html">Solutions</a></li>
                                        <li><a href="client-success.html">Portfolio</a></li>
                                        <li><a href="insights.html">Blog</a></li>
                                        <li><a href="book-consultation.html">Contact</a></li>
                                    </ul>"""
    
    new_nav = """<ul class="menu">
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

    # We might need to use regex for the nav since whitespace varies slightly or it might already have updated links inside.
    # Let's write a generic mobile and desktop nav replacer
    
    desktop_nav_pattern = re.compile(r'<ul class="menu">[\s\S]*?<li><a href="book-consultation\.html">Contact</a></li>\s*</ul>', re.IGNORECASE)
    content = re.sub(desktop_nav_pattern, new_nav, content)

    mobile_nav_pattern = re.compile(r'<ul id="menu-main-menu" class="mobile_mainmenu">[\s\S]*?<li><a href="book-consultation\.html">Contact</a></li>\s*</ul>', re.IGNORECASE)
    new_m_nav = new_nav.replace('<ul class="menu">', '<ul id="menu-main-menu" class="mobile_mainmenu">')
    content = re.sub(mobile_nav_pattern, new_m_nav, content)

    footer_nav_pattern = re.compile(r'<div class="footer-menu">\s*<ul>[\s\S]*?</ul>\s*</div>', re.IGNORECASE)
    new_f_nav = """<div class="footer-menu">
                        <ul>
                            <li><a href="./">Home</a></li>
                            <li><a href="about-us.html">Who We Are</a></li>
                            <li><a href="services.html">Services</a></li>
                            <li><a href="client-success.html">Client Success</a></li>
                            <li><a href="insights.html">Insights</a></li>
                            <li><a href="book-consultation.html">Book Consultation</a></li>
                        </ul>
                    </div>"""
    content = re.sub(footer_nav_pattern, new_f_nav, content)
    
    # Also fix any missed "Portfolio" or "Blog" text in the menu
    content = content.replace('<li><a href="client-success.html">Portfolio</a></li>', '<li><a href="client-success.html">Client Success</a></li>')
    content = content.replace('<li><a href="insights.html">Blog</a></li>', '<li><a href="insights.html">Insights</a></li>')
    content = content.replace('<li><a href="book-consultation.html">Contact</a></li>', '<li><a href="book-consultation.html">Book Consultation</a></li>')
    content = content.replace('<li><a href="book-consultation.html">Contacts</a></li>', '<li><a href="book-consultation.html">Book Consultation</a></li>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
print("Phase 1 replacements applied.")
