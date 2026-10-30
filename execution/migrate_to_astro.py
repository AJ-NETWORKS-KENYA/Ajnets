import os
import re
import json
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent.parent

STANDARD_FOOTER_SCRIPTS = {
    "/js/jquery.min.js",
    "/js/jquery.magnific-popup.min.js",
    "/js/jquery.isotope.min.js",
    "/js/owl.carousel.min.js",
    "/js/scripts.js",
    "/js/header-mobile.js",
    "/js/cookie-consent.js",
}

PAGE_SOURCES = [
    ("system", "index", ROOT_DIR / "index.html"),
    ("system", "404", ROOT_DIR / "404.html"),
    ("system", "elements", ROOT_DIR / "elements" / "elements.html"),
    ("company", "about-us", ROOT_DIR / "company" / "about-us.html"),
    ("company", "book-consultation", ROOT_DIR / "company" / "book-consultation.html"),
    ("company", "faq", ROOT_DIR / "company" / "faq.html"),
    ("company", "privacy", ROOT_DIR / "company" / "privacy.html"),
    ("company", "responsible-disclosure", ROOT_DIR / "company" / "responsible-disclosure.html"),
    ("company", "terms", ROOT_DIR / "company" / "terms.html"),
    ("services", "services", ROOT_DIR / "services" / "services.html"),
    ("services", "cybersecurity", ROOT_DIR / "services" / "cybersecurity.html"),
    ("services", "networking", ROOT_DIR / "services" / "networking.html"),
    ("services", "performance-seo", ROOT_DIR / "services" / "performance-seo.html"),
    ("services", "software-engineering", ROOT_DIR / "services" / "software-engineering.html"),
    ("services", "technology-strategy", ROOT_DIR / "services" / "technology-strategy.html"),
    ("caseStudies", "client-success", ROOT_DIR / "portfolio" / "client-success.html"),
    ("caseStudies", "case-study-audiophile", ROOT_DIR / "portfolio" / "case-study-audiophile.html"),
    ("caseStudies", "case-study-bada", ROOT_DIR / "portfolio" / "case-study-bada.html"),
    ("caseStudies", "case-study-crappo", ROOT_DIR / "portfolio" / "case-study-crappo.html"),
    ("caseStudies", "case-study-greenremedies", ROOT_DIR / "portfolio" / "case-study-greenremedies.html"),
    ("caseStudies", "case-study-racnyali", ROOT_DIR / "portfolio" / "case-study-racnyali.html"),
    ("caseStudies", "case-study-sgss", ROOT_DIR / "portfolio" / "case-study-sgss.html"),
    ("caseStudies", "case-study-transitflow", ROOT_DIR / "portfolio" / "case-study-transitflow.html"),
    ("insights", "insights", ROOT_DIR / "insights" / "insights.html"),
    ("insights", "post", ROOT_DIR / "insights" / "post.html"),
]


