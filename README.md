# Manifesto Growth Architects: Website Information Architecture (v5)

This repository holds the Information Architecture (IA) package for the new Manifesto Growth Architects (MGA) website. It is documentation plus a clickable full-site wireframe. There is no production website code here and no visual design. The package defines what the site contains, how it is organised, how it is navigated, and which page owns which topic.

**v2 replaced v1 in full.** v1 was rejected on 14 September because the navigation was too complicated and Andy's Growth Architecture triangle was not visible in it.

**v3 was a wording pass on v2.** Labels rewritten in plain, search-friendly language; three services renamed to what prospects search for.

**v4 simplified the whole concept.** Gary's feedback on v3 was that it still felt too complicated as a whole. v4 kept the structure and the labels and took out everything that was explaining them (`docs/v4-simplification.md`).

**v5 takes the pages to best in class on evidence.** Gary's feedback on v4 (16 September) was that the navigation was calm but not yet best in class, and that Andy's deck might not be fully reflected. v5 reviewed the live navigation of ten real peers and six pattern references (`docs/competitor-nav-review.md`), audited the deck slide by slide (`docs/andy-deck-coverage.md`), and made eight refinements (`docs/v5-refinements.md`). The finding: the menu was already sparser than any peer's; the gap was on the pages. So v5 rebuilds the Services hub as the Growth Architecture story with a way in by problem, puts proof under each offer, names the system and its frameworks where a buyer can see them, and adds exactly one quiet link to the menu.

**This pass does not replace the v5 IA.** It extends the v5 mock into a clickable full-site wireframe covering the sitemap, with page notes, heading maps, and UK keyword intel (`docs/heading-map.md`, `docs/keyword-findings.md`). A MURAL pass folded current-site labels and keep/drop modules into the chrome (six header items, Our thinking, Careers first-class) without adopting the old sitemap. This pass: makes mega-nav group titles obvious hubs; treats CEO Advisory as a full-weight pillar; puts a keyword-led subtitle under every strand; moves Our thinking up the homepage; indexes live **page modules** (not working notes) at `/catalogue/`; fills footer, forms, listing states and utility stubs. See `docs/thinking-placement.md` and `docs/strand-gap-check.md`. The client-facing recommendations are in `docs/client-report-andy.md`.

## The one idea to hold in your head

The What we do menu **is** Andy's triangle: three linked hub headings (each with a trailing arrow), three short lines, Overview rows on Growth Strategy and Activation, seven service labels, two CEO Advisory strands (Side-by-Side, Our advisors), one thin row of links. Nothing else.

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

Column headings are the pillar hubs. Under the columns, one thin row: All services, Expertise, Our work. Hub rows (Overview) make the group titles obviously clickable. CEO Advisory is full visual weight (same contrast as the other pillars). The v3 panel had about 200; Prophet's has about 25 links and Elixirr's about 60 against our panel.

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
| `mocks/index.html` | Clickable full-site wireframe. Home is the entry. Primary nav, mega-nav and footer work on every sitemap page. Each page has a sidebar with its fundamentals (URL, H1, keywords, ordered H2s and H3s, intent, content notes) and an inventory of the components on the canvas (the component library has no sidebar). | Anyone. Start here. |
| `mocks/README.md` | How to click through locally, what is in the mega-nav, how to regenerate | Anyone opening the mock |
| `docs/client-report-andy.md` | Client-facing IA recommendations report | Client review |
| `docs/keyword-findings.md` | UK DataForSEO volumes (16 Sep 2026) used for strand subtitles and H2s | SEO, content |
| `docs/heading-map.md` | Recommended H1 / H2 / H3 plus UK keyword targets for every URL | SEO, content |
| `docs/thinking-placement.md` | Why Latest thinking moved up the homepage | Gary reviewing Home |
| `docs/strand-gap-check.md` | Old IA columns and early Home / Services wireframes vs current IA, especially CIVD and Side-by-Side | Gary and Andy checking missed strands |
| `docs/mural-gap-check.md` | What the MURAL board added to nav, page notes and headings; what was left out; open questions | Reviewing the wireframe chrome |
| `docs/v5-refinements.md` | What v5 changes and why, with the competitor and deck evidence for each; old to new; the tests v5 has to pass | Gary and Andy reviewing v5 |
| `docs/competitor-nav-review.md` | How ten real peers and six pattern references structure nav, services and IA; what is best in class; what to avoid; a patterns table against v4 | Anyone asking "is this best in class?" |
| `docs/andy-deck-coverage.md` | Every element of Andy's deck, slide by slide: Present, Partial or Missing in the IA, and where v5 puts it | Andy, and Gary checking the deck is reflected |
| `docs/v4-simplification.md` | What v4 cut and why; old to new; where each piece of explanation went | Anyone tracing why the chrome is so sparse |
| `docs/00-sources.md` | What each source said and which one wins where | Anyone checking a decision against its evidence |
| `docs/01-primary-navigation.md` | Every header and footer item, the mega-nav in full, desktop and mobile behaviour | Anyone |
| `docs/02-sitemap.md` | Every URL, its page type, purpose and weight (Canonical, Supporting, Light, Utility) | Content, SEO, developers |
| `docs/03-page-layouts.md` | The on-page tag rule, then block-by-block templates for each page type | Designers, content, developers |
| `docs/04-canonicals-and-seo.md` | Which page owns which topic, where the search vocabulary now lives, what is indexed, how pages link | SEO, content, developers |
| `docs/05-content-matrix.md` | Content types against pages, and launch minimums | Content, CMS modelling |
| `docs/06-decisions-log.md` | Why v1 was rejected, why later versions exist, and every decision (D-01 to D-59) with sources and fallbacks | Stakeholders reviewing the IA |
| `docs/nav-wording-decisions.md` | Every v2 to v3 label change with its reason, the v4 status of each, and what competitors call the same thing | Anyone editing a label |
| `docs/diagrams/` | Mermaid diagrams of the mega-nav and sitemap | Anyone who prefers a picture |

