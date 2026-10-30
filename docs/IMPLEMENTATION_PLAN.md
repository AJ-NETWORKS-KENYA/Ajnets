# AJNETWORKS — Implementation Plan (IMPLEMENTATION_PLAN.md)

> **Version:** 2.0.0  
> **Maintainer:** AJNETWORKS Engineering  
> **Target Branch:** `feature/astro-migration` (cut from `dev`)  

---

## 1. Objective & Measurable Outcomes

Migrate the `ajnets` platform from 25 standalone raw HTML files (maintained via 70+ ad-hoc Python DOM-patching scripts) to **Astro 5+ Static Site Generation (SSG)** with **Zod-validated Content Collections** and **1:1 visual and SEO parity**.

### Measurable Outcomes
1. **Template Consolidation:** Reduce 25 duplicated `<head>`, `<header>`, `<footer>`, and `<div id="cookie-consent-banner">` definitions down to **1 canonical `<BaseLayout.astro>`** and shared partial components (`Header.astro`, `Footer.astro`, `CookieConsent.astro`, `RwandaBanner.astro`).
2. **Typed Content Collections:** Migrate all Case Studies (`portfolio/case-study-*.html`), Practice Areas (`services/*.html`), and Insights (`insights/*.html`) into Zod-validated Astro Content Collections (`src/content/`).
3. **Zero Client Framework Bloat:** Ship **0 KB** of additional client-side framework JavaScript (`output: 'static'`).
4. **100% Gate & Eval Compliance:**
   - `npm test` (`api/contact.test.js` + Astro build & schema verification tests) passes in `<2s`.
   - `python execution/test_brand_links.py` passes with `0 errors` across all 25 generated HTML pages in `dist/`.
   - `python execution/eval_brand_seo.py` achieves a `100.0%` compliance score.
   - `python execution/comprehensive_audit.py` reports `0` duplicate titles, `0` duplicate descriptions, `0` missing image `alt` attributes, and `0` corrupt characters.
5. **100% Visual Parity:** Verified across Mobile, Tablet, and Desktop viewports via browser tooling.

---

## 2. Ordered Build Phases

### Phase 1: 6-Document Gate & Architecture Alignment
- [x] Create `feature/astro-migration` branch from `dev`.
- [x] Author `docs/BACKEND_SCHEMA.md`, `docs/IMPLEMENTATION_PLAN.md`, and `docs/DECISIONS.md`.
- [x] Update `docs/PRD.md`, `docs/TRD.md`, `docs/APP_FLOW.md`, `docs/UI_UX.md`, and `docs/ARCHITECTURE.md`.

### Phase 2: Astro 5+ Scaffolding & Public Asset Organization
- [x] Update `package.json` with `astro` (latest stable v5+) and scripts (`dev`, `build`, `preview`, `test`, `audit`).
- [x] Configure `astro.config.mjs` with `output: 'static'`, `build: { format: 'file' }`, `site: 'https://ajnetworks.co'`, and a Vite dev/preview middleware plugin that mirrors `vercel.json` clean-URL rewrites locally.
- [x] Move static runtime assets (`css/`, `js/`, `images/`, `fonts/`, `style.css`, `style.min.css`, `robots.txt`, `sitemap.xml`, `.htaccess`) into `public/` so Astro copies them cleanly to `dist/` at build time.
- [x] Keep `api/contact.js` and `api/contact.test.js` intact at root `/api` for Vercel Serverless Functions.

### Phase 3: Shared Layouts, Components & Content Collections
- [x] Create `src/layouts/BaseLayout.astro` encapsulating `<head>` metadata, favicons, CSS imports, Google Consent Mode v2, GA4 tag, guarded LinkedIn Insight tag, Canonical & Open Graph tags, Twitter cards, Schema.org `Organization` JSON-LD, page-specific JSON-LD injection, `<Header />`, `<Footer />`, and `<CookieConsent />`.
- [x] Create `src/components/Header.astro`, `src/components/Footer.astro`, `src/components/CookieConsent.astro`, and `src/components/RwandaBanner.astro`.
- [x] Create `src/content.config.ts` defining Zod schemas for `caseStudies`, `services`, `companyPages`, and `insights`.
- [x] Deterministically extract all 25 existing HTML pages into Astro Content Collections and `src/pages/` routes (`src/pages/index.astro`, `src/pages/404.astro`, `src/pages/company/[slug].astro`, `src/pages/services/[slug].astro`, `src/pages/portfolio/[slug].astro`, `src/pages/insights/[slug].astro`, `src/pages/elements/elements.astro`), removing the legacy root `.html` files so `src/` is the single source of truth.

### Phase 4: Gate Tests, SEO Evals & CI Pipeline Update
- [x] Update `execution/test_brand_links.py`, `execution/eval_brand_seo.py`, and `execution/comprehensive_audit.py` to automatically target `dist/` (the Astro build output) when present.
- [x] Add deterministic gate tests (`tests/astro-build.test.js`) verifying Astro build output, Content Collection integrity, and clean URL routing.
- [x] Update `.github/workflows/ci.yml` to run `npm ci`, `npm run build`, `npm test`, `python execution/test_brand_links.py`, and `python execution/eval_brand_seo.py`.

### Phase 5: Visual Browser Verification & Final Audit
- [x] Start the Astro server and verify Desktop, Tablet, and Mobile viewports via `chrome-devtools-mcp`.
- [x] Update `docs/CHANGELOG.md` and `README.md`, run secret scan checks, and commit cleanly using Conventional Commits.
