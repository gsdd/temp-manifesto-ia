# 01. Primary navigation (v2)

This document describes everything a visitor can click in the site header and footer, in the order it appears, and what happens when they do. It is written so that someone who is not a designer or developer can picture the navigation without a wireframe.

v2 replaces the v1 navigation in full. The v1 mega-nav (four columns plus a bottom strip) was rejected as too busy and for hiding the Growth Architecture triangle. The v2 mega-nav has **three columns, one per pillar of Andy's triangle**, and nothing else competing with them. See `06-decisions-log.md`, section "Why v1 was rejected".

Related: `02-sitemap.md` lists every URL referenced here. `diagrams/mega-nav.md` shows the same mega-nav as a diagram. `../mocks/index.html` is the clickable wireframe.

---

## 1. Header at a glance

The header has one row. From left to right:

| Position | Element | Behaviour | Links to |
|---|---|---|---|
| Left | MGA logo | Click returns to Home | `/` |
| Centre | **What we do** | Opens the mega-nav (section 3) | `/services/` |
| Centre | **Our work** | Plain link, no dropdown | `/work/` |
| Centre | **Insights** | Opens a small dropdown (section 4) | `/insights/` |
| Centre | **About** | Opens a small dropdown (section 5) | `/about/` |
| Right | **Contact** (button style) | No dropdown. Direct link. | `/contact/` |

Five items plus the logo. Only one mega-nav (What we do) and two small dropdowns (Insights, About). Our work is a plain link because its filters live on the page; a filter list in the header was noise.

Sectors are not in the header at all. They live in the footer, as filters on Our work and Insights, and as light landing pages (section 7; `06-decisions-log.md`, D-08).

### Nav label rules

- Labels are plain English and describe what the visitor gets, not internal team names.
- **What we do** is the visible label (Source A uses it for the grouping). The URL is `/services/` because that is what people search for and type. Source A notes What we do itself is not a route; clicking it here lands on the services hub, which is the Growth Architecture page.
- The header is the same on every page. Nothing is added or removed by section.
- The current page's top-level item is shown in an active state.

---

## 2. General dropdown behaviour (desktop)

The same rules apply to the mega-nav and the small dropdowns.

| Interaction | Behaviour |
|---|---|
| Hover over a top-level label | Opens after a short delay (around 150 ms) so passing the cursor across the header does not flicker menus open |
| Click a top-level label | Navigates to the landing page (for example `/services/`). The dropdown also opens on click for touch laptops and keyboard users who press Enter |
| Move the cursor out of the dropdown | Closes after a short delay (around 300 ms) so diagonal movement does not close it |
| Press Escape | Closes the dropdown and returns focus to the top-level label |
| Tab / Shift+Tab | Moves through items inside the open dropdown in reading order (column by column, top to bottom) |
| Click anywhere outside | Closes the dropdown |
| Only one dropdown open at a time | Opening a second closes the first |

Accessibility: every top-level label with a dropdown is a button with `aria-expanded`, and the dropdown is a labelled region. Click-to-navigate means the landing page is always reachable without hover.

---

## 3. What we do: the mega-nav

This is the only mega-nav on the site. It is a full-width panel below the header. It contains **one heading line, three columns and one thin footer row**. That is all.

### 3.1 The rule for this panel

The panel is Andy's Growth Architecture triangle (Source B) laid flat, in the order of prominence agreed on the 7 September call (Source C): Growth Strategy first, Activation Services second, CEO Advisory third and quieter. A prospect should be able to name the three pillars within two seconds of the panel opening (Source D).

Things that are deliberately **not** in this panel, and where they went:

| Removed from the v1 mega-nav | Now lives |
|---|---|
| Expertise column (five themes) | Insights dropdown (section 4), footer, one text link in the panel footer row, `/expertise/` pages |
| Featured case study card | Home (T1 block 4) and the Work hub |
| "How we work" link | About dropdown and footer |
| "Talk to us" link | Panel footer row as "Contact" (one word), plus the header button |
| "Who we work with" (sectors) | Footer only |
| "Column 1 / Column 2" labels and long descriptors | Gone. One plain subtitle per column. |

