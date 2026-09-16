# 03. Page layouts (v5)

Templates for each page type, described as an ordered list of blocks. For every block: what it contains, where its content comes from, and when it appears. This is structure, not visual design. Block names are working names for the CMS and wireframes.

v4 changes (`v4-simplification.md`): Home goes from seven blocks to six; every template follows the **one chip dimension, three visible** rule set out below; the Work and Insights hubs open with one filter group; the sector index page is gone.

**v5 changes** (`v5-refinements.md`): the pages catch up with the best of the peer set without the chrome growing. Home block 2 gains one line under the triangle (R2). The Services hub (T2) becomes the Growth Architecture story: H1 "Our Growth Architecture", a "Where are you starting from?" block, and one plain sentence, service cards and one case per pillar; the separate Proof block goes (R1 to R3). Service pages (T3) open the Why with three situations, move Proof up to follow What we do, add a numbers line where the deck gives a number, and tighten each service module so every slide's structure has a stated home (R6). The Activation group page adds "Which of the six do you need?" (R5). People becomes Always when a lead is flagged, and the Team listing gains an optional Associates group (R7). How we work names the five frameworks and tools explicitly (R3). The chip rule, filters, and every other template are unchanged.

Related: `05-content-matrix.md` shows the same information as a grid; `04-canonicals-and-seo.md` sets the linking rules the "Related" blocks follow.

---

## On-page tags: one dimension per page type

Gary's v4 feedback: page tags were too busy. The cause was structural. The IA has three intersecting dimensions (services, expertise themes, sectors) and v3 showed all three as tags wherever they were tagged. The cross-referencing model is right; showing it everywhere is not.

The rule: **each page type shows tags from one dimension only, capped at three visible.** The other dimensions still exist as CMS tags, drive filters and auto modules, and appear as blocks (a list of cards, a "Where we help" list) where the template calls for them. They are not displayed as a second tag row.

Working notes in the wireframe sidebar (weight, primary keyword, related URLs) are review annotations. They are not live page modules. The **Page modules** catalogue (`/catalogue/`) shows live blocks only (D-59). Do not call these "chips" in UI copy.

| Page type | Tag dimension | Cap | Not shown as tags |
|---|---|---|---|
| Home | Expertise (one row of plain text links) | 5 | Services (the triangle is three blocks, not tags), sectors, insight types |
| Services hub | None | | The expertise line is one sentence with a link |
| Service detail | Expertise (Related expertise block) | 3 | Sectors; other services (Related services is two or three cards) |
| Expertise theme | None | | Services (Where we help is a list with a line each); sectors (row cut) |
| Sector landing | None | | Themes (row cut); services (Services most used here is a short list) |
| Work hub | Service, one per card | 1 | Themes and sectors on cards; they remain filters |
| Case study | Services used (hero) | 3 | Sector and themes in the hero. Related expertise appears once, at the foot, capped at 3 |
| Insights hub | Expertise, one per card | 1 | Type is a word in the meta line, not a tag |
| Insight | Expertise (hero) | 3 | Services (Related services is a block, max 2); sectors |
| Team profile | None | | Focus is a sentence with links |

Where a page has more tags than the cap, the template shows the first three (editor-ordered) and nothing else. There is no "+2 more" control. The full set is visible on the filter hubs.

Sectors are shown as tags nowhere. They live in the Work and Insights filters (behind More filters), the footer, and their own light landings.

---

## Conventions used in every template

| Term | Meaning |
|---|---|
| **Always** | The block is present on every page of this type. |
| **Conditional** | The block appears only when the stated condition is true. If the condition fails, the block is skipped and nothing takes its place. |
| **Editorial** | The block appears when a content editor chooses to add it. |
| **Auto** | Content is pulled automatically from tags and relationships in the CMS. |
| **Curated** | Content is hand-picked by an editor. Falls back to Auto if nothing is picked. |
| **CTA** | Call to action. Primary CTA is a button to `/contact/` (Work with us, or Work for us on careers routes), optionally with `?topic=`. Secondary CTA is a text link, usually "See our work" or "What we do". |

Global blocks on every page, not repeated below: Header (see `01-primary-navigation.md`), Breadcrumbs (all pages except Home), Footer (services, expertise, sectors, company including The Nutshell, legal, search), cookie bar.

