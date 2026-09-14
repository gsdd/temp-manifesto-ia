# 04. Canonicals and SEO

Which page owns which topic, how the overlaps between services, expertise themes and sectors are resolved, what is and is not indexed, and how pages link to one another. The aim is a site that originates enquiries from search, not just one that confirms credibility after a referral.

Related: weights are defined in `02-sitemap.md`. The "Related" blocks referenced here are specified in `03-page-layouts.md`.

---

## 1. The core rule: services are the spine

Every capability topic has exactly one canonical page, and that page lives under `/services/`.

| Rule | Detail |
|---|---|
| One topic, one URL | A capability (what MGA does) is described fully in one place only. Other pages may mention it in a sentence and must link to it. |
| Services own "how" | Any content that explains how MGA delivers something (scope, phases, deliverables, tooling) belongs on a service page. |
| Themes own "why and what" | Expertise pages explain the problem, MGA's view of it, and the outcome. They hand off to services for the how. |
| Sectors own nothing | Sector pages hold a short intro and aggregate proof. They do not own any topic. |
| Methodology is not a service | Frameworks and ways of working are described once at `/about/how-we-work/`. Service pages reference and link to them. |
| Home owns nothing | Home is a router. Its copy is a summary of pages that exist elsewhere. |

Consequence for search: internal links, structured data and metadata all push authority toward the eleven Canonical pages (Home, Services hub, eight service details, Work hub). Every Supporting and Light page links up to at least one of them.

---

## 2. Topic ownership map

The canonical home for each topic cluster, and the pages that may reference but not own it.

| Topic cluster | Canonical owner | May reference (with link) | Must not have own page |
|---|---|---|---|
| Growth strategy, customer-led growth strategy, growth consultancy | `/services/growth-strategy/` | Home, About, all theme pages, case studies | Any theme or sector variant such as "growth strategy for retail" |
| Proposition design, proposition innovation, new proposition development, CIVD | `/services/proposition-innovation/` | Growth Strategy page, How we work (framework explanation only) | A separate CIVD page |
| Strategy activation, strategy to execution | `/services/activation/` (group) | Home, Services hub, all activation services | |
| Customer intelligence, customer insight, segmentation, customer research | `/services/customer-intelligence/` | Experience Engineering (research for design), Customer Value theme | A separate research service page |
| Experience engineering, customer experience design, CX consultancy, website design and build, digital product design, user research, usability testing | `/services/experience-engineering/` | Customer Intelligence (for analytical research), case studies | Separate CX, UX, website or research pages. All of these are H2 sections of this page. |
| Data agents, AI agents for marketing and data, AgentLab, marketing automation agents, attribution, CDP clean-up, tagging | `/services/data-agents/` | AI Enablement, Operating Architecture, How we work | Individual agent pages in v1; `/agentlab/` as a page (redirect only) |
| Operating model, operating architecture, adaptive operating model, value streams | `/services/operating-architecture/` | Growth Office, AI Enablement | |
| Interim growth leadership, growth office, embedded growth team, fractional CMO or CGO | `/services/growth-office/` | Operating Architecture, CEO Advisory | |
| AI enablement, AI adoption, AI value cases, AI business model innovation | `/services/ai-enablement/` | Data Agents, Operating Architecture | A generic "AI" page |
| CEO advisory, side-by-side advisory, executive advisor retainer | `/services/ceo-advisory/` | Team profiles flagged as advisor, Growth Office | |
| Loyalty strategy, loyalty programme design, loyalty economics | `/expertise/loyalty/` | Services (as related theme), case studies, insights, sectors | `/services/loyalty/`, `/sectors/retail/loyalty/` |
| Membership models, member economics | `/expertise/membership/` | As above | |
| Subscription growth, churn, retention | `/expertise/subscriptions/` | As above | |
| Pricing strategy, value-based pricing | `/expertise/pricing/` | As above | |
| Customer lifetime value, customer value management | `/expertise/customer-value/` | Customer Intelligence (analytics), Growth Strategy | |
| Financial services, media, consumer, retail (as "consultancy for X" queries) | `/sectors/{sector}/` (Light, no keyword targets) | Case studies, Home logo strip | Sector points of view, sector-specific service pages |
| Ways of working, frameworks, engagement models | `/about/how-we-work/` | Every service page (block 5) | Method pages under `/services/` |

