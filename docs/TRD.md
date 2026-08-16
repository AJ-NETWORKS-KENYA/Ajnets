# AJNETWORKS — Technical Requirements Document (TRD)

> **Version:** 1.0.0  
> **Maintainer:** AJNETWORKS Engineering  

---

## 1. Tech Stack
- **Frontend Core:** HTML5, Modern Vanilla CSS (Tokens & Variables), Modular JavaScript (ES6+).
- **Headless CMS:** Sanity.io (`services/cms/`) for structured publishing (Insights, Case Studies, Services).
- **Hosting & Edge Delivery:** Vercel Edge Network (Primary) with automated deploy hooks.
- **API Runtime:** Vercel Serverless Functions (`/api/*`) with honeypot bot trap & IP rate limiting.
- **Language / Automation:** Python 3.11+ for gate testing, SEO evals, build minification, and tooling.

## 2. Environment Variables & Credentials
- Stored securely in Vercel environment settings and `.env` / `.env.local` (gitignored).
- `CONTACT_RECIPIENT_EMAIL`: Primary lead notification address.
- `TURNSTILE_SECRET_KEY`: Bot verification token.

## 3. SEO & Metadata Standards
- Canonical domain: `https://ajnetworks.co`
- JSON-LD Structured Data: `Organization`, `WebSite`, `BreadcrumbList`.
- Open Graph (`og:url`, `og:image`, `og:title`, `og:description`) on all HTML entrypoints.
- Automated gate tests & eval scripts in `execution/` enforcing strict compliance.
