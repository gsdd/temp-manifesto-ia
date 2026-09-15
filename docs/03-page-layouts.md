# 03. Page layouts (v4)

Templates for each page type, described as an ordered list of blocks. For every block: what it contains, where its content comes from, and when it appears. This is structure, not visual design. Block names are working names for the CMS and wireframes.

v4 changes (`v4-simplification.md`): Home goes from seven blocks to six and loses the pyramid diagram, the tagged cards and the theme descriptors; every template follows the **one chip dimension, three visible** rule set out below; the Work and Insights hubs open with one filter group and put the rest behind "More filters"; the sector rows on theme pages and the theme rows on sector pages are cut; the sector index page is gone. Service names, the "also known as" hero line and the plain H2s from v3 are unchanged.

Related: `05-content-matrix.md` shows the same information as a grid; `04-canonicals-and-seo.md` sets the linking rules the "Related" blocks follow.

---

## Chips and tags: one dimension per page type

Gary's v4 feedback: page chips are too busy. The cause was structural. The IA has three intersecting dimensions (services, expertise themes, sectors) and v3 showed all three as chips wherever they were tagged. The cross-referencing model is right; showing it everywhere is not.

The rule: **each page type shows chips from one dimension only, capped at three visible.** The other dimensions still exist as CMS tags, drive filters and auto modules, and appear as blocks (a list of cards, a "Where we help" list) where the template calls for them. They are not displayed as chips.

| Page type | Chip dimension | Cap | Not shown as chips |
|---|---|---|---|
| Home | Expertise (one row of plain text links) | 5 | Services (the triangle is three blocks, not chips), sectors, insight types |
| Services hub | None | | The expertise line is one sentence with a link |
| Service detail | Expertise (Related expertise block) | 3 | Sectors; other services (Related services is two or three cards) |
| Expertise theme | None | | Services (Where we help is a list with a line each); sectors (row cut) |
| Sector landing | None | | Themes (row cut); services (Services most used here is a short list) |
| Work hub | Service, one per card | 1 | Themes and sectors on cards; they remain filters |
| Case study | Services used (hero) | 3 | Sector and themes in the hero. Related expertise appears once, at the foot, capped at 3 |
| Insights hub | Expertise, one per card | 1 | Type is a word in the meta line, not a chip |
| Insight | Expertise (hero) | 3 | Services (Related services is a block, max 2); sectors |
| Team profile | None | | Focus is a sentence with links |

Where a page has more tags than the cap, the template shows the first three (editor-ordered) and nothing else. There is no "+2 more" control on chips; the full set is visible on the filter hubs.

Sectors are shown as chips nowhere. They live in the Work and Insights filters (behind More filters), the footer, and their own light landings.

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

Purpose: say who MGA is for, show the Growth Architecture triangle once, and route into services, work and insights. Home carries no unique long-form content. Everything it shows exists in full somewhere else. Home has one chip set (block 4), one CTA path (Contact, in the hero and again at the foot) and no tags on any card.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Positioning statement from Source B ("Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth"), the line "Strategy that works. Execution that delivers.", one primary CTA to Contact, one text link to `/services/` ("What we do"). Beneath, a thin row of 8 client logos. | Always. Logos link to the case study if one exists, otherwise to `/work/`. |
| 2 | Growth Architecture triangle | Three blocks, each with the pillar label and the same short pillar line as the mega-nav: Growth Strategy ("Where and how you grow"), Activation Services ("Turning strategy into results"), CEO Advisory ("One-to-one support for leaders"). Each block links to its pillar page. Growth Strategy and Activation equal weight; CEO Advisory narrower and quieter. Section heading "What we do". | Always. The triangle is drawn once, here. No pyramid diagram, no Source B one-liners, no second rendering. The three lines are shared data with the mega-nav (`05-content-matrix.md`). |
| 3 | Our work | Three case studies, curated, spanning at least two pillars. Card: image, client, one-line result. No tags. Link "All work". | Always. Curated; falls back to newest. |
| 4 | Expertise | Heading "Growth problems we know best" and the five theme names as plain text links in one row. No descriptors, no cards, no counts. | Always. This is the only row of topic links on Home. Cap is five; a sixth theme does not appear here until one of the five is retired. |
| 5 | Latest insights | Three newest insights, auto: title and date. No type or theme tags. Link "All insights". | Always |
| 6 | Closing CTA | "Tell us about your growth challenge" and a Contact button | Always |

What Home does not do: no long "about us" copy, no full service descriptions, no methodology explanation, no team grid, no sector block, no filter chips, no type or theme tags on cards. Each of those has a page.

v1 had ten blocks here. v2 and v3 had seven, with the triangle drawn twice (three cards plus a pyramid). v4 has six: the logo strip is folded into the hero, the pyramid is gone, the cards carry no tags, and the expertise row is names only (D-41).

---

## T2. Services hub: Growth Architecture (`/services/`)

