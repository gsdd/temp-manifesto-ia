# Information architecture recommendations

**Manifesto Growth Architects**  
Shed Collective · September 2026

This report sets out the recommended information architecture for the new Manifesto Growth Architects website: the hierarchy and primary navigation, the full sitemap, the What we do mega-nav, the page templates and the reusable components they are built from, and the search language that sits beneath Manifesto's own labels. It is the output of the UX and IA process. The clickable wireframe at https://temp-manifesto-ia.pages.dev/ is the same set of recommendations as a working model. Both are generated from one source and do not disagree.

Each section states the recommendation, then the evidence behind it. Section 7 indexes the evidence. Section 8 lists the decisions that remain with Manifesto.

Conventions: URLs carry a trailing slash. Search volumes are average monthly UK Google searches from DataForSEO (16 September 2026) and appear only where that pull returned a figure. Nothing is estimated.

---

## 1. Executive summary

We recommend a services-led site built around the Growth Architecture triangle: **Growth Strategy**, **Activation Services** and **CEO Advisory**. Services are the spine of the site and the canonical home of every capability topic. Expertise themes and sectors are real, indexable dimensions with their own pages, but they intersect the services through links and tags rather than competing with them in the header.

The header carries six items, logo aside: **What we do**, **Our work**, **Our thinking**, **About**, **Careers** and a **Contact** button. What we do is the only mega-nav, and it is the triangle laid flat: three linked pillar hubs, eleven strands, one thin footer row. Nothing else joins it.

CEO Advisory is a full-weight third pillar. Same ink and heading weight as Growth Strategy and Activation Services. It is quieter only because its column is slightly narrower and holds two strands where Activation holds seven. It is not greyed out, because a muted pillar reads as a second-class offer.

Every strand carries a short keyword-led subtitle so a prospect who has never heard of Manifesto can see what they get. Manifesto's labels stay. Search language sits under the label, in page support lines, H2s and title tags.

The site has one job the current site does not do: originate enquiries from people who arrive cold. So every key page answers, in order: what can you do for me, do you understand my problem, have you done this for businesses like mine, prove it.

Pages are built from a fixed vocabulary of 32 named components in seven interaction types. The wireframe's component library (`/catalogue/`) is the index, and every page's sidebar lists the components on that page by the same names. Designers and developers build from the library, not from rectangles.

**Evidence**

- Andy's Growth Architecture Services deck (Source B): the offer is the triangle of Growth Strategy, Activation Services and CEO Advisory under the name Growth Architecture Services. Positioning line: "Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth." Strapline: "Strategy that works. Execution that delivers."
- 7 September check-in with Andy (Source C): order of prominence is Growth Strategy, then Activation, then CEO Advisory; do not design the whole site around advisory; the deck is not website copy; today's site is a post-referral credibility check and the rebuild has to originate.
- Gary's IA feedback (Source A): three intersecting dimensions (services, expertise, sectors); one canonical home per topic; Home is a page, not a hub; separate tangible services from methodology.
- MURAL keep/drop: six-item chrome with Our thinking and Careers first-class; Trusted partners high; no homepage reports grid; keep CIVD with new visuals; The Nutshell is the newsletter name.
- Competitor review (`docs/competitor-nav-review.md`; ten peers and six pattern references read 15 September 2026): Prophet's What We Do panel carries about 25 links, Elixirr's Services panel about 60, Baringa's Capabilities 18 flat. Manifesto's 17-link panel is at the calm end of the set. The gap to best in class is on the pages: two ways in, proof under the offer, a visible home for the named system.
- UK keyword findings (`docs/keyword-findings.md`): exact Manifesto phrases are thin; adjacent demand (customer journey mapping ~2,900, target operating model ~1,600, value proposition design ~140, interim CMO ~110 to 140) belongs in subtitles and H2s, not as extra nav items.

---

## 2. Recommended hierarchy and primary navigation

### 2.1 Header

**What we do** | **Our work** | **Our thinking** | **About** | **Careers** | **Contact**

Six items, logo aside. That is the cap.

| Item | Behaviour | Lands on |
|---|---|---|
| Logo | Home | `/` |
| What we do | Mega-nav on hover or click; the label itself goes to the services hub | `/services/` |
| Our work | Plain link | `/work/` |
| Our thinking | Small type dropdown: Reports, Articles, Events and news, All thinking | `/insights/` |
| About | Small dropdown: Our people, Our approach, Values and culture | `/about/` |
| Careers | Plain first-class link | `/careers/` |
| Contact | Button, the primary enquiry route | `/contact/` |

Rationale

- Services are the spine. A prospect's first question is what Manifesto can do, so the first item is the triangle.
- Our work is the proof engine and a plain link. Its filters live on the page.
- Our thinking is Manifesto's name for the insights library. The URL is `/insights/` because that is the searched word.
- Careers is first-class so Contact can honestly split Work with us from Work for us.
- Expertise appears in the header once, as a link in the mega-nav footer row. Sectors do not appear in the header at all. They live in the footer, in the Work and Thinking filters, and as light landing pages.
- Search is a footer field plus `/search/`, not a seventh header item.

### 2.2 Calls to action

- Primary: the Contact button, repeated as a Closing CTA band on every content page. Careers routes use Work for us.
- Secondary: a text link, usually See our work or What we do.
- CEO Advisory uses a quieter primary: Arrange a conversation.
- Contact has two forms with stable anchors, `#work-with-us` and `#work-for-us`. Roles stay on Careers.

### 2.3 Footer

The footer is the second navigation system. It carries the full structure, including the two dimensions kept out of the header.

| Column | Links |
|---|---|
| What we do | Growth Strategy, Proposition Innovation, Customer Research and Insight, Experience Engineering, AI Agents for Marketing, Operating Model Design, Growth Office, AI Enablement, CEO Advisory, All services |
| Expertise | Loyalty, Membership, Subscriptions, Pricing, Customer Value |
| Who we work with | Financial services, Media, Consumer, Retail (the heading is plain text; there is no sector index page) |
| Company | About, Our people, Our approach, Values and culture, Careers, Our work, Our thinking, The Nutshell, Contact |
| Bottom row | Company registration, search field, Privacy policy, Cookie policy, Terms, Accessibility statement, social links |

A site-wide cookie bar sits above the footer. Accept dismisses it; Cookie policy is the text link.

### 2.4 Breadcrumbs and mobile

