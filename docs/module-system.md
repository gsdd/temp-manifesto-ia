# Module system (proposed)

Build contract for the Manifesto Growth Architects wireframe and, later, the live site.

This is a naming and behaviour spec. It is not a visual redesign. Current CSS class names stay until a craft pass remaps them.

Reviewed against the live wireframe at [https://temp-manifesto-ia.pages.dev/](https://temp-manifesto-ia.pages.dev/). Full findings: [`docs/wireframe-review-fresh.md`](wireframe-review-fresh.md).

Wireframe-only samples, with on-unit labels: [`mocks/catalogue/index.html`](../mocks/catalogue/index.html). `/catalogue/` is not a live client URL.

---

## 1. Rules that apply to every module

### 1.1 What a unit is

Say the **job**, then the **shape**.

- A **card** is a destination: title, optional media, optional summary, whole surface is one link.
- A **tile** is a pillar entry on the triangle. Not a card.
- A **box** is a diagram cell, a number, or a logo. Not a destination unless the spec says it links (logo to a case).
- A **row** is one line in a list. The line may be a link.
- A **tag** is a cross-link to one theme or, on a case, one service. Cap three visible.
- A **chip** is a filter control. Never a tag, never a working note.
- A **section** is a page region (hero, pillar, prose, closing).

Do not call live units "chips" or "blocks" in stakeholder copy. `.block` may remain a CSS wrapper.

### 1.2 Link vs button

| Button (commits or toggles) | Link (goes somewhere) |
|---|---|
| Form submit | Any page or in-page anchor |
| Cookie accept | Header, footer, mega-nav, breadcrumbs |
| Filter on/off | Whole-card destinations |
| Clear filters | Theme tags, situation rows, chooser rows |
| | Secondary CTA: "See our work", "What we do", "All thinking" |

Header **Contact** is a button-styled **link** to `/contact/`. That is allowed. Label it Primary action / page link, not Button, when the target is a URL.

If the control has an `href` and does not change data, it is a link.

### 1.3 When to use a card

Use a card only for Offer, Case, Thinking, or Person.

Do not use a card for: pillar entry (use Pillar tile), "More work", "Our people" as a listing shortcut, expertise themes (use Theme card only if you add that specialist; otherwise text links or a dedicated Theme card, never Offer), job vacancies (Role row or a future Role card), CIVD cells, metrics, filters.

### 1.4 CEO Advisory and keywords (constraints)

- CEO Advisory uses the same ink and heading weight as Growth Strategy and Activation. Quieter only by column width and content volume. Do not grey it.
- Every mega-nav strand keeps a keyword-led subtitle.
- This document does not ship on the live site. The catalogue remains wireframe-only.

---

## 2. Core modules (12)

### 2.1 Page hero

**Purpose.** Answer where I am, whether it is for me, and the next action.

**Anatomy.** Optional eyebrow. One H1. Strapline or definition line. Optional who-for. Optional also-known-as (renamed deck terms only). Optional Metric set (only if the deck gives a figure). Action pair.

**Link vs button.** Primary = Primary action (Contact, Arrange a conversation, Work for us). Secondary = text link.

**Shape.** Section.

**Use on.** Every template except utility stubs that have no CTA.

**Current CSS.** `.block.hero`, `.eyebrow`, `.who`, `.aka`, `.cta`

**Do not.** Put Theme tags in the hero except on a case study (services used) or an article (themes). Never put filters in the hero.

---

### 2.2 Pillar tile

**Purpose.** Enter one of the three Growth Architecture pillars.

**Anatomy.** Pillar name (strong). Pillar line (the mega-nav line). Three tiles, equal ink.

**Link vs button.** Whole tile is a link. Home: pillar URL. Hub: in-page anchor to the pillar section (and the section heading still links to the pillar URL).

**Shape.** Tile. Not an Offer card.

**Use on.** Home What we do. Services hub Three ways we work with you. Catalogue sample.

**Current CSS.** `.tri a`

**Do not.** Grey the third tile. Do not add a fourth tile. Do not reuse this skin for services.

---

### 2.3 Offer card

**Purpose.** Enter one buyable service (or the Activation group when it is sold as a set).

**Anatomy.** Service name. One-line summary (capability, not a paragraph). No image.

**Link vs button.** Whole card is a link to the service URL.

**Shape.** Card.

**Use on.** Services hub pillar sections. Related services. Activation catalogue if you keep cards as well as chooser rows (prefer one; see review).

**Current CSS.** `.card.offer`, `.card.flat`

**Do not.** Use for articles, jobs, expertise themes, or people.

---

### 2.4 Case card

**Purpose.** Enter one case study.

**Anatomy.** Image slot (16:10). Client name. Result line. On listing cards, one primary service name may replace the result line. Not both until design.

**Link vs button.** Whole card is a link to `/work/{client}/`.

**Shape.** Card.

**Use on.** Home Our work, Work listing, service Proof, case related work.

**Current CSS.** `.card` + `.ph`

**Do not.** Use a Case card for "More work" or "All case studies". That is a text link (All work).

---

### 2.5 Thinking card

**Purpose.** Enter one report or article.

**Anatomy.** Report: document slot + title + type line. Article: title + meta (type, optional theme). Two variants, one module.

**Link vs button.** Whole card is a link to `/insights/{slug}/`.

**Shape.** Card. Never the Offer fill.

**Use on.** Home Our thinking. Thinking listing. Featured report.

**Current CSS.** Report: `.card` + `.doc`. Article: currently `.card.offer` (wrong; remap to a thinking variant).

**Do not.** Put thinking items in Offer cards. Related thinking on service pages may stay as Link list rows.

---

### 2.6 Person card

**Purpose.** Enter one person's profile.

**Anatomy.** Avatar. Name. Role or former-role line.

**Link vs button.** Whole card is a link to `/about/team/{name}/`.

**Shape.** Card.

**Use on.** CEO Advisory Our advisors. Services hub CEO section. Our people listing. About leadership (real people only).

**Current CSS.** `.card.person`

**Do not.** Use a Person card for "Our people" as a listing shortcut. That is a text link.

---

### 2.7 Situation row

**Purpose.** Let a prospect recognise themselves.

**Anatomy.** One line, eight words or fewer where possible, in the prospect's voice.

**Link vs button.** Hub: each row is a link to the matching service. Service Why: static lines (not links), same visual family. Label the mode in the wireframe (LINK ROW vs STATIC ROW).

**Shape.** List row.

**Use on.** Services hub Where are you starting from. Service Why this, now (static).

**Current CSS.** `.situations li` (with or without `a`)

**Do not.** Turn these into cards. Do not add icons in the IA.

---

### 2.8 Chooser row

**Purpose.** Pick among sibling services when the visitor already knows the pillar.

**Anatomy.** Service name (strong). One problem line.

**Link vs button.** The row is a link to the service.

**Shape.** List row. Not a card.

**Use on.** Activation "Which of the six do you need?". Optionally How we work engagement shapes.

**Current CSS.** `.list li` (Activation chooser)

**Do not.** Repeat the same sentence on Offer cards underneath unless the cards use **capability** summaries instead of the problem lines.

---

### 2.9 Theme tag

**Purpose.** Cross-link the one dimension this page type is allowed to show as tags.

**Anatomy.** Short theme (or, on a case, service) name. Maximum three visible. No "+2 more".

**Link vs button.** Each tag is a link. Not a filter.

**Shape.** Tag.

**Use on.** Service Related expertise. Case hero (services used) and Related expertise. Article hero (themes).

**Current CSS.** `.page-tags a`

**Do not.** Use this skin for filters. Do not show sectors as tags.

---

### 2.10 Filter chip

**Purpose.** Narrow Work or Thinking results.

**Anatomy.** Group label. Chips. One group open on load (Service on Work, Type on Thinking). More filters reveals the rest. Selected state is visible and named.

**Link vs button.** Toggle is a button. Clear filters is a button. Changing the URL query is the result, not the control type.

**Shape.** Chip (control).

**Use on.** `/work/`, `/insights/`. Search is a form, not this module.

**Current CSS.** `.filter`, `.filter.on`, `.filter.more`

**Do not.** Render filters as inert spans in the next craft pass. Do not show the Empty state at the same time as results.

---

### 2.11 Quote

**Purpose.** Attributed proof next to work.

**Anatomy.** Quote. Cite (client or person). Optional link on the cite to the case.

**Link vs button.** The block is not a button. Cite may be a link.

**Shape.** Block.

**Use on.** Home with work. Work featured. Inside the case result.

**Current CSS.** `blockquote.quote`

**Do not.** Build a testimonials page. Do not put quotes on Contact.

---

### 2.12 Action pair

**Purpose.** The next thing to do.

**Anatomy.** Primary action + secondary text link. Closing band may repeat the pair with a short line.

**Link vs button.** Primary: button-styled link when the target is `/contact/` (or thank-you after a real submit). Secondary: text link. Form Send, cookie Accept, Clear filters are true buttons.

**Shape.** Pair.

**Use on.** Heroes, closing bands, empty states (Clear), cookie bar (Accept + policy link).

**Current CSS.** `.cta .btn`, `.cta .text`, `.closing`, `.more` (fold `.more` into secondary)

**Do not.** Use Primary action for in-page jumps that are not Contact. Do not use two primaries side by side.

**CEO Advisory.** Hero primary label is Arrange a conversation. Closing should use the same label, not Contact.

---

## 3. Specialist modules

Not in the twelve. Do not invent new cards for them.

| Name | Purpose | Anatomy | Action | Current CSS |
|---|---|---|---|---|
| **Logo strip** | Proof of clients or awards | Row of logo slots | Link to the case only if a case exists; else `/work/` or static | `.logos`, `.logo-ph` |
| **Video frame** | Showreel or case film | 16:9 placeholder | Not a button | `.video-ph` |
| **Metric set** | Numbers the deck actually gives | Figure + label | Not clickable | `.metrics`, `.metric` |
| **CIVD frame** | Growth Strategy diagram | Four cells: Customer, Innovation, Value, Delivery | Cells are not cards. Optional text link to `#civd` | `.civd-grid`, `.civd-cell` |
| **Form** | Work with us / Work for us / Nutshell / Search | Label, field type, required, helper, error, submit | Submit is a button | `.form`, `.field`, `.box` |
| **Empty state** | No results for this filter or query | Message + Clear (button) | Shown only when the set is empty | `.empty-state` |
| **Pagination** | Move through a listing | Page numbers + Next | Links | `.pagination` |
| **Cookie bar** | Consent | Policy link + Accept | Accept is a button | `.cookie-bar` |
| **Link list** | Related thinking, events, footer-style lists | Title + meta | Each row a link | `.list` |
| **Text link row** | Theme names on Home; hub shortcuts | Names only | Links | `.row-links` |

Chrome (not page modules): site header, mega-nav hub and strand, dropdown, breadcrumbs, footer. Strand anatomy: label + keyword subtitle (`small`). Hub: linked title + chevron + pillar line.

Annotation (not live UI): working notes. Current CSS `.chip`, `.ia-chips`. Sidebar heading must stay "Working notes", never "Modules".

---

## 4. Visual legend (what to draw on a unit)

On the catalogue, and later on annotated pages, each sample carries two lines:

```
MODULE: Offer card
ACTION: whole-card link (not a button)
```

Optional third line when needed:

```
MODE: static (Why) | link (hub)
```

Ink: small caps, mid grey, above the unit. Never inside the live heading.

| Module | Legend text |
|---|---|
| Page hero | MODULE: Page hero / ACTION: primary = page link to Contact; secondary = text link |
| Pillar tile | MODULE: Pillar tile / ACTION: whole-tile link / NOTE: equal ink, including CEO Advisory |
| Offer card | MODULE: Offer card / ACTION: whole-card link |
| Case card | MODULE: Case card / ACTION: whole-card link |
| Thinking card | MODULE: Thinking card / ACTION: whole-card link / VARIANT: report or article |
| Person card | MODULE: Person card / ACTION: whole-card link / NOTE: a person only |
| Situation row | MODULE: Situation row / ACTION: link or static |
| Chooser row | MODULE: Chooser row / ACTION: row link |
| Theme tag | MODULE: Theme tag / ACTION: text link / NOT a filter |
| Filter chip | MODULE: Filter chip / ACTION: toggle button / NOT a tag |
| Quote | MODULE: Quote / ACTION: none |
| Action pair | MODULE: Action pair / ACTION: primary + secondary as specified |

---

## 5. Template to module map (audited pages)

| Page | Modules in order |
|---|---|
| Home | Page hero, Logo strip, Pillar tile x3, Thinking card x2, Case card x2, Quote, Logo strip (awards), Text link row, Action pair |
| Services hub | Page hero, Pillar tile x3, Situation row x7, Offer cards, CIVD frame (compact), Case line (text), Person cards (CEO), Action pair |
| Growth Strategy | Page hero, Situation row (static), prose, Case cards, CIVD frame, Theme tags, Offer cards, Link list, Action pair |
| Activation | Page hero, prose, Chooser row x6, optional Offer cards, Case cards, Link list, Action pair |
| CEO Advisory | Page hero (Arrange a conversation), Situation row (static), prose (Side-by-Side), Person cards, prose (retainer), Link list, Action pair |
| Work listing | Page hero, Case card (featured), Quote, Filter chips, Case cards, Pagination, Empty state (conditional), Link list, Action pair |
| Thinking listing | Page hero, Thinking cards (reports), Filter chips, Thinking cards (articles), Pagination, Empty state (conditional), Link list, Text link row, Action pair |
| Contact | Page hero, Form, Form, prose | Direct contact has no Action pair; submit is the primary |
| Catalogue | Samples of the twelve plus specialists. Wireframe only |

---

## 6. What this system refuses

- A fifth card type without a new job.
- Greying CEO Advisory.
- Keyword volume as a reason to add nav items.
- Shipping `/catalogue/` on the live site.
- Calling sidebar notes "chips" in the live UI.
- Using Offer card as a default grey box.
