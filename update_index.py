import os
import re

file_path = r"c:\My Web Sites\ajnets\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove Revolution Slider CSS
rev_css_pattern = re.compile(r'<!-- REVOLUTION SLIDER CSS -->\s*<link[\s\S]*?href="plugins/revolution/revolution/css/settings\.css"[\s\S]*?/>\s*<!-- REVOLUTION NAVIGATION STYLE -->\s*<link[\s\S]*?href="plugins/revolution/revolution/css/navigation\.css"[\s\S]*?/>', re.IGNORECASE)
content = re.sub(rev_css_pattern, '', content)

# 2. Add Schema and LinkedIn Tag before </head>
schema_and_linkedin = """
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "name": "AJNETWORKS",
          "url": "https://ajnetworkskenya.it.com/",
          "logo": "https://ajnetworkskenya.it.com/images/logo.png",
          "description": "AJNETWORKS is a technology consulting firm delivering strategic advisory, software engineering, cybersecurity, and IT infrastructure solutions.",
          "founder": {
            "@type": "Person",
            "name": "Abraham John"
          },
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+254-758-238-617",
            "contactType": "customer service",
            "email": "hello@ajnetworkskenya.it.com",
            "areaServed": "KE",
            "availableLanguage": "en"
          }
        },
        {
          "@type": "LocalBusiness",
          "name": "AJNETWORKS",
          "image": "https://ajnetworkskenya.it.com/images/logo.png",
          "url": "https://ajnetworkskenya.it.com/",
          "telephone": "+254 758 238 617",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Nairobi",
            "addressRegion": "Nairobi County",
            "addressCountry": "KE"
          }
        }
      ]
    }
    </script>
    
    <!-- LinkedIn Insight Tag -->
    <script type="text/javascript">
    _linkedin_partner_id = "YOUR_LINKEDIN_PID";
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(_linkedin_partner_id);
    </script><script type="text/javascript">
    (function(l) {
    if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
    window.lintrk.q=[]}
    var s = document.getElementsByTagName("script")[0];
    var b = document.createElement("script");
    b.type = "text/javascript";b.async = true;
    b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
    s.parentNode.insertBefore(b, s);})(window.lintrk);
    </script>
    <noscript>
    <img height="1" width="1" style="display:none;" alt="" src="https://px.ads.linkedin.com/collect/?pid=YOUR_LINKEDIN_PID&fmt=gif" />
    </noscript>
"""
content = re.sub(r'</head>', schema_and_linkedin + '\n</head>', content)

# 3. Replace the Revolution Slider block with Static Hero
slider_pattern = re.compile(r'<div\s*id="rev_slider_one_wrapper"[\s\S]*?<div\s*class="tp-bannertimer"[\s\S]*?</div>\s*</div>\s*</div>', re.IGNORECASE)

static_hero = """
        <div class="static-hero" style="background: url('images/slider/slide1-home1.jpg') no-repeat center center/cover; padding: 150px 0 100px; position: relative;">
            <div style="position: absolute; top:0; left:0; right:0; bottom:0; background: rgba(0,0,0,0.6);"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <div class="row">
                    <div class="col-lg-8 col-md-10">
                        <div class="title" style="color:#fff; font-family:'Nunito Sans', sans-serif; font-size:20px; text-transform:uppercase; margin-bottom:15px; font-weight: 600;">// Strategic Technology Consulting</div>
                        <h1 style="color:#fff; font-family:'Montserrat', sans-serif; font-size:60px; font-weight:900; line-height:1.2; margin-bottom: 25px;">
                            Technology decisions <br/>that move business forward
                        </h1>
                        <p style="color:#e0e0e0; font-family:'Nunito Sans', sans-serif; font-size:18px; line-height:1.8; margin-bottom:40px; max-width: 600px;">
                            AJNETWORKS is a technology consulting firm that designs, engineers, and secures digital systems aligned with real business goals.
                        </p>
                        <a href="book-consultation.html" class="octf-btn octf-btn-primary btn-slider btn-large" style="padding: 15px 35px; border-radius: 4px; font-weight: 700; font-size: 16px;">Book Advisory Session</a>
                    </div>
                </div>
            </div>
        </div>
"""

content = re.sub(slider_pattern, static_hero, content)

# 4. Remove Revolution JS Scripts at bottom of index.html
js_pattern = re.compile(r'<!-- REVOLUTION JS FILES -->[\s\S]*?<!-- SLIDER REVOLUTION 5\.0 EXTENSIONS  \(Load Extensions only on Local File Systems !  The following part can be removed on Server for On Demand Loading\) -->[\s\S]*?<script>[\s\S]*?revapi1\.showDoubleJqueryError[\s\S]*?</script>', re.IGNORECASE)
content = re.sub(js_pattern, '', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully with Schema, Static Hero, and Slider dependencies removed.")
