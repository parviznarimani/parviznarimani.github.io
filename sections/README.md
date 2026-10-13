# sections

Website version 3.3 · Last updated: October 2026

Homepage source modules. Publication content lives in pages/publications/. The root build.py combines the seven homepage sections into index.html.

## Contents

- [about/](about/)
- [contact/](contact/)
- [hero/](hero/)
- [jewelry/](jewelry/)
- [projects/](projects/)
- [research/](research/)
- [strategy/](strategy/)

## Build and publish

From the website root, run `python3 build.py` after changes. Upload the changed sources and generated output, including sitemap.xml when page URLs change. The build runs locally; GitHub Pages serves the generated files.