Block order matters. The first two blocks on any page must answer "where am I and is this for me?" before any proof or detail.

---

## T1. Home (`/`)

Purpose: say who MGA is for, show the Growth Architecture triangle once, and route into services, thinking, work and expertise. Home carries no unique long-form content. Everything it shows exists in full somewhere else. Home has one chip set (block 5), one CTA path (Contact, in the hero and again at the foot) and no tags on any card.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Positioning statement from Source B ("Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth"), the line "Strategy that works. Execution that delivers.", one primary CTA to Contact, one text link to `/services/` ("What we do"). Showreel placeholder beneath (film later). | Always. |
| 2 | Trusted partners | Heading "Trusted partners" and a thin row of 8 client logos. | Always. Logos link to the case study if one exists, otherwise to `/work/`. High, before What we do (MURAL). |
| 3 | Growth Architecture triangle | Three blocks, each with the pillar label and the same short pillar line as the mega-nav: Growth Strategy ("Where and how you grow"), Activation Services ("Turning strategy into results"), CEO Advisory ("One-to-one support for leaders"). Each block links to its pillar page. All three pillars use the same contrast and weight. CEO Advisory is not greyed out. Section heading "What we do". Beneath the three blocks, one line in small type, the **triangle line**: "Strategy first. Activation to deliver it. Advisors alongside." (v5, R2), with a text link "Our Growth Architecture" to `/services/`. | Always. The triangle is drawn once, here. No pyramid diagram, no Source B one-liners, no second rendering. The three pillar lines and the triangle line are shared data with the mega-nav and the Services hub (`05-content-matrix.md`). The triangle line is the only sentence in this block. |
| 4 | Our thinking | Heading "Our thinking". One featured report card and one article card, then a text link "All thinking" to `/insights/`. | Always. Placed after the triangle and before Our work so thinking is not a strip at the foot (`thinking-placement.md`). Not a reports grid. |
| 5 | Our work | Three case studies, curated, spanning at least two pillars. Card: image, client, one-line result. No tags. Link "All work". A quote with the work. | Always. Curated; falls back to newest. |
| 6 | Awards | Heading "Awards" and a short logo row. FT sits here, not in the hero. | Always. |
| 7 | Expertise | Heading "Growth problems we know best" and the five theme names as plain text links in one row. No descriptors, no cards, no counts. | Always. Cap is five; a sixth theme does not appear here until one of the five is retired. |
| 8 | Closing CTA | "Tell us about your growth challenge" and a Contact button | Always |

What Home does not do: no long "about us" copy, no full service descriptions, no methodology explanation, no team grid, no sector block, no filter chips, no type or theme tags on cards, no reports grid. Each of those has a page.

v1 had ten blocks here. v2 and v3 had seven, with the triangle drawn twice (three cards plus a pyramid). v4 has six: the logo strip is folded into the hero, the pyramid is gone, the cards carry no tags, and the expertise row is names only (D-41). v5 keeps six and adds one line to block 2. The MURAL pass split logos and awards out of the hero. This pass moves thinking from the foot to after the triangle (D-55).

---

## T2. Services hub: Growth Architecture (`/services/`)

Purpose: this is the Growth Architecture page. Name the system, show the three pillars and how they connect, let a visitor find their own situation, and route to the right service with proof beside it, in one scroll.