Every page below the top level shows a breadcrumb beneath the header, starting at Home and using the nav labels: `Home > What we do > Activation Services > Experience Engineering`. Activation services show the group in the trail even though the URL is flat.

Below roughly 1024 px the header collapses to logo, Contact button and a Menu button that opens a full-screen panel. What we do expands first, as one flat list with small pillar labels and no nested accordions. Our work, Our thinking, About and Careers follow. Sectors are footer only on every device. Tap targets are 44 px or larger.

**Evidence**

- Source A: three intersecting dimensions with one canonical home per topic; Home is a page reached by the logo; a clear About hub and a clear Careers hub instead of one "Life at" page doing both jobs; What We Do as the grouping label.
- Source C: sectors are proof, not a second services taxonomy; light landings for search, discoverable through tagging, "buried a bit, no children".
- MURAL: Our thinking, Our people, Our approach as the visible labels; Careers first-class; Work with us / Work for us split; The Nutshell; Our clients and Our blog not as top-level items.
- Competitor review: "What we do" is the services label at Prophet, Yonder and Deloitte Digital. Header counts across the peer set run from four (Lippincott) to seven (Elsewhen, Mando). No small peer puts sectors in the header: Prophet, Yonder, The Foundation, frog, Lippincott, Elsewhen, Mando and Ellipsis all leave them out. Elsewhen's separate Blog and Reports header items are the pattern Our thinking's dropdown avoids.

---

## 3. Full sitemap

### 3.1 Weights

Every page carries a weight that sets its content and search investment.

| Weight | Meaning | Typical size | Indexed |
|---|---|---|---|
| Canonical | The single page that owns a topic. Everything else on the topic links here. | 800 to 1,500 words plus components | Yes |
| Supporting | Substantial content that strengthens a canonical with proof, context or another way in. Never restates it. | 400 to 1,000 words | Yes |
| Light | A short landing that routes and aggregates. | 150 to 300 words of intro | Yes, once it meets its content threshold |
| Utility | Functional pages. | As needed | Mostly no |

Services are Canonical, expertise themes and work are Supporting, sectors are Light.

### 3.2 URL rules

Lowercase, hyphenated, trailing slash. No dates, IDs or file extensions. Maximum three levels below the root. Service URLs are **flat under `/services/`** even though the menu groups them by pillar: grouping is a menu concern, and flat URLs survive if the packaging changes. Filters are query strings (`?service=`, `?expertise=`, `?sector=`, `?type=`), never paths.

### 3.3 Every URL

| URL | Page | Weight |
|---|---|---|
| `/` | Home | Canonical |
| `/services/` | Our Growth Architecture (services hub) | Canonical |
| `/services/growth-strategy/` | Growth Strategy, with the CIVD frame at `#civd` | Canonical |
| `/services/proposition-innovation/` | Proposition Innovation | Canonical |
| `/services/activation/` | Activation Services (group page) | Supporting |
| `/services/customer-research/` | Customer Research and Insight | Canonical |
| `/services/experience-engineering/` | Experience Engineering (`#customer-experience`, `#website-and-digital`, `#research-and-testing`) | Canonical |
| `/services/ai-agents-for-marketing/` | AI Agents for Marketing, with AgentLab at `#agentlab` | Canonical |
| `/services/operating-model-design/` | Operating Model Design, with the Operating Architecture framework at `#operating-architecture` | Canonical |
| `/services/growth-office/` | Growth Office | Canonical |
| `/services/ai-enablement/` | AI Enablement | Canonical |
| `/services/ceo-advisory/` | CEO Advisory (`#side-by-side`, `#advisors`) | Supporting |
| `/expertise/` | Expertise hub | Supporting |
| `/expertise/loyalty/`, `/expertise/membership/`, `/expertise/subscriptions/`, `/expertise/pricing/`, `/expertise/customer-value/` | Expertise themes | Supporting |
| `/sectors/financial-services/`, `/sectors/media/`, `/sectors/consumer/`, `/sectors/retail/` | Sector landings | Light |
| `/work/` | Our work | Canonical |
| `/work/{client}/` | Case study | Supporting |
| `/insights/` | Our thinking | Supporting |
| `/insights/{slug}/` | Article, report or event | Supporting |
| `/about/` | About | Supporting |
| `/about/team/` | Our people (`#advisors`) | Supporting |
| `/about/team/{name}/` | Profile | Light |
| `/about/how-we-work/` | Our approach | Supporting |
| `/about/values/` | Values and culture | Light |
| `/careers/` | Careers | Light |
| `/careers/{role}/` | Role | Light |
| `/contact/` | Contact (`#work-with-us`, `#work-for-us`) | Utility, indexed |
| `/contact/thank-you/` | Thank you | Utility |
| `/newsletter/` | The Nutshell | Utility, indexed |
| `/search/` | Search | Utility |
| `/privacy-policy/`, `/cookie-policy/`, `/terms/`, `/accessibility/` | Legal | Utility, indexed |
| `/404/` | Page not found | Utility |
| `/sitemap.xml`, `/robots.txt` | System | Utility |

Forty fixed pages at launch, of which eleven are Canonical: Home, the services hub, the eight service pages and Our work. Case studies, articles, profiles and roles are added from the CMS.

### 3.4 Redirects, not pages

- `/sectors/` redirects to `/work/`. The footer lists the four sectors; an index page would only repeat it.
- `/growth-architecture/` redirects to `/services/`. `/agentlab/` and `/data-agents/` redirect to `/services/ai-agents-for-marketing/#agentlab`. `/side-by-side/` redirects to `/services/ceo-advisory/`. `/advisors/`, if used in print or at the October event, redirects to `/services/ceo-advisory/#advisors`.
- Deck-name slugs (`/services/customer-intelligence/`, `/services/data-agents/`, `/services/operating-architecture/`) redirect to the searched-term slugs.
- Every URL on the current site that returns 200 gets a 301 to its closest new page before launch, followed by 90 days of 404 monitoring.

### 3.5 Deliberately not in the sitemap

