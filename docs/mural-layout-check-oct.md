# Mural layout check, October pass

**For Bruno.** This is the single change log for the 15 October pass, which folds Manifesto's confirmed Mural page layouts into the wireframes. Everything below is live in `mocks/` and the repo is the source of truth: if this document and a wireframe page disagree, the wireframe wins and this document has a bug.

Each changed page carries a **Client layout (Mural, 15 Oct)** row in its wireframe sidebar listing the client modules used on that page. Every new module is in the Component library at `/catalogue/` under the same names used here.

The decisions behind this pass are D-64 to D-71 in `06-decisions-log.md`. The Mural boards are Source I in `00-sources.md`.

---

## 1. The rename: Growth Office is now Value Orchestration

The client's boards use **Value Orchestration** for the interim growth team service. That retires the old label everywhere: nav strand, mega-nav, Activation hub, page title, H1, every internal link, and every document in this package.

| | Old | New |
|---|---|---|
| Label | Growth Office | Value Orchestration |
| Slug | `/services/growth-office/` | `/services/value-orchestration/` |
| Title tag | Growth Office: interim growth team and programme office | Value Orchestration: interim growth team and programme office |
| Quiet line | Interim growth team | Interim growth team (unchanged) |

At build, the old slug should **301 redirect** to the new one. The old label appears nowhere else in the package; the wireframe build now fails if it reappears in generated HTML. The quiet line stays because the new name is also coined: it has no measured search volume (the retired label polled about 10 a month), so "interim growth team" still carries the search intent on the page. One flag for copywriting: Ekimetrics markets "Customer Value Orchestration"; the labels are distinct but close.

## 2. The taxonomy: one industry list, with Energy added

The client's Mural filters say Finance and CPG and add Energy. The package uses one list for the Work filters, the case study tag pills and the sector landings:

| Mural label | Package label | Landing |
|---|---|---|
| Finance | **Financial services** | `/sectors/financial-services/` |
| CPG | **Consumer** | `/sectors/consumer/` |
| (unchanged) | Media | `/sectors/media/` |
| (unchanged) | Retail | `/sectors/retail/` |
| Energy (new) | **Energy** | `/sectors/energy/` (new light landing) |

Energy follows the same rules as the other four: light weight, noindex until it clears the content threshold, no child pages. The footer's Who we work with column now lists five.

---

## 3. What changed per page

### Case study pages (`/work/dayinsure/`, `/work/key-group/`, and the template)

- **Hero**: eyebrow "Case study", client name as H1, one-line project title, tag pills for service, industry and expertise (each pill links to its matching service, sector or expertise page), main image.
- **Sticky stat rail** on the left: two stat cards and a Contact us button, pinned while the story scrolls.
- **Attributed client testimonial** straight after the hero, beside the stats: quote with name, role and client, plus a film snippet placeholder where one exists.
- Then **The Opportunity**, **The Solution**, **The Impact** (bullets).
- Then **See more of our case studies** using the thought leadership card, and the related thinking row.
- All stats and quotes are placeholders marked "to be confirmed". No client facts are invented. Any Trojan copy, if used later, must be clearly labelled as an example.

### Case study index (`/work/`)

- Nav label and H1 stay **Our work**; the client's "Our clients" idea is the support line under the H1.
- Short intro, then an **auto-scrolling client logo band** (constant speed, pauses on hover and under reduced motion; link a logo only if a case exists).
- **One grid** of thought leadership cards with a filter bar of **Industry** and **Service** groups (Expertise behind More filters) and a See more link. The old Featured / All split is removed: it fought the single grid.
- **Testimony video** block (16:9, speaker named beneath), then the contact band.

### Service and strand pages (all seven services and CEO Advisory)

Client structure, applied to every page:

1. **Hero**: name, strapline (the existing hero line), image.
2. **Overview**.
3. **Why now?**
4. **How can we help you?**: the former capability H2s are now H3s under this heading. Nothing hides: **no accordion, no tabs**; every section is a real H2 or H3 in the page source for search and AI answers.
5. **Related case studies**: a constant-speed carousel of thought leadership cards, directly after the offer (the proof-up rule from v5 survives here).
6. **Why us?**
7. **Our experts**: Person cards that open a **profile pop-up** (biography, focus, link to the full profile page, whose URL keeps working for search).
8. How it works, where the deck gives one, then the Expertise links and the contact band.

The framework modules keep their anchored homes where they add value: Customer, Innovation, Value and Delivery on Growth Strategy (`#civd`), AgentLab on AI Agents for Marketing (`#agentlab`), Our Operating Architecture framework on Operating Model Design (`#operating-architecture`), Side-by-Side on CEO Advisory (`#side-by-side`). CEO Advisory keeps `#advisors` so the mega-nav's Our advisors link still lands.

The pillar hub pages (`/services/` and `/services/activation/`) keep their current hub roles. The client's separate landing ideas for Growth Strategy and Activation are open items, not applied.

### What we do landing (`/services/`)

Light touch only: rename-related changes (the Value Orchestration card and links). The client's board shows two white frames (Option A and B) whose content is undecided; the page keeps its current structure until the client picks one.

