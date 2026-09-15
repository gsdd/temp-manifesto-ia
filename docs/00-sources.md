# 00. Sources

The five inputs the package is built from, what each one contributed, and how conflicts between them were resolved. Read this before the decisions log.

v1 was produced from a brief that summarised these sources rather than supplying them. v2 was produced from the full text of A, B and C plus Gary's direction D. v3 adds Gary's wording brief E, which changes how B is used: B still decides what the services are and how they group, but no longer decides what they are called in the nav.

---

## Precedence

| Question | Source that wins | Why |
|---|---|---|
| What sections exist and how they relate | **A** (Gary's IA feedback) | It is the structural brief from the IA lead |
| What the services are and how they group (the triangle, the six activation services) | **B** (Andy's deck) | It is the client's own taxonomy |
| What the services are called in the nav, and what the subtitles say | **C** (Otter call) and **E** (Gary, 15 Sept) over **B** | Andy and Gary agreed on the call that the deck is not website copy and that plain, searched language wins. E makes that the rule for the nav. |
| Which services lead, how sectors and themes are weighted | **C** (Otter call) | It is where Gary and Andy agreed the weighting |
| How simple the mega-nav must be, and that CEO Advisory must be visible as a pillar | **D** (Gary, 14 Sept) | It is the instruction behind the v2 redo |

---

## Source A: Gary's IA feedback document

**What it is**: Feedback on the previously proposed sitemap, plus a suggested IA.

**Key points used**

- The current site's problem: content in silos, no taxonomy spanning them. Three dimensions to reframe around: **capabilities/services** (what can MGA do for me), **expertise/growth themes** (loyalty, subscriptions, pricing, customer value), **sectors** (financial services, media, consumer, retail). "These dimensions need their own sections/pages, but they should intersect rather than become isolated content silos."
- **Home** is a page, not a hub. No direct sub pages. Reached via logo or a Home link.
- **Services** was the biggest weakness: "growth partner", "strategy and execution", "side by side" mixed proposition, methodology and ways of working. "Carefully separate tangible service offerings from methodology, as well as sectors." A client should answer "can these people solve my growth problem?" within seconds.
- **Work**: case studies under Work; testimonials inside case studies, not a separate page.
- **Insights**: hub with a "latest" section (latest is a presentation concept, not IA); articles directly under `/insights/`; filters by service, expertise, sector and type; any article on loyalty links back to the canonical Loyalty page.
- **About and Careers**: "Life at" sounds employer-focused and overlaps careers; there is no obvious About destination. Break into a clear About hub and a clear Careers hub.
- **Suggested IA**: Home; What We Do (a mega-nav grouping, not a route) surfacing Growth Architecture (CIVD featured here), Services / Capabilities hub with canonical capability pages, Expertise / Growth Themes hub with canonical theme pages, Sectors hub; Work; Insights; About (Who We Are / Story, Team, Values / Culture, DEI); Careers (Life at Manifesto, Benefits, Open Roles, Individual Role); Contact.
- **Cross-linking table**: each canonical page type should surface and link to the others (service to themes, sectors, case studies, insights, methodology; theme to services, sectors, case studies, insights; sector to services, themes, case studies, insights; case study to services, themes, sector; insight to services, themes, sector, related insights).
- **Principle**: "one canonical page for each important proposition/topic, with the rest of the site linking into and out of it." Define the buckets first: what are the actual services, what are genuinely distinct areas of expertise, what is methodology rather than service, which sectors matter, where does each topic have its one canonical home.

**How v2 uses it**: Whole-site structure (`02-sitemap.md`), the three dimensions and their cross-linking rules (`04-canonicals-and-seo.md`), the About / Careers split, testimonials inside case studies, Insights with a latest section. The Growth Architecture page is merged with the services hub (D-03).

---

## Source B: Andy's Growth Architecture Services deck (working draft, Sept 26)

**What it is**: A slide deck describing MGA's packaged services as a triangle.

**Key points used**

- Title: "Manifesto's Growth Architecture Services".
- **The triangle** (slides 2 and 3): three pillars labelled **CEO Advisory**, **Growth Strategy**, **Activation Services**. Positioning: "Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth." "Manifesto's Growth Architecture offers clients a better way to unlock customer value growth by combining market-leading strategic thinking with AI-powered activation services." Strapline: **"Strategy that works. Execution that delivers."**
- **Pillar one-liners** (slide 3): Growth Strategy: "Architecting strategies and value propositions that deliver sustainable customer value growth." Activation Services: "Building the bridge from strategy to execution through new operating models and AI-powered, human-led activation services." CEO Advisory: "Direct support that sits side-by-side with leaders, offering expert advice to facilitate good decisions."
- **Service labels** (slide 3): Growth Strategy, Proposition Innovation (under Growth Strategy); Customer Intelligence, Experience Engineering, Data Agents, Operating Models / Operating Architecture, Growth Office, AI Enablement (under Activation Services); Side by Side (SxS) (under CEO Advisory).
- **Side-by-Side**: personalised one-to-one support for senior executives from proven growth leaders; "driving customer-led growth is demanding and lonely"; a select group of senior leaders armed with Manifesto thinking and frameworks; adaptive, personality-led, virtual or in person, retainer-based.
- **Growth Strategy slide**: the words Customer, Innovation, Delivery, Value (the CIVD frame); "to be updated from existing content on growth architecture / approach".
- **Proposition Innovation slide**: "to be updated from existing content on how we design new value propositions that grow sustainable customer value".
- **Customer Intelligence**: AI-powered insight, research and sensemaking that gets to the "So What" faster. Insight Projects; Intelligence Capabilities. Inputs: digital listening, qual research, customer data analytics, internal knowledge, external market data, quant research. Examples: Mars PPC, Trojan Energy, BBC, PEX, Skillshare.
- **Experience Engineering**: finding, redesigning, testing and scaling experiences that drive disproportionate value; squads combining customer insight, value analytics, CX design and digital technology; consistently over 3x EBITDA ROI. Examples: TransferGo, Dayinsure, Merlin Short Breaks, WSJ, Key Group.
- **Data Agents**: AI-powered performance marketing guided by experts; 4 weeks audit, 6 weeks first agents, ongoing portfolio; AgentLab catalogue grouped as Reporting and Analytics, Data and Infrastructure, Strategy and Planning, Automation and Execution. Examples: PEX, Parkdean, TSB, Standard Chartered.
- **Operating Architecture**: adaptive operating models for the age of AI; grounded in customer value growth, fuelled by high-quality data, redesigned around humans and AI agents, orchestrated and linked to impact. Examples: Post Office, BBC, TSB, WSJ, Meta, IAG, Microsoft. Appendix diagrams of the adaptive operating model.
- **Growth Office**: lean teams of interim growth experts bridging strategy and execution through Culture, Capability and Value; interim support then new ways of working. Examples: Mars, Dowds, News Corp.
- **AI Enablement**: skills building, value case targeting, business model innovation; maturity assessment then programmes across AI Adoption, Value Case Delivery, Business Model Innovation. Examples: IAG, Meta, Microsoft, McKinsey.

**How v2 uses it**: The three mega-nav columns and their order of labels (`01-primary-navigation.md`); the triangle block on Home and the Services hub (`03-page-layouts.md`); service page Why / What / module content; the CIVD placement under Growth Strategy; the client list for case study planning.

---

## Source C: Otter transcript, Shed x Manifesto check-in, 7 September 2026

**What it is**: 37-minute call between Gary Duncan (Shed) and Andy Bacon (Manifesto).

**Key points used**

- The services deck is "a bit of the jigsaw": packaged services MGA wants to be recognised for, not everything they do.
- **Triangle order of prominence**: Top (new) CEO Advisory = Side-by-Side: ex-CEOs and senior leaders on speed-dial, retainer, personality-led, low direct revenue, relationship value, event pushed to October, showcase heavyweight advisor profiles, new and testable, could flop. **Do not design the site around it.** Lead with Growth Strategy, then Activation, bolt CEO Advisory on the end / secondary. CEOs will not find MGA via the website. Middle (bread and butter) Growth Strategy = customer value growth strategy (where to play / how to win) + Proposition Innovation (loyalty, membership, subscriptions, D2C propositions). Bottom: Activation Services = bridge from strategy to execution, not owning ongoing ops, six offerings.
- **Language**: HPX failed; clients look for CX. Experience Engineering needs subtitles / keywords so "can you build a website?" maps clearly. Growth Office terminology is hard. The deck is not website copy.
- **Sectors versus themes**: Andy would not have sector-specific POV pages; services are sector-agnostic; case studies organised by sector is fine for proof. Themes are the expertise story: "loyalty and membership experts who work cross-sector". Gary still wants light sector landings for SEO and AI search (H1 plus proof), not shouted in nav, buried a bit, no children. Andy agrees: discoverable via tagging, not a lead for layout.
- **Site role**: today a post-referral credibility check; the rebuild should enable origination and compete with consultancies.
- **Brand**: name and logo stay; colour likely to change; fonts under debate; Sarah leading brand; Andy leading content.
- **Andy on simplification**: "the continued checking challenge is what's going to work well, and simplification of language is helpful, and then the balance of simple layout, but being able to see this cross reference on themes and sectors, so they're discoverable, but not too confusing in terms of how we lay it all out."
- **Actions**: Gary to iterate sitemap and nav, then wireframes. Andy to source services copy, case studies, testimonials, team.

**How v2 uses it**: Column order and CEO Advisory weighting (D-01, D-02); subtitles (D-05); sectors out of the header (D-08); themes as the expertise story with calm placement (D-04); Activation framing (D-13); Experience Engineering treatment (D-14); origination features (D-23); open items on copy, advisors and the October event.

---

## Source D: Gary's direction after rejecting v1 (14 September, evening)

**What it is**: Gary's response to the v1 package.

**Key points used**

- The v1 nav is very complicated; too much going on.
- He does not clearly see Andy's triangle contents, for example CEO Advisory. "Something has gone wrong."
- The first brief did not include all source material; retry with full sources.
- Structure source of truth remains Gary's IA doc (A). Services taxonomy = Andy's triangle (B). Sectors light.
- The mega-nav must make the triangle obvious at a glance. Under two seconds.
- CEO Advisory / Side-by-Side is part of the triangle and must be visible as such, not hidden so well the triangle disappears. Still secondary: Growth Strategy first, Activation second, CEO Advisory last and quieter.
- Expertise themes and sectors must not clutter the services mega-nav into a kitchen sink. Themes stay important for SEO and cross-linking but do not need a fourth busy column.
- Prefer the simple layout Andy asked for on the call: simple, with themes and sectors discoverable without confusion.
- Suggested shape: three columns matching the triangle; Proposition Innovation under Growth Strategy; six activation items with one-line subtitles where labels are opaque; CEO Advisory column with a subtitle and a link to advisors; optional thin footer row (All services, Expertise themes hub, Contact); no Featured card column.

**How v2 uses it**: The whole shape of the mega-nav (`01-primary-navigation.md`, section 3), the "Why v1 was rejected" record in `06-decisions-log.md`, the mock opening with the panel visible (D-25).

---

## Source E: Gary's v3 wording brief (15 September)

**What it is**: Gary's follow-up after reviewing v2, asking for a search-friendly wording pass on the nav.

**Key points used**

- The v2 nav may have taken Andy's literal services deck wording too literally.
- Restates what Andy and Gary agreed on the 7 September call: prefer search-friendly, plain language normal people and Google understand; HPX failed as a term and clients look for CX; Experience Engineering especially needs subtitles and keywords so "can you build a website?" and CX and research map clearly; the services deck is a starting point for alignment, not website copy; "simplification of language is helpful".
- Rewrite primary nav, mega-nav labels and service link text for discoverability. Prefer what a prospect would type or search over internal product names where they conflict.
- Keep Andy's triangle structure and relative weighting (CEO Advisory / Side-by-Side secondary, quieter).
- For hyper-technical or Manifesto-coined labels, keep a clear primary label and add a subtitle or supporting line in the mega-nav (Experience Engineering given as the example; apply the same pattern to Growth Office, Operating Architecture / Models, Data Agents, Proposition Innovation, Side-by-Side / CEO Advisory and anywhere else that needs it).
- Update sitemap and URL slugs if labels change. Keep services as canonicals, sectors light, no sector point-of-view rabbit holes.
- Refresh the mock so the mega-nav shows primary labels and subtitles clearly.
- Record every departure from Andy's deck wording: old label, new label, why.
- Success: mega-nav still three columns; no unexplained jargon without a plain subtitle; someone searching "customer experience", "website", "loyalty", "membership", "AI" and so on can map those intents onto nav items.

**How v3 uses it**: The wording rule and every label change (`nav-wording-decisions.md`); the rewritten mega-nav (`01-primary-navigation.md`, section 3); three renamed services and slugs (`02-sitemap.md`); the "also known as" hero line (`03-page-layouts.md`, T3); anchor text, title tag and redirect updates (`04-canonicals-and-seo.md`); decisions D-26 to D-33 (`06-decisions-log.md`); the refreshed mock with a "show v2 labels" review aid.
