# Competitor navigation and IA review (v5, Part A)

Gary's ask of 16 September: the v4 navigation is calm but not yet best in class, and Andy's Growth Architecture Services deck may not be fully reflected. Before refining, look at how Manifesto's real peers structure their navigation, services and IA.

This document records what those sites actually do. Every label, grouping and count below was read from the live site on 15 September 2026 (header and footer markup, plus the services hub and one service page where it mattered). Where a site could not be read, that is stated rather than guessed. The conclusions are in the patterns table at the end and are carried into `v5-refinements.md`.

Related: `andy-deck-coverage.md` (Part B), `v5-refinements.md` (Part C).

---

## 1. Who the peers are

Manifesto sells customer-led growth strategy, proposition and loyalty work, customer experience and digital activation, AI-enabled marketing activation, and a senior advisory retainer, to UK mid-cap and corporate leaders. The peer set below is biased toward firms that sell the same things, at a comparable scale, to the same buyers. Big-firm practices are included only for pattern, and are marked as such.

| # | Firm | Why it is a peer | Read from |
|---|---|---|---|
| 1 | **Prophet** (prophet.com) | Growth strategy consultancy; brand, experience, AI-driven marketing; "strategy to execution" positioning almost identical to Andy's | Home, What We Do mega-nav, Growth Strategy service page |
| 2 | **Yonder Consulting** (yonderconsulting.com) | UK insight, strategy, brand and experience consultancy; London-based; financial services, luxury, retail | Home, What we do hub |
| 3 | **The Foundation** (the-foundation.com) | "The customer-led growth consultancy", London; proposition development and customer growth strategy; the closest positioning match in the UK | Home, What we do (Our Work), Our Perspectives, Our Team, Contact. Header markup is blocked to scripted requests; sections inferred from page titles and internal links |
| 4 | **Simon-Kucher** (simon-kucher.com) | Commercial growth consultancy: pricing, propositions, sales, customer strategy; strong on pricing, one of MGA's expertise themes | Home, Consulting hub |
| 5 | **Elixirr** (elixirr.com) | UK challenger consultancy; strategy, digital experience, research and insights, AI, and "Execution Edge" (the nearest thing to Growth Office on any peer site) | Home mega-nav, Execution Edge page |
| 6 | **Baringa** (baringa.com) | UK consultancy with a Customer and Digital capability; loyalty in financial services; FT-ranked | Home mega-nav, Customer and Digital capability page |
| 7 | **Ellipsis** (ellipsisandco.com) | Loyalty consultancy ("We Are The Loyalty Experts"); Customer Science method; the loyalty specialist pattern | Home, header |
| 8 | **Ekimetrics** (ekimetrics.com) | AI and data for marketing and commercial decisions; marketing effectiveness, customer value orchestration; nearest peer to AI Agents for Marketing | Home, header |
| 9 | **Elsewhen** (elsewhen.com) | UK AI and digital product consultancy; user research, CX strategy, product design and build; the "can you build a website?" competitor | Home, Services hub |
| 10 | **Mando** (mando-connect.co.uk, redirects to mando.co.uk) | UK loyalty, rewards and partnerships agency; the loyalty activation pattern | Home, header |
| P1 | **Deloitte Digital** (deloittedigital.com) | Pattern only: large practice, function-led What we do | UK and US home header |
| P2 | **Bain, Customer Strategy and Marketing** (bain.com) | Pattern only: how a strategy house frames customer strategy | Capability page header |
| P3 | **frog, part of Capgemini Invent** (frog.co) | Pattern only: design and innovation; problem-led services hub | Home, Services hub |
| P4 | **Lippincott** (lippincott.com) | Pattern only: brand and experience consultancy with a four-item header and named frameworks | Home, Solutions hub |
| P5 | **Valtech** (valtech.com, absorbed Kin + Carta) | Pattern only: experience consultancy with coined offering names | UK home header |
| P6 | **Criticaleye** (criticaleye.com) | Pattern only: peer-to-peer board community with Board Mentors; the nearest public model to Side-by-Side | Home |

