<h1><img src="parviznarimaniMainLogo70X.png" alt="Parviz Narimani logo" width="70" height="70"> Parviz Narimani</h1>

<img align="right" src="sections/hero/medias/parviznarimani-small.png" alt="Parviz Narimani portrait" width="260">

**Last updated: October 2026 · Website version: 3**

**Strategy · Research · Machine Learning · Jewelry**

<br clear="all">

---

I work at the intersection of **strategic thinking and design thinking**, taking a multidisciplinary approach to extend the intelligence of **machine learning and data analytics** across engineering, research, and business management. Alongside this technical and strategic work, **jewelry and gold manufacturing** is both my profession and a long-standing passion—a field where my experience in **business management, strategy, and digital transformation** comes together with creativity, craftsmanship, and technology.

[Visit my website](https://parviznarimani.github.io/) · [GitHub](https://github.com/parviznarimani) · [LinkedIn](https://www.linkedin.com/in/parviznarimani/) · [WhatsApp](https://wa.me/989363084896) · [Email](mailto:parviznarimani91@gmail.com)

## About this repository

This repository contains my personal website: a responsive, static portfolio bringing together strategy, research, gold and jewelry, publications, and ongoing projects. It uses HTML, CSS, JavaScript, and a small Python build script. No npm dependencies, database, or application server are needed.

The portrait beside the title is a plain image. The website’s animated frame and visual effects are not included in this README.

## Website sections

| Section | Content |
| --- | --- |
| Introduction | Portrait, professional interests, biography, and links into the site |
| About | “Building across disciplines” and four areas of focus |
| Strategy | “Strategy is a pattern in decisions,” strategic interests, and an illustrative growth chart |
| Research | “Intelligence by Design,” Generic ML, Ensemble / Stacking, and Symbolic ML |
| Gold & Jewelry | “Eternal Light,” a three-image carousel, and a dedicated jewelry page with imagery, a transformation diagram and an action-plan download |
| Ongoing projects | “Currently building,” three editable project cards, and progress percentages |
| Connect | WhatsApp, Email, LinkedIn, and Download CV |
| Blog | Six source-linked articles, original covers, and editable post folders |

The publications page contains separate tables for ongoing projects and published papers/preprints. Individual project and paper pages provide dedicated destinations. A custom 404 page offers a return link.

## Repository structure

Every folder below contains its own README.md with local file inventory and editing guidance.

```text
.
├── index.html
├── 404.html
├── build.py
├── README.md
├── parviznarimaniMainLogo70X.png
├── robots.txt
├── sitemap.xml
├── .nojekyll
├── assets/
│   └── licenses/
├── sections/
│   ├── about/
│   │   └── medias/
│   ├── contact/
│   │   └── medias/
│   ├── hero/
│   │   └── medias/
│   ├── jewelry/
│   │   └── medias/
│   ├── projects/
│   │   ├── medias/
│   │   ├── project1/
│   │   ├── project2/
│   │   └── project3/
│   ├── research/
│   │   └── medias/
│   └── strategy/
│       └── medias/
└── pages/
    ├── blog/                  # Blog post content and build script
    ├── jewelry/
    │   └── medias/
    ├── project-1/
    │   └── medias/
    ├── project-2/
    │   └── medias/
    ├── project-3/
    │   └── medias/
    └── publications/          # Publication content, paper pages and PDFs
```

Homepage sections have their own `section.html` and `style.css`. Keep section images and other media in their respective `medias/` folders.

## Run locally

Install Python 3, then run these commands from the repository root:

```sh
python3 build.py
python3 -m http.server 8765
```

Open [the local website](http://localhost:8765/). The root opens `index.html` directly. Stop the preview server with `Ctrl+C`.

Use the local HTTP server rather than opening the HTML directly: browsers need HTTP access to fetch the editable text files reliably.

## Edit section descriptions

| Content | Editable source |
| --- | --- |
| Hero biography | `sections/hero/aboutMe.txt` |
| About | `sections/about/aboutDescription.txt` |
| Strategy | `sections/strategy/aboutStartegy.txt` |
| Research | `sections/research/researchDirections.txt` |
| Jewelry | `sections/jewelry/jewelryDirectionAbout.txt` |
| Ongoing projects | `sections/projects/ongoingProjectsAbout.txt` |

Use `**words**` to emphasize phrases in these descriptions. The spelling of `aboutStartegy.txt` is intentional in the current implementation; keep it unchanged unless you also update its references.

The browser fetches these descriptions when the homepage loads. The build also embeds them directly in HTML so content remains available to crawlers and visitors without JavaScript. **Always run `python3 build.py` after editing**, then upload the source files and regenerated output together.

To change headings, labels, links, or card structure, edit the relevant `section.html`. To change appearance, edit that section’s `style.css`. Shared styles and interactions live in `assets/`. Dedicated page templates are currently defined in `build.py`.

## Edit project cards

Each project has its own folder under `sections/projects/`: `project1`, `project2`, and `project3`. Each contains four text files:

| File | What to enter |
| --- | --- |
| `projectStatus.txt` | A status such as `In development` or `Concept` |
| `projectName.txt` | The project’s display name |
| `projectDescription.txt` | A plain-text description of 25–35 words |
| `projectProgress.txt` | An integer from `1` to `99`, without a percent sign |

For example, entering `56` displays **56%**. The homepage reads these values on load; rebuilding also updates the static cards and the project names, descriptions, and statuses used in generated project pages and the ongoing-projects table.

The build rejects progress values outside 1–99. The description length is an editorial guideline rather than an automatic restriction. Keep progress values representative of the actual project status.

For a fourth project, extend the generator, section template, and corresponding file structure; creating another folder alone does not add a new card.

## Images and typography

- Portrait: `sections/hero/medias/parviznarimani-small.png`.
- Jewelry images: `sections/jewelry/medias/Image1.png`, `Image2.png`, and `Image3.png`.
- Jewelry captions: Luxury Contents, Brand Awareness, and Visual Campaign.
- Jewelry tiles retain a rectangular 3:4 aspect ratio, with contained images and gold background glows.
- The supplied Inter font is self-hosted at `sections/hero/medias/Inter-Variable.ttf`.

Keep filenames, capitalization, and paths exact. Use optimized images and meaningful alternative text when adding assets. Replacing an image with the same filename preserves its existing references.

## Publications

Publication records are stored in `pages/publications/papers.json`. Run the build after changing records. The current collection includes seven journal articles and one preprint.

Each record supplies bibliographic information, an abstract, a slug, and optional DOI/dataset links. Inspect an existing record for the field structure before adding one. Place its PDF at:

```text
pages/publications/papers/<slug>/medias/paper.pdf
```

The build generates an individual reading page alongside that PDF.

- Journal titles link to their DOI when available; otherwise they open the local reading page.
- Every entry provides a local reading link and a PDF download.
- Dataset buttons are not displayed in the current publication table.
- Individual reading pages offer Download paper, Open on GPT, and a publisher or preprint link when available.
- `pages/publications/universalScholarlyAnalysisPrompt.md` contains the editable scholarly analysis instructions. Open on GPT passes public links; visitors may need to attach files manually.
- A green tick identifies a published journal article; it does not certify dataset quality or indexing.
- Search and year filters enhance the static publication table.

Preserve the distinction between preprints and published journal versions. Verify metadata and ensure you have permission to share each uploaded PDF.

## GitHub Pages deployment

The intended repository is `parviznarimani/parviznarimani.github.io`.

1. Run `python3 build.py` locally.
2. Copy the contents of this website directory into the repository root. Do not nest them inside an extra `website` or `outputs` folder, and do not upload only a ZIP.
3. Include `index.html`, `404.html`, `.nojekyll`, `assets/`, `sections/`, `pages/`, `robots.txt`, and `sitemap.xml`, plus the root logo `parviznarimaniMainLogo70X.png`. Keep `build.py` and this README for maintenance. Skip macOS `.DS_Store` files.
4. In repository **Settings → Pages**, choose **Deploy from a branch**, select the branch containing the files, and select **/ (root)**.
5. Wait for the deployment to finish, then check the live homepage, images, contact links, paper downloads, and a nonexistent URL to verify the 404 page.

The homepage is `index.html`, which GitHub Pages serves directly at the root domain. No homepage redirect is needed.

GitHub Pages serves the generated files; it does not run this Python script under the branch-based setup above. No automated rebuild workflow is included. Rebuild locally before publishing content changes.

## Search visibility and sitemap

Generated pages include canonical URLs, descriptions, and Open Graph metadata. The homepage includes structured information about the site owner. Paper pages include bibliographic citation metadata, visible abstracts, and PDF links intended to support scholarly crawling.

`build.py` regenerates `sitemap.xml` from the pages it creates, excluding the 404 page. Editing content on an existing URL does not add a sitemap entry. Add new pages to the generator so their URLs are included automatically.

Crawler-compatible markup supports discovery but does not guarantee Google or Google Scholar indexing. Review the live deployment and bibliographic metadata before requesting indexing.

## Accessibility and interactions

The website includes a skip link, semantic headings, keyboard focus styles, a mobile navigation toggle, and labeled carousel controls. Jewelry slides can be navigated using controls, arrow keys, and touch gestures. Reduced-motion preferences disable CSS and canvas animations. Animated GIF artwork continues playing independently. Core content and navigation remain present in generated HTML.

## Maintenance checklist

- Edit source templates or text files, not generated HTML pages.
- Run `python3 build.py` and resolve any reported errors.
- Preview desktop and mobile layouts.
- Check changed links, images, downloads, and project progress.
- Upload the changed sources and regenerated pages together.
- Check the live site after deployment.

The jewelry page includes its model introduction, six-image slideshow, digital transformation diagram, downloadable action plan and a dedicated contact section. Project detail pages also provide starting points for future milestones and methodology.

## Contact

- [WhatsApp](https://wa.me/989363084896)
- [Email](mailto:parviznarimani91@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/parviznarimani/)

---

Born curious. Building with ❤️ since 1991.

© Parviz Narimani

## Animation attribution

The portrait’s dotted Thinking animation adapts the composing/ribbon renderer from [Thinking Orbs by Jakub Antalik](https://github.com/Jakubantalik/thinking-orbs). Its MIT license is included in `assets/licenses/thinking-orbs-LICENSE.txt`.

## Version 3 content guide

- Current logo and favicon: `parviznarimaniMainLogo70X.png`.
- Projects: Alvyn® Symbol (70%), Alvyn® Engine (30%), and SkyWings® (10%, Concept).
- CV: `sections/contact/medias/ParvizNarimani_CV.pdf`.
- Jewelry introduction: `pages/jewelry/jewelryDescription.txt`.
- Jewelry diagram: `pages/jewelry/digitalTransformation.html`.
- Jewelry artwork and action plan: `pages/jewelry/medias/`, including the four GIF icons and `applicationNote.pdf`.
- Blog: `pages/blog/`. Copy `_template` to `Post7[YYYY-MM-DD]`, fill `title.txt`, `metadescription.txt`, and `mainText.txt`, and add a cover in `medias/`. Optional `sources.json` records references.

Run `python3 pages/blog/build.py` from the website root to build the blog and regenerate the full site sitemap. This delegates to the shared build so other site pages remain listed. The six initial posts are dated October 9, 2026; their source publication dates are distinguished in article text. SVG covers are supported alongside PNG, JPEG, WebP and AVIF.

Blog main text supports paragraphs, **bold**, H2 (`##`) and H3 (`###`) headings. It is not a full Markdown renderer. For detailed publishing instructions, see [the blog README](pages/blog/README.md).
