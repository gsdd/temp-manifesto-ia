# Information architecture recommendations

**Manifesto Growth Architects**  
Shed Collective · September 2026

This report recommends the information architecture for the new Manifesto Growth Architects website: hierarchy, navigation, sitemap, mega-nav, page templates, and search language. It is the client-facing summary of the IA package. The clickable wireframe is the working model of the same recommendations (`mocks/index.html`).

---

## 1. Executive summary

We recommend a services-led site organised around Andy's Growth Architecture triangle: **Growth Strategy**, **Activation Services**, and **CEO Advisory**. Six items sit in the header. What we do is the only mega-nav. Our work, Our thinking, About, Careers and Contact complete the chrome. Expertise and sectors are real dimensions with their own pages, but they do not compete with services in the top bar.

The current site works as a credibility check after a referral. The rebuild has to originate enquiries from people who have never heard of Manifesto. That means the first screen must answer "what can you do for me?", then "do you understand my problem?", then "have you done this for businesses like mine?"

CEO Advisory is a full-weight third pillar. Same contrast and heading weight as Growth Strategy and Activation. It is quieter only because the column is slightly narrower and holds two strands rather than six. Greying it out makes it look like a second-class offer. It is not.

Every strand in the mega-nav now carries a short, keyword-led subtitle so a prospect can see what they get. Manifesto labels stay. Search language sits under the label and on the page. Volumes cited in this report are UK Google Ads averages from DataForSEO, 16 September 2026. None are invented.

CIVD stays as an on-page module on Growth Strategy, not a nav item. Named frameworks each have one home. Cross-links run Services ↔ Expertise ↔ Work ↔ Thinking. Footer, forms, listing filters, empty states, pagination, search, 404 and legal pages are in the wireframe as stubs or full templates.

**Evidence**

- Andy's deck (Source B): the offer is the triangle of Growth Strategy, Activation Services and CEO Advisory; the hub name is Growth Architecture Services.
- 7 September Otter check-in (Source C): Growth Strategy first, Activation second, CEO Advisory third; do not design the whole site around advisory; the deck is not website copy.
- MURAL keep/drop: six-item chrome (Our thinking, Careers first-class); no homepage reports grid; CIVD keep, new visuals; The Nutshell named from the current contact form.
- Competitor review (`docs/competitor-nav-review.md`): Prophet's What We Do panel is about 25 links; Elixirr's Services panel about 60. A sparse triangle menu is already calmer than the peer set. The gap to best in class is on the pages, not extra nav items.
- UK keyword findings (`docs/keyword-findings.md`): exact Manifesto phrases are often thin; adjacent demand (journey mapping, value proposition design, target operating model, interim CMO) belongs in subtitles and H2s, not as extra top-nav labels.

---

## 2. Recommended hierarchy and primary navigation

**Header (six items, plus logo and Contact button)**

**What we do** | **Our work** | **Our thinking** | **About** | **Careers** | **Contact**

That is the cap. Nothing else joins the top bar.

| Item | Behaviour | Lands on |
|---|---|---|
| Logo | Home | `/` |
| What we do | Mega-nav on hover; click goes to the hub | `/services/` |
| Our work | Plain link | `/work/` |
| Our thinking | Small type dropdown: Reports, Articles, Events and news, All thinking | `/insights/` |
| About | Small dropdown: Our people, Our approach, Values and culture | `/about/` |
| Careers | Plain first-class link | `/careers/` |
| Contact | Button | `/contact/` |

**Rationale**

- Services are the spine. A prospect's first question is what Manifesto can do.
- Careers is first-class so Contact can honestly split Work with us from Work for us.
- Our thinking is Manifesto's name for the insights library (MURAL). The URL stays `/insights/`.
- Sectors stay out of the header. They live in the footer, in Work and Thinking filters, and as light landings.
- Search is a footer field plus `/search/`, not a seventh header item.

**Primary and secondary CTAs**

- Primary: Contact button (Work with us). Careers routes use Work for us.
- Secondary: text link, usually See our work or What we do.
- Forms: Contact has two blocks, `#work-with-us` and `#work-for-us`. Careers still owns roles, Life at Manifesto, DEI and benefits.

**Evidence**

