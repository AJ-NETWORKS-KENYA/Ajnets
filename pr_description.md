💡 **What:** Added a module-level cache for Nodemailer transport instances in `api/contact.js`.

🎯 **Why:** To improve performance on serverless environments (like Vercel) by reusing existing connections across warm invocations. This avoids repeatedly invoking `nodemailer.createTransport`, which can be computationally expensive and introduce latency on every single request.

📊 **Measured Improvement:**
- **Baseline (1000 requests):** `createTransport` was called 1000 times.
- **Improved (1000 requests):** `createTransport` is called only 1 time (for requests hitting the same cached credentials).
- **Impact:** Significant reduction in initialization overhead per request on warm serverless functions.
