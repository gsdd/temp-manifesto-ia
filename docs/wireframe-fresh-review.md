# Wireframe fresh review: Manifesto Growth Architects IA mocks

Independent second-opinion pass on the clickable IA wireframe at https://temp-manifesto-ia.pages.dev/ and the package in this repository. Written for Gary Duncan. Review first; no redesign. The only mock change in this pass is a new wireframe tool page, `mocks/modules-taxonomy.html`, which puts the taxonomy in section 5 next to live examples of each unit.

**How this was done**

- Crawled every page in the live sitemap (46 HTML files) at 1480 x 900 desktop and 390 x 844 mobile, with the mega-nav, About and Our thinking menus open. Full-page screenshots of 34 pages plus menu states.
- Checked that the live site is the repository: every one of the 46 files at temp-manifesto-ia.pages.dev is byte-identical to `mocks/` on `main` at commit `cb76246`. Re-ran `python3 mocks/_build.py` on `main`: no diff. What you see live is what the repo builds.
- Counted units by class on every page (links, `.btn`, cards, tags, filters, boxes, forms) to score the taxonomy rather than guess.
- Read the IA docs (`README.md`, `docs/00-sources.md` to `06-decisions-log.md`, `client-report-andy.md`, `andy-deck-coverage.md`, `mural-gap-check.md`, `strand-gap-check.md`, `thinking-placement.md`, `v5-refinements.md`).
- Went back to two primary inputs rather than their summaries: the full Otter transcript of the Shed x Manifesto check-in (7 September 2026, 37 min) and Gary's "MGA - Feedback on proposed IA/Sitemap" Google Doc (Source A). Two further Otter recordings were used only to resolve "C and N" (28 April 2025 and 21 August 2025). The services deck itself was not in the shared Drive; the deck audit in `andy-deck-coverage.md` is taken as read.

No em dashes are used in this document.

---

## 1. Executive summary

- **The IA is sound and the live mock matches the repo exactly.** Six-item header, triangle mega-nav readable in two seconds, 46 pages all resolving, breadcrumbs, current-section underline, keyboard access to menus. The structural work is done. The remaining problems are in the units on the page, not the map.
- **Gary's concern is correct and measurable: the wireframe has one visual shape (a bordered box) doing at least six jobs.** Clickable offer cards, non-clickable CIVD cells, non-clickable metric boxes, the hero numbers line, inert filter chips and the empty state all share border, fill or both. A reviewer cannot tell what is clickable by looking. Section 5 gives the taxonomy and section 5.4 scores every unit type against it.
- **Links and buttons are muddy because there are no buttons.** There is not a single `<button>` element in the wireframe. Every `.btn` is an `<a>`: Contact (a page), Send (should submit), Accept cookies (goes to the cookie policy page), Clear filters (goes to /work/), Read on this page (goes to /newsletter/). Filters and pagination are `<span>`s, so the two most important controls on the listing pages do nothing and cannot be told apart from linked tags.
- **The same thing is drawn in two shapes on the same page.** Services hub: Growth Strategy is a large triangle block and then a grey offer card, both to the same URL. Activation page: the six services are a list of lines and then six cards with the identical text. Home: "More work" is a case card with an image placeholder that is really a link to the listing. This is where "cards vs random boxes" comes from.
- **Mobile is missing.** The spec (`01-primary-navigation.md` 3.5) defines a Menu button, a full-screen panel and expand rows. The live wireframe wraps the desktop header onto three lines and the mega-nav opens on hover only. The v4 mock had a Mobile view (D-45); the full-site rebuild dropped it.
- **Against the inputs, the deck is well covered; the call and Gary's IA doc are not.** Under-represented: Andy's request that the front page explain what Growth Architecture is and why it matters; the "heavyweight" Side-by-Side advisor showcase (drawn as the smallest card in the system); the wider community (Colour of Numbers, which the repo still lists as an unknown "C and N"; the Otter transcripts resolve it); Growth Collective, a live subdomain with no link anywhere; sector FAQs, which Gary asked for on the call; and case-study impact numbers on cards.
- **Several spec blocks never made it into the mock.** People and FAQ on service pages (T3 blocks 12 and 13), Team and Related work on case studies (T8), author box and related insights on articles (T10), the client logo wall on About (T11), `?topic=` on every Contact CTA. Appendix A lists them. Either the mock or the spec needs to move.
- **Priority for the next pass:** (P0) one shape per interaction class, real controls, and a named unit set the catalogue defines rather than lists; (P1) mobile view, remove same-page duplicates, promote the advisor and case-card units, close the spec-vs-mock block gaps; (P2) realistic placeholder copy from the deck, contact topic prefill, annotation styling.

---

## 2. What is strong

Keep these. Do not spend the next iteration re-litigating them.

| Strength | Evidence |
|---|---|
| The triangle is readable in two seconds, and CEO Advisory reads as a full pillar without dominating | https://temp-manifesto-ia.pages.dev/ with What we do open: three hub headings in the same ink and weight, grid 1fr / 1.15fr / 0.85fr, every strand with a subtitle. Word count of the open panel is modest against Prophet (about 25 links) and Elixirr (about 60). |
| The header is six items and stays six | Every page: What we do, Our work, Our thinking, About, Careers, Contact button. Footer carries sectors, legal, search, The Nutshell. |
| The Services hub is a story, not a menu on a page | https://temp-manifesto-ia.pages.dev/services/ : H1 Our Growth Architecture, strapline, two deck paragraphs, triangle plus triangle line, seven situation lines, three pillar sections each with a sentence, cards and a case line. This is the best page in the set. |
| Every URL in the sitemap is a real page and every footer link resolves | 46 files; `sitemap.html` lists all with weights; `/catalogue/` linked from every heading map. Cookie bar, 404, search, legal stubs, thank-you all exist. |
| Wayfinding basics are in | Breadcrumbs on every page except Home; `aria-current="page"` and an underline on the active header item on 39 pages; skip link; visible focus ring; ArrowDown opens menus and Escape closes them. |
| The heading map sidebar ties every page to an SEO target | Right-hand panel on every page: URL, H1, primary keyword with UK volume, alts, ordered H2s, H3s, one-line intent. Consolidated in `docs/heading-map.md` and generated from the same source as the HTML, so they cannot drift. |
| The build is honest | `mocks/_build.py` regenerates every page; running it on `main` produces no diff. Live equals repo. |
| Listing pages show filters, pagination and an empty state | https://temp-manifesto-ia.pages.dev/work/ and /insights/ : one filter group open, More filters row, results, pagination, labelled empty state with a clear-filters action. |
| Deliberate departures are logged | D-01 to D-59 record why CEO Advisory is third, why three deck labels were renamed, why sectors are footer-only. A reviewer can trace any choice to a source letter. |

