# AJNETWORKS — Design System & File Reference

> **Version:** 1.0  
> **Maintained by:** AJNETWORKS Engineering  
> **Last Updated:** 2026-05-19  
> **Scope:** Website design system, CSS conventions, file structure, and component catalogue for `ajnets` — the official AJNETWORKS corporate site.

---

## 1. Brand Identity

| Property      | Value                                           |
| ------------- | ----------------------------------------------- |
| **Full Name** | AJNETWORKS                                      |
| **Tagline**   | Engineering technology that accelerates business growth |
| **Domain**    | ajnetworks.co                          |
| **Region**    | East Africa (Kenya HQ · Rwanda operations)      |
| **Contact**   | hello@ajnetworks.co · +254 758 238 617 |
| **Hours**     | Mon – Sat: 8:00 am – 7:00 pm                    |

### Logo Guidelines (Brand Book Specs)

| Property | Standard | Rule |
| --- | --- | --- |
| **Logo Clear Space** | `50px` | Always maintain 50px padding around logo edges for legibility. |
| **Minimum Width** | `128px` (`1.33"`) | Do not render smaller than 128px width to preserve detail. |

### Logo Files

| File                          | Usage                                |
| ----------------------------- | ------------------------------------ |
| `images/logo.svg`             | Primary logo (header, light BG)      |
| `images/logo-light.svg`       | White/reverse logo (dark BG, footer) |
| `images/logo-transparent.svg` | Transparent background variant       |
| `images/favicon.svg`          | Browser favicon (SVG)                |
| `images/favicon-96x96.png`    | 96×96 PNG favicon                    |
| `images/favicon.ico`          | Legacy ICO favicon                   |
| `images/apple-touch-icon.png` | 180×180 Apple touch icon             |
| `images/og-home.jpg`          | Open Graph social share image        |

---

## 2. Color Palette (Official Brand Book)

### Core Brand Colors

| Token / Color Name | Hex Code | RGB | HSL | Usage |
| --- | --- | --- | --- | --- |
| **Blackberry Purple** | `#1E2132` | `30, 33, 50` | `231, 25%, 16%` | Deep background, dark navy sections |
| **Pure White** | `#FFFFFF` | `255, 255, 255` | `0, 0%, 100%` | Primary background, light buttons, text on dark |
| **Maldives Teal** | `#43D9AD` | `67, 217, 173` | `162, 66%, 56%` | Success badges, teal accents, highlight elements |
| **Capri Blue** | `#00A3FF` | `0, 163, 255` | `202, 100%, 50%` | Primary buttons, link hover states, active accents |
| **Twilight Blue** | `#2B3B85` | `43, 59, 133` | `229, 51%, 35%` | Top bar background, secondary buttons, banners |

### Regional Banner Colors

| Region | Background | Accent Text |
| ------ | ---------- | ----------- |
| Rwanda | `#2B3B85` (`Twilight Blue`) | `#FF9900` |

---

## 2.1 Brand Voice & Aesthetics

* **Values:** Strategic Clarity, Engineering Excellence, Security-first Delivery, Business Impact, Intentionality
* **Aesthetic:** Sleek, modern, corporate, strategic, data-driven, sophisticated
* **Tone of Voice:** Professional, strategic, authoritative, ambitious, outcome-driven

---

## 3. Typography

### Font Stack

| Role            | Family                          | Import Source                                  |
| --------------- | ------------------------------- | ---------------------------------------------- |
| **Headings**    | `Montserrat`                    | Google Fonts                                   |
| **Body / UI**   | `Nunito Sans`                   | Google Fonts                                   |
| **Subheadings** | `Nunito`                        | Google Fonts                                   |
| **Alternate**   | `Poppins`                       | Google Fonts                                   |
| **Display**     | `Inter`                         | Google Fonts                                   |
| **Accent**      | `Sora`, `Epilogue`, `Gothic A1` | Google Fonts                                   |
| **Icons**       | `Flaticon`, `Font Awesome 5`    | Local CSS (flaticon.css, font-awesome.min.css) |

### Heading Scale

```css
h1 {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.2;
}
h2 {
  font-size: 36px;
  font-weight: 800;
}
h3 {
  font-size: 30px;
  font-weight: 800;
}
h4 {
  font-size: 24px;
  font-weight: 700;
}
h5 {
  font-size: 20px;
  font-weight: 700;
}
h6 {
  font-size: 18px;
  font-weight: 700;
}
```

### Hero Overrides (inline styles — `index.html`)