Purpose: this is the triangle page. Explain the three pillars and route to the right service in one scroll.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | H1 "What we do", subheading "Our Growth Architecture", the strapline "Strategy that works. Execution that delivers." and two short paragraphs from Source B: the path from strategy to execution has become complex and fragmented; Growth Architecture combines market-leading strategic thinking with AI-powered activation services. | Always. This is where the strapline lives now that it is out of the mega-nav (D-34). |
| 2 | The triangle | The same three-block triangle as Home block 2, larger, with the same three pillar lines. Each block anchors to the pillar section below and links to the pillar page. | Always |
| 3 | Pillar 1: Growth Strategy | Pillar heading and pillar line, two service cards (Growth Strategy, Proposition Innovation) each with a two-line summary and link | Always. First pillar section. |
| 4 | Pillar 2: Activation Services | Pillar heading and pillar line, one paragraph on strategy-to-execution and "not ongoing operations", link to `/services/activation/`, six service cards in nav order, each with a one-line summary written for the card (the card is where the v3 subtitle wording can be reused) | Always |
| 5 | Pillar 3: CEO Advisory | Pillar heading and pillar line, one paragraph naming Side-by-Side, up to three advisor profile cards (auto from the advisor flag), link to `/services/ceo-advisory/` | Always. Third and visibly quieter than pillars 1 and 2, but a full section, not a footnote. |
| 6 | Proof | Three case studies spanning at least two pillars, curated. Cards carry no tags. | Always |
| 7 | Expertise | One sentence, "We apply these services to the growth problems we know best", with a single link to `/expertise/` | Always. One line, one link. The five names are on Home, in the footer and on the hub. |
| 8 | Closing CTA | Contact | Always |

v1 carried a services-against-themes cross-reference grid here. v2 and v3 replaced it with a five-link strip. v4 reduces that to one sentence and one link (D-42). The intersection is carried by the Related expertise block on every service page and by the Where we help block on every theme page.

---

## T3. Service detail (`/services/{service}/`)

Used for all eight canonical services and, with the noted variations, the Activation group page and CEO Advisory.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Service name as H1 (the nav label, exactly), a one-line plain definition carrying the searched terms (this is where the v3 mega-nav subtitle wording now lives: for example Experience Engineering, "Customer experience (CX), website and digital design, build and testing"), one-line "who this is for", primary CTA (`/contact/?topic={service}`). No chips in the hero. For services renamed from the deck (Customer Research and Insight, AI Agents for Marketing, Operating Model Design) a small "also known as" line under the H1 names the deck term: "Our Customer Intelligence practice", "Data Agents, built in AgentLab", "Our Operating Architecture framework". | Always. The "also known as" line is Conditional: only on renamed services. |
| 2 | Pillar context | One line placing the service in the triangle ("Part of Activation Services" or "Part of Growth Strategy") linking to the pillar page | Always for Activation services and Proposition Innovation. Omitted for Growth Strategy (it is the pillar) and CEO Advisory (it is the pillar). v3 also had previous / next service links here; cut in v4 as chrome (D-42). |
| 3 | Why | Two to four short paragraphs on the situations that lead clients to this service. Source B provides a "Why" paragraph for every service; start from it. | Always |
| 4 | What we do | The service explained: scope, typical deliverables, what the client gets. Source B provides a "What" section for every service. Subheadings carry the search-friendly terms. | Always. This is the canonical description; no other page restates it. |
| 5 | How it works | Typical phases or shape of the engagement, duration where Source B gives it (AI Agents for Marketing: 4 weeks, 6 weeks, ongoing), who from MGA is involved | Always. Links to `/about/how-we-work/` for general methodology rather than repeating it. |
| 6 | Service-specific module | Varies by service (table below) | Conditional per service |
| 7 | Proof | Case studies tagged to this service, auto, up to four, with the option to pin one. Cards: client and one-line result, no tags. Source B names example clients per service. | Always when at least one tagged case study exists. If none, show a client logo list instead. |
| 8 | Related expertise | Themes where this service is commonly applied, as chips, each with one line on the intersection | Always. Set per service in the CMS. Minimum one, **maximum three visible**. This is the one chip dimension on a service page. |
| 9 | Related services | Two or three services most often bought alongside this one, as cards | Always. Curated. Cards, not chips. |
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
| Activation group page | Replaces blocks 3 to 6 with: "What Activation means here" (the bridge from strategy to execution, AI-powered and human-led, not ongoing operations), then six service cards, each with a one-line summary. Blocks 7 to 13 as standard. |

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
| 6 | People | Team members who lead on this theme | Editorial |
| 7 | Related themes | The other four themes as plain text links in one line | Always |
| 8 | CTA | Contact with topic pre-set | Always |

v3 had a "Sectors where this matters" row between Insights and People. Cut in v4 (D-42): sectors are reached through the Work filters and the footer, and a sector row on a theme page was a second chip dimension. The sector tags on the underlying case studies are unchanged.

---

## T6. Sector light landing (`/sectors/{sector}/`)

