# AJNETWORKS — Enterprise Technology Consultancy Platform

> **Domain:** [https://ajnetworks.co](https://ajnetworks.co)  
> **Architecture:** Astro SSG (`output: 'static'`) + Zod Content Collections + Vercel Serverless API  

---

## 1. Overview

AJNETWORKS is an enterprise technology consultancy headquartered in Nairobi, Kenya with regional operations in Rwanda. This repository contains the production web platform delivering strategic advisory, custom software engineering, cybersecurity assurance, IT infrastructure, and technical SEO practice areas, client case studies, and engineering insights.

---

## 2. Project Architecture

```
ajnets/
├── api/                     # Vercel Serverless Functions (contact.js + contact.test.js)
├── docs/                    # 6-Document Gate (PRD, TRD, APP_FLOW, UI_UX, BACKEND_SCHEMA, IMPLEMENTATION_PLAN, ARCHITECTURE, DECISIONS, CHANGELOG)
├── execution/               # Deterministic Python Gate Tests, SEO Evals & Migration Tooling
├── public/                  # Static assets copied 1:1 to dist/ (css/, js/, images/, fonts/, style.min.css, robots.txt, sitemap.xml)
├── services/cms/            # Sanity Studio Headless CMS schemas
├── src/
│   ├── components/          # Shared Astro UI components (Header, Footer, CookieConsent, RwandaBanner)
│   ├── content/             # Zod-validated Content Collections (caseStudies, services, company, insights, system)
│   ├── content.config.ts    # Content Layer Zod Schema Definitions
│   ├── layouts/             # BaseLayout.astro (Canonical SEO <head>, Consent Mode v2, JSON-LD, Layout Shell)
│   └── pages/               # Static route generators outputting 25 HTML entrypoints
├── tests/                   # Node.js gate tests (astro-build.test.js)
├── astro.config.mjs         # Astro configuration + local Vercel clean-URL rewrite middleware
└── vercel.json              # Edge security headers (CSP, HSTS), cleanUrls, redirects, and rewrites
```

---

## 3. Quick Start & Commands

### Prerequisites
- **Node.js:** `>= 22.0.0`
- **Python:** `>= 3.11` (with `beautifulsoup4` for HTML audits)

### Development & Build
```bash
# Install dependencies
npm install

# Start Astro development server on http://localhost:3000 (with Vercel clean-URL rewrites)
npm run dev

# Build static production output to dist/
npm run build

# Preview production build locally on http://localhost:3000
npm run preview
```

### Verification (Gate Tests & Evals)
```bash
# Run Node.js Gate Tests (Contact API security + Astro Content Collections & dist/ verification)
npm test

# Run Python Gate Tests (Social links, Schema.org JSON-LD sameAs, canonical domains, robots & sitemap)
python execution/test_brand_links.py

# Run SEO & Brand Alignment Evaluation (100% threshold required)
python execution/eval_brand_seo.py

# Run Comprehensive HTML & Metadata Audit (Duplicate titles/descriptions, image alt attributes)
npm run audit
```