- Source A: three intersecting dimensions (services, expertise, sectors) with one canonical home per topic; Home is a page, not a hub.
- Source D / F: simplify the mega-nav; make the triangle obvious; five to six header items, not seven content peers.
- MURAL: Our thinking, Our people, Our approach, Careers first-class, split work-with-us / work-for-us.
- Competitor pattern: "What we do" is the services label at Prophet, Yonder and Deloitte Digital. Lippincott runs a four-item header. No peer in the set puts sectors in a services mega-nav as equals.

---

## 3. Full sitemap

URL pattern: trailing slash, kebab-case slugs, **flat services** under `/services/` even when the menu groups them. Grouping is a menu concern. URLs survive if the packaging changes.

### Canonical and supporting pages

| URL | Page | Weight |
|---|---|---|
| `/` | Home | Canonical |
| `/services/` | Our Growth Architecture (services hub) | Canonical |
| `/services/growth-strategy/` | Growth Strategy (includes `#civd`) | Canonical |
| `/services/proposition-innovation/` | Proposition Innovation | Canonical |
| `/services/activation/` | Activation Services group | Supporting |
| `/services/customer-research/` | Customer Research and Insight | Canonical |
| `/services/experience-engineering/` | Experience Engineering | Canonical |
| `/services/ai-agents-for-marketing/` | AI Agents for Marketing (`#agentlab`) | Canonical |
| `/services/operating-model-design/` | Operating Model Design | Canonical |
| `/services/growth-office/` | Growth Office | Canonical |
| `/services/ai-enablement/` | AI Enablement | Canonical |
| `/services/ceo-advisory/` | CEO Advisory (`#side-by-side`, `#advisors`) | Supporting |
| `/expertise/` | Expertise hub | Supporting |
| `/expertise/{loyalty,membership,subscriptions,pricing,customer-value}/` | Theme pages | Supporting |
| `/sectors/{financial-services,media,consumer,retail}/` | Light sector landings | Light |
| `/work/` | Our work listing | Canonical |
| `/work/{client}/` | Case study | Supporting |
| `/insights/` | Our thinking listing | Supporting |
| `/insights/{slug}/` | Article or report | Supporting |
| `/about/` | About | Supporting |
| `/about/team/` | Our people | Supporting |
| `/about/team/{name}/` | Profile | Light |
| `/about/how-we-work/` | Our approach | Supporting |
| `/about/values/` | Values and culture | Light |
| `/careers/` | Careers | Light |
| `/careers/{role}/` | Role | Light |
| `/contact/` | Contact | Utility |
| `/contact/thank-you/` | Thank you | Utility |
| `/newsletter/` | The Nutshell | Utility |
| `/search/` | Search | Utility |
| `/privacy-policy/`, `/cookie-policy/`, `/terms/`, `/accessibility/` | Legal stubs | Utility |
| `/404/` | Page not found | Utility |
| `/catalogue/` | Page modules (wireframe only) | Not a live URL |

There is no `/sectors/` index. `/sectors/` redirects to `/work/`. There is no separate `/side-by-side/`, `/civd/`, `/agentlab/` or events URL unless Decision 8 (Events) later warrants one.

**Evidence**

- Source A: one canonical home per topic; themes under `/expertise/`; sectors light.
- Source B: eight buyable services plus the Activation grouping and CEO Advisory as the third pillar.
- Source C: sector-agnostic services; four sectors; travel and leisure under Consumer.
- MURAL: The Nutshell; no more PDFs (reports expand on the page); blogs merged into articles.

---

## 4. Mega-nav / What we do

The panel is the triangle laid flat. Three linked hub headings, each with a trailing arrow. Strands sit as siblings under the hub. Growth Strategy and Activation start with Overview so the heading never looks like a fake label over a lonely child. CEO Advisory shows both named strands.

| Growth Strategy | Activation Services | CEO Advisory |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one support for leaders |
| Overview · Where to grow and how to win | Overview · Hands-on delivery, six services | Side-by-Side · One-to-one advisory retainer |
| Proposition Innovation · Value proposition design | Customer Research and Insight · Research methods and journey mapping | Our advisors · Experienced growth leaders |
| | Experience Engineering · Customer experience and websites | |
| | AI Agents for Marketing · AI marketing agents, guided by experts | |
| | Operating Model Design · Target operating model | |
| | Growth Office · Interim growth team | |
| | AI Enablement · AI skills and adoption | |

Footer row under the columns: **All services** · **Expertise** · **Our work**.

CEO Advisory uses the same ink and heading weight as the other pillars. The column is slightly narrower because it holds two strands, not because it is de-emphasised.

