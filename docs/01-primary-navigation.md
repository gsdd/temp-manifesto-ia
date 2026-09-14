# 01. Primary navigation

This document describes everything a visitor can click in the site header and footer, in the order it appears, and what happens when they do. It is written so that someone who is not a designer or developer can picture the navigation without a wireframe.

Related: `02-sitemap.md` lists every URL referenced here. `diagrams/mega-nav.md` shows the same mega-nav as a diagram.

---

## 1. Header at a glance

The header has one row. From left to right:

| Position | Element | Behaviour | Links to |
|---|---|---|---|
| Left | MGA logo | Click returns to Home | `/` |
| Centre | **What we do** | Opens the mega-nav (see section 3) | `/services/` |
| Centre | **Our work** | Opens a small dropdown (see section 4) | `/work/` |
| Centre | **Insights** | Opens a small dropdown (see section 5) | `/insights/` |
| Centre | **About** | Opens a small dropdown (see section 6) | `/about/` |
| Right | **Contact** (button style) | No dropdown. Direct link. | `/contact/` |

Five items plus the logo. Sectors are not in the primary nav. They live in the footer, as filters on Our work and Insights, and as light landing pages (see section 8 and `06-decisions-log.md`, decision D-07).

### Nav label rules

- Labels are plain English and describe what the visitor gets, not internal team names.
- **What we do** is preferred over "Services" as the visible label because it works for people who do not think in consultancy terms. The URL remains `/services/` because that is what people search for and type.
- The header is the same on every page. Nothing is added or removed by section.
- The current page's top-level item is shown in an active state (for example, on `/services/growth-strategy/` the What we do item is active).

---

## 2. General dropdown behaviour (desktop)

The same rules apply to the mega-nav and the small dropdowns.

| Interaction | Behaviour |
|---|---|
| Hover over a top-level label | Dropdown opens after a short delay (around 150 ms) so that passing the cursor across the header does not flicker menus open |
| Click a top-level label | Navigates to the landing page for that item (for example `/services/`). The dropdown also opens on click for touch-based laptops and for keyboard users who press Enter |
| Move the cursor out of the dropdown | Dropdown closes after a short delay (around 300 ms) so that diagonal cursor movement does not close it |
| Press Escape | Closes the dropdown and returns focus to the top-level label |
| Tab / Shift+Tab | Moves through the items inside the open dropdown in reading order (column by column, top to bottom) |
| Click anywhere outside | Closes the dropdown |
| Only one dropdown open at a time | Opening a second closes the first |

Accessibility: every top-level label with a dropdown is a button with `aria-expanded`, and the dropdown itself is a labelled region. The click-to-navigate behaviour means the landing page is always reachable without needing hover.

---

## 3. What we do: the mega-nav

This is the only mega-nav on the site. It is a full-width panel below the header with **four columns** and a **bottom strip**.

### 3.1 Why these columns

The panel mirrors the Andy services triangle (Source B) and the Gary three-dimension model (Source A):

- Columns 1 and 2 are **services** (what MGA does). Growth Strategy comes first because it is the bread-and-butter offer. Activation Services come second because they turn strategy into execution.
- Column 3 is **expertise themes** (the growth problems MGA understands). This is the intersecting dimension. It sits inside the mega-nav so that a visitor who thinks "I have a loyalty problem" rather than "I need a strategy service" still finds their way in from the same menu.
- Column 4 is **proof and orientation**: a featured piece of work and a link to how MGA works.
- The bottom strip carries the **downweighted** items: CEO Advisory (Side-by-Side) and the all-services link.

### 3.2 The columns, exactly as they appear

Read each column top to bottom. Bold text is a column heading and is itself a link.

**Column 1: Growth Strategy**
Small descriptor under heading: "Strategy that works. Our core offer."

| Order | Label | Links to |
|---|---|---|
| Heading | **Growth Strategy** | `/services/growth-strategy/` |
| 1 | Growth Strategy | `/services/growth-strategy/` |
| 2 | Proposition Innovation | `/services/proposition-innovation/` |

Note: the heading and item 1 point to the same page. This is intentional. The heading names the group; item 1 is the specific service inside it. On mobile the duplicate is removed (see 3.5).

**Column 2: Activation Services**
Small descriptor under heading: "Execution that delivers. From strategy to live results."

| Order | Label | Links to |
|---|---|---|
| Heading | **Activation Services** | `/services/activation/` |
| 1 | Customer Intelligence | `/services/customer-intelligence/` |
| 2 | Experience Engineering | `/services/experience-engineering/` |
| 3 | Data Agents (AgentLab) | `/services/data-agents/` |
| 4 | Operating Architecture | `/services/operating-architecture/` |
| 5 | Growth Office | `/services/growth-office/` |
| 6 | AI Enablement | `/services/ai-enablement/` |