v5 rebuilds this template (R1 to R3). The competitor evidence: Prophet and Yonder give a buyer two ways in (by problem, by capability); Elsewhen and Baringa put proof directly under each offer; Lippincott and Ellipsis give their named system a visible home. The deck evidence: slide 1's title, slide 2's triangle logic and slide 3's pillar one-liners had no stated home in v4 (`andy-deck-coverage.md`).

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Intro | Eyebrow "What we do". H1 **"Our Growth Architecture"**. The strapline "Strategy that works. Execution that delivers." Two short paragraphs from Source B: the path from strategy to execution has become complex and fragmented; Growth Architecture combines market-leading strategic thinking with AI-powered activation services. | Always. v4 had the H1 and subheading the other way round (D-51). This is where the strapline lives now that it is out of the mega-nav (D-34). |
| 2 | The triangle | Section heading "Three ways we work with you". The same three-block triangle as Home block 2, larger, with the same three pillar lines, and the same triangle line beneath: "Strategy first. Activation to deliver it. Advisors alongside." Each block anchors to the pillar section below and links to the pillar page. | Always. Shared data with Home and the mega-nav. |
| 3 | Where are you starting from? | Heading "Where are you starting from?" and seven situations, one line each, each a link: We need to decide where and how to grow (Growth Strategy); We need a new proposition, loyalty or membership offer (Proposition Innovation); We need to understand our customers better (Customer Research and Insight); Our journeys or website are not converting (Experience Engineering); Our strategy is not turning into results (Activation Services); We want AI to pay off (AI Enablement); I want a sounding board I trust (CEO Advisory). | Always (v5, R1, D-46). Seven lines, eight words or fewer each, no descriptors, no icons, each destination once. Wording is a proposal for Andy; each line must be something a prospect would say. |
| 4 | Pillar 1: Growth Strategy | Pillar heading and pillar line. One plain sentence from the slide 3 one-liner: "We work out where the growth is and design the propositions that win it, using our Customer, Innovation, Value and Delivery frame" (the frame links to `/services/growth-strategy/#civd`). A compact four-cell CIVD module on this section (Customer, Innovation, Value, Delivery), then two service cards (Growth Strategy, Proposition Innovation) each with a two-line summary and link. One case line: client and one-line result, curated, tagged to this pillar. | Always. First pillar section. The case line carries no tags (v5, R2, D-47). CIVD stays a module, not a page (`strand-gap-check.md`). |
| 5 | Pillar 2: Activation Services | Pillar heading and pillar line. One plain sentence: "We build the bridge from strategy to results: new operating models and AI-powered, human-led delivery" linking to `/services/activation/`. Six service cards in nav order, each with a one-line summary written for the card (the card is where the v3 subtitle wording can be reused). One case line, curated, tagged to an Activation service. | Always |
| 6 | Pillar 3: CEO Advisory | Pillar heading and pillar line. One plain sentence: "Experienced growth leaders alongside you, on retainer, to help you make good decisions." Up to three advisor profile cards (auto from the advisor flag), link "Our advisors" to `/services/ceo-advisory/#advisors`. One client quote line if one exists for this offer, otherwise nothing. | Always. Third and visibly quieter than pillars 1 and 2, but a full section, not a footnote. The advisors are this pillar's proof. |
| 7 | Expertise | One sentence, "We apply these services to the growth problems we know best", with a single link to `/expertise/` | Always. One line, one link. The five names are on Home, in the footer and on the hub. |
| 8 | Closing CTA | Contact | Always |

Eight blocks, as v4. The v4 Proof block (three cases at the foot) is replaced by one case inside each pillar section; the v4 "one paragraph" under pillars 2 and 3 becomes one sentence under each of the three. v1 carried a services-against-themes cross-reference grid here; v2 and v3 a five-link strip; v4 one sentence and one link (D-42), which stands.

What this page does not do: no frameworks list (that is How we work, T13 block 4), no team grid, no insights, no sector block, no chips.

---

## T3. Service detail (`/services/{service}/`)

Used for all eight canonical services and, with the noted variations, the Activation group page and CEO Advisory.

