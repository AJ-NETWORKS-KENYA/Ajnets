import os
import re
from bs4 import BeautifulSoup

ROOT = r"c:\My Web Sites\ajnets\portfolio"

# We want the sidebar to have: Client, Industry, Technologies, Timeline, Related Services
def process_case_study(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
    except Exception as e:
        return False

    changed = False

    # 1. Update Sidebar
    sidebar = soup.find("ul", class_="sidebar-meta-list")
    if sidebar:
        # Extract existing values if any
        client = "TBD"
        industry = "TBD"
        tech = []
        
        for item in sidebar.find_all("li", class_="sidebar-meta-item"):
            label_div = item.find("div", class_="sidebar-meta-label")
            val_div = item.find("div", class_="sidebar-meta-value")
            if label_div and val_div:
                lbl = label_div.get_text(strip=True).lower()
                val = val_div.get_text(strip=True)
                if "client" in lbl:
                    client = val
                elif "industry" in lbl:
                    industry = val
                elif "platform" in lbl or "tech" in lbl:
                    tech.append(val)
                    
        # If tech is empty, grab it from badges in the hero
        if not tech:
            badges = soup.find_all("span", class_="tech-badge")
            for b in badges:
                tech.append(b.get_text(strip=True))

        tech_str = ", ".join(tech) if tech else "Various"

        new_sidebar_html = f"""
        <ul class="sidebar-meta-list">
            <li class="sidebar-meta-item">
                <div class="sidebar-meta-label">Client</div>
                <div class="sidebar-meta-value">{client}</div>
            </li>
            <li class="sidebar-meta-item">
                <div class="sidebar-meta-label">Industry</div>
                <div class="sidebar-meta-value">{industry}</div>
            </li>
            <li class="sidebar-meta-item">
                <div class="sidebar-meta-label">Technologies</div>
                <div class="sidebar-meta-value">{tech_str}</div>
            </li>
            <li class="sidebar-meta-item">
                <div class="sidebar-meta-label">Timeline</div>
                <div class="sidebar-meta-value">4 - 8 Weeks</div>
            </li>
            <li class="sidebar-meta-item">
                <div class="sidebar-meta-label">Related Services</div>
                <div class="sidebar-meta-value"><a href="/services/services.html" style="color: #43D9AD;">View Services</a></div>
            </li>
        </ul>
        """
        sidebar.replace_with(BeautifulSoup(new_sidebar_html, "html.parser"))
        changed = True

    # 2. Add Bottom CTA
    main_col = soup.find("div", class_="col-lg-8")
    if main_col:
        # Check if CTA already exists
        if not main_col.find("div", class_="case-study-cta"):
            cta_html = """
            <div class="case-study-cta" style="background-color: #f8f9fa; padding: 40px; border-radius: 8px; margin-top: 50px; border-left: 4px solid #43D9AD;">
                <h3 style="font-size: 24px; margin-bottom: 15px;">Ready to transform your business?</h3>
                <p style="margin-bottom: 25px;">Partner with us to engineer a technology solution that drives measurable growth and resilience.</p>
                <a href="/company/book-consultation.html" class="octf-btn octf-btn-primary">Book Advisory Session</a>
            </div>
            """
            
            # Insert before case-study-nav if it exists
            nav = main_col.find("nav", class_="case-study-nav")
            if nav:
                nav.insert_before(BeautifulSoup(cta_html, "html.parser"))
            else:
                main_col.append(BeautifulSoup(cta_html, "html.parser"))
            changed = True
            
    # 3. Rename headings if needed (Measurable Outcomes -> Business Results)
    headings = soup.find_all(["h2", "h3"])
    for h in headings:
        if "Measurable Outcomes" in h.get_text():
            h.string = "Business Results & Metrics"
            changed = True

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        return True
    return False

def main():
    count = 0
    for fname in os.listdir(ROOT):
        if fname.startswith("case-study-") and fname.endswith(".html"):
            fpath = os.path.join(ROOT, fname)
            if process_case_study(fpath):
                print(f"Updated {fname}")
                count += 1
    print(f"Done - updated {count} case studies.")

if __name__ == "__main__":
    main()
