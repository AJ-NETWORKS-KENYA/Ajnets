# AJNETWORKS — System Architecture (ARCHITECTURE.md)

> **Version:** 2.0.0  
> **Maintainer:** AJNETWORKS Architecture Team  

---

## 1. System Overview

```
                    +-----------------------------------+
                    |   Astro 5+ Build Pipeline (SSG)   |
                    |  src/layouts + src/components +   |
                    |  src/content (Zod Collections)    |
                    +-----------------+-----------------+
                                      |
                                      | astro build (0 KB Framework JS)
                                      v
                          +------------------------+
                          |    Vercel Edge CDN     |
                          |  (Global Distribution) |
                          +-----------+------------+
                                      |
           +--------------------------+--------------------------+
           |                                                     |
           v                                                     v
+-----------------------+                             +--------------------+
| Static Output (dist/) |                             | Serverless API     |
| (25 HTML Pages, CSS,  |                             | (/api/contact.js)  |
|  JS, WebP, Sitemap)   |                             | Rate-Limited SMTP  |
+-----------------------+                             +--------------------+
```

## 2. Source Directory Architecture

```
<project-root>/
├── api/                     # Vercel Serverless Functions (contact.js + contact.test.js)
├── docs/                    # 6-Document Gate + Architecture & Decision Logs
├── execution/               # Deterministic Python Gate Tests & SEO Evals
├── public/                  # Static assets copied 1:1 to dist/ (css/, js/, images/, fonts/, robots.txt, sitemap.xml)
├── services/cms/            # Sanity Studio Headless CMS schemas
├── src/
│   ├── components/          # Reusable UI Partials (Header.astro, Footer.astro, CookieConsent.astro, RwandaBanner.astro)
│   ├── content/             # Structured JSON/Markdown Collections (caseStudies, services, company, insights)
│   ├── content.config.ts    # Zod Schema Definitions for Content Collections
│   ├── layouts/             # BaseLayout.astro (Single Source of Truth for SEO <head>, Consent Mode, JSON-LD, Shell)
│   └── pages/               # File-based routing generating all 25 static HTML entrypoints
├── tests/                   # Node.js gate tests for Astro build & Content Collections
├── astro.config.mjs         # Astro 5 configuration + local Vercel clean-URL rewrite middleware
└── vercel.json              # Edge security headers, cleanUrls, redirects, and rewrites
```

## 3. Infrastructure & Hosting
- **Edge Network:** Hosted on Vercel with automatic SSL, HTTP/2, and global edge caching of Astro's `dist/` output.
- **Minified Delivery:** Production CSS served via `/style.min.css`.
- **Security Envelope:** Guarded by Content Security Policy (CSP), HSTS, and frame protection headers configured in `vercel.json` and `public/.htaccess`.

## 4. Automated Quality & Regression Testing
- **Gate Tests (<2s):** `npm test` (validates `/api/contact` security + Astro build output & schema integrity) and `python execution/test_brand_links.py`.
- **SEO & Brand Evals:** `python execution/eval_brand_seo.py` and `python execution/comprehensive_audit.py` running against `dist/`.
- **CI Pipelines:** Enforced via GitHub Actions (`.github/workflows/ci.yml`) on every Pull Request and push.
