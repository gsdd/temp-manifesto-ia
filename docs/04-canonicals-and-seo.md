# 04. Canonicals and SEO (v4)

Which page owns which topic, how the overlaps between services, expertise themes and sectors are resolved, what is and is not indexed, and how pages link to one another. The aim is a site that originates enquiries from search, not just one that confirms credibility after a referral (Source C).

v3 renamed three services to the searched term (Customer Research and Insight, AI Agents for Marketing, Operating Model Design). v4 (`v4-simplification.md`) takes the item subtitles out of the mega-nav, so the **search vocabulary now has to be carried by the pages**: hero lines, H2s, title tags, meta descriptions and FAQs (section 6). Nothing about ownership, indexing or linking changes except that the `/sectors/` index page is cut and redirected (sections 4 and 7).

The principle is Source A's: one canonical page for each important proposition or topic, with the rest of the site linking into and out of it. Services are canonical. Themes and sectors intersect them through links and tags, never through duplicate pages.

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
| Growth Architecture (the proposition), "strategy that works, execution that delivers" | `/services/` | Home (triangle block), About | A separate `/growth-architecture/` page (redirect only) |
| Growth strategy, customer value growth strategy, growth consultancy, CIVD (Customer, Innovation, Value, Delivery) | `/services/growth-strategy/` | Home, About, all theme pages, case studies, How we work (framework explanation only) | Any theme or sector variant such as "growth strategy for retail"; a separate CIVD page |
| Proposition design, proposition innovation, new proposition development, D2C propositions | `/services/proposition-innovation/` | Growth Strategy page, Loyalty / Membership / Subscriptions theme pages | |
| Strategy activation, strategy to execution, activation services | `/services/activation/` (group) | Home, Services hub, all activation services | |
| Customer research, customer insight, market research, surveys, segmentation, voice of the customer, digital listening, customer intelligence | `/services/customer-research/` | Experience Engineering (research for design), Customer Value theme | A separate research or market research page |
| Experience engineering, customer experience design, CX consultancy, website design and build, digital product design, user research, usability testing | `/services/experience-engineering/` | Customer Research and Insight (for analytical research), case studies | Separate CX, UX, website or research pages. All of these are H2 sections of this page. |
| AI agents for marketing, marketing AI, data agents, AgentLab, marketing automation agents, attribution, CDP clean-up, customer data quality, tagging | `/services/ai-agents-for-marketing/` | AI Enablement, Operating Model Design, How we work | Individual agent pages; `/agentlab/` or `/data-agents/` as pages (redirects only) |
| Operating model design, operating model consultancy, operating architecture, adaptive operating model, value streams | `/services/operating-model-design/` | Growth Office, AI Enablement, How we work (framework explanation only) | |
| Growth office, interim growth leadership, embedded growth team, programme office, modern PMO, fractional CMO or CGO | `/services/growth-office/` | Operating Model Design, CEO Advisory | |
| AI enablement, AI adoption, AI training, AI maturity, AI value cases, AI business model innovation | `/services/ai-enablement/` | AI Agents for Marketing, Operating Model Design | A generic "AI" page |
| CEO advisory, Side-by-Side, SxS, executive advisor retainer | `/services/ceo-advisory/` | Team profiles flagged as advisor, Team listing `#advisors`, Growth Office | A separate `/side-by-side/` page (redirect only) |
| Loyalty strategy, loyalty programme design, loyalty economics | `/expertise/loyalty/` | Services (as related theme), case studies, insights, sectors | `/services/loyalty/`, `/sectors/retail/loyalty/` |
| Membership models, member economics | `/expertise/membership/` | As above | |
| Subscription growth, churn, retention | `/expertise/subscriptions/` | As above | |
| Pricing strategy, value-based pricing | `/expertise/pricing/` | As above | |
| Customer lifetime value, customer value management | `/expertise/customer-value/` | Customer Research and Insight (analytics), Growth Strategy | |
| Financial services, media, consumer, retail (as "consultancy for X" queries) | `/sectors/{sector}/` (Light, no keyword targets) | Case studies, Home logo strip | Sector points of view, sector-specific service pages, a sector index (cut in v4) |
| Ways of working, frameworks, engagement models | `/about/how-we-work/` | Every service page (block 5) | Method pages under `/services/` |
| Values, culture, DEI | `/about/values/` | About, Careers | Separate DEI page at launch |
| Careers, life at Manifesto, benefits, open roles | `/careers/` | About, Values, Team listing | A "Life at Manifesto" page competing with About (Source A) |

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
| How MGA measures loyalty economics | `/services/customer-research/` | Capability |
| A retail loyalty case study | `/work/{client}/` tagged Loyalty, Retail, Proposition Innovation, Customer Research and Insight | Proof. Surfaces automatically on all four related pages. |
| Loyalty in retail as a sector view | Nowhere as a page. The retail sector landing shows loyalty in its "Themes that matter here" block, auto-derived from case study tags. | Sectors are light |
| An article on loyalty trends | `/insights/{slug}/` tagged Loyalty | Thinking. Surfaces on the theme page. |

