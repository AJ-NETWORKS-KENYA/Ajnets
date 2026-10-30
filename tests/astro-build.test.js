const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.resolve(__dirname, '..');
const DIST = path.join(ROOT, 'dist');
const CONTENT = path.join(ROOT, 'src', 'content');

const EXPECTED_DIST_HTML = [
  'index.html',
  '404.html',
  'elements/elements.html',
  'company/about-us.html',
  'company/book-consultation.html',
  'company/faq.html',
  'company/privacy.html',
  'company/responsible-disclosure.html',
  'company/terms.html',
  'services/services.html',
  'services/cybersecurity.html',
  'services/networking.html',
  'services/performance-seo.html',
  'services/software-engineering.html',
  'services/technology-strategy.html',
  'portfolio/client-success.html',
  'portfolio/case-study-audiophile.html',
  'portfolio/case-study-bada.html',
  'portfolio/case-study-crappo.html',
  'portfolio/case-study-greenremedies.html',
  'portfolio/case-study-racnyali.html',
  'portfolio/case-study-sgss.html',
  'portfolio/case-study-transitflow.html',
  'insights/insights.html',
  'insights/post.html',
];

test('Astro Architecture & Build Verification Suite', async (t) => {
  await t.test('Content Collections JSON entries exist and have required SEO fields', () => {
    const collections = ['system', 'company', 'services', 'caseStudies', 'insights'];
    let totalEntries = 0;

    for (const col of collections) {
      const colDir = path.join(CONTENT, col);
      assert.ok(fs.existsSync(colDir), `Missing content collection directory: ${col}`);
      const files = fs.readdirSync(colDir).filter((f) => f.endsWith('.json'));
      for (const file of files) {
        totalEntries++;
        const raw = fs.readFileSync(path.join(colDir, file), 'utf-8');
        const data = JSON.parse(raw);
        assert.ok(data.slug, `[${col}/${file}] missing slug`);
        assert.ok(data.title && data.title.length >= 10, `[${col}/${file}] invalid title`);
        assert.ok(data.description && data.description.length >= 30, `[${col}/${file}] invalid description`);
        assert.ok(data.canonicalUrl && data.canonicalUrl.startsWith('https://ajnetworks.co'), `[${col}/${file}] invalid canonicalUrl`);
        assert.ok(data.bodyHtml && data.bodyHtml.length > 0, `[${col}/${file}] empty bodyHtml`);
      }
    }

    assert.strictEqual(totalEntries, 25, 'Expected exactly 25 content collection entries across all 5 collections');
  });

  await t.test('Astro static build (dist/) outputs all 25 HTML pages and static assets', () => {
    assert.ok(fs.existsSync(DIST), 'dist/ directory does not exist — run npm run build first');

    for (const relHtml of EXPECTED_DIST_HTML) {
      const fullPath = path.join(DIST, relHtml);
      assert.ok(fs.existsSync(fullPath), `Missing built HTML file: dist/${relHtml}`);
      const html = fs.readFileSync(fullPath, 'utf-8');
      assert.ok(html.includes('type="application/ld+json"'), `Missing JSON-LD in dist/${relHtml}`);
      assert.ok(html.includes('rel="canonical"'), `Missing canonical link in dist/${relHtml}`);
      assert.ok(html.includes('id="site-header"'), `Missing shared Header in dist/${relHtml}`);
      assert.ok(html.includes('id="site-footer"'), `Missing shared Footer in dist/${relHtml}`);
      assert.ok(html.includes('id="cookie-consent-banner"'), `Missing CookieConsent in dist/${relHtml}`);
    }

    assert.ok(fs.existsSync(path.join(DIST, 'style.min.css')), 'Missing dist/style.min.css');
    assert.ok(fs.existsSync(path.join(DIST, 'sitemap.xml')), 'Missing dist/sitemap.xml');
    assert.ok(fs.existsSync(path.join(DIST, 'robots.txt')), 'Missing dist/robots.txt');
  });

  await t.test('vercel.json rewrites map cleanly to generated dist/ HTML targets', () => {
    const vercelConfig = JSON.parse(fs.readFileSync(path.join(ROOT, 'vercel.json'), 'utf-8'));
    for (const rule of vercelConfig.rewrites) {
      const targetHtml = path.join(DIST, `${rule.destination.replace(/^\//, '')}.html`);
      assert.ok(
        fs.existsSync(targetHtml),
        `Rewrite ${rule.source} -> ${rule.destination} points to missing ${targetHtml}`
      );
    }
  });

  await t.test('About Us page has clean Bootstrap grid nesting and zero stock template artifacts', () => {
    const aboutHtml = fs.readFileSync(path.join(DIST, 'company', 'about-us.html'), 'utf-8');
    assert.ok(!aboutHtml.includes('Glorious Years'), 'About Us still contains stock template counter "Glorious Years"');
    assert.ok(!aboutHtml.includes('data-to="330"'), 'About Us still contains stock template counter 330');
    assert.ok(!aboutHtml.includes('data-to="850"'), 'About Us still contains stock template counter 850');
    assert.ok(!aboutHtml.includes('Sarah Kimani'), 'About Us still contains commented-out dummy team member');
    assert.ok(!aboutHtml.includes('We hire and build your own remote dedicated development'), 'About Us still contains stock template copy');
    assert.ok(aboutHtml.includes('object-fit: cover'), 'About Us leadership portrait missing circular aspect-ratio styling');
  });
});

