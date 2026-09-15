# 06. Decisions log (v3)

Every significant IA decision, the options considered, what was chosen, and the trade-off. Each entry names the sources it rests on. The five sources are summarised in `00-sources.md`:

- **Source A**: Gary's IA feedback document (structure, three intersecting dimensions, one canonical home per topic, About and Careers split).
- **Source B**: Andy's Growth Architecture Services deck, working draft Sept 26 (the triangle, service grouping, Why and What copy per service).
- **Source C**: Otter transcript of the Shed x Manifesto check-in, 7 September 2026 (weighting, language, sectors versus themes, site role).
- **Source D**: Gary's direction of 14 September after reviewing v1 (simplify, make the triangle obvious, CEO Advisory visible as a pillar, themes calm).
- **Source E**: Gary's v3 wording brief of 15 September (plain, search-friendly labels; subtitles for coined terms; deck is not website copy).

Precedence: structure from A; service taxonomy from B; weight and order from C; simplification from D; nav wording from C and E. Where B and E conflict on what a service is called in the nav, E wins: B decides what the services are, not what the site calls them.

---

## Why v3 exists

Gary reviewed v2 on 15 September and raised one concern: the nav labels may have taken Andy's deck wording too literally (Source E). v2 had made that literal use a rule ("service labels are used exactly as in the Source B deck; do not abbreviate or rename in the nav", v2 `01-primary-navigation.md` section 3.3). The rule contradicted what Andy and Gary had already agreed on the 7 September call (Source C): plain language, HPX failed and clients look for CX, the deck is not website copy, simplification helps.

| Problem with v2 | Evidence | What v3 does instead |
|---|---|---|
| **Deck labels used verbatim, by rule.** Customer Intelligence, Data Agents and Operating Architecture are internal names that no prospect searches. "Data Agents" can read as data brokerage. | Source E; Source C ("deck is NOT website copy") | Rule replaced with "what would a prospect type to find this?" Three services renamed to the searched term (D-27, D-28, D-29). Deck terms kept on the page and as redirects. |
| **Subtitles mixed plain English with deck phrasing.** "Gets to the so what faster", "where to play and how to win", "the bridge from strategy to execution", "value cases", "adaptive operating models for the age of AI". | Source E ("no unexplained jargon"); Source C ("simplification of language is helpful") | All thirteen subtitles rewritten in plain English, each carrying at least one term a prospect would search (D-30). |
| **Acronyms in the nav.** "Side-by-Side (SxS)", "D2C", "CX" on its own. | Source E; Source C (HPX failed as a term) | Acronyms removed or expanded: "Side-by-Side", "direct-to-consumer", "customer experience (CX)" (D-31). |
| **IA vocabulary leaking into the visitor's view.** "Expertise themes" as a heading and link. | Source E (plain language) | Visitor sees "Expertise"; "expertise themes" stays as the IA term in the documents (D-32). |

What v2 got right and v3 keeps, unchanged: three columns in the order Growth Strategy, Activation Services, CEO Advisory; CEO Advisory quieter with an advisors link; expertise and sectors out of the mega-nav; the five-item header; Our work as a plain link; the sitemap structure and weights; Home as a page; flat service URLs; every rule about canonicals, linking and indexing.

---

## Why v1 was rejected

Gary reviewed v1 on 14 September and rejected it (Source D). Recorded here so the reasons are not lost.

