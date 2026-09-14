# 03. Page layouts

Templates for each page type, described as an ordered list of blocks. For every block: what it contains, where its content comes from, and when it appears. This is structure, not visual design. Block names are working names for the CMS and wireframes.

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

Purpose: say who MGA is for, name the lead offer, and route into the three dimensions within one screen. Home carries no unique long-form content. Everything it shows exists in full somewhere else.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Positioning statement (sustainable customer-led growth, strategy plus AI-powered activation), one line of who it is for, primary CTA to Contact, secondary CTA to `/services/` | Always |
| 2 | Client logo strip | 8 to 12 logos from the example client list, linking to `/work/` | Always. Logos link to the case study if one exists, otherwise to `/work/?sector=`. |
| 3 | What we do | Three cards: Growth Strategy (largest), Activation Services, and a small text link for CEO Advisory. Each card links to its hub or detail page. | Always. Growth Strategy is visually first and largest. CEO Advisory never gets a card. |
| 4 | Expertise strip | The five themes as a single row of links with one-line descriptors | Always |
| 5 | Featured work | Three case studies, curated | Always. Curated; falls back to newest. Must span at least two different services. |
| 6 | Proof point band | Three to four outcome statistics with the client and a link to each case study | Editorial |
| 7 | How we work teaser | One paragraph plus link to `/about/how-we-work/` | Always |
| 8 | Latest insights | Three newest insights, auto | Always |
| 9 | Who we work with | Four sector links with a logo each | Always. This is the only sector module on Home and it stays small. |
| 10 | Closing CTA | Contact CTA with a plain-English prompt ("Tell us about your growth challenge") | Always |

What Home does not do: no long "about us" copy, no full service descriptions, no methodology explanation, no team grid. Each of those has a page.

---

## T2. Service hub (`/services/`)

Purpose: explain the triangle and route to the right service in one scroll.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "What we do", two-paragraph explanation of the triangle: Growth Strategy at the core, Activation to deliver it, CEO Advisory for leaders who want a standing partner | Always |
| 2 | Growth Strategy group | Group heading, descriptor, two service cards (Growth Strategy, Proposition Innovation) each with a two-line summary and link | Always. First group. |
| 3 | Activation Services group | Group heading, descriptor explaining strategy-to-execution, link to `/services/activation/`, six service cards in nav order | Always |
| 4 | Services and expertise cross-reference | A compact table or grid: five expertise themes across the top, services down the side, with a marker where a service is commonly applied to a theme. Each theme heading links to `/expertise/{theme}/`. | Always. This block makes the intersecting dimension visible. Markers are set in the CMS per service. |
| 5 | How we work teaser | One paragraph and a link to `/about/how-we-work/` | Always |
| 6 | Proof | Three case studies spanning at least two service groups, curated | Always |
| 7 | CEO Advisory mention | Quiet single-row block: one sentence and a link to `/services/ceo-advisory/` | Always. Sits below the fold, styled quieter than the groups above. |
| 8 | Closing CTA | Contact | Always |

---

## T3. Service detail (`/services/{service}/`)

Used for all eight canonical services and, with the noted variations, the Activation group page and CEO Advisory.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Service name as H1, one-sentence definition, one-line "who this is for", primary CTA (`/contact/?topic={service}`) | Always |
| 2 | Group context | One line placing the service in the triangle ("Part of Activation Services") linking to the group page, and previous / next service links within the group | Always for Activation services and Proposition Innovation. Omitted for Growth Strategy (it is the group) and CEO Advisory (it is its own group). |
| 3 | The problem | Two to four short paragraphs on the situations that lead clients to this service. Written in client language. | Always |
| 4 | What we do | The service explained: scope, typical deliverables, what the client gets. Subheadings carry the search-friendly terms (for Experience Engineering: CX design, website design and build, customer research). | Always. This is the canonical description; no other page restates it. |
| 5 | How it works | Typical phases or shape of the engagement, duration range, who from MGA is involved | Always. Links to `/about/how-we-work/` for the general methodology rather than repeating it. |
| 6 | Service-specific module | Varies by service (see table below) | Conditional per service |
| 7 | Proof | Case studies tagged to this service, auto, up to four, with the option to pin one | Always when at least one tagged case study exists. If none, show a single quote or client list instead. |
| 8 | Related expertise | Themes where this service is commonly applied, each with one line on the intersection | Always. Set per service in the CMS. Minimum one, maximum five. |
| 9 | Related services | Two or three services most often bought alongside this one | Always. Curated. |
| 10 | Insights | Up to three insights tagged to this service, auto | Conditional: at least one tagged insight exists |
| 11 | People | One to three team profiles who lead this service | Editorial |
| 12 | FAQ | Three to six questions clients ask about this service, marked up as FAQ structured data | Editorial. Recommended for every canonical service because it captures long-tail search phrasing. |
| 13 | Closing CTA | Contact with topic pre-set | Always |