---

## 3. Resolving overlaps between the three dimensions

The three dimensions intersect by design. The rule for any piece of content is: **decide what question it answers, then it has one home.**

| Question the content answers | Home | Example |
|---|---|---|
| What can you do for me? | Service page | "Our customer intelligence work covers segmentation, value analytics and research" |
| Do you understand my problem? | Expertise theme page | "Most loyalty programmes fail because they reward behaviour the customer would have shown anyway" |
| Have you worked with businesses like mine? | Sector landing (intro) and case study tags | "We have worked with TSB, Standard Chartered and Post Office on customer growth" |
| Prove it | Case study | "Dayinsure: rebuilt the quote journey and lifted conversion by X" |
| What do you think about this? | Insight | "Why membership economics beat discounting in 2026" |

Worked example: loyalty content.

| Content | Where it lives | Why |
|---|---|---|
| MGA's view on loyalty and what goes wrong | `/expertise/loyalty/` | Problem understanding |
| How MGA designs a loyalty proposition | `/services/proposition-innovation/` (with loyalty named in Related expertise) | Capability |
| How MGA measures loyalty economics | `/services/customer-intelligence/` | Capability |
| A retail loyalty case study | `/work/{client}/` tagged Loyalty, Retail, Proposition Innovation, Customer Intelligence | Proof. Surfaces automatically on all four related pages. |
| Loyalty in retail as a sector view | Nowhere as a page. The retail sector landing shows loyalty in its "Themes that matter here" block, auto-derived from case study tags. | Sectors are light |
| An article on loyalty trends | `/insights/{slug}/` tagged Loyalty | Thinking. Surfaces on the theme page. |

Result: one loyalty page, one retail page, two service pages, and the proof and thinking flow between them through tags. No duplicate loyalty content anywhere.

### 3.1 Specific overlap rulings

| Overlap | Ruling |
|---|---|
| Growth Strategy vs Proposition Innovation | Growth Strategy is where to play and how to win at business level. Proposition Innovation is designing the specific offer. Growth Strategy page names Proposition Innovation as the natural next step; Proposition Innovation page opens with one line placing it inside the Growth Strategy group. Neither restates the other. |
| Growth Strategy vs CEO Advisory | Growth Strategy is a project with outputs. CEO Advisory is a standing relationship. CEO Advisory page may say advisors draw on Growth Strategy thinking and link to it. Growth Strategy page does not promote CEO Advisory. |
| Activation group vs the six activation services | The group page explains the concept and lists. It never describes an individual service beyond the card summary. |
| Customer Intelligence vs Experience Engineering (research) | Research that produces insight and segmentation lives in Customer Intelligence. Research that directly informs design (usability, journey research) lives in Experience Engineering under its "Customer research and testing" H2. Each page links to the other in one sentence. |
| Experience Engineering vs separate CX / website / research pages | No separate pages. Experience Engineering carries three H2 sections, each with its own anchor (`#customer-experience`, `#website-and-digital`, `#research-and-testing`). Metadata, FAQ and internal anchor text use the plain terms so that the page ranks for them. |
| Data Agents vs AI Enablement | Data Agents is the tooling: specific agents doing specific jobs. AI Enablement is adoption and value strategy. AI Enablement links to Data Agents as "the tooling side"; Data Agents links to AI Enablement as "if you are earlier in the journey". |
| Data Agents vs Operating Architecture | Operating Architecture designs the model in which humans and agents work. Data Agents supplies the agents. Cross-linked once each. |
| Growth Office vs Operating Architecture | Operating Architecture designs; Growth Office staffs. Cross-linked once each. |
| Expertise theme vs a service that mainly serves it (for example Customer Value vs Customer Intelligence) | The theme page states the problem and links to the service for the analytics. The service page lists the theme under Related expertise. If a service page is found to be mostly about one theme, its copy is corrected, not the theme page. |
| Sector landing vs sector case studies | Landing aggregates; case studies hold the substance. The landing never summarises case studies in prose beyond the hero paragraph. |
| Methodology (for example CIVD) vs Proposition Innovation | How we work explains the framework once. Proposition Innovation says "we use our CIVD approach" and links. |
| Insight vs theme page | An insight is a dated point of view. A theme page is the evergreen position. If an insight becomes the definitive view, its key points are folded into the theme page and the insight links to it. |

