# 06. Decisions log

Every significant IA decision, the options considered, what was chosen, and the trade-off. Each entry states how it relates to the Gary three-dimension model (Source A) and the Andy services triangle (Source B), and where Source C (Otter, 7 Sept) shaped the weighting.

Precedence used throughout: structure from A, service taxonomy from B, weighting from C plus the services-canonical instruction.

---

## Summary table

| ID | Decision | Sources in tension | Winner |
|---|---|---|---|
| D-01 | Five primary nav items; Expertise not a top-level item | A suggested a Thinking/Expertise top level | Brief's suggested nav, with A's intent kept via mega-nav column |
| D-02 | Services Canonical, themes Supporting, sectors Light | A treats three dimensions as peers | Services-canonical instruction and C |
| D-03 | Flat service URLs under `/services/` | B's triangle implies nesting | Resilience to repackaging (C) |
| D-04 | Expertise themes are column 3 of the What we do mega-nav | B has no themes in its triangle | A |
| D-05 | Themes repeated in the Insights dropdown | Duplication vs findability | Findability, with one URL home |
| D-06 | Labels: "What we do" and "Insights" | A used "Thinking" | Plain English |
| D-07 | Sectors out of the primary nav | A lists sectors as a dimension | C and client preference |
| D-08 | Four sectors; travel and leisure under Consumer | B's client list spans more sectors | A's sector list |
| D-09 | CEO Advisory in the mega-nav bottom strip only, Supporting weight | B places it as one of three triangle sides | C |
| D-10 | Growth Strategy is both group heading and lead service | B groups Growth Strategy and Proposition Innovation | B, simplified |
| D-11 | Data agents are catalogue entries, not pages | B lists many agents | Thin-content avoidance |
| D-12 | Experience Engineering label kept; CX, website, research as H2 sections | Label vs search language | Both, via on-page structure (C) |
| D-13 | Methodology lives at `/about/how-we-work/` | A: separate method from services | A |
| D-14 | Home is a page with no children | A | A |
| D-15 | Activation has a group page | B groups six services under Activation | B, at Supporting weight |
| D-16 | Five themes including Membership | A lists four; brief lists five | Brief |
| D-17 | Filters are query strings; no tag, author or category archives | SEO sprawl vs browsability | Canonical discipline |
| D-18 | Work hub is Canonical; case studies Supporting | Proof weight | A: proof closes the journey |
| D-19 | Proposition Innovation has its own page | Could be a section of Growth Strategy | B |
| D-20 | Origination features: indexable themes, FAQs, plain-language metadata | Credibility site vs originating site | C |
| D-21 | Contact is a header button, not a dropdown | Convention | Conversion |

---

## D-01. Five primary nav items, Expertise not a top-level item

**Options**
1. Five items as suggested in the brief: What we do, Our work, Insights, About, Contact.
2. Six items: add Expertise as a top-level item with its own dropdown, matching Gary's "Thinking / Expertise themes" section.
3. Four items: fold Insights into What we do.

**Chosen**: Option 1.

**Rationale**: A five-item header is easy to hold in the head and matches the brief. Gary's intent (themes as a first-class dimension) is preserved by giving themes their own column in the mega-nav and their own dropdown column under Insights, plus their own `/expertise/` section. Option 2 would have been legitimate but adds a top-level item whose relationship to What we do needs explaining on every visit. Option 3 buries thinking.

**Trade-off vs Gary model**: Slight. Expertise is one click deeper in the header than services, but has equal footing in the URL structure and the footer.

**Trade-off vs Andy triangle**: None. The triangle is fully represented inside What we do.

---

## D-02. Services Canonical, themes Supporting, sectors Light

