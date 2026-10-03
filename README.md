# Parviz Narimani Portfolio

## Structure
- `index.html` — site shell; loads homepage sections in order.
- `assets/site.css` — global design system.
- `assets/site.js` — section loader + global interactions.
- `sections/<name>/section.html` — content for one homepage section.
- `sections/<name>/style.css` — styles only for that section.
- `pages/publications/` — publications page.
- `pages/project-1/`, `project-2/`, `project-3/` — individual ongoing-project pages.

## Important edits before publishing
1. In `sections/hero/section.html`, replace `YOUR_NUMBER` with your WhatsApp number in international format without `+` or spaces.
2. In `sections/contact/section.html`, replace the Scholar, LinkedIn, ORCID and ResearchGate placeholders.
3. Replace the jewelry placeholder backgrounds with your own images when ready.
4. Replace project progress percentages and Project 03 name/content with current values.
5. Fill the Publications page with your real publication list.

## Local preview
Because the homepage uses `fetch()` to load section files, opening `index.html` directly with `file://` may be blocked by the browser. Preview through a local server, e.g. VS Code Live Server, or deploy to GitHub Pages. GitHub Pages serves it normally.