### 3.2 The panel, exactly as it appears

**Heading line** (full width, above the columns)

| Element | Text | Links to |
|---|---|---|
| Small heading | "Our Growth Architecture" | `/services/` |
| One-line subtitle | "Strategy that works. Execution that delivers." (Source B) | not a link |

**Column 1: Growth Strategy** (leftmost, full weight)

| Order | Label | Subtitle (one line, plain English) | Links to |
|---|---|---|---|
| Heading | **Growth Strategy** | "Where to play and how to win. Our core offer." | `/services/growth-strategy/` |
| 1 | Growth Strategy | "Customer value growth strategy for leadership teams" | `/services/growth-strategy/` |
| 2 | Proposition Innovation | "New propositions: loyalty, membership, subscription and D2C models" | `/services/proposition-innovation/` |

The heading and item 1 point to the same page. This is intentional: the heading names the pillar, item 1 is the service. On mobile the duplicate is removed (section 3.5).

**Column 2: Activation Services** (centre, full weight)

| Order | Label | Subtitle (one line, plain English) | Links to |
|---|---|---|---|
| Heading | **Activation Services** | "The bridge from strategy to execution. AI-powered, human-led." | `/services/activation/` |
| 1 | Customer Intelligence | "Research and insight that gets to the so what faster" | `/services/customer-intelligence/` |
| 2 | Experience Engineering | "CX design, website and digital build, testing at scale" | `/services/experience-engineering/` |
| 3 | Data Agents | "AI agents for performance marketing and customer data" | `/services/data-agents/` |
| 4 | Operating Architecture | "Adaptive operating models for the age of AI" | `/services/operating-architecture/` |
| 5 | Growth Office | "Interim growth teams that get strategy delivered" | `/services/growth-office/` |
| 6 | AI Enablement | "AI skills, value cases and business model innovation" | `/services/ai-enablement/` |

Order follows the Source B deck. Subtitles exist because Andy said on the call that labels like Experience Engineering are opaque and "can you build a website?" must map clearly (Source C). Subtitles are set text, not CMS descriptions, and must stay one line.

**Column 3: CEO Advisory** (rightmost, narrower, quieter type)

| Order | Label | Subtitle (one line) | Links to |
|---|---|---|---|
| Heading | **CEO Advisory** | "Side-by-Side: one-to-one support for senior leaders" | `/services/ceo-advisory/` |
| 1 | Side-by-Side (SxS) | "Proven growth leaders on speed-dial, on retainer" | `/services/ceo-advisory/` |
| 2 | Meet the advisors | "The people behind Side-by-Side" | `/about/team/#advisors` |

This column is visibly the third pillar of the triangle. It is quieter by width and type weight, not by being hidden. Source C: do not design the site around it, but it is part of the triangle. Source D: it must be visible as such.

**Panel footer row** (full width, one thin line, small text, separated by a rule)

| Order | Label | Links to |
|---|---|---|
| Left | "All services" | `/services/` |
| Middle | "Expertise themes: loyalty, membership, subscriptions, pricing, customer value" | `/expertise/` |
| Right | "Contact" | `/contact/` |

Three text links. The middle one is the only place themes appear in the mega-nav, as a single link with the five theme names as its text. It is not a column and has no sub-items.

### 3.3 Mega-nav wording rules

- Service labels are used exactly as in the Source B deck. Do not abbreviate or rename in the nav. "Data Agents" drops the "(AgentLab)" suffix used in v1; AgentLab is named on the page.
- One subtitle per label, one line, no more than ten words, no full stops except the heading subtitles.
- No icons are required for comprehension. If icons are used later, labels must still stand alone.
- No "Column 1", "Pillar 1" or similar labels in the live nav. The three-column layout does the work.

