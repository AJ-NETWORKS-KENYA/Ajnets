# AJNETWORKS — Data Architecture & Content Schema (BACKEND_SCHEMA.md)

> **Version:** 2.0.0  
> **Maintainer:** AJNETWORKS Engineering  

---

## 1. Overview

AJNETWORKS operates a hybrid static-first data architecture:
1. **Astro Content Collections (`src/content/`):** Build-time, Git-backed, Zod-validated structured content for **Case Studies (`caseStudies`)**, **Practice Areas (`services`)**, and **Technical Insights (`insights`)**.
2. **Serverless Lead Intake API (`api/contact.js`):** Stateless Vercel Serverless Function enforcing strict schema validation, honeypot bot mitigation, in-memory IP rate limiting, and regional SMTP routing (Kenya HQ & Rwanda operations).
3. **Headless CMS Schema Parity (`services/cms/`):** Sanity Studio schema definitions mirroring Astro's Content Collections for future editorial webhook workflows.

---

## 2. Astro Content Collections (`src/content.config.ts`)

All collections are strictly validated at build time using `astro:content` and `zod`. Any schema violation fails `astro build` deterministically.

### 2.1 `caseStudies` Collection (`src/content/caseStudies/*.json`)
Represents client delivery engagements rendered at `/portfolio/[slug]` (and rewritten cleanly at `/[slug]`).

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `slug` | `string` | Required, `^case-study-[a-z0-9-]+$` | URL slug (e.g., `case-study-bada`) |
| `title` | `string` | Required, max 80 chars | SEO `<title>` tag |
| `description` | `string` | Required, 50–200 chars | Meta & Open Graph description |
| `keywords` | `string` | Required | Meta keywords string |
| `canonicalPath` | `string` | Required | Clean canonical path (e.g., `/case-study-bada`) |
| `client` | `string` | Required | Client display name |
| `industry` | `string` | Required | Industry vertical |
| `technologies` | `string` | Required | Sidebar technology summary |
| `timeline` | `string` | Required | Delivery duration (e.g., `4 - 8 Weeks`) |
| `heroImage` | `string` | Required | Background image path for `.page-hero` |
| `heroSummary` | `string` | Required | Subtitle summary in `.page-hero` |
| `badges` | `string[]` | Required, min 1 | Tech badges displayed in the hero |
| `bodyHtml` | `string` | Required | Structured HTML body for main column & sidebar |
| `extraJsonLd` | `array` | Optional | Additional Schema.org JSON-LD blocks (e.g., `Article`) |

### 2.2 `services` Collection (`src/content/services/*.json`)
Represents core consulting and engineering practice pages rendered at `/services/[slug]` (and rewritten at `/[slug]`).

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `slug` | `string` | Required | URL slug (e.g., `cybersecurity`, `software-engineering`) |
| `title` | `string` | Required | SEO `<title>` tag |
| `description` | `string` | Required | Meta & Open Graph description |
| `keywords` | `string` | Required | Meta keywords string |
| `canonicalPath` | `string` | Required | Clean canonical path (e.g., `/cybersecurity`) |
| `breadcrumbTitle` | `string` | Required | Current breadcrumb label |
| `heroTitle` | `string` | Required | `<h1>` heading in `.page-hero` |
| `heroSubtitle` | `string` | Required | Subtitle text in `.page-hero` |
| `bodyHtml` | `string` | Required | Structured HTML body for the practice page |
| `extraJsonLd` | `array` | Optional | Additional Schema.org JSON-LD objects (e.g., `BreadcrumbList`, `Service`) |

### 2.3 `insights` Collection (`src/content/insights/*.json`)
Represents thought leadership articles and the insights hub rendered at `/insights/[slug]`.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `slug` | `string` | Required | URL slug (`insights`, `post`) |
| `title` | `string` | Required | SEO `<title>` tag |
| `description` | `string` | Required | Meta & Open Graph description |
| `keywords` | `string` | Required | Meta keywords string |
| `canonicalPath` | `string` | Required | Clean canonical path (`/insights`, `/post`) |
| `ogType` | `enum` | `'website' \| 'article'` | Open Graph resource type |
| `bodyHtml` | `string` | Required | Structured HTML content |
| `extraJsonLd` | `array` | Optional | Additional Schema.org JSON-LD (`Article`, `BreadcrumbList`) |

---

## 3. Serverless Contact API Contract (`POST /api/contact`)

### Request Payload (`application/json`)
```json
{
  "name": "Jane Mwangi",
  "email": "jane@enterprise.co.ke",
  "phone": "+254700000000",
  "region": "Kenya",
  "service": "Cybersecurity & Assurance",
  "message": "We need an infrastructure security audit.",
  "bot_field": ""
}
```

### Validation & Security Rules
- **CORS Policy:** Strictly restricted to `https://ajnetworks.co`.
- **Method Enforcement:** `POST` and `OPTIONS` only (`405 Method Not Allowed` otherwise).
- **Honeypot Trap:** If `bot_field` is non-empty, returns silent `200 OK` without dispatching email.
- **Rate Limiting:** Max 5 requests per 60 seconds per client IP (`429 Too Many Requests`).
- **Required Fields:** `name`, `email` (RFC-compliant regex), `region`, `message` (`400 Bad Request` on missing/invalid fields).
- **Regional SMTP Routing:** Routes to `RWANDA_*` SMTP credentials when `region === "Rwanda"`, defaulting to primary `SMTP_*` credentials otherwise.

