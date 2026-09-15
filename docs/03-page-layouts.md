# 03. Page layouts (v3)

Templates for each page type, described as an ordered list of blocks. For every block: what it contains, where its content comes from, and when it appears. This is structure, not visual design. Block names are working names for the CMS and wireframes.

v3 changes are confined to wording: service names follow the v3 nav labels (`nav-wording-decisions.md`), the service hero gains an "also known as" line for renamed services, and the Experience Engineering H2s use the plain terms. Block order and rules are unchanged from v2.

Related: `05-content-matrix.md` shows the same information as a grid; `04-canonicals-and-seo.md` sets the linking rules the "Related" blocks follow.

---

## Conventions used in every template

| Term | Meaning |
|---|---|
| **Always** | The block is present on every page of this type. |
| **Conditional** | The block appears only when the stated condition is true. If the condition fails, the block is skipped and nothing takes its place. |
| **Editorial** | The block appears when a content editor chooses to add it. |
| **Auto** | Content is pulled automatically from tags and relationships in the CMS. |
| **Curated** | Content is hand-picked by an editor. Falls back to Auto if nothing is picked. |
| **CTA** | Call to action. On this site every primary CTA leads to `/contact/`, optionally with `?topic=`. |

Global blocks on every page, not repeated below: Header (see `01-primary-navigation.md`), Breadcrumbs (all pages except Home), Footer, cookie notice.

Block order matters. The first two blocks on any page must answer "where am I and is this for me?" before any proof or detail.

---

## T1. Home (`/`)

Purpose: say who MGA is for, show the Growth Architecture triangle, and route into services, work and insights within one screen. Home carries no unique long-form content. Everything it shows exists in full somewhere else.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Positioning statement from Source B ("Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth") and the line "Strategy that works. Execution that delivers.", one line of who it is for, primary CTA to Contact, secondary CTA to `/services/` | Always |
| 2 | Client logo strip | 8 to 12 logos from the Source B client list, linking to `/work/` | Always. Logos link to the case study if one exists, otherwise to `/work/?sector=`. |
| 3 | Growth Architecture triangle | The triangle drawn as three connected blocks with the Source B one-liners: Growth Strategy ("Architecting strategies and value propositions that deliver sustainable customer value growth"), Activation Services ("Building the bridge from strategy to execution"), CEO Advisory ("Direct support that sits side-by-side with leaders"). Each block links to its pillar page. Growth Strategy is largest, Activation second, CEO Advisory smallest and quietest. | Always. This is the block Gary asked for: the triangle must be pointable within seconds. Uses the same three labels as the mega-nav. The one-liners are Source B copy and should get the same plain-language pass as the nav when Andy writes the service copy (open item in `06-decisions-log.md`). |
| 4 | Featured work | Three case studies, curated, spanning at least two pillars | Always. Curated; falls back to newest. This is where the v1 mega-nav featured card moved to. |
| 5 | Expertise themes strip | The five themes as a single calm row of links with one-line descriptors, heading "Growth problems we know deeply" | Always. One row, no cards. |
| 6 | Latest insights | Three newest insights, auto | Always |
| 7 | Closing CTA | Contact CTA with a plain-English prompt ("Tell us about your growth challenge") | Always |

What Home does not do: no long "about us" copy, no full service descriptions, no methodology explanation, no team grid, no sector block (sectors are in the footer and on the logo strip through case study links). Each of those has a page.

v1 had ten blocks here. v2 has seven. The proof band, How we work teaser and Who we work with block were cut as noise.

---

## T2. Services hub: Growth Architecture (`/services/`)

Purpose: this is the triangle page. Explain the three pillars and route to the right service in one scroll.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | H1 "What we do", subheading "Our Growth Architecture", two short paragraphs from Source B: the path from strategy to execution has become complex and fragmented; Growth Architecture combines market-leading strategic thinking with AI-powered activation services. | Always |
| 2 | The triangle | The same three-block triangle as Home block 3, larger, with the three Source B one-liners. Each block anchors to the pillar section below and links to the pillar page. | Always |
| 3 | Pillar 1: Growth Strategy | Pillar heading and one-line subtitle (as in the mega-nav), two service cards (Growth Strategy, Proposition Innovation) each with a two-line summary and link | Always. First pillar section. |
| 4 | Pillar 2: Activation Services | Pillar heading and subtitle, one paragraph on strategy-to-execution and "not ongoing operations", link to `/services/activation/`, six service cards in nav order, each with the one-line subtitle from the mega-nav | Always |
| 5 | Pillar 3: CEO Advisory | Pillar heading and subtitle, one paragraph on Side-by-Side, up to three advisor profile cards (auto from the advisor flag), link to `/services/ceo-advisory/` | Always. Third and visibly quieter than pillars 1 and 2, but a full section, not a footnote. |
| 6 | Proof | Three case studies spanning at least two pillars, curated | Always |
| 7 | Expertise themes strip | The five theme links, one row, heading "We apply these services to the growth problems we know best" | Always. This is the intersecting dimension made visible without a grid. |
| 8 | Closing CTA | Contact | Always |