Substitutions from the brief's suggested list, and why:

- **Fahrenheit 212**: site no longer serves (TLS failure); the firm was folded into Capgemini Invent. frog, the Capgemini Invent design and strategy brand, is used instead as a pattern reference.
- **Made Thought**: a brand and design studio, not a growth or loyalty consultancy. Replaced by Ellipsis and Mando, which are real loyalty and CX peers.
- **Accenture Song**: its pages on accenture.com return 404 or a JavaScript shell to a plain request, so no navigation could be read. Deloitte Digital is used for the large-practice pattern instead.
- **McKinsey Growth, Marketing and Sales**: request timed out twice. Bain's equivalent page is used for the strategy-house pattern.
- **Dayinsure / Key Group world**: these are Andy's clients, not competitors. The UK firms that sell into that world (Elsewhen, Elixirr Digital Experience, Baringa Customer and Digital) are covered.

---

## 2. Site by site

For each site: primary nav labels exactly as shown; how services are grouped; how method, offers, industries and expertise themes are handled; what is best in class; what to avoid. Counts are links, not words.

### 2.1 Prophet

**Primary nav**: What We Do, Work, Thinking, About, Connect (contact).

**Services grouping**: One mega-nav under What We Do with four groups. Three are outcome-led "solution" families and one is a capability list:

- Growth Solutions (6): Growth Strategy, Go-to-Market Innovation, Brand-Led Business Transformation, M&A Growth Acceleration, Culture as Catalyst, New Business Building
- Marketing Solutions (3): Build, Launch and Grow Brands; Demand Marketing; Campaigns, Media and Experiences
- Augmented Intelligence (7): AEO Moves, AI-Driven Commercial Impact, AI-Driven Marketing Modernization, AI-Augmented Customer Insights, AI-Native Innovation, Agentic Deployment, AI-Enabled Culture
- Services (5): Brand Building, Marketing Excellence, Business Strategy, Experience & Innovation, Organization & Culture

Around 25 links in the panel. Work has three children (Case Studies, Prophet Studio, Testimonials). Thinking has a posts archive, a named-author section (Aaker) and three featured reports. About has Leadership, Culture, News & Press, Uncommon Growth Lab, Impact, Careers.

**Method vs offers vs industries vs themes**: No industries in the header at all. Method and named IP live as a lab ("Uncommon Growth Lab") under About and as named reports under Thinking. The distinction between "Solutions" (what outcome you want) and "Services" (what capability you buy) is made explicit in the same panel.

**Service page pattern** (Growth Strategy): H1 with a plain promise ("Customer-focused growth strategies built to win"), one paragraph, then **"What is your company's context for growth?"** with three named situations (current strategy unlikely to hit target; change in customer behaviour requires revitalisation; need new or adjacent sources of growth). Then proprietary research, then thinking, then contact. Problem entry lives on the page, not in the menu.

**Best in class**: Five header items; a single mega-nav; "Work" and "Thinking" as plain sections; problem-led entry handled as a block on each service page; named IP given a home (a lab) without a nav item; no sector menu.

**Avoid**: Coined solution names ("Culture as Catalyst", "AEO Moves", "Uncommon" everything) that need a sentence to decode. The `/what-we-do/` hub page currently renders Lorem Ipsum placeholder copy: a hub that exists only to hold a menu gets neglected. Testimonials as a separate page (Source A already ruled this out).

### 2.2 Yonder Consulting

**Primary nav**: What we do, Work, Thinking, About, Join, Offices. No dropdowns.

**Services grouping**: The What we do page is the whole menu. It opens "Engage through outcome-led solutions or tap into specialist services" and then shows both:

- Five outcome-led groups, each with three bullets: Reconnecting brands and audiences; Unlocking unfair advantage; Shaping minds and markets; Creating the case for change; Activating people and culture
- Six standalone services with sub-bullets: Insight, Omnibus, Data science & Analytics, Strategy, Creative, Data Solutions

