# AJNETWORKS — Engineering Decision Log (DECISIONS.md)

> **Version:** 1.0.0  
> **Maintainer:** AJNETWORKS Architecture Team  

---

## ADR-001: Migrate Static HTML Codebase to Astro 5+ with Content Collections

- **Date:** 2026-10-30
- **Status:** Accepted
- **Deciders:** AJ, AJNETWORKS Engineering

### Context
The `ajnets` web platform consisted of 25 standalone `.html` files across root, `company/`, `services/`, `portfolio/`, `insights/`, and `elements/`. Because raw HTML lacks layout inheritance, shared components, or build-time content schemas, every global change (navigation updates, footer links, Consent Mode v2, JSON-LD schema injection, asset path fixes) required writing and executing ad-hoc Python DOM-patching scripts in `execution/` (accumulating 70+ scripts). Furthermore, adding new Case Studies or Insights required cloning full 450–900 line HTML files.

### Decision
Migrate the frontend build architecture to **Astro 5+ (`output: 'static'`, `build.format: 'file'`)** with **Zod-validated Astro Content Collections (`src/content/`)**:
1. Extract the global `<head>`, `<header>`, `<footer>`, Rwanda geolocation banner, and Cookie Consent UI into reusable Astro components (`BaseLayout.astro`, `Header.astro`, `Footer.astro`, `CookieConsent.astro`, `RwandaBanner.astro`).
2. Model `services`, `portfolio` (case studies), `company`, and `insights` pages using typed Content Collections validated at build time with Zod.
3. Preserve 1:1 HTML/CSS output and URL structure (`dist/`) so all existing CSS (`style.min.css`), client scripts, Vercel clean URL rewrites (`vercel.json`), and `/api/contact.js` serverless functions work without regression.

### Alternatives Considered
1. **Keep Raw HTML + Python Codemods:** Zero build step, but high maintenance friction and error-prone regex/BeautifulSoup mutations across 25 files.
2. **Next.js (App Router):** Heavy React client runtime (~90KB+ JS) unnecessary for a content-driven B2B consultancy platform; violates the "Ship Less JavaScript" and "Vanilla by Default" principles when interactive React state is not required.
3. **11ty (Eleventy):** Capable static generator, but lacks Astro's native TypeScript/Zod Content Collections, component scoping, and modern Vite pipeline.

### Consequences & Tradeoffs
- **Positive:** Single source of truth for layouts, navigation, footer, and SEO `<head>` tags; compile-time Zod validation for all content; 0 KB client framework JS shipped; 100% compatibility with Vercel static hosting and existing Python SEO/link gate tests.
- **Negative / Tradeoff:** Introduces a fast Node.js build step (`npm run build` / `astro build`, ~2 seconds) prior to deployment and HTML gate testing.