v1 carried a services-against-themes cross-reference grid here. It is removed from the hub as visual noise. The intersection is carried by the Related expertise block on every service page and by the Where we help block on every theme page.

---

## T3. Service detail (`/services/{service}/`)

Used for all eight canonical services and, with the noted variations, the Activation group page and CEO Advisory.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Service name as H1 (the v3 nav label, exactly), a one-line plain definition (start from the mega-nav subtitle, then the Source B one-liner if it adds something), one-line "who this is for", primary CTA (`/contact/?topic={service}`). For services renamed from the deck (Customer Research and Insight, AI Agents for Marketing, Operating Model Design) a small "also known as" line under the H1 names the deck term: "Our Customer Intelligence practice", "Data Agents, built in AgentLab", "Our Operating Architecture framework". | Always. The "also known as" line is Conditional: only on renamed services. |
| 2 | Pillar context | One line placing the service in the triangle ("Part of Activation Services" or "Part of Growth Strategy") linking to the pillar page, and previous / next service links within the pillar | Always for Activation services and Proposition Innovation. Omitted for Growth Strategy (it is the pillar) and CEO Advisory (it is the pillar). |
| 3 | Why | Two to four short paragraphs on the situations that lead clients to this service. Source B provides a "Why" paragraph for every service; start from it. | Always |
| 4 | What we do | The service explained: scope, typical deliverables, what the client gets. Source B provides a "What" section for every service. Subheadings carry the search-friendly terms. | Always. This is the canonical description; no other page restates it. |
| 5 | How it works | Typical phases or shape of the engagement, duration where Source B gives it (AI Agents for Marketing: 4 weeks, 6 weeks, ongoing), who from MGA is involved | Always. Links to `/about/how-we-work/` for general methodology rather than repeating it. |
| 6 | Service-specific module | Varies by service (table below) | Conditional per service |
| 7 | Proof | Case studies tagged to this service, auto, up to four, with the option to pin one. Source B names example clients per service. | Always when at least one tagged case study exists. If none, show a client logo list instead. |
| 8 | Related expertise | Themes where this service is commonly applied, each with one line on the intersection | Always. Set per service in the CMS. Minimum one, maximum five. |
| 9 | Related services | Two or three services most often bought alongside this one | Always. Curated. |
| 10 | Insights | Up to three insights tagged to this service, auto | Conditional: at least one tagged insight exists |
| 11 | People | One to three team profiles who lead this service | Editorial |
| 12 | FAQ | Three to six questions clients ask about this service, marked up as FAQ structured data | Editorial. Recommended for every canonical service because it captures long-tail search phrasing. |
| 13 | Closing CTA | Contact with topic pre-set | Always |

Service-specific module (block 6), drawn from Source B:

| Service | Module |
|---|---|
| Growth Strategy | The CIVD frame (Customer, Innovation, Value, Delivery) from the Source B Growth Strategy slide, as a four-part diagram with a paragraph each. Plus a link to Proposition Innovation as the natural next step. Source B marks this slide "to be updated from existing content on growth architecture / approach". |
| Proposition Innovation | How MGA designs new value propositions that grow sustainable customer value, with the proposition types named on the call (loyalty, membership, subscription, D2C) each linking to its expertise theme. |
| Customer Research and Insight | Two offers as sub-sections with plain H2s ("Research projects": qualitative, quantitative, surveys, digital listening; "Always-on customer insight": voice of the customer tools, panels, intelligence platforms) and the input types as a scannable list: digital listening, qual research, quant research, customer data analytics, internal knowledge, external market data. "Customer Intelligence" is used in body copy as the practice name. |
| Experience Engineering | Three sub-sections with their own plain H2s: Customer experience (CX) design; Website and digital product design and build; User research and testing (with customer and value analytics). Each two paragraphs. Plus the Source B proof line: engagements consistently deliver over 3x EBITDA return on investment. This is how customer experience, website and research searches are caught on one canonical page. Reference model: Dayinsure and Key Group. |
| AI Agents for Marketing | Timeline (4 weeks audit, 6 weeks first agents, ongoing portfolio) then the AgentLab catalogue grouped as in Source B: Reporting and Analytics; Data and Infrastructure; Strategy and Planning; Automation and Execution. Agents are entries in this list, not pages. "Data Agents" and "AgentLab" are named in the module heading. |
| Operating Model Design | The four qualities of an adaptive operating model (grounded in customer value growth; fuelled by high-quality data; redesigned around humans and AI agents; orchestrated and linked to impact) and the Source B appendix diagram (Growth Strategy, Data and Tools, New Work Units, Orchestration, value streams) as a captioned figure titled "Our Operating Architecture framework". |
| Growth Office | The three connected elements from Source B (Culture, Capability, Value) as sub-sections, and the note that MGA provides interim support then establishes ongoing ways of working. Body copy uses the plain terms "interim growth team" and "programme office" alongside the label. |
| AI Enablement | Three programmes as sub-sections with plain H2s (AI skills and adoption; Finding where AI pays off (value cases); New business models with AI) with the maturity assessment as the entry step. Cross-link to AI Agents for Marketing for tooling. |
| CEO Advisory (Side-by-Side) | Why (driving customer-led growth is demanding and lonely) and What (a select group of senior leaders armed with Manifesto thinking and frameworks; adaptive and personality-led; virtual or in person; retainer-based). Advisor profiles pulled from `/about/team/` where the person is flagged as advisor: this block is the heart of the page. How the retainer works. No FAQ module. Quieter CTA ("Arrange a conversation"). |
| Activation group page | Replaces blocks 3 to 6 with: "What Activation means here" (the bridge from strategy to execution, AI-powered and human-led, not ongoing operations), then six service cards with subtitles. Blocks 7 to 13 as standard. |

---

## T4. Expertise hub (`/expertise/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Our expertise", one paragraph explaining these are the growth problems MGA is known for and that each cuts across services and sectors | Always |
| 2 | Theme cards | Five cards in nav order, each with a definition line and the count of case studies and insights available | Always |
| 3 | Latest insights across themes | Six newest insights tagged to any theme | Always |
| 4 | CTA | Contact | Always |

---

## T5. Expertise theme (`/expertise/{theme}/`)

Purpose: prove MGA understands the problem, then hand off to the services that solve it. This page describes problems and outcomes. It never describes how a service is delivered.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Theme name as H1, one-sentence framing of the problem space, CTA (`/contact/?topic={theme}`) | Always |
| 2 | Our view | Three to five short paragraphs: what MGA believes about this theme, common failure modes, what good looks like. This is the unique content on the page. | Always. 300 to 600 words. |
| 3 | Where we help | The services applied to this theme, each with one line on how it applies here, linking to the service page | Always. Curated per theme. Minimum two. This block is the hand-off to the canonicals. |
| 4 | Proof | Case studies tagged to this theme, auto, up to six | Always when at least two exist. Below two, the theme page should not have been published. |
| 5 | Insights | Insights tagged to this theme, auto, up to six, with a link to `/insights/?expertise={theme}` | Always when at least two exist |
| 6 | Sectors where this matters | Small row of sectors with case studies tagged to both this theme and the sector | Conditional: at least one such case study exists. Links to `/sectors/{sector}/`. |
| 7 | People | Team members who lead on this theme | Editorial |
| 8 | Related themes | The other four themes as links | Always |
| 9 | CTA | Contact with topic pre-set | Always |

---

## T6. Sector light landing (`/sectors/{sector}/`)

Purpose: reassure "you have worked with businesses like mine" and route to proof. Deliberately short. No sector point of view (Source C).

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Sector name as H1, two or three sentences on the kind of work MGA does in this sector and the clients it has worked with | Always. 150 to 300 words maximum. |
| 2 | Client logos | Logos of clients in this sector | Always |
| 3 | Case studies | All case studies tagged to this sector, auto | Always. If fewer than three, the page is noindex. |
| 4 | Services most used here | The two or three services most frequently tagged alongside this sector, auto from case study tags | Always |
| 5 | Themes that matter here | Themes tagged alongside this sector, auto | Conditional: at least one |
| 6 | Insights | Insights tagged to this sector, auto, up to three | Conditional: at least two exist |
| 7 | CTA | Contact | Always |

