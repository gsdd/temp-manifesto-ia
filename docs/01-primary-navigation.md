# 01. Primary navigation (v5)

This document describes everything a visitor can click in the site header and footer, in the order it appears, and what happens when they do. It is written so that someone who is not a designer or developer can picture the navigation without a wireframe.

**Wireframe chrome (MURAL pass, pending sign-off).** The clickable mock in `mocks/` currently shows six header items, logo aside: **What we do** | **Our work** | **Our thinking** | **About** | **Careers** | **Contact**. Our thinking is the Insights hub (`/insights/`) with a type dropdown (Reports, Articles, Events and news, All thinking). About dropdown labels: Our people, Our approach, Values and culture. Careers is first-class so Contact can split work-with-us / work-for-us. The tables below remain the v5 IA spec until that chrome is signed, **except the mega-nav group pattern in section 3**, which this pass updates so pillar hubs are obviously clickable and CEO Advisory shows both strands. See `docs/mural-gap-check.md`, `docs/thinking-placement.md`, `docs/strand-gap-check.md`.

v2 gave the mega-nav its shape: three columns, one per pillar of Andy's Growth Architecture triangle. v3 rewrote the words in plain, search-friendly language. v4 stripped the concept back to labels, three short pillar lines and two quiet lines (`v4-simplification.md`). **v5 makes two small changes after the competitor review** (`competitor-nav-review.md`, `v5-refinements.md` R4): the CEO Advisory column carries one quiet link to the advisors, and the panel footer row drops the Contact link that duplicated the header button. Everything else in the header, menu and footer is as v4. The larger v5 changes are on the pages (`03-page-layouts.md`).

Related: `02-sitemap.md` lists every URL referenced here. `diagrams/mega-nav.md` shows the same mega-nav as a diagram. `../mocks/index.html` is the wireframe.

---

## 1. Header at a glance

The header has one row. From left to right:

| Position | Element | Behaviour | Links to |
|---|---|---|---|
| Left | MGA logo | Click returns to Home | `/` |
| Centre | **What we do** | Opens the mega-nav (section 3) | `/services/` |
| Centre | **Our work** | Plain link | `/work/` |
| Centre | **Insights** | Plain link | `/insights/` |
| Centre | **About** | Opens a small dropdown (section 4) | `/about/` |
| Right | **Contact** (button style) | Plain link | `/contact/` |

Five items plus the logo. One mega-nav (What we do) and one small dropdown (About). Our work and Insights are plain links because their filters live on the page.

Sectors are not in the header. They live in the footer, as filters on Our work and Insights, and as light landing pages (section 6; `06-decisions-log.md`, D-08).

### Nav label rules

- Labels are plain English and describe what the visitor gets. The test for every label is "what would a prospect who has never heard of Manifesto type into Google to find this?" (`nav-wording-decisions.md`).
- **What we do** is the visible label (Source A uses it for the grouping). The URL is `/services/`. Clicking it lands on the services hub, which is the Growth Architecture page.
- The header is the same on every page. The current page's top-level item is shown in an active state.

---

## 2. General dropdown behaviour (desktop)

The same rules apply to the mega-nav and the About dropdown.

| Interaction | Behaviour |
|---|---|
| Hover over a top-level label | Opens after a short delay (around 150 ms) so passing the cursor across the header does not flicker menus open |
| Click a top-level label | Navigates to the landing page. The dropdown also opens on click for touch laptops and keyboard users who press Enter |
| Move the cursor out of the dropdown | Closes after a short delay (around 300 ms) |
| Press Escape | Closes the dropdown and returns focus to the top-level label |
| Tab / Shift+Tab | Moves through items inside the open dropdown in reading order (column by column, top to bottom) |
| Click anywhere outside | Closes the dropdown |
| Only one dropdown open at a time | Opening one closes the other |

Accessibility: every top-level label with a dropdown is a button with `aria-expanded`, and the dropdown is a labelled region. Click-to-navigate means the landing page is always reachable without hover.

