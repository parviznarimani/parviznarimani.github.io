# publications

Website version 3.3 · Last updated: October 2026

Publication sources, generated listing, individual reading pages, PDFs and the shared analysis prompt. Paper records come from pages/publications/papers.json; ongoing publication fields come from ongoing/paper1 through paper3, independently of homepage projects.

## Contents

- [ongoing/](ongoing/)

- [medias/](medias/)
- [papers/](papers/)
- [index.html](index.html)
- [papers.json](papers.json)
- [universalScholarlyAnalysisPrompt.md](universalScholarlyAnalysisPrompt.md)

## Build and publish

From the website root, run `python3 build.py` after changes. Upload the changed sources and generated output, including sitemap.xml when page URLs change. The build runs locally; GitHub Pages serves the generated files.

## Editing publications

Edit `papers.json` for bibliographic records. Each article is generated at `papers/<slug>/index.html`, and its PDF belongs in `papers/<slug>/medias/paper.pdf`. Edit `universalScholarlyAnalysisPrompt.md` for the ChatGPT analysis instructions. Run `python3 build.py` from the website root to update pages, metadata, links and the sitemap.