CIVD is not in this menu. AgentLab is not in this menu. Growth Partner is not a sold-service label. Those live on pages.

**Evidence**

- Source B slide 2: triangle of CEO Advisory, Growth Strategy, Activation Services; strapline "Strategy that works. Execution that delivers."
- Source B slide 3: six Activation services in deck order; Proposition Innovation under Growth Strategy; Side-by-Side as the CEO Advisory product.
- Source C (Otter): Experience Engineering must map to "can you build a website?"; Growth Office terminology is hard; order of prominence Growth Strategy, then Activation, then CEO Advisory.
- D-02 originally chose a quieter type treatment. Client review of the wireframe: grey reads as second-class. D-57 replaces type-quieting with width-only quieting.
- D-35 had retired item subtitles except two quiet lines. Client review: those lines mostly said nothing useful, except Experience Engineering. D-58 restores a short subtitle on every strand, drawn from keyword findings, not from deck one-liners.
- Competitor review: Elixirr uses "Target Operating Model"; frog uses "Customer Research & Insights"; Prophet uses "Agentic Deployment". Manifesto labels stay; those phrases inform subtitles and H2s.

---

## 5. Page-type structures

Each template is an ordered list of modules. Shapes stay consistent: offer cards for services, image cards for cases, document cards for reports, person cards for people, logo rows for clients and awards, quote blocks for testimonials, 16:9 for film, four-cell for CIVD, metric boxes for numbers.

### Home (`/`)

1. Hero: positioning H1, strapline, primary Contact, secondary What we do, showreel placeholder.
2. Trusted partners: logo row.
3. What we do: three equal-weight triangle blocks plus the triangle line and a link to Our Growth Architecture.
4. Our thinking: featured report + article, All thinking. After the triangle, not a strip at the foot.
5. Our work: three case cards, quote, All work.
6. Awards: logo row (FT sits here, not in the hero).
7. Growth problems we know best: five theme names as text links.
8. Closing CTA: Contact + See our work.

### Services hub (`/services/`)

1. Hero: eyebrow What we do, H1 Our Growth Architecture.
2. Three ways we work with you: equal-weight triangle.
3. Where are you starting from?: seven situation lines.
4. Growth Strategy pillar: sentence, compact CIVD, two service cards, one case line.
5. Activation Services pillar: sentence, six service cards, one case line.
6. CEO Advisory pillar: sentence, advisor cards, Our advisors.
7. Link through to Expertise.
8. Closing CTA.

### Service page (canonical services)

1. Hero: H1 (Manifesto label), optional also-known-as, hero line, who it is for, numbers where the deck gives a figure, primary Contact, secondary See our work.
2. Why this, now: three situations plus short copy.
3. What we do / named modules (CIVD, AgentLab, Find-Redesign-Test-Scale, target operating model, interim growth team, and so on).
4. Proof: case cards.
5. Related expertise (tags, max three).
6. Related services (cards).
7. Related thinking (report + article).
8. Closing CTA.

Activation group page adds "Which of the six do you need?" and proof, then related thinking. CEO Advisory adds Side-by-Side, Our advisors, how the retainer works, then related thinking. Primary CTA on CEO Advisory is Arrange a conversation.

### Expertise hub and theme

Hub: five theme cards, latest thinking, closing CTA.  
Theme: Our view, Where we help (service list), Proof, Insights, related themes, closing CTA.

### Work listing and case

Listing: featured case + quote; filters (Service open, Expertise and Sector behind More filters); results; pagination; empty state; related thinking; closing CTA.  
Case: result hero with service tags; at a glance metrics; challenge; what we did; result + quote + optional film; related expertise; related thinking; closing CTA.

### Thinking listing and article

Listing: Reports; Articles with type filters plus More filters; pagination; empty state; Events and news + The Nutshell; related services / expertise / work; closing CTA.  
Article or report: hero with theme tags; body; optional email gate on reports; how we help (service + theme); closing CTA.

### About, people, approach

About: story, what makes us different, leadership, how we work teaser, clients, values and careers teaser, CTA.  
Our people: role groups, Side-by-Side advisors, optional associates.  
Our approach: principles, engagement shapes, the five named frameworks (each linked to its home), working with AI, CTA. Growth partner language and partner films live here, not in the mega-nav.

### Careers and Contact

