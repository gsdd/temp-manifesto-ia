# Wireframe fresh-eye review

**Live site:** [https://temp-manifesto-ia.pages.dev/](https://temp-manifesto-ia.pages.dev/)  
**Source:** `mocks/` served as site root  
**Review date:** 16 September 2026  
**Scope:** Named on-page units, wireframe craft, and coverage against the existing IA package. Not a redesign. Not extra pages.

This is a review of the clickable wireframes as they stand. The IA spine (triangle mega-nav, services as canonicals, expertise supporting, sectors light) is already in place. The next pass should make each on-page unit readable as a named type with rules.

**Primary signal for this review:** modules are not clear; links and buttons are muddled; cards and random boxes are muddled. The work is to name what these units *are*.

**Hard rules used here**

- CEO Advisory keeps full visual weight. Do not grey it out.
- `/catalogue/` is a wireframe-only index of blocks. Do not ship it as a live URL.
- Prefer clarity on the pages that already exist, not more pages.
- Catalogue labels in this pass stay internal to the mock.

---

## Verdict

The live mock already carries the triangle, the Growth Architecture hub, situation entry, strand subtitles, and full-weight CEO Advisory. A prospect can name the three pillars from the open mega-nav in under two seconds.

What it does not yet do is behave like a **wireframe of components**. Most units are the same bordered rectangle with a strong title and a grey line. Header Contact, hero Contact, cookie Accept, form Send, and empty-state Clear filters all use the same outline button. Service offers, expertise themes, open roles, and one Home article all use the same offer-card treatment. Case studies and a "More work" listing link share the same image card. CIVD cells, metric boxes, and offer cards share the same grey fill.

Until those types are named and enforced, a designer will invent a visual system, and a CMS will invent content types, from the same ambiguous boxes.

The catalogue at [https://temp-manifesto-ia.pages.dev/catalogue/](https://temp-manifesto-ia.pages.dev/catalogue/) lists several blocks, but the labels are a gallery, not a rule set, and they do not appear on the pages themselves. Working notes in the right-hand sidebar are IA annotations (`docs/03-page-layouts.md`, on-page tags section). They are not module type labels on the canvas.

---

## 1. Wireframe craft gaps

These are missing for the mock to be a proper wireframe rather than a greyscale site.

### 1.1 On-canvas annotations

| Needed | What is live | Evidence |
|---|---|---|
| Module type label on each unit | Almost never. `.wf-label` exists in CSS and is used for "More filters" and "Empty state" on listing pages only | [Our work](https://temp-manifesto-ia.pages.dev/work/), [Our thinking](https://temp-manifesto-ia.pages.dev/insights/). Home, hub, and service pages have no type labels. |
| Interaction notes | None on the canvas | Mega-nav hover delay is in JS only (`mocks/assets/nav.js`). Filters, pagination, and forms are inert. |
| Content density notes | None | Activation repeats the same six lines as a list and as cards. Home packs eight blocks plus cookie bar. |
| CTA hierarchy rules | A pair exists in the catalogue, not as a rule applied on pages | Catalogue "Primary and secondary CTA". Header Contact is a `.btn` with no label saying it is a utility, not the page primary. |
| State board | Hover is underline-on-title for cards; focus is a generic 2px outline; empty is always-on; error and loading are absent | `mocks/assets/wireframe.css` (`.card:hover strong`, `a:focus-visible`). No `:hover` fill on `.btn`. |
| Mobile as a designed state | Header wraps. There is no Menu button, no full-screen panel, no 44px toggles | Spec: `docs/01-primary-navigation.md` section 3.5. Live: [Home at narrow width](https://temp-manifesto-ia.pages.dev/). Mega-nav is hover-only. |

**What a wireframe annotation should look like on the next pass:** a small uppercase label above the unit (`Service card`, `Primary button`, `Situation list`), plus one line of density or interaction copy where the behaviour is not obvious. Keep that chrome off the eventual live site. Keep it on this mock.

### 1.2 Links versus buttons

Live actions collapse into two looks: an outline rectangle (`.btn`) and grey underlined text (`.cta a.text` or `.more`).

| Live control | URL | Class | Job it is doing |
|---|---|---|---|
| Header Contact | every page | `.btn` | Persistent utility |
| Hero Contact | [Home](https://temp-manifesto-ia.pages.dev/) | `.btn` | Page primary |
| Arrange a conversation | [CEO Advisory](https://temp-manifesto-ia.pages.dev/services/ceo-advisory/) | `.btn` | Page primary (correct quieter wording) |
| Cookie Accept | every page | `.btn` | Consent |
| Form Send | [Contact](https://temp-manifesto-ia.pages.dev/contact/) | `.btn` | Submit |
| Clear filters | [Our work](https://temp-manifesto-ia.pages.dev/work/) | `.btn` | Reset a listing |
| What we do / See our work | heroes and closing bands | `.text` | Secondary |
| All work / All thinking / Our advisors | Home, hubs, CEO Advisory | `.more` | Tertiary, but same grey underline as secondary |
| Footer links | every page | unstyled until hover | Navigation |
| Whole card | many pages | `<a class="card">` | The card *is* the link; no inner text-link treatment |
| Filters and pagination | Work, thinking | `<span>` | Look clickable, are not |

Rule that is missing: **one filled or high-contrast primary per page view; text links for secondary; a quieter tertiary for "see all"; header Contact as a utility that is not the same object as hero Contact; cookie and filter resets are not primaries.**

CEO Advisory is the only page that changes the primary label ("Arrange a conversation"). The closing band on that page then switches back to "Contact" ([CEO Advisory](https://temp-manifesto-ia.pages.dev/services/ceo-advisory/)). That is a hierarchy miss on a page that otherwise treats the offer correctly.

### 1.3 Cards versus boxes

Shared drawing: 1px `#cfcfcf` border, strong title, grey supporting line. Fill toggles between white, `#f7f7f7`, and `#fafafa`.

| Live shape | Used for | Why it blurs |
|---|---|---|
| `.tri a` | Growth Architecture triangle on Home and the hub | Same bordered block as a service card, without a type label |
| `.card.offer` / `.card.flat` | Services, expertise themes, Home article, open roles | One object doing four jobs |
| `.card` + `.ph` | Case studies *and* Home "More work" | Listing link dressed as a case |
| `.card` + `.doc` | Reports | Closest to a distinct type; still a bordered card |
| `.card.person` | Advisors, leadership, recent joiners, and on About a "Our people" listing shortcut | Person card used as a navigation tile |
| `.civd-cell` | CIVD frame | Grey fill, strong + span: reads as a small offer card |
| `.metric` | Case "At a glance" *and* service numbers | Same box used for a case dashboard and for the deck's numbers line |
| `.logo-ph` | Trusted partners and Awards | Distinct because of the dashed placeholder; still a box |
| `.filter` and `.page-tags a` | Filters and tags | Same chip |

The catalogue currently names "Service cards", "Case cards", "Report cards", "Person cards", "Stats", and "Triangle blocks" as siblings in a gallery. It does not say when one must not be used as the other. That is the gap this review's taxonomy is for.

### 1.4 States

| State | Present? | Note |
|---|---|---|
| Hover | Partial | Cards underline the title. Buttons do not change. Filters do not toggle. |
| Focus | Generic | 2px black outline on links and buttons. No note on the canvas. |
| Empty | Misplaced | Shown on Work and Thinking *while results are also on the page*. Spec: conditional (`docs/03-page-layouts.md` T7 block 5, T9 block 5). |
| Error | Missing | Contact and report-gate forms are inert grey boxes, not fields, so validation cannot be shown. |
| Loading | Missing | No submit-in-progress, no filter-in-progress. |
| Filter active | Partial | `.filter.on` exists. "All services" is on by default. Extra filters are always visible, so "More filters" is a label not a control (`docs/03-page-layouts.md` T7: one group open on load). |
| Current nav item | Spec only | `docs/01-primary-navigation.md` section 1: current top-level item in an active state. Live header never sets `aria-current="page"`. |

### 1.5 Mobile

`docs/01-primary-navigation.md` section 3.5 specifies: logo left, Contact right, Menu button, full-screen panel, What we do open by default as a flat two-level list, 44px plus/minus targets, Contact and close pinned.

Live behaviour below 720px (`mocks/assets/wireframe.css`): header wraps; all six items plus Contact stay in the bar; mega-nav still depends on `mouseenter`. There is no Menu button. There is no annotation that says "mobile: replace this header with the panel in 3.5".

CEO Advisory must stay full weight on mobile too: a small label plus Side-by-Side and Our advisors, not a greyed third group (`docs/01-primary-navigation.md` 3.5 and D-57).

### 1.6 Density and "finished site" risk

The mock is greyscale and placeholder-led, which is right. It still reads as a complete site because:

- Every listing shows empty state *and* results.
- Forms look like a finished layout with no field, error, or success variants.
- Closing CTA is identical on almost every page, including Work, where the secondary is "See our work" pointing at itself ([Our work](https://temp-manifesto-ia.pages.dev/work/)).
- Activation shows "Which of the six" and then the same six as service cards ([Activation](https://temp-manifesto-ia.pages.dev/services/activation/)).

A wireframe should show **one** intended density per template, with extra states parked in labelled stubs, not stacked into the happy path.

---

## 2. Misses versus input docs

Only items the live pages under-represent. Deliberate cuts (Growth Collective in the header, AgentLab in the mega-nav, sectors as a fourth column, homepage reports grid) are not listed as misses.

### 2.1 Highest-impact misses (already specified, not drawn)

| Miss | Live URL | Source | What is missing |
|---|---|---|---|
| Numbers *line* drawn as a metric strip | [Experience Engineering](https://temp-manifesto-ia.pages.dev/services/experience-engineering/) (one `3x` box), [AI Agents for Marketing](https://temp-manifesto-ia.pages.dev/services/ai-agents-for-marketing/) (two boxes) | `docs/03-page-layouts.md` T3 block 2; `docs/v5-refinements.md` R6; `docs/andy-deck-coverage.md` slides 8 and 9 | Spec is one line of figures in the deck's words ("Over 3x EBITDA return on investment, consistently"; "4 weeks to audit your data. 6 weeks to your first agents."). Live uses the same `.metric` boxes as case "At a glance". |
| What we do block on Experience Engineering | [Experience Engineering](https://temp-manifesto-ia.pages.dev/services/experience-engineering/) | T3 blocks 5 then 6: What we do, then Proof | Live jumps Why to Proof to Find / Redesign / Test / Scale. The canonical description is absent. Squads language from the deck has no home. |
| People on the offer | Canonical service pages, e.g. [Growth Strategy](https://temp-manifesto-ia.pages.dev/services/growth-strategy/), [Experience Engineering](https://temp-manifesto-ia.pages.dev/services/experience-engineering/) | T3 block 12; `docs/v5-refinements.md` R7; `docs/competitor-nav-review.md` (Baringa partners on the capability page); Otter notes in `docs/00-sources.md` Source C (referred visitors check people) | No People block. CEO Advisory correctly uses advisor cards as proof; other services do not show a lead. |
| FAQ stubs | Same service pages | T3 block 13; `docs/04-canonicals-and-seo.md` (FAQPage, long-tail); `docs/keyword-findings.md` (plain H2s and FAQs carry search language) | No FAQ module on any canonical service. |
| Related expertise as tags without a line | Service pages, e.g. [Growth Strategy](https://temp-manifesto-ia.pages.dev/services/growth-strategy/) | T3 block 9: chips, each with one line on the intersection | Live is `.page-tags` only. Looks like filters. |
| AgentLab as a catalogue of named entries | [AI Agents for Marketing `#agentlab`](https://temp-manifesto-ia.pages.dev/services/ai-agents-for-marketing/) | `docs/andy-deck-coverage.md` slide 9; T3 AI Agents module; D-15 (entries, not pages) | Four group headings with prose. The twelve named agents are not listed as entries. |
| Operating Architecture as a captioned figure | [Operating Model Design `#operating-architecture`](https://temp-manifesto-ia.pages.dev/services/operating-model-design/) | T3 Operating Model Design module; deck appendix in `docs/andy-deck-coverage.md` | H2 plus three H3s. No figure placeholder, no caption linking Orchestration to Growth Office (the cross-link is a sentence, not a diagram). |
| Case study related services and related work | [Dayinsure](https://temp-manifesto-ia.pages.dev/work/dayinsure/) | T8 blocks 8 and 10 | Related expertise tags and a thinking list are present. Related *service cards* and related *case cards* are not. Team on the engagement is absent (T8 block 7, editorial). |
| Home third work slot is a fake case | [Home](https://temp-manifesto-ia.pages.dev/) | T1 block 5: three case studies, curated, spanning at least two pillars. Card: image, client, one-line result. Then a link "All work". | Live: Dayinsure, Key Group, then a case-shaped card "More work / All case studies", plus another "All work" text link. Two cases, not three. The listing link is wearing a case card. |
| Work cards missing the one service tag | [Our work](https://temp-manifesto-ia.pages.dev/work/) | T7 block 4: client, one-line result, one service tag | Grid cards use the service name *as* the result line ("Experience Engineering"). Featured uses a result line and no tag. |
| Insights hub is not the T9 "Latest" pattern | [Our thinking](https://temp-manifesto-ia.pages.dev/insights/) | T9: Latest (one large plus next three), then Type filters on the results list. MURAL in `docs/mural-gap-check.md`: reports at the top, articles underneath. | Reports section plus an Articles section that also holds type filters (including Report and Event). No large Latest. Article uses an offer card. Empty state stacked under results. |
| Theme cards without counts | [Expertise](https://temp-manifesto-ia.pages.dev/expertise/) | T4 block 2: definition line and count of case studies and insights | Five offer cards, all subtitled "Cases and thinking". |
| Associates group has no cards | [Our people](https://temp-manifesto-ia.pages.dev/about/team/) | T12 block 5; R7; Source B slide 12 | Heading only: "Associates, expert network and C and N members". |
| About is missing clients and careers teaser as specified | [About](https://temp-manifesto-ia.pages.dev/about/) | T11 blocks 6 and 7 | Leadership uses a person card for "Our people" (a listing link). No client logo wall. Values and Careers are a sentence, not two links as a pair. C and N members is a heading with no confirmed content (`docs/mural-gap-check.md` open question 1). |

### 2.2 Wireframe-specified chrome that is not on the live mock

| Miss | Live URL | Source |
|---|---|---|
| Mobile menu | All pages at narrow width | `docs/01-primary-navigation.md` 3.5 |
| Click-to-open mega-nav for touch, current page `aria-current` | Header on every page | `docs/01-primary-navigation.md` sections 1 and 2. Live: hover only (`mocks/assets/nav.js`). Top-level "What we do" is an `<a>`, not a button with `aria-expanded` as the spec's accessibility line asks. |
| Trusted partner logos link only when a case exists | [Home](https://temp-manifesto-ia.pages.dev/) | T1 block 2; `docs/mural-gap-check.md` open question 8 | Logos are not links at all, so the rule cannot be demonstrated. |
| Contact `?topic=` | Service heroes | T3 block 1 | Hero Contact goes to `/contact/` with no topic query. |
| Direct contact as data, not a sentence | [Contact](https://temp-manifesto-ia.pages.dev/contact/) | T16 block 4; MURAL "Email Mark" in `docs/mural-gap-check.md` | "Email, phone, office address" is prose. No labelled fields for those values. No note of the tracked Email Mark route on the canvas (it sits in the sidebar only). |
| Careers empty state for no open roles | [Careers](https://temp-manifesto-ia.pages.dev/careers/) | T15 block 4 | One role card is shown. The empty state ("No open roles right now" plus speculative contact) is not drawn as a labelled stub. |
| Report gate states | [The Pricing Paradox](https://temp-manifesto-ia.pages.dev/insights/pricing-paradox/) | T10 block 3 | Email box plus a button labelled "Read on this page". No ungated / gated / submitted variants. |

### 2.3 Keyword and deck language that is present but easy to miss because the unit is wrong

These are not missing ideas. They are under-represented because they sit in the wrong shape.

| Intent | Live | Source | Issue |
|---|---|---|---|
| Journey mapping, CX, websites | [Experience Engineering](https://temp-manifesto-ia.pages.dev/services/experience-engineering/) H2s; mega-nav subtitle | `docs/keyword-findings.md`; Otter in `docs/00-sources.md` Source C | H2s exist. They are indistinguishable from any other heading block. Find / Redesign / Test / Scale is How it works, but it is drawn as four ordinary H2s, not a phase module. |
| Interim growth team / interim CMO | Activation "which of the six" and Growth Office | `docs/keyword-findings.md`; Source B Growth Office | Present in copy. No named "two-phase How it works" module (interim, then new ways of working). |
| CIVD is strategy, not Side-by-Side | [Services hub](https://temp-manifesto-ia.pages.dev/services/) compact four-cell; [Growth Strategy `#civd`](https://temp-manifesto-ia.pages.dev/services/growth-strategy/) | `docs/strand-gap-check.md`; MURAL keep/drop | The module exists. Compact hub cells look like metric boxes. Full page cells look like offer cards. |
| So What | [Customer Research](https://temp-manifesto-ia.pages.dev/services/customer-research/) situation line three | `docs/andy-deck-coverage.md` slide 7 | Present as a situation line. The Why hook is still generic "two to four short paragraphs". Six inputs are H3s with no list module. |

### 2.4 What is *not* a miss

Called out so the next pass does not "fix" decisions that already landed.

- CEO Advisory is full weight in the mega-nav, on Home, and on the hub. Keep that. (`docs/01-primary-navigation.md` D-57; client report `docs/client-report-andy.md`.)
- Catalogue is reachable from the sidebar "Page modules" link. That is correct for the mock. Do not add it to the live sitemap or footer.
- Deck one-liners and AgentLab are not in the mega-nav. Correct (`docs/andy-deck-coverage.md` section 3; `docs/mural-gap-check.md`).
- Testimonials are inside case studies, not a page. Correct (Source A).
- Sectors stay in the footer and filters. Correct (Source C, D-08).
- Home thinking is a teaser after the triangle, not a reports grid. Correct (`docs/thinking-placement.md`).

---

## 3. Module taxonomy

Enforce this set. Do not invent a parallel set in Figma or in the CMS. If a unit is not in this list, it is either a heading plus prose, or it should not be on the page.

Visual language is still greyscale. Distinction comes from **structure**, not colour: image vs no image, avatar vs no avatar, fill vs no fill, line vs cell, button vs text.

### 3.1 Actions

#### Primary button

- **Looks like:** High-contrast control. In this greyscale mock, a filled black rectangle with white type, or a 2px border plus heavier type than the header utility. Padding that reads as a button, not a card.
- **Use:** One per page view for the conversion action: Contact, Arrange a conversation, Send, Work for us (careers routes only).
- **Must not look like:** A card, a filter, cookie Accept, or header Contact.
- **Live blur:** `.btn` is shared by header Contact, hero Contact, cookie Accept, Send, Clear filters, 404 actions. [Home](https://temp-manifesto-ia.pages.dev/), [Contact](https://temp-manifesto-ia.pages.dev/contact/), cookie bar on every page.

#### Text link (secondary CTA)

- **Looks like:** Underlined sentence-case text, same size as body or slightly larger. No box.
- **Use:** The alternative next to a primary: What we do (Home hero), See our work (service heroes). Pair with a primary; do not sit alone as a fake button.
- **Must not look like:** A primary button, a tertiary "see all", or a footer link.
- **Live blur:** Same underline and grey as tertiary `.more`. [Home](https://temp-manifesto-ia.pages.dev/) hero "What we do" versus "All thinking" later on the page.

#### Tertiary link

- **Looks like:** Smaller, mid grey, underline. Optional trailing arrow. Never a card.
- **Use:** All work, All thinking, Our advisors, Open the CIVD module, Current opportunities.
- **Must not look like:** A case card (Home "More work"), a service card, or a primary.
- **Live blur:** [Home](https://temp-manifesto-ia.pages.dev/) "More work" is a case card *and* there is a tertiary "All work" under the quote.

#### Header utility (Contact)

- **Looks like:** Outline control in the header only. Lighter than the page primary. Persistent on every page including Contact.
- **Use:** Header Contact, and the pinned Contact in the mobile menu specified in `docs/01-primary-navigation.md` 3.5.
- **Must not look like:** The page primary, cookie Accept, or a nav text link.
- **Live blur:** Identical `.btn` to the hero primary.

Cookie Accept is neither of the above. Treat it as **consent control**: text plus a compact action, labelled as such. Do not reuse primary button.

### 3.2 Cards (clickable destinations)

A card is a destination. It has a title, one supporting line, and a single hit area. If it does not go somewhere, it is not a card.

#### Service card

- **Looks like:** No image. Title is a *service name*. One-line offer (what you buy). Optional quiet fill. Never an avatar, never a 16:10 image, never a document thumbnail.
- **Use:** Hub pillar sections, Activation six, related services on a service or case page. Maximum three in a related-services row (T3 block 10).
- **Must not look like:** The triangle, a theme card, a role, an article, or CIVD.
- **Live blur:** Same `.card.offer` used for themes, roles, and the Home article. [Services hub](https://temp-manifesto-ia.pages.dev/services/), [Expertise](https://temp-manifesto-ia.pages.dev/expertise/), [Careers](https://temp-manifesto-ia.pages.dev/careers/), [Home](https://temp-manifesto-ia.pages.dev/) "Loyalty without the discount".

#### Theme card

- **Looks like:** No image. Title is a *theme name*. Definition line plus counts (cases, insights) as specified in T4. Visually quieter than a service card (no offer fill, or a text-forward tile).
- **Use:** Expertise hub only.
- **Must not look like:** A service card. Themes are problems, not things you buy.
- **Live blur:** [Expertise](https://temp-manifesto-ia.pages.dev/expertise/) uses `.card.offer` with "Cases and thinking" on all five.

#### Case card

- **Looks like:** 16:10 image placeholder, client name, one-line result. Optional one service tag (Work hub only). No theme tags on the card (T7).
- **Use:** Home work (real cases only), Work grid, service Proof, theme Proof, sector cases, related work.
- **Must not look like:** A listing link, a report, or a logo tile.
- **Live blur:** [Home](https://temp-manifesto-ia.pages.dev/) "More work". Work grid uses the service name as the result line.

#### Featured case

- **Looks like:** Case card at larger size (image dominant). Quote may sit *beside* it, not inside the card.
- **Use:** Work hub Featured (T7 block 2). One only.
- **Must not look like:** The default grid card at the same size. [Our work](https://temp-manifesto-ia.pages.dev/work/) Featured is a two-column grid with one default case card.

#### Report card

- **Looks like:** Portrait document thumbnail labelled Report, title, one-line hook. Not a 16:10 image.
- **Use:** Home thinking (featured report), Thinking hub Reports, related thinking when the item is a report.
- **Must not look like:** A case card. Do not put "Image" in a landscape slot and call it a report.
- **Live blur:** Distinct `.doc` treatment is already the best-separated card. Keep it; do not let articles borrow it or vice versa.

#### Article card

- **Looks like:** Title, meta line (Article · theme · date). No document thumbnail, no 16:10 work image, no offer fill.
- **Use:** Home thinking (the non-featured item), Thinking hub articles list, related thinking.
- **Must not look like:** A service card.
- **Live blur:** Home and Thinking use `.card.offer` for "Loyalty without the discount".

#### Advisor card (person)

- **Looks like:** Circular avatar placeholder, name, one-line former role or current role. Optional "Available through Side-by-Side" on advisor-flagged profiles.
- **Use:** CEO Advisory `#advisors`, hub pillar 3, Team listing groups, service People block, About leadership.
- **Must not look like:** A service card, and must not be reused as a "see all people" tile.
- **Live blur:** [About](https://temp-manifesto-ia.pages.dev/about/) second person card is "Our people / Everyone client-facing". [Careers](https://temp-manifesto-ia.pages.dev/careers/) recent joiners are the same object as advisors.

#### Role card

- **Looks like:** Role title, location · type · hiring state. List-like, not an offer fill.
- **Use:** Careers open roles.
- **Must not look like:** A service card.
- **Live blur:** [Careers](https://temp-manifesto-ia.pages.dev/careers/) Growth Architect uses `.card.offer`.

### 3.3 Proof, media, and diagrams (usually not cards)

#### Logo row

- **Looks like:** Dashed rectangular placeholders in a single row. Label "Logo" or a named client. Link only if a case exists; otherwise the tile is inert (`docs/mural-gap-check.md` Q8).
- **Use:** Home Trusted partners, About clients, sector client logos. Awards is a *separate* row labelled Award, not mixed into partners.
- **Must not look like:** Case cards.
- **Live blur:** Partners and awards are correctly dashed. They are not links, so the case-exists rule is invisible.

#### Quote

- **Looks like:** Left rule, quote, cite. Not a card, not a metric.
- **Use:** Inside a case, beside Home work, optional on CEO Advisory if a quote exists.
- **Must not look like:** A testimonial page or a featured case card.

#### Media placeholder

- **Looks like:** 16:9 dashed rectangle with a job label: Showreel, Film, Studio, Working with Manifesto.
- **Use:** Home hero showreel; case film if it applies; Our approach growth partner videos; Careers studio. Different labels, same ratio.
- **Must not look like:** A case card image (those are 16:10 inside a card).

#### Metric strip

- **Looks like:** Three or four cells: figure plus unit label (Conversion, Value, Time, NPS). For **outcomes**.
- **Use:** Case study At a glance (T8 block 2) only.
- **Must not look like:** CIVD, and must not be used for the service numbers line.
- **Live blur:** [Dayinsure](https://temp-manifesto-ia.pages.dev/work/dayinsure/) and Experience Engineering numbers share `.metric`.

#### Numbers line

- **Looks like:** One horizontal line of text under the service hero, in the deck's words. Not a grid of cells.
- **Use:** Experience Engineering and AI Agents for Marketing only (T3 block 2). Nowhere else; do not invent figures.
- **Must not look like:** A metric strip or a CIVD row.

#### Situation list

- **Looks like:** Two columns of one-line links (hub) or one-line statements (service Why). Hairline separators. No boxes, no icons (`docs/v5-refinements.md` R1).
- **Use:** Hub "Where are you starting from?"; service Why (three lines); Activation "Which of the six" (one line per service).
- **Must not look like:** Service cards. If the six Activation services are a situation list, do not also render them as a six-card grid with the same sentences.
- **Live blur:** [Activation](https://temp-manifesto-ia.pages.dev/services/activation/) does both. Hub situations are correct in shape; several lines run longer than the eight-word cap in R1.

#### Framework cell (CIVD)

- **Looks like:** Four named cells: Customer, Innovation, Value, Delivery. Short gloss, not an offer line. Compact on the hub; larger with a paragraph each on Growth Strategy `#civd`.
- **Use:** Growth Strategy and the hub pillar 1 section only. Linked from Our approach. Not on Home, not on CEO Advisory (`docs/strand-gap-check.md`).
- **Must not look like:** Metric cells or service cards.
- **Live blur:** `.civd-cell` fill matches `.card.offer`. [Services hub](https://temp-manifesto-ia.pages.dev/services/) compact row sits next to service cards.

#### Triangle (architecture)

- **Looks like:** Three equal-weight blocks: Growth Strategy, Activation Services, CEO Advisory. Shared pillar lines. Triangle line underneath: "Strategy first. Activation to deliver it. Advisors alongside." CEO Advisory uses the same ink as the others.
- **Use:** Home What we do; Services hub "Three ways we work with you". Drawn twice only, shared data (`docs/03-page-layouts.md` T1 and T2).
- **Must not look like:** A row of service cards. The triangle is the system; service cards are things you buy inside a pillar.
- **Live blur:** `.tri a` is a bordered box with strong + span, same silhouette as `.card.offer`. [Home](https://temp-manifesto-ia.pages.dev/) and [Services hub](https://temp-manifesto-ia.pages.dev/services/).

#### Architecture diagram

- **Looks like:** A captioned figure placeholder with a title ("Our Operating Architecture framework") and a caption that names the layers, including the Orchestration cross-link to Growth Office.
- **Use:** Operating Model Design `#operating-architecture` only.
- **Must not look like:** CIVD, the triangle, or a stack of H3s.
- **Live blur:** [Operating Model Design](https://temp-manifesto-ia.pages.dev/services/operating-model-design/) has no figure.

### 3.4 Chrome and listing units

#### Mega-nav hub title

- **Looks like:** Linked heading, trailing arrow, underline. Pillar line under it is not a link.
- **Use:** What we do panel only.
- **Must not look like:** A strand, or a service card dropped into the menu.

#### Mega-nav strand

- **Looks like:** Label plus keyword subtitle (`<small>`). Overview is weight 600. Not a card.
- **Use:** Children under each hub. CEO Advisory: Side-by-Side and Our advisors, full contrast.

#### Page tag

- **Looks like:** Quiet chip. Read as metadata. Links through to the canonical.
- **Use:** The one dimension allowed on that page type (`docs/03-page-layouts.md` on-page tags table). Service pages: expertise, max three, each with a supporting line. Case hero: services used, max three.
- **Must not look like:** A filter, and must not appear as a second row of another dimension.

#### Filter chip

- **Looks like:** Chip with an obvious on/off (`.filter.on` is not enough if every chip looks equally "on"). Grouped. "More filters" is a *control* that reveals Expertise and Sector.
- **Use:** Work and Thinking hubs only.
- **Must not look like:** A page tag or a service card.
- **Live blur:** [Our work](https://temp-manifesto-ia.pages.dev/work/) shows service chips and extra filters at once. Tags on [Dayinsure](https://temp-manifesto-ia.pages.dev/work/dayinsure/) match the same bordered chip.

#### Case line

- **Looks like:** One sentence: client, one-line result, text link "Read the case study". No image, no card.
- **Use:** One per pillar on the Services hub (T2). This is proof under the offer without a second work grid.
- **Must not look like:** A case card.
- **Live:** Already correct on the hub. Keep it. Do not "upgrade" it to cards.

#### Empty state

- **Looks like:** Dashed region, message, tertiary or secondary action to clear filters. Labelled "Empty state" in the wireframe. Shown **instead of** the grid, not under it.
- **Use:** Work, Thinking, Careers (no roles), Search.
- **Live blur:** [Our work](https://temp-manifesto-ia.pages.dev/work/) and [Our thinking](https://temp-manifesto-ia.pages.dev/insights/) stack empty under results. Clear filters is a primary `.btn`.

#### Form

- **Looks like:** Labelled fields (real inputs in the wireframe, so states can be drawn). Work with us and Work for us are two forms, not one form with two headings.
- **States to draw once, on Contact and on the catalogue:** default, focus, error, submitting, success (thank-you is already a page).
- **Live blur:** Fields are empty grey rectangles, visually close to logo placeholders. [Contact](https://temp-manifesto-ia.pages.dev/contact/).

#### Closing band

- **Looks like:** Short prompt plus primary + secondary. Not a third hero.
- **Use:** End of templates that close with Contact. On Careers, primary is Work for us. On CEO Advisory, primary stays Arrange a conversation.
- **Must not** repeat "See our work" on the Work hub.

---

## 4. Ranked opportunities (next pass)

Maximum eight. Highest leverage first. No new pages.

1. **Put the taxonomy on the canvas.** Label every unit with its type (`Service card`, `Primary button`, `Situation list`, `CIVD cell`, `Triangle`, `Numbers line`, …). One line of use/not-use where the live site currently blurs. Catalogue stays the index; pages must show the same names. This is the pass that makes the mock a wireframe.

2. **Split actions.** Primary button, text link, tertiary link, header utility, consent control. One primary per view. Stop using `.btn` for cookie Accept, Clear filters, and pagination. Keep CEO Advisory's "Arrange a conversation" in both hero and closing band.

3. **Split cards.** Service / theme / case / featured case / report / article / advisor / role. Remove Home "More work" as a case card; use a tertiary "All work" only. Stop using `.card.offer` for themes, articles, and roles.

4. **Split boxes that are not cards.** Triangle is not a service card. CIVD is not a metric. Numbers line is not a metric strip. Architecture diagram is a figure. Logo row is not a case. Draw those rules, then the designer is not guessing.

5. **Split tags and filters, and draw states.** Page tag plus supporting line on service pages. Filter chips with on/off and a real More filters control. Empty state replaces the grid. Hover and focus notes on primary, cards, strands, and filters. Form default / error / submitting once.

6. **Draw the specified mobile menu**, as a labelled alternate header state (Home + one inner page is enough). Full-screen panel, What we do open, CEO Advisory full weight, 44px toggles (`docs/01-primary-navigation.md` 3.5). Do not leave wrap-and-hope as the mobile wireframe.

7. **Complete T3 on existing service URLs** (no new URLs): What we do on Experience Engineering; People stubs where a lead would show; FAQ stubs; AgentLab as twelve named entries in four groups; Operating Architecture as a captioned figure; numbers as a line; How it works as a named phase module (Find / Redesign / Test / Scale; 4 weeks / 6 weeks; interim then embed). Related expertise keeps a one-line intersection.

8. **Fix density, do not add modules.** Activation: situation list *or* service cards, not both with the same copy. Home: three real cases or two cases plus tertiary, not a fake third card. Work closing band: drop the self-link "See our work". Stacked empty states come off the happy path.

---

## 5. Recommended next-pass brief

**Goal.** A reviewer can point at any block and name its type. A designer can implement from those types without inventing a second system. Andy's triangle, CIVD, AgentLab, and Side-by-Side stay where the IA already put them.

**In**

- On-canvas module labels using the taxonomy in section 3.
- Action hierarchy applied on Home, Services hub, one Activation service (Experience Engineering), CEO Advisory, Work, one case, Thinking, Contact, and the catalogue.
- Card and box splits on those same pages (the rest follow by template).
- Mobile menu as a labelled state.
- T3 completeness on Experience Engineering, AI Agents for Marketing, Operating Model Design, and Growth Strategy (People, FAQ, numbers line, modules). Hub and Home proof honesty (case line vs case card vs tertiary).
- Catalogue labels aligned to this taxonomy. Catalogue remains wireframe-only.

**Out**

- Visual brand, colour, typefaces, illustration.
- New pages, new sold services, `/catalogue/` as a live URL.
- Greying or shrinking CEO Advisory.
- Putting AgentLab, CIVD, or deck one-liners into the mega-nav.
- A second homepage thinking grid.
- Expanding the header.

**Pages to touch, in order**

1. Catalogue (names and rules only).
2. Home and mega-nav (triangle vs service card; cases vs tertiary; action hierarchy; mobile header).
3. Services hub (triangle, situations, service cards, case line, advisor cards, compact CIVD).
4. Experience Engineering, AI Agents for Marketing, Operating Model Design, CEO Advisory (T3 units).
5. Work hub + Dayinsure (filters, empty as alternate, featured vs grid, related services).
6. Contact (form states). Other templates inherit.

**Done when**

- Gary can name the module types from the canvas without opening the sidebar.
- Primary / secondary / tertiary never share a drawing.
- A service card cannot be mistaken for the triangle, a case, a theme, or an article.
- CEO Advisory is still full weight.
- No new URLs have been added.
