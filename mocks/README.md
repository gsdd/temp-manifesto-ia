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
4. Every sitemap URL is a real HTML page. **All pages** in the heading map opens `sitemap.html`. **Page modules** opens the wireframe catalogue.
5. The **main column** is the page layout (hero, modules, footer). Supplementary IA lives in the **sidebar** on most pages: working notes (weight, primary keyword, strand subtitle, related themes / sectors / services, MURAL modules) plus the **heading map**. The catalogue page has no sidebar.

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

Home; Services hub; Growth Strategy; Proposition Innovation; Activation group and the six activation services; CEO Advisory (Side-by-Side + Our advisors); Expertise hub and Loyalty / Membership / Subscriptions / Pricing / Customer Value; four light sectors (Financial Services, Media, Consumer, Retail); Work hub plus Dayinsure and Key Group shells; Our thinking hub plus one article and one report shell; About (story, Our people, Our approach, values); Careers (Life at Manifesto + one role shell); Contact (work with us / work for us, plus thank-you); The Nutshell and legal / 404 / search utilities so every footer link resolves; **Page modules** (`catalogue/`) as a wireframe-only index of live blocks.

## Page notes, heading map and on-page shapes

- **Working notes** (sidebar) are an IA annotation, not the live-site tag rule in `docs/03-page-layouts.md`. They show canonical weight, the primary keyword target (with UK monthly volume when this pull has it), the strand subtitle if the page has one, and related themes / sectors / services. A Modules row lists MURAL keep/drop notes when that page absorbed one.
- **Heading map** (sidebar) lists the recommended H1 (one), H2s in order, H3s where useful, primary keyword, two to four alts, and a one-line intent note. It is not body copy. The same content is consolidated in `docs/heading-map.md`.
- **On-page modules** in the main column use named shapes: service cards, case cards, article cards, person cards, triangle tiles, logo strips, quotes, 16:9 video, metric boxes, CIVD cells (static, dashed), tags, filter buttons, empty states, pagination links, forms. See **Page modules** (`catalogue/`) for the six interaction types (Button, Text link, Card, Tag, Filter, Static). Related-theme tags that would appear on the live page stay in the body as page tags, not as working notes.

Keyword rules applied here: Manifesto labels stay in the nav (Proposition Innovation, Experience Engineering, Growth Office, CEO Advisory). Buyer language is in strand subtitles and on the page. AI phrases stay marketing-qualified. Growth Office SEO is interim / embedded growth team (interim CMO where accurate), not "growth office" as primary.

## Regenerating

Pages are generated from `mocks/_build.py` so HTML and `docs/heading-map.md` cannot drift.

```
python3 mocks/_build.py
```

Shared CSS and JS live in `mocks/assets/`. Do not edit generated `index.html` files by hand; change the builder.

## Rules for editing

- Labels, order, pillar lines, strand subtitles, the triangle line, the seven situation lines and URLs must match `docs/01-primary-navigation.md`, `docs/03-page-layouts.md` and `docs/02-sitemap.md`. Change the document first, then the builder.
- The open mega-nav keeps the triangle. Adding a sold-service link to it is an IA decision to log in `docs/06-decisions-log.md`. Overview rows, full-weight CEO Advisory, and all-strand subtitles are the current pattern (D-54, D-57, D-58).
- No visual brand redesign. Keep it greyscale and dependency-free: no external CSS, JavaScript, fonts or images.
- No em dashes in any copy. British English.
