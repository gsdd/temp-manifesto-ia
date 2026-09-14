# Manifesto Growth Architects: Website Information Architecture (v1)

This repository holds the Information Architecture (IA) package for the new Manifesto Growth Architects (MGA) website. It is documentation only. There is no website code here and no visual design. The package defines what the site contains, how it is organised, how it is navigated, and which page owns which topic.

## What this package is for

The current MGA site works as a credibility check after a referral. The rebuild has to do more: it has to originate enquiries from people who have never heard of MGA and who arrive through search or a shared link. The IA is designed around the questions a prospective client asks, in order:

1. What can you do for me? (Services)
2. Do you understand my problem? (Expertise themes)
3. Have you worked with businesses like mine? (Sectors, kept light)
4. Prove it. (Work, Insights, Team)

Services are the spine of the site and the canonical home for every capability topic. Expertise themes and sectors are real, navigable dimensions that intersect the services and cross-link into them rather than duplicating them.

## Sources and how conflicts were resolved

| Source | Used for | Precedence |
|---|---|---|
| Source A: Gary IA feedback | Site structure, the three intersecting dimensions, the shape of the sitemap | Wins on structure |
| Source B: Andy services triangle deck (Sept 26 draft) | Service labels, grouping and order | Wins on service taxonomy |
| Source C: Otter call notes, 7 Sept | Weighting (Growth Strategy first, CEO Advisory downweighted, sectors light, Activation is strategy-to-execution) and the origination goal | Wins on weight and emphasis |

Where sources disagree, the decision and the trade-off are recorded in `docs/06-decisions-log.md`.

## How to read the package

Read the documents in number order. Each one builds on the previous.

| File | What it answers | Read it if you are |
|---|---|---|
| `docs/01-primary-navigation.md` | What is in the header, the footer, and every dropdown, including the full What we do mega-nav, with desktop and mobile behaviour | Anyone. Start here. |
| `docs/02-sitemap.md` | Every URL on the site, its page type, its purpose in one line, and its weight (Canonical, Supporting, Light, Utility) | Content, SEO, developers |
| `docs/03-page-layouts.md` | The block-by-block template for each page type, and the rules for when a block appears | Designers, content, developers |
| `docs/04-canonicals-and-seo.md` | Which page owns which topic, how overlaps between services, themes and sectors are resolved, what is indexed, and how pages link to each other | SEO, content, developers |
| `docs/05-content-matrix.md` | Which content types appear on which pages, and whether the page is the primary home for that content or just surfaces it | Content, CMS modelling |
| `docs/06-decisions-log.md` | Every significant IA decision, the alternatives considered, and the trade-off against the Gary three-dimension model and the Andy triangle | Stakeholders reviewing the IA |
| `docs/diagrams/` | Mermaid diagrams of the mega-nav and sitemap for quick visual reference | Anyone who prefers a picture |
| `mocks/index.html` | Interactive greyscale wireframe of the header, mega-nav, dropdowns, mobile menu and sitemap. Open it in a browser; no build step. See `mocks/README.md`. | Stakeholders who want to click through the navigation |

## Terms used throughout

- **Service**: a tangible, buyable offering (for example Growth Strategy, Experience Engineering). Lives under `/services/`.
- **Expertise theme**: a growth problem MGA understands deeply and is known for (loyalty, membership, subscriptions, pricing, customer value). Lives under `/expertise/`. Themes are not services; they point to services.
- **Sector**: an industry grouping used as a proof point and a filter (financial services, media, consumer, retail). Lives under `/sectors/` as light landings only.
- **Methodology / how we work**: MGA's ways of working, frameworks and engagement models. Kept separate from services so that a method is never mistaken for a product.
- **Weight**: how much content and SEO investment a page receives. Defined in `docs/02-sitemap.md`.
- **Canonical page**: the single page that owns a topic. Every other page that mentions the topic links to it instead of restating it.

## What this package deliberately does not cover

- Visual design, typography, colour, imagery or component styling
- Copywriting beyond nav labels, page purposes and example headings
- CMS platform choice or technical build
- Wireframes (these are the next step after this IA is agreed)

## Scope guardrails

- Home is a page, not a hub. Nothing lives under `/` as a child URL.
- Services are canonical. There are no heavy sector point-of-view pages.
- CEO Advisory (Side-by-Side) is included but downweighted in navigation.
- Growth Strategy is the lead service. Activation is strategy-to-execution, not ongoing operations.
- Experience Engineering keeps its label, and the page is written so that people searching for CX, website and research work can find it.
- Brand name and logo are unchanged.