| Excluded | Why |
|---|---|
| A separate Growth Architecture page | `/services/` is the Growth Architecture page. One hub carries the triangle. |
| A sectors index, sector points of view, or pages under a sector | Sectors are proof and a filter, not a destination. |
| Separate CIVD, AgentLab or Side-by-Side pages | Each named framework has one anchored home on the service that owns it, and is listed once on Our approach. |
| Separate CX, UX, website or research pages | Sections of Experience Engineering with their own anchors, so those searches land on one strong page. |
| A generic AI page | Two labels already carry "AI" (AI Agents for Marketing, AI Enablement). A third page would be thin and compete with both. |
| Methodology under `/services/` | Method is not a product. It lives at `/about/how-we-work/`. |
| A testimonials page, a blog, an events URL, a clients page | Quotes live inside case studies; articles and events are types within Our thinking; clients are Trusted partners on Home, proof on Our work and logos on sector landings. |
| Author, tag and category archives | Filters and profiles cover them without thin pages. |
| `/catalogue/` as a live URL | The component library is a wireframe tool. It is not in the header, footer or XML sitemap. |

**Evidence**

- Source A: one canonical page per topic; themes under `/expertise/`; testimonials inside case studies; articles directly under `/insights/`; Insights filterable by service, expertise, sector and type.
- Source B: eight buyable services, the Activation grouping, CEO Advisory as the third pillar; Side-by-Side as the named product; AgentLab as a catalogue of twelve named agents, which are entries rather than pages.
- Source C: services are sector-agnostic; four sectors; travel and leisure under Consumer; technology clients appear in Our work without a sector landing.
- MURAL: The Nutshell; reports read on the page, no PDFs; blogs merged into articles; Our clients and Our blog not as top-level items.
- Competitor review: The Foundation has no service pages and therefore no landing for capability searches, which is the credibility-check model the rebuild has to move past. Prophet and Ekimetrics give their labs a page under About; a section anchor is the calmer version for a twelve-entry catalogue.

---

## 4. Mega-nav and strand structure

### 4.1 The panel

The What we do panel is the triangle laid flat, in order of prominence. Three linked pillar headings, each with a trailing arrow. Strands sit as siblings under each heading, each with a keyword-led subtitle. Growth Strategy and Activation Services open with an Overview strand so the heading never reads as a label over a single child. CEO Advisory shows both of its named strands. One thin row of links closes the panel.

| Growth Strategy → | Activation Services → | CEO Advisory → |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one support for leaders |
| **Overview** Where to grow and how to win | **Overview** Hands-on delivery, six services | **Side-by-Side** One-to-one advisory retainer |
| **Proposition Innovation** Value proposition design | **Customer Research and Insight** Research methods and journey mapping | **Our advisors** Experienced growth leaders |
| | **Experience Engineering** Customer experience and websites | |
| | **AI Agents for Marketing** AI marketing agents, guided by experts | |
| | **Operating Model Design** Target operating model | |
| | **Growth Office** Interim growth team | |
| | **AI Enablement** AI skills and adoption | |

Footer row: **All services** · **Expertise** · **Our work**

Seventeen links to thirteen pages. The pillar headings land on `/services/growth-strategy/`, `/services/activation/` and `/services/ceo-advisory/`. Overview repeats the pillar destination as a visible row. Side-by-Side and Our advisors are anchors on the CEO Advisory page, not separate URLs.

### 4.2 Rules for the panel

- The three pillar headings share one ink colour and one heading weight. A prospect names all three within two seconds of the panel opening, without reading anything in smaller type.
- CEO Advisory's column is slightly narrower. That, and two strands against Activation's seven, is the whole of its quieter treatment.
- One pillar line per column, four to six words, shared word for word with the triangle tiles on Home and the services hub.
- One subtitle per strand, two to six words, in the buyer's language. Subtitles explain the label. They do not rename it.
- Not in the panel: deck one-liners, CIVD, AgentLab, Growth Partner, sector or theme names, a Contact link (the header button is directly above), acronyms. "SxS" does not appear anywhere on the site.
- Adding a strand is an IA decision, not a content edit. The default answer is no.

### 4.3 Why each strand reads as it does

| Strand | Subtitle | Why this wording |
|---|---|---|
| Growth Strategy Overview | Where to grow and how to win | The pillar's job in plain words. "Growth strategy" is the searched phrase (~480). |
| Proposition Innovation | Value proposition design | The commercial phrase buyers use (~140). "Proposition innovation" has no usable volume. |
| Activation Overview | Hands-on delivery, six services | Says what Activation is and how many doors it has. |
| Customer Research and Insight | Research methods and journey mapping | Method language outranks the consultancy noun: customer research methods ~720, customer journey mapping ~2,900. |
| Experience Engineering | Customer experience and websites | The two intents Andy named on the call: CX, and "can you build a website?" |
| AI Agents for Marketing | AI marketing agents, guided by experts | Marketing-qualified (~390) rather than bare "AI agents" (~9,900 and generic). "Guided by experts" is the deck's own human-led point. |
| Operating Model Design | Target operating model | The strongest Activation phrase after journey mapping (~1,600). |
| Growth Office | Interim growth team | "Growth office" has about 10 searches a month. Interim CMO has ~110 to 140. The subtitle carries the buyer's term. |
| AI Enablement | AI skills and adoption | The plain content of the deck's three programmes. |
| Side-by-Side | One-to-one advisory retainer | Names the category before the product name. |
| Our advisors | Experienced growth leaders | The people are the proof of the third pillar. |

**Evidence**

- Source B slide 2: the triangle of CEO Advisory, Growth Strategy and Activation Services. Slide 3: Proposition Innovation under Growth Strategy; six Activation services in the order used here; Side-by-Side as the CEO Advisory product. Slide 4: retainer-based, virtual or in person, "a select group of senior leaders".
- Source C: Growth Strategy first, Activation second, CEO Advisory third; CEOs will not find Manifesto through the website, so the pillar is present but not the lead; Experience Engineering must map to CX and websites; Growth Office terminology is hard; showcase heavyweight advisor profiles.
- Wireframe review feedback: a greyed pillar reads as a second-class offer; pillar headings must be obviously clickable hubs; CEO Advisory has two strands and both should be visible; every strand needs a human-readable cue.
- Competitor review: Prophet lists Growth Strategy as a service and gives its lab a home off the nav; Elixirr uses "Target Operating Model"; frog uses "Customer Research & Insights"; Baringa's "CFO Advisory" validates "CEO Advisory" as a plain label; Criticaleye sells its senior advisory model on the mentors. No peer uses "Experience Engineering" or "Growth Office", which is why both carry a subtitle that says what they are.
- Keyword findings: "Do not rename the triangle for volume." Subtitles carry adjacent demand; labels stay Manifesto's.

---

## 5. Page templates and components

### 5.1 The component vocabulary