Careers: Life at Manifesto, DEI, benefits, open roles, speculative route to Work for us, closing CTA.  
Contact: Work with us form, Work for us form, direct contact, The Nutshell. Thank-you: three onward links.

### Page modules catalogue (`/catalogue/`)

Wireframe only. Live blocks in order, no working-notes sidebar. Title and nav labels say Page modules, not chips.

**Evidence**

- Source B slide 5: CIVD (Customer, Innovation, Value, Delivery) still on the Growth Strategy slide, marked "to be updated" as copy, not retirement. MURAL: keep CIVD, different visuals; it is the strategy frame, not Side-by-Side. Placement: on-page module, not nav (`docs/strand-gap-check.md`).
- Source B slides 7 to 12: each Activation service has a named structure (methods, Find/Redesign/Test/Scale, AgentLab groups, Operating Architecture, interim then embed, AI skills). Those are page modules.
- Competitor review: Prophet and Yonder give two ways in (problem and capability); Elsewhen and Baringa put proof under the offer; Lippincott and Ellipsis give named systems a visible home. That is why the hub has situations plus the triangle, and why proof sits high on service pages.
- MURAL: Trusted partners high; FT not at the top; no homepage reports grid; quotes with work; reports at the top of Our thinking; no more PDFs.

---

## 6. Evidence blocks

This section indexes the sources behind the recommendations. Individual **Evidence** blocks also sit under sections 1 to 5 and 7. Nothing here is an invented quote or volume.

### Andy's Growth Architecture triangle / deck (Source B)

- Working draft "Manifesto's Growth Architecture Services", confirmed current against the Drive file on 16 September 2026 (`docs/andy-deck-coverage.md`).
- Slide 1: the whole offer is named Growth Architecture Services.
- Slide 2: triangle of CEO Advisory, Growth Strategy, Activation Services; positioning line "Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth"; "Strategy that works. Execution that delivers."
- Slide 3: services on the triangle, including six Activation services.
- Slide 4: Side-by-Side as the named CEO Advisory product (retainer, virtual or in person). SxS is not used on the site.
- Slide 5: CIVD frame still present.
- AgentLab: named catalogue of marketing and data agents on the AI Agents for Marketing page, not a nav item.

### Otter notes (Source C)

- Shed x Manifesto check-in, 7 September 2026. Recorded in `docs/00-sources.md` and cited through `docs/06-decisions-log.md`.
- Weighting: Growth Strategy first, Activation second, CEO Advisory third.
- Language: the deck is not website copy; plain searched language wins in the nav.
- Experience Engineering needs to be understandable as websites / CX. Growth Office terminology is hard.
- Sectors are proof, not a second services taxonomy.

### MURAL keep / drop (`docs/mural-gap-check.md`)

- Keep: Trusted partners high; case studies pulled up; reports at the top of thinking; The Nutshell; CIVD with new visuals; Life at Manifesto on Careers; Work with us / Work for us split.
- Drop: homepage reports grid; FT in the hero; PDFs as the reading format; Our clients as a top-level item; Our blog as a separate nav item; old seven-item sitemap as peers.

### Competitor nav patterns (`docs/competitor-nav-review.md`)

Read from live sites on 15 September 2026.

- Prophet: What We Do mega-nav, about 25 links; Growth Strategy as a service name; two ways into services.
- Elixirr: large Services panel (about 60 links); "Target Operating Model"; "Execution Edge" as the nearest peer to Growth Office.
- frog: "Customer Research & Insights".
- Elsewhen: proof under digital / CX offers; website and product build.
- Lippincott / Ellipsis: named frameworks on a hub, not in the primary nav.
- Yonder, frog, Lippincott: some peers have no mega-nav at all. Manifesto's triangle panel is already sparse relative to Prophet and Elixirr.

### UK keyword findings (`docs/keyword-findings.md`)

DataForSEO Google Ads Search Volume plus Labs Keyword Suggestions. United Kingdom, 16 September 2026. Average monthly volumes.

| Phrase | UK vol (approx.) | Used as |
|---|---|---|
| growth strategy | ~480 | Growth Strategy primary; Overview subtitle "Where to grow and how to win" |
| value proposition design | ~140 | Proposition Innovation subtitle |
| customer research methods / companies | ~720 | Customer Research subtitle (with journey mapping ~2,900) |
| experience engineering | ~90 | Keep label; subtitle "Customer experience and websites" |
| ai marketing agents | ~390 | AI Agents subtitle (not bare "ai agents" ~9,900) |
| target operating model | ~1,600 | Operating Model Design subtitle |
| interim cmo / interim growth team | ~110 to 140 | Growth Office subtitle (growth office itself ~10) |
| ai enablement | ~170 | AI Enablement subtitle |
| ceo advisory | ~10 | Keep label; relationship page, not volume-led |