The sector index (`/sectors/`) is T6 block 1 (generic) plus a four-card list and CTA.

---

## T7. Work hub (`/work/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Our work", one line | Always |
| 2 | Featured | One curated case study, large | Editorial. Falls back to newest. |
| 3 | Filters | Three filter groups: Service (grouped by pillar: Growth Strategy and Proposition Innovation; the six Activation services; CEO Advisory), Expertise (five), Sector (four). Multi-select within a group, AND across groups. Filters update the URL query string. | Always |
| 4 | Results grid | Case study cards: client, one-line result, service and theme tags. Newest first by default, pinned items first. | Always. Paginated or load-more after 12. |
| 5 | Empty state | If a filter combination returns nothing: message plus links to the nearest broader filter | Conditional |
| 6 | CTA | Contact | Always |

---

## T8. Case study (`/work/{client}/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Client name, one-line headline result, sector, services used (linked), themes (linked) | Always |
| 2 | At a glance | Three to four headline numbers or outcomes | Always |
| 3 | The challenge | Two to four paragraphs | Always |
| 4 | What we did | Narrative of the approach, with the services referenced inline and linked. Does not explain what the service is in general; links do that. | Always |
| 5 | The result | Outcomes, quantified where permitted | Always |
| 6 | Client quote | Attributed testimonial. Testimonials live here, not on a separate page (Source A). | Editorial |
| 7 | Team | The MGA people on the engagement, linking to profiles | Editorial |
| 8 | Related services | The services used, as cards | Always |
| 9 | Related work | Three more case studies sharing a service or theme, auto | Always |
| 10 | CTA | Contact with the primary service pre-set | Always |

Anonymised case studies use the same template with the client name replaced by a sector descriptor.

---

## T9. Insights hub (`/insights/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Insights", one line | Always |
| 2 | Latest | One curated or newest insight, large, plus the next three | Always. "Latest" is a section here, not a page (Source A). |
| 3 | Filters | Type (article, report, event), Expertise, Service, Sector | Always |
| 4 | Results list | Cards: title, type, date, theme tags, reading time | Always. Paginated after 12. Past events hidden by default. |
| 5 | Newsletter sign-up | Inline form or link to `/newsletter/` | Always |

---

## T10. Insight (`/insights/{slug}/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Title as H1, type label, date, author(s) linked to profiles, reading time, theme tags | Always |
| 2 | Body | Long-form content with standard rich text | Always |
| 3 | Gated download | Form to receive a report | Conditional: type is report and gating is enabled |
| 4 | Event details | Date, time, location or link, registration | Conditional: type is event |
| 5 | Author box | Author profile summary linking to `/about/team/{name}/` | Always |
| 6 | Related services | Services tagged to this insight, maximum two, with a one-line "how we help" | Always when tagged. This is how thinking hands off to the canonical. |
| 7 | Related expertise | Theme(s) tagged, linking to `/expertise/{theme}/` | Always when tagged |
| 8 | Related insights | Three, sharing a theme, auto | Always |
| 9 | Newsletter sign-up | Inline | Always |
| 10 | CTA | Contact | Always |

---

## T11. About (`/about/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | "About Manifesto Growth Architects", positioning statement | Always |
| 2 | Who we are and our story | Origin, what MGA believes about growth, why customer-led | Always |
| 3 | What makes us different | Three to four points, one of which is the Growth Architecture model (strategy plus AI-powered activation) | Always |
| 4 | Leadership | Founders and partners with links to profiles | Always |
| 5 | How we work teaser | Paragraph plus link to `/about/how-we-work/` | Always |
| 6 | Clients | Logo wall | Always |
| 7 | Values and careers teaser | Two links: `/about/values/`, `/careers/` | Always |
| 8 | CTA | Contact | Always |

---

## T12. Team listing (`/about/team/`) and Team profile (`/about/team/{name}/`)

