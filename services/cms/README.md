# AJNETWORKS CMS Architecture & Editorial Guide

This directory contains the headless CMS schema models, desk customization, and content architecture for **AJNETWORKS**.

---

## 1. Schema Hierarchy & Models

```
Content Hub (Sanity Studio)
├── Tech Insights & Articles (`post`)
│   ├── Title, Slug, Category, Author
│   ├── Excerpt / Meta Description (140-160 chars)
│   ├── Cover Image (Hotspot + Alt Text)
│   └── Rich Text Body (H2, H3, Code, Quotes, Images)
│
├── Client Case Studies (`caseStudy`)
│   ├── Client Name, Industry, Practice Reference
│   ├── Executive Summary & Business Challenge
│   ├── Technical Architecture & Solution Body
│   ├── Quantifiable Metrics (Uptime, Latency, Conversion)
│   └── Hero Cover Image
│
├── Practice Areas (`service`)
│   ├── Title, Slug, Tagline, Overview
│   ├── Capabilities List
│   └── Practice FAQs (Structured Q&A)
│
├── Consultants & Authors (`teamMember`)
│   └── Name, Role, Bio, Avatar, LinkedIn URL
│
└── Global Settings (`siteSettings`)
    └── Site Name, Base URL, Contact Details, Addresses
```

---

## 2. Editor Workflow (Non-Technical Guide)

### Adding a New Insight Article
1. Log into Sanity Studio.
2. Select **Tech Insights & Articles** -> Click **Create New**.
3. Fill in:
   - **Article Title:** Clear and descriptive (<65 characters).
   - **Slug:** Click "Generate" to create a clean URL.
   - **Practice Area:** Select the relevant discipline (e.g. *Custom Software Engineering*).
   - **Excerpt:** Write a summary (140–160 chars) for search snippets and LinkedIn cards.
   - **Cover Image:** Upload high-resolution WebP/PNG image; ensure **Alt Text** is provided.
   - **Body:** Use formatting tools for headings (H2 for main sections, H3 for sub-sections).
4. Click **Publish**.

### Publishing a Client Case Study
1. Navigate to **Client Case Studies** -> Click **Create New**.
2. Enter **Client Name**, **Industry**, and **Challenge**.
3. Detail the **Solution Architecture**.
4. In **Quantifiable Results**, add at least 2 metrics (e.g. `99.9% Uptime`, `40% Cost Reduction`).
5. Click **Publish**.

---

## 3. Automated Webhook Deployment

When content is published in Sanity Studio:
1. A **Vercel Deploy Hook** is triggered automatically via Sanity Webhooks.
2. Static HTML is regenerated with fresh content and deployed to edge nodes in < 30 seconds.
3. No code commits or developer involvement required.

---

## 4. Image Guidelines & Standards
- **Format:** WebP or SVG preferred (JPEG/PNG are automatically converted via Sanity CDN).
- **Hero Banners:** 1200 x 630 px (16:9 ratio).
- **Icons / Badges:** SVG vector format.
- **Alt Text:** Mandatory on all images to maintain 100% SEO accessibility score.
