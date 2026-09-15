# Wireframe mock (v5)

A single self-contained HTML file showing the v5 navigation, homepage, Services hub, mobile menu and sitemap. Greyscale, system font, no brand colours, no imagery, no dependencies. It is a wireframe, not a design.

v4 rebuilt the mock to be as calm as the IA it shows. v5 keeps that and adds one view, the Services hub, because that page is where most of the v5 refinements land (`../docs/v5-refinements.md`). In the menu, the CEO Advisory column has one quiet item and the footer row has two links.

## How to open it

Locally: clone the repository and open `mocks/index.html` in any modern browser. No server, build step or internet connection is needed. From GitHub: use the raw or preview link, or enable GitHub Pages and visit `/mocks/index.html`.

## The two-second test

The page loads on the Navigation view with the What we do menu already open. Without reading anything in grey, name the three pillars: **Growth Strategy**, **Activation Services**, **CEO Advisory**. If that takes longer than two seconds, or you find yourself reading, the mock has failed.

Then switch to the Services hub. Without scrolling, see the name of the system and the three pillars. In the next screen, find your own situation in seven lines.

## The five views

| View | Shows | Source |
|---|---|---|
| Navigation | Desktop header with the mega-nav open: three columns, three short pillar lines, eight service labels, two quiet lines, one quiet "Our advisors" item, a footer row of two links. The About dropdown opens on hover. Our work and Insights are plain links. | `docs/01-primary-navigation.md` |
| Homepage | The same frame with the menu closed: six blocks (hero with logos, triangle with the triangle line, work, one row of expertise links, latest insights, closing CTA) and the footer. | `docs/03-page-layouts.md`, T1 |
| Services hub | The same frame on `/services/`: eyebrow "What we do", H1 "Our Growth Architecture", strapline, triangle with the triangle line, "Where are you starting from?" (seven lines), three pillar sections each with a sentence, its services and one case, the expertise sentence, closing CTA. The triangle blocks scroll to their pillar section. | `docs/03-page-layouts.md`, T2 |
| Mobile | Phone frame with the menu open and What we do expanded: three small pillar labels above a flat list (CEO Advisory now has Our advisors beneath it), then Our work, Insights, About, Contact. Two levels deep. | `docs/01-primary-navigation.md`, section 3.5 |
| Sitemap | Every URL as a plain indented list with its weight in grey. | `docs/02-sitemap.md` |

## How to use it

- Hover or click What we do and About to open them. Escape or clicking outside closes them.
- Links do not navigate. Clicking one writes its URL into the frame's address bar. The exception is the three triangle blocks on the Services hub, which scroll to their section as the live page would.
- In the Mobile view, tap the plus or minus to expand a row and the label text to "navigate". Close and Menu toggle the panel.
- `#nav`, `#home`, `#hub`, `#mobile` or `#sitemap` in the URL opens that view directly.

## Rules for editing

- Labels, order, pillar lines, quiet lines, the triangle line, the seven situation lines and URLs must match `docs/01-primary-navigation.md`, `docs/03-page-layouts.md` and `docs/02-sitemap.md` exactly. Change the document first, then the mock.
- The open mega-nav stays at fifty words or fewer. Adding a subtitle or a link to it is an IA decision to log in `docs/06-decisions-log.md`, and the default answer is no.
- The Services hub stays at eight blocks. Adding a block is an IA decision.
- No chrome that explains the mock: no banners, legends, toggles, notes or toasts. If something needs explaining, explain it in this README.
- Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy. British English.