---

## 3. What we do: the mega-nav

This is the only mega-nav on the site. It is a full-width panel below the header. It contains **three columns and one thin footer row**. That is all. There is no heading line above the columns.

### 3.1 The rule for this panel

The panel is Andy's Growth Architecture triangle (Source B) laid flat, in the order of prominence agreed on the 7 September call (Source C): Growth Strategy first, Activation Services second, CEO Advisory third. A prospect should be able to name the three pillars within two seconds of the panel opening without reading anything in smaller type (Source D, Source F). CEO Advisory is a full-weight pillar: same contrast and type weight as the other two. It is quieter only by column width and by having two strands rather than six (D-57).

Each **group title is a hub**: a linked heading with a trailing arrow, so it never reads as a static label. Under the title, **strands are siblings**. Where a pillar has only one child service, an **Overview** row is the second visible strand so the header does not look like a fake heading over a lonely child. CEO Advisory always shows **two named strands**: Side-by-Side and Our advisors. Activation already has six services; it still gets Overview so every column uses the same hub-plus-strands pattern.

The panel carries labels plus a short keyword-led subtitle under every strand (D-58). Longer explanation still lives on the pages. Pillar lines stay one short line per column.

Against the peer set this is still a sparse services panel. The hub-and-strands pattern adds Overview rows and restores Side-by-Side as a strand (D-54). Deck one-liners do not return.

### 3.2 The panel, exactly as it appears

**Column 1: Growth Strategy** (leftmost, full weight)

| Element | Text | Strand subtitle | Links to |
|---|---|---|---|
| Heading (hub) | **Growth Strategy →** | | `/services/growth-strategy/` |
| Pillar line | Where and how you grow | | not a link |
| Strand 1 | Overview | Where to grow and how to win | `/services/growth-strategy/` |
| Strand 2 | Proposition Innovation | Value proposition design | `/services/proposition-innovation/` |

The heading is the pillar hub (D-11, D-54). Overview is the same destination, labelled so the column always shows two strands: the hub page and the child service. v4 cut a duplicate "Growth Strategy" item (D-36); Overview is the replacement that makes the hub clickable without repeating the group name as a child.

**Column 2: Activation Services** (centre, full weight; slightly wider because it holds six services)

| Element | Text | Strand subtitle | Links to |
|---|---|---|---|
| Heading (hub) | **Activation Services →** | | `/services/activation/` |
| Pillar line | Turning strategy into results | | not a link |
| Strand 1 | Overview | Hands-on delivery, six services | `/services/activation/` |
| Strand 2 | Customer Research and Insight | Research methods and journey mapping | `/services/customer-research/` |
| Strand 3 | Experience Engineering | Customer experience and websites | `/services/experience-engineering/` |
| Strand 4 | AI Agents for Marketing | AI marketing agents, guided by experts | `/services/ai-agents-for-marketing/` |
| Strand 5 | Operating Model Design | Target operating model | `/services/operating-model-design/` |
| Strand 6 | Growth Office | Interim growth team | `/services/growth-office/` |
| Strand 7 | AI Enablement | AI skills and adoption | `/services/ai-enablement/` |

Order of the six services follows the Source B deck. Overview is the group page. Labels are the v3 labels (`nav-wording-decisions.md`), unchanged. Every strand has a short subtitle in buyer language (`docs/keyword-findings.md`). Deck one-liners still do not return.

**Column 3: CEO Advisory** (rightmost, slightly narrower, full visual weight)

| Element | Text | Strand subtitle | Links to |
|---|---|---|---|
| Heading (hub) | **CEO Advisory →** | | `/services/ceo-advisory/` |
| Pillar line | One-to-one support for leaders | | not a link |
| Strand 1 | Side-by-Side | One-to-one advisory retainer | `/services/ceo-advisory/#side-by-side` |
| Strand 2 | Our advisors | Experienced growth leaders | `/services/ceo-advisory/#advisors` |