```css
h1 {
  font-size: 60px;
  font-weight: 900;
  font-family: "Montserrat";
}
.hero-eyebrow {
  font-size: 20px;
  font-weight: 600;
  text-transform: uppercase;
  font-family: "Nunito Sans";
}
```

### Body Text

```css
body {
  font-family: "Nunito Sans", sans-serif;
  font-size: 16px;
  line-height: 1.875;
  color: #6d6d6d;
}
p {
  margin: 0 0 20px;
}
.lead {
  font-size: 18px;
}
```

### Font-weight Utilities

| Class      | Weight |
| ---------- | ------ |
| `.bolder`  | 900    |
| `.bold`    | 700    |
| `.medium`  | 500    |
| `.normal`  | 400    |
| `.lighter` | 300    |

---

## 4. Spacing & Layout

### Section Padding

| Class                 | Value                   |
| --------------------- | ----------------------- |
| `.section-padd`       | `padding: 110px 0`      |
| `.section-padd-bot`   | `padding-bottom: 110px` |
| `.section-padd-top`   | `padding-top: 110px`    |
| `.section-padd-top70` | `padding-top: 70px`     |
| `.padding-half`       | half-standard padding   |

### Grid System

The site uses **Bootstrap 4** grid (`css/bootstrap.min.css`).

- `container` → centered fixed-width
- `container-fluid` → full-width (used in header)
- Standard 12-column `col-*` grid
- Breakpoints: xs, sm, md, lg, xl

### Box-shadow Utility

```css
.b-shadow {
  box-shadow: 15px 15px 38px 0px rgba(0, 0, 0, 0.1);
}
```

---

## 5. Button System

All buttons use the base `.octf-btn` class with variant modifiers.

### Variants

| Class                 | BG        | Text      | Hover BG  |
| --------------------- | --------- | --------- | --------- |
| `.octf-btn` (default) | `#43baff` | `#fff`    | `#7141b1` |
| `.octf-btn-second`    | `#7141b1` | `#fff`    | `#43baff` |
| `.octf-btn-light`     | `#fff`    | `#1b1d21` | `#1b1d21` |
| `.octf-btn-dark`      | `#1b1d21` | `#fff`    | `#fff`    |
| `.octf-btn-third`     | Accent    | `#fff`    | Custom    |

### Properties

```css
.octf-btn {
  font-size: 14px;
  padding: 14px 30px;
  text-transform: uppercase;
  font-weight: bold;
  border-radius: 0; /* flat by default */
  transition: all 0.3s linear;
}
```

### Hero Button Override

```css
/* Used on homepage CTA */
.octf-btn.btn-large {
  padding: 15px 35px;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 700;
}
```

### Text Link Button

```css
.btn-details {
  font-size: 14px;
  font-weight: bold;
  color: #43baff;
}
```

---

## 6. Navigation

### Desktop Header Structure

```
.header-topbar          — dark navy strip: email, hours, social icons
.octf-main-header       — main menu row: logo + nav + CTA
  .site-logo            — images/logo.svg
  .main-navigation      — ul.menu with sub-menus
  .octf-btn-cta         — search icon, phone, "Request Consultation" button
```

### Main Navigation Pages

| Label                           | URL                         |
| ------------------------------- | --------------------------- |
| Home                            | `./`                        |
| Who We Are                      | `about-us.html`             |
| Services                        | `services.html`             |
| → Technology & Digital Strategy | `technology-strategy.html`  |
| → Software Engineering          | `software-engineering.html` |
| → Cybersecurity & Assurance     | `cybersecurity.html`        |
| → Networking & Infrastructure   | `networking.html`           |
| → Performance & SEO             | `performance-seo.html`      |
| Client Success                  | `client-success.html`       |
| Insights                        | `insights.html`             |
| Book Consultation               | `book-consultation.html`    |

### Mobile Header

```
.header_mobile          — shown on small screens
  .mobile_logo          — images/logo.svg
  #mmenu_toggle         — hamburger button (aria-expanded)
  .mobile_mainmenu      — mirrors desktop nav
```

### Header CSS Classes (sticky behaviour)

```
.site-header.header-style-2.header-fullwidth.sticky-header.header-static
```

---

## 7. Components

### 7.1 Section Heading (`.ot-heading`)

```html
<div class="ot-heading">
  <span>// about company</span>
  <h2 class="main-heading">
    Your Technology <br />
    Consulting Partner
  </h2>
</div>
```

- `<span>` eyebrow uses `//` prefix convention (e.g. `// strategic technology consulting`)
- `<h2>` is the section title

### 7.2 Client Logo Carousel

Uses **Owl Carousel** (`css/owl.carousel.min.css`, `css/owl.theme.css`).