**Options**
1. Three equal dimensions with equal content depth (a literal reading of Source A).
2. Services as the spine and canonical home for capability content; themes as Supporting pages with real content; sectors as Light landings (Source A's "services = spine" plus Source C).
3. Themes as the spine (the "expertise story") with services underneath.

**Chosen**: Option 2.

**Rationale**: The brief is explicit that canonicals are services and sectors are light. Gary also says services are the spine. Themes are kept as a real dimension with their own indexable pages and unique point-of-view content, but they hand off to services for anything about delivery. This avoids three parallel descriptions of the same work.

**Trade-off vs Gary model**: Gary's model is honoured in structure (three dimensions, all navigable, all cross-linking) but the dimensions are not equal in weight. That is a deliberate narrowing.

**Trade-off vs Andy triangle**: None.

---

## D-03. Flat service URLs

**Options**
1. Nested: `/services/activation/customer-intelligence/`, `/services/growth-strategy/proposition-innovation/`.
2. Flat: `/services/customer-intelligence/`, `/services/proposition-innovation/`, with grouping shown in nav, breadcrumbs and hub.

**Chosen**: Option 2.

**Rationale**: Source C notes the services deck is a packaged subset and may change. Flat URLs mean a service can move between groups, or a group can be renamed, with no URL change. Breadcrumbs still show the group so the triangle is visible. Shorter URLs are also easier to share and remember.

**Trade-off vs Andy triangle**: The triangle is not encoded in URLs, only in presentation. Acceptable.

---

## D-04. Expertise themes inside the What we do mega-nav

**Options**
1. Mega-nav is services only (two columns plus featured).
2. Mega-nav includes an Expertise column.

**Chosen**: Option 2.

**Rationale**: Prospects arrive with either a capability mindset ("I need a strategy partner") or a problem mindset ("our loyalty programme is not working"). Both should be served from the same menu. A three-column mega-nav also has enough content to justify being a mega-nav; services alone would be thin.

**Trade-off vs Andy triangle**: The triangle does not include themes. Adding them beside the services could imply themes are services. Mitigated by a distinct column heading and descriptor ("The growth problems we know inside out") and by theme pages that clearly route to services.

---

## D-05. Themes repeated in the Insights dropdown

**Options**
1. Themes appear only in the mega-nav.
2. Themes appear in both the mega-nav and the Insights dropdown.

**Chosen**: Option 2.

**Rationale**: Someone browsing thinking wants to browse by theme. Making them go back to What we do breaks the flow. Both lists link to the same five URLs, so there is no duplicate content, only a duplicate entry point. This is the only repetition in the header and is called out in `01-primary-navigation.md`.

**Trade-off**: Slightly longer header markup. No structural cost.

---

## D-06. Labels: "What we do" and "Insights"

**Options for the services item**: "Services", "What we do", "Expertise" (rejected, conflicts with themes).
**Options for the thinking item**: "Thinking", "Insights", "Ideas".

**Chosen**: "What we do" (URL `/services/`) and "Insights" (URL `/insights/`).

**Rationale**: "What we do" is friendlier to non-consultancy buyers and is the brief's own phrasing. The URL stays `/services/` because that is the searched-for term. "Insights" matches its URL and is universally understood; "Thinking" is a house style word that some visitors read as a verb. Gary's "Thinking" section is delivered as `/expertise/` plus `/insights/`, so the content he described still exists.

**Trade-off vs Gary model**: Label only.

---

## D-07. Sectors out of the primary nav

**Options**
1. Sectors as a top-level nav item.
2. Sectors as a mega-nav column.
3. Sectors in the footer, as filters on Work and Insights, as a text link in the mega-nav bottom strip, and as Light landings.

**Chosen**: Option 3.

**Rationale**: Source C and the client preference are clear that sectors are proof points, not points of view. Putting them in the header would signal a depth of sector content that the site deliberately does not have and would draw investment away from services. The footer, filters and light landings still let a visitor answer "have you worked with businesses like mine?" within one or two clicks.

**Trade-off vs Gary model**: Gary lists sectors as one of three dimensions. They remain a dimension in the data model (tags), in filters and in URLs, but not in the header. This is the intended narrowing.

---

## D-08. Four sectors; travel and leisure under Consumer; no technology sector

**Options**
1. Exactly Gary's four: financial services, media, consumer, retail.
2. Add travel and leisure (Merlin, Parkdean, IAG) and technology (Meta, Microsoft) as sectors five and six.

**Chosen**: Option 1 at launch, with a published rule for adding sectors.

**Rationale**: Sectors are light, so fewer is better. Travel and leisure fits under Consumer without strain. Technology clients are visible in Our work through logos and case studies, and a technology sector landing would be thin. A new sector is added only when it has three case studies and two insights (the same threshold used to index a landing).

**Trade-off vs Andy triangle**: The client list in Source B is broader than the four sectors. Clients not covered by a sector still appear on Home, About and Work.

---

## D-09. CEO Advisory downweighted

**Options**
1. CEO Advisory as a third mega-nav column, matching its position as one side of the triangle.
2. CEO Advisory as a text link in the mega-nav bottom strip, last in the footer services list, a quiet block on the Services hub, and a Supporting-weight page.
3. CEO Advisory omitted from the nav entirely and reached only from About or advisor profiles.

**Chosen**: Option 2.

**Rationale**: Source C says CEO Advisory is new and testable and should be downweighted. Omitting it (option 3) would make it unfindable for the senior leader who has been told about Side-by-Side and comes looking. The bottom strip gives it a stable, findable but unpromoted position. Advisor profiles under `/about/team/` carry the Side-by-Side link so the personality-led nature of the offer is preserved.

**Trade-off vs Andy triangle**: This is the most visible departure from the triangle. The deck presents three sides as peers; the site presents Growth Strategy as the core, Activation as its delivery, and CEO Advisory as an additional route. If CEO Advisory proves itself, promoting it to a mega-nav column is a nav change only, with no URL change.

---

## D-10. Growth Strategy is both group heading and lead service

**Options**
1. A group page `/services/growth-strategy/` listing Growth Strategy and Proposition Innovation as children, with the service itself at `/services/growth-strategy/strategy/` or similar.
2. `/services/growth-strategy/` is the lead service page and also acts as the head of its group; Proposition Innovation is a sibling.

**Chosen**: Option 2.

**Rationale**: Growth Strategy is the bread-and-butter offer (Source C). It should be the strongest single page on the site, not a thin group page with the real content one level down. The mega-nav column heading and first item both point to it, which is stated openly in `01-primary-navigation.md`.

**Trade-off vs Andy triangle**: The Growth Strategy side of the triangle has no separate group page, unlike Activation. This asymmetry is intentional and reflects that Growth Strategy is one service with a close companion, while Activation is six services that need a shared explanation.

---

## D-11. Data agents are catalogue entries, not pages

**Options**
1. A page per agent (reporting, attribution, tagging, and so on).
2. One canonical Data Agents page with a filterable catalogue module.

**Chosen**: Option 2 for v1.

**Rationale**: A dozen agent pages with two paragraphs each would be thin and would compete with each other. One strong page ranks for the cluster. If AgentLab is productised with pricing and sign-up, agents can become Light pages under `/services/data-agents/{agent}/` without disturbing anything else.

**Trade-off vs Andy triangle**: The deck lists the agents at length. That detail is kept, but on one page.

---

## D-12. Experience Engineering label kept, with CX, website and research as on-page sections

**Options**
1. Rename the service to something search-friendly ("Customer Experience and Digital").
2. Keep "Experience Engineering" and create separate CX, website and research service pages.
3. Keep the label and structure the page with three H2 sections and anchors, using plain-language terms in metadata, FAQs and anchor text.

**Chosen**: Option 3.

**Rationale**: The brief requires the label to stay. Separate pages would fragment a single offer and create overlap with Customer Intelligence. On-page sections with anchors catch the plain-language searches while keeping one canonical. The Dayinsure and Key Group work is the reference model for the page's proof.

**Trade-off**: A single page ranks less precisely for "website design agency" than a dedicated page would. Accepted, because MGA sells experience engineering as a whole, not web design as a commodity.

---

## D-13. Methodology lives under About

**Options**
1. `/services/how-we-work/`.
2. `/how-we-work/` at top level.
3. `/about/how-we-work/`, cross-linked from the mega-nav.

**Chosen**: Option 3.

**Rationale**: Gary asked for tangible services to be separated from methodology. Placing method under `/services/` blurs that line. A top-level URL would need a top-level nav item to justify it. Under About it sits with the company story while remaining one click from the mega-nav via column 4.

**Trade-off vs Gary model**: None; this is his instruction.

---

## D-14. Home is a page with no children

**Chosen**: Home is a single URL. Anything that would have been a Home child (why us, our approach) lives under About.

**Rationale**: Explicit in the brief and Source A. Home's job is to route, and Home carries no content that does not exist in full elsewhere.

---

## D-15. Activation has a group page

**Options**
1. No group page; the Services hub explains Activation and the six services are flat.
2. A Supporting-weight group page at `/services/activation/`.

**Chosen**: Option 2.

**Rationale**: "Activation" is MGA's own term and needs a home that explains it as strategy-to-execution and not ongoing operations (Source C). Buyers also purchase Activation as a bundle. The page is Supporting, not Canonical, because it owns no capability topic; the six services do.

**Trade-off vs Gary model**: Adds one page that is neither service, theme nor sector. Justified by the triangle.

---

## D-16. Five themes including Membership

**Options**
1. Gary's four: loyalty, subscriptions, pricing, customer value.
2. The brief's five: loyalty, membership, subscriptions, pricing, customer value.

**Chosen**: Option 2.

**Rationale**: The brief's constraint lists membership explicitly, and Key Group style work supports it. Membership and subscriptions are related but distinct commercial models; combining them would weaken both pages. Each theme must meet the two-case-study, two-insight threshold before publishing, so if membership proof is short at launch it can be held back without changing the IA.

---

## D-17. Filters are query strings; no tag, author or category archives

**Chosen**: All browsing states on Work and Insights are `?param=` and canonicalise to the hub. There are no `/insights/tag/`, `/insights/author/` or `/work/sector/` paths.

**Rationale**: Archive pages are the classic source of thin, duplicate, competing URLs. The sitemap stays small and every indexed URL earns its place. Authors are served by team profiles; themes by expertise pages; sectors by light landings.

**Trade-off**: Filtered views are not shareable as ranking pages. Acceptable; they are shareable as links.

---

## D-18. Work hub is Canonical; case studies Supporting

**Rationale**: Gary's journey ends in proof. The Work hub is the one place where all proof is filterable across all three dimensions, which makes it structurally central. Individual case studies are Supporting because each proves one engagement and links up to services and themes.

---

## D-19. Proposition Innovation has its own page

**Options**
1. A section within Growth Strategy.
2. Its own canonical page.

**Chosen**: Option 2.

**Rationale**: Source B lists it as a named offer with its own approach (CIVD). It targets a distinct search cluster (proposition design). Folding it into Growth Strategy would lose that and make the Growth Strategy page do two jobs.

---

## D-20. Origination features

**Chosen**: Theme pages are indexable with unique points of view; every canonical service carries FAQs and plain-language metadata; case studies and team profiles are indexed; Experience Engineering carries plain-language section headings; Home carries the positioning statement and logo strip above the fold.

**Rationale**: Source C states the current site works only after a referral and the rebuild must originate. Each of these features exists to catch a visitor who has never heard of MGA, at the point where they are searching for a capability, a problem or a peer.

**Trade-off**: More content is required at launch (see `05-content-matrix.md`, section 3). That is the cost of origination.

---

## D-21. Contact is a header button with no dropdown

**Rationale**: Conversion pages should be one click from everywhere with nothing to expand. Contact also stays visible in the collapsed mobile header.

---

## Open items for the next stage (wireframes)

These are not IA decisions but were noted while producing the package.

| Item | Note |
|---|---|
| CIVD naming | Source B marks CIVD as work in progress. The Proposition Innovation module and How we work framework block use it as a placeholder. |
| Mobile accordion tap behaviour | Two acceptable patterns are given in `01-primary-navigation.md`, section 3.5. Pick one in wireframes. |
| Featured case study fallback | Column 4 of the mega-nav falls back to newest. Confirm whether an editor-set default is preferred. |
| Contact topic list | The `?topic=` values should be the service and theme slugs. Confirm whether "general" and "careers" are also needed. |
| Anonymised case study count | Some example clients may not permit naming. Confirm which can be named before the twelve-case-study launch minimum is planned. |
| Sector index page | `/sectors/` is included as a Light page for footer and bottom-strip linking. If it feels redundant in wireframes, the "Who we work with" links can point straight to the four landings and the index can be dropped. |
