# Manifesto Growth Architects: Website Information Architecture (v4)

This repository holds the Information Architecture (IA) package for the new Manifesto Growth Architects (MGA) website. It is documentation plus one wireframe. There is no website code here and no visual design. The package defines what the site contains, how it is organised, how it is navigated, and which page owns which topic.

**v2 replaced v1 in full.** v1 was rejected on 14 September because the navigation was too complicated and Andy's Growth Architecture triangle was not visible in it.

**v3 was a wording pass on v2.** Labels rewritten in plain, search-friendly language; three services renamed to what prospects search for.

**v4 simplifies the whole concept.** Gary's feedback on v3 (15 September, evening) was that it still felt too complicated as a whole: the mega-nav was busy, the page chips were busy, the homepage had too much going on, and the mock was fussy. v4 keeps the structure and the labels and takes out everything that was explaining them. What was cut, why, and where each piece of explanation went is in `docs/v4-simplification.md`.

## The one idea to hold in your head

The What we do menu **is** Andy's triangle: three headings, three short lines, seven service labels, one thin row of links. Nothing else.

| Growth Strategy | Activation Services | CEO Advisory (quieter) |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one advice for senior leaders |
| Proposition Innovation | Customer Research and Insight | |
| | Experience Engineering, *Customer experience and websites* | |
| | AI Agents for Marketing | |
| | Operating Model Design | |
| | Growth Office, *Interim growth team* | |
| | AI Enablement | |

Column headings are the pillar links. Under the columns, one thin row: All services, Expertise, Contact. About 45 words. The v3 panel had about 200.

Everything that explains a service lives on its page: hero line, H2s, title tag. Expertise themes (loyalty, membership, subscriptions, pricing, customer value) are a real, indexable dimension with their own pages and cross-links; in the chrome they appear as one link in the menu's footer row, one row of five names on Home, and a footer column. Sectors are footer, filters and light landings only.

## What this package is for

The current MGA site works as a credibility check after a referral. The rebuild has to originate enquiries from people who have never heard of MGA. The IA is designed around the questions a prospective client asks, in order:

1. What can you do for me? (Services: the triangle)
2. Do you understand my problem? (Expertise themes)
3. Have you worked with businesses like mine? (Sectors, kept light)
4. Prove it. (Work, Insights, Team)

Services are the spine of the site and the canonical home for every capability topic. Themes and sectors intersect the services through tags and links rather than duplicating them, and v4 stops showing that intersection as chips on every page: one dimension per page type, three visible.

## Sources and precedence

| Source | Used for | Wins on |
|---|---|---|
| A: Gary's IA feedback | Site structure, the three intersecting dimensions, one canonical home per topic, About and Careers split | Structure |
| B: Andy's Growth Architecture Services deck (Sept 26 draft) | The triangle, what the services are and how they group, Why and What copy per service | Service taxonomy (not nav wording) |
| C: Otter call notes, 7 Sept | Order of prominence, plain language, sectors light, themes as the expertise story, which coined names need help | Weight and language |
| D: Gary's direction, 14 Sept | Simplify the mega-nav; make the triangle obvious; CEO Advisory visible as a pillar | The mega-nav's shape |
| E: Gary's v3 wording brief, 15 Sept | Search-friendly labels; deck is not website copy | The mega-nav's words |
| F: Gary's v4 feedback, 15 Sept evening | Simplify the whole concept; fewer words; sparse chips; calm homepage; clean mock | How much the chrome may say |

Full summaries of all six are in `docs/00-sources.md`.

## How to read the package

| File | What it answers | Read it if you are |
|---|---|---|
| `mocks/index.html` | The wireframe. Opens with the mega-nav visible. Four plain views: Navigation, Homepage, Mobile, Sitemap. No build step. | Anyone. Start here. |
| `docs/v4-simplification.md` | What v4 cut and why; old to new; where each piece of explanation went; the tests v4 has to pass | Gary and Andy reviewing v4 |
| `docs/00-sources.md` | What each source said and which one wins where | Anyone checking a decision against its evidence |
| `docs/01-primary-navigation.md` | Every header and footer item, the mega-nav in full, desktop and mobile behaviour | Anyone |
| `docs/02-sitemap.md` | Every URL, its page type, purpose and weight (Canonical, Supporting, Light, Utility) | Content, SEO, developers |
| `docs/03-page-layouts.md` | The chip rule, then block-by-block templates for each page type | Designers, content, developers |
| `docs/04-canonicals-and-seo.md` | Which page owns which topic, where the search vocabulary now lives, what is indexed, how pages link | SEO, content, developers |
| `docs/05-content-matrix.md` | Content types against pages, and launch minimums | Content, CMS modelling |
| `docs/06-decisions-log.md` | Why v1 was rejected, why v3 and v4 exist, and every decision (D-01 to D-45) with its sources and fallbacks | Stakeholders reviewing the IA |
| `docs/nav-wording-decisions.md` | Every v2 to v3 label change with its reason, and the v4 status of each | Anyone editing a label |
| `docs/diagrams/` | Mermaid diagrams of the mega-nav and sitemap | Anyone who prefers a picture |

## Terms used throughout

- **Growth Architecture**: MGA's overarching proposition (Source B). The triangle of Growth Strategy, Activation Services and CEO Advisory. Its page is `/services/`.
- **Pillar**: one of the three sides of the triangle. In the menu, a column heading that links to the pillar page.
- **Pillar line**: the short line under each pillar heading (four to six words). Shared by the menu, Home and the Services hub.
- **Quiet line**: the small grey line under Experience Engineering and Growth Office in the menu. The only two.
- **Service**: a tangible, buyable offering. Lives flat under `/services/`.
- **Nav label**: what the site calls a service. Follows what a prospect would search for.
- **Hero line**: the one line under a service page's H1 that carries its searched terms. Where the v3 menu subtitles went.
- **Expertise theme**: a growth problem MGA understands deeply. Lives under `/expertise/`. Shown to visitors as "Expertise".
- **Sector**: an industry grouping used as a proof point and a filter. Four light landings, no index page.
- **Chip**: a small linked tag on a page. Each page type shows chips from one dimension only, three visible.
- **Weight**: how much content and SEO investment a page receives. Defined in `docs/02-sitemap.md`.
- **Canonical page**: the single page that owns a topic.

## Scope guardrails

- Home is a page, not a hub. Six blocks. One row of expertise links, no other tags.
- Services are canonical and flat under `/services/`. No heavy sector point-of-view pages.
- The mega-nav shows the triangle and only the triangle, in the order Growth Strategy, Activation Services, CEO Advisory. Labels, three pillar lines, two quiet lines, three footer links. Under fifty words.
- CEO Advisory is visible as the third pillar, quieter than the other two.
- One header mega-nav, one small dropdown (About). Our work and Insights are plain links.
- One chip dimension per page type, three visible. Sectors are never chips.
- Nav labels use the words prospects search for. No acronyms in the nav.
- No em dashes anywhere in the package. British English.
- Brand name and logo are unchanged.

## What this package deliberately does not cover

- Visual design, typography, colour, imagery or component styling
- Copywriting beyond nav labels, pillar lines, page purposes and example headings
- CMS platform choice or technical build
- Full wireframes of page bodies (the mock covers navigation and the homepage; other pages are specified as block lists)