Purpose: reassure "you have worked with businesses like mine" and route to proof. Deliberately short. No sector point of view (Source C).

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Sector name as H1, two or three sentences on the kind of work MGA does in this sector and the clients it has worked with | Always. 150 to 300 words maximum. |
| 2 | Client logos | Logos of clients in this sector | Always |
| 3 | Case studies | All case studies tagged to this sector, auto. Cards: client and result, no tags. | Always. If fewer than three, the page is noindex. |
| 4 | Services most used here | The two or three services most frequently tagged alongside this sector, as a short list with a line each, auto from case study tags | Always |
| 5 | Insights | Insights tagged to this sector, auto, up to three | Conditional: at least two exist |
| 6 | CTA | Contact | Always |

v3 had a "Themes that matter here" row after Services most used here. Cut in v4 (D-42) for the same reason as the sector row on theme pages. There is no sector index page in v4 (D-44); the footer heading "Who we work with" is plain text and the four landings are reached from the footer and the Work filters.

---

## T7. Work hub (`/work/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Our work", one line | Always |
| 2 | Featured | One curated case study, large | Editorial. Falls back to newest. |
| 3 | Filters | One filter group open on load: Service, grouped by pillar (Growth Strategy and Proposition Innovation; the six Activation services; CEO Advisory). A "More filters" control reveals Expertise (five) and Sector (four). Multi-select within a group, AND across groups. Filters update the URL query string. Active filters from any group are shown as removable chips above the grid. | Always. v3 opened all three groups at once; v4 opens one (D-43). Arriving with `?expertise=` or `?sector=` in the URL opens More filters with that group visible. |
| 4 | Results grid | Case study cards: client, one-line result, one service tag (the primary service). Newest first by default, pinned items first. | Always. Paginated or load-more after 12. Theme tags on cards were cut in v4. |
| 5 | Empty state | If a filter combination returns nothing: message plus links to the nearest broader filter | Conditional |
| 6 | CTA | Contact | Always |

---

## T8. Case study (`/work/{client}/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Client name, one-line headline result, services used as chips (linked, maximum three) | Always. The one chip dimension on a case study. v3 also showed sector and theme chips here; cut in v4 (D-42). Sector and themes stay as CMS tags so the case study still surfaces on sector landings, theme pages and in filters. |
| 2 | At a glance | Three to four headline numbers or outcomes | Always |
| 3 | The challenge | Two to four paragraphs | Always |
| 4 | What we did | Narrative of the approach, with the services referenced inline and linked. Does not explain what the service is in general; links do that. | Always |
| 5 | The result | Outcomes, quantified where permitted | Always |
| 6 | Client quote | Attributed testimonial. Testimonials live here, not on a separate page (Source A). | Editorial |
| 7 | Team | The MGA people on the engagement, linking to profiles | Editorial |
| 8 | Related services | The services used, as cards | Always |
| 9 | Related expertise | The themes tagged, as chips, maximum three | Always when tagged. This is the only place themes appear on a case study. |
| 10 | Related work | Three more case studies sharing a service or theme, auto. Cards carry no tags. | Always |
| 11 | CTA | Contact with the primary service pre-set | Always |

Anonymised case studies use the same template with the client name replaced by a sector descriptor.

---

## T9. Insights hub (`/insights/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Insights", one line | Always |
| 2 | Latest | One curated or newest insight, large, plus the next three | Always. "Latest" is a section here, not a page (Source A). |
| 3 | Filters | One filter group open on load: Type (article, report, event). A "More filters" control reveals Expertise, Service and Sector. Filters update the URL query string. | Always. v3 opened all four groups; v4 opens one (D-43). This is also where the v3 Insights dropdown's type links now live (D-38). |
| 4 | Results list | Cards: title, one meta line (type, date, reading time), one theme tag | Always. Paginated after 12. Past events hidden by default. |
| 5 | Newsletter sign-up | Inline form or link to `/newsletter/` | Always |

---

## T10. Insight (`/insights/{slug}/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Title as H1, one meta line (type, date, reading time, author(s) linked to profiles), theme chips (maximum three) | Always. Themes are the one chip dimension on an insight. |
| 2 | Body | Long-form content with standard rich text | Always |
| 3 | Gated download | Form to receive a report | Conditional: type is report and gating is enabled |
| 4 | Event details | Date, time, location or link, registration | Conditional: type is event |
| 5 | Author box | Author profile summary linking to `/about/team/{name}/` | Always |
| 6 | Related services | Services tagged to this insight, maximum two, as a block with a one-line "how we help" each | Always when tagged. This is how thinking hands off to the canonical. A block, not chips. |
| 7 | Related expertise | Theme(s) tagged, linking to `/expertise/{theme}/` | Always when tagged. Repeats the hero chips as a labelled block for readers who skipped the hero. |
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
| 4 | Side-by-Side advisors | Anchor `#advisors`. Profile cards for advisors, with a one-line note and link to `/services/ceo-advisory/`. The CEO Advisory page links here; the mega-nav no longer does (v3's "Meet the advisors" item was cut, D-36). | Conditional: at least one advisor is flagged. |
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
| T6 Sector light landing | `/sectors/{sector}/` (no index page) |
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
