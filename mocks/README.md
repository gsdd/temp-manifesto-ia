# Wireframe mock (full-site, extending v5)

A clickable, desktop-first HTML wireframe of the Manifesto Growth Architects site. Greyscale, system font, no brand colours, no imagery, no network dependencies. It is a wireframe, not a design.

This extends the v5 IA (`docs/01-primary-navigation.md`, `docs/02-sitemap.md`, `docs/03-page-layouts.md`). It does not invent a competing IA. Nav labels, strand subtitles, weights and URLs follow the current IA. The header chrome is MURAL-informed (six items: What we do, Our work, Our thinking, About, Careers, Contact) without adopting the old sitemap. See `docs/mural-gap-check.md`. UK keyword intel (DataForSEO, Sep 2026) is applied in strand subtitles, H1/H2/H3s and page notes, not as extra top-nav items.

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
4. Every sitemap URL is a real HTML page. **All pages** in the sidebar opens `sitemap.html`. **Component library** opens the wireframe catalogue at `catalogue/`.
5. The **main column** is the page canvas: header, breadcrumb, the page's components with scant placeholder copy, cookie bar, footer. The **sidebar** on every page except the catalogue holds the page fundamentals and the component inventory (see below).

From GitHub: use the preview or raw HTML, or enable GitHub Pages and visit `/mocks/index.html`.

## What you should see in two seconds

Home loads with the menu closed. Open **What we do**. Without reading anything in grey, name the three pillars: **Growth Strategy**, **Activation Services**, **CEO Advisory**. All three headings use the same ink. If that takes longer than two seconds, the mock has failed.

Then go to **All services**. Without scrolling, see **Our Growth Architecture** and the three pillars. In the next screen, find your own situation in seven lines.

## What is in the mega-nav (hub titles + strands)

Three columns, in call order, plus a thin footer row. Group titles are linked hubs with a trailing arrow. Growth Strategy and Activation start with Overview. CEO Advisory shows both strands at full visual weight. Every strand has a short subtitle.

| Growth Strategy | Activation Services | CEO Advisory |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one support for leaders |
| Overview *Where to grow and how to win* | Overview *Hands-on delivery, six services* | Side-by-Side *One-to-one advisory retainer* |
| Proposition Innovation *Value proposition design* | Customer Research and Insight *Research methods and journey mapping* | Our advisors *Experienced growth leaders* |
| | Experience Engineering *Customer experience and websites* | |
| | AI Agents for Marketing *AI marketing agents, guided by experts* | |
| | Operating Model Design *Target operating model* | |
| | Growth Office *Interim growth team* | |
| | AI Enablement *AI skills and adoption* | |

Footer row: All services | Expertise | Our work. Contact is not repeated (the header button already does that). Deck one-liners and the AgentLab catalogue are not in the menu.

## Pages included

Home; Services hub; Growth Strategy; Proposition Innovation; Activation group and the six activation services; CEO Advisory (Side-by-Side + Our advisors); Expertise hub and Loyalty / Membership / Subscriptions / Pricing / Customer Value; four light sectors (Financial Services, Media, Consumer, Retail); Work hub plus Dayinsure and Key Group shells; Our thinking hub plus one article and one report shell; About (story, Our people, Our approach, values); Careers (Life at Manifesto + one role shell); Contact (work with us / work for us, plus thank-you); The Nutshell and legal / 404 / search utilities so every footer link resolves; the **Component library** (`catalogue/`) as a wireframe-only index of the reusable blocks.

## Sidebar: page fundamentals and components

The sidebar is annotation for this wireframe. Nothing in it is a live component. It has two panels in one visual language (small grey label, plain value):

- **Page fundamentals**: URL; template and weight, with the weight explained in plain English; H1; keywords (primary target with UK monthly volume where the pull has it, then two to four alts); menu subtitle where the page has one; H2s in order; H3s where useful; intent (what the page is for, one or two sentences); content notes, present tense, only where they change what a designer builds; and the pages this one links to. The same content is consolidated in `docs/heading-map.md`.
- **Components on this page**: an inventory of the reusable blocks on the canvas, in order, with a count where a block repeats (Offer card ×6) and the block heading on the right. The list is generated from the canvas itself: every component in the HTML carries `data-module="<name>"` and the builder reads those back, so the sidebar cannot disagree with the page. Hover any block on the canvas to see its name.

## Components

Every block on every page is one of the named components in the **Component library** (`catalogue/`): one name, one shape, one interaction type. The seven interaction types are Band, Button, Text link, Card, Tag, Filter and Static. Cards are visually distinct by type: Offer card (grey fill), Theme card and Role card (outline; Role has a top rule), Article card (no fill, no image), Case card (image placeholder), Report card (portrait document), Person card (avatar). Tags are small squared labels; filters are pills; pagination is numbered squares; buttons are 1.5px outlined. The library is generated from the same vocabulary the pages use, and the build fails if a page names a component the library does not have.

Keyword rules applied here: Manifesto labels stay in the nav (Proposition Innovation, Experience Engineering, Growth Office, CEO Advisory). Buyer language is in strand subtitles and on the page. AI phrases stay marketing-qualified. Growth Office SEO is interim / embedded growth team (interim CMO where accurate), not "growth office" as primary.

## Regenerating

Pages, the component library, `sitemap.html` and `docs/heading-map.md` are all generated from `mocks/_build.py` so they cannot drift. The page registry (`PAGES`) holds the fundamentals; `COMPONENTS` holds the vocabulary; `body_for()` lays out each template from the shared component helpers.

```
python3 mocks/_build.py
```

Shared CSS and JS live in `mocks/assets/`. Do not edit generated `index.html` files by hand; change the builder.

## Rules for editing

- Labels, order, pillar lines, strand subtitles, the triangle line, the seven situation lines and URLs must match `docs/01-primary-navigation.md`, `docs/03-page-layouts.md` and `docs/02-sitemap.md`. Change the document first, then the builder.
- The open mega-nav keeps the triangle. Adding a sold-service link to it is an IA decision to log in `docs/06-decisions-log.md`. Overview rows, full-weight CEO Advisory, and all-strand subtitles are the current pattern (D-54, D-57, D-58).
- No visual brand redesign. Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy. British English.
