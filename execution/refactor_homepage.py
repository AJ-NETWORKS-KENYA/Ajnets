import re

def refactor_homepage():
    file_path = "c:\\My Web Sites\\ajnets\\index.html"
    print(f"Refactoring homepage: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Counter/Stats section (from <section class="pt-0 pb-290"> to the next <section>)
    counter_pattern = r'<section class="pt-0 pb-290">.*?</section>\s*<section class="bg-light-1 no-padding">'
    new_counter_block = """<section class="pt-0 pb-290">
          <div class="container">
            <div class="row mt--130">
              <div class="col-md-6 col-sm-12 mb-4 mb-md-0">
                <div class="misc-box text-white misc-box-bg1">
                  <div class="ot-counter">
                    <div>
                      <span class="num" data-to="20" data-time="2000">0</span>
                      <span>+</span>
                    </div>
                  </div>
                  <h5>Systems Delivered</h5>
                  <p>
                    Deploying production-ready, secure software platforms and network architectures that support core business workflows.
                  </p>
                </div>
              </div>
              <div class="col-md-6 col-sm-12">
                <div class="misc-box misc-box-bg2">
                  <div class="ot-counter">
                    <div>
                      <span class="num" data-to="100" data-time="2000">0</span>
                      <span>%</span>
                    </div>
                  </div>
                  <h5>Delivery Track Record</h5>
                  <p>
                    Engineering solutions on-time and with rigorous technical audits, ensuring smooth handover and system continuity.
                  </p>
                </div>
              </div>
            </div>
            <div class="space-120"></div>
          </div>
        </section>
        <section class="bg-light-1 no-padding">"""
    
    content = re.sub(counter_pattern, new_counter_block, content, flags=re.DOTALL)

    # 2. Update Consulting Practices / Services section (inside the class="over-hidden" after space-120, wait, it's inside <section class="pt-0 pb-290">... wait, look at line 884-886, wait, the service boxes start after <div class="space-120"></div> inside the same section?)
    # Let's check where the service boxes are. They are in a section starting after <div class="space-120"></div>?
    # Actually, in the HTML, the counter boxes and service boxes are in the same section or adjacent?
    # Let's inspect the files. Yes, in the standard index.html:
    # Line 887: <section class="bg-light-1 no-padding"> has class="cta" (Let's build your website)
    # The service boxes are after line 802:
    # Line 944 of index.html: `<div class="row">` followed by `<div class="col-lg-4 col-md-6 col-sm-12">`
    # Let's replace the entire services row block (lines 944 to 1030 in original, or line 944 to 1030 in current file).
    # Let's write a replacement for the services grid starting from `<div class="row">` after `<div class="space-55"></div>`.
    
    services_pattern = r'<div class="space-55"></div>\s*<div class="row">.*?</div>\s*</div>\s*</section>\s*<section class="bg-light-1 no-padding">'
    new_services_grid = """<div class="space-55"></div>
            <div class="row">
              <div class="col-lg-4 col-md-6 col-sm-12">
                <div class="icon-box-s2 s1 pb-60">
                  <div class="icon-main">
                    <span class="flaticon-report-1"></span>
                  </div>
                  <div class="content-box">
                    <h5>1. Technology &amp; Strategy</h5>
                    <p>
                      Strategic advisory, digital transformation roadmaps, systems audits, and feasibility reviews to align investments with objectives.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-sm-12">
                <div class="icon-box-s2 s1 pb-60">
                  <div class="icon-main">
                    <span class="flaticon-code"></span>
                  </div>
                  <div class="content-box">
                    <h5>2. Software Engineering</h5>
                    <p>
                      Engineering custom web architectures, cloud platforms, database systems, and mobile applications built for high performance.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-sm-12">
                <div class="icon-box-s2 s1 pb-60">
                  <div class="icon-main">
                    <span class="flaticon-shield"></span>
                  </div>
                  <div class="content-box">
                    <h5>3. Cybersecurity &amp; Assurance</h5>
                    <p>
                      Integrating threat assessments, system hardening, access reviews, and compliance planning into every stage of development.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-sm-12">
                <div class="icon-box-s2 s1 sm-pb-60">
                  <div class="icon-main">
                    <span class="flaticon-computer"></span>
                  </div>
                  <div class="content-box">
                    <h5>4. Networking &amp; Infrastructure</h5>
                    <p>
                      Designing and optimizing secure enterprise network topologies, cloud connectivity, and communication infrastructures.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-sm-12">
                <div class="icon-box-s2 s1 xs-pb-60">
                  <div class="icon-main">
                    <span class="flaticon-monitor"></span>
                  </div>
                  <div class="content-box">
                    <h5>5. Performance &amp; Technical SEO</h5>
                    <p>
                      Hardening frontend loading speeds, eliminating layout shifts, and aligning technical search metadata to maximize visibility.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 col-sm-12">
                <div class="icon-box-s2 s1">
                  <div class="icon-main">
                    <span class="flaticon-gear"></span>
                  </div>
                  <div class="content-box">
                    <h5>6. Operations &amp; Support</h5>
                    <p>
                      Consulting-governed post-handover support, server oversight, and proactive maintenance retainers to protect software investments.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="bg-light-1 no-padding">"""

    content = re.sub(services_pattern, new_services_grid, content, flags=re.DOTALL)

    # 3. Update CTA bar "Let's Build Your Website!" to outcome-driven CTA
    cta_pattern = r'<div class="cta">.*?<a\s+href="/company/book-consultation"\s+class="octf-btn btn-border".*?>contact us</a>.*?</div>'
    new_cta_block = """<div class="cta">
                  <div class="row">
                    <div class="col-md-9 text-md-left text-center mb-4 mb-md-0">
                      <div class="ot-heading">
                        <span>// OUTCOME-DRIVEN ENGAGEMENTS</span>
                        <h2 class="main-heading">Let's align technology with your business outcomes.</h2>
                      </div>
                    </div>
                    <div class="col-md-3 text-md-right text-center align-self-end">
                      <a href="/company/book-consultation" class="octf-btn octf-btn-primary btn-border" role="button">Book Advisory Call</a>
                    </div>
                  </div>
                </div>"""
    content = re.sub(cta_pattern, new_cta_block, content, flags=re.DOTALL)

    # 4. Case Studies intro block: update headline and text
    case_intro_pattern = r'<span>// latest case studies</span>\s*<h2 class="main-heading">Introduce Our Projects</h2>.*?<p class="mb-0">.*?</p>'
    new_case_intro = """<span>// latest case studies</span>
                  <h2 class="main-heading">Featured Engagements</h2>
                </div>
              </div>
              <div class="col-md-7">
                <p class="mb-0">
                  Every engagement is designed to solve a specific business problem and deliver a measurable impact. We partner closely with our clients to engineer robust, maintainable systems built on trust.
                </p>"""
    content = re.sub(case_intro_pattern, new_case_intro, content, flags=re.DOTALL)

    # 5. Case studies items (carousel slider)
    # Let's replace the carousel slider block starting with `<div class="owl-carousel owl-theme project-slider">` to `</section>`
    slider_pattern = r'<div class="owl-carousel owl-theme project-slider">.*?</div>\s*</section>\s*<section class="technology-v1">'
    new_slider = """<div class="owl-carousel owl-theme project-slider">
            <div class="project-item projects-style-2">
              <div class="projects-box">
                <div class="projects-thumbnail">
                  <a href="/portfolio/case-study-bada">
                    <img src="/images/projects/project7-720x520.jpg" alt="Bada Language Institute Platform" width="720" height="520" />
                    <span class="overlay"></span>
                  </a>
                </div>
                <div class="portfolio-info">
                  <div class="portfolio-info-inner">
                    <a title="Right Arrow 1" class="btn-link" href="/portfolio/case-study-bada"><i class="flaticon-right-arrow-1"></i></a>
                    <h5>
                      <a href="/portfolio/case-study-bada">Bada Language Institute</a>
                    </h5>
                    <p class="portfolio-cates">
                      <a href="/services/software-engineering">Software Engineering</a><span>/</span>
                      <a href="/services/technology-strategy">LMS</a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="project-item projects-style-2">
              <div class="projects-box">
                <div class="projects-thumbnail">
                  <a href="/portfolio/case-study-racnyali">
                    <img src="/images/projects/project-720x520.jpg" alt="Rotaract Club of Nyali Portal" width="720" height="520" />
                    <span class="overlay"></span>
                  </a>
                </div>
                <div class="portfolio-info">
                  <div class="portfolio-info-inner">
                    <a title="Right Arrow 1" class="btn-link" href="/portfolio/case-study-racnyali"><i class="flaticon-right-arrow-1"></i></a>
                    <h5>
                      <a href="/portfolio/case-study-racnyali">Rotaract Club Nyali Portal</a>
                    </h5>
                    <p class="portfolio-cates">
                      <a href="/services/software-engineering">Software Engineering</a><span>/</span>
                      <a href="/services/technology-strategy">NGO System</a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="project-item projects-style-2">
              <div class="projects-box">
                <div class="projects-thumbnail">
                  <a href="/portfolio/case-study-sgss">
                    <img src="/images/projects/project3-720x520.jpg" alt="SGSS Mombasa Medical Fund Portal" width="720" height="520" />
                    <span class="overlay"></span>
                  </a>
                </div>
                <div class="portfolio-info">
                  <div class="portfolio-info-inner">
                    <a title="Right Arrow 1" class="btn-link" href="/portfolio/case-study-sgss"><i class="flaticon-right-arrow-1"></i></a>
                    <h5>
                      <a href="/portfolio/case-study-sgss">SGSS Mombasa Medical Fund</a>
                    </h5>
                    <p class="portfolio-cates">
                      <a href="/services/software-engineering">Software Engineering</a><span>/</span>
                      <a href="/services/cybersecurity">Cybersecurity</a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div class="project-item projects-style-2">
              <div class="projects-box">
                <div class="projects-thumbnail">
                  <a href="/portfolio/case-study-transitflow">
                    <img src="/images/projects/project4-720x520.jpg" alt="Transit Flow Logistics System" width="720" height="520" />
                    <span class="overlay"></span>
                  </a>
                </div>
                <div class="portfolio-info">
                  <div class="portfolio-info-inner">
                    <a title="Right Arrow 1" class="btn-link" href="/portfolio/case-study-transitflow"><i class="flaticon-right-arrow-1"></i></a>
                    <h5>
                      <a href="/portfolio/case-study-transitflow">Transit Flow Logistics</a>
                    </h5>
                    <p class="portfolio-cates">
                      <a href="/services/software-engineering">Software Engineering</a><span>/</span>
                      <a href="/services/technology-strategy">Logistics</a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="technology-v1">"""
    
    content = re.sub(slider_pattern, new_slider, content, flags=re.DOTALL)

    # 6. Technology Index heading and typos (Wearalables -> Wearables)
    tech_heading_pattern = r'<span>// TECHNOLOGY INDEX</span>\s*<h2 class="main-heading">.*?</h2>'
    new_tech_heading = """<span>// TECHNOLOGY INDEX</span>
                  <h2 class="main-heading">
                    Technical Ecosystems We Engineer
                  </h2>"""
    content = re.sub(tech_heading_pattern, new_tech_heading, content, flags=re.DOTALL)
    
    # 7. Testimonials section: change heading and testimonials contents
    testi_section_pattern = r'<section class="bg-map-dots">.*?</section>\s*</div>\s*<footer'
    new_testi_section = """<section class="bg-map-dots">
          <div class="container">
            <div class="row">
              <div class="col-md-12">
                <div class="ot-heading text-center">
                  <span>// our clients</span>
                  <h2 class="main-heading">
                    Client Perspectives
                  </h2>
                </div>
              </div>
            </div>
            <div class="space-35"></div>
            <div class="row">
              <div class="col-md-12">
                <div class="ot-testimonials">
                  <div class="owl-carousel owl-theme testimonial-inner ot-testimonials-slider">
                    <div class="testi-item">
                      <div class="layer1"></div>
                      <div class="layer2">
                        <div class="t-head flex-middle">
                          <img src="/images/testi2.png" alt="Bada Language Institute Client" class="lazyloaded" />
                          <div class="tinfo">
                            <h6>Bada Language Institute</h6>
                            <span>Education Provider</span>
                          </div>
                        </div>
                        <div class="ttext">
                          "AJNETWORKS delivered a complete student LMS and event manager. It streamlined our enrolment process and course scheduling, allowing us to grow our regional student reach. They are detailed, security-first, and highly professional."
                        </div>
                      </div>
                    </div>
                    <div class="testi-item">
                      <div class="layer1"></div>
                      <div class="layer2">
                        <div class="t-head flex-middle">
                          <img src="/images/testi1.png" alt="Rotaract Nyali Client" class="lazyloaded" />
                          <div class="tinfo">
                            <h6>Rotaract Club Nyali</h6>
                            <span>Community Organization</span>
                          </div>
                        </div>
                        <div class="ttext">
                          "The portal they built for our Rotaract community simplified membership tracking and event sign-ups. Their team worked with extreme clarity, milestones, and original ideas."
                        </div>
                      </div>
                    </div>
                    <div class="testi-item">
                      <div class="layer1"></div>
                      <div class="layer2">
                        <div class="t-head flex-middle">
                          <img src="/images/testi2.png" alt="SGSS Mombasa Client" class="lazyloaded" />
                          <div class="tinfo">
                            <h6>SGSS Mombasa</h6>
                            <span>Healthcare / Community</span>
                          </div>
                        </div>
                        <div class="ttext">
                          "AJNETWORKS modernized our medical fund platform. Their security assurance and software engineering capabilities ensured patient and donor records were fully secured. A truly reliable technology partner."
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
      <footer"""

    content = re.sub(testi_section_pattern, new_testi_section, content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Homepage refactoring complete.")

if __name__ == "__main__":
    refactor_homepage()