Result: one loyalty page, one retail page, two service pages, and the proof and thinking flow between them through tags. No duplicate loyalty content anywhere.

### 3.1 Specific overlap rulings

| Overlap | Ruling |
|---|---|
| Services hub vs Growth Architecture | One page. `/services/` is the Growth Architecture page and shows the triangle. There is no second proposition page for the triangle to be repeated on. |
| Growth Strategy vs Proposition Innovation | Growth Strategy is where to play and how to win at business level. Proposition Innovation is designing the specific offer. Growth Strategy page names Proposition Innovation as the natural next step; Proposition Innovation page opens with one line placing it inside the Growth Strategy pillar. Neither restates the other. |
| Growth Strategy vs CIVD | CIVD is the Growth Strategy frame (Source B Growth Strategy slide: Customer, Innovation, Value, Delivery). It is a module on the Growth Strategy page and is explained as a framework once in How we work. In v1 it was wrongly attached to Proposition Innovation. |
| Growth Strategy vs CEO Advisory | Growth Strategy is a project with outputs. CEO Advisory is a standing relationship. CEO Advisory page may say advisors draw on Growth Strategy thinking and link to it. Growth Strategy page does not promote CEO Advisory. |
| CEO Advisory vs advisor profiles | The offer is described once on `/services/ceo-advisory/`. The people are described once each on `/about/team/{name}/`. The offer page surfaces the profiles; the profiles carry a one-line note and link back. Neither copies the other. |
| Activation group vs the six activation services | The group page explains the concept and lists. It never describes an individual service beyond the card summary. |
| Customer Research and Insight vs Experience Engineering (research) | Research that produces insight and segmentation lives in Customer Research and Insight. Research that directly informs design (usability, journey research) lives in Experience Engineering under its "User research and testing" H2. Each page links to the other in one sentence. |
| Experience Engineering vs separate CX / website / research pages | No separate pages. Experience Engineering carries three H2 sections, each with its own anchor (`#customer-experience`, `#website-and-digital`, `#research-and-testing`). Metadata, FAQ and internal anchor text use the plain terms so that the page ranks for them. |
| AI Agents for Marketing vs AI Enablement | AI Agents for Marketing is the tooling: specific agents doing specific jobs. AI Enablement is adoption and value strategy. AI Enablement links to AI Agents for Marketing as "the tooling side"; AI Agents for Marketing links to AI Enablement as "if you are earlier in the journey". Both labels carry "AI" so a visitor with an AI intent sees two doors; the labels themselves ("for Marketing" versus "Enablement") tell them which, and the page hero lines confirm it. |
| AI Agents for Marketing vs Operating Model Design | Operating Model Design designs the model in which humans and agents work. AI Agents for Marketing supplies the agents. Cross-linked once each. |
| Growth Office vs Operating Model Design | Operating Model Design designs; Growth Office staffs. Cross-linked once each. |
| Nav label vs deck name (renamed services) | The nav label is the H1 and the slug. The deck name (Customer Intelligence, Data Agents, Operating Architecture) appears once in the hero as an "also known as" line and may be used in body copy as the practice, product or framework name. It is never a second page. |
| Expertise theme vs a service that mainly serves it (for example Customer Value vs Customer Research and Insight) | The theme page states the problem and links to the service for the analytics. The service page lists the theme under Related expertise. If a service page is found to be mostly about one theme, its copy is corrected, not the theme page. |
| Sector landing vs sector case studies | Landing aggregates; case studies hold the substance. The landing never summarises case studies in prose beyond the hero paragraph. |
| Methodology vs services | How we work explains each framework once. A service page says "we use our X approach" and links. |
| Insight vs theme page | An insight is a dated point of view. A theme page is the evergreen position. If an insight becomes the definitive view, its key points are folded into the theme page and the insight links to it. |