def extract_page_data(collection: str, slug: str, filepath: Path) -> dict:
    raw = filepath.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")
    head = soup.find("head")

    title_tag = head.find("title") if head else None
    title = title_tag.get_text().strip() if title_tag else f"{slug} | AJNETWORKS"

    desc_tag = head.find("meta", attrs={"name": re.compile(r"^description$", re.I)}) if head else None
    description = desc_tag.get("content", "").strip() if desc_tag else ""

    kw_tag = head.find("meta", attrs={"name": re.compile(r"^keywords$", re.I)}) if head else None
    keywords = kw_tag.get("content", "").strip() if kw_tag else None

    canon_tag = head.find("link", attrs={"rel": "canonical"}) if head else None
    canonical_url = canon_tag.get("href", "").strip() if canon_tag else f"https://ajnetworks.co/{slug}"

    og_type_tag = head.find("meta", attrs={"property": "og:type"}) if head else None
    og_type = og_type_tag.get("content", "website").strip() if og_type_tag else "website"
    if og_type not in ("website", "article"):
        og_type = "website"

    og_image_tag = head.find("meta", attrs={"property": "og:image"}) if head else None
    og_image = og_image_tag.get("content", "https://ajnetworks.co/images/og-home.webp").strip() if og_image_tag else "https://ajnetworks.co/images/og-home.webp"

    preload_tag = head.find("link", attrs={"rel": "preload", "as": "image"}) if head else None
    preload_image = preload_tag.get("href", "").strip() if preload_tag else None

    extra_head_styles = []
    if head:
        for st in head.find_all("style"):
            css_text = st.string or st.get_text()
            if css_text and css_text.strip():
                extra_head_styles.append(css_text.strip())

    extra_json_ld = []
    if head:
        for script_tag in head.find_all("script", attrs={"type": "application/ld+json"}):
            raw_json = (script_tag.string or script_tag.get_text() or "").strip()
            if not raw_json:
                continue
            try:
                parsed = json.loads(raw_json)
                if isinstance(parsed, dict) and parsed.get("@type") == "Organization" and "sameAs" in parsed:
                    continue
                extra_json_ld.append(json.dumps(parsed, indent=2))
            except Exception:
                extra_json_ld.append(raw_json)

    # Extract body html strictly between </header> and <footer
    header_end = raw.find("</header>")
    footer_start = raw.find('<footer class="site-footer')
    if footer_start == -1:
        footer_start = raw.find("<footer")
    if header_end == -1 or footer_start == -1:
        raise ValueError(f"Could not locate </header> or <footer> in {filepath}")

    body_html = raw[header_end + len("</header>"):footer_start].strip()

    # Check if extra scripts exist in body
    extra_footer_scripts = []
    body = soup.find("body")
    if body:
        for sc in body.find_all("script"):
            src = sc.get("src")
            if src and src not in STANDARD_FOOTER_SCRIPTS:
                extra_footer_scripts.append(src)

    show_rwanda_banner = 'id="rwanda-banner"' in raw
    wrap_in_site_div = '<div class="site" id="page">' in raw or '<div id="page" class="site">' in raw

    data = {
        "slug": slug,
        "title": title,
        "description": description,
        "canonicalUrl": canonical_url,
        "ogType": og_type,
        "ogImage": og_image,
        "extraJsonLd": extra_json_ld,
        "extraHeadStyles": extra_head_styles,
        "extraFooterScripts": extra_footer_scripts,
        "showRwandaBanner": show_rwanda_banner,
        "wrapInSiteDiv": wrap_in_site_div,
        "bodyHtml": body_html,
    }
    if keywords:
        data["keywords"] = keywords
    if preload_image:
        data["preloadImage"] = preload_image

    # Collection-specific structured fields
    if collection == "caseStudies":
        badges = [b.get_text().strip() for b in soup.select(".tech-badge") if b.get_text().strip()]
        data["badges"] = badges
        for item in soup.select(".sidebar-meta-item"):
            label_el = item.select_one(".sidebar-meta-label")
            val_el = item.select_one(".sidebar-meta-value")
            if label_el and val_el:
                lbl = label_el.get_text().strip().lower()
                val = val_el.get_text().strip()
                if lbl == "client":
                    data["client"] = val
                elif lbl == "industry":
                    data["industry"] = val
                elif lbl == "technologies":
                    data["technologies"] = val
                elif lbl == "timeline":
                    data["timeline"] = val

    if collection == "services":
        hero_h1 = soup.select_one(".page-hero h1")
        hero_p = soup.select_one(".page-hero p")
        if hero_h1:
            data["heroTitle"] = hero_h1.get_text().strip()
        if hero_p:
            data["heroSubtitle"] = hero_p.get_text().strip()

    return data


def copy_static_assets_to_public():
    public_dir = ROOT_DIR / "public"
    public_dir.mkdir(exist_ok=True)

    asset_dirs = ["css", "js", "images", "fonts"]
    for d in asset_dirs:
        src_dir = ROOT_DIR / d
        dst_dir = public_dir / d
        if src_dir.exists():
            if dst_dir.exists():
                shutil.rmtree(dst_dir)
            shutil.copytree(src_dir, dst_dir)
            print(f"Copied directory {d}/ -> public/{d}/")

    asset_files = ["style.css", "style.min.css", "robots.txt", "sitemap.xml", ".htaccess"]
    for f in asset_files:
        src_file = ROOT_DIR / f
        dst_file = public_dir / f
        if src_file.exists():
            shutil.copy2(src_file, dst_file)
            print(f"Copied file {f} -> public/{f}")


def main():
    print("Starting deterministic migration to Astro Content Collections...")
    for collection, slug, filepath in PAGE_SOURCES:
        if not filepath.exists():
            raise FileNotFoundError(f"Missing expected source file: {filepath}")
        out_dir = ROOT_DIR / "src" / "content" / collection
        out_dir.mkdir(parents=True, exist_ok=True)
        data = extract_page_data(collection, slug, filepath)
        out_file = out_dir / f"{slug}.json"
        out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  [OK] {collection}/{slug}.json ({len(data['bodyHtml'])} bytes body)")

    copy_static_assets_to_public()
    print("Migration extraction complete!")


if __name__ == "__main__":
    main()