**Method vs offers vs industries vs themes**: No industries in the nav; a one-line client sentence on Home names four sectors. No separate method section; "how" is folded into the outcome groups. No expertise themes as a dimension.

**Best in class**: The flattest header in the set that still works. The hub makes the two-axis idea (outcome entry and capability entry) explicit in one sentence. Everything a buyer needs is one click from Home.

**Avoid**: Outcome headings are poetic and opaque ("Unlocking unfair advantage", "Shaping minds and markets"). They read well but fail Source A's test: can a client tell within seconds whether you solve their problem? Six standalone services with fifteen-plus sub-bullets on one page is also a long scroll.

### 2.3 The Foundation

**Sections found**: Home; What we do (the page is titled "Our Work" and is a case study list); Our Perspectives; Our Team; Our Publications; Contact Us; a newsletter ("The Pioneer"). No service pages were found.

**Services grouping**: There are no service pages. Offers appear only as tags on case studies ("Proposition Development", "Customer Growth Strategy"). The positioning line ("The customer-led growth consultancy") and two books do the explaining.

**Method vs offers vs industries vs themes**: Method is the brand (the Customer Copernicus framework, "customer pioneers"). No industries. No themes. Team is a first-class section with long biographies including Associates.

**Best in class**: Proof-first. Case studies with plain outcome headlines ("Creating a billion-pound, customer-led turnaround") carry the site. Team biographies are substantial and are a section in their own right, which is exactly what Otter asks for on advisor profiles. Named IP (two books, a framework) is a section (Our Publications), not a nav gimmick.

**Avoid**: With no service pages, a prospect cannot answer "can they do X for me?" without reading case studies. Search intent for "customer strategy consultancy" or "proposition development" has no canonical landing. This is the credibility-check site Andy described MGA's current site as being, done well; it is not an origination site.

### 2.4 Simon-Kucher

**Primary nav** (from header markup): Consulting, Industries, What we think, Careers, Events, Who we are, Contact us. Plus a link to their software product (Engine).

**Services grouping**: Consulting is a mega-nav with capability families and sub-offers: Commercial Strategy & Pricing (Customer, Product & Market Strategy; Pricing Strategy & Revenue Management with Dynamic Pricing, Monetization Strategy, Revenue Management; Sales Excellence; Sustainability), Digital Growth "Elevate" (Advanced analytics, Customer experience strategy, Technology strategy, Digital transformation strategy), Transaction Services & Private Equity.

**Method vs offers vs industries vs themes**: Industries is the biggest menu on the site: five sectors with around fifty sub-industry links. Insights are organised by industry and by hot topic (Generative AI, Tariffs, Price Inflation, Sustainability). Method is not separated; it lives in capability copy ("scientific methodologies").

**Best in class**: Plain capability labels a buyer would search ("Customer experience strategy", "Pricing Strategy & Revenue Management"). A one-line positioning promise repeated on every hub ("unlocking better growth").

**Avoid**: Sector-led IA. Fifty industry links is a directory, not a menu. Coined programme names inside the menu ("Elevate") need an "Overview" item to explain them. Country selector in the header (irrelevant to MGA).

### 2.5 Elixirr

**Primary nav**: Industries, Services, Case Studies, Resources, Careers, About, Investors.

**Services grouping**: Services is a mega-nav with six families, each with seven to eleven children, around 60 links in total:

- Strategy & Transformation (10, including Business Strategy, Define C-Suite Agenda, Pricing Excellence, Go-to-Market Transformation, Transformation Management)
- Operational Excellence (8, including Business & Operating Models, Target Operating Model, Change Management)
- AI, Data & Technology (9, including AI Consulting, Data & Analytics, Data Strategy)
- Digital Experience (8, including Customer Experience, Digital Design & Build, App Design & Development, Digital Marketing)
- Research & Insights (7, including Customer Understanding, Behavioural & Advanced Analytics, Product & Service Innovation)
- Execution Edge (10, including Strategic Mandates, Prioritisation Systems, Execution Culture, Capability Activation, Execution Tracking)