---

## 4. Index and noindex rules

| Page or pattern | Index status | Canonical tag | Reason |
|---|---|---|---|
| All Canonical pages | index, follow | Self | Core targets |
| All Supporting pages | index, follow | Self | Secondary and long-tail targets |
| Sector landings | index, follow when threshold met; otherwise noindex, follow | Self | Threshold: at least 150 words of unique intro, three published case studies, two insights tagged to the sector. Prevents thin pages competing with services. |
| `/sectors/` index | index, follow | Self | Short but unique, and it is the sector navigation home |
| Team profiles | index, follow when biography is at least 100 words; otherwise noindex, follow | Self | Named-person search is a real path; thin stubs are not useful |
| Case studies | index, follow | Self | Proof pages earn brand and client-name searches |
| Anonymised case studies | index, follow | Self | Still unique content |
| Insights | index, follow | Self | Long-tail |
| Insights of type event, after the event date | index, follow, with a "this event has passed" note | Self | Keeps any earned links working |
| `/work/?service=…`, `/work/?expertise=…`, `/work/?sector=…` | noindex, follow | Points to `/work/` | Filter states are not destinations |
| `/insights/?type=…`, `/insights/?expertise=…` and other insight filters | noindex, follow | Points to `/insights/` | As above |
| Pagination (`?page=n`) on Work and Insights | index, follow | Self (each page is its own canonical) | Standard pagination practice so deep content stays discoverable |
| `/contact/?topic=…` | noindex | Points to `/contact/` | Parameter variant |
| `/contact/thank-you/` | noindex, nofollow | Self | Conversion confirmation only |
| `/search/` and results | noindex, follow | Self | Internal search |
| `/404/` | noindex | Self | Error |
| `/newsletter/` | index, follow | Self | Legitimate destination |
| Legal pages | index, follow | Self | Standard |
| Draft or unpublished content | Not served | | Never leak drafts to the live site |

Thin content guards, applied automatically in the CMS where possible:

- A theme page cannot be published with fewer than two case studies and two insights tagged to it.
- A sector landing switches to noindex when it drops below the threshold (for example if a case study is unpublished).
- A service page always meets the threshold by definition of being canonical. If a service is discontinued, the page is kept and redirected (see section 7), never left thin.

---

## 5. Internal linking rules

Internal links are how the three dimensions intersect without duplicate pages. These rules are mandatory for content editors and should be enforced by the templates.

### 5.1 Every page links up to a canonical

| Page type | Must link to |
|---|---|
| Expertise theme | At least two service pages (Where we help block) and `/work/?expertise={theme}` |
| Sector landing | At least two service pages (Services most used here block, auto) and `/work/?sector={sector}` |
| Case study | Every service used (hero and Related services), every theme tagged, one sector |
| Insight | At least one service (Related services block) and at least one theme |
| Team profile | The services and themes the person leads on |
| How we work | Every service group it mentions |
| Home | Services hub, Growth Strategy, Activation, Expertise hub, Work hub |

### 5.2 Canonicals link across and down

| Page type | Must link to |
|---|---|
| Service detail | Its group page (or Services hub), two or three related services, one to five related themes, tagged case studies, How we work |
| Services hub | Every service, every theme (cross-reference grid), How we work |
| Work hub | Nothing mandatory beyond filters; the case study cards carry the links |

### 5.3 Anchor text

- Link to a service using its exact service label ("Experience Engineering"), optionally followed by a plain-language gloss in the sentence ("Experience Engineering, our CX and website practice").
- Link to a theme using the theme name.
- Never use "click here" or "read more" as the only link text.
- Anchor links into Experience Engineering sections may use the plain terms ("website design and build").