---

## 3. Gaps vs wireframe best practice

What a clickable IA wireframe at this stage should show, and where this one does not. Each row gives what was seen and where.

### 3.1 Interaction honesty

| Gap | What was seen | Where |
|---|---|---|
| No real buttons anywhere | Zero `<button>` elements across 46 pages. All 30 or so `.btn` instances are anchors. | Every page. Counted from the HTML. |
| Buttons that navigate somewhere unrelated to their label | Accept (cookie bar) links to `/cookie-policy/`. Read on this page (report gate) links to `/newsletter/`. Clear filters links to `/work/` or `/insights/` (a reload, which is acceptable, but it is styled the same as Contact). Send links to `/contact/thank-you/` with no fields required. | Cookie bar on every page; https://temp-manifesto-ia.pages.dev/insights/pricing-paradox/ ; /work/ ; /contact/ |
| Filters and pagination are inert text | `.filter` and `.pagination` items are `<span>`s. Nothing happens on click, no hover, no focus. "More filters" looks like a control and is not one. | /work/, /insights/, /catalogue/ |
| Form fields are empty divs | `.field .box` and `.footer-search .box` are `<div>` placeholders. Acceptable for a wireframe, but the Send button beside them is a link, so the whole form reads as decoration. | /contact/, /newsletter/, /search/, /404/, /insights/pricing-paradox/, footer |
| Logo tiles do not show their link rule | Spec T1 block 2: "Logos link to the case study if one exists, otherwise to /work/". Tiles are `<span class="logo-ph">`. MURAL open question 8 (link only where a case exists) cannot be judged from the mock. | Home Trusted partners and Awards; /sectors/*/ Clients; /catalogue/ |

### 3.2 Responsive behaviour

| Gap | What was seen | Where |
|---|---|---|
| No mobile navigation pattern | At 390 px the header wraps to three rows (logo / What we do, Our work / Our thinking, About, Careers / Contact). No Menu button, no panel, no expand rows. The mega-nav still opens on hover, which does not exist on touch. | Any page at 390 px. Spec: `01-primary-navigation.md` 3.5 and D-40. The v4 mock had a Mobile view (D-45). |
| Grid collapse only | Cards and columns stack at 1100 px and 720 px. That is a CSS fallback, not a designed small-screen wireframe. Sidebar working notes drop below the page at 1100 px and read as page content. | `assets/wireframe.css` media queries. |

### 3.3 Module clarity (Gary's lens)

| Gap | What was seen | Where |
|---|---|---|
| One shape, six jobs | Solid 1 px border and/or grey fill is used by: offer card (link), triangle block (link), CIVD cell (not a link), metric box (not a link), hero numbers line (not a link), filter chip (should be a control), page tag (link), empty state (dashed), logo tile (dashed). Card hover underlines the title; nothing else has a hover state, so at rest they are indistinguishable. | Compare /services/ (triangle blocks, offer cards, compact CIVD) with /services/growth-strategy/ (CIVD cells) and /work/dayinsure/ (metrics). |
| Same destination drawn twice on one page | Services hub: Growth Strategy and Proposition Innovation appear as triangle blocks and again as offer cards inside the pillar section. Activation page: "Which of the six do you need?" lines and "The six Activation services" cards carry the identical sentence for each service. | /services/ ; /services/activation/ |
| Card used as a "more" link | Home Our work: third card is "More work / All case studies" with an image placeholder, then an "All work" text link directly beneath it. Two routes to /work/ in one block, one dressed as content. | https://temp-manifesto-ia.pages.dev/ |
| Duplicated content inside a module | Growth Strategy: the CIVD four-cell is followed by four H3s (Customer, Innovation, Value, Delivery) repeating each cell's line. | /services/growth-strategy/ |
| Named structures rendered as page sections instead of one module | Find / Redesign / Test / Scale are four separate `.block` sections with rules between them, at the same level as Proof and Why. Same for Culture / Capability / Value (Growth Office) and North Star / Growth priorities / Demand signals / Scenario planning (Growth Strategy). The spec calls these "How it works" phases and "candidate H2s inside What we do", but the mock flattens them to top-level sections, so the page reads as eleven equal blocks. | /services/experience-engineering/ (11 blocks), /services/growth-strategy/ (11 blocks), /services/growth-office/ |
| Mock and its own heading map disagree on order | Growth Strategy page renders Proof before North Star; the sidebar heading map lists Proof after CIVD. | /services/growth-strategy/ sidebar vs page |
| Related services cards say the same thing everywhere | Every related-service card reads "Often bought alongside". Three cards sit in a two-column grid, leaving an orphan. | /services/growth-strategy/, /services/growth-office/, /services/ai-agents-for-marketing/ |
| No block identifiers on the page | Spec templates number blocks (T3 block 1 to 14). The mock shows no block names or numbers, so a reviewer cannot say "block 8 is wrong" or see which blocks are Conditional and switched off. | Every page. |
| Working-notes chips look like page tags | Sidebar chips (weight, keyword, MURAL notes) use the same bordered-pill shape as on-page tags and filters. D-59 says do not call them chips, but they still look like the live unit. | Every page with a sidebar. |
| Section heading styles vary without a stated rule | Home uses small uppercase eyebrows for every section. Service pages mix eyebrows (Related expertise, Related thinking) with 22 px plain headings (Why this, now). The rule is probably "primary vs related", but nothing says so and the catalogue does not show either. | / vs /services/growth-strategy/ |
| Resting affordance on list links is hover-only | Situations, Related thinking rows, Where we help rows, expertise row-links and mega-nav strands are not underlined until hover. Inline links, "more" links and the secondary CTA are underlined. Two link conventions with no rule. | /services/ situations; /expertise/loyalty/ Where we help; Home Growth problems row |

### 3.4 Content realism

| Gap | What was seen | Where |
|---|---|---|
| Placeholder copy where real copy exists | Every service page: "Two to four short paragraphs on why this matters now." and "What we do in this service, in plain words." The deck supplies a Why and a What for all six Activation services and Side-by-Side (`andy-deck-coverage.md` slides 4, 7 to 12). Showing the deck sentence would let Andy judge fit and let Gary judge length. | /services/*/ |
| Case cards have no impact slot | Every case card is "Client / One-line result". Andy on the call: case studies must "talk about impact" with "good ROI numbers" and a client quote. The card shape has no metric. The featured case on /work/ has a quote but still no number. | / , /work/, service Proof blocks |
| Uneven page depth | Values and culture, the role page and the advisor profile are three or four lines with one link each. The role page says "Form or email" but shows no form, while Contact and the report gate show fields. Team listing is the only content page without a closing CTA. | /about/values/, /careers/growth-architect/, /about/team/ |
| Contact prefill not shown | Spec T3: primary CTA is `/contact/?topic={service}`. Zero occurrences of `topic=` in the mock. The Contact form has a Topic field with no indication it is prefilled. | Every service page CTA; /contact/ |
| Home hero media dominates the first screen | At 1480 x 900 the 16:9 Showreel placeholder fills about 60 percent of the viewport and Trusted partners sits on the fold line. MURAL asked for the partner banner "up". | https://temp-manifesto-ia.pages.dev/ |

