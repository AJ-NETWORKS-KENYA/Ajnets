# Original User Request

## Initial Request — 2026-08-15T22:35:17Z

This is a single self-contained set of fixes; keep it small and focused.
Implement the "Quick Wins" identified in the AJNETWORKS SEO & Performance Audit Remediation Roadmap.

Working directory: C:\My Web Sites\ajnets
Integrity mode: development

## Requirements

### R1. Meta Tags
Add unique meta titles and descriptions to all main HTML pages (e.g., index, services, case studies, blog, about, contact, FAQ) according to the SEO Action Plan. Do not use generic or duplicate tags.

### R2. Form Fix
Fix the contact form validation on the Contact page (`company/book-consultation.html`). Hide error text on load, and ensure the region dropdown is populated and functional.

### R3. Image Optimization
Implement `loading="lazy"` on all non-critical (below-the-fold) images and add descriptive `alt` attributes to all images across the site.

### R4. Sitemap and Robots
Verify and update (or create) the `robots.txt` and `sitemap.xml` to ensure they are properly formatted and accessible.

## Verification Resources
- Use the `regression-audit` skill (`C:\Users\lenovo\.gemini\config\skills\regression-audit\SKILL.md`) for guidance on running local audits.

## Acceptance Criteria

### Static Verification
- [ ] `grep` confirms all `.html` files have exactly one `<title>` and `<meta name="description">` tag, and they are unique per page.
- [ ] `grep` confirms all `<img>` tags below the fold have `loading="lazy"` and `alt` attributes.
- [ ] `robots.txt` and `sitemap.xml` exist in the root directory and are valid.

### Visual & Performance Verification
- [ ] The `browser` subagent is invoked to navigate to the local contact page and confirms that validation error messages are hidden on initial load.
- [ ] The `browser` subagent confirms the region dropdown has selectable options.
- [ ] The `regression-audit` skill is executed, running `lighthouse` or equivalent performance tools on the local dev server to capture performance, SEO, and Core Web Vitals, confirming no regressions.

## Follow-up — 2026-08-16T13:02:04Z

# Teamwork Project Prompt — Draft

> Status: Step 1 — Eliciting project idea
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: Full standard team

Comprehensive internal audit of AJNETWORKS' digital presence, covering business, technical, UX, UI, security, performance, SEO, credibility, and strategic positioning.

Working directory: C:/My Web Sites/ajnets/teamwork_audit

## Requirements

### R1. Perform a full crawl and inspection of https://ajnetworks.co/, documenting technical, content, and UX attributes per the provided audit rubric.

### R2. Produce a structured report with findings categorized, prioritized, and actionable, adhering to the specified format.

## Acceptance Criteria

### Acceptance Criteria
- [ ] All pages are crawled and data extracted without errors.
- [ ] Report contains at least 30 distinct findings with proper evidence and classifications.
- [ ] Findings are organized into the required sections and include priority matrix.
- [ ] The report meets the executive summary length constraints.

---

*Next: when approved → delegate via invoke_subagent (see Delegation Protocol)*