```html
<div class="owl-carousel owl-theme home-client-carousel">
  <div class="partners-slide">
    <a href="..." class="client-logo">
      <figure class="partners-slide-inner">
        <img
          class="partners-slide-image"
          src="images/client-logos/..."
          alt="Client Name"
        />
      </figure>
    </a>
  </div>
</div>
```

**Actual client logos in use:**

| Client                  | File                                                                  |
| ----------------------- | --------------------------------------------------------------------- |
| Rotaract Club of Nyali  | `images/client-logos/Rotaract Club of Nyali Logo(Cranberry)_EN21.png` |
| Bada Language Institute | `images/client-logos/BLI logoo.png`                                   |
| SGSS Mombasa            | `images/client-logos/sgss-mombasa-logo.png`                           |
| SGSS Medical Fund       | `images/client-logos/sgss-medical-fund-logo.png`                      |

### 7.3 Hero Section (Static)

Homepage uses a static hero with inline styles (no JS slider):

```html
<div
  class="static-hero"
  style="background: url('images/slider/slide1-home1.webp') no-repeat center/cover; padding: 150px 0 100px;"
>
  <!-- 60% dark overlay -->
  <div style="position:absolute; inset:0; background: rgba(0,0,0,0.6);"></div>
  <div class="container" style="position:relative; z-index:2;">
    <div class="col-lg-8">
      <!-- eyebrow, h1, p, CTA button -->
    </div>
  </div>
</div>
```

Hero image: `images/slider/slide1-home1.webp` (preloaded via `<link rel="preload">`)

### 7.4 Regional Geo Banner

IP-based banner shown to Rwandan visitors only:

```html
<div
  id="rwanda-banner"
  style="display:none; background:#2b3b85; color:white; text-align:center; padding:10px;"
>
  🇷🇼 Karibu! We now have local operations in Rwanda.
  <a href="book-consultation.html" style="color:#ff9900;"
    >Contact our regional team today</a
  >.
</div>
```

Detection script uses `https://ipapi.co/json/` and triggers on `country_code === "RW"`.

### 7.5 Cookie Consent Banner

- Script: `js/cookie-consent.js` (deferred)
- Styles: `css/cookie-consent.css`
- Analytics: Google Tag Manager (`G-2E6LLT0TT7`) with Consent Mode v2 (deny-by-default)

### 7.6 Footer Gallery

Images: `images/ft-gallery-1.jpg` → `ft-gallery-6.jpg`

---

## 8. Form System

All input elements share:

```css
background: #f6f6f6;
border: none;
padding: 10px 20px;
color: #b5b5b5; /* placeholder */
```

Focus state: `color: #6d6d6d`

Contact form functionality:

- Styles: `css/contact-form.css`
- Serverless handler: `api/contact.js` (Vercel)

---

## 9. CSS Architecture

### Stylesheet Loading Order (`<head>`)

```html
1. css/bootstrap.min.css — Grid (Bootstrap 4) 2. css/font-awesome.min.css — Icon
set 3. css/flaticon.css — Custom icon font 4. css/owl.carousel.min.css —
Carousel core 5. css/owl.theme.css — Carousel theme 6. css/magnific-popup.css —
Lightbox 7. style.css — ⭐ Master stylesheet (327 KB) 8. css/logo-ajnetworks.css
— Logo-specific overrides 9. css/cookie-consent.css — Cookie banner 10.
css/trust-strip.css — Trust logos strip
```

### `style.css` Internal Sections (Table of Contents)

```
# Normalize          (lines 12–369)   — normalize.css v8, Google Font imports
# Typography         (370–695)        — headings, body, utilities
# Elements           (696–798)        — reset, lists, table, images
# Forms / Buttons    (799–974)        — .octf-btn variants, inputs
# Navigation         (952–)           — links, header topbar, menus
```

---

## 10. File System Structure

