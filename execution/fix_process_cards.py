import os
from bs4 import BeautifulSoup

filepath = r"c:\My Web Sites\ajnets\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the "Our Engagement Model" section
engagement_section = None
for sec in soup.find_all("section"):
    heading = sec.find("h2", string="How We Deliver Value")
    if heading:
        engagement_section = sec
        break

if engagement_section:
    new_html = """
    <section class="section-padd bg-dark-primary">
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
            <div class="row">
                <!-- Step 1 -->
                <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="serv-box-2 s2">
                        <span class="big-number">01</span>
                        <div class="icon-main"><span class="flaticon-search"></span></div>
                        <div class="content-box">
                            <h5>Discover</h5>
                            <div>Analyze business goals and technical gaps.</div>
                        </div>
                    </div>
                </div>
                <!-- Step 2 -->
                <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="serv-box-2 s2">
                        <span class="big-number">02</span>
                        <div class="icon-main"><span class="flaticon-settings"></span></div>
                        <div class="content-box">
                            <h5>Architect</h5>
                            <div>Design secure, scalable systems.</div>
                        </div>
                    </div>
                </div>
                <!-- Step 3 -->
                <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="serv-box-2 s2">
                        <span class="big-number">03</span>
                        <div class="icon-main"><span class="flaticon-code"></span></div>
                        <div class="content-box">
                            <h5>Build</h5>
                            <div>Execute with engineering excellence.</div>
                        </div>
                    </div>
                </div>
                <!-- Step 4 -->
                <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="serv-box-2 s2">
                        <span class="big-number">04</span>
                        <div class="icon-main"><span class="flaticon-shield"></span></div>
                        <div class="content-box">
                            <h5>Secure</h5>
                            <div>Implement security by design.</div>
                        </div>
                    </div>
                </div>
                <!-- Step 5 -->
                <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="serv-box-2 s2">
                        <span class="big-number">05</span>
                        <div class="icon-main"><span class="flaticon-startup"></span></div>
                        <div class="content-box">
                            <h5>Deploy</h5>
                            <div>Launch with zero downtime strategies.</div>
                        </div>
                    </div>
                </div>
                <!-- Step 6 -->
                <div class="col-xl-4 col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="serv-box-2 s2">
                        <span class="big-number">06</span>
                        <div class="icon-main"><span class="flaticon-support"></span></div>
                        <div class="content-box">
                            <h5>Support</h5>
                            <div>Monitor, optimize, and scale continuously.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    engagement_section.replace_with(BeautifulSoup(new_html, "html.parser"))
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Updated index.html to use serv-box-2 for Engagement Model")
else:
    print("Could not find Engagement Model section")