### 3.5 Spec vs mock

Appendix A lists template blocks in `03-page-layouts.md` that are absent from the corresponding mock page. Eleven blocks across six templates. This is the "what ships vs what the repo claims" list.

---

## 4. Gaps vs input documentation

Items from the source inputs that are missing or under-represented on the live wireframe. Each row quotes or cites the source, then says what the mock shows.

### 4.1 Otter, Shed x Manifesto check-in, 7 September 2026 (Source C, full transcript)

| Input | Source quote | What the mock shows | Verdict |
|---|---|---|---|
| Home must explain Growth Architecture | Andy, 0:24:18: "fundamentally the front page of the single manifesto is this pioneers and growth architecture. What is growth architecture? Why is it important as the sort of entry point." | Home hero has the positioning line and strapline. The only Growth Architecture content is the triangle line ("Strategy first. Activation to deliver it. Advisors alongside.") and a text link to the hub. No unit on Home says what Growth Architecture is or why it matters. | Under-represented |
| Showcase the Side-by-Side advisors as heavyweight people | Andy, 0:09:59 block: "we need to showcase the people that are part of that side by side community ... quite an illustrious bunch". 0:36:55: "the profiles of these side by side advisors are going to be a good [asset] because they're all pretty heavyweight folks ... industry luminaries". | Advisor unit is the person card: 40 px circle, name, "Former role, one line". It is the smallest card in the system, smaller than a case card, and is the main proof block on /services/ceo-advisory/. | Under-weighted |
| The wider community, not just the core team | Andy, 0:29:09 block: "we need to refresh how we're positioning all of the colour and numbers folks and the sort of growth collective folks ... we do want to showcase that broader community, not just the our core team members." | /about/team/ has one prose line under "Associates, expert network and C and N members" and no cards. /about/ has an H3 "C and N members: A named group." The repo lists C and N as unresolved (`client-report-andy.md` section 8, `mural-gap-check.md` Q1). | Under-represented, and the open question is answerable (see 4.4) |
| Case studies must show impact and testimonials | Andy, 0:29:09 block: "they talk about impact and we have a lot more client testimonials ... being able to point at the growth we've delivered ... clients saying we're great rather than us saying we're great". Target "12 to 15" cases. | Case card: image, client, "One-line result". No metric on the card. Case page has an At a glance metric row (all TBC) and a quote. Work hub featured card has a quote, no number. | Partial |
| Sector landing content | Gary, 0:23:37: "even if it is a page with some simple landing copy, some FAQs, the reports, and then the case studies". | /sectors/financial-services/: hero copy, client logos, two case cards, three services, related thinking. No FAQ unit anywhere in the wireframe (also absent from spec T6). | Missing |
| Growth Office is the orchestration layer | Andy, 0:09:59 block: "the modern version of a PMO or a transformation programme office ... providing that orchestration layer ... culture, value tracking, and then coordinating the standing up of new capabilities". | /services/growth-office/ hero: "Interim growth team and programme office that gets strategy delivered". Culture / Capability / Value present. "Orchestration" appears only in the Operating Model figure caption. | Present |
| Experience Engineering is the web-build route | Andy, 0:07:54 block: "how we want to talk about how we partner with you guys to do the digital experiences web build type stuff ... that would specifically talk to the Dayinsure type work". Gary, 0:17:42: "can you build a website? So yes, we can. That fits inside the experience engineering." | Subtitle "Customer experience and websites"; H2 "Website and digital product"; hero line names website. Dayinsure and Key Group as proof. | Present. Whether to name delivery partners is Andy's call. |
| Five-to-six-word subtitles in the menu | Gary, 0:19:27: "contextualise these headings with a five six word subtitle". | Every strand has one (D-58). | Present |
| CEO Advisory quieter, possibly outside the main menu | Gary, 0:36:35: "there's even a choice as to whether you put it in the sort of main navigation or not ... this advisory thing sits on its own somewhere". Andy: "we just shouldn't design the site around it". | Full-weight third column (D-57, from client review). Documented decision, not a gap. Flagged so Gary sees the mock went the other way from his own remark on the call. | Decision, logged |

### 4.2 Gary's "MGA - Feedback on proposed IA/Sitemap" (Source A, Google Doc)

