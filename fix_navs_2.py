import os
import glob
import re

directory = r"c:\My Web Sites\ajnets"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    if file_path.endswith("index.html"):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The mobile menu wrapper goes all the way to </header>. 
    # Let's replace the whole mmenu_wrapper block
    pattern = re.compile(r'<div class="mmenu_wrapper">.*?</header>', re.DOTALL)
    
    correct_block = """<div class="mmenu_wrapper">
              <div class="mobile_nav collapse">
                <ul id="menu-main-menu" class="mobile_mainmenu">
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
              </div>
            </div>
          </div>
        </div>
      </header>"""

    content = re.sub(pattern, correct_block, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Fixed mobile nav headers globally across files.")