### 5.4 Link volume

- Body copy: two to five contextual links per 500 words. Related-content modules do not count toward this.
- Do not link the same destination more than once in body copy on a page.
- Footer links exist on every page and are excluded from these counts.

### 5.5 Tagging model (how auto modules work)

Every case study, insight and team profile carries three tag sets: services (required for case studies), expertise themes (optional), sectors (optional). Modules such as "Proof", "Insights", "Themes that matter here" and "Services most used here" are generated from these tags. Good tagging discipline is what makes the intersecting dimensions work without editors hand-curating every page.

---

## 6. Metadata and structured data

| Item | Rule |
|---|---|
| Title tags | `{Page title} \| Manifesto Growth Architects`. Service titles carry the plain-language term where it aids search, for example `Experience Engineering: CX, website and research \| Manifesto Growth Architects`. Under 60 characters where practical. |
| Meta descriptions | Unique per page, 140 to 160 characters, written as an answer to the visitor's question. |
| H1 | One per page, matching the page's nav label or title. Service H1s use the exact service label. |
| Organization schema | Site-wide, with name, logo, sameAs (LinkedIn), contactPoint. Name and logo unchanged (Source C). |
| Service schema | On each service detail page: name, description, provider, areaServed, and serviceType using the plain-language terms. |
| BreadcrumbList schema | All pages with breadcrumbs. |
| Article schema | Insights, with author linked to the team profile URL. |
| Person schema | Team profiles, with jobTitle and worksFor. |
| FAQPage schema | Service pages with the FAQ module. |
| Open Graph and Twitter cards | All indexable pages, with a default image where none is set. |
| XML sitemap | Includes all index, follow URLs. Excludes filter states, thank-you, search, 404. Split by section if it exceeds 1,000 URLs. |
| hreflang | Not required. Single-language site (British English). |

---

## 7. Redirects and migration

The current site's URLs are not listed in the sources, so this section sets the rules rather than the map.

| Rule | Detail |
|---|---|
| Map every existing indexed URL | Crawl the current site before launch. Every URL that returns 200 today gets a 301 to the closest new page. Nothing is left to 404 if it has traffic or backlinks. |
| Service redirects | Old service or capability pages redirect to the matching `/services/` canonical. Old CX, UX, website or research pages redirect to `/services/experience-engineering/` and may target a section anchor. |
| Sector redirects | Any old industry pages redirect to `/sectors/{sector}/` if the sector exists, otherwise to `/work/?sector=` or `/work/`. |
| Content redirects | Old articles redirect to their new `/insights/{slug}/` URL, keeping slugs where possible. |
| Marketing shortcuts | `/agentlab/` 301 to `/services/data-agents/`. `/side-by-side/` 301 to `/services/ceo-advisory/`. |
| Repackaging later | If services are renamed or regrouped (Source C notes the deck is a subset and may change), the old `/services/{slug}/` 301s to the new one. Flat service URLs make this a single redirect per service. |
| Testing | Redirect map is tested before go-live and monitored for 404s for 90 days after. |

---

## 8. Search intent coverage: origination

The site must catch people who do not know MGA. The mapping below shows which page catches each intent type. If an intent has no row, it is not a target.

| Intent type | Example query shape | Catching page |
|---|---|---|
| Capability | "growth strategy consultancy", "customer experience consultancy UK", "AI enablement consultancy" | Service detail |
| Problem | "how to fix a loyalty programme", "subscription churn strategy", "pricing strategy consultancy" | Expertise theme |
| Sector reassurance | "growth consultancy financial services" | Sector landing (Light; ranks only opportunistically) plus the service page, which mentions sectors in proof |
| Proof | "{client name} case study", "{client name} Manifesto" | Case study |
| Person | "{consultant name}" | Team profile |
| Brand | "Manifesto Growth Architects", "Manifesto Growth" | Home, About |
| Product | "AgentLab" | Data Agents |
| Thought leadership | Long-tail topical questions | Insight, handing off to a theme and a service |

Sector queries are the weakest intentionally. Sector authority is earned through case studies and service pages that name sectors, not through sector content hubs.