Industries is a second mega-nav with around 25 links and sub-sectors.

**Service page pattern** (Execution Edge): plain problem statement ("Strategy sets the direction. Execution decides whether it creates value"), "Our Execution expertise" (how they work: embedded, senior-led, AI-enabled), "Real results", ten capability cards, one case study, contact with office list. This is the strategy-to-execution pitch MGA makes for Activation Services and Growth Office, written by a peer.

**Best in class**: Labels are mostly plain and searched ("Customer Experience", "Target Operating Model", "Data Strategy"). The Execution Edge page puts the "why" first, then "how we are different", then proof, then the list. A coined family name (Execution Edge) is explained in the first sentence of its page.

**Avoid**: Sixty links in one panel, plus a second panel of twenty-five. Sector-led first item. Investor relations in the primary nav. Ten near-synonymous sub-capabilities under one family (Execution Edge) dilute the offer.

### 2.6 Baringa

**Primary nav**: Insights, Industries, Capabilities, People, Impact, About, Careers, plus a Contact button.

**Services grouping**: Capabilities is a flat alphabetical list of 18 (Artificial Intelligence, CFO Advisory, Cloud and Platforms, Customer and Digital, Data and AI, Digital Risk and Cyber Security, Digital Strategy and Business Models, Enterprise Value Creation, Operational Excellence, Organisational Transformation, Procurement, Policy Regulation and Economics, Strategy, Supply Chain, Sustainability, Talent and Culture, Technology, Transaction Advisory, Transformation). Industries has around 25 links with sub-sectors. Insights is a mega-nav of around 30 featured topics.

**Capability page pattern** (Customer and Digital): H1 promise, one paragraph, three named sub-offers with a sentence each (Customer-led growth and value creation; Customer experience innovation, design and delivery; Customer service reimagined), one case study, one partner quote, an insights strip, then **seven named partners with photos**, then a contact prompt. People are on the offer page.

**Method vs offers vs industries vs themes**: Industries and Capabilities are equal peers in the header. Themes appear as Insights hubs ("Architecting Loyalty in Financial Services"). Method is not a section. "Impact" holds client stories and awards.

**Best in class**: Named people on the capability page. Proof (case, quote) directly under the offer. "CFO Advisory" as a plain label for a senior-advisor offer validates "CEO Advisory" as a label.

**Avoid**: Eighteen flat capabilities with no grouping. Insights mega-nav of thirty items. Sector-led IA.

### 2.7 Ellipsis

**Primary nav**: Customer Science, Loyalty Consulting (with Diagnose, Design, Implement, Operate, Optimise), Customer Analytics (Insights, Reporting, Forecasting), News & Insights, About Us, Careers, Contact. Plus a ventures link.

**Services grouping**: The services dropdown is the engagement journey, not a list of offers: five stages from Diagnose to Optimise. Data products sit in their own dropdown. Home repeats the journey and shows three offer groups (Strategy & Design, Implementation & Launch, Performance Acceleration).

**Method vs offers vs industries vs themes**: Method is the first nav item (Customer Science, a registered mark). No industries. The one expertise theme (loyalty) is the whole company.

**Best in class**: A named method with its own page, one click from anywhere. Trademarked outcome language ("Return On Loyalty") used consistently. Plain stage names.

**Avoid**: Journey stages as the services menu. It works for a single-offer specialist but it conflates method with offer, which is Source A's central complaint about MGA's old site. Registered-mark symbols in nav labels.

### 2.8 Ekimetrics

**Primary nav**: Eki.Decisions (product), Solutions, Industries, About, Resources (News & Insights, Events, Podcasts), Careers (Join, Life at Eki).

