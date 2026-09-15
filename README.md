# Manifesto Growth Architects: Website Information Architecture (v5)

This repository holds the Information Architecture (IA) package for the new Manifesto Growth Architects (MGA) website. It is documentation plus one wireframe. There is no website code here and no visual design. The package defines what the site contains, how it is organised, how it is navigated, and which page owns which topic.

**v2 replaced v1 in full.** v1 was rejected on 14 September because the navigation was too complicated and Andy's Growth Architecture triangle was not visible in it.

**v3 was a wording pass on v2.** Labels rewritten in plain, search-friendly language; three services renamed to what prospects search for.

**v4 simplified the whole concept.** Gary's feedback on v3 was that it still felt too complicated as a whole. v4 kept the structure and the labels and took out everything that was explaining them (`docs/v4-simplification.md`).

**v5 takes the pages to best in class on evidence.** Gary's feedback on v4 (16 September) was that the navigation was calm but not yet best in class, and that Andy's deck might not be fully reflected. v5 reviewed the live navigation of ten real peers and six pattern references (`docs/competitor-nav-review.md`), audited the deck slide by slide (`docs/andy-deck-coverage.md`), and made eight refinements (`docs/v5-refinements.md`). The finding: the menu was already sparser than any peer's; the gap was on the pages. So v5 rebuilds the Services hub as the Growth Architecture story with a way in by problem, puts proof under each offer, names the system and its frameworks where a buyer can see them, and adds exactly one quiet link to the menu.

## The one idea to hold in your head

The What we do menu **is** Andy's triangle: three headings, three short lines, seven service labels, one quiet advisors link, one thin row of links. Nothing else.

| Growth Strategy | Activation Services | CEO Advisory (quieter) |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one support for leaders |
| Proposition Innovation | Customer Research and Insight | Our advisors |
| | Experience Engineering, *Customer experience and websites* | |
| | AI Agents for Marketing | |
| | Operating Model Design | |
| | Growth Office, *Interim growth team* | |
| | AI Enablement | |

Column headings are the pillar links. Under the columns, one thin row: All services, Expertise. Fifty words. The v3 panel had about 200; Prophet's has about 25 links and Elixirr's about 60 against our 13.

The menu opens onto `/services/`, whose H1 is **Our Growth Architecture**. That page says how the three pillars connect ("Strategy first. Activation to deliver it. Advisors alongside."), lets a visitor find their own situation in seven lines, and gives each pillar a plain sentence, its services and one proof. Everything that explains a service lives on its page: three situations, hero line, H2s, proof directly under the offer, the people who lead it. Expertise themes (loyalty, membership, subscriptions, pricing, customer value) are a real, indexable dimension with their own pages and cross-links; in the chrome they appear as one link in the menu's footer row, one row of five names on Home, and a footer column. Sectors are footer, filters and light landings only.

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
| G: Gary's v5 brief, 16 Sept | Best in class on competitor evidence; full deck fidelity; no deck copy in the mega-nav | Where the pages go beyond the peer set |

Full summaries of all seven are in `docs/00-sources.md`. The competitor review is cited as evidence for G, not as a source of its own.

## How to read the package

| File | What it answers | Read it if you are |
|---|---|---|
| `mocks/index.html` | The wireframe. Opens with the mega-nav visible. Five plain views: Navigation, Homepage, Services hub, Mobile, Sitemap. No build step. | Anyone. Start here. |
| `docs/v5-refinements.md` | What v5 changes and why, with the competitor and deck evidence for each; old to new; the tests v5 has to pass | Gary and Andy reviewing v5 |
| `docs/competitor-nav-review.md` | How ten real peers and six pattern references structure nav, services and IA; what is best in class; what to avoid; a patterns table against v4 | Anyone asking "is this best in class?" |
| `docs/andy-deck-coverage.md` | Every element of Andy's deck, slide by slide: Present, Partial or Missing in the IA, and where v5 puts it | Andy, and Gary checking the deck is reflected |
| `docs/v4-simplification.md` | What v4 cut and why; old to new; where each piece of explanation went | Anyone tracing why the chrome is so sparse |
| `docs/00-sources.md` | What each source said and which one wins where | Anyone checking a decision against its evidence |
| `docs/01-primary-navigation.md` | Every header and footer item, the mega-nav in full, desktop and mobile behaviour | Anyone |
| `docs/02-sitemap.md` | Every URL, its page type, purpose and weight (Canonical, Supporting, Light, Utility) | Content, SEO, developers |
| `docs/03-page-layouts.md` | The chip rule, then block-by-block templates for each page type | Designers, content, developers |
| `docs/04-canonicals-and-seo.md` | Which page owns which topic, where the search vocabulary now lives, what is indexed, how pages link | SEO, content, developers |
| `docs/05-content-matrix.md` | Content types against pages, and launch minimums | Content, CMS modelling |
| `docs/06-decisions-log.md` | Why v1 was rejected, why v3, v4 and v5 exist, and every decision (D-01 to D-53) with its sources and fallbacks | Stakeholders reviewing the IA |
| `docs/nav-wording-decisions.md` | Every v2 to v3 label change with its reason, the v4 status of each, and what competitors call the same thing | Anyone editing a label |
| `docs/diagrams/` | Mermaid diagrams of the mega-nav and sitemap | Anyone who prefers a picture |

## Terms used throughout

- **Growth Architecture**: MGA's overarching proposition (Source B). The triangle of Growth Strategy, Activation Services and CEO Advisory. Its page is `/services/`.
- **Pillar**: one of the three sides of the triangle. In the menu, a column heading that links to the pillar page.
- **Pillar line**: the short line under each pillar heading (four to six words). Shared by the menu, Home and the Services hub.
- **Triangle line**: the one sentence under the three pillar blocks on Home and the Services hub that says how the pillars connect. Shared data.
- **Quiet line**: the small grey line under Experience Engineering and Growth Office in the menu. The only two.
- **Situation line**: a one-line problem in the visitor's words that links to the service that answers it. Seven on the Services hub, three at the top of each service page.
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
- The mega-nav shows the triangle and only the triangle, in the order Growth Strategy, Activation Services, CEO Advisory. Labels, three pillar lines, two quiet lines, one quiet advisors link, two footer links. Fifty words or fewer.
- CEO Advisory is visible as the third pillar, quieter than the other two.
- The Services hub is the Growth Architecture story: name the system, connect the pillars, offer a way in by problem, put proof under each pillar. It is not a menu on a page.
- Deck copy goes on pages, not in the menu. Named frameworks (Growth Architecture, CIVD, Operating Architecture, AgentLab, Side-by-Side) have anchored homes and are listed once on How we work.
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
