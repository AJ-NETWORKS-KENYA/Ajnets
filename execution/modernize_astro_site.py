import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / "src" / "content"
PUBLIC_DIR = ROOT_DIR / "public"

HTML_404 = """
<div class="site-content" id="content">
  <div class="page-hero bg-dark-primary" style="padding: 130px 0 90px;">
    <div class="container text-center">
      <nav aria-label="Breadcrumb" class="breadcrumb-nav justify-content-center d-flex mb-3">
        <a href="/">Home</a>
        <span class="separator mx-2">/</span>
        <span class="current">404 Error</span>
      </nav>
      <span style="color: #43D9AD; font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 16px; letter-spacing: 2px; text-transform: uppercase;">// HTTP 404 — Resource Not Found</span>
      <h1 class="text-white mt-3" style="font-size: 56px; font-weight: 900;">Page Not Found</h1>
      <p style="color: rgba(255,255,255,0.8); font-size: 18px; max-width: 620px; margin: 18px auto 0;">
        The page or resource you requested may have been relocated, renamed, or retired as part of our platform architecture upgrades.
      </p>
    </div>
  </div>
  <section class="section-padd">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-8 text-center">
          <div class="outcome-box" style="background-color: #f8f9fa; padding: 48px; border-radius: 8px; border-left: 4px solid #00A3FF;">
            <h2 style="font-size: 28px; margin-bottom: 16px; color: #1E2132;">Where would you like to go next?</h2>
            <p style="font-size: 17px; color: #4b5563; margin-bottom: 32px;">
              Explore our core engineering practices, review verified client case studies, or schedule a direct advisory session with our team.
            </p>
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
              <a class="octf-btn octf-btn-primary" href="/">Return to Homepage</a>
              <a class="octf-btn octf-btn-third" href="/services">Explore Services</a>
              <a class="octf-btn octf-btn-third" href="/client-success">Client Case Studies</a>
              <a class="octf-btn octf-btn-third" href="/book-consultation">Book Consultation</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
""".strip()

HTML_PRIVACY = """
<div class="site-content" id="content">
  <div class="page-hero bg-dark-primary">
    <div class="container">
      <nav aria-label="Breadcrumb" class="breadcrumb-nav">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <span class="current">Privacy Policy</span>
      </nav>
      <h1 class="text-white mt-3">Privacy Policy</h1>
      <p style="color: rgba(255,255,255,0.75); font-size: 17px; max-width: 680px; margin-top: 15px;">
        How AJNETWORKS collects, processes, and safeguards personal and enterprise data in accordance with the Kenya Data Protection Act (2019), Rwanda Law No. 058/2021, and GDPR.
      </p>
    </div>
  </div>
  <section class="section-padd">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 offset-lg-2">
          <p style="color: #64748b; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Effective Date: August 16, 2026 | Last Updated: October 30, 2026</p>

          <div class="mb-5 mt-4">
            <div class="ot-heading">
              <span>// 01. data controller &amp; scope</span>
              <h2 class="main-heading">1. Overview &amp; Regulatory Alignment</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              AJNETWORKS ("we", "our", or "us") is committed to protecting the privacy and security of personal data entrusted to us by clients, prospective partners, and website visitors across Kenya, Rwanda, East Africa, and globally. We process personal data in strict compliance with the <strong>Kenya Data Protection Act, 2019</strong>, <strong>Rwanda Law No. 058/2021 Relating to the Protection of Personal Data and Privacy</strong>, and the <strong>EU General Data Protection Regulation (GDPR)</strong>.
            </p>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 02. information we collect</span>
              <h2 class="main-heading">2. Categories of Personal Data</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              We collect only the minimum data necessary to deliver our technology advisory and engineering services:
            </p>
            <ul style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              <li><strong>Consultation &amp; Inquiry Data:</strong> Name, organization name, email address, phone number, operating region, and project description when you submit our strategy call form.</li>
              <li><strong>Telemetry &amp; Consent-Gated Analytics:</strong> Anonymized interaction signals collected via Google Analytics 4 (GA4) strictly governed by <strong>Google Consent Mode v2</strong> (defaulting to <code>denied</code> until explicit opt-in consent is granted via our privacy banner).</li>
              <li><strong>Security &amp; Rate-Limiting Logs:</strong> Ephemeral IP metadata processed solely to prevent automated spam and abuse on our API endpoints.</li>
            </ul>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 03. purpose &amp; legal basis</span>
              <h2 class="main-heading">3. How We Use Your Data</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              We process personal information to respond to consultation requests, scope technical engagements, fulfill contractual obligations, maintain infrastructure security, and comply with statutory legal obligations. We never sell, rent, or trade personal data to third parties.
            </p>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 04. security &amp; retention</span>
              <h2 class="main-heading">4. Data Security &amp; Retention</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              All data transmissions are encrypted in transit via TLS 1.3 and guarded by HTTP Strict Transport Security (HSTS) and Content Security Policy (CSP) controls. Inquiry records are retained only for the duration required to service the business relationship or satisfy statutory record-keeping requirements.
            </p>
          </div>

          <div class="outcome-box" style="background-color: #f8f9fa; padding: 36px; border-radius: 8px; border-left: 4px solid #43D9AD;">
            <h3 style="font-size: 22px; margin-bottom: 12px; color: #1E2132;">5. Your Data Subject Rights &amp; Contact</h3>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563; margin-bottom: 0;">
              You have the right to request access, rectification, erasure, restriction of processing, or data portability at any time. To exercise your rights, contact our Data Protection Officer at <a href="mailto:hello@ajnetworks.co" style="color: #00A3FF; font-weight: 700;">hello@ajnetworks.co</a>.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
""".strip()

