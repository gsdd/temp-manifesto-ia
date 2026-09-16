# Fresh wireframe review

**Manifesto Growth Architects**  
Independent IA / wireframe pass against the live clickable site and the source pack.  
Live site reviewed: https://temp-manifesto-ia.pages.dev/  
Sources: client report v7, Andy's Growth Architecture deck, 7 Sep Otter, MURAL keep/drop, in-repo `docs/` and `mocks/`.

This is not a defence of prior work. The IA hierarchy is treated as agreed. The review asks whether the wireframe is a clear handoff of that IA, and whether page modules are named units a designer or developer could implement without guessing.

**Verdict.** The sitemap, mega-nav, and page list match v7. Gary's four concerns are real. The catalogue names modules. The live pages do not. Boxes of similar weight are used for cards, filters, tags, metrics, CIVD cells, logos, and triangle tiles. Almost every control is an `<a>`. Filters and pagination are `<span>`s that look like buttons. That is the main handoff gap. Do not add top-nav items. Fix the unit language first.

---

## How this was tested

Walked the live site: Home, What we do mega-nav, Our thinking and About dropdowns, services hub, all service pages, expertise hub and Loyalty, Financial services, Our work, Dayinsure, Our thinking, Pricing Paradox, article, About, Our people, Our approach, Careers, Contact, thank-you, catalogue, search, 404, legal stubs, newsletter, sitemap. Desktop plus a 375px pass on Home, Contact, and catalogue.

**Evidence**

- Live URLs cited below are on https://temp-manifesto-ia.pages.dev/ unless noted.
- Repo checked as generated HTML from `mocks/_build.py` plus `mocks/assets/wireframe.css`.
- Source claims are tied to a named sticky, slide, or v7 section, not to taste.

---

## Gary's four hypotheses

Tested as primary, not as optional colour.

| Hypothesis | Result | Where it shows |
|---|---|---|
| Modules are not clear | Confirmed | Catalogue at `/catalogue/` names units. In-page modules have no labels. Home triangle tiles, CIVD cells, metrics, service cards, and awards all read as similar rectangles. |
| Links vs buttons are muddled | Confirmed | Header Contact is `a.btn`. Nav items are text links. Filters on `/work/` and `/insights/` are `<span class="filter">`. Pagination is `<span>`. Cookie Accept is `a.btn` to the policy, not an accept action. Send, Search, and Clear filters are also `a.btn`. |
| Cards vs random boxes | Confirmed | Clickable cards (`.card`, `.tri a`) share a 1px solid box with static CIVD cells, metrics, logo placeholders, and form fields. Home "More work" is a listing link wearing a case card. |
| Need to be focused on what these UI units are | Confirmed | Six interaction types are in use (button, text link, card, tag, filter, static box) but only two visual treatments (outlined box vs underlined text). |

The IA is not the problem. The wireframe does not yet teach the component set.

---

## 1. Wireframe gaps

What a client-handoff wireframe still lacks. These are missing states and annotations, not missing pages.

### Interaction and states

- **No hover, focus, selected, disabled, or loading** on buttons, cards, filters, or links. Filter `.on` is the only selected state, and only one chip is marked on.
- **Forms are boxes, not fields.** `/contact/#work-with-us` has Name, Company, Email, Topic, Message as empty rectangles. No required marker, helper text, focus, error, or success. Topic is a text box. It should be a select fed by `?topic=`. Send is a link to thank-you, not a submit.
- **Empty states are always on the page.** `/work/`, `/insights/`, and `/search/` show results and the empty stub together. The stub is labelled, but a designer can read it as a permanent block. Spec in `docs/03-page-layouts.md` T7/T9: empty is Conditional.
- **Filters do not filter.** `/work/` and `/insights/` look interactive. They do not change the grid or the URL. "More filters" is a caption, not a control that reveals a hidden group.
- **Pagination does not paginate.** Numbered boxes are inert spans. They look like buttons. They should be page links, with the current page as text, not a control.
- **Cookie Accept** (`a.btn` on every page) goes to `/cookie-policy/`. That is a navigation link dressed as an action. Accept should dismiss. Cookie policy should be the text link (already present).
- **Search** at `/search/` and in the footer is a dummy box plus a Go/Search link. No query string, no type-to-filter, no no-results that replaces results.
- **404** at `/404/` exists and routes correctly. No in-page broken-link demo from a real nav item.