Every page is an ordered list of named components. A component has one name, one shape and one interaction type. The component library at `/catalogue/` in the wireframe is the index. Each page's sidebar lists the components on that page, in canvas order, by the same names, and the wireframe build fails if a page uses a name the library does not have. The sidebar is annotation; nothing in it is a live component.

Seven interaction types:

| Type | What it does | Never |
|---|---|---|
| Band | Full-width block that composes others: Hero, Closing CTA band | |
| Button | An action: Send, Accept, Clear filters, Search, the primary of a CTA pair, header Contact | Link to a content page, except header Contact |
| Text link | Navigate: strands, situations, breadcrumbs, footer, See our work | Sit in a box |
| Card | The whole unit is the hit area to one destination page | Toggle a filter; hold a statistic |
| Tag | Small linked label, one dimension, three at most | Act as a filter |
| Filter | Toggle a listing; pill-shaped control | Navigate away |
| Static | Not clickable: logos, metrics, CIVD cells, video, quote, prose, empty message | Look like a card |

Thirty-two components in six groups:

| Group | Components |
|---|---|
| Chrome | Header Contact, Mega-nav hub and strands, Breadcrumb, Cookie bar |
| Heroes and bands | Hero, CTA pair, Closing CTA band, Prose, Metric box |
| Cards | Offer card (buyable service, grey fill), Theme card (outline), Case card (image placeholder), Report card (portrait document), Article card (no fill, no image), Person card (avatar), Role card (outline, top rule), Triangle tile (a pillar, not a service) |
| Lists and locators | Page tag, Filter bar, Situations list, Row of text links, Link list, Case line, Link line, Pagination, Empty state |
| Proof and media | Logo strip, Quote, Video 16:9, CIVD four-cell, Article body |
| Forms | Form (Work with us, Work for us, email capture, search, report copy) |

Do not mix: a Filter is not a Tag; a Tag is not a Button; a Triangle tile is not an Offer card; a CIVD cell and a Metric box are not Cards; a listing link is not a Case card. The Chrome group appears on every page and is not repeated in the templates below.

### 5.2 Tags: one dimension per page type

Each page type shows tags from one dimension only, three visible at most. The other dimensions still exist as CMS tags and drive filters and automatic proof blocks. Sectors are never shown as tags.

| Page type | Tag dimension |
|---|---|
| Home | Expertise, as one row of five text links (not tags) |
| Service page | Expertise (Related expertise) |
| Case study | Services used |
| Article or report | Expertise |
| Services hub, theme, sector, profile | None |

### 5.3 Home (`/`)

H1: "Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth."

1. **Hero**: H1, strapline "Strategy that works. Execution that delivers.", CTA pair (Contact; What we do), Video 16:9 showreel placeholder.
2. **Trusted partners**: Logo strip. A logo links only where a case study exists.
3. **What we do**: three Triangle tiles with their pillar lines, then the triangle line "Strategy first. Activation to deliver it. Advisors alongside." with a text link to Our Growth Architecture.
4. **Our thinking**: one Report card, one Article card, All thinking. After the offer and before the proof. Not a reports grid.
5. **Our work**: Case cards, a Quote, All work.
6. **Awards**: Logo strip. The FT award sits here, not in the hero.
7. **Growth problems we know best**: Row of text links, the five theme names.
8. **Closing CTA band**.

Home owns no topic. Everything on it exists in full on another page. No long copy, no tags on cards, no sector block, no team grid.

### 5.4 Services hub (`/services/`)

Eyebrow "What we do". H1 **"Our Growth Architecture"**. This is the Growth Architecture page. It names the system, connects the pillars, gives a way in by problem, and puts proof beside each offer.

1. **Hero**: eyebrow, H1, strapline, two short paragraphs from the deck (the path from strategy to execution has become complex and fragmented; Growth Architecture combines market-leading strategic thinking with AI-powered, human-led activation).
2. **Three ways we work with you**: Triangle tiles and the triangle line, anchoring to the three pillar sections below.
3. **Where are you starting from?**: Situations list, seven lines in the visitor's words, each a link. We need to decide where and how to grow (Growth Strategy). We need a new proposition, loyalty or membership offer (Proposition Innovation). We need to understand our customers better (Customer Research and Insight). Our journeys or website are not converting (Experience Engineering). Our strategy is not turning into results (Activation Services). We want AI to pay off (AI Enablement). I want a sounding board I trust (CEO Advisory).
4. **Growth Strategy**: pillar line, one plain sentence, compact CIVD four-cell with a Link line to its home, two Offer cards, one Case line.
5. **Activation Services**: pillar line, one plain sentence linking to Which of the six do you need?, six Offer cards, one Case line.
6. **CEO Advisory**: pillar line, one plain sentence, three Person cards, Our advisors link.
7. **Link line** to Expertise: "We apply these services to the growth problems we know best."
8. **Closing CTA band**.

### 5.5 Service page (eight canonical services)

H1 is the nav label, exactly. H2s carry the searched terms.

1. **Hero**: H1; an also-known-as line where the deck name differs (Our Customer Intelligence practice; Data Agents, built in AgentLab; Our Operating Architecture framework); one support line carrying the searched terms; who this is for; Metric boxes only where the deck gives a figure (Experience Engineering: over 3x EBITDA return; AI Agents for Marketing: 4 weeks to audit, 6 weeks to first agents); CTA pair (Contact with `?topic=`; See our work).
2. **Why this, now**: Situations list, three static lines in the prospect's words, then short copy.
3. **What we do**: Prose. The canonical description. Subheadings use the plain terms.
4. **Proof**: Case cards tagged to the service, directly under the offer. Logo strip as the fallback where no case exists yet.
5. **Named module**: the structure the deck gives each service (table below).
6. **How it works**: phases, named where the deck names them.
7. **Related expertise**: Page tags, three at most.
8. **Related services**: two or three Offer cards.
9. **Related thinking**: Link list.
10. **Closing CTA band**.

People (lead profiles as Person cards) and an FAQ block are specified for every canonical service. They fill as profiles are flagged and questions are written.

