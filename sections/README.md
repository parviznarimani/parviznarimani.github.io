# Sections Architecture Guide

This document explains the modular `sections/` directory used by the
Parviz Narimani portfolio website. The homepage is intentionally divided
into independent sections so that each professional area can be edited,
redesigned, or replaced without rebuilding the entire site.

## 1. Directory Structure

``` text
sections/
├── hero/
│   ├── section.html
│   └── style.css
├── about/
│   ├── section.html
│   └── style.css
├── strategy/
│   ├── section.html
│   └── style.css
├── research/
│   ├── section.html
│   └── style.css
├── jewelry/
│   ├── section.html
│   └── style.css
├── projects/
│   ├── section.html
│   └── style.css
└── contact/
    ├── section.html
    └── style.css
```

Each folder represents one major homepage section.

-   `section.html` contains that section's semantic HTML and content.
-   `style.css` contains styling specific to that section.
-   Shared design rules such as colors, typography, `.glass`, `.btn`,
    `.section`, `.display`, and reveal behavior belong in
    `/assets/site.css`.
-   Global JavaScript, section loading, cursor effects, and shared
    interactions belong in `/assets/site.js`.
-   Standalone pages such as Publications and individual project pages
    are not homepage sections; they belong under `/pages/`.

------------------------------------------------------------------------

# 2. Hero Section

**Folder:** `sections/hero/`

**Purpose:** The Hero is the first visual and informational contact with
the visitor. It should establish identity immediately rather than trying
to explain the entire career history.

The Hero should communicate three things within a few seconds:

1.  Who the person is: **Parviz Narimani**
2.  What broad professional space he occupies
3.  What action the visitor can take next

## Recommended Content

The section should contain:

-   Personal portrait/image
-   Full name
-   Short professional descriptor
-   Concise introductory paragraph
-   Primary WhatsApp/contact button
-   Optional secondary navigation button
-   Animated background or decorative interactive element

The introductory copy should remain short. Detailed explanations of
research, marketing, jewelry, and projects belong in later sections.

## Visual Direction

The Hero should be visually strong and premium. The portrait can occupy
one side of the composition while the name and introduction occupy the
other. The background animation should support the composition without
competing with the portrait.

Appropriate effects include:

-   animated gradient fields
-   subtle particles
-   orbital lines
-   cursor-reactive light
-   blurred glowing shapes
-   slow parallax movement

Avoid excessive animation around the face or text because the primary
purpose is identification.

## Contact Button

The primary CTA is WhatsApp. Its URL should use the international
telephone format:

``` html
<a href="https://wa.me/YOUR_NUMBER" target="_blank" rel="noopener">
    Connect on WhatsApp
</a>
```

Replace `YOUR_NUMBER` with the complete country code and number without
`+`, spaces, parentheses, or hyphens.

------------------------------------------------------------------------

# 3. About / Multidisciplinary Identity Section

**Folder:** `sections/about/`

**Purpose:** This section explains the multidisciplinary nature of the
professional profile.

This section is based on the strongest interactive concept from the
earlier portfolio: a large statement accompanied by compact
professional-domain indicators and mouse-responsive visual behavior.

## Core Message

The section should communicate that the career is not restricted to one
discipline. The professional identity combines areas such as:

-   Strategy & Marketing
-   Machine Learning
-   Research & Development
-   Technology
-   Engineering
-   Creative/Luxury work

The section should not duplicate the Hero biography. The Hero answers
**"Who is Parviz?"** while this section answers **"How does he work
across disciplines?"**

## Interaction

This is an appropriate location for:

-   mouse-reactive movement
-   animated statistics
-   glowing cards
-   dynamic labels
-   subtle perspective transforms

The interaction should remain smooth and lightweight.

## Editing Guidance

Keep broad professional categories here. Specific research topics should
be moved to Research, jewelry work to Jewelry, and marketing frameworks
to Strategy.

------------------------------------------------------------------------

# 4. Strategy & Marketing Section

**Folder:** `sections/strategy/`

**Purpose:** This section presents business strategy and marketing as a
distinct professional capability.

It should show that the work extends beyond academic research and
software development into strategic thinking, market analysis,
positioning, content, brand development, and measurement.

## Recommended Narrative

The section can be structured around a strategy process such as:

``` text
Insight → Direction → Execution → Measure
```

### Insight

Understanding the market, customer, organization, competitors,
constraints, and available evidence.

Possible topics:

-   market research
-   customer behavior
-   competitor analysis
-   content analysis
-   business diagnosis

### Direction

Translating evidence into strategic choices.

Possible topics:

-   positioning
-   brand direction
-   marketing objectives
-   communication priorities
-   channel selection
-   strategic planning

### Execution

Turning strategy into operational programs.

Possible topics:

-   content systems
-   campaigns
-   digital marketing
-   social media
-   brand implementation
-   marketing workflows

### Measure

Evaluating whether the strategy and execution produce the intended
result.

Possible topics:

-   KPIs
-   performance analysis
-   conversion
-   engagement
-   marketing analytics
-   continuous optimization

## Visual Direction