---

## 4. Index and noindex rules

| Page or pattern | Index status | Canonical tag | Reason |
|---|---|---|---|
| All Canonical pages | index, follow | Self | Core targets |
| All Supporting pages | index, follow | Self | Secondary and long-tail targets |
| Sector landings | index, follow when threshold met; otherwise noindex, follow | Self | Threshold: at least 150 words of unique intro, three published case studies, two insights tagged to the sector. Prevents thin pages competing with services. |
| `/sectors/` | 301 to `/work/` | | No index page in v4 (D-44). The footer lists the four sectors directly. |
| Team profiles | index, follow when biography is at least 100 words; otherwise noindex, follow | Self | Named-person search is a real path; thin stubs are not useful. Advisor profiles are a priority because CEO Advisory depends on them. |
| `/careers/{role}/` | index, follow while open; noindex or 301 to `/careers/` when closed | Self | Roles expire |
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
| Team profile | The services and themes the person leads on; advisors link to `/services/ceo-advisory/` |
| How we work | Every pillar it mentions |
| Home | Services hub, all three pillar pages (Growth Strategy, Activation, CEO Advisory), Work hub, Insights hub, the five theme pages (the one expertise row) |

### 5.2 Canonicals link across and down

| Page type | Must link to |
|---|---|
| Service detail | Its pillar page (or Services hub), two or three related services, one to three related themes (the visible cap; more may be tagged), tagged case studies, How we work |
| Services hub | All three pillar pages, every service, the Expertise hub (one sentence, one link) |
| Work hub | Nothing mandatory beyond filters; the case study cards carry the links |

### 5.3 Anchor text

- Link to a service using its nav label exactly ("Customer Research and Insight", "AI Agents for Marketing", "Operating Model Design", "Experience Engineering"). Never link using a retired deck label on its own.
- Where the nav label is a Manifesto term (Experience Engineering, Growth Office, Side-by-Side, Proposition Innovation), follow it with a plain gloss in the sentence the first time it appears on a page ("Experience Engineering, our customer experience and website practice").
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

### 6.1 Where the search vocabulary lives (v4)

v3 put a plain-English subtitle under every mega-nav item so that "customer experience", "website", "research", "loyalty", "AI", "operating model", "interim" and so on were visible in the menu. v4 removes those subtitles (D-35). The words are not dropped; each service page must carry them in the places search engines and visitors read first. This is now a hard requirement per canonical service, checked at content sign-off:

| Service | Terms the page must carry (hero line, at least one H2, title tag, meta description) |
|---|---|
| Growth Strategy | growth strategy, customer-led growth, where to focus and how to win |
| Proposition Innovation | new propositions, loyalty, membership, subscription, direct-to-consumer (one H2 per proposition type, each linking to its expertise theme) |
| Customer Research and Insight | customer research, customer insight, market research, surveys, analytics, customer listening, AI-powered research |
| Experience Engineering | customer experience (CX), website design and build, digital product, user research and testing (H2 per section, as in `03-page-layouts.md` T3) |
| AI Agents for Marketing | AI agents, marketing performance, customer data quality, data agents, AgentLab |
| Operating Model Design | operating model, teams, data and AI agents working together, operating architecture |
| Growth Office | interim growth team, programme office, PMO, strategy delivered |
| AI Enablement | AI skills, AI training, AI adoption, where AI pays off |
| CEO Advisory | CEO advisor, senior leaders, advisory retainer, Side-by-Side, advisor profiles |