Order follows the triangle deck. Customer Intelligence and Experience Engineering come first because they are the most established and most searched-for. AI Enablement closes the list because it is the newest and most exploratory label.

**Column 3: Expertise**
Small descriptor under heading: "The growth problems we know inside out."

| Order | Label | Links to |
|---|---|---|
| Heading | **Expertise** | `/expertise/` |
| 1 | Loyalty | `/expertise/loyalty/` |
| 2 | Membership | `/expertise/membership/` |
| 3 | Subscriptions | `/expertise/subscriptions/` |
| 4 | Pricing | `/expertise/pricing/` |
| 5 | Customer Value | `/expertise/customer-value/` |

Order groups the related recurring-revenue themes together (Loyalty, Membership, Subscriptions), then the commercial levers (Pricing, Customer Value).

**Column 4: Featured**
No heading link. This column is editorial and is managed in the CMS.

| Order | Element | Links to |
|---|---|---|
| 1 | Featured case study card: client name, one-line result, small image | The chosen `/work/{client}/` page |
| 2 | Text link: "How we work" | `/about/how-we-work/` |
| 3 | Text link: "Talk to us about your growth challenge" | `/contact/` |

If no featured case study is set, the card shows the most recent case study automatically.

**Bottom strip** (full width, quieter styling, single row)

| Order | Label | Links to | Notes |
|---|---|---|---|
| Left | "All services" | `/services/` | Always present |
| Middle | "CEO Advisory: Side-by-Side" | `/services/ceo-advisory/` | Downweighted by position and style. It is present so that senior leaders who are looking for it can find it, but it does not compete with Growth Strategy for attention. |
| Right | "Who we work with" | `/sectors/` | The only place sectors appear in the header. Text link only. |

### 3.3 Mega-nav wording rules

- Service labels are used exactly as in the triangle deck. Do not abbreviate or rename in the nav. Any subtitle or search-friendly wording (for example "CX, website and research") belongs on the page, not in the menu.
- Descriptors under column headings are one short sentence, no more than nine words.
- No icons are required for comprehension. If icons are used later, labels must still stand alone.

### 3.4 Desktop layout notes (structural, not visual)

- Columns 1 to 3 are equal width. Column 4 can be slightly wider to hold the card.
- The panel has a maximum width matching the page content, centred.
- Column headings align on one baseline so the three groups read as peers, with Growth Strategy leftmost.
- The bottom strip is separated by a rule and uses smaller text.

### 3.5 Mobile and tablet behaviour (below roughly 1024 px)

The header collapses to: logo (left), Contact button (right, kept visible), and a Menu button that opens a full-screen panel.

Inside the panel:

1. **What we do** is an accordion. Tapping it expands to show three sub-groups, each also an accordion, in this order:
   - Growth Strategy (expanded by default): Growth Strategy, Proposition Innovation
   - Activation Services (collapsed): the six services in the same order as desktop
   - Expertise (collapsed): the five themes
   - Then two plain links: "All services", "CEO Advisory: Side-by-Side"
   - The featured card (column 4) is not shown on mobile. "How we work" moves under About.
2. **Our work**: plain link plus a "Filter by" sub-list (see section 4)
3. **Insights**: plain link plus content type links (see section 5)
4. **About**: accordion with About, Team, How we work, Careers
5. **Contact**: plain link (also present as the header button)
6. Below the primary items, a quieter block: "Who we work with" with the four sector links

Rules:
- Tapping a parent label with an arrow toggles the accordion. Tapping the label text navigates. On small screens the arrow target is at least 44 px square so this distinction is usable. If the team prefers simplicity, the whole row toggles and a separate "View all" link at the top of each expanded group navigates. Either is acceptable; pick one and use it everywhere.
- The panel scrolls if content exceeds the viewport. The Contact button and close control stay pinned.
- No hover states exist on touch. Everything is reachable by tap.

---

## 4. Our work dropdown

A small, single-column dropdown. The purpose is to let a visitor jump straight to filtered proof rather than opening the full Work hub and filtering manually.

| Order | Label | Links to |
|---|---|---|
| 1 | All work | `/work/` |
| Group heading | By service | |
| 2 | Growth Strategy | `/work/?service=growth-strategy` |
| 3 | Activation | `/work/?service=activation` |
| Group heading | By expertise | |
| 4 | Loyalty | `/work/?expertise=loyalty` |
| 5 | Subscriptions | `/work/?expertise=subscriptions` |
| 6 | Pricing | `/work/?expertise=pricing` |
| Group heading | By sector | |
| 7 | Financial services | `/work/?sector=financial-services` |
| 8 | Media | `/work/?sector=media` |
| 9 | Consumer | `/work/?sector=consumer` |
| 10 | Retail | `/work/?sector=retail` |

