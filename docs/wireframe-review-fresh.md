# Independent wireframe review

**Manifesto Growth Architects** clickable wireframe  
Fable · 16 September 2026  
Live site reviewed: [https://temp-manifesto-ia.pages.dev/](https://temp-manifesto-ia.pages.dev/)  
Repo: `mocks/**` on `main` (commit `cb76246`), plus `docs/**`

This is a second opinion on the wireframe as a design and delivery artefact. It is not a new IA. It does not propose a redesign of the live pages.

Gary's note is the right diagnosis: modules are not clear; links and buttons are muddled; cards and random boxes are muddled. The package needs to say what each unit **is**.

Companion: [`docs/module-system.md`](module-system.md). Catalogue demo (wireframe only): [`mocks/catalogue/index.html`](../mocks/catalogue/index.html).

---

## Verdict in one screen

The IA is in good shape. The triangle, six-item chrome, keyword subtitles, CEO Advisory at full ink, and catalogue-as-wireframe-only all hold on the live site. What fails a professional wireframe test is **unit identity**.

A designer or developer opening Home or the Services hub cannot tell, from the shapes alone:

- which bordered rectangle is a destination card, a section, a diagram cell, or a number
- which control is a primary action, a navigation link, a filter, or a tag
- which grey chip is live page UI and which is an IA working note

Fix the module language first. Do not invent more IA in this pass.

**Self-check (pass)**

| Check | Live evidence |
|---|---|
| CEO Advisory full weight | Home triangle, hub triangle, mega-nav H3 all use the same ink and weight. Column is narrower (`0.85fr` vs `1fr` / `1.15fr` in `.mega-cols`), not paler. |
| Keyword subtitles | Every mega-nav strand has a `<small>` line. |
| Catalogue is wireframe-only | `/catalogue/` is not in the header or footer. Linked from the heading-map "Page modules" and `sitemap.html` Wireframe tools. |
| No greying of CEO Advisory | No grey type, no quieter class on the third pillar. D-57 holds. |

---

## 1. Wireframe gaps

What a professional IA wireframe package usually includes, and what this one currently gives a reviewer.

Evidence is from the live Pages site and matching files under `mocks/`.

### 1.1 Component legend

**Missing on every content page.** The catalogue at [https://temp-manifesto-ia.pages.dev/catalogue/](https://temp-manifesto-ia.pages.dev/catalogue/) is an inventory of live blocks, but it still names things as "cards", "triangle blocks", "stats", and "page tags". It does not say: this unit is an Offer card (whole-card link); this unit is a Theme tag (text link, not a filter); this unit is a Primary button (do this).

The sidebar "Working notes" use class `.chip` and a heading "Modules". Those chips are IA annotations (`docs/03-page-layouts.md`: not live page modules). On screen they look like the same family as `.page-tags a` and `.filter`.

### 1.2 Interaction states

**Missing.** CSS has `:hover` underline and `:focus-visible` outline. There is no documented default / hover / active / disabled / current / error / success for:

- primary button (`.btn` is always an `<a>`)
- filter chips (they are `<span class="filter">`, not controls)
- form fields (empty grey `.box` only)
- mega-nav open vs closed (works in JS; no annotated state sheet)

A developer cannot implement filters or forms from the wireframe without guessing.

### 1.3 Mobile

**Not a wireframe deliverable.** `mocks/assets/wireframe.css` collapses grids at `1100px` and `720px`. There are no mobile frames, no hamburger spec, no stacked mega-nav. The mock is declared desktop-first in `mocks/README.md`. That is fine as a decision. It is not fine as an unspoken gap: the next design pass will have to invent mobile IA (especially What we do) with no wireframe constraint.

### 1.4 On-canvas annotations

**Sidebar only, and only on pages that are not the catalogue.** Most pages put purpose, weight, keyword, and MURAL notes in `.sidebar` (`.ia-chips` + `.heading-map`). The main column has almost no labels. Exceptions: `.wf-label` on Work, Thinking, and Search empty states ("Empty state") and on "More filters".

Those labels are useful. They are also easy to misread as live copy, because they sit inside `main.page`.

Page purpose is in the heading-map "Intent" line. It is not on the canvas of the page it describes.

### 1.5 Empty, error, loading

| State | Present? | Evidence |
|---|---|---|
| Empty (listings) | Stub only, always on | [Work](https://temp-manifesto-ia.pages.dev/work/) and [Thinking](https://temp-manifesto-ia.pages.dev/insights/) show the empty module **under** results. It is not a state of the grid. |
| Form error / validation | No | [Contact](https://temp-manifesto-ia.pages.dev/contact/) fields are blank boxes. No required, helper, or error. |
| Loading | No | Filters do not load. Search does not load. |
| 404 | Yes | `/404/` with routes to What we do, Our work, Contact, Search. |
| Thank you | Yes | `/contact/thank-you/` |

The always-visible empty stub is the wrong teaching example. It looks like a page section called "Empty state".

### 1.6 Form field specs

**Thin.** Work with us: Name, Company, Email, Topic, Message, Send. Work for us: Name, Email, Message, Send. No field type, required flag, Topic option list (the IA says `?topic=`), file upload, privacy tick, or error copy. Send is an `<a class="btn">` to thank-you, not a submit control.

### 1.7 Content inventory labels

**Missing in the main column.** Placeholder copy is prose ("Two to four short paragraphs", "One-line result", "Logo"). It does not mark region vs unique content, CMS field, or character count. The heading map lists H1/H2/H3, which is necessary but not a content inventory.

### 1.8 Responsive breakpoints

CSS breakpoints exist (`1100px`, `720px`). They are not named in the package, not drawn as frames, and not listed in the catalogue. The layout grid (`.layout`) is page-plus-sidebar; at 1100px the sidebar stacks under the page, which is an annotation layout, not a site breakpoint.

### 1.9 Page purpose statements

Present in the sidebar Intent line, and in `docs/02-sitemap.md` / `docs/03-page-layouts.md`. **Not on-canvas.** A stakeholder looking only at the "browser" column cannot see why the page exists.

### 1.10 Decision notes on-canvas

MURAL keep/drop and keyword notes sit in sidebar chips. D-57 (do not grey CEO Advisory) and D-58 (strand subtitles) are visible in the mega-nav itself, which is the right place. Other decisions (CIVD is not a nav item, catalogue is not live, Careers is first-class) are not labelled on the units they affect.

`docs/02-sitemap.md` still says "Careers is not in the header." The live header has Careers as a first-class `.top-link.plain`. The wireframe is right; that sitemap line is stale.

### 1.11 What the package already does well

Do not throw these away in the next pass:

- Full sitemap of real HTML pages, not a handful of templates.
- Shared header, mega-nav, footer, cookie bar, breadcrumbs.
- Heading map and working notes beside the page (right idea; wrong visual language).
- Catalogue exists and is correctly excluded from live chrome.
- Greyscale, no brand, no imagery: it still reads as a wireframe.

---

## 2. Module taxonomy clarity

Audit of recurring on-page units. Scope: Home, Services hub, Growth Strategy, Activation, CEO Advisory, Work listing, Thinking listing, Contact, Catalogue. Other templates are cited where they prove a collision.

### 2.1 How to read this table

**What it currently is** is the job the unit is doing, not the CSS name. **CSS** is the live class. **Problem** is where the same look means two jobs, or two looks mean one job.

### 2.2 Chrome (every page)

| Unit | What it currently is | CSS / node | Evidence | Problem |
|---|---|---|---|---|
| Logo | Home link | `a.logo` | Header on all pages | Dashed box. Fine as a placeholder. |
| What we do | Nav link that also opens mega-nav | `a.top-link` + `aria-haspopup` | Header | Looks like Our work (plain link) except for the caret. Click goes to `/services/`; hover opens panel. Not labelled. |
| Our work, Careers | Plain nav links | `a.top-link.plain` | Header | Same visual weight as dropdown parents. |
| Our thinking, About | Nav links with dropdown | `a.top-link` + `.dropdown` | Header | Dropdown items are plain text links. Good. |
| Contact in header | Primary action, visually a button, actually a link | `a.btn` | Header | First example of link-as-button. Correct pattern for "go to Contact". Never explained. |
| Mega-nav pillar title | Hub link | `a.pillar-hub` | What we do panel | Underlined heading with chevron. Same destination as Overview on GS/Activation. |
| Mega-nav strand | Nav link + keyword subtitle | `li a` + `small` | Panel | Overview uses `.strand-overview` (bold). Other strands are regular. Subtitles are the keyword layer (D-58). |
| Mega-nav footer row | Utility nav links | `.mega-row a` | Panel | Mid grey, small. Fine. |
| Breadcrumb | Path links | `.crumbs a` | All except Home | Fine. |
| Footer column links | Nav links | `.footer-cols a` | All pages | Fine. |
| Footer search Go | Text link pretending to submit | `form.footer-search a` | Footer | A link, not a submit. |
| Cookie Accept | Action, visually a button, actually a link | `.cookie-bar a.btn` | All pages | Same `.btn` as Contact. Should be a button in production. Cookie policy is a text link beside it. Good contrast, unnamed. |

### 2.3 Home (`/`)

[https://temp-manifesto-ia.pages.dev/](https://temp-manifesto-ia.pages.dev/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Hero H1 + strapline | Positioning, not a module with a name | `.hero h1`, `.hero p` | Fine. |
| Contact + What we do | Primary button-link + secondary text link | `.cta a.btn` + `a.text` | Correct pair. Not named. |
| Showreel | Media placeholder | `.video-ph` | Fine. |
| Trusted partners | Logo strip | `.logos .logo-ph` | Dashed boxes. Not links, despite MURAL "link only if a case exists". |
| Triangle | Three **pillar tiles** | `.tri a` | Bordered box, title + subtitle. Looks like an Offer card, but it is a pillar hub, not a service. CEO Advisory is equal ink (pass). |
| Triangle line | Caption + text link | `.tri-line` | Fine. |
| Featured report | Thinking card (document) | `.card` + `.doc` | Correct card type. |
| Featured article | Intended as a thinking card | `.card.offer` | **Collision.** Offer skin (grey fill, no media) used for an article. Same class as a service card on `/services/`. |
| All thinking | Text link | `a.more` | Same job as `.cta a.text`, different class. |
| Case cards | Proof cards | `.card` + `.ph` | Correct. |
| "More work" | Listing shortcut dressed as a case | `.card` + `.ph` | **Collision.** A third "case" that is not a case. |
| Quote | Quote | `blockquote.quote` | Fine. |
| Awards | Logo strip (same as partners) | `.logos` | Same visual as Trusted partners, different meaning. Need a label, not a new shape. |
| Growth problems we know best | Theme names as text links | `.row-links a` | Correct: not cards, not tags. |
| Closing | Repeat of the action pair | `.closing` + `.cta` | Fine. |

### 2.4 Services hub (`/services/`)

[https://temp-manifesto-ia.pages.dev/services/](https://temp-manifesto-ia.pages.dev/services/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Eyebrow | Section label | `.eyebrow` | Fine. |
| Triangle (anchors) | Pillar tiles linking to `#hub-gs` etc. | `.tri a` | Same look as Home, different destinations (in-page vs pillar URL). Not labelled. |
| Situations | Problem-entry **link rows** | `ul.situations a` | Correct module. |
| Pillar section | Section, not a card | `.pillar-sec` | Fine. |
| CIVD compact | Framework diagram cells | `.civd-grid.compact .civd-cell` | Grey filled boxes. Same family as Offer cards and metric boxes. |
| Offer cards (GS, Activation) | Service destinations | `.card.offer` | Correct use. |
| Case line | Text link to one case | `.case-line a` | Correct: not a card. |
| Advisor cards | Person cards | `.card.person` | Correct. Proof for this pillar is people, not a case. |
| Our advisors | Text link | `a.more` | Fine. |
| Expertise sentence | Prose + text link | `.one-line` | Fine. |

CEO Advisory on this hub is a full section with the same heading class as Growth Strategy and Activation (`h2.plain`). It is not greyed. It is quieter only because it holds people instead of six offer cards. That matches the IA.

### 2.5 Growth Strategy (`/services/growth-strategy/`)

[https://temp-manifesto-ia.pages.dev/services/growth-strategy/](https://temp-manifesto-ia.pages.dev/services/growth-strategy/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Hero | Service hero: H1, definition, who-for, action pair | `.hero` | No `.aka` (not a renamed deck term). Fine. |
| Why situations | Static problem lines, not links | `ul.situations li` (no `<a>`) | **Same class as hub situations, different behaviour.** Hub rows navigate. These do not. |
| What we do / North Star set | Prose sections | `.prose` | Fine as content. Not a named "framework list" module. |
| Proof | Case cards | `.card` + `.ph` | Fine. Same two clients as almost every service page. |
| CIVD | Framework diagram + H3s | `.civd-grid` | Cells look like metrics and like offer cards. |
| Related expertise | Theme tags | `.page-tags a` | Looks like `.filter`. Job is navigate-to-theme, not filter. |
| Related services | Offer cards | `.card.offer` | Fine. |
| Related thinking | Link list | `ul.list` | Same content type as Thinking cards on Home, different visual. |

Missing vs T3: People block, FAQ, numbers line (deck gives none: correct to omit).

### 2.6 Activation (`/services/activation/`)

[https://temp-manifesto-ia.pages.dev/services/activation/](https://temp-manifesto-ia.pages.dev/services/activation/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Which of the six | Decision **link list** | `ul.list a` | Correct module for chooser copy. |
| The six Activation services | The **same six destinations as Offer cards** | `.card.offer` | **Duplicate.** List rows and offer cards say the same thing twice. Pick one module for the chooser, one for the catalogue, or make the difference explicit (chooser = problem line; card = capability summary). Right now they repeat the problem line on the card. |

### 2.7 CEO Advisory (`/services/ceo-advisory/`)

[https://temp-manifesto-ia.pages.dev/services/ceo-advisory/](https://temp-manifesto-ia.pages.dev/services/ceo-advisory/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Hero CTA | Primary action, different label | `a.btn` "Arrange a conversation" | Correct product CTA. Closing band below still says button "Contact" under heading "Arrange a conversation". Mixed. |
| Side-by-Side | Prose section, named product | `#side-by-side` | Full weight. Not a grey box. Pass. |
| Our advisors | Person cards | `.card.person` + `#advisors` | Full weight. Pass. |
| How the retainer works | Prose | `.prose` | Fine. |

No greying. Same `.hero h1` size as Growth Strategy. Pass.

### 2.8 Work listing (`/work/`)

[https://temp-manifesto-ia.pages.dev/work/](https://temp-manifesto-ia.pages.dev/work/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Featured case | Case card | `.card` + `.ph` | Fine. |
| Quote | Quote | `.quote` | Fine. |
| Service filters | Filter chips | `span.filter` | Look like tags. Are not links, not buttons, not inputs. `.filter.on` is "selected" with no accessible state. |
| More filters | Group label + more chips | `.wf-label` + `.filter` | Expertise and sector chips look identical to service chips. IA wants them behind a control; here they are always visible. |
| Results | Case cards | `.card` + `.ph` | Span text is a service name, not a result line (Home uses result line). Same card, different subtitle job. |
| Pagination | Page index | `.pagination span` | Not links. `.on` marks current. |
| Empty state | Always-on stub | `.empty-state` + `a.btn` "Clear filters" | Button-link used for a filter action. Stub sits under real results. |
| Related thinking | Link list | `ul.list` | Fine. |
| Closing secondary | "See our work" on the work page | `a.text` | Dead-end secondary. |

### 2.9 Thinking listing (`/insights/`)

[https://temp-manifesto-ia.pages.dev/insights/](https://temp-manifesto-ia.pages.dev/insights/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Report | Thinking card (document) | `.card` + `.doc` | Correct. |
| Type filters | Filter chips | `span.filter` | Same look as Work. |
| Article | Intended thinking card | `.card.offer` | **Collision again.** Article uses the Offer skin. |
| Events | Link list | `ul.list` | Fine. |
| Related services | Text links | `.row-links` | Same class as Home theme names. Here the links are What we do / Expertise / Our work, not themes. |

### 2.10 Contact (`/contact/`)

[https://temp-manifesto-ia.pages.dev/contact/](https://temp-manifesto-ia.pages.dev/contact/)

| Unit | What it currently is | CSS | Problem |
|---|---|---|---|
| Work with us / Work for us | Form blocks | `.form` | Split is correct (MURAL). |
| Fields | Unspecified inputs | `.field .box` | No type, required, or error. |
| Send | Primary action as link | `a.btn` | Same class as header Contact and cookie Accept. |
| Direct contact / Nutshell | Prose + text links | `.prose a` | Fine. |

No closing CTA band (unlike most pages). Fine for a form page; not noted.

### 2.11 Catalogue (`/catalogue/`)

[https://temp-manifesto-ia.pages.dev/catalogue/](https://temp-manifesto-ia.pages.dev/catalogue/) (wireframe only)

Before this pass: grouped as "Cards" and "Triangle blocks" with labels "Service cards", "Stats", "Page tags". That inventory is why Gary cannot see what the units **are**. This pass adds proposed names on the catalogue only. See section 3.

### 2.12 Collisions, summarised

**Same look, different jobs**

1. **Grey filled rectangle** = Offer card (service) = Article on Home and Thinking = Role card on Careers = Theme card on Expertise = CIVD cell (diagram) = compact CIVD on the hub.
2. **Small bordered pill** = Theme tag (navigate) = Filter chip (toggle, inert) = Sidebar working-note chip (annotation, not live).
3. **Bordered tile with title + line** = Pillar tile (`.tri a`) = Offer card (`.card.offer`) = Metric (`.metric`) = CIVD cell.
4. **Solid outline control** = Header Contact = Hero Contact = Form Send = Cookie Accept = Empty-state Clear = 404 Search. All `a.btn`.
5. **Underlined small link** = Secondary CTA (`.text`) = More link (`.more`) = Case line = Footer Go = Mega-row.

**Same job, different looks**

1. **Go to a thinking item**: document card on Home/Reports; offer-skin card on Articles; list row on service "Related thinking".
2. **Go to a service**: pillar tile, offer card, situation link, list row ("which of the six"), footer link, mega-nav strand.
3. **Primary action**: Contact, Arrange a conversation, Work for us, Send, Accept, Clear filters, Search. One skin, many verbs, always an `<a>`.

Gary's "cards vs random boxes" is this list. The boxes are not random; they are un-named.

---

## 3. Proposed module system

A designer/dev set. Twelve named modules, plus a short specialist list. Full anatomy, link-vs-button, and CSS map: [`docs/module-system.md`](module-system.md).

Rename away from "chip" and "block" in UI copy. Keep `.block` as the CSS section wrapper if useful, but never as a stakeholder name.

### 3.1 The twelve

| Name | Purpose | Anatomy | Link or button | Card, row, or section |
|---|---|---|---|---|
| **Page hero** | Where am I, is this for me, what next | Eyebrow (optional), H1, strapline, who-for, optional metric set, action pair | Button = primary action. Text link = secondary. | Section |
| **Pillar tile** | Enter one of the three triangle offers | Title + pillar line. Three equal ink. | Whole tile is a **link**. Never a button. | Tile (not a card) |
| **Offer card** | Enter one buyable service | Title + one-line summary. No image. | Whole card is a **link**. | Card |
| **Case card** | Enter one engagement | Image slot, client, result line, optional one service name | Whole card is a **link**. | Card |
| **Thinking card** | Enter one report or article | Report: document slot + title + type. Article: title + meta. Never the Offer skin. | Whole card is a **link**. | Card |
| **Person card** | Enter one profile | Avatar, name, role line | Whole card is a **link**. Only for a person. | Card |
| **Situation row** | Problem entry | One line the prospect would say | **Link** on hubs. Static line on a service Why. Same family, two modes, labelled. | List row |
| **Chooser row** | Pick among siblings | Title + problem line | **Link**. Use this instead of repeating Offer cards. | List row |
| **Theme tag** | Cross-link one expertise (or service on a case) | Short label, max three visible | **Link**. Not a filter. Not a button. | Tag |
| **Filter chip** | Narrow a listing | Label, on/off, optional More filters | **Button** (toggle) in production. Not a link. | Chip (control) |
| **Quote** | Attributed proof | Quote + cite | Not clickable (cite may link the case). | Block |
| **Action pair** | Do the next thing | Primary + secondary | **Primary = button** (or button-styled link only when the target is a page: Contact). **Secondary = text link.** | Pair |

### 3.2 Specialists (do not inflate the core set)

Logo strip, Video frame, Metric set, CIVD frame, Form, Empty state, Pagination, Cookie bar, Closing band. Each is one job. CIVD and Metric are **diagram / number boxes**, never cards.

### 3.3 Link vs button (non-negotiable)

| Use a **button** (or button-styled control) | Use a **link** |
|---|---|
| Submit a form | Go to a page or in-page anchor |
| Accept cookies | Nav, footer, breadcrumbs, tags |
| Toggle or clear a filter | Whole-card destinations |
| | Secondary CTA ("See our work", "What we do") |

If it has a URL and does not change data, it is a link. If it commits, toggles, or submits, it is a button. The current `.btn` class may stay as a visual skin for the Contact page-link. Call it **Primary action** in the legend, and mark on the catalogue whether this instance is "page link" or "true button".

### 3.4 Card vs box vs row

- **Card**: a destination with a title, optional media, optional summary. Four cards only: Offer, Case, Thinking, Person.
- **Tile**: the triangle cell. Same weight for all three pillars. Not an Offer card.
- **Box**: CIVD cell, metric, logo placeholder. Not clickable unless the spec says so (logo to case).
- **Row**: situation, chooser, related-thinking list, footer list.
- **Section**: hero, pillar section, prose, closing.

"More work" on Home is not a Case card. "Our people" on About is not a Person card. Expertise themes are not Offer cards. Jobs are not Offer cards. Articles are not Offer cards.

### 3.5 CSS map (current to proposed)

| Proposed name | Current classes |
|---|---|
| Page hero | `.block.hero`, `.eyebrow`, `.who`, `.aka` |
| Pillar tile | `.tri a` |
| Offer card | `.card.offer`, `.card.flat` |
| Case card | `.card` + `.ph` |
| Thinking card | `.card` + `.doc` (report); article currently `.card.offer` (wrong) |
| Person card | `.card.person` |
| Situation row | `.situations li` |
| Chooser row | `.list li` on Activation "Which of the six" |
| Theme tag | `.page-tags a` |
| Filter chip | `.filter`, `.filter.on`, `.filter.more` |
| Quote | `.quote` |
| Action pair | `.cta .btn`, `.cta .text`, `.closing` |
| More link (fold into Action pair secondary) | `.more` |
| Logo strip | `.logos`, `.logo-ph` |
| Video frame | `.video-ph` |
| Metric set | `.metrics`, `.metric` (also `.numbers`, unused on live pages) |
| CIVD frame | `.civd-grid`, `.civd-cell` |
| Form | `.form`, `.field`, `.box` |
| Empty state | `.empty-state` |
| Pagination | `.pagination` |
| Cookie bar | `.cookie-bar` |
| Mega-nav hub / strand | `.pillar-hub`, `small`, `.strand-overview` |
| Working note (not a live module) | `.chip`, `.ia-chips` |

Stop calling working notes "Modules" in the sidebar.

---

## 4. Missed inputs

Diff of live wireframe + sitemap against Andy's deck, 7 Sep Otter, MURAL keep/drop, and the v7 IA report. Status: **missing**, **diluted**, **contradicted**, or **present**.

### 4.1 Andy's Growth Architecture Services deck

Source: uploaded deck extract; `docs/andy-deck-coverage.md`; live service pages.

| Deck element | Status on live wireframe | Evidence |
|---|---|---|
| Whole offer named Growth Architecture Services | **Present** | Hub H1 "Our Growth Architecture", eyebrow "What we do". |
| Triangle of three pillars | **Present** | Home `.tri`, hub `.tri`, mega-nav `.mega-cols`. Order is GS, Activation, CEO (Otter), not deck's CEO-on-top. Deliberate. |
| Positioning line and strapline | **Present** | Home H1 and strapline. |
| Triangle logic in one line | **Present** | `.tri-line` "Strategy first. Activation to deliver it. Advisors alongside." |
| Six Activation services + Proposition Innovation + Side-by-Side | **Present** | Mega-nav and hub cards. Deck names (Customer Intelligence, Data Agents, Operating Architecture) appear as `.aka` on those three pages. |
| Side-by-Side retainer model | **Present** | `/services/ceo-advisory/#side-by-side`. SxS not used. Pass. |
| Advisor profiles as the offer's proof | **Present** | `#advisors` person cards. |
| CIVD | **Present** | Hub compact + `/services/growth-strategy/#civd`. Not in the nav. Pass. |
| North Star, growth priorities, demand signals, scenario planning | **Present** | Growth Strategy H2s. Copy is stub. |
| Customer Intelligence: So What, Insight Projects, Intelligence Capabilities, six inputs | **Present, diluted** | "so-what arrives too late" in Why. Research projects + six H3s. Always-on / VoC is thin. |
| Experience Engineering: Find, Redesign, Test, Scale; 3x EBITDA; CX / digital / research | **Present** | H2s Find, Redesign, Test, Scale; `.metric` 3x; three anchored sections. |
| Experience Engineering Squads | **Missing** | No squad / team-composition line. Deck is explicit. |
| Data Agents timeline 4 / 6 weeks | **Present** | Hero metrics. |
| AgentLab four groups | **Present** | `#agentlab` H3s. |
| Twelve named agents as a catalogue | **Diluted** | Groups name the agents in a sentence. Not twelve scannable entries as the deck lists them. |
| Operating Architecture qualities + appendix diagram | **Diluted** | Qualities in prose. Framework is three H3s, not a captioned figure with value streams / human+AI. |
| Growth Office: Culture, Capability, Value; interim then embed | **Present** | Those H2s. |
| AI Enablement: three programmes + maturity | **Present** | Three H2s + how it works. |
| "AI practitioners from our expert network" | **Present, thin** | One sentence on AI Enablement. Team Associates group is still optional/stub. |
| Example logos per service (Mars, BBC, Dayinsure, PEX, …) | **Missing / contradicted** | Almost every Proof block shows Dayinsure and Key Group, including pages the deck ties to other clients. No per-service logo-list fallback when the case is the wrong client. |
| "including c&n" on AI Enablement examples | **Missing on that page** | Stub lives on About as "C and N members", not on AI Enablement. Still an open client question. |
| "Growth Architects" as the people term | **Diluted** | Role title on Careers. Not used as the team name on `/about/team/`. Optional in v5; still unused. |

Deliberate departures (do not treat as misses): CEO Advisory third, not top; deck labels not in the nav; AgentLab not a URL; no extra mega-nav one-liners.

### 4.2 Otter (7 September check-in)

| Otter point | Status | Evidence |
|---|---|---|
| Deck is packaged services, not the whole firm | **Present** | Expertise, work, thinking, about sit outside the triangle. |
| Do not design the whole site around CEO Advisory; lead GS then Activation; advisory may live outside the menu | **Contradicted by later IA, on purpose** | Live site puts CEO Advisory in the mega-nav at full ink (v7 / D-57). Otter's "bolt on the end / secondary / maybe outside What we do" is not the current rule. **Keep the later rule.** Do not grey it to honour a superseded line. |
| Showcase heavyweight advisor profiles | **Diluted** | Three identical "Advisor name" cards. Structure is right; content is not yet heavyweight. |
| Event pushed to October | **Missing as a named item** | Thinking has Events and news, but no CEO Advisory event line. |
| Experience Engineering must map to CX / website | **Present** | Strand subtitle "Customer experience and websites"; page H2s. |
| Growth Office terminology is hard | **Present** | Subtitle "Interim growth team"; page uses interim CMO where needed. |
| Deck is not website copy; plain language in the nav | **Present** | Renames + subtitles. |
| Sector-agnostic services; light sector landings; no sector POV | **Present** | Footer + `/sectors/{…}/`. No `/sectors/` index. |
| Themes = expertise story, not FS-who-do-loyalty | **Present** | `/expertise/` hub and Home text links. |
| Rebuild should originate, not only reassure after referral | **Present as intent** | Home still leads with positioning, then triangle. Origination depends on copy and proof, still stubbed. |
| Simplification + cross-reference without confusion | **Diluted** | Cross-reference exists (tags, related cards, lists) but three visuals compete. This is the module problem, not a missing page. |

### 4.3 MURAL keep / drop (`docs/mural-gap-check.md`)

| MURAL item | Status | Evidence |
|---|---|---|
| Six-item chrome, Our thinking, Careers first-class | **Present** | Header. (Sitemap doc line about Careers is stale.) |
| Trusted partners high | **Present** | Home, before What we do. |
| FT / awards not at the top; not on Contact | **Present** | Awards below work. Contact has no awards. |
| No homepage reports grid | **Present** | One report + one article, not a grid. |
| Showreel at launch | **Present** | `.video-ph` in Home hero. |
| Quotes with work | **Present** | Home, Work featured, case result. |
| Case studies pulled up; tagging | **Present** | Work featured + filters (inert). |
| Reports at top of thinking; blogs merged; no PDFs | **Present** | `/insights/` H2 order. Report expands on the page. |
| Events + Nutshell | **Present** | `#events`, newsletter utility. |
| Origins; how we are distinct | **Present** | About. |
| Life at Manifesto on Careers, not duplicated as a section on About | **Present** | Careers owns it. |
| C and N members | **Present as stub** | About H3. |
| Growth partner videos on Our approach | **Present** | `/about/how-we-work/` video placeholder. |
| CIVD keep, new visuals; strategy not Side-by-Side | **Present** | Growth Strategy only. |
| Split Work with us / Work for us | **Present** | Contact `#work-with-us` / `#work-for-us`. |
| Email Mark as one tracked route | **Diluted** | Sidebar chip on Contact only. Not on-canvas. |
| Trusted partner logos link only if a case exists | **Missing** | Logos are dead placeholders. Dayinsure / Key Group are the only cases; those logos are not wired. |
| About client logo wall | **Missing** | T11 block 6. About has no `.logos` section. |
| Values and careers teaser on About | **Diluted** | Approach paragraph links values; no careers teaser block. Closing is the generic Contact pair. |
| Old seven-item sitemap / Our clients top-level / Our blog / Growth Collective in header | **Correctly out** | Do not add. |
| Homepage reports grid / FT in hero / PDFs | **Correctly out** | Do not add. |

### 4.4 v7 IA report vs live

The live site is largely the v7 model. Gaps are template fidelity and wireframe craft, not a different IA.

| v7 requirement | Status | Evidence |
|---|---|---|
| Six header items; What we do is the only mega-nav | **Present** | Header. |
| Strand subtitles on every item | **Present** | Mega-nav `<small>`. |
| CEO Advisory full ink, width-only quieting | **Present** | `.mega-cols` `0.85fr`. |
| CIVD on-page, not nav | **Present** | |
| Catalogue wireframe-only | **Present** | |
| Home module order (partners, triangle, thinking, work, awards, themes, close) | **Present** | |
| Hub: situations + three pillar sections | **Present** | |
| Service: Why with three situations; proof under the offer; numbers where the deck gives a figure | **Diluted** | Why is present. Proof often sits **before** What we do (Experience Engineering has no What we do; Proof then Find). Numbers use `.metrics` not `.numbers`. |
| People block when a lead is flagged | **Missing** | No service page audited shows a People module. |
| FAQ (editorial) | **Missing** | No FAQ on service pages. |
| Related expertise: tags with one line on the intersection | **Diluted** | Tags only, no intersection line. |
| Work: Service filter open; Expertise/Sector behind More filters | **Diluted** | More filters are a label; the second row is always open. Filters do not work. Empty state always visible. |
| Thinking: type filter; reports at top | **Present, mixed** | Reports are a separate section (MURAL), then Articles with type filters. Slightly different from T9 "Latest then one filter group". Acceptable if named. |
| Case: video snippet if it applies | **Present** | Dayinsure `.video-ph` "Film". |
| Expertise hub: cards with counts | **Diluted** | Offer cards saying "Cases and thinking", no counts. |
| How we work: five named frameworks | **Present** | |
| Contact two forms | **Present** | |
| Search, 404, legal, Nutshell | **Present** | |
| Primary CTA Contact; Careers routes Work for us; CEO Arrange a conversation | **Mostly present** | CEO hero is right; CEO closing button still says Contact. |

### 4.5 Wireframe-only extras (keep out of the live site brief)

These help reviewers. They must not ship.

| Extra | Where | Live-brief rule |
|---|---|---|
| `/catalogue/` | Catalogue, sitemap Wireframe tools | Not a client URL. No header/footer link. |
| Sidebar working notes and heading map | `.sidebar` on most pages | Annotation. Not page tags. Do not design "chips" into the live page because the sidebar used that word. |
| Always-on empty state stubs | Work, Thinking, Search | Teach as a **state**, not a section. |
| `.wf-label` ("Empty state", "More filters") | Inside `main` | Wireframe label. Not copy. |
| `sitemap.html` All pages | Wireframe tool | Not a live IA page (XML sitemap is separate). |
| Repeated Dayinsure / Key Group on every Proof | Service templates | Placeholder. Live proof must follow tags / deck examples. |
| "TBC" metrics | Case at-a-glance | Placeholder. |
| Duplicate Activation chooser (list + the same lines as cards) | Activation | Pick the module; do not ship both as-is. |
| Home "More work" fake case card | Home | Use All work text link only. |
| About "Our people" person card | About leadership | Use a text link, not a fake person. |

---

## 5. Opportunities (next passes only)

Highest leverage, ranked. Clarity of modules and wireframe craft over new IA. Maximum eight.

1. **Adopt the twelve-module legend on the catalogue, then on one hub.** Names, link-vs-button, card-vs-box. Stop saying "chips" and "blocks" to stakeholders. This pass starts the catalogue. Next: label units on Home and `/services/` only.

2. **Give each card one skin and one job.** Offer, Case, Thinking, Person. Stop using `.card.offer` for articles, jobs, and expertise themes. Stop using Case card for "More work". Stop using Person card for "Our people".

3. **Codify Primary action vs text link vs filter vs tag.** Four true buttons in production: form submit, cookie accept, filter toggle, filter clear. Contact in the header may stay a button-styled **link**. Draw that on the catalogue until every `.btn` on a page is labelled "page link" or "button".

4. **Make listing controls real, and empty a state.** Work and Thinking filters should look like controls, sit in one open group, and hide the empty module until the grid is empty. Pagination should be links.

5. **On-canvas page purpose + module labels; retitle sidebar notes.** One line above the hero: "Purpose: …". Sidebar heading "Working notes", never "Modules". Move `.wf-label` to a style that cannot be confused with live copy.

6. **Restore the missing T3/T11 blocks that sources already asked for.** Service People (when a lead exists), FAQ stub, About client logo wall, per-service proof that is not always Dayinsure/Key Group (logo list fallback). AgentLab as twelve entries. Operating Architecture as a captioned figure. Named October CEO Advisory event under Events if the date still holds.

7. **Activation chooser: one module.** Keep "Which of the six" as Chooser rows. Offer cards can stay as a compact catalogue **or** go. Do not repeat the same sentence in both.

8. **Add a mobile frame of the header + What we do, and a one-page state sheet.** 720px hamburger, stacked triangle, open mega-nav, form error, filter empty. No new pages. Without this, design will invent mobile IA.

Out of scope for the next pass: new services, sectors in the header, greying CEO Advisory, renaming the triangle for keyword volume, a live `/catalogue/` URL.

---

## 6. How to use this review

1. Read [`docs/module-system.md`](module-system.md) as the build contract.
2. Open the catalogue and check that each sample is labelled `MODULE:` and `ACTION:`.
3. Do not restyle the site until those names are agreed.
4. When you do restyle, change CSS class names toward the proposed names, or map them 1:1 in the front-end, but do not invent a thirteenth card type.

Independent of v7: the sitemap and nav can stand. The wireframe cannot yet stand as a specification of components. Gary's three sentences are the brief for the next craft pass.