This section can use a horizontal process, connected glass cards, or a
progressive visual flow.

It should feel more structured and business-oriented than the Research
section.

------------------------------------------------------------------------

# 5. Research Direction Section

**Folder:** `sections/research/`

**Purpose:** Present the principal academic and engineering research
directions clearly without turning the homepage into a publication
database.

The homepage version should remain concise and lead visitors to the
dedicated Publications page.

## Three Primary Tiles

### 1. Machine Learning

This tile represents data-driven modeling of engineering systems.

Potential technologies/topics include:

-   Support Vector Regression
-   Gaussian Process Regression
-   Artificial Neural Networks
-   XGBoost
-   ensemble learning
-   model evaluation
-   explainable/interpretive analysis

### 2. Symbolic Machine Learning

This tile focuses on interpretable mathematical modeling and symbolic
regression.

Potential topics include:

-   symbolic regression
-   interpretable machine learning
-   mathematical expression discovery
-   Alvyn® Symbol
-   engineering equation discovery
-   data-to-equation workflows

### 3. Manufacturing & Engineering

This tile represents experimental engineering research and
manufacturing/process applications.

Potential areas include:

-   grinding
-   materials
-   manufacturing processes
-   experimental characterization
-   process optimization
-   engineering data analysis

## Glass Design

All three tiles should share a coherent glassmorphism system:

-   translucent background
-   subtle border
-   blur
-   controlled glow
-   hover elevation
-   optional mouse perspective

The tiles should look related but can use different accent treatments.

## Publications CTA

Under the three cards, include a clear button:

``` text
View Publications →
```

The button should link to:

``` text
/pages/publications/
```

The Publications page should contain the detailed publication list,
external publication identifiers, journal information, and links where
appropriate.

------------------------------------------------------------------------

# 6. Jewelry Profession Section

**Folder:** `sections/jewelry/`

**Purpose:** Present jewelry-related professional work as a visually
distinct creative discipline.

Unlike Research and Projects, this section should not primarily rely on
text-heavy glass cards. Jewelry is visual; therefore imagery should
dominate.

## Recommended Format

Use a horizontal scrollable gallery or editorial image sequence.

Possible categories include:

-   Visual Identity
-   Product Storytelling
-   Luxury Content
-   Jewelry Campaigns
-   Naming & Narrative
-   Creative Direction

Each item can contain:

-   jewelry image
-   short category label
-   title
-   one-line description

## Image Strategy

Use real project photography whenever possible. Placeholder gradients
should only be temporary.

Recommended image organization:

``` text
assets/
└── images/
    └── jewelry/
        ├── visual-identity.jpg
        ├── product-storytelling.jpg
        ├── luxury-content.jpg
        └── naming-narrative.jpg
```

The section HTML can then reference these assets.

## Interaction

Suitable interactions include:

-   horizontal drag/scroll
-   image scale on hover
-   soft text reveal
-   parallax image movement
-   edge fade indicating more content
-   scroll snapping

The visual effects should remain refined because luxury presentation
benefits from restraint.

------------------------------------------------------------------------

# 7. Ongoing Projects Section

**Folder:** `sections/projects/`

**Purpose:** Show active work rather than only completed achievements.

The section contains three primary project tiles. Each tile displays the
project identity, short description, and current progress.

## Project Tile Structure

Each tile should contain:

-   project name
-   project category
-   one-sentence description
-   numerical progress percentage
-   circular or linear progress visualization
-   link to the project's dedicated page

Example:

``` text
Alvyn® Symbol
Symbolic Machine Learning

78%

Explore Project →
```

## Progress Values

Progress values are manually maintained unless a future automated data
source is introduced.

Do not present placeholder percentages as factual project status. Update
each percentage when the real status changes.

## Dedicated Project Pages

Each tile links to a separate page:

``` text
pages/
├── project-1/
│   └── index.html
├── project-2/
│   └── index.html
└── project-3/
    └── index.html
```

These pages can later be renamed to descriptive slugs, for example:

``` text
pages/
├── alvyn-symbol/
├── alvyn-engine/
└── another-project/
```

Descriptive names are preferable for maintainability and URLs.

## What a Project Page Can Include

A detailed project page can contain:

-   project overview
-   problem statement
-   motivation
-   current development status
-   architecture
-   technology stack
-   screenshots
-   research background
-   milestones
-   roadmap
-   related publications
-   GitHub link, if public
-   project updates

The homepage card should summarize; the project page should explain.

------------------------------------------------------------------------

# 8. Contact / Closing Section

**Folder:** `sections/contact/`

**Purpose:** Close the homepage with a strong professional statement and
provide external profile links.

This section continues the visual language of the existing portfolio
closing section.

A central statement such as:

> Ideas become interesting when disciplines collide.

works as the final conceptual message before the visitor leaves the
homepage.

## Recommended Links

The section can include:

-   GitHub
-   LinkedIn
-   Google Scholar
-   ORCID
-   ResearchGate
-   Scopus
-   Web of Science
-   email
-   WhatsApp
-   downloadable CV

External links should normally use:

``` html
target="_blank" rel="noopener"
```

Example:

``` html
<a
    href="YOUR_LINKEDIN_URL"
    target="_blank"
    rel="noopener"
>
    LinkedIn ↗
</a>
```

## Security

Never place passwords, private API keys, access tokens, private phone
data not intended for publication, or confidential documents inside the
repository.

The GitHub Pages repository is public, so HTML, CSS, JavaScript, images,
and other committed files should be treated as publicly accessible.

------------------------------------------------------------------------

# 9. How the Sections Are Loaded

The root `index.html` acts as the homepage shell.

The section files are modular fragments rather than complete independent
websites. `/assets/site.js` loads them into the homepage in the intended
sequence.

Conceptually:

``` text
index.html
    ↓
site.js
    ↓
loads:
    hero/section.html
    about/section.html
    strategy/section.html
    research/section.html
    jewelry/section.html
    projects/section.html
    contact/section.html
```

The intended homepage order is:

``` text
01  Hero
02  About
03  Strategy & Marketing
04  Research Direction
05  Jewelry Profession
06  Ongoing Projects
07  Contact
```

Changing this order should be done in the section-loading configuration
in the global JavaScript rather than by physically merging section HTML
files.

------------------------------------------------------------------------

# 10. CSS Responsibility

The website uses two levels of CSS.

## Global CSS

File:

``` text
/assets/site.css
```

Use global CSS for reusable design primitives such as:

-   color variables
-   body/background
-   global typography
-   navigation
-   `.section`
-   `.section-label`
-   `.display`
-   `.lead`
-   `.glass`
-   `.btn`
-   `.reveal`
-   cursor glow
-   shared responsive behavior

## Section CSS

Files:

``` text
/sections/[section-name]/style.css
```

Use section CSS only for styles unique to that section.

For example:

``` text
hero/style.css
```

should contain Hero-specific portrait, animation, layout, and decorative
rules---not generic button styling.

This separation prevents duplicated CSS and makes redesigns safer.

------------------------------------------------------------------------

# 11. JavaScript Responsibility

Global functionality belongs in:

``` text
/assets/site.js
```

Examples:

-   loading sections
-   global reveal observer
-   navigation behavior
-   cursor glow
-   shared animation initialization

Section-specific JavaScript should only be introduced when a section
genuinely needs independent behavior.

Avoid inline JavaScript inside section HTML unless there is a strong
reason. Keeping behavior centralized makes debugging easier.

------------------------------------------------------------------------

# 12. Standalone Pages vs. Homepage Sections

A homepage **section** and a standalone **page** serve different
purposes.

## Section

A section is part of the scrolling homepage.

Example:

``` text
sections/research/section.html
```

## Page

A page has its own URL and provides deeper information.

Example:

``` text
pages/publications/index.html
```

The Research section summarizes research directions; the Publications
page lists publications.

The Projects section summarizes ongoing projects; individual Project
pages explain them.

This prevents the homepage from becoming excessively long while still
allowing detailed professional information.

------------------------------------------------------------------------

# 13. Editing Workflow

When updating the website, first identify what type of change is being
made.

### Change text in one homepage section

Edit:

``` text
sections/[name]/section.html
```

### Change the appearance of one section

Edit:

``` text
sections/[name]/style.css
```

### Change a global color, button, navigation, or typography rule

Edit:

``` text
assets/site.css
```

### Change global interaction or section loading

Edit:

``` text
assets/site.js
```

### Change publication information

Edit:

``` text
pages/publications/index.html
```

### Change detailed project information

Edit the relevant file under:

``` text
pages/[project-name]/index.html
```

This modular approach is the main reason for separating the website into
folders.

------------------------------------------------------------------------

# 14. Recommended Future Improvements

The current architecture is designed so additional capabilities can be
added without rebuilding the homepage.

Useful future additions include:

1.  Replace the Hero placeholder with a professional portrait.
2.  Add real jewelry campaign images.
3.  Populate Publications with verified publication records.
4.  Replace placeholder project percentages with actual progress.
5.  Rename generic project folders to descriptive project slugs.
6.  Add a downloadable CV.
7.  Connect LinkedIn, Google Scholar, ORCID, ResearchGate, Scopus, and
    Web of Science.
8.  Add project screenshots and demos.
9.  Add structured metadata for search engines.
10. Optimize images to WebP/AVIF for faster loading.
11. Add accessible alternative text to all meaningful images.
12. Test responsive behavior on mobile, tablet, and desktop.
13. Add a custom domain later if desired.

------------------------------------------------------------------------

# 15. Design Principle

The homepage should not present every achievement at once.

Its job is to establish a coherent professional identity across several
disciplines and then allow visitors to choose the area most relevant to
them.

The intended narrative is:

``` text
WHO I AM
    ↓
HOW I THINK ACROSS DISCIPLINES
    ↓
STRATEGY & MARKETING
    ↓
RESEARCH & ENGINEERING
    ↓
JEWELRY & CREATIVE WORK
    ↓
WHAT I AM BUILDING NOW
    ↓
CONNECT WITH ME
```

This sequence makes the site function as a professional portfolio rather
than a conventional résumé page.