Two strands, both visible (D-54). The heading is the pillar hub. Side-by-Side is the named retainer product (Source B slide 4); Our advisors is the people. v4/v5 had collapsed this column to heading plus one child, which read as a single strand. Side-by-Side is not a second URL and not an acronym (SxS stays off the site, D-31). The column is not greyed out (D-57). It is quieter only because it has two strands and a slightly narrower grid track.

**Panel footer row** (full width, one thin line, small text, separated by a rule)

| Order | Label | Links to |
|---|---|---|
| Left | All services | `/services/` |
| Right | Expertise | `/expertise/` |

Two short links. Expertise is the only place expertise appears in the header. v3 spelled out the five theme names here; v4 did not (D-37). v4 also had "Contact" here; v5 cuts it (D-50) because the Contact button sits in the header directly above the open panel, so the link duplicated a control a few centimetres away. The same duplicate-route rule that cut the Growth Strategy item and "About Manifesto" (D-36, D-39). No peer repeats Contact inside its services panel.

### 3.3 Mega-nav wording rules

- Labels use the words a prospect would search for. Where the deck label and the searched term conflict, the searched term is the label and the deck term lives on the page. The reasoning per label is in `nav-wording-decisions.md`; v4 changes no label.
- No acronyms or internal shorthand in the nav.
- **One pillar line per column**, four to six words, no full stop. The same three lines are used on the Home and Services hub triangle blocks (shared data, `05-content-matrix.md`).
- **One strand subtitle under every strand**, two to six words, keyword-led and human-readable (D-58). Subtitles help a prospect understand what they get. They do not rename the Manifesto label. Adding a third CEO child or putting SxS in the menu is an IA decision with the default: no.
- **Column 3 has two strands and no more.** Side-by-Side is the named product; Our advisors is the people.
- Search vocabulary also lives in service page H1s, H2s, title tags and FAQs (`04-canonicals-and-seo.md`, section 6; `docs/keyword-findings.md`). Volumes are not invented.
- No "Column 1", "Pillar 1" or similar labels in the live nav.

### 3.4 Desktop layout notes (structural, not visual)

- Grid: Activation slightly wider than Growth Strategy; CEO Advisory slightly narrower. Same ink colour and heading weight on all three. The panel has a maximum width matching the page content, centred.
- Column headings align on one baseline. Reading left to right gives Growth Strategy, Activation Services, CEO Advisory.
- Column 3 uses the same structure (heading, pillar line, strands). It is not set in quieter grey.
- The footer row is separated by a rule and uses smaller text. It carries All services, Expertise, Our work.
- Word budget is no longer a hard cap. Hub rows and strand subtitles are the cost of making the offer readable (D-54, D-58).

### 3.5 Mobile and tablet behaviour (below roughly 1024 px)

The header collapses to: logo (left), Contact button (right, kept visible), and a Menu button that opens a full-screen panel.

Inside the panel, five rows in order:

1. **What we do** (expands; open by default when the menu opens). One flat list, two levels deep in total:
   - small label **Growth Strategy** (hub link to `/services/growth-strategy/`), then Overview, then Proposition Innovation
   - small label **Activation Services** (hub link to `/services/activation/`), then Overview, then the six services in desktop order, with the same two quiet lines
   - small label **CEO Advisory** (hub link to `/services/ceo-advisory/`), quieter, then Side-by-Side (`#side-by-side`) and Our advisors (`#advisors`)
   - then one thin row of two links: All services, Expertise (the same two as the desktop footer row)
2. **Our work**: plain row
3. **Insights**: plain row
4. **About** (expands): Our team, How we work, Values and culture, Careers
5. **Contact**: plain row (also the pinned header button)

