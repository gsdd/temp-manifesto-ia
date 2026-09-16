# v5: refinements toward best in class

Gary's feedback on v4 (16 September, Source G): the navigation is calm but **not yet best in class**, and he is not sure Andy's Growth Architecture Services deck is fully reflected. He asked for a review of real competitors' navigation and IA, then refinements.

This document is the record of what v5 changes and why. Each refinement cites its competitor evidence (`competitor-nav-review.md`) and its deck evidence (`andy-deck-coverage.md`). The detailed specifications are in `01-primary-navigation.md`, `02-sitemap.md` and `03-page-layouts.md`; the decisions are logged as D-46 to D-53 in `06-decisions-log.md`.

---

## The finding in one paragraph

The v4 header and mega-nav are already at the calm end of the peer set: 13 links where Prophet has about 25 and Elixirr about 60, no sectors, plain labels, five header items. **The gap to best in class is not in the menu. It is on the pages the menu opens onto.** The best peers give a buyer two ways into services (by problem and by capability), put proof directly beneath each offer, name their system where a buyer can see it, and put people on the offer page. v4 does none of these. And three pieces of the deck have no stated home: the pillar one-liners, the logic that connects the pillars, and the appendix's Growth Strategy terms. v5 fixes the pages and adds one quiet link to the menu. Nothing else in the chrome grows.

---

## What v5 changes

| # | Refinement | Where | Competitor evidence | Deck evidence |
|---|---|---|---|---|
| R1 | Problem entry on the Services hub: "Where are you starting from?" | T2 block 3 | Prophet ("What is your company's context for growth?"), Yonder ("outcome-led solutions or specialist services"), frog (problem-led hub) | Source A: a client must be able to answer "can these people solve my problem?" within seconds |
| R2 | The hub tells the Growth Architecture story: triangle line, one plain sentence per pillar, one case per pillar | T1 block 2, T2 blocks 2, 4, 5, 6 | Elixirr ("Strategy sets the direction. Execution decides whether it creates value"), Elsewhen (cases under each service group), Baringa (case under the offer) | Slide 2 triangle logic; slide 3 one-liners had no home |
| R3 | The named system is visible: hub H1 "Our Growth Architecture"; frameworks and tools named once with links; AgentLab anchored | T2 block 1, T13 block 4, T3 AI Agents module | Lippincott (Go-to Brands, Brand Aperture on the hub), Ellipsis (Customer Science page), Prophet and Ekimetrics (a named lab under About) | Slide 1 title; slide 9 AgentLab; Gary: "Growth Architecture as a named system" |
| R4 | Mega-nav column 3 carries one quiet link, "Our advisors"; panel footer row drops the duplicate Contact link | `01-primary-navigation.md` 3.2 | Baringa (partners on the capability page), Criticaleye (mentors are the credibility line), The Foundation (team as a first-class section) | Slide 4: advisors are the offer; Source C: "showcase advisor profiles, heavyweight" |
| R5 | Activation group page opens with the bridge and adds "Which of the six do you need?" | T3 Activation variant | Elixirr (Execution Edge explained in its first sentence; ten capabilities listed after the why) | Slide 3 Activation one-liner; Gary: operating model vs activation distinction |
| R6 | Service page template: three situations open the Why; Proof follows What we do; a numbers line where the deck gives a number; service modules tightened | T3 | Prophet (three situations), Elsewhen and Baringa (proof under the offer), Ekimetrics (numbers up front) | Slides 7 to 12: "so what", find / redesign / test / scale, 4 and 6 weeks, 3x EBITDA, AgentLab catalogue, interim then embed |
| R7 | People on the offer: People block is Always when a lead is flagged; optional Associates group on the Team listing | T3 block 12, T12 | Baringa, The Foundation (Associates) | Slide 4 "select group of senior leaders"; slide 12 "expert network" |
| R8 | Mock gains a fifth view, Services hub, so the refinements can be judged at a glance | `mocks/index.html` | n/a | n/a |