### Careers (`/careers/`)

- **Hero** with a **See open positions** anchor button and a brief description.
- **Life at Manifesto** kept on Careers, separate from Our people.
- **Values and culture**: four cards, linking to Values and culture.
- **Diversity, equity and inclusion** and **Benefits**: both kept. The Mural sketch does not draw them, but a layout sketch is not a cut list.
- **Application process**: five steps. Application, Interview with Partners, Case study, References, Decision.
- **Roles**: Open positions / All toggle, defaulting to Open positions, with an intro line inviting people to reach out even if no role fits.

### Single role page (`/careers/growth-architect/`)

Title, description, and **How to apply via LinkedIn**: the apply button links to the role's application page on LinkedIn (external; placeholder in the wireframe).

### Our thinking (`/insights/`)

- **Type filter tabs** in the order **All, Reports, Articles, News and events**, plus a tag filter. News and Events are one merged type.
- **One card design for every item** (the thought leadership card) with the type shown on the card.
- Grid runs one, two or three across depending on what the filter returns.
- **The filters work in the wireframe** (Gary, 19 October): tabs and tag pills hide and show cards client-side with a small vanilla script (`mocks/assets/filter.js`, no framework), with the active state shown. The tag pills on the cards drive the same tag filter. Deep links (`?type=reports` or `#reports`) from the nav dropdown open the matching state, and the empty state appears only when a combination returns nothing. Every card stays in the HTML, so the filters hide nothing from crawlers.
- The nav dropdown is ordered to match: All thinking, Reports, Articles, News and events.
- **No dates on cards** (reports are evergreen). The decision stands; the visible note about it was removed from the page itself and lives only here and in D-68.
- **No downloads from the grid.** Reports get their own single pages with the **email gate there** (full name, work email, company, an optional-updates tick).

### Article page (`/insights/loyalty-without-the-discount/`)

Title and image hero, article body, then a **related trio**: one article, one service, one report. The trio replaces the former How we help block; the service link moves into the trio.

### Thought leadership card (used everywhere above)

Rounded card, image on top, one coloured pill carrying the **primary service tag**, large title, short excerpt, a row of small uppercase **secondary tags** (industry or expertise), and a "Read more" link. Greyscale in the wireframe like every other component. It is the one listing card for Our thinking, related rows, and the case cards on `/work/` and case pages.

---

## 4. Judgement calls taken in this pass

| Call | Ruling |
|---|---|
| Client's fold-out sketches on service pages | Everything stays visible as real H2s and H3s. Crawlability and AI answers win over the sketch's accordions (D-69). |
| Where Related case studies sits | Straight after How can we help you?, keeping v5's proof-next-to-offer rule inside the client's running order. |
| Capability H2s on service pages | Demoted to H3s under How can we help you? rather than cut; they carry the searched terms the SEO doc requires. |
| "Our clients" on `/work/` | Support line, not the H1. The locked six-item header keeps Our work. |
| Featured / All split on `/work/` | Removed; it fought the client's single grid. |
| "Not hiring for a listed role?" on Careers | Folded into the Roles intro line instead of its own H2. |
| Article page How we help block | Replaced by the related trio; the service link lives in the trio. |
| DEI and Benefits on Careers | Kept, although the sketch does not draw them. |
| CIVD | Kept as the anchored module on Growth Strategy under the new structure; placement flagged as an open item below. |
| Finance and CPG filter labels | Mapped to Financial services and Consumer; one list everywhere (section 2). |

## 5. Open items (not applied; need a decision)

| Item | Note |
|---|---|
| **What we do white frames (Option A and B)** | Two undecided white frames on the client's board for `/services/`. The page keeps its current structure, rename aside, until an option is picked. |
| **Growth Strategy landing** | The client sketched a separate landing. The pillar hub keeps its current role; decide whether a second landing adds anything. |
| **Activation landing** | Same: `/services/activation/` keeps its hub role; the sketched landing is not applied. |
| **Our people auto-scrolling rows** | Sketched rows of team members with pop-up bios, and the middle group named "C&N" where this package says Expert Community (D-62). Neither applied. The profile pop-up component now exists on service pages, so applying the rows later is cheap once the naming is settled. |
| **CIVD placement** | The client's service template does not draw the framework module. It stays anchored on Growth Strategy; confirm whether the client wants it there, elsewhere, or retired. |
| **Reports: how gated** | Reports gate on their own pages. How much is readable before the gate, and whether any report is ungated, is still a content decision. |

## 6. Where to look

| What | Where |
|---|---|
| The wireframes | `mocks/` (open `mocks/index.html`, or the deployed preview) |
| New components, drawn once each | `/catalogue/` in the wireframes |
| Per-page modules used | The "Client layout (Mural, 15 Oct)" row in each changed page's sidebar |
| Decisions D-64 to D-71 | `06-decisions-log.md` |
| Source I summary and precedence | `00-sources.md` |
| Sitemap updates (Energy, renamed slug, new page purposes) | `02-sitemap.md`, `diagrams/sitemap.md`, `diagrams/mega-nav.md` |
| Heading-by-heading map of every page | `heading-map.md` (generated by the build) |