| Problem with v1 | Evidence | What v2 does instead |
|---|---|---|
| **The navigation was too complicated.** The What we do mega-nav had four columns (Growth Strategy, Activation Services, Expertise, Featured) plus a bottom strip of three links (All services, CEO Advisory, Who we work with): 22 links and 21 destinations in one panel. Gary: "very complicated, too much going on". | Source D | Three columns matching the three pillars, one heading line, one thin footer row of three text links. 17 links, 14 destinations, and everything above the footer row is a service. |
| **Andy's triangle was not visible.** CEO Advisory, one of the three pillars in Source B, was a small text link in the bottom strip. Expertise themes and a featured case study took the space a pillar should have had. Gary "could not see the triangle contents clearly", specifically CEO Advisory. | Source D, checked against Source B slides 2 and 3 | CEO Advisory is column 3 of the mega-nav, with a heading, subtitle and two links, styled quieter than columns 1 and 2 but structurally a peer. Home and the Services hub draw the triangle as three blocks with the Source B one-liners. |
| **The first brief under-supplied source material.** v1 was produced without the full text of Sources A, B and C, so it invented a hybrid: it read "downweight CEO Advisory" as "hide CEO Advisory", read "themes are a dimension" as "themes get a mega-nav column", and attached CIVD to Proposition Innovation when the Source B Growth Strategy slide shows CIVD is the Growth Strategy frame. | Source D; full Sources A to C now in `00-sources.md` | Every decision below cites the source it rests on. Themes moved to the Insights dropdown and footer. CIVD moved to Growth Strategy. Sources are recorded in `00-sources.md`. |
| **Expertise competed with services.** A fourth mega-column of five themes read as a fourth pillar and diluted the triangle. | Source D; Source C (Andy: "simple layout, but being able to see this cross reference on themes and sectors, so they're discoverable, but not too confusing") | Themes are a real dimension in the sitemap (`/expertise/`, Supporting weight, cross-linked from every service and case study) but appear in the header only as the second column of the Insights dropdown and one text link in the mega-nav footer row. |
| **Nav noise generally.** "Column 1 / Column 2" labels, nine-word descriptors, a featured card with an image, an Our work dropdown of ten filter links, an Insights dropdown that repeated the theme column. | Source D | Plain one-line subtitles under labels only where a label is opaque (Source C on Experience Engineering). Featured work moved to Home and the Work hub. Our work is a plain link. Insights dropdown trimmed. |

What v1 got right and v2 keeps: services canonical and flat under `/services/`; Home a page not a hub; sectors light; methodology under About; Growth Strategy first; Activation framed as strategy-to-execution; Experience Engineering label kept with plain-language sections; no thin archive pages; filters as query strings.

---

## Summary of v3 decisions (D-26 to D-33)

| ID | Decision | Sources |
|---|---|---|
| D-26 | Nav labels use the searched term; deck labels are kept only where they agree with it or are Manifesto terms that earn a subtitle | C, E |
| D-27 | Customer Intelligence becomes Customer Research and Insight (`/services/customer-research/`) | C, E |
| D-28 | Data Agents becomes AI Agents for Marketing (`/services/ai-agents-for-marketing/`) | B (strapline), C, E |
| D-29 | Operating Architecture becomes Operating Model Design (`/services/operating-model-design/`) | B (slide 3 "Operating Models"), E |
| D-30 | Experience Engineering, Growth Office, Proposition Innovation, AI Enablement, Activation Services and Side-by-Side keep their labels; all thirteen subtitles rewritten in plain English with searched terms | C, E |
| D-31 | No acronyms in the nav: SxS removed, D2C expanded, CX always written "customer experience (CX)" | C, E |
| D-32 | Visitor-facing label for the themes dimension is "Expertise", not "Expertise themes" | E |
| D-33 | The five header labels stay after review against "Services" and "Case studies" | A, E |

## Summary of v2 decisions

