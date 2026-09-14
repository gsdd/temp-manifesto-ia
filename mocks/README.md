# Navigation wireframe mock

A single self-contained HTML file that shows the navigation and sitemap from the IA documents so stakeholders can see the structure without reading markdown. It is a wireframe: grey boxes, system font, no brand colours, no imagery. It is not a design.

## How to open it

Option 1, locally: download or clone the repository and double-click `mocks/index.html`. It opens in any modern browser. No server, build step or internet connection is needed.

Option 2, from GitHub: open `mocks/index.html` in the GitHub file view and use the raw or preview link, or enable GitHub Pages on the branch and visit `/mocks/index.html`.

## What it contains

Three tabs at the top of the page:

| Tab | Shows | Source document |
|---|---|---|
| Desktop navigation | The five-item header, the What we do mega-nav (four columns plus bottom strip), the Our work, Insights and About dropdowns, Contact as a button, the Home page block order as grey placeholders, and the footer | `docs/01-primary-navigation.md`, `docs/03-page-layouts.md` (T1) |
| Mobile navigation | A phone frame with the collapsed header and the full-screen menu: What we do as a nested accordion, Our work filters, Insights, About, Contact, and the quiet Who we work with block | `docs/01-primary-navigation.md`, section 3.5 |
| Sitemap | Every URL as a tree with weight badges (Canonical, Supporting, Light, Utility) | `docs/02-sitemap.md` |

## How to use it

- Hover over or click What we do, Our work, Insights or About to open each menu. Hover opens after a short delay and closes after a short delay when the cursor leaves, as specified in the nav doc.
- Press Escape or click outside to close a menu.
- Links do not navigate anywhere. Clicking one shows the URL it would open on the live site.
- In the mobile tab, tap the plus or minus to expand a group and the label text to "navigate". The Menu button opens and closes the panel.

## Rules for editing

- Labels, order and URLs must match `docs/01-primary-navigation.md` and `docs/02-sitemap.md` exactly. Change the document first, then the mock.
- Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy.