v5 changes (R6, D-48): the Why block opens with three situations (Prophet's pattern); Proof moves up to follow What we do (Elsewhen and Baringa put proof under the offer); a numbers line appears under the hero where, and only where, the deck gives a number (Ekimetrics' pattern); People is Always when a lead is flagged (Baringa); and each service module names the structure its slide has.

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Service name as H1 (the nav label, exactly), a one-line plain definition carrying the searched terms (this is where the v3 mega-nav subtitle wording now lives: for example Experience Engineering, "Customer experience (CX), website and digital design, build and testing"), one-line "who this is for", primary CTA (`/contact/?topic={service}`). No chips in the hero. For services renamed from the deck (Customer Research and Insight, AI Agents for Marketing, Operating Model Design) a small "also known as" line under the H1 names the deck term: "Our Customer Intelligence practice", "Data Agents, built in AgentLab", "Our Operating Architecture framework". | Always. The "also known as" line is Conditional: only on renamed services. |
| 2 | Numbers line | One line of figures from Source B, in the deck's own words: Experience Engineering "Over 3x EBITDA return on investment, consistently"; AI Agents for Marketing "4 weeks to audit your data. 6 weeks to your first agents." | Conditional: only where Source B gives a figure. Nothing is invented for the other services (v5, R6). |
| 3 | Pillar context | One line placing the service in the triangle ("Part of Activation Services" or "Part of Growth Strategy") linking to the pillar page | Always for Activation services and Proposition Innovation. Omitted for Growth Strategy (it is the pillar) and CEO Advisory (it is the pillar). v3 also had previous / next service links here; cut in v4 as chrome (D-42). |
| 4 | Why | Opens with **three situations**, one line each, that lead clients to this service ("You are here if..."), then two to four short paragraphs. Source B provides a "Why" paragraph for every service; start from it. | Always. The three lines are the page-level version of the hub's "Where are you starting from?" (v5, R6). |
| 5 | What we do | The service explained: scope, typical deliverables, what the client gets. Source B provides a "What" section for every service. Subheadings carry the search-friendly terms. | Always. This is the canonical description; no other page restates it. |
| 6 | Proof | Case studies tagged to this service, auto, up to four, with the option to pin one. Cards: client and one-line result, no tags. Source B names example clients per service. | Always when at least one tagged case study exists. If none, show a client logo list instead. Moved up from block 7 in v4 so proof sits directly under the offer (v5, R6). |
| 7 | How it works | Typical phases or shape of the engagement, named where Source B names them (table below), duration where Source B gives it, who from MGA is involved | Always. Links to `/about/how-we-work/` for general methodology rather than repeating it. |
| 8 | Service-specific module | Varies by service (table below) | Conditional per service |
| 9 | Related expertise | Themes where this service is commonly applied, as chips, each with one line on the intersection | Always. Set per service in the CMS. Minimum one, **maximum three visible**. This is the one chip dimension on a service page. |
| 10 | Related services | Two or three services most often bought alongside this one, as cards | Always. Curated. Cards, not chips. |
| 11 | Insights | Up to three insights tagged to this service, auto | Conditional: at least one tagged insight exists |
| 12 | People | One to three team profiles flagged as lead for this service, auto, with the option to curate | Always when at least one profile is flagged as lead (v5, R7). v4 had this as Editorial. |
| 13 | FAQ | Three to six questions clients ask about this service, marked up as FAQ structured data | Editorial. Recommended for every canonical service because it captures long-tail search phrasing. |
| 14 | Closing CTA | Contact with topic pre-set | Always |

Service-specific module (block 8) and named How it works phases (block 7), drawn from Source B. Anchors are the linkable homes listed in `02-sitemap.md`.