| ID | Decision | Sources | Changed from v1? |
|---|---|---|---|
| D-01 | The mega-nav is the triangle: three columns, Growth Strategy, Activation Services, CEO Advisory, in that order | B, C, D | Yes |
| D-02 | CEO Advisory is a visible third column, quieter, with an advisors link | B, C, D | Yes |
| D-03 | `/services/` is the Growth Architecture page; no separate `/growth-architecture/` | A, B | Yes (v1 had no Growth Architecture concept) |
| D-04 | Expertise themes leave the mega-nav; home in Insights dropdown, footer and one text link | A, C, D | Yes |
| D-05 | One-line plain-English subtitles under service labels (wording revised in v3, see D-30) | C, D | Yes |
| D-06 | Featured case study removed from the mega-nav | D | Yes |
| D-07 | Our work is a plain header link; filters live on the hub | A, D | Yes |
| D-08 | Sectors out of the header entirely (footer, filters, light landings) | A, C | Yes (v1 had a strip link) |
| D-09 | Four sectors; travel and leisure under Consumer; no technology sector | A, B | No |
| D-10 | CIVD belongs to Growth Strategy | B | Yes |
| D-11 | Growth Strategy is both pillar heading and lead service | B, C | No |
| D-12 | Flat service URLs under `/services/` | C | No |
| D-13 | Activation has a Supporting group page | B, C | No |
| D-14 | Experience Engineering label kept; CX, website, research as H2 sections and subtitle (subtitle rewritten in v3, see D-30) | C | No (subtitle added) |
| D-15 | Data agents are catalogue entries, not pages | B | No |
| D-16 | Services Canonical, themes Supporting, sectors Light | A, C | No |
| D-17 | Home is a page with seven blocks including the triangle | A, D | Yes (block list) |
| D-18 | About and Careers are separate hubs; Values and culture page | A | Yes |
| D-19 | Methodology lives at `/about/how-we-work/` | A | No |
| D-20 | Filters are query strings; no tag, author or category archives | A | No |
| D-21 | Testimonials live inside case studies | A | Made explicit |
| D-22 | Labels "What we do" and "Insights" | A | No |
| D-23 | Origination features kept | C | No |
| D-24 | Contact is a header button with no dropdown | Convention | No |
| D-25 | Mock opens with the mega-nav visible | D | New |

---

## D-01. The mega-nav is the triangle

**Options**
1. Keep the v1 four-column panel and promote CEO Advisory into it as a fifth element.
2. Three columns, one per pillar, plus a thin footer row for the three utility links (All services, Expertise themes, Contact).
3. Two columns (Growth Strategy, Activation) with CEO Advisory in the footer row, as v1.

**Chosen**: Option 2.

**Rationale**: Source B presents Growth Architecture as three things: CEO Advisory, Growth Strategy, Activation Services (slides 2 and 3). Source C gives their order of prominence: Growth Strategy is the bread and butter, Activation is the bridge to execution, CEO Advisory is new and testable and should not lead. Source D says the mega-nav must make the triangle obvious at a glance. Three columns in the Source C order does all three. Option 1 keeps the noise Gary rejected. Option 3 is v1 and hides a pillar.

**Trade-off**: The panel has less in it than a typical consultancy mega-nav. That is the point. Themes, featured work and sectors have homes elsewhere in the header and footer.

---

## D-02. CEO Advisory as a visible, quieter third column

**Options**
1. Bottom-strip text link (v1).
2. Full-weight third column equal to the other two.
3. Third column with the same structure (heading, subtitle, two links) but narrower and lighter, placed last.
4. Not in the mega-nav at all; reached from About and advisor profiles (Source C floated "may live outside main What we do menu").

**Chosen**: Option 3.

**Rationale**: Source D is explicit: CEO Advisory is part of the triangle and must be visible as such, but still last and quieter per Source C. Option 3 satisfies both. Option 2 would contradict "do not design the site around it". Option 4 removes a pillar and would repeat the v1 failure. The second link in the column, "Meet the advisors", goes to `/about/team/#advisors` because Source C says advisor profiles are what make the offer credible ("showcase advisor profiles, heavyweight").

**Trade-off**: A quieter column can still be read as a lesser service. Accepted, because Source C says it is one, and the structure (a full column) makes it unmistakably the third pillar.

---

## D-03. `/services/` is the Growth Architecture page

**Options**
1. Source A's literal suggestion: `/growth-architecture/` for the proposition and `/capabilities/` for the services hub, two pages.
2. One hub at `/services/`, titled "What we do" with the subheading "Our Growth Architecture", carrying the triangle and routing to every service. `/growth-architecture/` redirects to it.

**Chosen**: Option 2.