The two quiet lines that remain in the menu (Experience Engineering: "Customer experience and websites"; Growth Office: "Interim growth team") are a courtesy for the two labels Andy flagged as opaque, not the primary carrier of these terms.

### 6.2 Rules

| Item | Rule |
|---|---|
| Title tags | `{Page title} \| Manifesto Growth Architects`. Service titles carry the plain-language term where the label is a Manifesto term, for example `Experience Engineering: customer experience and websites \| Manifesto Growth Architects`, `Growth Office: interim growth team and programme office \| Manifesto Growth Architects`, `Proposition Innovation: loyalty, membership and subscription propositions \| Manifesto Growth Architects`. Renamed services already carry the searched term in the label. Our work uses `Case studies \| Manifesto Growth Architects`. Under 60 characters where practical. |
| Meta descriptions | Unique per page, 140 to 160 characters, written as an answer to the visitor's question and carrying the page's terms from 6.1. |
| H1 | One per page, matching the page's nav label or title. Service H1s use the exact nav label. Renamed services carry a one-line "also known as" under the H1 naming the deck term. |
| Service hero line | One line under the H1 carrying the searched terms. Start from the v3 mega-nav subtitle for that service (`nav-wording-decisions.md`), which was written for exactly this purpose. |
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
| Marketing shortcuts | `/growth-architecture/` 301 to `/services/`. `/agentlab/` and `/data-agents/` 301 to `/services/ai-agents-for-marketing/`. `/side-by-side/` 301 to `/services/ceo-advisory/`. `/life-at-manifesto/` (if it exists today) 301 to `/careers/`. |
| `/sectors/` | 301 to `/work/`. The v3 sector index page was cut in v4 (D-44); the Work hub with its sector filter is the nearest destination. |
| v2 service slugs (deck names) | `/services/customer-intelligence/` 301 to `/services/customer-research/`. `/services/data-agents/` 301 to `/services/ai-agents-for-marketing/`. `/services/operating-architecture/` 301 to `/services/operating-model-design/`. Nothing is live, so these matter only if the v2 URLs were shared; they cost nothing to keep. |
| Repackaging later | If services are renamed or regrouped (Source C notes the deck is a subset and may change), the old `/services/{slug}/` 301s to the new one. Flat service URLs make this a single redirect per service. v3 is the first use of this rule. |
| Testing | Redirect map is tested before go-live and monitored for 404s for 90 days after. |

---

## 8. Search intent coverage: origination

The site must catch people who do not know MGA. The mapping below shows which page catches each intent type. If an intent has no row, it is not a target.

| Intent type | Example query shape | Catching page |
|---|---|---|
| Capability | "growth strategy consultancy", "customer experience consultancy UK", "customer research agency", "AI agents for marketing", "operating model design consultancy", "AI enablement consultancy" | Service detail |
| Problem | "how to fix a loyalty programme", "subscription churn strategy", "pricing strategy consultancy" | Expertise theme |
| Sector reassurance | "growth consultancy financial services" | Sector landing (Light; ranks only opportunistically) plus the service page, which mentions sectors in proof |
| Proof | "{client name} case study", "{client name} Manifesto" | Case study |
| Person | "{consultant name}", "{advisor name}" | Team profile |
| Brand | "Manifesto Growth Architects", "Manifesto Growth", "Growth Architecture" | Home, About, Services hub |
| Product and deck names | "AgentLab", "Data Agents", "Side-by-Side advisory", "Manifesto Customer Intelligence" | AI Agents for Marketing, CEO Advisory, Customer Research and Insight (via the "also known as" line and redirects) |
| Thought leadership | Long-tail topical questions | Insight, handing off to a theme and a service |

Sector queries are the weakest intentionally. Sector authority is earned through case studies and service pages that name sectors, not through sector content hubs.

The nav-level version of this table (which header or mega-nav item a visitor with each intent would click, and where on the page the word appears now that the menu carries labels only) is in `nav-wording-decisions.md`, section "Search intent to nav item".