Service-specific module (block 6):

| Service | Module |
|---|---|
| Growth Strategy | "What a growth strategy from Manifesto contains": a short list of the strategy outputs. Plus a link to Proposition Innovation as the natural next step. |
| Proposition Innovation | The CIVD stages explained briefly (work in progress in Source B; placeholder until confirmed). |
| Customer Intelligence | Types of research and analytics offered, as a scannable list. |
| Experience Engineering | Three sub-sections with their own H2s: Customer experience (CX) design; Website and digital product design and build; Customer research and testing. Each two paragraphs. This is how CX, website and research searches are caught on one canonical page. Reference model: Dayinsure and Key Group. |
| Data Agents (AgentLab) | Agent catalogue: a filterable list of agents (reporting, data infrastructure, automation, QA, channel optimisation, test and learn, attribution, segmentation, CDP clean-up, tagging, journey mapping), each with a one-line job description. Agents are entries in this list, not pages. |
| Operating Architecture | The four layers (data and tools, work units, orchestration culture, value streams with humans and AI) as a diagram with captions. |
| Growth Office | Roles available on an interim basis, and the culture / capability / value framing. |
| AI Enablement | Three offers as sub-sections: adoption, value cases, business model innovation. Cross-link to Data Agents for the tooling side. |
| CEO Advisory (Side-by-Side) | Advisor profiles pulled from `/about/team/` where the person is flagged as an advisor. How the retainer works. No FAQ module. Quieter CTA ("Arrange a conversation"). |
| Activation group page | Replaces blocks 3 to 6 with: "What Activation means here" (strategy-to-execution, not ongoing operations), then six service cards. Blocks 7 to 13 as standard. |

---

## T4. Expertise hub (`/expertise/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Our expertise", one paragraph explaining that these are the growth problems MGA is known for and that each cuts across services and sectors | Always |
| 2 | Theme cards | Five cards in nav order, each with a definition line and the number of case studies and insights available | Always |
| 3 | How themes and services connect | Same cross-reference grid as T2 block 4, flipped so themes are down the side | Always |
| 4 | Latest insights across themes | Six newest insights tagged to any theme | Always |
| 5 | CTA | Contact | Always |

---

## T5. Expertise theme (`/expertise/{theme}/`)

Purpose: prove MGA understands the problem, then hand off to the services that solve it. This page describes problems and outcomes. It never describes how a service is delivered.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Theme name as H1, one-sentence framing of the problem space, CTA (`/contact/?topic={theme}`) | Always |
| 2 | Our view | Three to five short paragraphs: what MGA believes about this theme, common failure modes, what good looks like. This is the unique content on the page. | Always. 300 to 600 words. |
| 3 | Where we help | The services applied to this theme, each with one line on how it applies to this theme specifically, linking to the service page | Always. Curated per theme. Minimum two. This block is the hand-off to the canonicals. |
| 4 | Proof | Case studies tagged to this theme, auto, up to six | Always when at least two exist. Below two, the theme page should not have been published (see `02-sitemap.md`). |
| 5 | Insights | Insights tagged to this theme, auto, up to six, with a link to `/insights/?expertise={theme}` | Always when at least two exist |
| 6 | Sectors where this matters | Small row of the sectors with case studies tagged to both this theme and the sector | Conditional: at least one such case study exists. Links to `/sectors/{sector}/`. |
| 7 | People | Team members who lead on this theme | Editorial |
| 8 | Related themes | The other four themes as links | Always |
| 9 | CTA | Contact with topic pre-set | Always |

---

## T6. Sector light landing (`/sectors/{sector}/`)

Purpose: reassure "you have worked with businesses like mine" and route to proof. Deliberately short. No sector point of view.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Sector name as H1, two or three sentences on the kind of work MGA does in this sector and the clients it has worked with | Always. 150 to 300 words maximum. |
| 2 | Client logos | Logos of clients in this sector | Always |
| 3 | Case studies | All case studies tagged to this sector, auto | Always. If fewer than three, the page is noindex. |
| 4 | Services most used here | The two or three services most frequently tagged alongside this sector, auto from case study tags, with links | Always |
| 5 | Themes that matter here | Themes tagged alongside this sector, auto from case study tags | Conditional: at least one |
| 6 | Insights | Insights tagged to this sector, auto, up to three | Conditional: at least two exist |
| 7 | Sector lead | One team profile flagged as sector lead | Editorial |
| 8 | CTA | Contact | Always |