**Rationale**: Source B's deck is titled "Growth Architecture Services": the proposition and the services are the same thing seen from two distances. Two hub pages would split the triangle across two URLs and force a visitor to work out which to read. One page with the triangle at the top and the pillar sections below is simpler (Source D) and keeps `/services/` as the searched-for URL. Source A's intent, that the Growth Architecture proposition has a clear home, is met.

**Trade-off**: If Growth Architecture later needs a long-form narrative page (for example a manifesto or methodology story), it goes under About or How we work, not as a second hub.

---

## D-04. Expertise themes leave the mega-nav

**Options**
1. Themes as a mega-nav column (v1).
2. Themes as a top-level header item.
3. Themes in the Insights dropdown (second column), the footer, and a single text link in the mega-nav footer row. Full `/expertise/` section unchanged in the sitemap.

**Chosen**: Option 3.

**Rationale**: Source A makes themes one of three dimensions that intersect rather than silo, and insists on a canonical theme page (a Loyalty page that surfaces relevant services, sectors, case studies and insights). That is fully kept in the sitemap and linking rules. Source C frames themes as the expertise story and Andy asks for a simple layout where themes and sectors are discoverable "but not too confusing". Source D says themes must not clutter the services mega-nav. The Insights dropdown is the natural calm home: someone browsing thinking browses by problem, and every theme page hands off to services. Option 2 adds a sixth header item and a fourth dropdown. Option 1 is the rejected v1.

**Trade-off vs Source A**: Themes are one click less prominent than services in the header. They keep equal footing in URL structure, footer, filters and cross-linking, which is where Source A's SEO and GEO argument is actually made.

---

## D-05. One-line subtitles under service labels

**Chosen**: Every service label in the mega-nav carries one plain-English line, fixed text, no more than ten words. Pillar headings carry one short line each.

**Rationale**: Source C: "HPX failed; clients look for CX"; Experience Engineering "needs subtitles / keywords so 'can you build a website?' maps clearly"; Growth Office terminology is "hard". Source D asks for "plain subtitles under labels". Subtitles are the lightest way to make Source B's labels legible.

**Trade-off**: Subtitles add text to the panel. They are kept to one line and are the only text besides labels, so the panel still reads as three short lists.

**v3 note**: v2 wrote the subtitles partly in deck language. D-30 rewrites all thirteen. The mechanism (one line, ten words, fixed text) is unchanged.

---

## D-06. Featured case study removed from the mega-nav

**Chosen**: No editorial card in the mega-nav. Featured work is Home block 4 and the Work hub's first block.

**Rationale**: Source D: no Featured card column; move featured work to Home or the Work hub. A card with an image was the single largest visual element in the v1 panel and it was not a service.

---

## D-07. Our work is a plain header link

**Options**
1. Dropdown with filter shortcuts by service, expertise and sector (v1: ten links).
2. Plain link to `/work/`; filters on the page.

**Chosen**: Option 2.

**Rationale**: Source A: "Work (filter by theme, capability, sector etc. - no hub for every filter)". Filters belong on the hub. Source D asks for fewer, calmer menus. One fewer dropdown in the header.

---

## D-08. Sectors out of the header entirely

**Options**
1. Sectors as a top-level nav item or mega-nav column.
2. "Who we work with" text link in the mega-nav footer row (v1 bottom strip).
3. Footer column, filters on Work and Insights, light landings. Nothing in the header.

**Chosen**: Option 3.

**Rationale**: Source C: Andy would not have sector POV pages; services are sector-agnostic; Gary wants light sector landings for SEO and AI search "not shouted in nav; buried a bit; no children". Source D: sectors stay light, not primary nav. Removing the strip link frees the mega-nav footer row for the three links it needs and removes a non-service from the services panel.

**Trade-off vs Source A**: Source A lists sectors as a dimension with a hub. They remain a dimension in tags, filters, URLs and the footer. The narrowing is deliberate and agreed on the call.

---

## D-09. Four sectors; travel and leisure under Consumer; no technology sector