Notes:
- The "By expertise" group shows a maximum of three themes to keep the dropdown short. Which three is a CMS setting; the default is the three with the most published case studies.
- Filtered URLs use query strings and are canonicalised to `/work/` (see `04-canonicals-and-seo.md`).
- On mobile this appears as a single list under the Our work accordion.

---

## 5. Insights dropdown

A small, two-column dropdown.

**Column 1: Browse**

| Order | Label | Links to |
|---|---|---|
| 1 | Latest insights | `/insights/` |
| 2 | Articles | `/insights/?type=article` |
| 3 | Reports and guides | `/insights/?type=report` |
| 4 | Events and webinars | `/insights/?type=event` |
| 5 | Newsletter | `/newsletter/` |

**Column 2: By theme**

| Order | Label | Links to |
|---|---|---|
| Heading | Explore our expertise | `/expertise/` |
| 1 | Loyalty | `/expertise/loyalty/` |
| 2 | Membership | `/expertise/membership/` |
| 3 | Subscriptions | `/expertise/subscriptions/` |
| 4 | Pricing | `/expertise/pricing/` |
| 5 | Customer Value | `/expertise/customer-value/` |

Note: the themes appear both here and in the What we do mega-nav. This is the one deliberate repetition in the header. Themes are the bridge between "what you sell" and "what you think", so they need to be reachable from both mindsets. Both lists link to the same five `/expertise/` pages; there is no duplicate content. See `06-decisions-log.md`, decision D-05.

The label "Insights" was chosen over "Thinking" because it is the more widely understood term and matches the URL. See decision D-06.

---

## 6. About dropdown

A small, single-column dropdown.

| Order | Label | Links to |
|---|---|---|
| 1 | About Manifesto | `/about/` |
| 2 | Our team | `/about/team/` |
| 3 | How we work | `/about/how-we-work/` |
| 4 | Careers | `/about/careers/` |

"How we work" lives under About, not under What we do, because it describes method rather than a buyable service. It is cross-linked from the mega-nav column 4 so that people evaluating services can still reach it in one click.

---

## 7. Contact

A button-styled link with no dropdown. Present on every page in the header, including the collapsed mobile header. Links to `/contact/`.

Secondary calls to action inside pages (for example "Talk to us about loyalty") also point to `/contact/` and may pass a context parameter (for example `/contact/?topic=loyalty`) to pre-select the enquiry subject. These parameters are canonicalised to `/contact/`.

---

## 8. Footer

The footer is the second navigation system. It is identical on every page and carries the full site structure, including sectors, which are deliberately kept out of the header.

**Footer column 1: What we do**
Growth Strategy, Proposition Innovation, Customer Intelligence, Experience Engineering, Data Agents (AgentLab), Operating Architecture, Growth Office, AI Enablement, CEO Advisory: Side-by-Side, All services

**Footer column 2: Expertise**
Loyalty, Membership, Subscriptions, Pricing, Customer Value

**Footer column 3: Who we work with**
Financial services, Media, Consumer, Retail (each to `/sectors/{slug}/`)

**Footer column 4: Company**
About, Our team, How we work, Careers, Our work, Insights, Newsletter, Contact

**Footer bottom row**
Company registration line, Privacy policy, Cookie policy, Terms, Accessibility statement, social links

Footer rules:
- Footer links are plain text lists with column headings. No descriptors.
- The footer lists every Canonical and Supporting page in the sitemap except individual case studies, individual insights and individual team profiles.
- Sectors appear here in full. This is their primary navigation home.

---

## 9. Breadcrumbs

Every page below the top level shows a breadcrumb trail directly beneath the header. Home is always the first item and is labelled "Home".

Examples:
- `Home > What we do > Experience Engineering`
- `Home > What we do > Activation Services > Data Agents (AgentLab)` (Activation services show the Activation group in the trail even though the URL is flat; see `02-sitemap.md`)
- `Home > Expertise > Loyalty`
- `Home > Our work > Dayinsure`
- `Home > About > Our team > {Name}`

Breadcrumbs are marked up with `BreadcrumbList` structured data (see `04-canonicals-and-seo.md`).

---

## 10. Quick reference: where does each dimension live in the nav?

| Dimension | Header | Footer | Filters | Own pages |
|---|---|---|---|---|
| Services | Mega-nav columns 1 and 2, bottom strip | Column 1 | Our work, Insights | `/services/...` (Canonical) |
| Expertise themes | Mega-nav column 3, Insights dropdown column 2 | Column 2 | Our work, Insights | `/expertise/...` (Supporting) |
| Sectors | Mega-nav bottom strip text link only | Column 3 | Our work, Insights | `/sectors/...` (Light) |
| Methodology | Mega-nav column 4 text link, About dropdown | Column 4 | None | `/about/how-we-work/` (Supporting) |
| CEO Advisory | Mega-nav bottom strip only | Column 1, last service | Our work (as a service filter value) | `/services/ceo-advisory/` (Supporting) |