### Wireframe craft (type, space, annotation)

- **No type scale.** H1 is 30px, section H2 `.plain` is 22px, uppercase `.sec` is 13px, body 15px. None of that is annotated on the page. A designer has to reverse-engineer CSS.
- **No spacing system.** `.block` uses 36px vertical padding. Card gap is 16px. Header is 64px. Not marked.
- **No grid overlay.** Content is a single padded column. Mega-nav is 3 columns of unequal width (CEO narrower by design, D-57). That rule is invisible unless you read the CSS.
- **No component names on pages.** Catalogue labels (Service card, Case card, CIVD four-cell) disappear in context. Cross-reference is a sidebar link to Page modules, easy to miss.
- **Working notes used "chip" CSS** (`.ia-chips`, `.chip`) for sidebar annotations. Live copy already said Page modules. The leftover word sat in the chrome of the mock, which is exactly where Gary is looking. This PR renames those classes to notes.

### Device and chrome

- **Mobile is a wrap, not a pattern.** At 375px the six-item header plus Contact wraps onto several rows. There is no hamburger, no full-screen mega-nav, no accordion for What we do. Hover mega-nav is a desktop assumption. Touch is unspecified.
- **Touch targets** are not called out. Filter boxes and footer links sit under 44px.
- **Mega-nav** on hover is the right IA. The wireframe does not show a keyboard or mobile equivalent (click-to-pin exists in `nav.js`; it is not annotated).

### Template holes vs v7 / T3

These are wireframe gaps because the template already names the block, and the page does not show it:

- Service **People** block (T3 block 12, Always when a lead is flagged): absent on every `/services/{service}/` page.
- Service **FAQ** (T3 block 13, Editorial, recommended): absent.
- **How it works** is missing on Experience Engineering. Find / Redesign / Test / Scale are four H2s, which is the right content, but they are not framed as the How it works module.
- **Operating Architecture** is H3 copy, not a captioned figure (`#operating-architecture`).
- **AgentLab** groups four buckets as paragraphs. The twelve named agents from the deck are not a scannable catalogue.
- Case study **Team** (T8 block 7) and **Related services as cards** (T8 block 8): absent on `/work/dayinsure/`.
- About **Clients logo wall** (T11 block 6): absent on `/about/`.
- Our approach **What clients say** (T13 block 6): absent.
- Careers **empty roles** stub: only a filled Growth Architect card. T15 asks for "No open roles right now" plus Work for us.
- Associates group on `/about/team/` is a heading and a sentence. No person cards.

None of this needs a new URL.

---

## 2. Module taxonomy

A named set. Six interaction types. One visual rule each. If a rectangle cannot be named from this list, it is a random box.

### Interaction types (use these words)

| Type | Element | Looks like | Does | Never |
|---|---|---|---|---|
| **Button** | `<button>` or submit input. In this grey mock, outlined control `.btn` | 1.5px ink border, 9px 18px padding, weight 600 | An action: Send, Subscribe, Accept, Clear filters, Search submit | Navigate to a content page |
| **Text link** | `<a>` with underline | Underlined, no box | Navigate: See our work, All thinking, situations, row-links, footer, breadcrumbs | Primary enquire action |
| **Card** | `<a class="card …">` whole card is the hit area | Solid box, title + support line, optional image / doc / avatar | One destination page (service, case, report, article, person, role, theme) | Toggle a filter; hold a statistic; hold CIVD |
| **Tag** | `<a>` inside `.page-tags` | Small outlined label | Jump to the one allowed dimension (expertise on services; service on cases) | Filter a listing; look like a button |
| **Filter** | `<button type="button" class="filter">` | Control, selected = `.on` | Toggle a listing. Updates query string | Navigate away; sit in a hero |
| **Static box** | `<div>` / `<span>`, not a link | Dashed box (placeholder or diagram) | Hold a logo, metric, CIVD cell, form field, video, empty message | Be clickable |