Nothing else changes. Labels, slugs, weights, the five header items, the About dropdown, the footer, the chip rule, the filters, every URL: all as v4.

---

## R1. Problem entry on the Services hub

**What**: A block on `/services/` headed "Where are you starting from?" with seven plain situations, one line each, each a link to the pillar or service that answers it:

| Situation (proposed wording) | Links to |
|---|---|
| We need to decide where and how to grow | `/services/growth-strategy/` |
| We need a new proposition, loyalty or membership offer | `/services/proposition-innovation/` |
| We need to understand our customers better | `/services/customer-research/` |
| Our journeys or website are not converting | `/services/experience-engineering/` |
| Our strategy is not turning into results | `/services/activation/` |
| We want AI to pay off | `/services/ai-enablement/` |
| I want a sounding board I trust | `/services/ceo-advisory/` |

**Why**: Every best-in-class peer offers a second way in beside the capability list. Prophet puts the "what is your context?" question on each service page; Yonder's hub opens by naming both routes; frog's whole hub is problem-led. v4 had no problem entry at all: the hub listed pillars and the menu listed labels. Source A's test ("can these people solve the particular growth problem that I have?") is answered by exactly this block.

**Why not a fourth mega-nav column**: Source D and F, and the brief. The menu stays the triangle. The situations live one click away, on the page the menu's own label leads to.

**Rules**: seven lines, eight words or fewer each, no descriptors, no icons. Each destination appears once. The wording is a proposal for Andy; the rule to keep is that each line is something a prospect would say, not something MGA would say.

---

## R2. The hub tells the Growth Architecture story

**What**, in four parts:

1. **Triangle line.** One shared line under the three pillar blocks on Home and the hub: **"Strategy first. Activation to deliver it. Advisors alongside."** Eight words. Shared data with the pillar lines.
2. **Pillar sentences.** Each pillar section on the hub opens with one plain sentence derived from its slide 3 one-liner:
   - Growth Strategy: "We work out where the growth is and design the propositions that win it, using our Customer, Innovation, Value and Delivery frame." (links CIVD to its module)
   - Activation Services: "We build the bridge from strategy to results: new operating models and AI-powered, human-led delivery." (links to `/services/activation/`)
   - CEO Advisory: "Experienced growth leaders alongside you, on retainer, to help you make good decisions."
3. **One case per pillar.** Each pillar section ends with one case study line (client and one-line result) tagged to that pillar, curated. The separate Proof block at the foot of the hub is removed; its three cases become these three lines.
4. **Hub blocks stay at eight.** Intro; triangle; Where are you starting from; Growth Strategy; Activation Services; CEO Advisory; Expertise; CTA. v4 also had eight.

**Why**: Slide 2 draws the pillars as one shape; v4 drew three blocks and never said how they relate. Elixirr states its strategy-to-execution logic in one line on the page. The slide 3 one-liners were the one piece of deck copy v4 left without a home ("page content, should get a plain-language pass"). Proof under each offer is the Elsewhen and Baringa pattern; a proof block at the foot is the v4 pattern, and it is the weaker of the two.

**Rules**: the triangle line is the only sentence under the triangle. Pillar sentences are one sentence each. Case lines carry no tags.

---

## R3. The named system is visible

**What**:

- `/services/` H1 becomes **"Our Growth Architecture"**. The eyebrow above it and the nav label stay **"What we do"**. Title tag: "What we do: our Growth Architecture | Manifesto Growth Architects".
- `/about/how-we-work/` block 4, "Frameworks and tools", names each piece of IP once and links to its home: Growth Architecture (`/services/`), Customer, Innovation, Value and Delivery (`/services/growth-strategy/#civd`), Adaptive operating model, our Operating Architecture framework (`/services/operating-model-design/#operating-architecture`), AgentLab (`/services/ai-agents-for-marketing/#agentlab`), Side-by-Side (`/services/ceo-advisory/`). v4 said "named frameworks (for example CIVD, the adaptive operating model)"; v5 makes the list explicit.
- AgentLab's module on the AI Agents for Marketing page gets the anchor `#agentlab`, the CIVD module `#civd`, and the Operating Architecture figure `#operating-architecture`, so each named thing has a linkable address without a page.

