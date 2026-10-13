# Post5[2026-10-09]

Website version 3.3 · Last updated: October 2026

Editable blog post. title.txt supplies the H1, metadescription.txt supplies the preview and metadata, and mainText.txt supplies the article. sources.json supplies source links; medias/ holds the cover. The folder date controls ordering and publication metadata.

## Contents

- [medias/](medias/)
- [index.html](index.html)
- [mainText.txt](mainText.txt)
- [metadescription.txt](metadescription.txt)
- [sources.json](sources.json)
- [title.txt](title.txt)

## Build and publish

From the website root, run `python3 pages/blog/build.py` after changes. Upload the changed sources and generated output, including sitemap.xml when page URLs change. The build runs locally; GitHub Pages serves the generated files.
