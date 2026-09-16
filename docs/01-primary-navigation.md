# 01. Primary navigation (v5)

This document describes everything a visitor can click in the site header and footer, in the order it appears, and what happens when they do. It is written so that someone who is not a designer or developer can picture the navigation without a wireframe.

**Wireframe chrome (MURAL pass, pending sign-off).** The clickable mock in `mocks/` currently shows six header items, logo aside: **What we do** | **Our work** | **Our thinking** | **About** | **Careers** | **Contact**. Our thinking is the Insights hub (`/insights/`) with a type dropdown (Reports, Articles, Events and news, All thinking). About dropdown labels: Our people, Our approach, Values and culture. Careers is first-class so Contact can split work-with-us / work-for-us. The tables below remain the v5 IA spec until that chrome is signed. See `docs/mural-gap-check.md`.

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

The panel is Andy's Growth Architecture triangle (Source B) laid flat, in the order of prominence agreed on the 7 September call (Source C): Growth Strategy first, Activation Services second, CEO Advisory third and quieter. A prospect should be able to name the three pillars within two seconds of the panel opening without reading anything in smaller type (Source D, Source F).

The panel carries labels, not copy. Explanation lives on the pages. The only supporting text is one short line per pillar and one quiet line under each of the two coined service names that Andy flagged as opaque.

Against the peer set this is already the sparsest services panel that still uses a mega-nav: 13 links where Prophet has about 25 and Elixirr about 60 (`competitor-nav-review.md`, 3.2). v5 keeps the count at 13: one quiet link is added in column 3 and one duplicate is cut from the footer row.

### 3.2 The panel, exactly as it appears

**Column 1: Growth Strategy** (leftmost, full weight)

| Element | Text | Links to |
|---|---|---|
| Heading | **Growth Strategy** | `/services/growth-strategy/` |
| Pillar line | Where and how you grow | not a link |
| Item 1 | Proposition Innovation | `/services/proposition-innovation/` |

The heading is the pillar and the lead service in one (D-11). v3 repeated "Growth Strategy" as an item beneath the heading, pointing at the same page; v4 cuts the duplicate (D-36).

**Column 2: Activation Services** (centre, full weight)

| Element | Text | Quiet line (small, grey) | Links to |
|---|---|---|---|
| Heading | **Activation Services** | | `/services/activation/` |
| Pillar line | Turning strategy into results | | not a link |
| Item 1 | Customer Research and Insight | | `/services/customer-research/` |
| Item 2 | Experience Engineering | Customer experience and websites | `/services/experience-engineering/` |
| Item 3 | AI Agents for Marketing | | `/services/ai-agents-for-marketing/` |
| Item 4 | Operating Model Design | | `/services/operating-model-design/` |
| Item 5 | Growth Office | Interim growth team | `/services/growth-office/` |
| Item 6 | AI Enablement | | `/services/ai-enablement/` |

Order follows the Source B deck. Labels are the v3 labels (`nav-wording-decisions.md`), unchanged. The two quiet lines are the only item-level text in the panel: Experience Engineering and Growth Office are the two names Andy said need a plain keyword beside them (Source C: "can you build a website?" must map; Growth Office "terminology hard"). Every other label is the searched term or close to it and stands alone (D-35).

**Column 3: CEO Advisory** (rightmost, narrower, quieter type)

| Element | Text | Links to |
|---|---|---|
| Heading | **CEO Advisory** | `/services/ceo-advisory/` |
| Pillar line | One-to-one support for leaders | not a link |
| Item 1 | Our advisors | `/services/ceo-advisory/#advisors` |

One item, in the same quiet type as the heading. The heading is the pillar link; the item lands on the advisor profile block that is the heart of the CEO Advisory page. v3 had "Side-by-Side" (same page as the heading) and "Meet the advisors" (`/about/team/#advisors`); v4 cut both (D-36). v5 adds back one link, to the offer page rather than to Our team, on new evidence (D-49): a senior advisory offer sells on its people (Criticaleye leads with its mentors; Baringa puts partners on the capability page; The Foundation makes its team a first-class section), Andy asked for heavyweight advisor profiles to be showcased (Source C), and a heading with nothing under it read as an afterthought rather than a pillar (Source D). Side-by-Side is still named in the hero of the CEO Advisory page, not in the menu. The column stays quieter by width and type weight, not by being empty.

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
- **No item subtitles**, with two exceptions: a quiet line of two to four words under Experience Engineering and Growth Office. Adding a third quiet line is an IA decision, not a content edit, and the default answer is no: put the explanation on the page.
- **Column 3 has one item and no more.** "Our advisors" is the people behind the offer, not a second description of it. Adding "Side-by-Side" or a description back is an IA decision with the same default: no.
- The search vocabulary that v3 carried in subtitles (customer experience, website, research, surveys, loyalty, membership, subscription, AI, operating model, interim, programme office, retainer) lives in service page H1s, H2s, title tags and FAQs (`04-canonicals-and-seo.md`, section 6). The menu does not have to carry it.
- No "Column 1", "Pillar 1" or similar labels in the live nav.

### 3.4 Desktop layout notes (structural, not visual)

- Grid: columns 1 and 2 equal width; column 3 roughly two thirds of that width. The panel has a maximum width matching the page content, centred.
- Column headings align on one baseline. Reading left to right gives Growth Strategy, Activation Services, CEO Advisory.
- Column 3 uses the same structure (heading, pillar line, item) with lighter type weight and a slightly smaller heading. The item is set in the same quiet grey as the pillar line.
- The footer row is separated by a rule and uses smaller text. It must not grow beyond three links; v5 uses two.
- Word budget for the whole open panel: fifty words or fewer. v4 was forty-nine; v5 is fifty (minus "Contact", plus "Our advisors").

### 3.5 Mobile and tablet behaviour (below roughly 1024 px)

The header collapses to: logo (left), Contact button (right, kept visible), and a Menu button that opens a full-screen panel.

Inside the panel, five rows in order:

1. **What we do** (expands; open by default when the menu opens). One flat list, two levels deep in total:
   - small label **Growth Strategy** (link to `/services/growth-strategy/`), then Proposition Innovation
   - small label **Activation Services** (link to `/services/activation/`), then the six services in desktop order, with the same two quiet lines
   - small label **CEO Advisory** (link to `/services/ceo-advisory/`), quieter, then Our advisors (`/services/ceo-advisory/#advisors`)
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
About, Our team, How we work, Values and culture, Careers, Our work, Insights, Newsletter, Contact

**Footer bottom row**
Company registration line, Privacy policy, Cookie policy, Terms, Accessibility statement, social links

Footer rules:
- Footer links are plain text lists with column headings. No subtitles or quiet lines. Service link text is the mega-nav label, exactly. CEO Advisory is listed as "CEO Advisory" (v3 wrote "CEO Advisory: Side-by-Side").
- The footer lists every Canonical and Supporting page in the sitemap except individual case studies, individual insights, individual roles and individual team profiles.
- Sectors appear here in full. This is their primary navigation home.

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
| CEO Advisory | Mega-nav column 3 (quieter): heading and "Our advisors" | Column 1, last service | Our work (service filter value) | `/services/ceo-advisory/` (Supporting) with `#advisors`; advisor profiles under `/about/team/` |

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
