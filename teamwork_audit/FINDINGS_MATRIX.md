# AJNETWORKS Digital Presence Audit — Prioritized Findings Matrix

This matrix categorizes all **36 distinct findings** discovered during the comprehensive internal audit of AJNETWORKS (`https://ajnetworks.co`).

**Priority Classifications**:
- **P0 (Critical)**: Active security compromise, critical functional blocker, or catastrophic data loss risk (0 found).
- **P1 (High)**: Major architectural flaw, compliance liability, significant SEO indexing penalty, or severe user experience defect (8 found).
- **P2 (Medium)**: Noticeable performance penalty, incomplete feature/schema standard, brand guideline divergence, or moderate security hardening gap (17 found).
- **P3 (Low)**: Minor code hygiene issue, asset optimization opportunity, typo, or secondary documentation gap (11 found).

---

## Comprehensive Findings Table

| ID | Priority | Category | Finding Summary | Affected File(s) / Route(s) | Root Cause | Remediation Strategy | Effort | Impact |
|:---|:---:|:---|:---|:---|:---|:---|:---:|:---:|
| **F-01** | **P1** | SEO | **Canonical Tag vs Sitemap URL Disparity** | All 20 Subpages (`company/*`, `services/*`, `portfolio/*`, `insights/*`) | Canonical tags hardcoded to internal file paths (`/company/about-us`) instead of public clean URLs (`/about-us`). | Update `<link rel="canonical">` across all HTML pages to match public clean URLs declared in `sitemap.xml`. | 2 hrs | High |
| **F-02** | **P1** | SEO | **Open Graph URL Disparity** | All 20 Subpages | `<meta property="og:url">` mirrors internal directory paths rather than public clean URLs. | Update all `og:url` tags to canonical public URLs (`https://ajnetworks.co/slug`). | 1 hr | High |
| **F-03** | **P1** | UX / Technical | **Missing Custom 404 Error Recovery Page** | Global / Root (`404.html`) | No custom `404.html` exists in root; Vercel serves default unbranded error page. | Create branded `404.html` matching design system with navigation, search, and CTA. | 3 hrs | High |
| **F-04** | **P1** | Compliance / Trust | **Missing Dedicated Legal & Privacy Policy Pages** | `company/privacy-policy.html`, `terms-of-service.html`, `responsible-disclosure.html` | Footer links proxy to `/faq` instead of actual legally binding policies. | Author and deploy dedicated policy pages adhering to Kenya DPA 2019 and `data.md`. | 4 hrs | High |
| **F-05** | **P1** | Security | **In-Memory Rate Limiting Fails in Serverless** | `api/contact.js` | Serverless lambda ephemeral memory prevents persistence of `ipRateLimit` Map across instances. | Replace in-memory Map with Upstash Redis / Vercel KV distributed rate limiter. | 4 hrs | High |
| **F-06** | **P1** | SEO | **Incomplete Schema.org Types on Specialized Pages** | `services/*.html`, `company/faq.html`, `portfolio/*.html` | All pages only declare generic `Organization` schema; missing domain-specific schemas. | Add `Service`, `FAQPage`, `Article`/`CreativeWork`, and `ContactPage` schemas. | 4 hrs | High |
| **F-07** | **P1** | SEO / Code Quality | **Empty Placeholder BreadcrumbList Comments** | All 8 Portfolio Pages (`portfolio/*.html`) | Comment `<!-- BreadcrumbList Schema -->` exists with no JSON-LD script underneath. | Inject valid `BreadcrumbList` JSON-LD schema on all portfolio and service pages. | 2 hrs | High |
| **F-08** | **P1** | Performance / Security | **Client-Side Runtime Tailwind CDN in CSP** | `vercel.json` | CSP permits `https://cdn.tailwindcss.com` which is intended solely for local prototyping. | Precompile Tailwind CSS via PostCSS/CLI build step and remove CDN from CSP. | 3 hrs | High |
| **F-09** | **P2** | Performance | **Uncompressed Image Assets Exceeding 200KB** | `images/` (34 assets, e.g. `favicon.svg`, `home-about.jpg`) | Large uncompressed SVG and high-res raster JPG/PNG assets committed to repository. | Compress SVGs (SVGO) and convert raster images to optimized WebP/AVIF (<100KB). | 3 hrs | Medium |
| **F-10** | **P2** | Performance / UX | **Missing Explicit Width and Height on Images** | 104+ Images across 21 pages (e.g. `insights/post.html`) | Omitted `width` and `height` attributes cause Cumulative Layout Shift (CLS). | Add exact `width` and `height` attributes or CSS aspect-ratio on all `<img>` tags. | 3 hrs | Medium |
| **F-11** | **P2** | Performance | **Missing `loading="lazy"` on Below-Fold Images** | Multiple subpage content and header illustrations | Eager image loading triggers bandwidth competition during First Contentful Paint. | Audit and apply `loading="lazy"` on all below-the-fold image tags. | 2 hrs | Medium |
| **F-12** | **P2** | Security | **Permissive CSP `'unsafe-inline'` Directive** | `vercel.json` | CSP uses `'unsafe-inline'` for `script-src` and `style-src` without hashes/nonces. | Refactor inline scripts to external bundles or inject SHA-256 script hashes in CSP. | 4 hrs | Medium |
| **F-13** | **P2** | Compliance | **Pre-Consent Third-Party Script Execution** | `gtag.js` and LinkedIn tags in `<head>` across all pages | Analytics scripts load synchronously before user accepts cookie consent banner. | Gate `gtag` and LinkedIn tracking behind `cookie-consent.js` user opt-in event. | 3 hrs | Medium |
| **F-14** | **P2** | Code Quality | **Placeholder LinkedIn Partner ID in Production** | All 21 HTML pages (`_linkedin_partner_id = "YOUR_LINKEDIN_PID"`) | Boilerplate snippet unconfigured with real client ID. | Replace with active production LinkedIn Partner ID or remove snippet until configured. | 1 hr | Medium |
| **F-15** | **P2** | UX / Credibility | **Dead Navigation Links (`href="#"`) in Footer** | All 21 HTML pages (`Status`, `Documentation`) | Hardcoded `#` anchor placeholders in footer widget resources list. | Replace with valid destinations or remove links until documentation portals launch. | 1 hr | Medium |
| **F-16** | **P2** | Credibility / UX | **Template Video Popup Linking to Dummy Video** | `company/about-us.html` (line 267) | WordPress theme relic video popup links to generic YouTube demo video (`lfDZJqSrIuk`). | Update to official AJNETWORKS YouTube video or replace with static consulting graphic. | 1 hr | Medium |
| **F-17** | **P2** | Architecture | **Unprotected Internal UI Catalog `elements.html`** | `elements/elements.html` | UI component sandbox is publicly accessible and crawlable without noindex directive. | Add `<meta name="robots" content="noindex, nofollow"/>` and disallow in `robots.txt`. | 1 hr | Medium |
| **F-18** | **P2** | Security | **Lack of Cryptographic CAPTCHA on Contact Form** | `api/contact.js` & `company/book-consultation.html` | Relies solely on hidden `bot_field` honeypot, vulnerable to automated headless bots. | Integrate Cloudflare Turnstile or Google reCAPTCHA v3 verification in backend. | 3 hrs | Medium |
| **F-19** | **P2** | Brand Positioning | **Banned Buzzwords Violating Tone Guidelines** | `company/faq.html`, `insights/post.html` | Text contains "innovative" and "cutting-edge" prohibited by `data.md` Section 5. | Rewrite copy to outcome-based phrasing per `data.md` consultant tone standard. | 1 hr | Medium |
| **F-20** | **P2** | UI / Credibility | **Typographical Error in Ecosystem Section** | `index.html` (line 779) | Typo: `<h5>Wearalables</h5>` instead of `Wearables`. | Correct typo to `Wearables`. | 0.5 hr | Medium |
| **F-21** | **P2** | UX / SEO | **Internal Links with `target="_blank"` & Deep Paths** | `index.html` (lines 748-783) | Internal tech ecosystem cards use `/services/software-engineering` with new tab target. | Change links to `/software-engineering` and remove `target="_blank"`. | 1 hr | Medium |
| **F-22** | **P2** | Strategic Positioning | **Case Studies Missing Structured 10-Point Elements** | `portfolio/case-study-*.html` | Case studies lack explicit Timelines, Tech Stack pills, and quantified ROI percentages. | Refactor case studies to include all 10 standard transformation sections from `data.md`. | 4 hrs | Medium |
| **F-23** | **P2** | Design System | **Non-Standard Font Declarations in CSS** | `css/*.css` | CSS mentions "DM Sans" and "Montserrat Alternates" not defined in design system. | Consolidate CSS typography strictly to Montserrat (headings) & Nunito Sans (body). | 2 hrs | Medium |
| **F-24** | **P2** | Accessibility | **Generic and Context-Poor Image Alt Text** | Global (`alt="Code 1"`, `alt="Our Mission"`, `alt="image"`) | Image alt attributes use theme template icon names or redundant phrases. | Enhance all alt text to be descriptive and context-rich for screen readers. | 2 hrs | Medium |
| **F-25** | **P2** | Security | **Missing Subresource Integrity (SRI) on CDNs** | `<head>` across all pages (Google Fonts, FontAwesome) | External CDN resources loaded without `integrity` cryptographic hash attributes. | Add `integrity="sha384-..."` and `crossorigin="anonymous"` to all third-party CDNs. | 2 hrs | Medium |
| **F-26** | **P3** | SEO | **Meta Descriptions Exceeding 160 Characters** | `company/about-us.html`, `index.html`, `company/faq.html` | Verbose meta descriptions (169–198 chars) cause truncation in search engine snippets. | Trim meta descriptions to concise 140–155 character summaries. | 1 hr | Low |
| **F-27** | **P3** | Performance | **Legacy Raster Assets Without AVIF/WebP Formats** | `images/` (419 legacy PNG/JPG assets) | Raster assets lack automated modern next-gen format conversion. | Implement automated WebP/AVIF image generation pipeline via build script. | 3 hrs | Low |
| **F-28** | **P3** | Technical / Hygiene | **Unused E-Commerce Stylesheet in Codebase** | `css/woocommerce.css` | 24KB WooCommerce stylesheet left over from base HTML template. | Remove `css/woocommerce.css` from repository and purge unused CSS classes. | 0.5 hr | Low |
| **F-29** | **P3** | Performance | **Legacy jQuery Plugins Loaded on Static Pages** | Global (`owl.carousel`, `isotope`, `magnific-popup`) | Heavy legacy libraries loaded globally even on pages where no carousels exist. | Conditionally load jQuery plugins only on pages where interactive components reside. | 3 hrs | Low |
| **F-30** | **P3** | Security | **Security Header Mismatch (`X-Frame-Options` vs CSP)** | `vercel.json` | `X-Frame-Options: SAMEORIGIN` vs CSP `frame-ancestors 'none'`. | Harmonize headers to `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'`. | 0.5 hr | Low |
| **F-31** | **P3** | Credibility | **Personal LinkedIn Profile Mixed in Corporate Pages** | `company/about-us.html` | Contains personal profile link (`/in/jabrahamjohns`) without distinct leadership context. | Clearly label as Founder/Managing Director profile or link to corporate LinkedIn page. | 0.5 hr | Low |
| **F-32** | **P3** | SEO / Technical | **Static XML Sitemap Lacks Dynamic Build Generator** | `sitemap.xml` | Lastmod timestamps are hardcoded and not automatically updated on build/commit. | Add `npm run sitemap` build script to auto-generate `sitemap.xml` with git mtimes. | 2 hrs | Low |
| **F-33** | **P3** | Performance | **Missing Preconnect & DNS-Prefetch Hints** | `<head>` across all pages | No preconnect hints for Google Fonts (`fonts.googleapis.com`) or Analytics CDNs. | Add `<link rel="preconnect" href="https://fonts.googleapis.com">` and `fonts.gstatic.com`. | 1 hr | Low |
| **F-34** | **P3** | SEO / Accessibility | **Heading Hierarchy Level Skips** | Several content sections (`<h2>` to `<h4>`) | Skipping `<h3>` violates sequential heading hierarchy rules for accessibility. | Refactor headings to strictly follow sequential `<h1>` -> `<h2>` -> `<h3>` -> `<h4>` hierarchy. | 2 hrs | Low |
| **F-35** | **P3** | Engineering System | **Missing Automated CI/CD Linting and Audit Gates** | `package.json` & `.github/workflows/` | No automated Lighthouse CI, HTML validator, or broken link checker in CI pipeline. | Configure GitHub Actions / npm scripts with HTML-validate and Lighthouse CI gates. | 3 hrs | Low |
| **F-36** | **P3** | SEO / Local Business | **Missing Opening Hours & Telephone Microdata** | `company/book-consultation.html` | Working hours and phone numbers are plaintext without schema markup. | Add `LocalBusiness` / `OpeningHoursSpecification` structured microdata to contact page. | 1 hr | Low |

---

## Findings Summary by Dimension

```
SEO & Discoverability:           7 Findings (F-01, F-02, F-06, F-07, F-26, F-32, F-36)
Performance & Core Web Vitals:   7 Findings (F-08, F-09, F-10, F-11, F-27, F-29, F-33)
Security & Data Privacy:         6 Findings (F-05, F-12, F-13, F-18, F-25, F-30)
Credibility & Compliance:        5 Findings (F-04, F-14, F-15, F-16, F-31)
UX / UI & Accessibility:         5 Findings (F-03, F-17, F-20, F-21, F-24)
Strategic Positioning:           3 Findings (F-19, F-22, F-34)
Technical & Code Hygiene:        3 Findings (F-23, F-28, F-35)
─────────────────────────────────────────────────────────────────────────────
Total Distinct Findings:         36 Findings (8 P1 High, 17 P2 Medium, 11 P3 Low)
```