## Terms used throughout

- **Growth Architecture**: MGA's overarching proposition (Source B). The triangle of Growth Strategy, Activation Services and CEO Advisory. Its page is `/services/`.
- **Pillar**: one of the three sides of the triangle. In the menu, a column heading that links to the pillar page.
- **Pillar line**: the short line under each pillar heading (four to six words). Shared by the menu, Home and the Services hub.
- **Triangle line**: the one sentence under the three pillar blocks on Home and the Services hub that says how the pillars connect. Shared data.
- **Strand subtitle**: the short line under every mega-nav strand. Keyword-led, human-readable. Not a rename of the Manifesto label.
- **Situation line**: a one-line problem in the visitor's words that links to the service that answers it. Seven on the Services hub, three at the top of each service page.
- **Service**: a tangible, buyable offering. Lives flat under `/services/`.
- **Nav label**: what the site calls a service. Follows what a prospect would search for.
- **Hero line**: the one line under a service page's H1 that carries its searched terms.
- **Expertise theme**: a growth problem MGA understands deeply. Lives under `/expertise/`. Shown to visitors as "Expertise".
- **Sector**: an industry grouping used as a proof point and a filter. Four light landings, no index page.
- **On-page tag**: a small linked tag on a page. Each page type shows tags from one dimension only, three visible. Do not call these chips in UI copy.
- **Page module / block**: a live content unit (card, logo row, quote, video, form, empty state). Indexed at `mocks/catalogue/`.
- **Weight**: how much content and SEO investment a page receives. Defined in `docs/02-sitemap.md`.
- **Canonical page**: the single page that owns a topic.

## Scope guardrails

- Home is a page, not a hub. Six blocks. One row of expertise links, no other tags.
- Services are canonical and flat under `/services/`. No heavy sector point-of-view pages.
- The mega-nav shows the triangle and only the triangle, in the order Growth Strategy, Activation Services, CEO Advisory. Group titles are linked hubs. Growth Strategy and Activation start with Overview. CEO Advisory shows Side-by-Side and Our advisors at full visual weight. Labels, three pillar lines, a strand subtitle under every strand, footer row (All services, Expertise, Our work).
- Home places Our thinking after the triangle, not as a strip at the foot (`docs/thinking-placement.md`).
- Reusable components are indexed in the component library at `mocks/catalogue/` (wireframe utility, not a live URL). Every page sidebar lists its components by the same names.
- CEO Advisory is visible as the third pillar, full contrast, slightly narrower column.
- The Services hub is the Growth Architecture story: name the system, connect the pillars, offer a way in by problem, put proof under each pillar. It is not a menu on a page.
- Deck copy goes on pages, not in the menu. Named frameworks (Growth Architecture, CIVD, Operating Architecture, AgentLab, Side-by-Side) have anchored homes and are listed once on How we work.
- One header mega-nav, one small dropdown for About, and (in the MURAL-informed mock) a type dropdown on Our thinking. Careers is first-class in the mock so Contact can split work-with-us / work-for-us. The v5 spec tables in `docs/01-primary-navigation.md` are unchanged until that chrome is signed (`docs/mural-gap-check.md`).
- One tag dimension per page type, three visible. Sectors are never tags.
- Nav labels use the words prospects search for. No acronyms in the nav.
- No em dashes anywhere in the package. British English.
- Brand name and logo are unchanged.

## What this package deliberately does not cover

- Visual design, typography, colour, imagery or component styling
- Copywriting beyond nav labels, pillar lines, page purposes, example headings and the SEO heading map
- CMS platform choice or technical build
- Visual design of the live site (the mock is greyscale wireframe only)