Header Contact is the one chrome exception: it is a **Button** that goes to `/contact/`. v7 already specifies that. Do not turn other nav items into buttons.

### Named modules

For each: purpose, shape in this wireframe, when to use which interaction type.

#### Chrome

| Module | Purpose | Shape | Interaction |
|---|---|---|---|
| **Site header** | Six items plus logo and Contact | 64px bar, text links, one Contact button | Links in the bar. Contact = Button |
| **Mega-nav panel** | Triangle laid flat | Three columns, CEO narrower, footer row | Hub headings and strands are **Text links**. Not cards |
| **Dropdown** | Our thinking / About | Small list under the label | Text links |
| **Breadcrumb** | Wayfinding except Home | `Home > …` mid grey | Ancestors are text links. Current page is text |
| **Cookie bar** | Notice | Bar above footer | Policy = text link. Accept = Button (dismiss) |
| **Footer** | Services, expertise, sectors, company, legal, search | Four columns + bottom row | Text links. Footer search Go is a Button |

#### Heroes and bands

| Module | Purpose | Shape | Interaction |
|---|---|---|---|
| **Hero** | Where am I, is this for me | H1, optional eyebrow / aka / who-for, optional numbers, CTA pair | Primary Button (Contact or Arrange a conversation). Secondary Text link (What we do / See our work) |
| **Numbers line** | Deck figure, only where Source B gives one | One line, or a row of **Metric boxes** | Static. EE 3x EBITDA; AI Agents 4 wks / 6 wks |
| **Closing CTA band** | Last enquire | Sentence + Button + Text link | Same pair as the hero. Careers uses Work for us |
| **Eyebrow** | Nav label above a different H1 | Small caps | Static. Used on `/services/` ("What we do" above "Our Growth Architecture") |

#### Cards (clickable content units)

| Module | Purpose | Shape | Use on |
|---|---|---|---|
| **Service card** | Buyable service | Grey fill, title + one line, no image. Class `card offer` | Hub pillars, related services, Activation six |
| **Theme card** | Expertise problem | Same shape as Service card | `/expertise/` only. Do not put themes in the mega-nav |
| **Case card** | Proof | Image 16:10 placeholder, client, one-line result. Optional one service tag on listing cards | Home, work hub, service Proof, sector, theme |
| **Report card** | Long-form thinking | Portrait "Report" placeholder, title, type | Home thinking, `/insights/#reports` |
| **Article card** | Short thinking | Title + type line, no grey fill, no image. Class `card article` | Home thinking side, `/insights/#articles` |
| **Person card** | Someone | Circle avatar, name, one line | Advisors, leadership, joiners |
| **Role card** | Job | Same shape as Service card | `/careers/` open roles |
| **Triangle tile** | Pillar, not a service | Three equal (Home) or width-quiet (mega-nav / hub) solid tiles. Class `.tri a` | Home What we do; hub Three ways. Links to pillar pages or in-page anchors. Not a Service card |

#### Lists and locators

| Module | Purpose | Shape | Interaction |
|---|---|---|---|
| **Situations list** | Prospect language in | Two-column text list, one line each | Text links on the hub. On a service page the three "You are here if" lines are **static** (they describe this page) |
| **Row of text links** | Names only | Horizontal text | Home "Growth problems we know best". Not cards, not tags |
| **Related list** | Compact related thinking / search hits | Title left, type right | Text links. Not cards |
| **Case line** | One proof under a pillar | One sentence + Read the case study | Text link. Not a Case card |
| **Filter bar** | Narrow a listing | One group open; More filters reveals the rest | Filter buttons. Active filters as removable tags above the grid (specified, not drawn) |
| **Pagination** | Next page of results | Current page as text; others as links | Links, not buttons |
| **Empty state** | No results for this query / filter | Dashed box, message, Clear filters Button | Conditional. Replace the grid. Do not sit under it |