HTML_TERMS = """
<div class="site-content" id="content">
  <div class="page-hero bg-dark-primary">
    <div class="container">
      <nav aria-label="Breadcrumb" class="breadcrumb-nav">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <span class="current">Terms of Service</span>
      </nav>
      <h1 class="text-white mt-3">Terms of Service</h1>
      <p style="color: rgba(255,255,255,0.75); font-size: 17px; max-width: 680px; margin-top: 15px;">
        Governing terms for accessing the AJNETWORKS digital platform and engaging our enterprise consulting and engineering services.
      </p>
    </div>
  </div>
  <section class="section-padd">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 offset-lg-2">
          <p style="color: #64748b; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Effective Date: August 16, 2026 | Last Updated: October 30, 2026</p>

          <div class="mb-5 mt-4">
            <div class="ot-heading">
              <span>// 01. agreement to terms</span>
              <h2 class="main-heading">1. Scope of Terms</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              By accessing <code>https://ajnetworks.co</code> or engaging AJNETWORKS for technology strategy, custom software engineering, cybersecurity assurance, or IT infrastructure services, you agree to be bound by these Terms of Service and any Master Services Agreement (MSA) or Statement of Work (SOW) executed between your organization and AJNETWORKS.
            </p>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 02. consulting &amp; engineering deliverables</span>
              <h2 class="main-heading">2. Professional Engagements &amp; Intellectual Property</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              Specific project scope, milestones, acceptance criteria, and fees are governed by written Statements of Work. Upon full settlement of agreed fees under a client SOW, ownership of custom-developed client deliverables transfers as specified in the applicable contract, while AJNETWORKS retains ownership of its pre-existing frameworks, tooling, and brand assets.
            </p>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 03. acceptable use</span>
              <h2 class="main-heading">3. Platform Use &amp; Security Conduct</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              Users may not attempt unauthorized access, automated scraping, denial-of-service disruption, or form spam against AJNETWORKS infrastructure. Authorized security researchers should follow our <a href="/responsible-disclosure" style="color: #00A3FF; font-weight: 600;">Responsible Disclosure Policy</a>.
            </p>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 04. warranties &amp; liability</span>
              <h2 class="main-heading">4. Limitation of Liability &amp; Governing Law</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              Website content is provided for informational purposes "as is" without implied warranties. Unless otherwise stipulated in a signed Master Services Agreement, these terms are governed by the laws of the <strong>Republic of Kenya</strong> (and, for regional engagements executed through our Kigali operations, the laws of the <strong>Republic of Rwanda</strong>).
            </p>
          </div>

          <div class="outcome-box" style="background-color: #f8f9fa; padding: 36px; border-radius: 8px; border-left: 4px solid #00A3FF;">
            <h3 style="font-size: 22px; margin-bottom: 12px; color: #1E2132;">Questions Regarding Contractual Terms?</h3>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563; margin-bottom: 0;">
              Contact our legal and commercial advisory team at <a href="mailto:hello@ajnetworks.co" style="color: #00A3FF; font-weight: 700;">hello@ajnetworks.co</a> or <a href="/book-consultation" style="color: #00A3FF; font-weight: 700;">request an advisory consultation</a>.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
""".strip()

