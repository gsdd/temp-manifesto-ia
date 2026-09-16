# Wireframe fresh-eye review

**Manifesto Growth Architects** clickable wireframe  
Live: [https://temp-manifesto-ia.pages.dev/](https://temp-manifesto-ia.pages.dev/)  
Repo root: `mocks/` (Pages)  
Date: 16 September 2026  
Scope: review only. No IA redesign. No restyle of the site.

Walked on the live site: Home, services hub, Growth Strategy, Activation, CEO Advisory, Our work, Our thinking, About, Contact, Careers, catalogue, Loyalty, Financial services, plus mega-nav, mobile wrap at ~390px, Experience Engineering, AI Agents, Our approach, The Nutshell, search. Checked against v7 client report, Andy's deck, 7 Sep Otter notes, `docs/`, `mocks/README.md`, `mocks/catalogue/`.

---

## Executive take

- The IA is holding. Triangle, six-item chrome, Careers first-class, CIVD on Growth Strategy, keyword subtitles, Work with us / Work for us, The Nutshell, light sectors. Andy and the client can already click the recommended structure.
- The wireframe is failing as a **module system**. Almost every unit is a grey bordered rectangle. A reviewer cannot tell what is a destination card, what is a static diagram, what is a filter, and what is a button.
- Links and buttons are one family. Header Contact, hero Contact, form Send, cookie Accept, and 404 "What we do" all use `a.btn`. Secondary actions are underlined text. Filters, pagination and "More filters" are inert `<span>`s that look like tags.
- `card.offer` is a dumping class: services, expertise themes, articles, job roles, and thank-you onward links. Triangle tiles (`.tri a`), CIVD cells, metric boxes, logo placeholders and filters share the same "box with a border" silhouette.
- The catalogue (`/catalogue/`) lists shapes, not jobs. It groups page tags with filters, omits list rows, case lines, numbers line vs stats, closing CTA band, and the header button rule. Docs still say "chips" in `03-page-layouts.md` after D-59 banned that word in UI copy.
- Source fidelity is stronger than craft. Deck named modules exist as homes (CIVD, AgentLab, Find/Redesign/Test/Scale, Side-by-Side). Several are diluted: AgentLab is group prose not a named-agent catalogue; Operating Architecture is headings not a captioned figure; related expertise is tags without the promised one-line intersection; service People and FAQ blocks are missing.
- Quickest client-review win is not more pages. It is a four-affordance key (button, text link, card-as-link, static block) applied consistently, plus filter/tag/chip pulled apart, plus catalogue rewritten as that taxonomy.
- Do not redesign the sitemap. Fix unit identity first.

---

## Thesis: what these units are

Gary's question is the right one. The mock has many boxes and almost no names that stick.

A wireframe for client review needs four affordances only. Everything else is a named variant of one of those four.

| Affordance | Looks like | Does | HTML rule |
|---|---|---|---|
| **Primary button** | Ink outline, padded, one per cluster | Starts an action: enquire, send, subscribe, accept, arrange a conversation | `a.btn` or `<button>` for true submit. Never for "go read a page". |
| **Text link** | Underlined text, no box | Goes to a page or in-page target | `a` / `a.text` / `a.more`. Header items except Contact. Situations. Footer. Mega-nav strands. |
| **Card-as-link** | One whole tile, one destination, hover underline on title | Routes to a content object | `<a class="card card--{type}">`. The type changes the silhouette (image, document, avatar, offer). |
| **Static block** | Box or diagram that is not a hit target as a unit | Explains. Internal text links allowed | Not an `<a>` wrapping the unit. CIVD, metrics, logos, quotes, film, numbers line, article body. |

Two extra **controls**, never dressed as cards or as destination tags:

| Control | Looks like | Does |
|---|---|---|
| **Filter** | Selected / unselected chip. "More filters" is a disclosure **button** | Narrows the listing. Does not navigate. Active filters are removable. |
| **Pagination** | Numbered controls, current state marked | Changes page of results. Links or buttons, not inert spans. |

**Page tag** is a text-sized destination to one dimension (max three). It must not look like a filter.

If a unit cannot be named from that list, it should not get a border.

---

## Module taxonomy proposal

Use these names in the catalogue, in working notes, and in any later CMS mapping. Stop mixing "module / block / chip / card / box".

| Name | Visual shape | When to use | Affordance | Live class today | Verdict |
|---|---|---|---|---|---|
| Primary button | Ink outline rectangle | Contact (Work with us), Arrange a conversation, Send, Subscribe, Accept cookies, Work for us (careers route), Clear filters | Button | `a.btn` | Shape is fine. Job is overloaded (see muddle list). |
| Secondary link | Underlined mid-ink text | What we do, See our work, All work, All thinking | Text link | `a.text`, `a.more` | Fine. Do not box these. |
| Header item | Text, optional caret | What we do, Our work, Our thinking, About, Careers | Text link that may open a panel | `a.top-link` | Fine. Contact stays the only header button. |
| Pillar tile | Three equal tiles, title + pillar line, no image | Home and services hub triangle only. Never a fourth tile. | Card-as-link to the pillar page (hub: in-page anchor plus page) | `.tri a` | Keep. Must not share fill/padding with offer cards or CIVD. |
| Offer card | Grey fill, title + one line, no image | Buyable services only | Card-as-link to `/services/{slug}/` | `a.card.offer` | **Broken.** Also used for themes, articles, roles, thank-you. |
| Work card | 16:10 image ph + client + result | Case studies | Card-as-link to `/work/{client}/` | `a.card` + `.ph` | Fine, except Home's third card is a listing shortcut in this costume. |
| Report card | Document silhouette + title | Reports | Card-as-link to the report | `a.card` + `.doc` | Fine. |
| Article card | Text-led, no document ph, no offer fill | Articles | Card-as-link | `a.card.offer` on Home and `/insights/` | **Wrong class.** Needs its own silhouette. |
| Person card | Avatar + name + one line | People, advisors, joiners | Card-as-link to profile | `a.card.person` | Fine, except About uses one as a "Our people" listing shortcut. |
| Role card | Title + location/type/hiring | Open roles | Card-as-link to `/careers/{role}/` | `a.card.offer` | **Wrong class.** Job, not a service. |
| Theme card | Title + definition + counts | Expertise hub only | Card-as-link to `/expertise/{theme}/` | `a.card.offer` | **Wrong class.** Not an offer. |
| Page tag | Small outline pill, text | The one dimension on that page type, max three | Text-sized link to the dimension page | `.page-tags a` | Fine if filters look different. They do not. |
| Filter | Pill with on/off. More filters is a button | Work and thinking listings | Control, not a link | `span.filter` | **Inert.** Looks like a tag. |
| List row | Full-width line, title left, meta right | Related thinking, search results, events, engagement shapes, "Where we help" | Text link on the row | `ul.list` | Fine. Missing from the catalogue. |
| Situations list | Two-column text lines, hairline rules, no boxes | Hub "Where are you starting from?" and Activation "Which of the six" | Text link to the matching service | `ul.situations` | Fine on the hub. On service pages the same class is static, unlinked. |
| Case line | One sentence + text link | Proof under a pillar when a grid would over-weight it | Text link | `p.case-line` | Fine. Missing from the catalogue. |
| CIVD four-cell | Four labelled cells | Growth Strategy `#civd`; compact on the hub | Static block | `.civd-grid` / `.civd-cell` | Right job. Looks like offer cards and metrics. |
| Metrics | Number + caption boxes | Case "At a glance"; deck figures on EE and AI Agents | Static block | `.metrics` / `.metric` | Docs asked for a **numbers line**. Live is a four-cell grid. Catalogue calls it "Stats". |
| Logo row | Dashed logo placeholders | Trusted partners, Awards, sector clients | Static, or link only if a case exists | `.logo-ph` | Home logos do not link (MURAL: link if a case exists). Same dashes as work-card image ph. |
| Quote | Left rule + cite | With work, never a testimonials page | Static | `blockquote.quote` | Fine. |
| Film 16:9 | Dashed 16:9 | Showreel, approach films, case film | Static | `.video-ph` | Fine. |
| Form field | Label + empty box | Contact, Nutshell, search | Input (wireframe can stay a box if labelled as a field) | `.field .box` | No control type, no required, no error, no select options. Send is a link. |
| Closing CTA band | Line + button + secondary link | End of content pages | Button + text link | `.closing` | Copy is identical almost everywhere, including on `/work/` ("See our work"). |
| Empty state | Dashed panel + recovery action | Listings when filters/search return nothing | Shown as a **state**, not a permanent extra section | `.empty-state` + `span.wf-label` | Label exists. Still sits under real results, so it reads as page content. |
| Working-note chip | Sidebar only | IA annotation | Not a live module | `.chip` | Correctly off the catalogue page. Name still leaks into docs. |

Chrome (header, mega-nav, dropdown, breadcrumb, footer, cookie bar) stays chrome. Do not catalogue those as page modules except as a one-line "not in this index" note. The current catalogue includes cookie bar and a mega-nav fragment, which blurs content vs chrome.

---

## Where the live wireframe muddies that

Each item is a taxonomy failure, not an IA change.

### 1. Button means "rectangle I might click"

`a.btn` is used for:

- Header Contact (correct: primary enquire)
- Hero Contact / Arrange a conversation (correct)
- Closing-band Contact (correct)
- Form Send and Subscribe (action, but it is a link to thank-you, not a submit)
- Cookie Accept, which **navigates to the cookie policy** (`mocks/assets` cookie bar on every page)
- Empty-state "Clear filters" (control, inert)
- 404 "What we do" (that is navigation; should be a secondary link)

A client cannot tell button from link from control. There is no filled primary vs outline secondary vs text. Cookie Accept is the loudest control on every page.

### 2. `card.offer` is not an offer

Offer fill is applied to:

- Services on the hub and related-services blocks (correct)
- Expertise hub themes (`/expertise/`: "Cases and thinking")
- Home featured article (`Loyalty without the discount`)
- Insights listing article
- Careers role (`Growth Architect`)
- Thank-you onward mix (What we do, a case, an insight)

Same grey tile, four different object types. Catalogue shows "Service cards" only.

### 3. Grey boxes with different jobs, same silhouette

On `/services/` a reviewer scrolls through, in order: pillar tiles, situations (text, good), CIVD four-cell, offer cards, person cards. CIVD, pillar tiles and offer cards are all bordered rectangles. On Growth Strategy, CIVD sits near related-service offer cards. On Experience Engineering and AI Agents, `.metric` boxes join that family. Logo dashes on Home match work-card image dashes.

### 4. Filters look like tags look like chips

- `/work/` and `/insights/`: `span.filter` and `span.filter.on`. Not buttons, not links, not toggling.
- "More filters" is `span.wf-label`, a caption, not a disclosure.
- `.page-tags a` on Growth Strategy related expertise, case heroes, insight heroes: same pill outline.
- Sidebar `.chip` (annotation) is the third pill family. Catalogue section "On-page tags" shows page tags **and** filters as siblings.

v7 and `03-page-layouts.md` still say related expertise is "chips, each with one line on the intersection". Live tags have no intersection line. The word "chip" was supposed to die in UI copy (D-59).

### 5. Situations are links on the hub, dead text on service pages

Same `ul.situations` class. On `/services/` each line is an `<a>`. On Growth Strategy, Activation, CEO Advisory, EE, the three "Why this, now" lines are `<li>` only. Visually identical, different behaviour.

### 6. Listing shortcuts dressed as content objects

- Home Our work: third tile is "More work / All case studies" in a work-card costume, then an "All work" text link under the quote. Two ways to do the same job, one of them fake.
- About Leadership: a person card labelled "Our people / Everyone client-facing" that goes to the listing.
- Activation repeats "Which of the six" as a linked list **and** as six offer cards with the same sentences.

### 7. Closing CTA does not know which page it is on

Almost every page ends with "Tell us about your growth challenge" + Contact + "See our work". On `/work/` the secondary link is "See our work" to itself. On CEO Advisory the hero button is "Arrange a conversation" (correct, quieter CTA) and the closing band heading matches that, then the button snaps back to "Contact".

### 8. Catalogue is a CSS zoo, not a system

Present: page tags, filters, four card types, logos, quote, video, stats, article prose, CIVD, triangle, mega-nav fragment, two situation lines, empty state, pagination, two forms, primary/secondary CTA, cookie bar.

Absent, though used on live pages: list row, row-links (Home expertise; theme related themes), case line, numbers line vs metrics, closing CTA band, role card, theme card, article card, pillar note, also-known-as line, breadcrumb, header button vs items, More-filters control, search field, `wf-label` as annotation.

`card.flat` is in CSS and unused.

---

## Gaps vs good wireframe practice

These are craft gaps. The IA does not need to move.

**States.** Empty and error are labelled stubs (`wf-label` + `.empty-state`) left **on** the populated listing. A client reads them as part of the page. They should be annotated as an alternate state, or shown once on a dedicated state board. No hover, selected, disabled, focus, validation error, or mega-nav open/closed notes on the page itself. Sidebar heading maps do not cover interaction.

**Mega-nav behaviour.** Desktop hover works (`nav.js`: 150 ms open, 300 ms close, Escape, click-outside). `docs/01-primary-navigation.md` also specifies click-to-open for touch, `aria-expanded` on a **button**, and a two-level **mobile menu** (logo, Contact, Menu, full-screen panel, 44 px toggles). Live: top-level items are links with carets; below ~720 px the header wraps; there is no Menu button. At ~390 px the six items plus Contact stack. Spec and mock disagree, and the mock has no annotation of the intended mobile panel.

**Mobile.** CSS collapses grids to two then one column. That is reflow, not a mobile wireframe. No hamburger, no sticky Contact, no sample of the collapsed What we do list. v4/v5 docs still claim a two-level mobile menu.

**Forms.** Fields are empty `.box` divs. No input type, required mark, helper text, error, or success. Topic is not a service select. Work with us has no "Email Mark" tracked control (MURAL / working notes mention it). Send is a link to thank-you, so the form never fails.

**Filters.** Spec: one group open, More filters reveals the rest, URL query, removable active chips, AND across groups (`03-page-layouts.md` T7/T9). Live: both rows visible, nothing works, pagination is inert spans.

**Content vs chrome.** The sidebar split is the best craft decision in the mock. Catalogue dropping the sidebar is correct (D-59). Cookie bar inside every page is chrome repeating as content. Catalogue then **re-lists** the cookie bar as a module.

**Hierarchy labels.** `h2.sec` (uppercase, mid ink) vs `h2.plain` (sentence case, large) is unexplained. A reviewer does not know which is a section kicker and which is a content H2. No "this is placeholder / this is proposed copy" mark on body prose vs nav labels.

**People and FAQ.** T3 makes People Always when a lead is flagged, FAQ Editorial but recommended. Neither appears on canonical service pages.

**Related expertise.** Specified as tags **plus** one line on the intersection. Live: pills only.

**Proof order.** T3: What we do, then Proof, then How it works, then the named module. Experience Engineering and Customer Research skip What we do and put Proof first. Growth Strategy has a stub What we do, then Proof, then North Star H2s, then CIVD, then How it works (module before method in the spec, reversed here).

**Docs drift.** `01-primary-navigation.md` section 1 still describes five header items, Insights as a plain link, Careers under About. The live mock (and the v7 report, and section 11 of the same file) is six items with Careers first-class and Our thinking dropdown. The mock is right; the spec's front is stale. Do not "fix" the mock back to five.

---

## Missed or diluted vs input sources

Authoritative claim set: v7 client report. Supporting: Andy's deck (Drive re-read 16 Sep), Otter 7 Sep, MURAL keep/drop in `docs/mural-gap-check.md`.

### Holding (do not reopen)

| Claim | Evidence | Live |
|---|---|---|
| Services-led, triangle in call order | v7 §1–4; Otter weighting; deck slides 2–3 | Mega-nav, Home, hub |
| Six-item chrome, Careers first-class, Contact button | v7 §2; MURAL | Header on every page |
| CEO Advisory full ink, quieter by width | v7 §1, D-57 | `grid-template-columns: 1fr 1.15fr 0.85fr` |
| Keyword subtitle on every strand | v7 §4, D-58 | Mega-nav `<small>` on all strands |
| CIVD on-page, not a nav item | v7 §1, deck slide 5, MURAL | `/services/growth-strategy/#civd` and compact on hub |
| Work with us / Work for us | v7 §2; MURAL | `/contact/#work-with-us`, `#work-for-us`; Careers speculative route |
| The Nutshell named | v7 sitemap; MURAL | Footer, Contact, `/insights/#events`, `/newsletter/` |
| Sectors light, not in header | Otter; v7 §2 | Footer + four landings; `/sectors/` not an index |
| No SxS abbreviation | v7 naming table; D-31 | "Side-by-Side" only |
| Also-known-as on renamed services | v7; deck names | Customer Intelligence, Data Agents / AgentLab, Operating Architecture |
| Reports on-page, not PDFs | MURAL | Report shell + "Read on this page" |
| FT / awards not in the hero | MURAL | Home Awards below work |
| No homepage reports grid | MURAL | Featured report + one article after the triangle |

### Diluted or missing

| Item | What we claimed | What live does | Pointer |
|---|---|---|---|
| Triangle **weight in the page**, not only the menu | Equal-contrast tiles; CEO not second-class | Tiles match. Hub CEO section is person cards plus a sentence, vs six offer cards above, so the **page** still reads quieter than the menu. That may be intended (Otter: do not design the site around advisory) but it is not annotated. | `/services/` CEO block vs Activation block |
| Numbers line | "One line of figures from Source B" (T3) | Metric **boxes**. EE: 3x EBITDA. AI Agents: 4 wks / 6 wks. Catalogue: "Stats". | `/services/experience-engineering/`, `/services/ai-agents-for-marketing/`, catalogue |
| AgentLab catalogue | Named agents as entries, grouped as the deck | Four H3 groups, names in prose, not a scannable catalogue | Deck AgentLab list vs `/services/ai-agents-for-marketing/#agentlab` |
| Operating Architecture figure | Captioned figure of the appendix diagram | H3s and paragraphs, no figure module | Deck appendix vs `/services/operating-model-design/#operating-architecture` |
| Find / Redesign / Test / Scale | Four named phases | Present as four H2s. Not a distinct "how it works" module in the catalogue | `/services/experience-engineering/` |
| Related expertise intersection line | "as chips, each with one line on the intersection" | Pills, no line | Growth Strategy related expertise |
| People on services | Always when a lead is flagged | Absent on canonical service pages | T3 vs e.g. Growth Strategy |
| FAQ | Recommended on canonical services | Absent | T3 |
| Expertise hub cards | Definition + counts of cases and insights | "Cases and thinking" on an offer card | `/expertise/` |
| Sector landings | Client logos always (T6) | Logo row is there. Case cards repeat Dayinsure/Key Group on every sector, so proof is not sector-true. | `/sectors/financial-services/` |
| About | Clients logo wall; values and careers teaser | No clients wall. Approach/values are two text links. C&N stub is present (open decision, OK). | `/about/` vs T11 |
| Email Mark | MURAL: keep, track which button | Working notes only. Not on the form. | Contact working notes vs `/contact/` |
| Trusted partners link to cases | MURAL: only if a case exists | Eight unlinked logo boxes. Dayinsure and Key Group exist. | Home Trusted partners |
| Insights hub structure | T9 "Latest" then type filters. MURAL: reports at the top | Live follows MURAL (Reports, then Articles+filters, then Events). T9 is stale. | `/insights/` vs T9 vs mural-gap-check |
| Closing CTA on CEO Advisory | Quieter "Arrange a conversation" | Hero yes, closing button "Contact" | `/services/ceo-advisory/` |
| Mobile What we do | Two-level menu in `01-primary-navigation.md` §3.5 | Not built | Live header wrap |
| Growth Collective | Open decision, off the public IA unless confirmed | Correctly absent | v7 §8 |
| C&N | Stub, do not invent | Stub on About | v7 §8, `/about/` |
| `01-primary-navigation.md` front matter | File still says five header items in §1 | Mock and v7 say six | Docs, not the live page |

Deck copy is correctly **not** dumped into the mega-nav (Otter: deck is not website copy). Gap is on-page module fidelity, which matches v7's own line: "The gap to best in class is on the pages, not extra nav items."

---

## Catalogue accuracy

| Catalogue section | Matches live? | Fix |
|---|---|---|
| On-page tags | Mixes tags and filters | Split: Page tag vs Filter |
| Service / case / report / person cards | Partial. Omits article, theme, role. Offer class leaked. | One row per card type in the table above |
| Proof and media | Logos, quote, video, stats | Rename Stats to Metrics. Add numbers line as a different shape |
| Article blocks | Prose only | Add Article card |
| CIVD | Yes | Mark **static** |
| Triangle | Yes | Mark **card-as-link, three only** |
| Mega-nav | Chrome, not a page module | Move to a chrome note |
| Situations | Two lines, both linked | Note hub = links, service Why = static |
| Empty state / pagination | Shown | Mark as listing **states/controls**, and that live stubs sit on populated pages |
| Forms | Two, Send as `a.btn` | Add field types and error; Nutshell form lives on `/newsletter/` not here |
| Primary and secondary CTA | Yes | Add closing band; CEO variant |
| Cookie bar | Chrome | Out of the page-module list |

Rebuild `/catalogue/` as this taxonomy, one labelled specimen each, with a one-line "when to use" under the specimen. That is a P0 for client review. It is not a site redesign.

---

## Prioritised opportunities

### P0 (do before the next Andy/client walkthrough)

1. **Publish the affordance key** on `/catalogue/` and in this doc. Four affordances plus filter vs page tag. One specimen each. Label "static" vs "whole unit is a link" vs "control".
2. **Stop using `card.offer` for non-services.** Article, theme, role, thank-you: different class, different silhouette (even a wireframe-level one: document vs avatar vs "Role" kicker vs text-only).
3. **Make CIVD, metrics, logos, and pillar tiles distinguishable.** Different treatment, not different copy. Suggestion: pillar tiles stay bordered and linked; CIVD gets a 2x2 with a "Frame (static)" kicker; metrics stay numbers; logos stay dashed but smaller and in a row labelled Logo row.
4. **Pull filters off the tag visual.** Selected/unselected. "More filters" as a button that is labelled as a disclosure. Page tags stay destination pills. Sidebar chips stay in the sidebar.
5. **Buttons only for actions.** Cookie Accept must not be the same component as "go to What we do". 404 primary can stay a button if the job is recovery; "Our work" and "Contact" there should not all be buttons. Header Contact remains the one chrome button.

### P1 (same sprint, still not an IA change)

6. Situations: if it is a router, keep it linked (hub, Activation six). If it is a "you are here if" list on a service page, drop the situations styling that implies a hit target, or annotate "static".
7. Remove fake object cards: Home "More work" tile; About "Our people" person card as a listing link. Use `a.more`.
8. Empty states: one annotated alternate, not a second block under results. Same for search.
9. Closing CTA: per-template secondary. On `/work/` drop "See our work" or point to What we do. On CEO Advisory keep "Arrange a conversation" through the closing button.
10. Related expertise: add the one-line intersection, or stop calling them chips and treat them as page tags only (already the v4 rule). Pick one and show it.
11. Forms: mark control types (text, email, select Topic = services, textarea). One error specimen. Send as a button to thank-you is acceptable in a wireframe if labelled "submit (goes to thank-you)".
12. Catalogue: add list row, case line, numbers line, closing band, role card, theme card, article card. Remove cookie bar and mega-nav from the page-module list, or put them under "Chrome".

### P2 (when the wireframe has to stand in for build)

13. Mobile menu as specified in `01-primary-navigation.md` §3.5, or annotate "desktop wireframe; mobile menu not in this mock" on every page. Do not leave a wrapping header as if it were the mobile IA.
14. Restore T3 People (when flagged) and a FAQ stub on one canonical service as the pattern.
15. AgentLab as a named-entry list (deck names). Operating Architecture as a captioned figure placeholder, not only H3s.
16. Numbers line as a **line** where the spec says line; keep metric boxes for case "At a glance" only.
17. Trusted partners: link Dayinsure and Key Group logos; leave the rest unlinked and say so.
18. Align `01-primary-navigation.md` §1 with the six-item chrome already live (docs fix). Align T9 Insights "Latest" with the MURAL reports-first hub, or the other way round. Pick MURAL; change the template text.
19. Mega-nav: add a one-line behaviour note in the sidebar on Home (hover delay, click goes to hub, intended mobile panel). Optional: click-to-open to match the spec.
20. Experience Engineering / Customer Research: restore a short What we do block so Proof is not the first body module after Why.

Out of scope: new sitemap URLs, Growth Collective, expanding C&N, putting CIVD or AgentLab in the mega-nav, greying CEO Advisory, adding sectors to the header.

---

## Optional: affordance key (specimen only)

Not applied to the site. Drop-in for catalogue if useful.

```html
<!-- Four affordances. Wireframe grey only. -->
<p class="wf-label">Primary button (action)</p>
<a class="btn" href="/contact/">Contact</a>

<p class="wf-label">Text link (navigate)</p>
<a class="text" href="/work/">See our work</a>

<p class="wf-label">Card-as-link (one object, one URL)</p>
<a class="card offer" href="/services/growth-strategy/">
  <strong>Growth Strategy</strong>
  <span>Where to focus and how to win</span>
</a>

<p class="wf-label">Static block (not a hit target)</p>
<div class="civd-grid compact">
  <div class="civd-cell"><strong>Customer</strong><span>Who you grow with.</span></div>
  <!-- three more cells -->
</div>

<p class="wf-label">Filter (control) vs page tag (destination)</p>
<button class="filter on" type="button">Experience Engineering</button>
<a class="page-tag" href="/expertise/loyalty/">Loyalty</a>
```

Rule in one sentence: **if the whole box goes somewhere, it is a card; if only the words go somewhere, it is a link; if nothing goes somewhere, it is static; if it changes this page's results, it is a filter.**

---

## Method

- Live Pages walk, desktop and ~390 px, 16 September 2026.
- Local HTML/CSS: `mocks/index.html`, `mocks/catalogue/index.html`, `mocks/assets/wireframe.css`, `mocks/assets/nav.js`, representative templates under `mocks/services/`, `work/`, `insights/`, `about/`, `contact/`, `careers/`, `expertise/`, `sectors/`.
- Sources: attached v7 report, Andy's services deck, Otter 7 Sep extract; in-repo `docs/03-page-layouts.md`, `docs/01-primary-navigation.md`, `docs/mural-gap-check.md`, `docs/andy-deck-coverage.md`, `mocks/README.md`.
- Not in scope: visual brand, copy polish, new pages, CMS modelling beyond naming units.