```
ajnets/                            <- project root (clean - HTML, CSS, configs only)
|
|-- [HTML Pages]
|   |-- index.html                 <- Homepage
|   |-- about-us.html              <- Company / Who We Are
|   |-- services.html              <- Services overview
|   |-- technology-strategy.html   <- Service: Technology & Digital Strategy
|   |-- software-engineering.html  <- Service: Software Engineering
|   |-- cybersecurity.html         <- Service: Cybersecurity & Assurance
|   |-- networking.html            <- Service: Networking & Infrastructure
|   |-- performance-seo.html       <- Service: Performance & SEO
|   |-- mobile-development.html    <- Service: Mobile Development
|   |-- web-development.html       <- Service: Web Development
|   |-- solutions.html             <- Solutions overview
|   |-- client-success.html        <- Case studies / portfolio landing
|   |-- case-study-*.html          <- Individual case study pages (7 files)
|   |-- portfolio-details-*.html   <- Portfolio detail pages
|   |-- book-consultation.html     <- Lead capture / contact form
|   |-- insights.html              <- Blog / insights landing
|   |-- post.html                  <- Blog post template
|   |-- faq.html                   <- FAQ page
|   -- elements.html               <- UI component reference / sandbox
|
|-- style.css                      <- Master stylesheet (327 KB)
|
|-- css/                           <- Vendor & custom CSS
|   |-- bootstrap.min.css          <- Grid system (Bootstrap 4)
|   |-- font-awesome.min.css       <- Icon set
|   |-- flaticon.css               <- Custom icon font
|   |-- owl.carousel.min.css       <- Carousel core
|   |-- owl.theme.css              <- Carousel theme
|   |-- magnific-popup.css         <- Lightbox
|   |-- animate.css                <- CSS animations
|   |-- contact-form.css           <- Form styles
|   |-- cookie-consent.css         <- Cookie banner
|   |-- logo-ajnetworks.css        <- Logo-specific overrides
|   |-- trust-strip.css            <- Trust logos strip
|   |-- home15.css / home16.css    <- Section-specific overrides
|   |-- royal-preload.css          <- Preloader
|   -- woocommerce.css             <- WooCommerce base styles
|
|-- js/                            <- JavaScript
|   |-- cookie-consent.js          <- Cookie banner logic (deferred)
|   -- [vendor JS files]           <- jQuery, Owl, plugins
|
|-- plugins/                       <- jQuery & carousel plugin bundles
|-- fonts/                         <- Self-hosted icon fonts (Flaticon glyphs)
|
|-- images/                        <- All image assets
|   |-- logo.svg                   <- Primary brand mark
|   |-- logo-light.svg             <- White/reversed logo (dark BG / footer)
|   |-- logo-transparent.svg       <- Transparent background variant
|   |-- favicon.*                  <- Favicon set (svg, png, ico, webmanifest)
|   |-- slider/
|   |   -- slide1-home1.webp       <- Homepage hero (WebP, LCP-preloaded)
|   |-- client-logos/              <- Client carousel logos (4 active clients)
|   |-- projects/                  <- Portfolio / case study project images
|   |-- blog/                      <- Blog post imagery
|   -- [section images]            <- BG textures, team photos, misc assets
|
|-- api/                           <- Vercel Serverless Functions (Layer 3)
|   -- contact.js                  <- Contact form handler with region routing
|
|-- execution/                     <- LAYER 3: Deterministic maintenance scripts
|   |-- run_audit.py               <- Runs the site audit
|   |-- print_audit.py             <- Prints audit results
|   |-- fix_audit_issues.py        <- Applies audit rule patches
|   |-- fix_lints.py               <- Lint remediation pass 1
|   |-- fix_lints2.py              <- Lint remediation pass 2
|   |-- fix_lints3.py              <- Lint remediation pass 3
|   |-- fix_navs.py                <- Navigation link fixer pass 1
|   |-- fix_navs_2.py              <- Navigation link fixer pass 2
|   |-- apply_p3_fixes.py          <- Priority-3 audit fixes
|   |-- apply_priority_fixes.py    <- General audit fixes
|   |-- refactor.py                <- General page refactor
|   |-- update_index.py            <- Updates index.html
|   |-- update_emails.py           <- Updates email addresses sitewide
|   |-- optimize_hero.py           <- Hero image optimizer
|   |-- append_modal_css.py        <- Appends modal CSS to pages
|   |-- inject_case_studies.py     <- Injects case study cards
|   |-- inject_crappo_card.py      <- Injects Crappo client card
|   |-- inject_foodex.py           <- Injects Foodex content
|   |-- inject_project_images.py   <- Injects project images
|   |-- inject_service_links.py    <- Injects service links
|   |-- create_case_studies.py     <- Generates case study page stubs
|   |-- create_crappo.py           <- Crappo case study builder
|   -- rebuild_case_studies.py     <- Full case study rebuild
|
|-- .agent/                        <- LAYER 2: Agent orchestration config
|   -- skills/                     <- Workspace-scoped Skill packages
|       -- [skill-name]/           <- Each: SKILL.md + scripts/ + references/
|
|-- .tmp/                          <- Intermediate files (gitignored, regeneratable)
|   |-- _audit_results.json        <- Last audit run output
|   -- services-backup.html        <- Archived backup page
|
|-- vercel.json                    <- Vercel deployment config (routes, headers)
|-- package.json                   <- Node.js manifest
|-- package-lock.json              <- Lockfile
|-- robots.txt                     <- SEO crawl rules
|-- sitemap.xml                    <- XML sitemap
|-- .htaccess                      <- Apache redirect rules (legacy)
|-- .env / .env.local              <- Environment variables & API keys (gitignored)
|-- credentials.json / token.json  <- OAuth credentials (gitignored)
|-- LICENSE                        <- Project licence
|-- .renderignore                  <- Render.com deploy ignore rules
|-- Gemini.md                      <- AI agent instructions (3-layer architecture)
|-- design.md                      <- This document - design system reference
-- data.md                         <- Structured content / copy reference
```