Team listing:

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading, one paragraph | Always |
| 2 | Leadership | Profile cards | Always |
| 3 | Consultants | Profile cards | Always |
| 4 | Side-by-Side advisors | Anchor `#advisors`. Profile cards for advisors, with a one-line note and link to `/services/ceo-advisory/`. This is the target of "Meet the advisors" in the mega-nav. | Conditional: at least one advisor is flagged. Until then the mega-nav link points to `/services/ceo-advisory/`. |
| 5 | Careers CTA | Link to `/careers/` | Always |

Team profile:

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Name, role, one-line focus, contact route (LinkedIn or contact form) | Always |
| 2 | Biography | Two to five paragraphs | Always. Under 100 words means noindex. |
| 3 | Focus | Services and themes this person leads on, linked | Always |
| 4 | Selected work | Case studies this person is tagged on | Conditional |
| 5 | Insights | Articles authored | Conditional |
| 6 | Advisor note | "Available through Side-by-Side" with link to `/services/ceo-advisory/` | Conditional: person is flagged as advisor |
| 7 | CTA | Contact | Always |

---

## T13. How we work (`/about/how-we-work/`)

Purpose: explain method without turning it into a product (Source A: separate methodology from services).

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | "How we work" | Always |
| 2 | Principles | The ways of working MGA holds to, as a short list with a paragraph each. Include "AI-powered, human-led" (Source B). | Always |
| 3 | Engagement shapes | Strategy project, strategy into activation, embedded growth office, advisory retainer. Each links to the relevant service or pillar. | Always |
| 4 | Frameworks and tools | Named frameworks (for example CIVD, the adaptive operating model) with a paragraph each. Frameworks are explained here once and referenced from service pages. | Always |
| 5 | Working with AI | How AI-powered activation works in practice; links to AI Agents for Marketing and AI Enablement | Always |
| 6 | What clients say | Two or three quotes about the experience of working with MGA | Editorial |
| 7 | CTA | Contact | Always |

---

## T14. Values and culture (`/about/values/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | "Values and culture" | Always |
| 2 | Values | Three to six values with a paragraph each | Always |
| 3 | Culture | How the team works together | Always |
| 4 | Diversity, equity and inclusion | MGA's commitments | Always |
| 5 | Careers teaser | Link to `/careers/` | Always |

---

## T15. Careers (`/careers/`) and Role (`/careers/{role}/`)

Careers hub:

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | "Careers at Manifesto" | Always |
| 2 | Life at Manifesto | What it is like to work here; links to `/about/values/` | Always |
| 3 | Benefits | List | Always |
| 4 | Open roles | Cards linking to `/careers/{role}/` | Always. Empty state: "No open roles right now" plus a speculative contact route. |

Role:

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Role title as H1, location, type | Always |
| 2 | About the role | Description, responsibilities, what we look for | Always |
| 3 | How to apply | Form or email route | Always |
| 4 | Other roles | Links to other open roles | Conditional |

---

## T16. Contact (`/contact/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading, one line, what happens after you get in touch | Always |
| 2 | Form | Name, company, email, topic selector (pre-filled from `?topic=`), message | Always |
| 3 | Direct contact | Email, phone, office address | Always |
| 4 | Reassurance | One or two lines on response time and confidentiality | Always |

Thank-you page: confirmation, then three curated links (a service, a case study, an insight).

---

## Template to URL mapping

| Template | URLs |
|---|---|
| T1 Home | `/` |
| T2 Services hub (Growth Architecture) | `/services/` |
| T3 Service detail | `/services/{service}/` including `/services/activation/` and `/services/ceo-advisory/` with noted variations |
| T4 Expertise hub | `/expertise/` |
| T5 Expertise theme | `/expertise/{theme}/` |
| T6 Sector light landing | `/sectors/`, `/sectors/{sector}/` |
| T7 Work hub | `/work/` |
| T8 Case study | `/work/{client}/` |
| T9 Insights hub | `/insights/` |
| T10 Insight | `/insights/{slug}/` |
| T11 About | `/about/` |
| T12 Team listing and profile | `/about/team/`, `/about/team/{name}/` |
| T13 How we work | `/about/how-we-work/` |
| T14 Values and culture | `/about/values/` |
| T15 Careers and Role | `/careers/`, `/careers/{role}/` |
| T16 Contact | `/contact/`, `/contact/thank-you/` |
| Generic content | Legal pages, `/newsletter/`, `/search/`, `/404/` |