| Input | Source text | What the mock shows | Verdict |
|---|---|---|---|
| Service page surfaces sectors and methodology | Cross-linking table: "Service / Capability: Relevant expertise themes, sectors, case studies, insights, methodology". | Service pages: Related expertise tags, Proof cards, Related thinking, Related services, one inline link to Our approach under How it works. Sectors not shown (cut by D-42 on Gary's later v4 feedback). | Sectors: deliberate cut, Gary's own. Methodology: present but as one inline link, easy to miss. |
| DEI has one home | Suggested IA: About > Who We Are / Story, Team, Values / Culture, DEI. Principle: "one canonical page for each important proposition/topic". | "Diversity, equity and inclusion" is an H2 on both /about/values/ and /careers/. Two homes for one topic. | Contradicts the one-home principle |
| What We Do is a grouping, not a route | "what we do would not be clickable and will not be a route e.g. /what-we-do" | The label links to /services/ (D-51). Logged decision. Fine, but note the departure. | Decision, logged |
| Sectors as a canonical hub | "Sectors (canonical hub: where we have market expertise)" | No /sectors/ index (D-44). Footer heading "Who we work with" is plain text. | Decision, logged (Gary's v4 feedback overrides) |
| Insights hub with a Latest section | "insights as the hub page, with a latest section" | /insights/ opens with Reports (one card) then Articles. No "Latest" unit. Spec T9 block 2 says "Latest: one curated or newest insight, large, plus the next three". | Missing vs both Source A and spec |

### 4.3 Andy's Growth Architecture Services deck (Source B, via `andy-deck-coverage.md`)

The coverage audit marks 55 Present, 16 Partial resolved by v5, 1 Missing resolved. Checking the wireframe against the audit's "where v5 puts it" column:

| Deck element | Audit says | Mock shows | Verdict |
|---|---|---|---|
| Why and What copy per service (slides 4, 7 to 12) | "T3 Why, from Source B"; "T3 What we do" | Placeholders: "Two to four short paragraphs", "in plain words". The situation lines are new writing; the deck's own Why sentences are not used even as placeholder. | Structurally present, content not shown |
| Twelve named AgentLab agents | "Listed in the T3 module spec" | /services/ai-agents-for-marketing/ AgentLab block: four groups with a few agent names each in one line. Present. | Present |
| Experience Engineering squads | "Body copy in What we do" | Not visible (What we do is a stub). | Not shown |
| "Growth Architects" as the team's name | "Optional ... Team listing intro" | Not used. | Optional, not used |
| Operating Architecture appendix figure | "Captioned figure" | /services/operating-model-design/ has the four qualities and an H2 "Our Operating Architecture framework" followed by three prose H3s (data and tools, new work units, orchestration). No figure or media slot. | Partial: no figure slot |
| 3x EBITDA and 4 / 6 week numbers | "Numbers line" | Present on Experience Engineering and AI Agents heroes. | Present |

### 4.4 Resolving "C and N" and Growth Collective from the recordings

The repo leaves both as open questions. The Otter archive answers the first and gives context for the second.

- **C and N is Colour of Numbers.** Otter, 7 September 2026, 0:03:35 block: "we might get Dave Henry from Colour of Numbers, who we slotted in in a permanent role with him at Trojan". Same call, 0:29:09 block: "positioning all of the colour and numbers folks and the sort of growth collective folks". Otter, "Digital Activation Services: Neat / Manifesto", 28 April 2025: action items to "Get the profiles for the wave 2 CNN community members uploaded" and "Evolve the color-numbers.com external site to better reflect the community and what Manifesto now does". So C and N is the Colour of Numbers practitioner community with member profiles on a platform. The wireframe should reserve a person-card group for it on /about/team/ and stop calling it "a named group". Andy to confirm the public label.
- **Growth Collective is a live subdomain that Manifesto wanted linked from the main nav.** Otter, "Manifesto <=> Shed catchup", 21 August 2025, 0:04:31, Sarah Ashdown: "we definitely want to be able to have a tab on the manifesto page that says the collective because we want to help drive traffic to the page." Michaela: it "will link out ... to growth collective.manifestogrowth.com". Otter, "Manifesto Growth Collective Update", 11 May 2026: the collective is active with governance and offer proposals. The wireframe has no link to it anywhere, header or footer. Gary's instruction stands that it is not a seventh header item; a footer Company-column link is the minimum that honours Sarah's request and costs nothing in the chrome.

### 4.5 MURAL and old IA columns (via `mural-gap-check.md`, `strand-gap-check.md`)

| Input | What the mock shows | Verdict |
|---|---|---|
| "Trusted partners banner up" | Present as block 2, but below a full-height showreel placeholder; on the fold at 1480 x 900. | Present, position weakened by the media slot |
| "Case studies pulled up; tagging; video snippets" | Work hub featured plus filters; case page has 16:9 film slot. | Present |
| "Meet the team; culture over headshots" | Team listing is a grid of headshot cards. No culture unit. Careers has "Pioneers / recent joiners" portraits. | Partial |
| "Growth partner videos; move video to Our approach" | Present on /about/how-we-work/. | Present |
| "Keep CIVD, different visuals" | Four-cell grid on Growth Strategy and hub. Cells look like offer cards. | Present, shape muddled (see 3.3) |
| Trusted partner logos link only where a case exists | Logos are inert spans; cannot be judged. | Not shown |
| Source F: "Cut redundant items (the duplicate Growth Strategy heading and item)" | D-36 cut it. D-54 then added an Overview row under Growth Strategy and Activation that links to the same URL as the hub heading two lines above it. Two adjacent links to one page per column. | Reintroduced. Gary to confirm he wants it (D-54 rationale is that the heading did not look clickable; the arrow now does that job). |

---

## 5. Module and component taxonomy recommendation

The wireframe needs a small, closed set of unit types, each with one shape and one behaviour. A unit is defined by four questions, answered in order. If two unit types give the same answers they are the same unit and must look the same; if they give different answers they must look different.

### 5.1 The four questions

1. **Does the whole unit go somewhere when clicked?** Yes: it is a Link unit or a Card. No: continue.
2. **Does it do something on this page (submit, filter, toggle, page, accept)?** Yes: it is a Control. No: continue.
3. **Is it framed content that stands on its own (a number, a quote, a figure, a placeholder)?** Yes: it is a Display unit. No: it is Text.
4. **If it goes somewhere: is it a title plus one supporting line plus an optional media slot, in a frame?** Yes: Card. No: Link.

Buttons are a Control that also covers exactly one case of navigation: the primary call to action on a screen (Contact / Arrange a conversation / Work for us). Nothing else that navigates may look like a button.

### 5.2 Unit types

| Class | Unit | Use it when | Wireframe shape | Interaction | Never |
|---|---|---|---|---|---|
| **Link** | Nav link | Header, footer, mega-nav strands, dropdown rows | Plain text; bold in the header; strand plus grey subtitle in the mega-nav | Goes to a page or anchor. Hover underline. | Boxed |
| Link | Hub link | Mega-nav column heading, hub H3 on the Services hub | Heading text with a trailing arrow and a rule beneath | Goes to the hub page | Repeated as a child row to the same URL |
| Link | Inline link | Inside a sentence (pillar sentence, case line, How it works) | Underlined, same colour as the text | Goes to a page | Grey without underline |
| Link | Row link | List of destinations with an optional meta value: Related thinking, Where we help, Services most used here, situation lines | Full-width row, thin rule above, title left, meta right in grey; whole row clickable; arrow or underline on hover, and the title underlined at rest | Goes to a page | Boxed; mixed with non-clickable rows in the same list |
| Link | More link | End of a block: All work, All thinking, Our advisors | Small underlined grey text, right after the list or grid | Goes to a listing | Dressed as a card |
| Link | Tag | Related expertise on a service page, services on a case hero, theme on an insight hero. One dimension, three visible. | Small pill, thin border, underlined text | Goes to the theme or service page | Used as a filter; used as a sidebar note |
| **Card** | Offer card | A service or pillar as a destination: hub pillar sections, Related services, Expertise hub, Activation six | Framed, grey fill, title plus one line, no media. Whole card clickable, title underlines on hover. | Goes to one page | Non-clickable copies (CIVD cells) |
| Card | Pillar block | The triangle, drawn once per page | Same as offer card but larger title and white fill, always three in a row | Goes to the pillar page | Appearing twice on one page with offer cards for the same URL |
| Card | Case card | Case study as destination | Framed, image slot 16:10, client, one-line result, one impact figure (bold), optional single service tag on listings | Goes to the case | "More" links dressed as a case card |
| Card | Report card | Report or article as destination | Framed, document slot 3:4 for reports, no media for articles, title, meta line (type, date) | Goes to the item | Doubling as a gate |
| Card | Person card | Leadership, consultants, associates, community | Framed, avatar, name, role | Goes to the profile | Used for advisors (see next) |
| Card | Advisor card | Side-by-Side advisors on CEO Advisory, Team, hub pillar 3 | Larger than a person card: portrait slot 4:5, name, former role and company, one-line focus. Three across. | Goes to the profile | Same size as a consultant card |
| Card | Situation line | "Where are you starting from?" and the three lines opening each service Why | A row link in the visitor's voice, two columns, whole line clickable | Goes to the service | Rendered as boxes |
| **Control** | Primary button | The one primary CTA on a screen: Contact, Arrange a conversation, Work for us; form submit | Solid dark fill, white text | Navigates to Contact or submits | Two on one screen; used for Accept, Clear, Read |
| Control | Secondary button | Actions that stay on the page or are low stakes: Accept cookies, Clear filters, Load more, Apply filters | Outlined, no fill | Does something; page does not change URL | Navigating to an unrelated page |
| Control | Filter chip | Work and Insights listings, More filters | Pill with a leading tick box or a pressed state; visibly different from a Tag (no underline, has a state) | Toggles; updates results and URL query | Inert span; identical to Tag |
| Control | Pagination | Under listings | Numbered squares plus Next, current one filled | Changes page | Inert |
| Control | Field | Forms and search | Label above, box, helper text | Accepts input; submit is a Primary button | A `<div>` beside a link dressed as a button |
| Control | Menu toggle (mobile) | Header below 1024 px | Menu word plus icon, Contact button pinned | Opens a full-screen panel with expand rows | Absent |
| **Display** | Metric | At a glance, numbers line, stats | No border. Large figure over a small grey label, separated by whitespace or a thin rule, never a box | None | Bordered like a card |
| Display | Frame cell (CIVD, four qualities, three elements) | A named framework shown as parts | Four or three cells on a tinted band with no individual borders, each a word plus one line; one caption with an anchor | None, except one caption link to the framework's home | Repeated as H3s beneath; styled as offer cards |
| Display | Process steps | Find / Redesign / Test / Scale; interim then embed; maturity assessment then programmes; 4 weeks then 6 weeks | One horizontal row of numbered steps inside one block titled How it works | None | Four separate page sections |
| Display | Quote | Testimonial inside Work, cases, hub pillar 3 | Left rule, larger italic text, cite line | None | Framed like a card |
| Display | Logo tile | Trusted partners, Awards, sector Clients | Dashed placeholder tile, in a row of eight. If linked, the tile carries the case link and shows a hover state; if not, it is a plain tile | Optional link to a case | Same shape whether linked or not |
| Display | Media slot | Showreel, case film, report cover, portrait | Dashed placeholder with ratio label (16:9, 16:10, 3:4, 4:5) | None in the wireframe | Solid border |
| Display | Empty state | No results, no open roles | Dashed frame, message, one Secondary button | Button clears or routes | Same frame as content |
| Display | Notice bar | Cookie bar | Full-width band above the footer, text plus Secondary button | Accept | Primary button |
| **Text** | Section heading A | A primary content block: Why this, now; What we do; Proof | 22 px plain | None | Eyebrow style |
| Text | Section heading B | A related or utility block: Related expertise, Related thinking, Awards, Our thinking teaser | Small uppercase eyebrow | None | Used for primary blocks |
| Text | Prose | Body copy | 15 px, max 760 px | Inline links only | Boxed |
| **Annotation** | Working note | Sidebar only: weight, keyword, MURAL note | Visibly not a page unit: dotted border, italic, monospace label | None | The Tag pill shape |
| Annotation | Block label | Small grey label at the top-left of every block: "T3.6 Proof (Always)" | Monospace, 11 px, toggled by a single review switch | None | Confused with an eyebrow heading |

### 5.3 Rules that fall out of the table

1. **Solid border means clickable.** Cards and buttons have solid borders. Nothing else does. Display units use whitespace, a tint band, a left rule or a dashed frame.
2. **Dashed means placeholder.** Media, logos, empty states. Never content and never clickable except a linked logo tile, which gets a hover state.
3. **One button style for the primary action, one for everything else.** A screen has at most one primary button in the page body plus the header Contact.
4. **Tags go somewhere; filters change something.** They must not share a shape. Filters carry a state.
5. **A destination appears once per page in one shape.** If the triangle is on the page, the pillar does not also get an offer card. If a service is listed as a line, it is not also a card with the same text.
6. **Named frameworks are Display, not Cards, and are drawn once.** No H3 repeat under the cells.
7. **Process phases are one module.** One block, one heading, one row of steps.
8. **Every list of links looks like a list of links at rest.** Underline or arrow on the title, not only on hover.
9. **Every block carries a label** tying it to the template number and its Always / Conditional / Editorial rule, switchable off for client viewing.
10. **The catalogue defines, it does not only show.** Each unit in `/catalogue/` gets the row from 5.2 beside its example.

### 5.4 Scorecard: live wireframe against the taxonomy

Scored from the HTML and screenshots of all 46 pages. Pass: the rule holds everywhere. Partial: holds in most places with named exceptions. Fail: the rule is not in force.

| # | Rule | Score | Evidence |
|---|---|---|---|
| 1 | Solid border means clickable | **Fail** | `.metric`, `.civd-cell`, `.numbers`, `.filter` all have solid borders and are not clickable. /work/dayinsure/ metrics; /services/growth-strategy/ CIVD; /services/experience-engineering/ numbers line. |
| 2 | Dashed means placeholder | **Pass** | `.logo-ph`, `.video-ph`, `.card .ph`, `.card .doc`, `.avatar`, `.empty-state` are the only dashed units. Consistent. |
| 3 | One primary button style, one secondary | **Fail** | One `.btn` style is used for Contact, Send, Accept, Clear filters, Read on this page, Search, Browse services, Work for us. No `<button>` element exists. |
| 4 | Tags and filters look different | **Fail** | `.page-tags a` and `.filter` are the same pill; filters are `<span>`s. /work/ and /insights/ vs /services/growth-strategy/ Related expertise. |
| 5 | A destination appears once per page in one shape | **Fail** | /services/ (pillar block plus offer card for Growth Strategy and Proposition Innovation); /services/activation/ (line plus card, same text, six times); / (More work card plus All work link). |
| 6 | Frameworks drawn once, as Display | **Partial** | CIVD is a grid, but styled as offer cards and repeated as four H3s on /services/growth-strategy/. Operating Architecture has no figure slot. |
| 7 | Process phases are one module | **Fail** | Find / Redesign / Test / Scale are four `.block` sections on /services/experience-engineering/. Culture / Capability / Value likewise on /services/growth-office/. |
| 8 | Link lists have resting affordance | **Partial** | Inline links, More links and secondary CTA are underlined. Situations, Related thinking rows, Where we help, row-links, mega-nav strands underline on hover only. |
| 9 | Every block is labelled | **Fail** | No block labels anywhere. Only the empty state and search results carry a `wf-label`. |
| 10 | The catalogue defines each unit | **Fail** | /catalogue/ lists examples under headings (Cards, Proof and media, Forms) with no definition, use rule or interaction note. It also uses names that differ from the spec ("Stats" vs "At a glance" / "Numbers line"). |

Two passes, two partials, six fails. That is the measured version of "modules are not clear, links vs buttons are muddy, cards vs random boxes".

### 5.5 Mapping today's classes to the taxonomy

For whoever edits `mocks/_build.py` and `assets/wireframe.css`. No new URLs; no IA change.

| Today | Becomes | Change |
|---|---|---|
| `a.btn` for Contact, Arrange a conversation, Work for us | Primary button | Solid fill. Keep as `<a>` (it navigates). |
| `a.btn` for Send, Search | Primary button, `<button type="submit">` inside a `<form>` | Element change; wireframe can still route to thank-you on submit. |
| `a.btn` for Accept, Clear filters | Secondary button, `<button>` | Outlined. Accept stays on page. |
| `a.btn` Read on this page | Remove; the report body is on the page. Gate becomes a Field plus Secondary button "Email me a copy" | Fix wrong destination (/newsletter/). |
| `span.filter` | Filter chip, `<button aria-pressed>` | Add tick box or pressed fill; drop underline. |
| `span` pagination | Pagination, `<a>` or `<button>` | |
| `.metric`, `.numbers` | Metric | Remove border; figure over label. |
| `.civd-cell` | Frame cell | Tint band, no per-cell border; delete the H3 repeat. |
| Find / Redesign / Test / Scale blocks; Culture / Capability / Value; Interim then embed; maturity then programmes | Process steps inside one How it works block | Collapse to one section. |
| `.tri a` on the hub plus `.card.offer` for the same pillar | Keep the pillar block, drop the duplicate offer card in that pillar section, or vice versa | Rule 5. |
| Activation "Which of the six" list plus six cards | Keep the six cards; put the "you need this when" line inside each card as its one supporting line | Rule 5. |
| Home "More work" card | More link | Delete the card; keep "All work". |
| `.card.person` for advisors | Advisor card (new, larger) | New class. |
| Case card `span` "One-line result" | Case card with impact figure | Add a bold figure slot. |
| `.chip` sidebar | Working note | Dotted border, italic. |
| `.situations a`, `.list a`, `.row-links a` | Row link | Underline at rest. |
| New | Block label | Small monospace label per block, one review toggle in the sidebar. |
| New | Menu toggle and mobile panel | Per `01-primary-navigation.md` 3.5. |

---

## 6. Opportunities, prioritised

**P0: fix before the next client review. These prove the taxonomy and remove the confusion Gary named.**

| # | Opportunity | Why | Where |
|---|---|---|---|
| P0-1 | Apply rule 1 and rule 3: solid border only on clickable units; two button styles; real `<button>` elements for Send, Accept, Clear, Search | Removes "random boxes" and "links vs buttons" in one CSS and builder pass | `assets/wireframe.css`; `_build.py` `card()`, `metrics_html()`, `civd_html()`, form and cookie snippets |
| P0-2 | Make filters real controls with a visible state and a different shape from tags | Listing pages are where the IA's three dimensions meet; today the controls are inert and look like tags | /work/, /insights/, /catalogue/ |
| P0-3 | Remove same-page duplicates: hub pillar cards, Activation line plus card, Home More work card, CIVD H3 repeat | Rule 5 and rule 6; every duplicate is a place a reviewer asks "which one is the module?" | /services/, /services/activation/, /, /services/growth-strategy/ |
| P0-4 | Turn the catalogue into a defined taxonomy: one row per unit (use, shape, interaction, never) beside its example, using the spec's block names | Rule 10. `mocks/modules-taxonomy.html` in this PR is the draft; fold it into `/catalogue/` when agreed | /catalogue/ |
| P0-5 | Collapse process phases into one How it works module per service | Rule 7; cuts service pages from 10 or 11 equal blocks to the spec's ordered list | Experience Engineering, Growth Office, AI Enablement, AI Agents, Operating Model Design |

**P1: next iteration.**

| # | Opportunity | Why | Where |
|---|---|---|---|
| P1-1 | Add the mobile view: Menu toggle, full-screen panel, expand rows, pinned Contact | Spec 3.5 exists and the v4 mock had it; a desktop-only IA wireframe cannot be signed off for a site whose senior visitors read on phones | Header on every page, or one representative page at 390 px |
| P1-2 | Block labels with template number and rule, behind one toggle | Lets Gary and Andy review block by block against `03-page-layouts.md` and see which Conditional blocks are off | Every page |
| P1-3 | Advisor card as a distinct, larger unit; use it on CEO Advisory, hub pillar 3 and Team | Andy: "heavyweight folks ... industry luminaries"; today they are the smallest card | /services/ceo-advisory/, /services/, /about/team/ |
| P1-4 | Case card gains an impact figure; Work featured card gains one too | Andy: cases must "talk about impact"; the card is the proof unit the whole IA leans on | Home, /work/, service Proof blocks, theme and sector pages |
| P1-5 | Close the spec-vs-mock block gaps in Appendix A, or edit the spec to match the mock and log it | Reviewers are told the templates are the source of truth; the mock disagrees in eleven places | T3, T8, T9, T10, T11, T13 pages |
| P1-6 | Add a "What is Growth Architecture" unit on Home: one heading, two lines, link to the hub | Andy's stated purpose for the front page (Otter 0:24:18); today Home only has the triangle line | / block 3 |
| P1-7 | Reserve a community group on Our people (person cards) labelled with the confirmed name for Colour of Numbers; add a Growth Collective link in the footer Company column | Otter resolves C and N; Sarah asked for a Growth Collective route; neither costs header space | /about/team/, footer |
| P1-8 | Decide the Overview row vs hub heading duplicate in the mega-nav | Source F asked to cut the duplicate; D-54 brought a version back. Either drop the arrow-link on the heading or drop Overview. | Mega-nav columns 1 and 2 |
| P1-9 | One home for DEI | Source A principle; today on both Values and Careers | /about/values/, /careers/ |
| P1-10 | Row links underlined at rest; secondary CTA and More link share one style | Rule 8 | Situations, Related lists, row-links |

**P2: polish and realism.**

| # | Opportunity | Why | Where |
|---|---|---|---|
| P2-1 | Use the deck's Why and What sentences as placeholder copy on each service page | The copy exists; showing it tests length and fit and answers Gary's "is the deck reflected" worry on the page itself | /services/*/ |
| P2-2 | `?topic={slug}` on every Contact CTA and a prefilled Topic field on /contact/ | Spec T3 block 1 | All CTAs |
| P2-3 | Working notes styled as annotations, not pills | Rule for Annotation units | Sidebar |
| P2-4 | Reduce the Home showreel slot or place Trusted partners above it | MURAL "banner up"; today the logos sit on the fold | / |
| P2-5 | FAQ unit (Editorial) drawn once on one service page and one sector page | Spec T3 block 13 says recommended for every canonical service; Gary asked for sector FAQs on the call; neither is drawn | One service, one sector |
| P2-6 | Insights hub: add the Latest unit the spec and Source A both call for | T9 block 2 | /insights/ |
| P2-7 | Operating Architecture appendix figure as a media slot with caption and anchor | Deck audit says "captioned figure"; the mock has prose | /services/operating-model-design/ |
| P2-8 | Consistent depth on thin pages: role page shows its form; Team gets a closing CTA; Values gets three value rows | Uneven depth reads as unfinished rather than deliberately light | /careers/growth-architect/, /about/team/, /about/values/ |
| P2-9 | Fix the Growth Strategy page order so it matches its own heading map | Sidebar says Proof after CIVD; page shows Proof before North Star | /services/growth-strategy/ |

---

## 7. Suggested next iteration checklist

Work through in order. Tick each only when it holds on every page, not one.

**Taxonomy (P0)**

- [ ] `wireframe.css`: solid border only on `.card`, `.tri a`, `.btn`, `.btn.secondary`. Remove border from `.metric`, `.numbers`, `.civd-cell`.
- [ ] `.btn` is solid fill; new `.btn.secondary` is outlined. Audit every `.btn` and assign one.
- [ ] Send, Search, Accept, Clear filters are `<button>` elements. Send and Search sit inside a `<form action="...">`.
- [ ] "Read on this page" removed from the report page; gate is a field plus secondary button.
- [ ] `.filter` becomes `<button class="filter" aria-pressed>` with a tick or pressed fill; no underline.
- [ ] Pagination items are links.
- [ ] CIVD: tint band, no per-cell border, caption with `#civd`, H3 repeat deleted.
- [ ] Find / Redesign / Test / Scale, Culture / Capability / Value, interim then embed, maturity then programmes: one How it works block each with a steps row.
- [ ] Hub: no offer card for a pillar that already has a triangle block in view, or no triangle block; choose one and log it.
- [ ] Activation: six cards only, "you need this when" line inside each card.
- [ ] Home: delete the More work card.
- [ ] `/catalogue/`: one definition row per unit beside its example; names match `03-page-layouts.md`. Retire `modules-taxonomy.html` once folded in.

**Fidelity (P1)**

- [ ] Mobile header with Menu toggle and panel on at least Home, Services hub and one service page at 390 px.
- [ ] Block label on every block: template ID, block name, Always / Conditional / Editorial. One toggle in the sidebar hides them.
- [ ] Advisor card class; used on CEO Advisory, hub pillar 3, Team.
- [ ] Case card with impact figure; Work featured card with impact figure.
- [ ] Appendix A blocks either added to the mock or removed from the spec with a D-number.
- [ ] Home: "What is Growth Architecture" unit after the triangle.
- [ ] Our people: community group with person cards; label confirmed with Andy (Colour of Numbers).
- [ ] Footer Company column: Growth Collective link, or a logged decision not to.
- [ ] Mega-nav: Overview row or hub-heading link, not both to the same URL; log the choice.
- [ ] DEI on one page; the other page links to it.
- [ ] Row links underlined at rest.

**Realism (P2)**

- [ ] Deck Why and What sentences as placeholder copy on the seven service pages and CEO Advisory.
- [ ] `?topic=` on every Contact CTA; Topic field shows the prefilled value.
- [ ] Sidebar chips restyled as notes.
- [ ] Home hero: smaller media slot or logos above it.
- [ ] One FAQ unit drawn on one service and one sector page.
- [ ] Insights hub Latest unit.
- [ ] Operating Architecture figure slot.
- [ ] Role page form; Team closing CTA; Values rows.
- [ ] Growth Strategy block order matches heading map.

**Sign-off tests (keep the v5 ones, add these)**

- [ ] Point at any framed unit on any page and say, without hovering, whether it is clickable. Ten out of ten.
- [ ] Find every button on the Contact page; each is a `<button>` or the header Contact.
- [ ] On /work/, click a filter and see its state change.
- [ ] On a phone-width viewport, open the menu and reach a service in two taps.
- [ ] Open `/catalogue/` and, for any unit on any page, find its row and its rule.

---

## Appendix A: spec blocks absent from the mock

Template blocks in `docs/03-page-layouts.md` with no corresponding unit on the live page. "Editorial" blocks are noted but not counted as gaps.

| Template | Block | Rule in spec | Mock page | Status |
|---|---|---|---|---|
| T1 Home | 5 Our work: "three case studies" | Always | / | Two cases plus a More work card |
| T3 Service | 12 People | Always when a lead is flagged | all /services/*/ | Absent on every service page |
| T3 Service | 13 FAQ | Editorial, "recommended for every canonical service" | all /services/*/ | Absent; not drawn anywhere |
| T3 Service | 1 Hero CTA `?topic=` | Always | all /services/*/ | No topic parameter anywhere |
| T8 Case study | 7 Team | Editorial | /work/dayinsure/ | Absent |
| T8 Case study | 8 Related services (cards) | Always | /work/dayinsure/ | Absent; services appear only as hero tags |
| T8 Case study | 10 Related work | Always | /work/dayinsure/ | Absent |
| T9 Insights hub | 2 Latest (one large plus three) | Always | /insights/ | Absent; opens with Reports |
| T9 Insights hub | 8 Newsletter sign-up | Always | /insights/ | The Nutshell is a paragraph with a link to /newsletter/; no inline field |
| T10 Insight | 5 Author box | Always | /insights/loyalty-without-the-discount/ | Author is a word in the meta line |
| T10 Insight | 8 Related insights | Always | both insight pages | Absent |
| T10 Insight | 9 Newsletter sign-up | Always | both insight pages | Absent |
| T11 About | 6 Clients logo wall | Always | /about/ | Absent |
| T11 About | 7 Values and careers teaser | Always | /about/ | Values linked; Careers not linked from About body |
| T13 How we work | 6 What clients say | Editorial | /about/how-we-work/ | Absent |
| T15 Careers | Open roles empty state | Always (empty state defined) | /careers/ | Not drawn |
| T15 Role | 3 How to apply form | Always | /careers/growth-architect/ | Text only |

Eleven Always blocks missing; four Editorial noted; two partial.

## Appendix B: page inventory reviewed

Home; Services hub; Growth Strategy; Proposition Innovation; Activation; Customer Research and Insight; Experience Engineering; AI Agents for Marketing; Operating Model Design; Growth Office; AI Enablement; CEO Advisory; Expertise hub; Loyalty; Membership; Subscriptions; Pricing; Customer Value; Financial services; Media; Consumer; Retail; Our work; Dayinsure; Key Group; Our thinking; Loyalty without the discount; The Pricing Paradox; About; Our people; Advisor profile; Our approach; Values and culture; Careers; Growth Architect role; Contact; Thank you; The Nutshell; Search; 404; Privacy; Cookie; Terms; Accessibility; Page modules catalogue; sitemap.html. Menu states: What we do open, Our thinking open, About open. Viewports: 1480 x 900, 390 x 844.

## Appendix C: unit counts used for the scorecard

Selected pages, counted from the live HTML. Full table in the review working notes; these are the rows the scorecard cites.

| Page | Links in main | `.btn` | Cards | Tri blocks | Metrics | CIVD cells | Tags | Filters (all inert) | `<button>` |
|---|---|---|---|---|---|---|---|---|---|
| / | 20 | 2 | 5 | 3 | 0 | 0 | 0 | 0 | 0 |
| /services/ | 33 | 1 | 11 | 3 | 0 | 4 | 0 | 0 | 0 |
| /services/growth-strategy/ | 17 | 2 | 5 | 0 | 0 | 4 | 3 | 0 | 0 |
| /services/activation/ | 22 | 2 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |
| /services/ceo-advisory/ | 12 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| /work/ | 9 | 2 | 3 | 0 | 0 | 0 | 0 | 8 | 0 |
| /work/dayinsure/ | 9 | 1 | 0 | 0 | 4 | 0 | 3 | 0 | 0 |
| /insights/ | 10 | 2 | 2 | 0 | 0 | 0 | 0 | 8 | 0 |
| /contact/ | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| /catalogue/ | 25 | 6 | 6 | 3 | 4 | 4 | 2 | 3 | 0 |