### 3.4 Desktop layout notes (structural, not visual)

- Grid: columns 1 and 2 equal width; column 3 roughly two thirds of that width. The panel has a maximum width matching the page content, centred.
- Column headings align on one baseline. Reading left to right gives Growth Strategy, Activation Services, CEO Advisory: the triangle in order of prominence.
- Column 3 uses the same structure as the others (heading, subtitle, list) so it reads as a peer pillar, but with lighter type weight and a slightly smaller heading.
- The footer row is separated by a rule and uses smaller text. It must not grow beyond three links.

### 3.5 Mobile and tablet behaviour (below roughly 1024 px)

The header collapses to: logo (left), Contact button (right, kept visible), and a Menu button that opens a full-screen panel.

Inside the panel, in order:

1. **What we do** (accordion). When expanded, a small line "Our Growth Architecture" then three sub-accordions in triangle order:
   - **Growth Strategy** (expanded by default): Growth Strategy, Proposition Innovation
   - **Activation Services** (collapsed): the six services in desktop order, each with its subtitle
   - **CEO Advisory** (collapsed, quieter): Side-by-Side (SxS), Meet the advisors
   - Then one thin row of two plain links: "All services", "Expertise themes"
2. **Our work**: plain link
3. **Insights** (accordion): Latest insights, Reports and guides, Events; then a small "Expertise themes" heading, All themes and the five theme links
4. **About** (accordion): About Manifesto, Our team, How we work, Values and culture, Careers
5. **Contact**: plain link (also present as the header button)
6. Below the primary items, a quieter block: "Who we work with" with the four sector links

Rules:
- Tapping the label text navigates. Tapping the plus or minus toggles the accordion. The toggle target is at least 44 px square. (The alternative whole-row toggle with a "View all" link is acceptable; pick one in wireframes and use it everywhere.)
- The panel scrolls if content exceeds the viewport. The Contact button and close control stay pinned.
- No hover states on touch. Everything is reachable by tap.

---

## 4. Insights dropdown

A small, two-column dropdown. This is the calm home for expertise themes in the header (Source D: themes matter for SEO and cross-linking but must not compete with the triangle).

**Column 1: Insights**

| Order | Label | Links to |
|---|---|---|
| 1 | Latest insights | `/insights/` |
| 2 | Reports and guides | `/insights/?type=report` |
| 3 | Events | `/insights/?type=event` |

**Column 2: Expertise themes**

| Order | Label | Links to |
|---|---|---|
| Heading | Expertise themes (label, not a link) | |
| 1 | All themes | `/expertise/` |
| 2 | Loyalty | `/expertise/loyalty/` |
| 3 | Membership | `/expertise/membership/` |
| 4 | Subscriptions | `/expertise/subscriptions/` |
| 5 | Pricing | `/expertise/pricing/` |
| 6 | Customer Value | `/expertise/customer-value/` |

