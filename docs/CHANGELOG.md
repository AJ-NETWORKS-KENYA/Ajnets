# AJNETWORKS — Change Log

All notable changes to the AJNETWORKS platform will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-07-19

### Added
- Created GitHub Actions CI workflow (`.github/workflows/ci.yml`) for automated gate testing and SEO evaluation on PRs and pushes.
- Established official 6-document documentation suite under `docs/` (`PRD.md`, `TRD.md`, `APP_FLOW.md`, `UI_UX.md`, `ARCHITECTURE.md`, `CHANGELOG.md`).
- Added asset minification script `execution/build_minified_assets.py` producing `style.min.css`.
- Added Vercel serverless contact API handler `api/contact.js`.
- Configured security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options) in `vercel.json` and `.htaccess`.

### Changed
- Standardized all social links to official company handles (`Facebook`, `LinkedIn`, `YouTube`, `Pinterest`).
- Unified JSON-LD structured data (`Organization`, `WebSite`, `BreadcrumbList`) across all 21 HTML pages.
- Updated core HTML templates to reference `style.min.css` in production.

## [1.0.0] - 2026-05-19
- Initial release of AJNETWORKS enterprise platform site.