#### Proof and media (mostly static)

| Module | Purpose | Shape | Interaction |
|---|---|---|---|
| **Logo strip** | Trusted partners / awards / sector clients | Dashed logo placeholders in a row | Static unless a case exists, then the logo is a link to that case (MURAL). Do not imply a case for Disney-style logos |
| **Quote** | Testimonial | Left rule, quote, cite | Static. Lives with work, not as a testimonials page |
| **Video 16:9** | Showreel, partner film, case film | Dashed 16:9 | Static placeholder. Film later |
| **Metric box** | A number | Dashed cell, big figure, caption | Static. At a glance; hero numbers |
| **CIVD four-cell** | Growth Strategy frame | Four dashed cells, then optional paragraphs | Static diagram. Link "Open the CIVD module" is a text link beside it, not the cells |
| **Operating Architecture figure** | Adaptive model | Captioned figure (not yet drawn) | Static. Caption links Orchestration to Growth Office |
| **AgentLab catalogue** | Named agents | Grouped list of entries, not pages | Static entries. Not nav items |
| **Phase row** | Named how-it-works | Find / Redesign / Test / Scale; 4 wks / 6 wks; interim then embed | Static process. Can be four short static boxes, not cards |

#### Forms

| Module | Purpose | Fields | Interaction |
|---|---|---|---|
| **Work with us** | Client enquire | Name, Company, Email, Topic (select), Message | Submit Button. Topic from `?topic=` |
| **Work for us** | Speculative hire | Name, Email, Message | Submit Button. Roles stay on Careers |
| **Newsletter (The Nutshell)** | Email sign-up | Email | Subscribe Button |
| **Report email gate** | Optional copy of a report | Email | Button. Report still readable on the page (no PDF) |
| **Search field** | Find a page | Query | Search Button. Results as Related list. Empty replaces results |

Show, at least on the catalogue: default, focus, error (invalid email), disabled submit.

#### On-page tags vs filters vs chips

- **Page tag:** one dimension, max three, linked. Service pages show expertise. Cases show services. Insights show expertise. Sectors are never tags (v7 / T3 rule).
- **Filter:** listing control. Service group open on `/work/`. Type open on `/insights/`. Expertise and Sector behind More filters.
- **Chip:** do not use this word in UI copy or in live module names. Sidebar working notes are annotations, not modules.

### Current "random boxes" (live)

Places that look like a unit but are not named, or use the wrong unit.

| Live place | What it looks like | What it should be |
|---|---|---|
| Home Trusted partners | Eight grey rectangles | Logo strip (static), optional link per logo if a case exists |
| Home What we do three tiles | Three cards | Triangle tiles, not Service cards |
| Home Our thinking article | Grey Service card | Article card |
| Home "More work" | Third Case card | Text link "All work" (already under the quote). Do not duplicate as a fake case |
| Home Awards | Three grey rectangles | Logo strip, award variant. FT lives here, not in the hero |
| Hub CIVD four-cell | Four Service-card lookalikes | Static CIVD cells |
| Hub Activation six | Service cards (correct) next to triangle tiles (different) | Keep both. Name them |
| Hub advisor row | Person cards (correct) | Keep. Name them |
| `/work/` filter row 1 vs row 2 | Same job, mixed caption vs boxes | One Filter bar |
| `/work/` pagination | Button-like spans | Pagination links |
| `/work/` empty state | A section under results | Conditional stub |
| Service Related expertise | Small boxes that look like filters | Tags |
| Service Related services | Grey cards | Service cards (correct) |
| Service Related thinking | List (correct) | Related list. Do not make these cards |
| `/work/dayinsure/` At a glance | Four boxes | Metric boxes, static |
| `/catalogue/` itself | Labels exist, no interaction type | This PR adds type badges |