Why themes sit here: someone browsing thinking wants to browse by problem. Themes are the evergreen version of that thinking, and every theme page routes to the services that solve the problem (Source A's intersecting model). Placing them under Insights keeps the What we do panel to the triangle. See `06-decisions-log.md`, D-04.

"Articles" and "Newsletter" from the v1 dropdown are removed. Latest insights is the article list; the newsletter is in the footer and on the Insights hub.

---

## 5. About dropdown

A small, single-column dropdown.

| Order | Label | Links to |
|---|---|---|
| 1 | About Manifesto | `/about/` |
| 2 | Our team | `/about/team/` |
| 3 | How we work | `/about/how-we-work/` |
| 4 | Values and culture | `/about/values/` |
| 5 | Careers | `/careers/` |

"How we work" lives under About, not under What we do, because it describes method rather than a buyable service (Source A: separate tangible services from methodology). Careers is a separate top-level section (`/careers/`, per Source A) reached from About and the footer; it does not need its own header item.

---

## 6. Contact

A button-styled link with no dropdown. Present on every page in the header, including the collapsed mobile header. Links to `/contact/`.

Secondary calls to action inside pages (for example "Talk to us about loyalty") also point to `/contact/` and may pass a context parameter (for example `/contact/?topic=loyalty`) to pre-select the enquiry subject. These are canonicalised to `/contact/`.

---

## 7. Footer

The footer is the second navigation system. It is identical on every page and carries the full site structure, including sectors and themes, which are deliberately kept out of or light in the header.

**Footer column 1: What we do**
Growth Strategy, Proposition Innovation, Customer Intelligence, Experience Engineering, Data Agents, Operating Architecture, Growth Office, AI Enablement, CEO Advisory: Side-by-Side, All services

**Footer column 2: Expertise themes**
Loyalty, Membership, Subscriptions, Pricing, Customer Value

**Footer column 3: Who we work with**
Financial services, Media, Consumer, Retail (each to `/sectors/{slug}/`)

**Footer column 4: Company**
About, Our team, How we work, Values and culture, Careers, Our work, Insights, Newsletter, Contact

**Footer bottom row**
Company registration line, Privacy policy, Cookie policy, Terms, Accessibility statement, social links

Footer rules:
- Footer links are plain text lists with column headings. No subtitles.
- The footer lists every Canonical and Supporting page in the sitemap except individual case studies, individual insights, individual roles and individual team profiles.
- Sectors appear here in full. This is their primary navigation home.

---

## 8. Breadcrumbs

Every page below the top level shows a breadcrumb trail directly beneath the header. Home is always the first item and is labelled "Home".

Examples:
- `Home > What we do > Growth Strategy`
- `Home > What we do > Activation Services > Experience Engineering` (Activation services show the group in the trail even though the URL is flat; see `02-sitemap.md`)
- `Home > What we do > CEO Advisory`
- `Home > Expertise > Loyalty`
- `Home > Our work > Dayinsure`
- `Home > About > Our team > {Name}`
- `Home > Careers > {Role}`

Breadcrumbs are marked up with `BreadcrumbList` structured data (see `04-canonicals-and-seo.md`).

---

## 9. Quick reference: where does each dimension live in the nav?

| Dimension | Header | Footer | Filters | Own pages |
|---|---|---|---|---|
| Services (the triangle) | Mega-nav, all three columns | Column 1 | Our work, Insights | `/services/...` (Canonical; Activation group and CEO Advisory Supporting) |
| Expertise themes | Insights dropdown column 2; one text link in the mega-nav footer row | Column 2 | Our work, Insights | `/expertise/...` (Supporting) |
| Sectors | Not in the header | Column 3 | Our work, Insights | `/sectors/...` (Light) |
| Methodology | About dropdown | Column 4 | None | `/about/how-we-work/` (Supporting) |
| CEO Advisory | Mega-nav column 3 (quieter) | Column 1, last service | Our work (service filter value) | `/services/ceo-advisory/` (Supporting), advisor profiles under `/about/team/` |

## 10. v1 to v2 header comparison

| | v1 | v2 |
|---|---|---|
| Mega-nav columns | 4 (Growth Strategy, Activation, Expertise, Featured) plus a 3-link bottom strip | 3 (Growth Strategy, Activation Services, CEO Advisory) plus a 3-link footer row |
| Links inside the mega-nav | 22 across 4 columns and a strip | 17 (1 heading, 13 in three columns, 3 in the footer row), of which 10 are the triangle's services |
| Distinct destinations | 21 | 14 |
| CEO Advisory position | Bottom strip text link | Third column, quieter, with advisors link |
| Themes in the mega-nav | Full column of 5 | One text link |
| Featured case study in the mega-nav | Yes | No (Home and Work hub) |
| Sectors in the mega-nav | Bottom strip link | No (footer only) |
| Header dropdowns | 4 (mega, Our work, Insights, About) | 3 (mega, Insights, About) |