| Service | Named module and H2s |
|---|---|
| Growth Strategy | North Star, Growth priorities, Demand signals, Scenario planning as candidate H2s; the CIVD four-cell (Customer, Innovation, Value, Delivery) at `#civd` |
| Proposition Innovation | Value proposition design; Loyalty, Membership, Subscription and Direct-to-consumer propositions, each handing off to its expertise theme |
| Customer Research and Insight | Customer research methods; Customer journey mapping; Research projects; Always-on customer insight; six input types as H3s (digital listening, qualitative, quantitative, customer data analytics, internal knowledge, external market data) |
| Experience Engineering | Find, Redesign, Test, Scale as the How it works sequence; Customer experience (CX) design; Website and digital product; User research and testing, each anchored |
| AI Agents for Marketing | AgentLab at `#agentlab`: twelve named agents in four groups (Reporting and Analytics; Data and Infrastructure; Strategy and Planning; Automation and Execution), entries not pages; 4 weeks, 6 weeks, ongoing as How it works |
| Operating Model Design | Target operating model; Adaptive operating model; Our Operating Architecture framework at `#operating-architecture` as a captioned figure, whose caption links Orchestration (culture, value, capability) to Growth Office |
| Growth Office | Interim growth team; Then embed; Culture, Capability, Value; interim CMO named where accurate |
| AI Enablement | AI skills and adoption; Finding where AI pays off; New business models with AI; maturity assessment as the entry step; the expert network named in the body |

### 5.6 Activation Services group page (`/services/activation/`)

Hero; **The bridge from strategy to results** (Prose: a brilliant strategy only counts if it gets executed and the value shows up; hands-on, AI-powered, human-led, not ongoing operations); **Which of the six do you need?** (Link list, one line per service, so the design / staff / tooling / skills distinction is explicit); **The six Activation services** (six Offer cards); Proof; Related thinking; Closing CTA band. Supporting weight: it explains a Manifesto term and routes, and owns no capability of its own.

### 5.7 CEO Advisory (`/services/ceo-advisory/`)

Hero with the quieter CTA, Arrange a conversation; **Why this, now** (three situations); **Side-by-Side** at `#side-by-side` (Prose: driving customer-led growth is demanding and lonely; a select group of senior leaders with Manifesto thinking and frameworks; adaptive, personality-led, retainer-based); **Our advisors** at `#advisors` (Person cards drawn from profiles flagged as advisor); **How the retainer works**; Related thinking; Closing CTA band. Side-by-Side is always written in full. The proof of this page is the people, so advisor profiles are the launch dependency.

### 5.8 Expertise hub and theme pages

Hub (`/expertise/`): Hero "Our expertise"; five Theme cards; Latest thinking across themes as a Link list; Closing CTA band.

Theme (`/expertise/{theme}/`): Hero with CTA pair; **Our view** (Prose, the unique content: what goes wrong, what good looks like); **Where we help** (Link list of services, the hand-off to the canonicals); **Proof** (Case cards); **Insights** (Link list); Related themes as a Row of text links; Closing CTA band. A theme page describes the problem. It never describes how a service is delivered.

### 5.9 Sector landings

Hero (150 to 300 words); **Clients** (Logo strip); **Case studies** (Case cards, auto from tags); **Services most used here** (Link list); Related thinking; Closing CTA band. No sector point of view, no sector-specific service copy, no children. Indexed only once the landing has three published case studies and two insights tagged to it.

### 5.10 Our work and case study

Our work (`/work/`): Hero; **Featured** (Case card and Quote); **All case studies** (Filter bar with Service open on load and Expertise and Sector behind More filters, Case cards with one service tag each, Pagination); Empty state, shown only when a filter returns nothing; Related thinking; Closing CTA band.

Case study (`/work/{client}/`): Hero with services used as Page tags; **At a glance** (Metric boxes); **The challenge**; **What we did**; **The result** with a Quote and an optional Video 16:9; Related expertise tags; Related thinking; Closing CTA band. Testimonials live here and nowhere else. Read on the page, no PDF.

### 5.11 Our thinking, article and report

Our thinking (`/insights/`): Hero; **Reports** (Report cards, first); **Articles** (Filter bar with Type open and the rest behind More filters, Article cards, Pagination); Empty state; **Events and news** (Link list) with The Nutshell; Related services as a Row of text links; Closing CTA band. Articles and blog posts are one type. Events are a section, not a URL.

Article: Hero with expertise tags; Article body; **What we think**; **How we help** (the hand-off to a service and a theme); Closing CTA band.

Report: Hero with tags; Article body read on the page; an optional Form to receive a copy by email, never a PDF gate; **How we help**; Closing CTA band.

### 5.12 About, Our people, Our approach, Values

About (`/about/`): **Who we are and our story** (with Origins); **How we are distinct** (the mix of agency, client and strategy backgrounds; the Growth Architecture model); **Leadership** (Person cards); **Our approach** teaser; C and N members as a labelled placeholder; Closing CTA band.

Our people (`/about/team/`): **Leadership**; **Consultants**; **Side-by-Side advisors** (`#advisors`); **Associates, expert network and C and N members**; Link line to Careers. Culture over headshots. The mega-nav's Our advisors strand lands on the CEO Advisory page, not here.

Our approach (`/about/how-we-work/`): **How we partner**; **Growth partner videos** (Video 16:9; the partner films live here, not on Home); **Principles**; **Engagement shapes** (strategy project, strategy into activation, embedded growth office, advisory retainer); **Frameworks and tools**, the one place all five named things are listed together, each linking to its anchored home: Growth Architecture, Customer, Innovation, Value and Delivery, Operating Architecture, AgentLab, Side-by-Side; **Working with AI**; Closing CTA band. Method is never a product.

Values and culture (`/about/values/`): Values; Culture; Diversity, equity and inclusion. Light.

### 5.13 Careers, Contact and utilities

Careers (`/careers/`): Hero with studio film; **Life at Manifesto** (Person cards, recent joiners); **Diversity, equity and inclusion**; **Benefits**; **Open roles** (Role cards, with an empty state when there are none); **Not hiring for a listed role?** routing to Work for us; Closing CTA band using Work for us. Role pages read on the page and are noindex once closed.

Contact (`/contact/`): **Work with us** (Form: name, company, email, topic as a select pre-filled from `?topic=`, message); **Work for us** (Form: name, email, message); **Direct contact**, with The Nutshell. Thank-you: one Offer card, one Case card, one Article card as next steps.

The Nutshell (`/newsletter/`): Hero and Form. Search: Form, Link list of results, Empty state. 404: Hero, CTA pair (What we do; Our work), search Form. Legal pages: Hero and Prose stub for legal review.

### 5.14 How the dimensions connect

Cross-links are how services, expertise, work and thinking intersect without duplicate pages. These are template rules, not editorial choices.

