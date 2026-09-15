# Wireframe mock (v4)

A single self-contained HTML file showing the v4 navigation, homepage, mobile menu and sitemap. Greyscale, system font, no brand colours, no imagery, no dependencies. It is a wireframe, not a design.

v4 rebuilt the mock to be as calm as the IA it shows. Gone from v3: the striped banner, the intro box, the "show what changed" toggle, the tabs, the behaviour notes, the sitemap legend and badges, the notes beside the phone, and the message on every click. What is left is one line of small text and four plain view switches.

## How to open it

Locally: clone the repository and open `mocks/index.html` in any modern browser. No server, build step or internet connection is needed. From GitHub: use the raw or preview link, or enable GitHub Pages and visit `/mocks/index.html`.

## The two-second test

The page loads on the Navigation view with the What we do menu already open. Without reading anything in grey, name the three pillars: **Growth Strategy**, **Activation Services**, **CEO Advisory**. If that takes longer than two seconds, or you find yourself reading, the mock has failed.

## The four views

| View | Shows | Source |
|---|---|---|
| Navigation | Desktop header with the mega-nav open: three columns, three short pillar lines, seven service labels, two quiet lines, a footer row of three links. The About dropdown opens on hover. Our work and Insights are plain links. | `docs/01-primary-navigation.md` |
| Homepage | The same frame with the menu closed: six blocks (hero with logos, triangle, work, one row of expertise links, latest insights, closing CTA) and the footer. | `docs/03-page-layouts.md`, T1 |
| Mobile | Phone frame with the menu open and What we do expanded: three small pillar labels above a flat list, then Our work, Insights, About, Contact. Two levels deep. | `docs/01-primary-navigation.md`, section 3.5 |
| Sitemap | Every URL as a plain indented list with its weight in grey. | `docs/02-sitemap.md` |

## How to use it

- Hover or click What we do and About to open them. Escape or clicking outside closes them.
- Links do not navigate. Clicking one writes its URL into the frame's address bar.
- In the Mobile view, tap the plus or minus to expand a row and the label text to "navigate". Close and Menu toggle the panel.

## Rules for editing

- Labels, order, pillar lines, quiet lines and URLs must match `docs/01-primary-navigation.md` and `docs/02-sitemap.md` exactly. Change the document first, then the mock.
- The open mega-nav stays under fifty words. Adding a subtitle or a link to it is an IA decision to log in `docs/06-decisions-log.md`, and the default answer is no.
- No chrome that explains the mock: no banners, legends, toggles, notes or toasts. If something needs explaining, explain it in this README.
- Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy. British English.