Rules:
- No sub-accordions inside What we do. v3 had one per pillar; v4 uses small pillar labels above a flat list (D-40).
- No sectors block in the menu. Sectors are in the page footer on every device.
- Tapping the label text navigates. Tapping the plus or minus toggles the group. The toggle target is at least 44 px square.
- The panel scrolls if content exceeds the viewport. The Contact button and close control stay pinned.

---

## 4. About dropdown

A small, single-column dropdown.

| Order | Label | Links to |
|---|---|---|
| 1 | Our team | `/about/team/` |
| 2 | How we work | `/about/how-we-work/` |
| 3 | Values and culture | `/about/values/` |
| 4 | Careers | `/careers/` |

Clicking About itself goes to `/about/`, so v3's first item "About Manifesto" was a duplicate and is cut (D-39). "How we work" lives here, not under What we do, because it describes method rather than a buyable service (Source A). Careers is a top-level section (`/careers/`) reached from here and the footer.

---

## 5. Insights and Our work

Both are plain header links. Neither has a dropdown.

- **Our work** (`/work/`): filters for Service, Expertise and Sector are on the hub. Service is open on load; Expertise and Sector are behind "More filters" (`03-page-layouts.md`, T7).
- **Insights** (`/insights/`): filters for Type, Expertise, Service and Sector are on the hub. Type is open on load; the rest are behind "More filters" (T9).

v3 gave Insights a two-column dropdown (three type filters plus Expertise with five theme links). v4 removes it (D-38). Where expertise is reachable in v4: the mega-nav footer row, the site footer, the Home expertise row, the `/expertise/` hub, and the More filters on Work and Insights. Themes keep their full weight in the sitemap and in cross-linking; they lose one header placement.

---

## 6. Footer

The footer is the second navigation system. It is identical on every page and carries the full site structure, including sectors and themes, which are kept out of the header.

**Footer column 1: What we do**
Growth Strategy, Proposition Innovation, Customer Research and Insight, Experience Engineering, AI Agents for Marketing, Operating Model Design, Growth Office, AI Enablement, CEO Advisory, All services

**Footer column 2: Expertise**
Loyalty, Membership, Subscriptions, Pricing, Customer Value

**Footer column 3: Who we work with** (heading is plain text; there is no sector index page in v4, D-44)
Financial services, Media, Consumer, Retail (each to `/sectors/{slug}/`)

**Footer column 4: Company**
About, Our people, Our approach, Values and culture, Careers, Our work, Our thinking, The Nutshell, Contact

**Footer bottom row**
Company registration line, Search field (submits to `/search/`), Privacy policy, Cookie policy, Terms, Accessibility statement, social links

A site-wide cookie bar sits above the footer on every page and links to `/cookie-policy/`.

Footer rules:
- Footer links are plain text lists with column headings. No strand subtitles. Service link text is the mega-nav label, exactly. CEO Advisory is listed as "CEO Advisory".
- The footer lists every Canonical and Supporting page in the sitemap except individual case studies, individual insights, individual roles and individual team profiles.
- Sectors appear here in full. This is their primary navigation home.
- Search is footer plus `/search/`, not a seventh header item. The Nutshell is the named newsletter.

---

## 7. Breadcrumbs

Every page below the top level shows a breadcrumb trail directly beneath the header. Home is always the first item and is labelled "Home". Breadcrumb text is the nav label.

Examples:
- `Home > What we do > Growth Strategy`
- `Home > What we do > Activation Services > Experience Engineering` (Activation services show the group in the trail even though the URL is flat)
- `Home > What we do > CEO Advisory`
- `Home > Expertise > Loyalty`
- `Home > Our work > Dayinsure`
- `Home > About > Our team > {Name}`

Breadcrumbs are marked up with `BreadcrumbList` structured data (see `04-canonicals-and-seo.md`).

---

## 8. Quick reference: where does each dimension live in the nav?