| Page | Must link to |
|---|---|
| Service page | Its pillar, two or three related services, up to three related themes, tagged case studies, Our approach |
| Services hub | All three pillar pages, every service (as cards and as situation lines), the CIVD anchor, the advisors anchor, one case per pillar, the Expertise hub |
| Expertise theme | At least two service pages (Where we help) and its filtered work list |
| Sector landing | At least two service pages (Services most used here) and its filtered work list |
| Case study | Every service used, every theme tagged, one sector |
| Article or report | At least one service (How we help) and at least one theme |
| Profile | The services and themes the person leads on; advisors link to CEO Advisory |
| Home | The services hub, the three pillar pages, Our work, Our thinking, the five theme pages |

Anchor text uses the nav label exactly. Where the label is a Manifesto term, the first mention on a page follows it with a plain gloss ("Experience Engineering, our customer experience and website practice").

**Evidence**

- Source B slides 5 to 12: each service has a named structure (CIVD; Find, Redesign, Test, Scale; the AgentLab groups and twelve agents; the adaptive operating model figure; interim then embed through Culture, Capability and Value; maturity assessment then three programmes). Those structures are the named modules. Slides 8 and 9 are the only slides that give figures, so those are the only pages with Metric boxes in the hero.
- Source B slide 4 and Source C: Side-by-Side is a retainer sold on the people; advisor profiles are the substance of the third pillar.
- Source A: the cross-linking table (service to themes, work and insights; theme to services, work and insights; case study to services and themes; insight to services and themes); Insights with a latest section; testimonials inside case studies.
- MURAL: Trusted partners high; FT not in the hero; no homepage reports grid; reports at the top of Our thinking; no PDFs; quotes with work; CIVD kept as the strategy frame with new visuals; growth partner films on Our approach; Life at Manifesto on Careers, not merged with the team listing; qualitative and quantitative evidence on Customer Research and Insight; C and N members as a named group.
- Competitor review: Prophet ("What is your company's context for growth?") and Yonder give two ways in, by problem and by capability, which is why the hub has both the triangle and the seven situations. Elsewhen and Baringa put proof directly under the offer, which is why Proof follows What we do on every service page and a Case line sits under each pillar on the hub. Baringa puts named partners on the capability page and The Foundation makes the team a substantial section, which is why People is specified on service pages and advisors are the CEO Advisory proof. Lippincott and Ellipsis give named systems a visible home, which is why the hub H1 is Our Growth Architecture and Our approach lists the five frameworks. Elixirr's Execution Edge page opens with the plain problem, which is the pattern for the Activation group page.
- Wireframe review (`docs/wireframe-fresh-review.md`): a wireframe hands off only if every rectangle can be named and its interaction type is unambiguous. The seven interaction types and the component library answer that test.

---

## 6. Search language and keyword-led subtitles

### 6.1 The rule

Manifesto's labels stay in the header, mega-nav, footer and H1s. Search language sits under and around them: strand subtitles, H1 support lines, H2s, title tags, meta descriptions and FAQs. Where a deck name and the searched term conflict, and the searched term is what the service actually is, the searched term is the label and the deck name appears once on the page as an also-known-as line. No acronyms or internal shorthand appear in the nav.

| Visible label | Why it stays | Where the search language lives |
|---|---|---|
| What we do | The prospect's question; the peer convention | URL `/services/`; hub H1 Our Growth Architecture |
| Our work | Plain consultancy convention | Title tag "Case studies" |
| Our thinking | Manifesto's own name for the library | URL `/insights/`; H2s Reports, Articles, Events and news |
| Our people, Our approach | Manifesto's labels | URLs `/about/team/` and `/about/how-we-work/` |
| Growth Strategy | Label and searched term agree (~480) | Subtitle "Where to grow and how to win"; support line carries customer-led growth |
| Proposition Innovation | Manifesto offer name; "proposition" is the UK term | Subtitle and H2 "Value proposition design" (~140); one H2 per proposition type |
| Activation Services | The pillar name in the deck and on the call | Subtitle "Hands-on delivery, six services"; the group page explains the bridge |
| Customer Research and Insight | Searched term (deck: Customer Intelligence) | Subtitle "Research methods and journey mapping"; H2s Customer research methods, Customer journey mapping |
| Experience Engineering | Manifesto offer name, the Dayinsure and Key Group model | Subtitle "Customer experience and websites"; H2s for CX, website and digital product, user research; title tag "Experience Engineering: customer experience and websites" |
| AI Agents for Marketing | Searched, marketing-qualified term (deck: Data Agents) | Subtitle "AI marketing agents, guided by experts"; AgentLab as an H2 |
| Operating Model Design | Searched term (deck: Operating Architecture) | Subtitle "Target operating model"; H2 Target operating model; Operating Architecture as the framework name |
| Growth Office | Manifesto offer name | Subtitle "Interim growth team"; H2 Interim growth team; H3 Interim CMO where accurate; title tag "Growth Office: interim growth team and programme office" |
| AI Enablement | Label is the searched term (~170) | Subtitle "AI skills and adoption"; H2s for skills, value cases and business models |
| CEO Advisory | Pillar name; parallels Baringa's CFO Advisory | Subtitles "One-to-one advisory retainer" and "Experienced growth leaders"; advisor and board language in body copy; coaching is adjacent, not the offer |
| Side-by-Side | Named product | Strand and `#side-by-side`. Never SxS. |

Growth Strategy is not retitled Brand Strategy, even though brand strategy (~1,600) outranks growth strategy (~480). Brand and go-to-market language appears in H2s only where the work is truly that.

### 6.2 UK keyword findings behind the subtitles

DataForSEO Google Ads Search Volume and Labs Keyword Suggestions, United Kingdom, 16 September 2026. Average monthly searches, approximate.