**Why**: Gary named "Growth Architecture as a named system" as a worry. v4 had it as a subheading under "What we do" and cut it from the menu (D-34, which stands). Lippincott presents its named frameworks on the Solutions hub; Ellipsis gives its method a page; Prophet and Ekimetrics give their labs a page under About. None puts the named system in the primary nav. The calm version for MGA is an H1 on the hub and an explicit list on How we work.

**Why not rename the nav label to "Growth Architecture"**: Source A and E. "What we do" is plain and is what Prophet, Yonder and Deloitte Digital use. The searched word is in the URL. The named system is one click away, as the first thing on the page.

---

## R4. Mega-nav column 3 gets one quiet link; the footer row loses one

**What**:

- Under the CEO Advisory heading and pillar line, one item in the same quiet type: **"Our advisors"**, linking to `/services/ceo-advisory/#advisors`, the advisor profile block that is the heart of that page.
- The panel footer row becomes **All services, Expertise**. "Contact" is cut: the Contact button sits in the header directly above the panel, so the link duplicated a control forty pixels away. No peer repeats Contact inside its services panel.
- The panel stays at **50 words** (v4: 49; minus "Contact", plus "Our advisors"). The v4 rule "under fifty" becomes "fifty or fewer".

**Why**: The v4 third column was a heading and a line. It read as an afterthought in a three-column grid, which is the opposite of what Source D asked for ("visible as a pillar"). A senior advisory offer sells on its people: Criticaleye leads with "over 110 Board Mentors"; Baringa puts seven partners on its capability page; The Foundation makes its team a first-class section with Associates. Andy's own words (Source C) were "showcase advisor profiles, heavyweight". One quiet link to those profiles gives the column its substance without promoting the pillar.

**Why this is not a reversal of D-36**: D-36 cut "Meet the advisors" because it pointed at `/about/team/#advisors` and "About covers it". v5's link points at the offer page itself, where the advisors are the main block, and is justified by new evidence (Part A) rather than by the About dropdown. D-36's other cuts (the duplicate Growth Strategy item, the Side-by-Side item) stand.

**Fallback**: if Gary prefers the bare column, remove the item and restore "Contact" to the footer row. The panel returns to v4 exactly.

**Mobile**: the flat list under the CEO Advisory small label gains the same single item; the thin row under the list stays All services, Expertise (it never had Contact).

---

## R5. The Activation group page explains the bridge and the six

**What**: `/services/activation/` (T3 variant) opens with the bridge in one line, in plain words ("A brilliant strategy only counts if it gets executed and the value shows up. Activation is how we get you there: hands-on, AI-powered, human-led, and not ongoing operations."), then a block headed **"Which of the six do you need?"** with one line per service:

| Service | One line (proposed) |
|---|---|
| Customer Research and Insight | You need to understand customers faster and agree one version of the truth |
| Experience Engineering | A journey, product or website is underperforming and you want it found, fixed, tested and scaled |
| AI Agents for Marketing | Your customer data is holding marketing back and you want agents doing the work |
| Operating Model Design | You need to redesign how teams, data and AI agents work together |
| Growth Office | You need an interim team to get the strategy delivered and the value tracked |
| AI Enablement | You want your people to use AI well and to find where it pays off |

Then the six service cards as v4, and the standard blocks from Proof onward.

**Why**: Gary's worry about the operating model versus activation distinction. In v4 the distinction was an internal ruling in `04-canonicals-and-seo.md` (Operating Model Design designs, Growth Office staffs, AI Agents supplies the agents) and was never said to a visitor. Elixirr's Execution Edge page is the peer example: the coined family name is explained in its first sentence, then the capabilities are listed with a line each. The deck's Growth Office "Why" ("a brilliant strategy only counts if it gets executed and the value shows up") is the plainest bridge sentence Andy has written; it belongs here.

