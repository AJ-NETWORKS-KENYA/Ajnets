# AJNETWORKS — Application Flow (APP_FLOW.md)

> **Version:** 2.0.0  
> **Maintainer:** AJNETWORKS Product Team  

---

## 1. Information Architecture & Route Map

All pages are generated at build time by Astro (`src/pages/`) into `dist/` and served with clean URLs via `vercel.json` rewrites (mirrored in `astro.config.mjs` for local development):

```
Home (/ -> src/pages/index.astro)
 ├── Services Hub (/services -> src/pages/services/[slug].astro)
 │    ├── Technology & Digital Strategy (/technology-strategy)
 │    ├── Custom Software Engineering (/software-engineering)
 │    ├── Cybersecurity & Assurance (/cybersecurity)
 │    ├── Infrastructure & Networking (/networking)
 │    └── Performance Engineering & SEO (/performance-seo)
 ├── Portfolio & Client Success (/client-success -> src/pages/portfolio/[slug].astro)
 │    ├── Bada Language Institute (/case-study-bada)
 │    ├── SGSS Mombasa Medical Fund (/case-study-sgss)
 │    ├── Rotaract Club Nyali (/case-study-racnyali)
 │    ├── Green Remedies E-Commerce (/case-study-greenremedies)
 │    ├── Audiophile E-Commerce (/case-study-audiophile)
 │    ├── Crappo Crypto Platform (/case-study-crappo)
 │    └── Transit Flow Logistics (/case-study-transitflow)
 ├── Insights & Articles (/insights -> src/pages/insights/[slug].astro)
 │    └── Featured Article (/post)
 ├── Company & Legal (/about-us -> src/pages/company/[slug].astro)
 │    ├── About Us (/about-us)
 │    ├── Book Consultation / Contact (/book-consultation, /contact)
 │    ├── Frequently Asked Questions (/faq)
 │    ├── Privacy Policy (/privacy)
 │    ├── Terms of Service (/terms)
 │    └── Responsible Disclosure (/responsible-disclosure)
 └── System Pages
      ├── Custom 404 Error Page (/404 -> src/pages/404.astro)
      └── UI Elements Reference (/elements/elements -> src/pages/elements/elements.astro)
```

## 2. User Journey & Lead Intake Flow

1. **Discovery:** Visitor lands on `/` or a practice/case-study landing page via organic search, AI citation, or direct referral.
2. **Regional Personalization:** Client-side idle check (`RwandaBanner.astro`) detects visitors from Rwanda (`country_code === "RW"`) and surfaces the localized Rwanda operations banner.
3. **Engagement:** User explores service capabilities, quantifiable case study outcomes, or technical insights.
4. **Conversion:** User submits the consultation form on `/book-consultation` (or `/contact`).
5. **Processing:** Serverless endpoint `POST /api/contact` verifies honeypot (`bot_field`), checks IP rate limits, validates fields, and dispatches lead notifications via regional SMTP.