| Page | Primary target | Strong adjacent phrases | Used as |
|---|---|---|---|
| Growth Strategy | growth strategy ~480 | growth strategy consultancy ~70; brand strategy consulting ~390; go to market strategy ~880 | Subtitle; support line; H2s where true to the work |
| Proposition Innovation | value proposition design ~140 | value proposition ~3,600 (broad, mixed intent); proposition design ~20; brand proposition ~90 | Subtitle; H2 |
| Customer Research and Insight | customer research methods / companies ~720 | customer journey mapping ~2,900; customer research techniques ~880; customer research agency ~20 | Subtitle; H2s |
| Experience Engineering | experience engineering ~90 | customer journey mapping ~2,900; experience design agency ~110; cx consultancy ~70; website design consultancy ~70 | Keep the label; subtitle and H2s carry CX and websites |
| AI Agents for Marketing | ai marketing agents ~390 | ai agents for marketing ~70; marketing automation consultancy ~90; bare ai agents ~9,900 (too generic to target alone) | Subtitle; title and H1 keep "for Marketing" |
| Operating Model Design | operating model ~880 | target operating model ~1,600; operating model design ~140; operating model consultancy ~10 | Subtitle; H2 |
| Growth Office | interim cmo ~110 to 140 | growth office ~10 (weak; not the primary target) | Subtitle; H2; H3 |
| AI Enablement | ai enablement ~170 | ai transformation consultancy ~10 | The label owns the term |
| CEO Advisory | ceo advisory ~10 | ceo coach ~320; board advisor ~90; executive advisor ~30 (all adjacent) | Relationship page, not volume-led |
| Services hub | growth architecture ~50 | | Named-system and brand page |

Expertise theme titles (Loyalty, Membership, Subscriptions, Pricing, Customer Value) were not keyworded in this pull. Sector landings have no dedicated targets by design.

### 6.3 Where each search intent lands

| A prospect searches or thinks | Lands on |
|---|---|
| customer experience, CX, website, can you build a website | Experience Engineering, via the subtitle and its three anchored sections |
| customer research, market research, surveys, journey mapping | Customer Research and Insight |
| loyalty, membership, subscription, direct-to-consumer | Proposition Innovation H2s; the expertise theme pages |
| pricing, customer lifetime value | Expertise themes; Growth Strategy |
| AI agents, marketing AI, customer data quality | AI Agents for Marketing |
| AI training, AI adoption, AI skills | AI Enablement |
| operating model, target operating model, ways of working | Operating Model Design |
| interim CMO, programme office, PMO | Growth Office |
| our strategy isn't landing, execution, delivery | Activation Services, and the hub's situation line |
| CEO advisor, sounding board, non-exec, retainer | CEO Advisory |
| Growth Architecture, AgentLab, CIVD, Side-by-Side | Services hub H1; the anchored module on the owning page; Our approach |
| a client name | The case study |
| financial services, media, consumer, retail | Footer, Work filters, the sector landing |

**Evidence**

- Source C: the deck is a starting point for alignment, not website copy; HPX failed as a term and clients look for CX; Experience Engineering needs keywords so "can you build a website?" maps clearly; "simplification of language is helpful".
- `docs/keyword-findings.md`: exact product phrases are thin and adjacent demand is the useful signal; "Do not rename the triangle for volume"; strand subtitles earn their keep.
- `docs/nav-wording-decisions.md`: the reasoning for each label, including the three searched-term labels (Customer Research and Insight, AI Agents for Marketing, Operating Model Design) and the coined names kept with supporting copy.
- Competitor review: frog "Customer Research & Insights"; Elixirr "Target Operating Model" and "Customer Experience"; Prophet "Agentic Deployment"; Baringa "CFO Advisory". Every searched-term label has a peer using the same plain phrase.

---

## 7. Evidence

The sources behind the recommendations and what each contributed. Individual Evidence blocks sit under sections 1 to 6. Nothing here is an invented quote or number.

### 7.1 Andy's Growth Architecture Services deck (Source B)

Working draft "Manifesto's Growth Architecture Services", confirmed current against the Drive file on 16 September 2026.

- Slide 1 names the whole offer Growth Architecture Services. That name is the hub H1.
- Slide 2: the triangle; the positioning line; "Strategy that works. Execution that delivers."; the path from strategy to execution has become complex and fragmented. Those lines are the Home hero and the hub intro.
- Slide 3: the services on the triangle, including six Activation services in the order used in the mega-nav, and the three pillar one-liners, which become the plain pillar sentences on the hub.
- Slide 4: Side-by-Side as the CEO Advisory product; retainer; virtual or in person; a select group of senior leaders. The named strand and the `#side-by-side` section.
- Slide 5: the CIVD frame on Growth Strategy, marked "to be updated" (a copy update, not a retirement). The `#civd` module and the compact four-cell on the hub.
- Slides 7 to 12: each service's why, what, structure, figures and example clients. The named modules, the two Metric box heroes, and the proof plan.
- Appendix: the adaptive operating model figure and the Growth Strategy layer (North Star, growth priorities, demand signals, scenario planning). The Operating Architecture figure and the Growth Strategy candidate H2s.

Coverage audit (`docs/andy-deck-coverage.md`): 72 deck elements checked and every one has a stated home in the IA. Deliberate departures from the deck are listed there with their source: CEO Advisory third rather than top; three labels in searched terms; no acronym; deck one-liners on pages rather than in the menu; agents as entries rather than pages.

### 7.2 Meeting with Andy, 7 September 2026 (Source C)

Otter transcript of the Shed and Manifesto check-in, 37 minutes.

- The deck is "a bit of the jigsaw": the packaged services Manifesto wants to be recognised for.
- Weighting: Growth Strategy is the bread and butter; Activation is the bridge from strategy to execution, six offerings, not ongoing operations; CEO Advisory is new, relationship-led, low direct revenue, and "do not design the site around it".
- Language: HPX failed; clients look for CX; Experience Engineering needs keywords so "can you build a website?" maps; Growth Office terminology is hard; the deck is not website copy.
- Sectors and themes: services are sector-agnostic; no sector point-of-view pages; case studies organised by sector are fine for proof; themes are the expertise story ("loyalty and membership experts who work cross-sector"); light sector landings for search, discoverable through tagging.
- Site role: today a post-referral credibility check; the rebuild has to originate and compete with consultancies.
- Actions on Manifesto's side: services copy, case studies, testimonials, team and advisor profiles. Brand: name and logo stay; colour likely to change.

### 7.3 Project documentation

- **Gary's IA feedback (Source A)**: the structural brief for the site. Three intersecting dimensions; one canonical home per topic; Home is a page; separate services from methodology and from sectors; testimonials inside case studies; Insights with a latest section and filters; a clear About hub and a clear Careers hub; the cross-linking table between page types.
- **MURAL board (current-site review, keep/drop, old sitemaps)**: input to chrome labels and page modules, not a competing IA. Absorbed: Our thinking, Our people, Our approach, Careers first-class, Work with us / Work for us, The Nutshell, Trusted partners high, FT not in the hero, no reports grid on Home, no PDFs, blogs merged into articles, CIVD kept, growth partner films on Our approach, Life at Manifesto on Careers, C and N members. Left out: the old seven-peer sitemap, Our clients and Our blog as top-level items, HPX and the old sold-service taxonomy, the 1:1 / Strategic / Execution pyramid. Detail in `docs/mural-gap-check.md`.
- **Old IA columns and early Home and Services wireframes**: checked strand by strand. Every strand has a home. CIVD is visible as a shaped module and Side-by-Side as a mega-nav strand. Detail in `docs/strand-gap-check.md`.
- **IA direction during the process (Sources D to G)**: the constraints these recommendations satisfy. The triangle readable in under two seconds; CEO Advisory visible as a pillar; plain, searched labels; calm density with few chrome elements; best in class on competitor evidence and full deck fidelity, with no deck copy in the menu.

