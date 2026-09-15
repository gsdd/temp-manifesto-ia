# 01. Primary navigation (v4)

This document describes everything a visitor can click in the site header and footer, in the order it appears, and what happens when they do. It is written so that someone who is not a designer or developer can picture the navigation without a wireframe.

v2 gave the mega-nav its shape: three columns, one per pillar of Andy's Growth Architecture triangle. v3 rewrote the words in plain, search-friendly language. **v4 strips the concept back** after Gary's feedback that the whole thing still felt too complicated: the mega-nav is now labels with three short pillar lines, the Insights dropdown is gone, the mobile menu has two levels instead of three, and every duplicate route is cut. What was cut and why is in `v4-simplification.md`.

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
| Pillar line | One-to-one advice for senior leaders | not a link |

No items. The heading is the link. v3 had two items beneath it: "Side-by-Side" (the same page as the heading) and "Meet the advisors" (`/about/team/#advisors`). Both are cut (D-36). Side-by-Side is named in the hero of the CEO Advisory page; the advisors are that page's main block and are also listed under Our team. The column stays: it is visibly the third pillar, quieter by width and type weight, not by being hidden (Source C, Source D).

**Panel footer row** (full width, one thin line, small text, separated by a rule)

| Order | Label | Links to |
|---|---|---|
| Left | All services | `/services/` |
| Middle | Expertise | `/expertise/` |
| Right | Contact | `/contact/` |

Three one-word or two-word links. The middle one is the only place expertise appears in the header. v3 spelled out the five theme names here; v4 does not (D-37).

### 3.3 Mega-nav wording rules

- Labels use the words a prospect would search for. Where the deck label and the searched term conflict, the searched term is the label and the deck term lives on the page. The reasoning per label is in `nav-wording-decisions.md`; v4 changes no label.
- No acronyms or internal shorthand in the nav.
- **One pillar line per column**, four to six words, no full stop. The same three lines are used on the Home and Services hub triangle blocks (shared data, `05-content-matrix.md`).
- **No item subtitles**, with two exceptions: a quiet line of two to four words under Experience Engineering and Growth Office. Adding a third quiet line is an IA decision, not a content edit, and the default answer is no: put the explanation on the page.
- The search vocabulary that v3 carried in subtitles (customer experience, website, research, surveys, loyalty, membership, subscription, AI, operating model, interim, programme office, retainer) lives in service page H1s, H2s, title tags and FAQs (`04-canonicals-and-seo.md`, section 6). The menu does not have to carry it.
- No "Column 1", "Pillar 1" or similar labels in the live nav.

### 3.4 Desktop layout notes (structural, not visual)

- Grid: columns 1 and 2 equal width; column 3 roughly two thirds of that width. The panel has a maximum width matching the page content, centred.
- Column headings align on one baseline. Reading left to right gives Growth Strategy, Activation Services, CEO Advisory.
- Column 3 uses the same structure (heading, pillar line) with lighter type weight and a slightly smaller heading.
- The footer row is separated by a rule and uses smaller text. It must not grow beyond three links.
- Word budget for the whole open panel: under fifty words. v4 as specified is about forty-five.

### 3.5 Mobile and tablet behaviour (below roughly 1024 px)

The header collapses to: logo (left), Contact button (right, kept visible), and a Menu button that opens a full-screen panel.

Inside the panel, five rows in order:

1. **What we do** (expands; open by default when the menu opens). One flat list, two levels deep in total:
   - small label **Growth Strategy** (link to `/services/growth-strategy/`), then Proposition Innovation
   - small label **Activation Services** (link to `/services/activation/`), then the six services in desktop order, with the same two quiet lines
   - small label **CEO Advisory** (link to `/services/ceo-advisory/`), quieter
   - then one thin row of two links: All services, Expertise
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
| CEO Advisory | Mega-nav column 3 (quieter) | Column 1, last service | Our work (service filter value) | `/services/ceo-advisory/` (Supporting), advisor profiles under `/about/team/` |

## 9. v1 to v4 header comparison

| | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| Mega-nav columns | 4 plus a 3-link strip | 3 plus a 3-link footer row | Same as v2 | 3 plus a 3-link footer row; no heading line |
| Links inside the mega-nav | 22 | 17 | 17 | 13 (3 headings, 7 items, 3 footer) |
| Distinct destinations | 21 | 14 | 14 | 12 |
| Words in the open panel (approx.) | 120 | 170 | 200 | 45 |
| Item subtitles | 0 | 10 | 10 | 0 (two quiet lines) |
| Pillar subtitles | 0 | 3 | 3 | 3, shortened to four to six words |
| Theme names in the mega-nav | Full column of 5 | In the footer-row link text | In the footer-row link text | None; one "Expertise" link |
| Header dropdowns | 4 | 3 | 3 | 2 (mega-nav, About) |
| Mobile depth inside What we do | 3 levels | 3 levels | 3 levels | 2 levels |
| Sectors in the mobile menu | Yes | Yes (quiet block) | Yes (quiet block) | No (footer only) |

## 10. v3 to v4 changes at a glance

| v3 | v4 |
|---|---|
| Heading line "Our Growth Architecture" with strapline | Cut from the menu |
| Column 1: heading plus items Growth Strategy, Proposition Innovation | Heading (link) plus Proposition Innovation |
| Column 3: heading plus items Side-by-Side, Meet the advisors | Heading (link) plus pillar line only |
| Ten item subtitles | Two quiet lines (Experience Engineering, Growth Office) |
| Pillar subtitles of seven to nine words | Pillar lines of four to six words |
| Footer row "Expertise: loyalty, membership, subscriptions, pricing, customer value" | "Expertise" |
| Insights two-column dropdown | Plain link |
| About dropdown with "About Manifesto" | Four items |
| Mobile: pillar sub-accordions, subtitles, sectors block | Flat list under small pillar labels; no sectors block |
| Footer: "CEO Advisory: Side-by-Side" | "CEO Advisory" |

Labels and slugs are unchanged from v3.