**Services grouping**: Solutions is seven outcome-led offers, one level deep: Marketing Effectiveness, Profitable Sustainable Growth, Campaign Optimization, Customer Value Orchestration, Revenue Growth Management, Commercial Excellence, Sustainability. Industries is six.

**Method vs offers vs industries vs themes**: Product first (Eki.Decisions), then solutions, then industries. A lab (Eki.Lab) sits under About. Proof is numeric and above the fold on Home (+5-10% revenue, x10 speed to deployment, +2-5pt margin, $10B gains).

**Best in class**: Seven solutions, one level, no sub-menus. Quantified proof on Home. A named lab under About rather than in the primary nav.

**Avoid**: Solution names that need decoding ("Customer Value Orchestration", "Commercial Excellence"). Awards wall on Home. Industry menu for a firm of this size.

### 2.9 Elsewhen

**Primary nav**: Case studies, Services, Reports, Blog, About, Careers, Contact, plus a "Get started" button.

**Services grouping**: One Services page with four groups, each with six bullets and **three case study cards directly beneath**: AI Strategy, AI Engineering, Cloud Platforms, Product Design & Build (User Research & CX Strategy, UX & Interface Design, Digital Product Development, and so on). Client quotes follow.

**Method vs offers vs industries vs themes**: No industries in the header; industries are tag pages in the footer. No separate method page. Case studies lead the header.

**Best in class**: Proof adjacent to the offer, on the hub: every service group has its own three case cards. Plain, searched sub-labels ("User Research & CX Strategy", "Digital Product Development"). Case studies as the first header item.

**Avoid**: A blog and a reports section as two header items (Source A merges them under Insights). Very long single-page hub.

### 2.10 Mando

**Primary nav**: About, Promotions, Partnerships, Rewards Platform, Work, Insight, Contact.

**Services grouping**: Flat. Three offers as header items, each a page. No dropdowns.

**Method vs offers vs industries vs themes**: None of the three dimensions beyond the offers. Work and Insight as plain sections.

**Best in class**: Nothing to decode. Seven items, seven pages. For a three-offer agency this is right.

**Avoid**: Offers as top-level items does not scale past three or four, and MGA has nine. Domain redirect from the old brand name to a new one without a bridge page.

### 2.11 Pattern references (not peers)