The sector index (`/sectors/`) is T6 block 1 (generic) plus a four-card list and CTA.

---

## T7. Work hub (`/work/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading "Our work", one line | Always |
| 2 | Filters | Three filter groups: Service (Growth Strategy, Proposition Innovation, Activation with its six children, CEO Advisory), Expertise (five), Sector (four). Multi-select within a group, AND across groups. Filters update the URL query string. | Always |
| 3 | Results grid | Case study cards: client, one-line result, service and theme tags. Newest first by default, pinned items first. | Always. Paginated or load-more after 12. |
| 4 | Empty state | If a filter combination returns nothing: message plus links to the nearest broader filter | Conditional |
| 5 | CTA | Contact | Always |

---

## T8. Case study (`/work/{client}/`)

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Client name, one-line headline result, sector, services used (linked), themes (linked) | Always |
| 2 | At a glance | Three to four headline numbers or outcomes | Always |
| 3 | The challenge | Two to four paragraphs | Always |
| 4 | What we did | Narrative of the approach, with the services referenced inline and linked. Does not explain what the service is in general; links do that. | Always |
| 5 | The result | Outcomes, quantified where permitted | Always |
| 6 | Client quote | Attributed quote | Editorial |
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
| 2 | Featured | One curated insight, large | Editorial. Falls back to newest. |
| 3 | Filters | Type (article, report, event), Expertise, Service, Sector | Always |
| 4 | Results list | Cards: title, type, date, theme tags, reading time | Always. Paginated after 12. Past events hidden by default. |
| 5 | Newsletter sign-up | Inline form or link to `/newsletter/` | Always |

---

## T10. Insight article (`/insights/{slug}/`)

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
| 2 | Who we are | Origin, what MGA believes about growth, why customer-led | Always |
| 3 | What makes us different | Three to four points, one of which is the strategy-to-activation model | Always |
| 4 | Leadership | Founders and partners with links to profiles | Always |
| 5 | How we work teaser | Paragraph plus link to `/about/how-we-work/` | Always |
| 6 | Clients | Logo wall | Always |
| 7 | Careers teaser | Link to `/about/careers/` | Always |
| 8 | CTA | Contact | Always |

---

## T12. Team listing (`/about/team/`) and Team profile (`/about/team/{name}/`)

Team listing:

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Heading, one paragraph | Always |
| 2 | Leadership | Profile cards | Always |
| 3 | Consultants | Profile cards | Always |
| 4 | Advisors | Profile cards for Side-by-Side advisors, with a one-line note and link to `/services/ceo-advisory/` | Conditional: at least one advisor is flagged |
| 5 | Careers CTA | Link to `/about/careers/` | Always |

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

Purpose: explain method without turning it into a product.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | "How we work" | Always |
| 2 | Principles | The ways of working MGA holds to, as a short list with a paragraph each | Always |
| 3 | Engagement shapes | The common shapes of engagement: strategy project, strategy into activation, embedded growth office, advisory retainer. Each links to the relevant service or group. | Always |
| 4 | Frameworks and tools | Named frameworks (for example CIVD) with a paragraph each. Frameworks are explained here once and referenced from service pages. | Always |
| 5 | Working with AI | How AI-powered activation works in practice; links to Data Agents and AI Enablement | Always |
| 6 | What clients say | Two or three quotes about the experience of working with MGA | Editorial |
| 7 | CTA | Contact | Always |

---

## T14. Contact (`/contact/`)

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
| T2 Service hub | `/services/` |
| T3 Service detail | `/services/{service}/` including `/services/activation/` and `/services/ceo-advisory/` with noted variations |
| T4 Expertise hub | `/expertise/` |
| T5 Expertise theme | `/expertise/{theme}/` |
| T6 Sector light landing | `/sectors/`, `/sectors/{sector}/` |
| T7 Work hub | `/work/` |
| T8 Case study | `/work/{client}/` |
| T9 Insights hub | `/insights/` |
| T10 Insight article | `/insights/{slug}/` |
| T11 About | `/about/` |
| T12 Team listing and profile | `/about/team/`, `/about/team/{name}/` |
| T13 How we work | `/about/how-we-work/` (Careers uses a simplified T13 with roles list) |
| T14 Contact | `/contact/`, `/contact/thank-you/` |
| Generic content | Legal pages, `/newsletter/`, `/search/`, `/404/` |