**Chosen**: Financial services, Media, Consumer, Retail (Source A's list). Merlin, Parkdean and IAG sit under Consumer. Meta and Microsoft appear in Our work without a sector landing.

**Rationale**: Sectors are light, so fewer is better. A new sector is added only when it has three case studies and two insights (the same threshold used to index a landing).

---

## D-10. CIVD belongs to Growth Strategy

**Chosen**: The CIVD frame (Customer, Innovation, Value, Delivery) is a module on `/services/growth-strategy/` and is explained once as a framework in How we work. v1 attached it to Proposition Innovation; that was wrong.

**Rationale**: Source B's Growth Strategy slide carries the four words Customer, Innovation, Delivery, Value and the note "to be updated from existing content on growth architecture / approach". Source A says "Growth Architecture (CIVD featured/described here)". Both point at the strategy layer, not at proposition design.

---

## D-11. Growth Strategy is both pillar heading and lead service

**Chosen**: `/services/growth-strategy/` is the lead service page and the head of its pillar; Proposition Innovation is its sibling. There is no separate Growth Strategy group page.

**Rationale**: Source C: Growth Strategy is the bread and butter and should be the strongest single page, not a thin group page with the real content one level down. The mega-nav heading and first item both point to it, stated openly in `01-primary-navigation.md`.

**Trade-off vs Source B**: The Growth Strategy pillar has no group page, unlike Activation. Intentional: one service with a close companion versus six services that need a shared explanation.

---

## D-12. Flat service URLs

**Chosen**: `/services/customer-research/`, not `/services/activation/customer-research/`. Grouping is shown in the nav, breadcrumbs and hub.

**Rationale**: Source C: the services deck is "a bit of the jigsaw" and may change. Flat URLs mean a service can move between pillars, or a pillar can be renamed, with no URL change.

---

## D-13. Activation has a Supporting group page

**Chosen**: `/services/activation/` explains Activation and lists the six services. Supporting weight.

**Rationale**: "Activation" is MGA's own term. Source C defines it as the bridge from strategy to execution, not owning ongoing operations. That needs saying once, and buyers purchase Activation as a set as well as individually. Supporting because it owns no capability topic; the six services do.

---

## D-14. Experience Engineering label kept, with plain-language sections and subtitle

**Chosen**: Label stays. Mega-nav subtitle (v3): "Customer experience (CX), website and digital design, build and testing". Page carries three H2 sections (Customer experience (CX) design; Website and digital product design and build; User research and testing) with anchors, and plain terms in metadata and FAQ.

**Rationale**: Source C: "website work lives here; need plain keywords CX / website / research". Source B: the squads combine customer insight, value analytics, CX design and digital technology; engagements return over 3x EBITDA ROI. Separate CX, website and research pages would fragment one offer and overlap Customer Research and Insight. Source E confirms the pattern: keep the label, make the subtitle do the mapping.

---

## D-15. Data agents are catalogue entries, not pages

**Chosen**: One canonical AI Agents for Marketing page with the AgentLab catalogue grouped as Source B groups it (Reporting and Analytics; Data and Infrastructure; Strategy and Planning; Automation and Execution). No page per agent.

**Rationale**: A dozen two-paragraph agent pages would be thin and compete with each other. If AgentLab is productised, agents can become Light pages under `/services/ai-agents-for-marketing/{agent}/` without disturbing anything else.

---

## D-16. Services Canonical, themes Supporting, sectors Light

**Chosen**: Unchanged from v1.

**Rationale**: Source A: services are the spine; a client should be able to answer "can these people solve my growth problem?" within seconds. Source C: sectors light. Themes keep real, indexable pages with unique points of view that hand off to services.

---

## D-17. Home is a page with seven blocks including the triangle

**Chosen**: Hero, client logos, Growth Architecture triangle, featured work, expertise themes strip, latest insights, closing CTA. No child URLs.

**Rationale**: Source A: home is a page, not a hub, reached by the logo; sections on the home page can sell the proposition in order. Source D: the triangle must be pointable. v1's ten blocks (proof band, How we work teaser, Who we work with) were cut as noise.

---

## D-18. About and Careers are separate hubs

**Chosen**: `/about/` (story), `/about/team/`, `/about/how-we-work/`, `/about/values/` (values, culture and DEI on one page). `/careers/` as a top-level section with Life at Manifesto, Benefits and Open roles as sections of one page, and `/careers/{role}/` for individual roles. Careers is reached from the About dropdown and the footer, not from a header item of its own.

**Rationale**: Source A: "Life at" overlaps with careers and there is no obvious About destination; "break this up so we have a clear about hub and a clear careers hub". Source A lists Values / Culture and DEI as separate About children and Life at Manifesto / Benefits / Open Roles as Careers children; at MGA's size those become sections of one page each rather than several thin pages.

**Trade-off vs Source A**: Fewer pages than Source A's list. Same destinations, less to maintain.

---

## D-19. Methodology lives at `/about/how-we-work/`

**Chosen**: Unchanged. Reached from the About dropdown and footer; no longer linked from the mega-nav.

**Rationale**: Source A: carefully separate tangible service offerings from methodology and ways of working. The v1 mega-nav link to How we work was a non-service in the services panel.

---

## D-20. Filters are query strings; no tag, author or category archives

**Chosen**: Unchanged. All browsing states on Work and Insights are `?param=` and canonicalise to the hub.

**Rationale**: Source A: "no hub for every filter"; Insights hub has filters for service, expertise, sector and content type. Archive pages are the classic source of thin, competing URLs.

---

## D-21. Testimonials live inside case studies

**Chosen**: No testimonials page. The client quote is a block of the case study template.

**Rationale**: Source A: a case studies page plus a case studies and testimonials page is redundant; testimonials should be inherently part of the content.

---

## D-22. Labels: "What we do" and "Insights"

**Chosen**: "What we do" as the mega-nav label (URL `/services/`), "Insights" for thinking (URL `/insights/`).

**Rationale**: Source A uses "What We Do" as the navigation grouping and "Insights" for the hub, with "latest" as a section rather than a page. Both are plain English.

---

## D-23. Origination features kept

**Chosen**: Indexable theme pages with unique points of view; FAQs and plain-language metadata on every canonical service; indexed case studies and team profiles; plain-language section headings on Experience Engineering; the triangle and positioning above the fold on Home.

**Rationale**: Source C: today the site is a post-referral credibility check; the rebuild should enable origination and compete with consultancies.

---

## D-24. Contact is a header button with no dropdown

**Rationale**: Conversion pages should be one click from everywhere with nothing to expand. Contact stays visible in the collapsed mobile header.

---

## D-25. The mock opens with the mega-nav visible

**Chosen**: `mocks/index.html` loads with the What we do panel already open so the first thing a reviewer sees is the three pillars. It closes on Escape, outside click or moving the cursor away, and reopens on hover as on the live site.

**Rationale**: Source D's success test is that Gary can open the mock and immediately point at the three pillars including CEO Advisory. This is a review aid, not a live-site behaviour.

**v3 note**: The mock gains a second review aid, a "Show what changed from v2" toggle that appends the v2 label after any renamed label. Off by default. Also not a live-site behaviour.

---

## D-26. Nav labels use the searched term, not the deck term

**Options**
1. Keep the v2 rule: deck labels verbatim, subtitles do all the explaining.
2. Rename every service to a plain descriptive phrase (for example "Customer Experience and Websites", "Interim Growth Team").
3. Per label: use the deck label where it is what prospects search; rename where the deck label and the searched term conflict; keep a Manifesto-coined label with a plain subtitle where Andy wants recognition for the term and no single plain phrase replaces it.

**Chosen**: Option 3.

**Rationale**: Source C: the deck is "a bit of the jigsaw" and "NOT website copy"; HPX failed and clients look for CX; simplification helps. Source E: prefer what a prospect would type over internal product names where they conflict, but keep a clear primary label plus subtitle for coined terms. Option 1 is what Gary pushed back on. Option 2 throws away names Andy is deliberately building recognition for (Experience Engineering, Side-by-Side) and would make the nav read like a generic agency. Option 3 applies a single test per label and records the answer (`nav-wording-decisions.md`).

**Trade-off**: The nav no longer matches the deck one-to-one, so a client who has seen the deck meets three different names. Mitigated by the "also known as" line on renamed service pages, by keeping deck terms in body copy, and by redirects from the deck-name slugs.

---

## D-27. Customer Intelligence becomes Customer Research and Insight

**Options**: keep "Customer Intelligence" with a subtitle; "Customer Insight"; "Customer Research"; "Customer Research and Insight".

**Chosen**: "Customer Research and Insight", slug `/services/customer-research/`.

**Rationale**: Prospects search "customer research", "market research", "customer insight". "Customer intelligence" reads as a software category. Andy described the service on the call as "customer insight / research; AI-enabled; standalone research too" (Source C). "Research" first because it is the higher-volume term; "Insight" kept because it is what the deck's second offer (intelligence capabilities, voice of the customer) delivers. Slug uses the head term only, to stay short.

**Trade-off**: "Customer Intelligence" is the name of Andy's team. It stays on the page as the practice name ("Our Customer Intelligence practice") and in body copy.

---

## D-28. Data Agents becomes AI Agents for Marketing

**Options**: keep "Data Agents" with a subtitle; "AI Marketing Agents"; "AI Agents for Marketing"; "Marketing and Data AI Agents".

**Chosen**: "AI Agents for Marketing", slug `/services/ai-agents-for-marketing/`.

**Rationale**: "Data Agents" carries no search signal and can be read as data brokerage. The deck's own strapline is "AI-powered performance marketing, guided by experts" (Source B) and Andy's summary on the call is "audit data, agents for marketing outcomes" (Source C). "AI agents for marketing" is the natural-language phrase a prospect types. It also puts "AI" on a label, which Source E lists among the intents the nav must catch. The data clean-up half of the offer lives in the subtitle ("AI that cleans up customer data and improves marketing performance").

**Trade-off**: Longer label than the others in the column (four words). Accepted; it is still one line. "Data Agents" and "AgentLab" stay on the page and `/data-agents/`, `/agentlab/` and `/services/data-agents/` redirect there.

---

## D-29. Operating Architecture becomes Operating Model Design

**Options**: keep "Operating Architecture" with a subtitle; "Operating Models" (the deck's own slide 3 label); "Operating Model Design".

**Chosen**: "Operating Model Design", slug `/services/operating-model-design/`.

**Rationale**: The deck uses both terms, so this is choosing between Andy's own alternatives. "Operating model design" is the phrase clients and search use ("we need a new operating model"). "Architecture" is the brand metaphor and is already carried by the company name and the "Our Growth Architecture" heading, so nothing is lost by taking it off this label. "Design" is added so the label is a service, not a topic.

**Trade-off**: "Operating Architecture" stays as the name of the framework module on the page and in How we work, so the deck's diagram keeps its title.

---

## D-30. Labels kept with rewritten subtitles

**Chosen**: Experience Engineering, Growth Office, Proposition Innovation, AI Enablement, Activation Services (pillar) and Side-by-Side keep their labels. All thirteen mega-nav subtitles are rewritten in plain English; each contains at least one term a prospect would search. The full list is in `01-primary-navigation.md` section 3.2 and the reasons per line in `nav-wording-decisions.md`.

**Rationale per label**:
- *Experience Engineering*: Source C and Source E both say keep it and subtitle it. It is the Dayinsure / Key Group model Andy wants to be known for. Subtitle: "Customer experience (CX), website and digital design, build and testing".
- *Growth Office*: Andy said the terminology is hard (Source C). Alternatives ("Growth Delivery Team", "Interim Growth Team") each lost part of culture plus capability plus value tracking. Short, parallels PMO / transformation office. Subtitle: "Interim growth team and programme office that gets strategy delivered".
- *Proposition Innovation*: both Gary's IA doc (Source A, "Proposition / Innovation") and the deck use "proposition"; it is standard UK marketing language; no single plain term covers loyalty, membership, subscription and direct-to-consumer. Subtitle carries those terms.
- *AI Enablement*: now common B2B language and searched. Wider than "training". Subtitle names the plain parts: "AI skills, training and adoption: finding where AI pays off".
- *Activation Services*: pillar name in the triangle; group page is Supporting, not a search target; the six services beneath carry the searched words. Subtitle: "Hands-on delivery that turns strategy into results".
- *Side-by-Side*: product name Andy is building the offer under; self-explanatory with the subtitle "Our advisory retainer: an experienced growth leader on call".

**Trade-off**: Six Manifesto terms remain in the panel. Each has a plain subtitle directly beneath it, which is the pattern Source E asks for.

---

## D-31. No acronyms in the nav

**Chosen**: "(SxS)" removed from the Side-by-Side label. "D2C" written "direct-to-consumer". "CX" only as "customer experience (CX)".

**Rationale**: Source C: HPX failed as a term; acronyms are the sharpest form of the problem Gary raised. "SxS" means nothing to a first-time visitor. "Customer experience (CX)" catches both the plain phrase and the abbreviation buyers use.

---

## D-32. "Expertise", not "Expertise themes", in the visitor's view

**Chosen**: Insights dropdown column heading, footer column heading and the mega-nav footer-row link all say "Expertise". The first item in the dropdown column is "All expertise". The documents keep "expertise themes" as the name of the dimension.

**Rationale**: "Themes" is an IA word. "Expertise" plus the five names says everything the visitor needs. Source E: plain language throughout the nav, not only in the service columns.

---

## D-33. Header labels unchanged after review

**Chosen**: What we do, Our work, Insights, About, Contact.

**Rationale**: Reviewed against "Services" and "Case studies" (Source E asks for the primary nav to be rewritten for discoverability). "What we do" is Source A's label and plain; the searched word is in the URL `/services/`. "Our work" is the plain consultancy convention; "case studies" goes in the page title and H1. The other three were never in question. The problem Gary raised was inside the mega-nav, not the header.

---

## Open items for the next stage (wireframes)

| Item | Note |
|---|---|
| **Andy's sign-off on the three renames** | Customer Research and Insight, AI Agents for Marketing, Operating Model Design change how three offers are described to the market. Confirm before wireframes lock. Fallback if any is refused: revert that one label and slug to the deck term and rely on its subtitle (D-30 pattern). |
| Growth Strategy and Proposition Innovation copy | Source B marks both slides "to be updated from existing content". Andy is sourcing (Source C action). |
| CEO Advisory event | Pushed to October (Source C). The page can launch with advisor profiles and the Why / What copy from Source B before the event. |
| Advisor profiles | Until at least one profile is flagged as advisor, "Meet the advisors" in the mega-nav points to `/services/ceo-advisory/`. |
| Subtitle wording | The thirteen mega-nav subtitles in `01-primary-navigation.md` are proposals for Andy to approve. Keep to one line and ten words; keep at least one searched term per line. |
| Triangle one-liners | The three Source B one-liners used on Home and the Services hub ("Architecting strategies and value propositions that deliver sustainable customer value growth" and so on) are page copy, not nav, and were out of scope for v3. They should get the same plain-language pass when Andy writes the service copy. |
| Mobile accordion tap behaviour | Two acceptable patterns are given in `01-primary-navigation.md`, section 3.5. Pick one in wireframes. |
| Contact topic list | `?topic=` values should be the service and theme slugs. Confirm whether "general" and "careers" are also needed. |
| Anonymised case studies | Some Source B example clients may not permit naming. Confirm before the twelve-case-study launch minimum is planned. |
| Sector index page | `/sectors/` is included as a Light page for the footer heading. If it feels redundant in wireframes, the footer heading can be plain text and the index dropped. |
| Brand | Name and logo stay; colour likely to change; fonts under debate; Sarah leading (Source C). None of this affects the IA. |
