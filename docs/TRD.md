# AJNETWORKS — Technical Requirements Document (TRD)

> **Version:** 2.0.0  
> **Maintainer:** AJNETWORKS Engineering  

---

## 1. Tech Stack
- **Static Site Generator & Framework:** Astro 5+ (`output: 'static'`, `build.format: 'file'`), shipping **0 KB** of client-side framework JavaScript by default.
- **Content Layer:** Astro Content Collections (`src/content/`) with build-time Zod schema validation (`src/content.config.ts`) for `caseStudies`, `services`, `companyPages`, and `insights`.
- **Frontend Styling & Interactions:** HTML5, Modern Vanilla CSS (`style.min.css`, Brand Book tokens), and progressively enhanced modular JavaScript.
- **Headless CMS Schema Parity:** Sanity.io (`services/cms/`) schemas aligned with Astro Content Collections.
- **Hosting & Edge Delivery:** Vercel Edge Network (Primary) serving Astro's `dist/` output with clean URLs and security headers.
- **API Runtime:** Vercel Serverless Functions (`/api/contact.js`) with honeypot bot trap (`bot_field`), IP rate limiting, and regional SMTP routing.
- **Language / Automation:** Node.js 22+ (`node --test`) and Python 3.11+ for gate testing, SEO evals, and regression audits (`execution/`).

## 2. Environment Variables & Credentials
- Stored securely in Vercel environment settings and `.env` / `.env.local` (gitignored).
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `RECEIVER_EMAIL`: Primary Kenya HQ notification SMTP settings.
- `RWANDA_SMTP_HOST`, `RWANDA_SMTP_PORT`, `RWANDA_SMTP_USER`, `RWANDA_SMTP_PASS`, `RWANDA_RECEIVER_EMAIL`: Regional Rwanda notification SMTP settings.

## 3. SEO & Metadata Standards
- Canonical domain: `https://ajnetworks.co`
- Enforced structurally via `src/layouts/BaseLayout.astro`:
  - JSON-LD Structured Data: `Organization` (global) plus page-specific `WebSite`, `BreadcrumbList`, `Article`, `FAQPage`, and `Service` schemas.
  - Open Graph (`og:url`, `og:image`, `og:title`, `og:description`, `og:type`) and Twitter Card tags on all 25 HTML entrypoints.
  - Google Consent Mode v2 (`default: denied`) + guarded Analytics tags.
- Automated gate tests & eval scripts (`npm test`, `execution/test_brand_links.py`, `execution/eval_brand_seo.py`) enforcing 100% compliance on `dist/`.