---

## 3. Missed inputs

Checked against the attached pack and in-repo docs. Represented means a visitor can see the idea on the live page, even as a stub. Not represented means the source item has no on-page home.

### Represented (do not reopen)

- Six-item chrome; What we do is the only mega-nav; Careers first-class; Contact as button. v7 §2, MURAL.
- Triangle order Growth Strategy, Activation, CEO Advisory. Otter: do not design the site around advisory. CEO uses the same ink, narrower column only (D-57).
- Strand subtitles and Overview rows (D-58, D-54).
- Hub H1 Our Growth Architecture; seven situations; pillar sentences; compact CIVD on the hub. v7 §5, deck slides 1 to 3.
- CIVD on Growth Strategy, not in the nav. MURAL keep, deck slide 5.
- Side-by-Side named, SxS unused. Deck slide 4, D-31.
- Activation "Which of the six do you need?". v5 R5.
- Find / Redesign / Test / Scale copy on Experience Engineering. Deck slide 8.
- AgentLab as an on-page H2, not a nav item. Deck slide 9, D-15.
- Light sector landings, no `/sectors/` index. Otter: sectors are proof.
- Our thinking label, `/insights/` URL, reports above articles, no PDFs. MURAL.
- Work with us / Work for us split. MURAL, v7.
- The Nutshell named. MURAL.
- Trusted partners high; FT not in the hero. MURAL.
- Growth partner videos on Our approach, not Home. MURAL.
- C and N as a labelled stub on About and Our people. Open decision, default followed.
- Open decisions left open: Growth Collective off the header; Events as a section not a URL.

### Not represented, or only in the sidebar

| Source | Item | Live gap |
|---|---|---|
| Deck slide 9 | Twelve named agents as catalogue **entries** | `/services/ai-agents-for-marketing/#agentlab` lists four group paragraphs. Names are buried in the sentence, not entries |
| Deck appendix | Adaptive operating model **figure** (value streams, AI-agent / Human) | `/services/operating-model-design/#operating-architecture` is three H3s. No captioned figure |
| Deck slides 7 to 12 | Example **client logos per service** (Mars, BBC, Dayinsure, PEX, …) | Proof is always the same two Case cards (Dayinsure, Key Group). Logo-list fallback when no tagged case (T3) is not shown |
| Deck slide 12 | "including c&n" on AI Enablement examples | Stub is on `/about/` and `/about/team/`, not on `/services/ai-enablement/` |
| v7 T3 / layouts | People block on service pages | No lead profiles on any service page |
| v7 T3 | FAQ module | None |
| v7 T3 | Numbers as "one line of figures" | EE and AI Agents use Metric boxes (acceptable) but Growth Strategy still has none, correctly. The `.numbers` one-line treatment in CSS is unused |
| v7 T8 | Case: related services as cards; team; optional film is there | `/work/dayinsure/` has film. No team. No related service cards |
| v7 T11 | About clients logo wall | `/about/` skips it |
| v7 T13 | What clients say on Our approach | `/about/how-we-work/` has principles, shapes, frameworks, AI. No quotes |
| v7 T15 | Empty roles state | `/careers/` only shows a filled Role card |
| v7 T7 | Active filters as removable chips above the grid | Not drawn on `/work/` |
| v7 T9 | Insights "Latest" featured block before filters | `/insights/` opens on Reports, then Articles with filters. No Latest row |
| Otter | Heavyweight advisor profiles | `/services/ceo-advisory/#advisors` and `/about/team/advisor-one/` are generic "Advisor name / Former role" |
| Otter | CEO Advisory event pushed to October | `/insights/#events` shows Pricing Paradox launch only |
| MURAL | Email Mark as a tracked route | Sidebar note on Contact. Not an on-page control |
| MURAL | Office / studio visuals | Careers hero has a Studio 16:9. Fine as a stub |
| MURAL | Qual and quant evidence | Pointed at Customer Research from Our approach. The methods list is on that service page. Fine |
| Layouts T3 | Situations on service pages are links on the hub, static on the page | Hub `/services/` situations are links (correct). Service-page situations are `<li>` text (correct). They **look** the same as the hub list, so they feel clickable |