| Dimension | Header | Footer | Filters | Own pages |
|---|---|---|---|---|
| Services (the triangle) | Mega-nav, all three columns | Column 1 | Our work (open on load), Insights (More filters) | `/services/...` (Canonical; Activation group and CEO Advisory Supporting) |
| Expertise themes (shown as "Expertise") | One link in the mega-nav footer row | Column 2 | Our work and Insights (More filters) | `/expertise/...` (Supporting) |
| Sectors | Not in the header | Column 3 | Our work and Insights (More filters) | `/sectors/{sector}/` (Light); no index page |
| Methodology | About dropdown | Column 4 | None | `/about/how-we-work/` (Supporting) |
| CEO Advisory | Mega-nav column 3 (full weight, narrower): hub heading, Side-by-Side, Our advisors | Column 1, last service | Our work (service filter value) | `/services/ceo-advisory/` (Supporting) with `#side-by-side` and `#advisors`; advisor profiles under `/about/team/` |

## 9. v1 to v5 header comparison

| | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|
| Mega-nav columns | 4 plus a 3-link strip | 3 plus a 3-link footer row | Same as v2 | 3 plus a 3-link footer row; no heading line | 3 plus a 2-link footer row |
| Links inside the mega-nav | 22 | 17 | 17 | 13 (3 headings, 7 items, 3 footer) | 13 (3 headings, 8 items, 2 footer) |
| Distinct destinations | 21 | 14 | 14 | 13 | 13 |
| Words in the open panel | about 120 | about 170 | about 200 | 49 | 50 |
| Item subtitles | 0 | 10 | 10 | 0 (two quiet lines) | 0 (two quiet lines) |
| Pillar subtitles | 0 | 3 | 3 | 3, shortened to four to six words | 3, unchanged |
| Items under CEO Advisory | 0 (bottom strip link) | 2 | 2 | 0 | 1 (Our advisors) |
| Theme names in the mega-nav | Full column of 5 | In the footer-row link text | In the footer-row link text | None; one "Expertise" link | None; one "Expertise" link |
| Header dropdowns | 4 | 3 | 3 | 2 (mega-nav, About) | 2 |
| Mobile depth inside What we do | 3 levels | 3 levels | 3 levels | 2 levels | 2 levels |
| Sectors in the mobile menu | Yes | Yes (quiet block) | Yes (quiet block) | No (footer only) | No |

For scale: Prophet's What We Do panel has about 25 links, Elixirr's Services panel about 60, Baringa's Capabilities 18 flat; Yonder, frog and Lippincott have no mega-nav at all (`competitor-nav-review.md`).

## 10. v4 to v5 changes at a glance

| v4 | v5 |
|---|---|
| Column 3: heading (link) plus pillar line only | Heading (link), pillar line, one quiet item "Our advisors" to `/services/ceo-advisory/#advisors` |
| Footer row: All services, Expertise, Contact | All services, Expertise |
| Word budget: under fifty (49) | Fifty or fewer (50) |
| Mobile: CEO Advisory small label only | Small label plus Our advisors |

Header items, About dropdown, footer, breadcrumbs, labels and slugs are unchanged from v4. The v3 to v4 changes are in `v4-simplification.md`.

## 11. This pass: hub titles, full-weight CEO, strand subtitles

| Previous menu | This pass |
|---|---|
| Group titles look like headings; Growth Strategy has one child | Group titles are linked hubs with a trailing arrow. Growth Strategy shows Overview + Proposition Innovation |
| Activation: six children, no Overview | Overview + the six |
| CEO Advisory: heading + Our advisors (reads as one strand), greyed or quieter type | Hub heading + Side-by-Side + Our advisors, same contrast as the other pillars (D-57) |
| Two quiet lines only (Experience Engineering, Growth Office) | Keyword-led subtitle under every strand (D-58) |
| Latest thinking at the foot of Home | Featured thinking after the triangle (`thinking-placement.md`) |
| Chips catalogue with working-notes sidebar | Component library, live components only (D-59, D-60) |

Top-level header stays at six items. Services remain the spine. See D-54.