| Service | How it works (block 7) | Module (block 8) |
|---|---|---|
| Growth Strategy | Shape of a strategy engagement; Andy's copy pending | The CIVD frame (Customer, Innovation, Value, Delivery) from the Source B Growth Strategy slide, as a four-part diagram with a paragraph each, anchored `#civd`. Plus a link to Proposition Innovation as the natural next step. Candidate H2s for the What we do block, from the deck appendix's Growth Strategy layer: North Star; Growth priorities; Demand signals; Scenario planning. Source B marks this slide "to be updated from existing content on growth architecture / approach". |
| Proposition Innovation | Shape of a proposition engagement; Andy's copy pending | How MGA designs new value propositions that grow sustainable customer value, with the proposition types named on the call (loyalty, membership, subscription, D2C) each linking to its expertise theme. |
| Customer Research and Insight | Insight project or capability build; typical durations to confirm | The Why block's hook is the deck's "So What": AI makes research faster and cheaper but creates multiple versions of the truth; the promise is getting to the so-what faster. Then two offers as sub-sections with plain H2s ("Research projects": qualitative, quantitative, surveys, digital listening; "Always-on customer insight": voice of the customer tools, panels, intelligence platforms) and the input types as a scannable list: digital listening, qual research, quant research, customer data analytics, internal knowledge, external market data. "Customer Intelligence" is used in body copy as the practice name. |
| Experience Engineering | **Four named phases from the deck: Find, Redesign, Test, Scale.** One line each. | Three sub-sections with their own plain H2s and anchors: Customer experience (CX) design (`#customer-experience`); Website and digital product design and build (`#website-and-digital`); User research and testing, with customer and value analytics (`#research-and-testing`). Each two paragraphs. The 3x EBITDA figure is the numbers line (block 2). Body copy may call the team a squad once glossed ("our Experience Engineering squad: insight, value analytics, CX design and digital technology specialists"). Reference model: Dayinsure and Key Group. |
| AI Agents for Marketing | **Timeline from the deck: 4 weeks audit, 6 weeks first agents, ongoing portfolio.** | H2 "AgentLab", anchored `#agentlab`: the catalogue grouped as in Source B, with the deck's named agents as entries. Reporting and Analytics: Effectiveness agent, Attribution mapping agent, Performance planning agent. Data and Infrastructure: CDP data clean-up agent, Tagging and data collection agent, Integration discovery agent. Strategy and Planning: Segmentation builder agent, Customer journey mapping agent, Audience opportunity agent. Automation and Execution: Channel optimisation agent, Test and learn agent, QA and deployment agent. Agents are entries, not pages (D-15). "Data Agents" and "AgentLab" are named in the heading. The grouping of individual agents is Andy's to confirm. |
| Operating Model Design | Diagnose the current model, design the adaptive model, implement; durations to confirm | The four qualities of an adaptive operating model (grounded in customer value growth; fuelled by high-quality data; redesigned around humans and AI agents; orchestrated and linked to impact) and the Source B appendix diagram (Growth Strategy; Data and Tools; New Work Units; Orchestration with Culture, Value, Capability; value streams of AI agents and humans) as a captioned figure titled "Our Operating Architecture framework", anchored `#operating-architecture`. The caption links Orchestration to Growth Office, which is the same three words. |
| Growth Office | **Two phases from the deck: interim activation support, then establishing the new ways of working.** | The three connected elements from Source B (Culture, Capability, Value) as sub-sections. Body copy uses the plain terms "interim growth team" and "programme office" alongside the label. |
| AI Enablement | Maturity assessment, then a bespoke programme across the three areas | Three programmes as sub-sections with plain H2s (AI skills and adoption; Finding where AI pays off (value cases); New business models with AI) with the maturity assessment as the entry step. Body copy names the expert network ("AI practitioners from our expert network") and links to the Team listing's Associates group when published. Cross-link to AI Agents for Marketing for tooling. |
| CEO Advisory (Side-by-Side) | How the retainer works: virtual or in person, disciplined but flexible, personality-led | **Side-by-Side**, anchored `#side-by-side`: Why (driving customer-led growth is demanding and lonely) and What (a select group of senior leaders armed with Manifesto thinking and frameworks; adaptive and personality-led; retainer-based so practitioners focus on delivering value, not selling). This is mega-nav strand 1. **Advisor profiles**, anchored `#advisors`, pulled from `/about/team/` where the person is flagged as advisor: this block is mega-nav strand 2. No FAQ module. Quieter CTA ("Arrange a conversation"). |
| Activation group page | n/a | Replaces blocks 4 to 8 with: the bridge in one line, in plain words ("A brilliant strategy only counts if it gets executed and the value shows up. Activation is how we get you there: hands-on, AI-powered, human-led, and not ongoing operations"); then **"Which of the six do you need?"**, one line per service (v5, R5, D-52): Customer Research and Insight, "you need to understand customers faster and agree one version of the truth"; Experience Engineering, "a journey, product or website is underperforming and you want it found, fixed, tested and scaled"; AI Agents for Marketing, "your customer data is holding marketing back and you want agents doing the work"; Operating Model Design, "you need to redesign how teams, data and AI agents work together"; Growth Office, "you need an interim team to get the strategy delivered and the value tracked"; AI Enablement, "you want your people to use AI well and to find where it pays off". Then six service cards, each with a one-line summary. Blocks 9 to 14 as standard. |

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
| 4 | Results grid | Case study cards: client, one-line result, one service tag (the primary service). Newest first by default, pinned items first. | Always. Paginated after 12. Theme tags on cards were cut in v4. |
| 5 | Empty state | If a filter combination returns nothing: message plus a control to clear filters | Conditional. Shown in the wireframe as a labelled stub. |
| 6 | Related thinking | Two thinking items plus All thinking | Always |
| 7 | CTA | Primary Contact, secondary See our work | Always |

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
| 5 | Empty state | If a filter combination returns nothing: message plus a control to clear filters | Conditional. Shown in the wireframe as a labelled stub. |
| 6 | Events and news | Launch events and recaps. The Nutshell sign-up. | Always. A separate `/events/` page only if there is enough recap content (open decision). |
| 7 | Related services | Links to What we do, Expertise, Our work | Always |
| 8 | Newsletter sign-up | Inline form or link to `/newsletter/` (The Nutshell) | Always |

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
| 4 | Side-by-Side advisors | Anchor `#advisors`. Profile cards for advisors, with a one-line note and link to `/services/ceo-advisory/`. The CEO Advisory page links here. The mega-nav's "Our advisors" (v5, D-49) lands on the CEO Advisory page's own advisor block, not here. | Conditional: at least one advisor is flagged. |
| 5 | Associates and expert network | Profile cards for associates: the AI practitioners of the AI Enablement expert network (Source B, slide 12) and any Side-by-Side advisor who is an associate rather than staff. One-line intro. The Foundation's team page uses the same group. | Conditional: at least one profile is flagged as associate (v5, R7, D-53). |
| 6 | Careers CTA | Link to `/careers/` | Always |