---

## R6. Service page template: proof up, situations first, modules tightened

**What**, in the T3 template:

1. **Three situations open the Why block.** The Why block (block 3) begins with three one-line situations that lead clients to this service, then the two to four paragraphs from Source B. Prophet's pattern.
2. **Proof follows What we do.** Proof moves from block 7 to block 5, directly after What we do and before How it works. Elsewhen and Baringa put proof under the offer; v4 put it after How it works and the service module.
3. **A numbers line where the deck gives a number.** Conditional block under the hero: Experience Engineering "Over 3x EBITDA return on investment, consistently"; AI Agents for Marketing "4 weeks to audit, 6 weeks to first agents"; nothing invented for the others. Ekimetrics' pattern, applied only where Source B supplies the figure.
4. **Service modules tightened** so each slide's structure has a stated home:

| Service | v5 module change |
|---|---|
| Growth Strategy | Candidate H2s for the What we do block from the appendix's Growth Strategy layer: North Star; Growth priorities; Demand signals; Scenario planning. Pending Andy's copy. CIVD module anchored `#civd` |
| Customer Research and Insight | Why block hook is the deck's "So What": the problem is multiple versions of the truth; the promise is getting to the so-what faster. Body copy, not nav |
| Experience Engineering | How it works block is the deck's four phases: Find, Redesign, Test, Scale. "Squad" allowed in body copy once glossed |
| AI Agents for Marketing | Hero line requirement gains "guided by experts". AgentLab H2 anchored `#agentlab`; the four groups and twelve named agents listed in the spec as catalogue entries (not pages) |
| Operating Model Design | Figure anchored `#operating-architecture`; caption cross-links Orchestration (Culture, Value, Capability) to Growth Office |
| Growth Office | How it works block is two phases: interim activation support, then establishing the new ways of working |
| AI Enablement | "Expert network" in What we do body copy; links to the optional Associates group if published |
| CEO Advisory | Advisor block anchored `#advisors`; quieter CTA unchanged |

**Why**: Slides 7 to 12 each have a Why, a What and a structure (phases, timeline, catalogue, three elements). v4 placed the Why and What and named the structures loosely ("typical phases", "agents are entries"). v5 names each structure so content and CMS build the same thing. None of this adds chrome: it is block content on pages that already exist.

---

## R7. People on the offer

**What**:

- T3 People block (now block 12) changes from Editorial to **Always when at least one team profile is flagged as lead for this service**; up to three profiles.
- T12 Team listing gains an optional group, **"Associates and expert network"**, Conditional on at least one profile flagged as associate. Used for the AI Enablement expert network (slide 12) and any Side-by-Side advisor who is an associate rather than staff.
- The Team listing intro may use "Our Growth Architects" once (slide 10's term for MGA's people). Optional.

**Why**: Baringa puts seven named partners on its capability page; The Foundation lists Associates on its team page and gives every person a long biography; Criticaleye's whole proposition is its mentors. Source C: the site today is a post-referral credibility check; people are what referred visitors check. Making People conditional on a flag rather than editorial choice means every service that has a lead shows one.

---

## R8. Mock: a fifth view

`mocks/index.html` gains a **Services hub** view showing T2 as v5 specifies it: eyebrow, H1 "Our Growth Architecture", strapline, triangle with the triangle line, "Where are you starting from?", three pillar sections with sentence, cards and one case line, the expertise sentence, CTA. The Navigation view shows the column 3 item and the two-link footer row. The Homepage view shows the triangle line. Mobile mirrors the menu. Still greyscale, still no chrome that explains itself.

---

## Nav labels: checked against competitors, unchanged

Part A gives the first outside evidence on the v3 labels. Verdicts, with the reasoning in `nav-wording-decisions.md`:

| Label | Competitor usage | Verdict |
|---|---|---|
| Customer Research and Insight | frog "Customer Research & Insights"; Elixirr "Research & Insights", "Customer Understanding" | Confirmed |
| Operating Model Design | Elixirr "Target Operating Model", "Business & Operating Models" | Confirmed |
| AI Agents for Marketing | Prophet "Agentic Deployment", "AI-Driven Marketing Modernization"; Elixirr "AI Consulting" | Confirmed; ours is the plainest |
| CEO Advisory | Baringa "CFO Advisory"; Elixirr "Define C-Suite Agenda" | Confirmed by the parallel |
| Growth Strategy | Prophet "Growth Strategy" | Confirmed |
| Experience Engineering | No peer uses it. Bain, Elixirr, Baringa, Simon-Kucher all say "Customer Experience"; Elixirr "Digital Design & Build" | **Flag for Andy.** The deck argues to keep it (it is the Dayinsure and Key Group model he wants to be known for); competitors argue for "Customer Experience and Digital". v5 keeps the label and the quiet line and does not decide this |
| Growth Office | No peer uses it. Elixirr coined "Execution Edge" for the same space, with "Transformation Management" as its plain sibling | **Flag for Andy.** Same treatment: kept with the quiet line "Interim growth team" |
| Proposition Innovation | The Foundation tags case studies "Proposition Development"; Simon-Kucher "value proposition design" | Confirmed; "proposition" is the UK term |
| What we do / Our work / Insights | Prophet, Yonder, Deloitte Digital "What we do"; Prophet, Yonder, frog, Mando "Work"; frog, Baringa "Insights", Prophet and Yonder "Thinking" | Confirmed |

---

## Old to new, structural changes only

| v4 | v5 |
|---|---|
| Mega-nav column 3: heading and pillar line | Heading, pillar line, one quiet item "Our advisors" |
| Panel footer row: All services, Expertise, Contact | All services, Expertise |
| Panel word budget: under fifty (49) | Fifty or fewer (50) |
| Services hub H1 "What we do", subheading "Our Growth Architecture" | Eyebrow "What we do", H1 "Our Growth Architecture" |
| Hub blocks: intro, triangle, three pillars (heading, line, cards), Proof, Expertise, CTA | Intro, triangle with triangle line, Where are you starting from, three pillars (sentence, cards, one case line), Expertise, CTA |
| Home triangle: three blocks | Three blocks and the triangle line |
| Service page: Why, What, How, module, Proof (block 7) | Why (three situations first), What, Proof (block 5), How, module; numbers line where the deck gives one |
| Activation group page: "What Activation means here", six cards | Bridge line, "Which of the six do you need?", six cards |
| How we work block 4: "named frameworks (for example CIVD...)" | Explicit list of five with links to anchored homes |
| People block: Editorial | Always when a lead is flagged |
| Team listing: Leadership, Consultants, Advisors | Plus optional Associates and expert network |
| Mock: four views | Five views (Services hub added) |

Nothing changed: the five header items; the About dropdown; the seven service labels and slugs; every URL; every weight; the chip rule; the filters; the footer; the sitemap count (40 fixed pages).

---

## Tests v5 has to pass

1. Open the Navigation view. Name the three pillars in two seconds. The third column now has something under its line, and it is one link, in quiet type.
2. Count the words in the open panel: fifty or fewer.
3. Open the Services hub view. Without scrolling past the first screen, see the name of the system and the three pillars. In the next screen, find your own situation in seven lines.
4. On any pillar section of the hub, find a client and a result without leaving the section.
5. Open the Homepage view. One new line under the triangle. Nothing else changed.
6. Check `andy-deck-coverage.md`: no row is Missing after v5.

---

## What this does not do

- Does not add a column, a heading line, subtitles or theme names to the mega-nav.
- Does not rename any service. Two labels are flagged for Andy with competitor evidence; the decision is his.
- Does not add or remove a URL. Anchors are added on three service pages.
- Does not return to v3's density anywhere: the hub gains one block and loses one; service pages reorder blocks and add one conditional line.
- Does not invent an offer. Every situation line and every "which of the six" line maps to a service Andy has defined.
- Does not create a Google Doc.
