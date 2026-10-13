# blog

Website version 3.3 · Last updated: October 2026

Blog sources, generated listing, and standalone build entry point.

## Contents

- [_template/](_template/)
- [Post1[2026-10-09]/](Post1%5B2026-10-09%5D/)
- [Post2[2026-10-09]/](Post2%5B2026-10-09%5D/)
- [Post3[2026-10-09]/](Post3%5B2026-10-09%5D/)
- [Post4[2026-10-09]/](Post4%5B2026-10-09%5D/)
- [Post5[2026-10-09]/](Post5%5B2026-10-09%5D/)
- [Post6[2026-10-09]/](Post6%5B2026-10-09%5D/)
- [build.py](build.py)
- [index.html](index.html)

## Build and publish

From the website root, run `python3 pages/blog/build.py` after changes. Upload the changed sources and generated output, including sitemap.xml when page URLs change. The build runs locally; GitHub Pages serves the generated files.

## Blog publishing instructions


1. Copy `_template` to a folder named `Post1[2026-10-09]` (use your post number and publication date).
2. Fill `title.txt`, `metadescription.txt`, and `mainText.txt`.
3. Put an image named `cover.png`, `cover.jpg`, or `cover.webp` in `medias/`. If no cover-named image exists, the first supported image alphabetically is used.
4. From the website root run `python3 pages/blog/build.py`. Alternatively run this folder’s `build.py` directly. It uses the shared site build to preserve all existing sitemap entries.
5. Upload the new post folder, generated blog listing, sitemap.xml, and any other changed generated files.

Newest dates appear first. Underscore-prefixed folders are drafts and are not published. Empty fields or a missing cover cause a build error rather than publishing unfinished content. Use blank lines for paragraphs, `## Heading` for H2, `### Heading` for H3, and `**bold**` for emphasis in mainText.txt. The post title is its sole H1. Use an H2 before its subordinate H3. Other Markdown features are not supported.

All published posts are statically generated and included in sitemap.xml. Rebuild after any edit. If removing a post, remove its folder locally and from GitHub, then rebuild and upload the listing and sitemap. Renaming a folder changes its public URL.

The six initial posts use original SVG covers. SVG is also supported. Optional sources.json stores an array of objects with title and HTTPS url fields; these render as clickable references beneath each article.