### 7.4 Competitor navigation review

`docs/competitor-nav-review.md`. Ten peers (Prophet, Yonder Consulting, The Foundation, Simon-Kucher, Elixirr, Baringa, Ellipsis, Ekimetrics, Elsewhen, Mando) and six pattern references (Deloitte Digital, Bain Customer Strategy and Marketing, frog, Lippincott, Valtech, Criticaleye), read from the live sites on 15 September 2026.

Patterns adopted: five or six header items; one mega-nav at most; two ways into services, by problem and by capability, without a second menu (Prophet, Yonder, frog); proof directly under the offer (Elsewhen, Baringa, Ekimetrics); the named system given a visible home off the primary nav (Lippincott, Ellipsis, Prophet, Ekimetrics); people on the offer page (Baringa, The Foundation, Criticaleye); the pillars' logic stated in one line (Elixirr, Prophet); a coined family name explained in its first sentence (Elixirr, Ellipsis).

Patterns rejected: sector-led IA or an Industries mega-nav (Simon-Kucher about 50 links, Elixirr about 25, Baringa, Bain 24); a sixty-link services panel (Elixirr); coined solution names that need decoding (Prophet, Valtech, Ekimetrics, Yonder); method as the services menu (Ellipsis); no service pages at all (The Foundation); a hub page that exists only to hold a menu (Prophet's placeholder copy); Blog and Reports as two header items (Elsewhen); a separate testimonials page (Prophet).

Scale: Manifesto's panel carries 17 links against Prophet's about 25, Elixirr's about 60 and Baringa's 18 flat. Yonder, frog and Lippincott have no mega-nav at all.

### 7.5 UK keyword findings

`docs/keyword-findings.md` and `docs/heading-map.md`. DataForSEO Google Ads Search Volume plus Labs Keyword Suggestions, United Kingdom, English, 16 September 2026. Every volume in this report comes from that pull and is listed in section 6.2. Theme titles were not keyworded; a second pass is an open item.

---

## 8. Open questions and decisions for Manifesto

The IA launches without any of these. The wireframe carries a default for each.

**Decisions**

1. **C and N members.** The AI Enablement examples in the deck say "including c&n" and the MURAL board asks for a section. Confirm what C and N refers to before the name is used in client-facing lists. Default: a labelled placeholder on About and Our people, no invented expansion, not a sold service.
2. **Growth Collective.** A current-site nav item with no home in the recommended sitemap. Decide whether it is a public destination (a footer line, a strand under Our thinking or About) or off the public site. Default: not in the header.
3. **Events.** Our thinking carries an Events and news section and a dropdown link. A first-class `/events/` page is justified only if there is enough recap and forthcoming content to sustain it. The October CEO Advisory event launches from the hub or the CEO Advisory page without a new URL. Default: section, not page.
4. **Three service names.** Customer Research and Insight (deck: Customer Intelligence), AI Agents for Marketing (deck: Data Agents) and Operating Model Design (deck: Operating Architecture) describe three offers to the market in searched terms. Peers use the same plain phrases. Fallback if any is refused: that one label and slug takes the deck term, with a subtitle carrying the searched words.
5. **Two coined labels.** No peer uses Experience Engineering or Growth Office. The deck argues for both; competitors argue for Customer Experience and Digital, and Interim Growth Team. Default: keep both with their subtitles.
6. **Careers as a header item.** Six items with Careers first-class keeps the Contact split honest. The alternative is five items plus Contact, with Careers under About. Default: first-class.
7. **Our thinking versus Insights.** Confirm the label. The URL stays `/insights/` either way.

**Confirmations that affect copy more than structure**

- Whether interim CMO language is accurate for Growth Office.
- Whether Growth Strategy should also target brand strategy consulting language, and how that overlaps with Proposition Innovation.
- The assignment of the twelve AgentLab agents to the four groups, which is a reading of slide 9.
- Whether the CIVD frame stays current once slide 5 is rewritten. If it is retired, the four-cell modules come out and no URL changes.
- Proposed fixed text: the triangle line, the three pillar sentences, the seven situation lines, the six "which of the six" lines, the pillar lines and the strand subtitles. Rules to keep: plain, in the visitor's words, one line each, no Manifesto shorthand.
- A second keyword pass on the five theme titles before those URLs lock.
- Advisor profiles, Growth Strategy and Proposition Innovation copy, case studies and testimonials, which Manifesto is sourcing.
- Whether the tracked Email Mark route stays on Work with us, and whether a still or a film opens the Home hero at launch.

---

## Appendix: reading the wireframe

1. Open https://temp-manifesto-ia.pages.dev/ or `mocks/index.html` from the repository. No build step or server is needed.
2. Home loads with the menu closed. Hover **What we do**. Name the three pillars without reading anything in grey. Every strand shows its subtitle, and the three headings share one contrast.
3. Click **All services**. The hub H1 reads Our Growth Architecture, the three tiles and the triangle line sit in the first screen, and the seven situations follow.
4. The sidebar on every page holds two panels. **Page fundamentals**: URL, template and weight, H1, keywords with UK volume where the pull has it, menu subtitle, ordered H2s and H3s, intent, content notes, links to. **Components on this page**: the reusable blocks on the canvas in order, by their library names. Hover any block on the canvas to see its name.
5. **All pages** (sidebar) or `sitemap.html` reaches every URL. **Component library** (`/catalogue/`) shows every component once, with its interaction type.
6. The specification behind the wireframe: `docs/01-primary-navigation.md`, `docs/02-sitemap.md`, `docs/03-page-layouts.md`, `docs/04-canonicals-and-seo.md`, `docs/heading-map.md`, `docs/keyword-findings.md`, `docs/competitor-nav-review.md`, `docs/andy-deck-coverage.md`, `docs/06-decisions-log.md`.
