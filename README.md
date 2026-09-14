# Manifesto Growth Architects: Website Information Architecture (v2)

This repository holds the Information Architecture (IA) package for the new Manifesto Growth Architects (MGA) website. It is documentation plus one clickable wireframe. There is no website code here and no visual design. The package defines what the site contains, how it is organised, how it is navigated, and which page owns which topic.

**v2 replaces v1 in full.** v1 was rejected on 14 September because the navigation was too complicated and Andy's Growth Architecture triangle was not visible in it. The reasons and the changes are recorded in `docs/06-decisions-log.md`, section "Why v1 was rejected".

## The one idea to hold in your head

The What we do mega-nav **is** Andy's triangle: three columns, nothing else.

| Column 1 | Column 2 | Column 3 (quieter) |
|---|---|---|
| **Growth Strategy** | **Activation Services** | **CEO Advisory** |
| Growth Strategy | Customer Intelligence | Side-by-Side (SxS) |
| Proposition Innovation | Experience Engineering | Meet the advisors |
| | Data Agents | |
| | Operating Architecture | |
| | Growth Office | |
| | AI Enablement | |

Under the columns, one thin row: All services, Expertise themes, Contact. That is the whole panel.

Expertise themes (loyalty, membership, subscriptions, pricing, customer value) are a real, indexable dimension of the site and are cross-linked from every service and case study. In the header they live calmly under Insights. Sectors (financial services, media, consumer, retail) are light landings reached from the footer and filters, not from the header.

## What this package is for

The current MGA site works as a credibility check after a referral. The rebuild has to originate enquiries from people who have never heard of MGA. The IA is designed around the questions a prospective client asks, in order:

1. What can you do for me? (Services: the triangle)
2. Do you understand my problem? (Expertise themes)
3. Have you worked with businesses like mine? (Sectors, kept light)
4. Prove it. (Work, Insights, Team)

Services are the spine of the site and the canonical home for every capability topic. Themes and sectors intersect the services and cross-link into them rather than duplicating them.

## Sources and precedence

| Source | Used for | Wins on |
|---|---|---|
| A: Gary's IA feedback | Site structure, the three intersecting dimensions, one canonical home per topic, About and Careers split | Structure |
| B: Andy's Growth Architecture Services deck (Sept 26 draft) | The triangle, service labels and grouping, Why and What copy per service | Service taxonomy |
| C: Otter call notes, 7 Sept | Order of prominence (Growth Strategy, Activation, CEO Advisory), plain language, sectors light, themes as the expertise story, origination goal | Weight and language |
| D: Gary's direction, 14 Sept | Simplify the mega-nav; make the triangle obvious; CEO Advisory visible as a pillar; themes calm | The mega-nav |

Full summaries of all four are in `docs/00-sources.md`.

## How to read the package

| File | What it answers | Read it if you are |
|---|---|---|
| `mocks/index.html` | The clickable wireframe. Opens with the mega-nav visible so the three pillars are the first thing you see. Desktop, mobile and sitemap tabs. No build step. | Anyone. Start here. |
| `docs/00-sources.md` | What each source said and which one wins where | Anyone checking a decision against its evidence |
| `docs/01-primary-navigation.md` | Every header and footer item, the three-column mega-nav in full, desktop and mobile behaviour | Anyone |
| `docs/02-sitemap.md` | Every URL, its page type, purpose and weight (Canonical, Supporting, Light, Utility) | Content, SEO, developers |
| `docs/03-page-layouts.md` | Block-by-block templates for each page type, including the triangle blocks on Home and the Services hub | Designers, content, developers |
| `docs/04-canonicals-and-seo.md` | Which page owns which topic, how overlaps are resolved, what is indexed, how pages link | SEO, content, developers |
| `docs/05-content-matrix.md` | Content types against pages, and launch minimums | Content, CMS modelling |
| `docs/06-decisions-log.md` | Why v1 was rejected, what v2 changed, and every decision with its sources | Stakeholders reviewing the IA |
| `docs/diagrams/` | Mermaid diagrams of the mega-nav and sitemap | Anyone who prefers a picture |

## Terms used throughout

- **Growth Architecture**: MGA's overarching proposition (Source B). The triangle of Growth Strategy, Activation Services and CEO Advisory. Its page is `/services/`.
- **Pillar**: one of the three sides of the triangle.
- **Service**: a tangible, buyable offering (for example Growth Strategy, Experience Engineering). Lives flat under `/services/`.
- **Expertise theme**: a growth problem MGA understands deeply (loyalty, membership, subscriptions, pricing, customer value). Lives under `/expertise/`. Themes are not services; they point to services.
- **Sector**: an industry grouping used as a proof point and a filter. Lives under `/sectors/` as light landings only.
- **Methodology / how we work**: MGA's ways of working and frameworks (for example CIVD). Kept under About, separate from services.
- **Weight**: how much content and SEO investment a page receives. Defined in `docs/02-sitemap.md`.
- **Canonical page**: the single page that owns a topic. Everything else links to it instead of restating it.

## Scope guardrails

- Home is a page, not a hub. Nothing lives under `/` as a child URL.
- Services are canonical and flat under `/services/`. No heavy sector point-of-view pages.
- The mega-nav shows the triangle and only the triangle, in the order Growth Strategy, Activation Services, CEO Advisory.
- CEO Advisory is visible as the third pillar, quieter than the other two, with advisor profiles behind it.
- Experience Engineering keeps its label and carries a plain-language subtitle so CX, website and research searches find it.
- No em dashes anywhere in the package. British English.
- Brand name and logo are unchanged.

## What this package deliberately does not cover

- Visual design, typography, colour, imagery or component styling
- Copywriting beyond nav labels, subtitles, page purposes and example headings
- CMS platform choice or technical build
- Full wireframes of page bodies (the mock covers navigation and shows page blocks as placeholders)