| Site | Header | Services structure | Take | Leave |
|---|---|---|---|---|
| **Deloitte Digital** | Our Work, Insights, What we do, Industries, Who We Are, Careers | What we do is function-led: Advertising, Marketing, Digital Commerce, Sales, Service, Digital Product; plus a Customer Strategy capability | Six plain buyer-function labels, one level | Function-led IA suits a firm that sells to CMOs, CROs and COOs separately; MGA sells to the CEO and growth leader |
| **Bain (Customer Strategy and Marketing)** | Industries (24), Consulting Services (7 top-level), Insights, About | Customer Experience and Sales & Marketing sit alongside Innovation, M&A, Operations, People & Organization | "Customer Experience" as the plain label, not "experience engineering" | 24 industries, 40-plus offices in the header |
| **frog** | Insights, Work, Services, Culture, Make Your Mark, Contact Us | Services hub is problem-led: "Make Bolder Choices", "Build Better Products & Experiences", "Nurture Lasting Relationships", "Master Scalable Operations", with capabilities beneath each | Six header items; Work and Services as siblings; problem-led hub headings with capabilities beneath | Headings are imperatives that hide what is actually sold (Source A's complaint about "growth partner"); very long hub |
| **Lippincott** | About Us, Our Work, Solutions, Ideas | Six one-word solutions (Brand, Growth, Experiences, Marketing, Engagement, Activation), each with a sentence; two named frameworks (Go-to Brands, Brand Aperture) on the same hub | Four header items; named IP presented on the hub as tools, not as nav items | One-word solutions are scannable but vague on their own |
| **Valtech** | Cases, Industries, Partners, Offerings (5), Careers, Insights, About | Five coined offerings (Experience Elevation, Commerce Acceleration, Enterprise Transformation, Marketing Creativity & Performance, Data & AI Revolution) | "Cases" first in the header | Coined offering names; industries in the header |
| **Criticaleye** | Membership types and mentors on Home | Executive Membership, Corporate Membership, NED Membership, Advisory Partnerships, Chair Ready Programme; "over 110 Board Mentors" as the credibility line | A senior advisory offer sells on the people and the model (peer community, mentors, retainer); people are the proof | Membership-tier IA does not fit a consultancy |

---

## 3. Patterns table

What the best of these sites do that v4 does not yet, what v4 already does as well or better, and what to deliberately not copy.

### 3.1 Best-in-class patterns v4 does not yet have

| Pattern | Evidence | v4 today | Carried into v5 as |
|---|---|---|---|
| **Two ways in on the services hub: by problem and by capability**, without a second menu | Prophet (Solutions and Services in one panel; "What is your company's context for growth?" on the service page); Yonder ("Engage through outcome-led solutions or tap into specialist services"); frog (problem-led hub headings) | Hub is pillar-led only. Problem entry exists nowhere except expertise themes | A "Where are you starting from?" block on the Services hub: six plain situations, each pointing at a pillar or service. Three situations at the top of every service page's Why block. No fourth mega-nav column (`v5-refinements.md`, R1, R5) |
| **Proof directly beneath the offer**, not in a separate proof section | Elsewhen (three case cards under each service group on the hub); Baringa (case, quote and partners on the capability page); Prophet (research on the service page); Ekimetrics (numbers above the fold) | Hub has one Proof block of three cases at the foot. Service pages have Proof as block 7 of 13 | One case per pillar section on the hub; Proof moves up to follow What we do on service pages; a numbers line where Source B gives a number (R2, R6) |
| **The named system has a visible home on the hub** | Lippincott (Go-to Brands and Brand Aperture on the Solutions hub); Ellipsis (Customer Science as a page); Prophet (Uncommon Growth Lab); Ekimetrics (Eki.Lab); The Foundation (Our Publications) | "Growth Architecture" is a subheading under an H1 of "What we do"; the word is not in the menu (D-34) | Hub H1 becomes "Our Growth Architecture" with "What we do" as the eyebrow and nav label. Frameworks and tools (Growth Architecture, CIVD, AgentLab, Operating Architecture, Side-by-Side) named once on How we work with links to their homes (R3) |
| **People on the offer page** | Baringa (seven partners on Customer and Digital); The Foundation (team is a first-class section with long biographies and Associates); Criticaleye (mentors are the credibility line) | Service page People block is Editorial; CEO Advisory page surfaces advisors; mega-nav column 3 is a heading and a line | People block becomes Always when a service lead is flagged. CEO Advisory column carries one quiet link, "Our advisors", to the advisor block, so the third pillar shows its substance in the menu (R4, R7) |
| **The pillars' logic is stated in one line** | Elixirr ("Strategy sets the direction. Execution decides whether it creates value"); Prophet ("from strategy to execution"); Simon-Kucher ("unlocking better growth" on every hub) | Three blocks with pillar lines; the strapline in the hero; the relationship between the pillars is not stated | One shared "triangle line" under the three blocks on Home and the hub: "Strategy first. Activation to deliver it. Advisors alongside." (R2) |
| **A coined family name explained in its first sentence** | Elixirr (Execution Edge page opens with the plain problem); Ellipsis (Customer Science defined on Home) | Activation group page explains "Activation"; Experience Engineering and Growth Office have quiet lines in the menu | Activation group page gains a "Which of the six do you need?" list so the operating model, activation and tooling distinction is explicit (R5) |

### 3.2 Where v4 is already at or ahead of the peer set

| Pattern | Peers | v4 |
|---|---|---|
| Five or six header items | Prophet 5, Yonder 6, frog 6, Lippincott 4, Elsewhen 7, Mando 7 | 5 plus a Contact button |
| One mega-nav at most | Prophet 1, Yonder 0, frog 0, Lippincott 0; Elixirr, Simon-Kucher, Baringa 2 to 3 | 1 mega-nav, 1 small dropdown |
| Links in the services panel | Prophet about 25, Elixirr about 60, Baringa 18 flat, Ekimetrics 7 | 13 |
| No sectors in the header | Prophet, Yonder, The Foundation, frog, Lippincott, Elsewhen, Mando, Ellipsis | None in the header |
| "Work" and "Insights" as plain sections | Prophet Work / Thinking; Yonder Work / Thinking; frog Work / Insights; Lippincott Our Work / Ideas; Deloitte Digital Our Work / Insights | Our work / Insights, plain links |
| Testimonials inside case studies | Elsewhen (quotes on hub), Baringa (quote on capability page); Prophet has a separate Testimonials page (the exception) | Inside case studies (Source A) |
| Labels a buyer would search | Simon-Kucher "Customer experience strategy"; Elixirr "Customer Experience", "Target Operating Model"; frog "Customer Research & Insights"; Baringa "CFO Advisory" | Customer Research and Insight, Operating Model Design, AI Agents for Marketing, CEO Advisory |
| Careers out of the primary nav | Prophet (under About), Yonder ("Join"), Lippincott (none) | Under About and in the footer |

### 3.3 What to deliberately not copy

| Anti-pattern | Seen at | Why not |
|---|---|---|
| Sector-led IA or an Industries mega-nav | Simon-Kucher (about 50 links), Elixirr (about 25), Baringa, Bain (24), Valtech, Ekimetrics | Source C: services are sector-agnostic; sectors are proof, not a lead. Every small peer agrees |
| Sixty-link services panel | Elixirr | Fails the two-second test |
| Coined solution names that need decoding | Prophet ("Culture as Catalyst", "AEO Moves"), Valtech ("Experience Elevation"), Ekimetrics ("Customer Value Orchestration"), Yonder ("Unlocking unfair advantage") | Source C and E: plain, searched language. Where a coined name stays (Experience Engineering, Growth Office), the quiet line and the page must carry the plain term |
| Imperative or poetic hub headings that hide the offer | frog, Yonder | Source A: a client must be able to tell within seconds whether you solve their problem |
| Method as the services menu | Ellipsis (Diagnose to Optimise) | Source A: separate method from offer. Method stays on How we work |
| No service pages at all | The Foundation | No canonical landing for capability searches; a credibility-check site, not an origination site (Source C) |
| Separate Testimonials page; Blog and Reports as two header items | Prophet; Elsewhen | Source A merges both into case studies and Insights |
| A hub page that exists only to hold the menu | Prophet's `/what-we-do/` (placeholder copy live) | The Services hub must be a page worth landing on: the Growth Architecture story |
| Investor, awards or office-selector chrome in the header | Elixirr, Simon-Kucher, Ekimetrics, Bain | Irrelevant to a firm of MGA's size |
| Function-led What we do (Advertising, Sales, Service) | Deloitte Digital | MGA sells to the CEO and growth leader, not to functions separately |

---

## 4. What this means for v4

The v4 header and mega-nav are already at the calm end of the peer set: fewer links than any peer with a mega-nav, no sectors, plain labels. The gap to best in class is not in the menu. It is on the pages the menu leads to:

1. The Services hub is a list of pillars, where the best peers give a buyer two ways in (problem and capability), put proof under each offer, and give their named system a visible home.
2. Service pages bury proof and people below the fold.
3. The third mega-nav column is a heading and a line, where a senior advisory offer sells on its people.
4. The relationship between the three pillars (strategy, then activation, with advisors alongside) is drawn but never said.

Each of these has a competitor precedent and a deck reason. `v5-refinements.md` sets out the changes; `andy-deck-coverage.md` shows where each piece of the deck lands.