Exact product phrases are often thin. That is normal for senior B2B consultancy. Adjacent demand informs subtitles and H2s. It does not rename the triangle.

---

## 7. Naming and search language decisions

| Visible label | Why it stays | Where search language lives |
|---|---|---|
| What we do | Prospect language; peer pattern | Hub H1 is Our Growth Architecture |
| Our thinking | MURAL / current-site name | URL `/insights/`; H2s Reports, Articles, Events and news |
| Our people / Our approach | MURAL labels | URLs stay `/about/team/` and `/about/how-we-work/` |
| Proposition Innovation | Manifesto offer name | Subtitle and H2: value proposition design |
| Experience Engineering | Manifesto offer name | Subtitle: customer experience and websites |
| Growth Office | Manifesto offer name | Subtitle: interim growth team |
| AI Agents for Marketing | Marketing-qualified, not generic AI | Subtitle: AI marketing agents, guided by experts. AgentLab on the page. |
| Operating Model Design | Searched term from v3 wording pass | Subtitle: target operating model |
| Customer Research and Insight | Searched term from v3 wording pass | Subtitle: research methods and journey mapping |
| CEO Advisory | Triangle pillar name | Subtitles: one-to-one advisory retainer; experienced growth leaders. Coaching is adjacent, not the offer. |
| Side-by-Side | Named product | On-page and as a strand. Never SxS. |

Do not retitle Growth Strategy to Brand Strategy (~1,600) even though volume is higher. Brand / GTM language may appear in H2s where the work is truly that.

**Evidence**

- `docs/nav-wording-decisions.md`: v3 renamed three deck terms to searched terms (Customer Research and Insight, AI Agents for Marketing, Operating Model Design) and kept coined names with supporting copy.
- Keyword findings: "Do not rename the triangle for volume."
- Source C: Andy agreed the deck is not website copy.

---

## 8. Open decisions still needing client input

These are decisions, not a covering letter. The IA can launch without them; the wireframe already has a default.

### C&N

The AI Enablement examples in the deck say "including c&n". The phrase is not expanded on the slide. **Decision:** confirm what C&N refers to before that name is used in client-facing lists (About, AI Enablement, or a membership block). Default in the wireframe: a labelled stub on About, no invented expansion.

### Growth Collective

Not a current sitemap URL. If it is a live offer or community, it needs a home (likely under About or Our thinking), a label, and a weight. If it is internal, it stays off the public IA. **Decision:** is Growth Collective a public destination, a footer line, or off-site?

### Events

Our thinking already has an Events and news section and a dropdown link. A separate `/events/` page is only justified if there is enough recap and forthcoming content to sustain it. **Decision:** section on the hub (current default) or a first-class listing? The CEO Advisory event noted for October can launch from the hub or the CEO page without a new URL.

Related confirmations that affect copy more than structure: whether interim CMO language is accurate for Growth Office; whether Growth Strategy should also target brand strategy consulting; a second keyword pass on theme titles (Loyalty, Membership, Subscriptions, Pricing, Customer Value); advisor profiles ready at launch.

---

## 9. How to open the clickable wireframe

1. Open `mocks/index.html` in a browser. No build step or server is required. From the `mocks/` folder, `python3 -m http.server` is optional.
2. Home loads with the menu closed. Hover **What we do** to open the mega-nav. Check that all three pillar headings share the same contrast, and that every strand has a subtitle.
3. Use **All pages** (heading map) or `mocks/sitemap.html` to reach every URL. **Page modules** (`mocks/catalogue/index.html`) lists live blocks only. It does not show working notes.
4. Footer links (The Nutshell, sectors, legal, search) all resolve. Cookie bar sits above the footer. Contact shows both forms. Our work and Our thinking show filters, pagination and an empty state.
5. Spec documents behind the mock: `docs/01-primary-navigation.md`, `docs/02-sitemap.md`, `docs/03-page-layouts.md`, `docs/keyword-findings.md`, `docs/06-decisions-log.md`.
