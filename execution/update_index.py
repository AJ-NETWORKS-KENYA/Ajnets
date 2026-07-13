import os
from bs4 import BeautifulSoup

filepath = r"c:\My Web Sites\ajnets\index.html"

try:
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
except Exception as e:
    print(f"Error opening file: {e}")
    exit(1)

# 1. Update Hero H1 and P
hero_h1 = soup.find("h1")
if hero_h1:
    # Preserve the style attribute
    style = hero_h1.get("style", "")
    hero_h1.clear()
    hero_h1.append(BeautifulSoup("Engineering technology<br/>that accelerates business growth", "html.parser"))

hero_p = soup.select_main = soup.select("div.static-hero p")
if hero_p:
    hero_p[0].clear()
    hero_p[0].append("AJNETWORKS helps businesses modernize, secure and scale their operations through thoughtful engineering and strategic technology consulting.")

# 2. Add Technologies Bar after partners section, or replace partners with it.
# Wait, let's just insert it after the partners section.
partners_section = soup.find("div", class_="padding-half bg-light-1")

tech_bar_html = """
<div class="padding-half bg-light-1" style="border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; background-color: #f8f9fa;">
    <div class="container">
        <div class="row">
            <div class="col-md-12 text-center mb-3">
                <span style="font-size: 14px; font-weight: 600; color: #64748b; text-transform: uppercase; letter-spacing: 1px;">Trusted Technologies &amp; Platforms</span>
            </div>
            <div class="col-md-12">
                <div class="d-flex flex-wrap justify-content-center align-items-center" style="gap: 30px; opacity: 0.6; font-family: 'Montserrat', sans-serif; font-weight: 700; font-size: 18px; color: #1e293b;">
                    <span>Cloudflare</span>
                    <span>Zoho</span>
                    <span>GitHub</span>
                    <span>Docker</span>
                    <span>Linux</span>
                    <span>Microsoft 365</span>
                    <span>Next.js</span>
                    <span>Node.js</span>
                    <span>PostgreSQL</span>
                </div>
            </div>
        </div>
    </div>
</div>
"""

process_section_html = """
<section class="section-padd" style="background-color: #1A1A2E; color: #fff;">
    <div class="container">
        <div class="row text-center mb-5">
            <div class="col-md-12">
                <div class="ot-heading">
                    <span style="color: #43D9AD;">// Our Engagement Model</span>
                    <h2 class="main-heading text-white">How We Deliver Value</h2>
                </div>
                <p style="color: #E0E0E0; max-width: 600px; margin: 0 auto;">We follow a rigorous, consulting-led engineering process to ensure technology decisions directly map to business outcomes.</p>
            </div>
        </div>
        <div class="row text-center">
            <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4">
                <div style="background: rgba(255,255,255,0.05); padding: 30px 15px; border-radius: 8px; border-bottom: 3px solid #43D9AD; height: 100%;">
                    <h4 class="text-white mb-2" style="font-size: 20px;">1. Discover</h4>
                    <p style="font-size: 14px; color: #E0E0E0; margin-bottom: 0;">Analyze business goals and technical gaps.</p>
                </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4">
                <div style="background: rgba(255,255,255,0.05); padding: 30px 15px; border-radius: 8px; border-bottom: 3px solid #43D9AD; height: 100%;">
                    <h4 class="text-white mb-2" style="font-size: 20px;">2. Architect</h4>
                    <p style="font-size: 14px; color: #E0E0E0; margin-bottom: 0;">Design secure, scalable systems.</p>
                </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4">
                <div style="background: rgba(255,255,255,0.05); padding: 30px 15px; border-radius: 8px; border-bottom: 3px solid #43D9AD; height: 100%;">
                    <h4 class="text-white mb-2" style="font-size: 20px;">3. Build</h4>
                    <p style="font-size: 14px; color: #E0E0E0; margin-bottom: 0;">Execute with engineering excellence.</p>
                </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4">
                <div style="background: rgba(255,255,255,0.05); padding: 30px 15px; border-radius: 8px; border-bottom: 3px solid #43D9AD; height: 100%;">
                    <h4 class="text-white mb-2" style="font-size: 20px;">4. Secure</h4>
                    <p style="font-size: 14px; color: #E0E0E0; margin-bottom: 0;">Implement security by design.</p>
                </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4">
                <div style="background: rgba(255,255,255,0.05); padding: 30px 15px; border-radius: 8px; border-bottom: 3px solid #43D9AD; height: 100%;">
                    <h4 class="text-white mb-2" style="font-size: 20px;">5. Deploy</h4>
                    <p style="font-size: 14px; color: #E0E0E0; margin-bottom: 0;">Launch with zero downtime strategies.</p>
                </div>
            </div>
            <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4">
                <div style="background: rgba(255,255,255,0.05); padding: 30px 15px; border-radius: 8px; border-bottom: 3px solid #43D9AD; height: 100%;">
                    <h4 class="text-white mb-2" style="font-size: 20px;">6. Support</h4>
                    <p style="font-size: 14px; color: #E0E0E0; margin-bottom: 0;">Monitor, optimize, and scale continuously.</p>
                </div>
            </div>
        </div>
    </div>
</section>
"""

if partners_section:
    new_tech = BeautifulSoup(tech_bar_html, "html.parser")
    partners_section.insert_after(new_tech)
    
    new_process = BeautifulSoup(process_section_html, "html.parser")
    # find where to insert process section - maybe before the "Industries" section or after the "about company" section
    about_section = soup.find("section", class_="over-hidden")
    if about_section:
        about_section.insert_after(new_process)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Updated index.html")
