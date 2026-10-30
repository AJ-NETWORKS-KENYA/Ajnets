import { defineConfig } from 'astro/config';
import fs from 'node:fs';
import path from 'node:path';

const vercelConfigPath = path.resolve('./vercel.json');
const vercelConfig = fs.existsSync(vercelConfigPath)
  ? JSON.parse(fs.readFileSync(vercelConfigPath, 'utf-8'))
  : { rewrites: [], redirects: [] };

const rewriteMap = new Map(
  (vercelConfig.rewrites || []).map((r) => [r.source, r.destination])
);
const redirectMap = new Map(
  (vercelConfig.redirects || []).map((r) => [r.source, r])
);

function attachVercelRouting(middlewares, isPreview = false) {
  middlewares.use((req, res, next) => {
    if (!req.url) return next();
    const [pathname, search] = req.url.split('?');
    const cleanPath = pathname.length > 1 && pathname.endsWith('/')
      ? pathname.slice(0, -1)
      : pathname;

    if (redirectMap.has(cleanPath)) {
      const rule = redirectMap.get(cleanPath);
      res.statusCode = rule.permanent ? 308 : 307;
      res.setHeader('Location', rule.destination + (search ? `?${search}` : ''));
      res.end();
      return;
    }

    let targetPath = rewriteMap.get(cleanPath) || cleanPath;

    if (isPreview && targetPath !== '/' && !path.extname(targetPath)) {
      const candidateHtml = path.resolve('./dist', `.${targetPath}.html`);
      if (fs.existsSync(candidateHtml)) {
        targetPath = `${targetPath}.html`;
      }
    }

    if (targetPath !== pathname) {
      req.url = targetPath + (search ? `?${search}` : '');
    }
    next();
  });
}

export default defineConfig({
  site: 'https://ajnetworks.co',
  output: 'static',
  trailingSlash: 'never',
  build: {
    format: 'file',
  },
  vite: {
    plugins: [
      {
        name: 'vercel-clean-url-rewrites',
        configureServer(server) {
          attachVercelRouting(server.middlewares, false);
        },
        configurePreviewServer(server) {
          attachVercelRouting(server.middlewares, true);
        },
      },
    ],
  },
});
