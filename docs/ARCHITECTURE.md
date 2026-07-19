# AJNETWORKS — System Architecture (ARCHITECTURE.md)

> **Version:** 1.0.0  
> **Maintainer:** AJNETWORKS Architecture Team  

---

## 1. System Overview

```
                          +------------------------+
                          |   Client Browser /     |
                          |     Mobile Users       |
                          +-----------+------------+
                                      |
                                      v
                          +------------------------+
                          |    Vercel Edge CDN     |
                          |  (Global Distribution) |
                          +-----------+------------+
                                      |
           +--------------------------+--------------------------+
           |                                                     |
           v                                                     v
+-----------------------+                             +--------------------+
| Static Web Assets     |                             | Serverless API     |
| (HTML, CSS, JS, Img)  |                             | (/api/contact.js)  |
+-----------------------+                             +--------------------+
```

## 2. Infrastructure & Hosting
- **Edge Network:** Hosted on Vercel with automatic SSL, HTTP/2, and global edge caching.
- **Minified Delivery:** Production CSS served via `style.min.css`.
- **Security Envelope:** Guarded by Content Security Policy (CSP), HSTS, and frame protection headers configured in `vercel.json` and `.htaccess`.

## 3. Automated Quality & Regression Testing
- **Execution Engine:** Python test & evaluation scripts (`execution/test_brand_links.py`, `execution/eval_brand_seo.py`).
- **CI Pipelines:** Enforced via GitHub Actions on every Pull Request.