HTML_RESPONSIBLE_DISCLOSURE = """
<div class="site-content" id="content">
  <div class="page-hero bg-dark-primary">
    <div class="container">
      <nav aria-label="Breadcrumb" class="breadcrumb-nav">
        <a href="/">Home</a>
        <span class="separator">/</span>
        <span class="current">Responsible Disclosure</span>
      </nav>
      <h1 class="text-white mt-3">Responsible Disclosure Policy</h1>
      <p style="color: rgba(255,255,255,0.75); font-size: 17px; max-width: 680px; margin-top: 15px;">
        Our security-first commitment to coordinated vulnerability disclosure and safe harbor for ethical security researchers.
      </p>
    </div>
  </div>
  <section class="section-padd">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 offset-lg-2">
          <div class="mb-5">
            <div class="ot-heading">
              <span>// 01. security-first philosophy</span>
              <h2 class="main-heading">1. Commitment &amp; Safe Harbor</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              At AJNETWORKS, security is foundational to every system we engineer. We welcome reports from independent security researchers who discover potential vulnerabilities across <code>*.ajnetworks.co</code>. If you conduct good-faith research in accordance with this policy, we consider your research authorized and will not initiate legal action against you.
            </p>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 02. rules of engagement</span>
              <h2 class="main-heading">2. Guidelines for Ethical Testing</h2>
            </div>
            <ul style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              <li><strong>Avoid Service Disruption:</strong> Do not perform Denial of Service (DoS/DDoS), automated high-volume brute-forcing, or spam submissions against <code>/api/contact</code>.</li>
              <li><strong>Protect Data Integrity:</strong> Do not access, modify, or exfiltrate data belonging to third parties or clients. Stop testing immediately once a proof-of-concept is established.</li>
              <li><strong>No Social Engineering:</strong> Phishing or physical testing against AJNETWORKS personnel or client offices is strictly out of scope.</li>
            </ul>
          </div>

          <div class="mb-5">
            <div class="ot-heading">
              <span>// 03. reporting &amp; response sla</span>
              <h2 class="main-heading">3. How to Submit a Vulnerability Report</h2>
            </div>
            <p style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              Send a detailed technical report (affected URL/endpoint, reproduction steps, and impact assessment) to <a href="mailto:hello@ajnetworks.co" style="color: #00A3FF; font-weight: 700;">hello@ajnetworks.co</a> with the subject line <code>[SECURITY DISCLOSURE]</code>:
            </p>
            <ul style="font-size: 17px; line-height: 1.8; color: #4b5563;">
              <li><strong>Acknowledgment SLA:</strong> Within <strong>24 business hours</strong> of receipt.</li>
              <li><strong>Triage &amp; Validation:</strong> Within <strong>3 business days</strong>.</li>
              <li><strong>Remediation Target:</strong> Critical/High findings patched within <strong>7 days</strong> prior to coordinated public disclosure.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""".strip()


def update_legal_and_404_pages():
    updates = [
        (CONTENT_DIR / "system" / "404.json", HTML_404),
        (CONTENT_DIR / "company" / "privacy.json", HTML_PRIVACY),
        (CONTENT_DIR / "company" / "terms.json", HTML_TERMS),
        (CONTENT_DIR / "company" / "responsible-disclosure.json", HTML_RESPONSIBLE_DISCLOSURE),
    ]
    for path, new_html in updates:
        data = json.loads(path.read_text(encoding="utf-8"))
        data["bodyHtml"] = new_html
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  [MODERNIZED] {path.relative_to(ROOT_DIR)} ({len(new_html)} bytes)")


def ensure_image_dimensions():
    count_fixed = 0
    for json_file in CONTENT_DIR.rglob("*.json"):
        data = json.loads(json_file.read_text(encoding="utf-8"))
        soup = BeautifulSoup(data["bodyHtml"], "html.parser")
        changed = False
        for img in soup.find_all("img"):
            if not img.get("width"):
                img["width"] = "600"
                changed = True
                count_fixed += 1
            if not img.get("height"):
                img["height"] = "400"
                changed = True
        if changed:
            data["bodyHtml"] = str(soup)
            json_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  [CLS FIX] Added explicit width/height to {count_fixed} content images.")


def prune_legacy_jquery_and_unused_assets():
    obsolete_files = [
        PUBLIC_DIR / "js" / "jquery.min.js",
        PUBLIC_DIR / "js" / "jquery.magnific-popup.min.js",
        PUBLIC_DIR / "js" / "jquery.isotope.min.js",
        PUBLIC_DIR / "js" / "owl.carousel.min.js",
        PUBLIC_DIR / "js" / "scripts.js",
        PUBLIC_DIR / "js" / "header-mobile.js",
        PUBLIC_DIR / "css" / "magnific-popup.css",
        PUBLIC_DIR / "css" / "owl.carousel.min.css",
        PUBLIC_DIR / "css" / "owl.theme.css",
        PUBLIC_DIR / "css" / "animate.css",
        PUBLIC_DIR / "css" / "drift-basic.min.css",
        PUBLIC_DIR / "css" / "royal-preload.css",
    ]
    removed = 0
    bytes_saved = 0
    for f in obsolete_files:
        if f.exists():
            bytes_saved += f.stat().st_size
            f.unlink()
            removed += 1
            print(f"  [PRUNED] {f.relative_to(ROOT_DIR)}")
    print(f"  [BUNDLE REDUCTION] Removed {removed} legacy jQuery/CSS files ({bytes_saved / 1024:.1f} KB saved)")


if __name__ == "__main__":
    print("Modernizing Astro content and stripping legacy jQuery dependencies...")
    update_legal_and_404_pages()
    ensure_image_dimensions()
    prune_legacy_jquery_and_unused_assets()
    print("Done!")

