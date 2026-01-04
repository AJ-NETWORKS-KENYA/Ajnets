## Quick orientation for AI coding agents

This repo is a static frontend site (HTML/CSS/JS) built from a theme. It is not a server-side app.
Keep changes minimal and targeted: most behavior is implemented in `index.html`, other top-level HTML pages (e.g. `about-us.html`, `services.html`, `portfolio.html`) and `js/` + `css/` folders.

Key things to know (why files are where they are):

- `index.html` is the homepage and contains the primary layout and the Revolution Slider config. Edit slides, copy or image references here. Example: homepage slider images are under `images/slider/` and configured inside `#rev_slider_one` in `index.html`.
- `js/scripts.js` contains theme-specific front-end logic (sticky header, search toggle, counters, Isotope filters). Prefer modifying this file or adding a small new file under `js/` rather than editing minified vendor files.
- `plugins/revolution/...` and `css/*.css` contain third-party vendor assets. Avoid editing vendor files in-place unless you must — prefer overrides in `style.css` or new stylesheet files (e.g. `css/home15.css`, `css/home16.css`).
- `images/`, `fonts/` and `css/` contain static assets; use existing folder structure and relative links.

Conventions and patterns discovered:

- Pages are simple static HTML (e.g., `about-us.html`, `contact.html`, `blog.html`). Navigation uses relative links. Keep file names and relative paths when changing links.
- UI uses jQuery plugins (Owl Carousel, Magnific Popup, Isotope, easyPieChart) and Revolution Slider. Scripts are initialized in `js/scripts.js` and `plugins/revolution/revolution/js/*.js`.
- Visual customizations are typically applied in `style.css`. Small behavior changes go into `js/scripts.js`.

Developer workflows (how to preview / quick dev commands):

- Preferred quick preview: use VS Code Live Server extension (recommended).
- Quick local server (PowerShell):

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Integration points & what to avoid:

- No backend code or build system present—this is a static site. There are no Node/npm or Python build files in the repo root.
- Do NOT modify files under `plugins/revolution/` unless fixing a critical bug; those are vendored plugin files. Prefer overriding CSS in `style.css` or extending behavior in `js/scripts.js`.

Examples to reference when making changes:

- To change header behavior (sticky header), edit `js/scripts.js` — search for "Sticky Header" and update scroll thresholds.
- To change the slider images or slide text, edit `index.html` inside the `#rev_slider_one` slides and put images in `images/slider/`.
- To add a new page, copy an existing page (e.g. `about-us.html`) and update navigation links in the header (`index.html` and other pages). Keep relative paths.

Commit guidelines for AI agents:

- Make one focused change per branch/PR. Keep vendor files untouched unless necessary. Include a short summary explaining why a change is safe (e.g., "override CSS to adjust hero padding" or "fix sticky header threshold for small screens").

If anything here is unclear or you need examples for another file (e.g., specific CSS overrides or how to reinitialize a Revolution slider), tell me which area to expand and I will iterate.
