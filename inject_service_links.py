import os
import re

directory = r"c:\My Web Sites\ajnets"

injections = {
    "software-engineering.html": """
      <!-- Related Case Studies Section -->
      <section style="padding: 80px 0; background-color: #fff;">
        <div class="container">
          <div class="row mb-4">
            <div class="col-12 text-center">
              <div class="ot-heading">
                <span>// proof of output</span>
                <h2 class="main-heading">Featured Engineering Portfolios</h2>
              </div>
            </div>
          </div>
          <div class="row justify-content-center">
            <div class="col-md-6 mb-4">
              <div style="padding: 30px; background: #f8f9fa; border-left: 4px solid #0056b3; border-radius: 4px; height: 100%;">
                <h4 class="mb-2"><a href="case-study-bada.html" style="color: #222;">Bada Language Institute</a></h4>
                <p class="mb-3" style="color: #555;">We engineered a robust digital platform to centralize the institute's course offerings and event schedules.</p>
                <a href="case-study-bada.html" style="font-weight: 600; color: #0056b3;">Read Case Study &rarr;</a>
              </div>
            </div>
            <div class="col-md-6 mb-4">
              <div style="padding: 30px; background: #f8f9fa; border-left: 4px solid #28a745; border-radius: 4px; height: 100%;">
                <h4 class="mb-2"><a href="case-study-audiophile.html" style="color: #222;">Audiophile E-Commerce</a></h4>
                <p class="mb-3" style="color: #555;">A deeply responsive e-commerce architecture showcasing advanced state management and dynamic routing.</p>
                <a href="case-study-audiophile.html" style="font-weight: 600; color: #0056b3;">Read Case Study &rarr;</a>
              </div>
            </div>
          </div>
          <div class="row pt-4">
            <div class="col-12 text-center">
              <a href="client-success.html" class="octf-btn octf-btn-third">View All Case Studies</a>
            </div>
          </div>
        </div>
      </section>
""",
    "cybersecurity.html": """
      <!-- Related Case Studies Section -->
      <section style="padding: 80px 0; background-color: #fff;">
        <div class="container">
          <div class="row mb-4">
            <div class="col-12 text-center">
              <div class="ot-heading">
                <span>// proof of output</span>
                <h2 class="main-heading">Featured Security Integrations</h2>
              </div>
            </div>
          </div>
          <div class="row justify-content-center">
            <div class="col-md-6 mb-4">
              <div style="padding: 30px; background: #f8f9fa; border-left: 4px solid #0056b3; border-radius: 4px; height: 100%;">
                <h4 class="mb-2"><a href="case-study-sgss.html" style="color: #222;">Siri Guru Singh Sabha Portal</a></h4>
                <p class="mb-3" style="color: #555;">A comprehensive community portal built from the ground up for secure, robust data management.</p>
                <a href="case-study-sgss.html" style="font-weight: 600; color: #0056b3;">Read Case Study &rarr;</a>
              </div>
            </div>
            <div class="col-md-6 mb-4">
              <div style="padding: 30px; background: #f8f9fa; border-left: 4px solid #28a745; border-radius: 4px; height: 100%;">
                <h4 class="mb-2"><a href="case-study-greenremedies.html" style="color: #222;">Green Remedies Auth</a></h4>
                <p class="mb-3" style="color: #555;">An authenticated e-commerce web app emphasizing role-based security architectures with Kinde Auth.</p>
                <a href="case-study-greenremedies.html" style="font-weight: 600; color: #0056b3;">Read Case Study &rarr;</a>
              </div>
            </div>
          </div>
          <div class="row pt-4">
            <div class="col-12 text-center">
              <a href="client-success.html" class="octf-btn octf-btn-third">View All Case Studies</a>
            </div>
          </div>
        </div>
      </section>
""",
    "technology-strategy.html": """
      <!-- Related Case Studies Section -->
      <section style="padding: 80px 0; background-color: #fff;">
        <div class="container">
          <div class="row mb-4">
            <div class="col-12 text-center">
              <div class="ot-heading">
                <span>// proof of output</span>
                <h2 class="main-heading">Featured Strategy Case Studies</h2>
              </div>
            </div>
          </div>
          <div class="row justify-content-center">
            <div class="col-md-6 mb-4">
              <div style="padding: 30px; background: #f8f9fa; border-left: 4px solid #0056b3; border-radius: 4px; height: 100%;">
                <h4 class="mb-2"><a href="case-study-bada.html" style="color: #222;">Bada Language Institute</a></h4>
                <p class="mb-3" style="color: #555;">Transforming an educational institute's digital operations through structured, scalable platform design.</p>
                <a href="case-study-bada.html" style="font-weight: 600; color: #0056b3;">Read Case Study &rarr;</a>
              </div>
            </div>
            <div class="col-md-6 mb-4">
              <div style="padding: 30px; background: #f8f9fa; border-left: 4px solid #28a745; border-radius: 4px; height: 100%;">
                <h4 class="mb-2"><a href="case-study-transitflow.html" style="color: #222;">Transit Flow Logistics</a></h4>
                <p class="mb-3" style="color: #555;">Rapid prototyping strategies demonstrating execution speed from Figma directly into responsive React code.</p>
                <a href="case-study-transitflow.html" style="font-weight: 600; color: #0056b3;">Read Case Study &rarr;</a>
              </div>
            </div>
          </div>
          <div class="row pt-4">
            <div class="col-12 text-center">
              <a href="client-success.html" class="octf-btn octf-btn-third">View All Case Studies</a>
            </div>
          </div>
        </div>
      </section>
"""
}

for filename, html_block in injections.items():
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Inject it right before the CTA Section
    if "<!-- CTA Section -->" in content:
        content = content.replace("<!-- CTA Section -->", html_block + "\n      <!-- CTA Section -->")
    else:
        # Fallback to before the footer
        content = content.replace('<footer id="site-footer"', html_block + '\n      <footer id="site-footer"')
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Injected case study links into service pages.")
