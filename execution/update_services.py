import os
from bs4 import BeautifulSoup

ROOT = r"c:\My Web Sites\ajnets\services"

SERVICES_CONTENT = {
    "technology-strategy.html": {
        "title": "Technology & Digital Strategy",
        "subtitle": "Aligning technology investments with business objectives.",
        "problem": "Disconnected technology investments lead to operational silos, wasted resources, and stalled growth. Many organizations adopt tools without a clear strategy, resulting in fragmented systems that hinder rather than help.",
        "solution": "We align technology with your business goals through strategic roadmaps, digital transformation planning, and process optimization. We identify where AI and automation can be integrated as practical enablers to eliminate bottlenecks and accelerate workflows.",
        "why_us": "We evaluate technology through a business lens. We prioritize ROI, operational efficiency, and long-term viability over adopting the latest trends.",
        "outcome": "A clear, actionable technology roadmap that reduces operational complexity, aligns your digital infrastructure with your business goals, and drives measurable growth."
    },
    "software-engineering.html": {
        "title": "Software Engineering",
        "subtitle": "Engineering custom systems that scale with your operations.",
        "problem": "Off-the-shelf software often forces businesses to adapt their unique processes to the tool, limiting scalability and creating operational inefficiencies.",
        "solution": "We engineer custom enterprise systems, web applications, and seamless integrations tailored to your exact workflows. We embed intelligent automation and AI capabilities directly into your software to eliminate repetitive manual tasks and enhance decision-making.",
        "why_us": "We prioritize architecture, security, and maintainability from day one. We don't just write code; we engineer robust platforms designed to evolve alongside your business.",
        "outcome": "Streamlined operations, significantly reduced manual effort, and a secure, scalable digital platform that provides a distinct competitive advantage."
    },
    "cybersecurity.html": {
        "title": "Cybersecurity & Assurance",
        "subtitle": "Protecting your critical assets with security by design.",
        "problem": "As organizations scale, their digital footprint expands, exposing them to sophisticated threats. Many businesses lack the specialized expertise to build resilient, proactive defenses.",
        "solution": "We provide comprehensive security assessments, vulnerability management, and secure architecture design. We identify weaknesses before they are exploited and implement robust controls to protect your critical data.",
        "why_us": "We do not sell fear. We position security as a fundamental business enabler that ensures compliance, protects your reputation, and guarantees operational continuity.",
        "outcome": "Minimized digital risk, fortified infrastructure, regulatory compliance readiness, and the confidence to operate securely in a digital-first environment."
    },
    "networking.html": {
        "title": "Networking & IT Infrastructure",
        "subtitle": "Building reliable foundations for your digital operations.",
        "problem": "Fragile, outdated, or poorly configured IT infrastructure creates operational bottlenecks, unexpected downtime, and severe communication breakdowns across teams.",
        "solution": "We design, deploy, and manage robust network architectures, cloud environments, and modern workspace solutions including Microsoft 365, Google Workspace, and Zoho Workplace.",
        "why_us": "We build for high availability and zero friction. We ensure your underlying infrastructure is robust and invisible to your team—because it simply works.",
        "outcome": "Consistent high availability, seamless team collaboration, and a scalable infrastructure foundation capable of supporting your long-term growth."
    },
    "performance-seo.html": {
        "title": "Performance & SEO",
        "subtitle": "Maximizing digital reach through technical excellence.",
        "problem": "Slow, inaccessible, or poorly optimized digital platforms lose potential clients and damage brand credibility before a conversation even begins.",
        "solution": "We execute rigorous technical SEO, optimize Core Web Vitals, and ensure full WCAG 2.2 AA accessibility compliance to maximize your platform's reach and usability.",
        "why_us": "We focus entirely on technical excellence, structural integrity, and measurable performance data rather than superficial vanity metrics.",
        "outcome": "Lightning-fast load times, significantly higher organic search visibility, and a barrier-free, inclusive experience for all users."
    }
}

def generate_service_html(data):
    return f"""
    <!-- Page Hero -->
    <div class="page-hero bg-dark-primary">
        <div class="container">
            <nav aria-label="Breadcrumb" class="breadcrumb-nav">
                <a href="/index.html">Home</a>
                <span class="separator">/</span>
                <a href="/services/services.html">Services</a>
                <span class="separator">/</span>
                <span class="current">{data['title']}</span>
            </nav>
            <h1 class="text-white mt-3">{data['title']}</h1>
            <p style="color: rgba(255,255,255,0.75); font-size: 17px; max-width: 600px; margin-top: 15px;">
                {data['subtitle']}
            </p>
        </div>
    </div>
    
    <!-- Main Service Content -->
    <section class="section-padd">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 offset-lg-2">
                    
                    <div class="mb-5">
                        <div class="ot-heading">
                            <span>// the challenge</span>
                            <h2 class="main-heading">What problem exists?</h2>
                        </div>
                        <p style="font-size: 18px; line-height: 1.8; color: #4b5563;">{data['problem']}</p>
                    </div>

                    <div class="mb-5">
                        <div class="ot-heading">
                            <span>// our approach</span>
                            <h2 class="main-heading">How AJNETWORKS solves it</h2>
                        </div>
                        <p style="font-size: 18px; line-height: 1.8; color: #4b5563;">{data['solution']}</p>
                    </div>
                    
                    <div class="mb-5">
                        <div class="ot-heading">
                            <span>// the difference</span>
                            <h2 class="main-heading">Why clients trust us</h2>
                        </div>
                        <p style="font-size: 18px; line-height: 1.8; color: #4b5563;">{data['why_us']}</p>
                    </div>

                    <div class="outcome-box" style="background-color: #f8f9fa; padding: 40px; border-radius: 8px; border-left: 4px solid #43D9AD; margin-bottom: 50px;">
                        <h3 style="font-size: 24px; margin-bottom: 15px; color: #1A1A2E;">Measurable Outcomes</h3>
                        <p style="font-size: 18px; line-height: 1.8; color: #4b5563; margin-bottom: 0;"><strong>What to expect:</strong> {data['outcome']}</p>
                    </div>
                    
                    <div class="text-center mt-5">
                        <a href="/company/book-consultation.html" class="octf-btn octf-btn-primary btn-large">Book Advisory Session</a>
                    </div>
                    
                </div>
            </div>
        </div>
    </section>
    """

def process_service(filepath, filename):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
    except Exception as e:
        return False

    if filename not in SERVICES_CONTENT:
        return False
        
    data = SERVICES_CONTENT[filename]
    
    # Remove everything between header and footer
    header = soup.find("header")
    footer = soup.find("footer")
    
    if not header or not footer:
        return False
        
    # Clear out the body between header and footer
    curr = header.find_next_sibling()
    while curr and curr != footer:
        nxt = curr.find_next_sibling()
        # If it's a script tag or cookie banner at the bottom, keep it
        if curr.name == "script" or curr.get("id") == "cookie-consent-banner":
            pass
        else:
            curr.extract()
        curr = nxt
        
    new_content = BeautifulSoup(generate_service_html(data), "html.parser")
    header.insert_after(new_content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    return True

def main():
    count = 0
    for fname in os.listdir(ROOT):
        if fname in SERVICES_CONTENT:
            fpath = os.path.join(ROOT, fname)
            if process_service(fpath, fname):
                print(f"Updated {fname}")
                count += 1
    print(f"Done - updated {count} service pages.")

if __name__ == "__main__":
    main()
