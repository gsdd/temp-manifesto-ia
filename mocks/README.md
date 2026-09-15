# Navigation wireframe mock (v3)

A single self-contained HTML file that shows the v3 navigation and sitemap so stakeholders can see the structure without reading markdown. It is a wireframe: grey boxes, system font, no brand colours, no imagery. It is not a design.

v3 changes the words, not the structure: the mega-nav shows the v3 labels and plain-English subtitles from `docs/01-primary-navigation.md`, and a "Show what changed from v2" toggle in the intro reveals the previous label next to any that was renamed. See `docs/nav-wording-decisions.md` for the reasons.

## How to open it

Option 1, locally: download or clone the repository and double-click `mocks/index.html`. It opens in any modern browser. No server, build step or internet connection is needed.

Option 2, from GitHub: open `mocks/index.html` in the GitHub file view and use the raw or preview link, or enable GitHub Pages on the branch and visit `/mocks/index.html`.

## The two-second test

The page loads with the What we do panel already open. The three pillars of Andy's Growth Architecture triangle should be readable immediately, left to right: **Growth Strategy**, **Activation Services**, **CEO Advisory**. If that is not the first thing you see, the mock has failed its job.

## The plain-language test (v3)

Pick an intent a prospect might arrive with: "customer experience", "website", "research", "loyalty", "membership", "AI", "operating model", "interim team", "CEO advisor". You should be able to point at the mega-nav item that catches it without knowing any Manifesto term, because the word is in a label or the subtitle directly beneath it. The full intent-to-item map is in `docs/nav-wording-decisions.md`.

## What it contains

Three tabs at the top of the page:

| Tab | Shows | Source document |
|---|---|---|
| Desktop navigation | The five-item header; the What we do mega-nav open on load (one heading line, three pillar columns with labels and subtitles, one thin footer row); the Insights and About dropdowns; Our work as a plain link; Contact as a button; the Home page block order as grey placeholders including the triangle block; the footer | `docs/01-primary-navigation.md`, `docs/03-page-layouts.md` (T1) |
| Mobile navigation | A phone frame with the collapsed header and the full-screen menu: What we do as a nested accordion headed Our Growth Architecture with the three pillars and their subtitles, Our work, Insights (with Expertise), About, Contact, and the quiet Who we work with block | `docs/01-primary-navigation.md`, section 3.5 |
| Sitemap | Every URL as a tree with weight badges (Canonical, Supporting, Light, Utility) and pillar badges on the three triangle pages | `docs/02-sitemap.md` |

## How to use it

- Hover over or click What we do, Insights or About to open each menu. Hover opens after a short delay and closes after a short delay when the cursor leaves, as specified in the nav doc.
- Press Escape or click outside to close a menu.
- Links do not navigate anywhere. Clicking one shows the URL it would open on the live site.
- In the mobile tab, tap the plus or minus to expand a group and the label text to "navigate". The Menu button opens and closes the panel.
- Tick "Show what changed from v2" in the intro to see the v2 label appended after each renamed item in the mega-nav, mobile menu, footer and sitemap. Untick to see the nav as a visitor would.

## Rules for editing

- Labels, order, subtitles and URLs must match `docs/01-primary-navigation.md` and `docs/02-sitemap.md` exactly. Change the document first, then the mock. A label change is an IA decision: record it in `docs/nav-wording-decisions.md` and `docs/06-decisions-log.md`.
- Every mega-nav item keeps a one-line subtitle of ten words or fewer with at least one searched term in it.
- The mega-nav must stay at three columns plus one footer row. Anything else goes elsewhere in the site.
- Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy.