### Deliberate absences (keep)

Do not add these as pages or nav items. The sources already decided.

- Growth Collective in the header (open, currently off).
- `/events/` as a first-class URL.
- CIVD, AgentLab, Side-by-Side as top-nav or mega-nav items.
- Sectors in the header.
- Search in the header.
- Homepage reports grid.
- PDF downloads.
- Coaching as the CEO Advisory offer name.

---

## 4. Opportunities (max 8)

Ranked by handoff value. Component clarity over new pages. No new top-nav.

1. **Publish the module taxonomy on `/catalogue/` and keep it honest.** Every live unit with a name, an interaction type badge (Button / Text link / Card / Tag / Filter / Static), and a one-line "when to use". This PR starts that. Designers should be told to implement from that page, not by copying random rectangles.

2. **Make the six interaction types visible in CSS, still grey.** Static boxes dashed. Cards solid. Filters as `<button class="filter">`. Pagination as links. Tags as small links. Buttons only for actions. Article cards must not reuse `card offer` (that is why Home thinking looks like a service).

3. **Stop drawing inert controls as if they work, or annotate the stub.** Filters, pagination, empty states, search, and cookie Accept either need a one-line wireframe note ("stub: hide when results exist") or a tiny bit of behaviour. Empty state under a filled grid is the most misleading.

4. **Put the missing T3/T8/T11 modules on the templates that already own them.** People and FAQ on one canonical service page as a pattern. Team + related service cards on Dayinsure. Clients logo wall on About. Empty roles stub on Careers. One AgentLab as a list of twelve entries. One Operating Architecture as a captioned dashed figure. No new URLs.

5. **Annotate mobile chrome once.** A 375px frame of the header: either a hamburger that opens the six items plus the triangle as an accordion, or a documented wrap. Hover-only mega-nav will fail client review on a phone.

6. **Form states on Contact only.** Required, Topic as select, error on Email, Send as a real Button. Thank-you already exists. This is the enquire path v7 cares about.

7. **Kill leftover "chip" language in the mock chrome.** Sidebar working notes should say notes, not chips. Live labels already say Page modules. Gary is reacting to the word as much as the boxes.

8. **Retire the Home "More work" fake case card.** Home T1 already has three cases plus All work. The third card is a listing link. Use three real cases or two plus the text link. Do not invent a case called More work.

Not in this list on purpose: new nav items, a sectors hub, a redesigned visual language, rewriting strand names.

---

## 5. IA hierarchy check

No rewrite. Evidence did not show a missing top-nav item.

- What we do / Our work / Our thinking / About / Careers / Contact is the cap. Sources agree.
- Expertise and sectors stay out of the header. Correct.
- CEO Advisory stays third and full weight. Correct against Otter plus D-57.
- Catalogue is wireframe-only. Correct.

The miss is modules, not map.

---

## What this PR changes in the mock

Small, grey, taxonomy-only:

- Catalogue rebuilt as the named set above, with interaction-type badges and a "do not mix" row.
- CSS: static cells (CIVD, metrics) dashed; article card class; filters as `<button class="filter">`; pagination as links; leftover `.chip` sidebar classes renamed to notes.
- Home thinking article no longer uses the service-card class.
- Empty states labelled as stubs that hide when results exist.

Not in this PR: new pages, nav changes, FAQ/People on every service, mobile hamburger, brand colour, removing the Home "More work" card (called out as opportunity 8).

Leave this PR open for Gary. The taxonomy pass is small and grey, but it is still a visual change to listing controls and static boxes.
