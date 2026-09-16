# Wireframe mock (full-site, extending v5)

A clickable, desktop-first HTML wireframe of the Manifesto Growth Architects site. Greyscale, system font, no brand colours, no imagery, no network dependencies. It is a wireframe, not a design.

This extends the v5 IA (`docs/01-primary-navigation.md`, `docs/02-sitemap.md`, `docs/03-page-layouts.md`). It does not invent a competing IA. Nav labels in the mega-nav, quiet lines, weights and URLs follow v5. The header chrome is MURAL-informed (six items: What we do, Our work, Our thinking, About, Careers, Contact) without adopting the old sitemap. See `docs/mural-gap-check.md`. UK keyword intel (DataForSEO, Sep 2026) is applied in quiet lines, H1/H2/H3s and page chips, not as extra top-nav items.

## How to click through

1. Clone the repository.
2. Open `mocks/index.html` in any modern browser. No server, build step or internet connection is needed. (A local server is fine if you prefer: `python3 -m http.server` from `mocks/`.)
3. Use the primary nav as you would on the live site:
   - **Logo** returns to Home.
   - **What we do** opens the mega-nav on hover (three columns plus a footer row). The label itself goes to `/services/`.
   - **Our work** is a plain link.
   - **Our thinking** opens a small dropdown (Reports, Articles, Events and news, All thinking). The label goes to `/insights/`.
   - **About** opens a small dropdown (Our people, Our approach, Values and culture). The label goes to `/about/`.
   - **Careers** is a plain first-class link.
   - **Contact** is the header button.
4. Every sitemap URL is a real HTML page. The top-right **All pages** link opens `sitemap.html`, a clickable index.
5. Each page has **page chips** (weight, primary keyword with UK volume when known, quiet line if any, related themes / sectors / services) and, where a MURAL keep/drop note landed, a second row of **MURAL modules**. An **Outside page / SEO heading map** panel sits to the right (below the frame on smaller screens).

From GitHub: use the preview or raw HTML, or enable GitHub Pages and visit `/mocks/index.html`.

## What you should see in two seconds

Home loads with the menu closed. Open **What we do**. Without reading anything in grey, name the three pillars: **Growth Strategy**, **Activation Services**, **CEO Advisory**. If that takes longer than two seconds, the mock has failed.

Then go to **All services**. Without scrolling, see **Our Growth Architecture** and the three pillars. In the next screen, find your own situation in seven lines.

## What is in the mega-nav (unchanged from v5)

Three columns, in call order, plus a thin footer row. About 50 words. Thirteen links.

| Growth Strategy | Activation Services | CEO Advisory (quieter) |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one support for leaders |
| Proposition Innovation | Customer Research and Insight | Our advisors |
| | Experience Engineering, *Customer experience and websites* | |
| | AI Agents for Marketing | |
| | Operating Model Design | |
| | Growth Office, *Interim growth team* | |
| | AI Enablement | |

Footer row: All services | Expertise. Contact is not repeated (the header button already does that). Deck one-liners and the AgentLab catalogue are not in the menu.

## Pages included

Home; Services hub; Growth Strategy; Proposition Innovation; Activation group and the six activation services; CEO Advisory (Side-by-Side + Our advisors); Expertise hub and Loyalty / Membership / Subscriptions / Pricing / Customer Value; four light sectors (Financial Services, Media, Consumer, Retail); Work hub plus Dayinsure and Key Group shells; Our thinking hub plus one article and one report shell; About (story, Our people, Our approach, values); Careers (Life at Manifesto + one role shell); Contact (work with us / work for us, plus thank-you); The Nutshell and legal / 404 / search utilities so every footer link resolves.

## Page chips and the heading map

- **Page chips** are an IA annotation, not the live-site chip rule in `docs/03-page-layouts.md`. They always show canonical weight, the primary keyword target (with UK monthly volume when this pull has it), the quiet line if the page has one, and related themes / sectors / services. A second row lists MURAL modules when that page absorbed a keep/drop note.
- **Outside page / SEO heading map** lists the recommended H1 (one), H2s in order, H3s where useful, primary keyword, two to four alts, and a one-line intent note. It is not body copy. The same content is consolidated in `docs/heading-map.md`.

Keyword rules applied here: Manifesto labels stay in the nav (Proposition Innovation, Experience Engineering, Growth Office, CEO Advisory). Buyer language is on the page. AI phrases stay marketing-qualified. Growth Office SEO is interim / embedded growth team (interim CMO where accurate), not "growth office" as primary.

## Regenerating

Pages are generated from `mocks/_build.py` so HTML and `docs/heading-map.md` cannot drift.

```
python3 mocks/_build.py
```

Shared CSS and JS live in `mocks/assets/`. Do not edit generated `index.html` files by hand; change the builder.

## Rules for editing

- Labels, order, pillar lines, quiet lines, the triangle line, the seven situation lines and URLs must match `docs/01-primary-navigation.md`, `docs/03-page-layouts.md` and `docs/02-sitemap.md`. Change the document first, then the builder.
- The open mega-nav stays at fifty words or fewer. Adding a subtitle or a link to it is an IA decision to log in `docs/06-decisions-log.md`, and the default answer is no.
- No visual brand redesign. Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy. British English.
