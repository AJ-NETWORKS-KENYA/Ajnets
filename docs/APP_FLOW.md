# AJNETWORKS — Application Flow (APP_FLOW.md)

> **Version:** 1.0.0  
> **Maintainer:** AJNETWORKS Product Team  

---

## 1. Information Architecture & Navigation Map

```
Home (index.html)
 ├── Services Overview (services/index.html)
 │    ├── Cloud Infrastructure (services/cloud.html)
 │    ├── Managed IT Services (services/managed-it.html)
 │    ├── Networking Solutions (services/networking.html)
 │    └── Cybersecurity Solutions (services/cybersecurity.html)
 ├── Portfolio & Case Studies (portfolio/index.html)
 ├── Industry Insights (insights/index.html)
 ├── Company Information (company/index.html)
 │    ├── About Us (company/about.html)
 │    └── Careers & Team (company/careers.html)
 └── Contact & Consultation (company/contact.html)
```

## 2. User Journey & Lead Intake Flow

1. **Discovery:** Visitor lands on `index.html` or a specialized service landing page via organic search or direct referral.
2. **Engagement:** User reviews service capabilities, case study portfolio, or technical insights.
3. **Conversion:** User fills out contact form on `company/contact.html` or clicks direct communication options (Email: `hello@ajnetworks.co`, Tel: `+254 758 238 617`).
4. **Processing:** Dynamic API endpoint `/api/contact` validates request body and routes lead notification to business operations.