The intro (block 1) may call the team "our Growth Architects" once, the deck's own term (slide 10). Optional.

Team profile:

| # | Block | Content | Rule |
|---|---|---|---|
| 1 | Hero | Name, role, one-line focus, contact route (LinkedIn or contact form) | Always |
| 2 | Biography | Two to five paragraphs | Always. Under 100 words means noindex. |
| 3 | Focus | Services and themes this person leads on, linked. A profile flagged as **lead** for a service surfaces in that service's People block (T3 block 12). | Always |
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
| 4 | Frameworks and tools | The five named things, each with a paragraph and a link to its anchored home (v5, R3, D-51): **Growth Architecture** (the system: strategy, activation, advisory) to `/services/`; **Customer, Innovation, Value and Delivery** (the Growth Strategy frame) to `/services/growth-strategy/#civd`; **the adaptive operating model, our Operating Architecture framework** to `/services/operating-model-design/#operating-architecture`; **AgentLab** (the catalogue of marketing and data agents) to `/services/ai-agents-for-marketing/#agentlab`; **Side-by-Side** (the advisory retainer) to `/services/ceo-advisory/`. Frameworks are explained here once and referenced from service pages. This is the one place all five are listed together; Lippincott and Ellipsis do the same on a hub, Prophet and Ekimetrics under About. | Always |
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
| 1 | Intro | Heading, one line | Always |
| 2 | Work with us | Form: name, company, email, topic (`?topic=`), message. Primary client enquiry. | Always. Anchor `#work-with-us`. |
| 3 | Work for us | Form: name, email, message. Speculative applications. Roles live on Careers. | Always. Anchor `#work-for-us`. |
| 4 | Direct contact | Email, phone, office address. Response time and confidentiality. | Always |
| 5 | The Nutshell | Link to `/newsletter/` | Always |

Thank-you page: confirmation, then three curated links (a service, a case study, an insight).

---

## T17. Page modules catalogue (`/catalogue/`)

Wireframe utility only. Not a live client URL. No working-notes sidebar.

Each live unit is named and given one interaction type (Button, Text link, Card, Tag, Filter, Static). The catalogue page is the index. The named set, random-box list, and link-versus-button rules live in `docs/wireframe-fresh-review.md` §2.

Ordered live blocks: header Contact, mega-nav hub and strands, breadcrumb, cookie bar, hero CTA pair, closing CTA band, metric box, service / theme / case / report / article / person / role cards, triangle tile, page tag, filter bar, situations list, row of text links, related list, case line, pagination, empty state, logo strip, quote, video 16:9, CIVD four-cell, article body, Work with us / Work for us forms.

---

## T18. Utility stubs

| URL | Blocks |
|---|---|
| `/privacy-policy/`, `/cookie-policy/`, `/terms/`, `/accessibility/` | Hero + summary stub. Cookie policy also names the site-wide cookie bar. Legal review before launch. |
| `/search/` | Query field, example results, empty state. |
| `/newsletter/` | The Nutshell sign-up. |
| `/404/` | Message, primary What we do, secondary Our work and Contact, plus search. |

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
| T17 Page modules catalogue | `/catalogue/` (wireframe only) |
| T18 Utility stubs | `/privacy-policy/`, `/cookie-policy/`, `/terms/`, `/accessibility/`, `/search/`, `/newsletter/`, `/404/` |