## 11. SEO & Meta Conventions

Every page must include:

```html
<!-- Basics -->
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="description" content="Page-specific description (120–160 chars)" />
<meta name="keywords" content="..." />
<title>Page Title — AJNETWORKS</title>

<!-- Canonical -->
<link rel="canonical" href="https://ajnetworks.co/page.html" />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:url" content="..." />
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta
  property="og:image"
  content="https://ajnetworks.co/images/og-home.jpg"
/>
<meta property="og:site_name" content="AJNETWORKS" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="..." />
<meta name="twitter:description" content="..." />

<!-- Favicon set -->
<link rel="icon" type="image/svg+xml" href="images/favicon.svg" />
<link
  rel="icon"
  type="image/png"
  sizes="96x96"
  href="images/favicon-96x96.png"
/>
<link
  rel="apple-touch-icon"
  sizes="180x180"
  href="images/apple-touch-icon.png"
/>
<link rel="manifest" href="images/site.webmanifest" />
```

### JSON-LD Schema (Homepage)

Three entities declared in `<script type="application/ld+json">`:

1. `Organization` — name, url, logo, founder (Abraham John), contactPoint
2. `LocalBusiness` — name, address (Nairobi, Kenya)
3. `WebSite` — name, alternateName, url

---

## 12. Analytics & Tracking

| Tool                 | ID / Status                   | Notes                            |
| -------------------- | ----------------------------- | -------------------------------- |
| Google Analytics 4   | `G-2E6LLT0TT7`                | Consent Mode v2, deny-by-default |
| Facebook Pixel       | Domain verified               | `r5liwwbty07nhozk87d1uwkz4fyp70` |
| LinkedIn Insight Tag | `YOUR_LINKEDIN_PID` (pending) | Replace with actual Partner ID   |

---

## 13. Deployment

| Property       | Value                            |
| -------------- | -------------------------------- |
| **Platform**   | Vercel                           |
| **Dev server** | `vercel dev` (local port 3000)   |
| **Config**     | `vercel.json`                    |
| **Functions**  | `api/contact.js` — email routing |
| **Domain**     | ajnetworks.co           |

---

## 14. Accessibility Conventions

- All images **must** have descriptive `alt` attributes (empty `alt=""` only for decorative images)
- Interactive elements must have `aria-label` or visible text (buttons, icon links)
- `#site-navigation` uses semantic `<nav>` with `role` attributes
- Mobile menu toggle: `aria-expanded` managed via JS
- Search button: `aria-label="Search"`, `type="button"`
- Form labels use `<label>` with `<span class="screen-reader-text">` for hidden labels
- Color contrast: headings `#1b1d21` on `#fff` ≥ 12:1 ✓ · body `#6d6d6d` on `#fff` ≥ 4.5:1 ✓

---

## 15. Design Conventions & Rules

1. **Section eyebrows** always prefix with `//` (e.g. `// about company`)
2. **Buttons** are ALL CAPS (`text-transform: uppercase`)
3. **Hero overlays** use `rgba(0,0,0,0.6)` for readability over dark photography
4. **Transitions** are `all 0.3s linear` throughout — consistent micro-animation speed
5. **Images** must be responsive (`max-width: 100%; height: auto`)
6. **Logo** must link to `./` (homepage root)
7. **External links** require `target="_blank" rel="noopener"` for security
8. **WebP format** is preferred for hero/large images; fallback PNG/JPG for older assets
9. **Cookie consent** must fire before any analytics data is collected
10. **Regional banners** are hidden by default and revealed by geolocation JS only

---

_This document is the authoritative design reference for all AJNETWORKS web properties. Update it whenever new patterns, pages, or components are introduced._


## Social Media & Brand Links
- **Website:** https://ajnetworks.co
- **Facebook:** https://facebook.com/ajnetworks
- **LinkedIn:** https://linkedin.com/company/ajnetworks
- **YouTube:** https://www.youtube.com/@ajnets
- **Pinterest:** https://pinterest.com/ajnetworks
