# Independent wireframe review (fresh eye)

Reviewed 16 September 2026 against the live Pages build at https://temp-manifesto-ia.pages.dev/ and the `mocks/` HTML in this repo. This is a second-pass review, not the authoring agent's notes.

Scope: Home, services hub and strands, work, thinking, about, careers, contact, catalogue, search, 404, legal stubs, mega-nav. Cross-checked against Sources A to G, Andy's deck coverage, 7 Sep Otter notes, MURAL keep/drop, the IA client report, competitor nav review, keyword findings, `mocks/README.md` and the page-modules catalogue.

---

## A. Executive verdict

- The IA is in good shape. The triangle is readable in two seconds, CEO Advisory is full weight, strand subtitles do the keyword job, and every sitemap URL that should exist as a page does exist.
- Gary is right on modules. The site is a stack of similar bordered rectangles. Offer cards, article cards, theme cards and role cards share one chrome. Filters, page tags, pagination and primary buttons are all small boxes. Designers cannot tell what a unit *is*.
- This is a page inventory with placeholder copy, not yet a proper wireframe. Missing: interaction notes, hover/focus/error/empty as real states, mobile nav behaviour, form field detail, and annotations on the page itself (the sidebar is IA notes, not module labels).
- Input coverage for the triangle, MURAL keep/drop and competitor page patterns is mostly present. The gaps that still matter are hosting (unknown URLs serve Home, unstyled), unimplemented redirects, About's missing clients wall, service-page People/FAQ, and several template blocks that collapsed into one grey box type.
- Do not redesign brand. Next build should be a named-module pass: one vocabulary, one shape per type, buttons versus links locked, then the missing states. Catalogue now shows the target vocabulary; live pages still mix types.

---

## B. Module taxonomy problem

**Gary is right.** Links versus buttons, cards versus random boxes, and "what is this unit?" are the main wireframe failure. The IA docs already name some types (`03-page-layouts.md`: offer cards, image cards, document cards, person cards, logo rows, quote blocks, 16:9, four-cell CIVD, metric boxes). The mock does not enforce them. The catalogue lists a subset and still uses the same `card offer` class for things that are not offers.

### Named vocabulary (use these names, these shapes)

| Name | When to use | Shape | Do not use for |
|---|---|---|---|
| **Hero** | First block. Where am I, is this for me, primary action. | H1, one or two lines, CTA pair. Optional eyebrow, also-known-as, who-for, numbers. No extra boxes. | Long body copy; a second hero later on the page |
| **Primary button** | The one action we want: Contact, Send, Subscribe, Arrange a conversation, Clear filters, Accept cookies. | Filled rectangle, 1.5px ink border, weight 600. One per cluster. | Navigation, filters, pagination, "All work" |
| **Text link** | Secondary path: What we do, See our work, All thinking, Our Growth Architecture. | Underline, no box, mid ink. | Primary enquiry; anything that submits a form |
| **Nav link** | Header items that go to a hub. | Text in the bar. **Contact in the header is the exception: it is a primary button.** | In-page modules |
| **Hub heading** | Mega-nav column title. | Linked label plus trailing arrow. Same ink on all three pillars. | Static unlinked labels |
| **Strand link** | Mega-nav child. | Label plus one keyword subtitle. Overview is a strand, not a fake heading. | Deck one-liners; AgentLab catalogue |
| **Offer card** | A buyable service. Hub pillars, related services, Activation six. | Grey fill, no image, name + one-line what you get. Whole card is the hit area. | Articles, themes, jobs, cases |
| **Theme card** | An expertise problem (Loyalty, Pricing, …). | Outline only, no fill. Name + "cases and thinking" or a count. | Services |
| **Case card** | Proof of work. | 16:10 image placeholder, client, one-line result. Optional one service tag on listing cards only. | "More work" as a fake third case |
| **Report card** | Long-form report. | Portrait document stub labelled Report, title, type line. | Articles |
| **Article card** | Short thinking. | Text only, no grey fill, no document stub. Title + "Article · theme". | Services |
| **Person card** | A named human. | Circle avatar, name, one line. | Roles, clients |
| **Role card** | A job. | Outline, title, location · type · hiring state. | Offer cards |
| **Quote** | Attributed testimonial. Lives with work, not as its own page. | Left rule, quote, cite. | Marketing slogans |
| **Logo strip** | Clients (Trusted partners) or awards. Same boxes, different heading. | Dashed logo placeholders in a row. Link a logo only if a case exists. | Offer proof |
| **Video 16:9** | Showreel, partner film, case film. | 16:9 dashed frame, label inside (Showreel / Film / Studio). | Cards |
| **Metric box** | A number we are allowed to show (3x EBITDA, 4 weeks, TBC). | Small bordered cell, number then label. | CIVD; decorative stats |
| **CIVD four-cell** | The Growth Strategy frame only. | Four named cells: Customer, Innovation, Value, Delivery. Not metrics. | Activation services |
| **Triangle block** | The three pillars on Home and the hub. | Three equal-weight linked panels, shared triangle line underneath. | A row of offer cards |
| **Situation line** | Problem entry. Hub list and service Why. | Text link or plain line, not a card. Eight words or fewer when it is a hub line. | Capability labels |
| **Filter chip** | Listing controls on Work and Thinking. | Pill outline. One group open; "More filters" reveals the rest. Active = heavier border. | Page tags; buttons |
| **Page tag** | The one live dimension on a page (max three). | Small outlined label, not a pill, not a button. | Filters |
| **List row** | Related thinking, engagement shapes, "which of the six". | Title left, type/meta right, rule between rows. | Cards |
| **Form block** | Work with us, Work for us, Nutshell, report gate, search. | Label above field, stacked. Submit is a primary button. | Decorative boxes |
| **Empty state** | Zero results for the current query/filters. Replaces the grid. | Dashed panel, message, Clear/Browse button. Never sit under a full results grid as if both were live. | A labelled stub parked under real results unless the stub is clearly an annotation |
| **Pagination** | Listing overflow after 12. | Numbered squares. Current page heavier. Not buttons. | Filters |
| **Closing CTA** | Last block on most pages. | Line + primary button + text link. | A second hero |
| **Cookie bar** | Global. | Message + text link to policy + Accept as primary button. | A second header |
| **Breadcrumb** | All pages except Home. | Home > section > page. | Tags |

### Current ambiguous boxes (live)

| What you see | What it is pretending to be | What it actually is | Fix |
|---|---|---|---|
| Grey filled card for "Loyalty without the discount" on Home | Article card | `card offer` (same as a service) | Article card, no fill |
| Grey filled card for Loyalty / Membership / … on `/expertise/` | Offer card | Theme card | Outline theme card |
| Grey filled card for "Growth Architect" on Careers | Offer card | Role card | Role chrome |
| Three Home work cards including "More work" | Three cases | Two cases plus a fake card that duplicates "All work" | Two or three real cases; "All work" stays a text link |
| Triangle panels | Offer cards | Pillar router | Keep triangle chrome; do not reuse offer fill |
| CIVD cells | Metric boxes | Named framework | Keep four named cells; never put numbers in them |
| Filter chips, page tags, pagination, primary buttons | Four different controls | Four similar bordered rectangles | Pill vs small tag vs number square vs filled button |
| Sidebar "chips" (Canonical, keywords, MURAL notes) | Live page tags | Review annotation | Keep in the sidebar; never style live tags to match |
| Cookie Accept and header Contact | Same as form Send | Correct: all three are primary buttons | Keep. Do not turn header Contact into a text link |
| Footer "Go" | Button | Underlined text next to a fake field | Search field + primary Go, or text link only |
| Empty state on Work and Thinking | Zero-results state | Annotation sitting under a populated grid | Either hide the grid in that state, or mark the block "Annotation: empty state" more strongly |

The catalogue at `/catalogue/` named some of these but not the ones that collide (theme, article, role, button vs link vs filter vs tag). That is why Gary cannot see the units.

---

## C. Wireframe gaps

What a designer still cannot take into production from this mock.

### Annotations

- Live pages have no on-canvas module names. The only labels are section H2s and the catalogue. A designer looking at Home cannot tell triangle block from offer card from case card.
- The right-hand sidebar is useful IA (weight, keyword, MURAL notes, heading map). It is not a wireframe annotation layer. It uses the word "chips" for notes, which collides with the v4 "do not call these chips" rule for live UI.
- No notes on hover delay (150 ms open / 300 ms close), keyboard (Escape, ArrowDown), or "click the label goes to the hub".
- No note that Trusted partner logos link only when a case exists (MURAL). Live logos are not links.

### States

- No hover, focus, active, disabled, current-page (header current exists as a bottom border only), error, success.
- Filters do not filter. Pagination does not paginate. Empty states are shown at the same time as results.
- Cookie Accept goes to the cookie policy; it does not dismiss the bar.
- Forms have no required marker, validation error, inline error, or success (thank-you is a separate page, which is fine, but the form itself has no error state).
- Search has example results and an empty state on the same page, both always visible.

### Mobile

- No hamburger. At ~390px the header wraps onto two rows plus Contact. It is readable as a stack, not as a planned mobile nav.
- Mega-nav is hover only. On a narrow viewport, "What we do" goes straight to `/services/`. There is no accordion, no full-screen panel, no "same three pillars, fewer nested levels" (Source F).
- Our thinking and About dropdowns have the same hover problem.
- Cards, triangle and CIVD collapse to one column. That is CSS, not a specified mobile composition (what stays above the fold, what is omitted).
- Touch targets on strand subtitles and footer links are not sized or noted.

### Empty / error / not found

- `/404/` is a good stub (message, What we do button, Our work and Contact as text links, search).
- Unknown URLs do **not** use it. `/this-page-does-not-exist/`, `/sectors/`, `/agentlab/`, `/side-by-side/`, `/civd/`, `/events/`, `/services/growth-architecture/` all return **200** with Home HTML. Because Home CSS is a relative `assets/wireframe.css`, those nested unknown paths render **unstyled Home**. Designers will think the site is broken; hosting has no `_redirects` / 404 fallback to `/404/`.
- Careers has no "No open roles right now" state (T15). One role is always shown.
- Associates on Our people is a heading and a sentence, no empty-or-populated person cards.

### Form fields

| Form | Specified | Live | Missing for a wireframe |
|---|---|---|---|
| Work with us | Name, company, email, topic (`?topic=`), message | Those five, as empty boxes | Required, topic as select (pre-filled from `?topic=`), privacy consent, error, helper text, Email Mark tracking note (MURAL open question) |
| Work for us | Name, email, message | Those three | CV / file, role applying for, consent, error |
| Role apply | Form or email | Sentence only, no fields | Fields or an explicit "mailto" annotation |
| The Nutshell | Email | Email | Frequency, privacy line, error |
| Report gate | Email to receive a copy | Email; button label is "Read on this page" | The button contradicts the gate. Name, consent, gated vs ungated states |
| Search | Query | Query box with no `<input>` | Real input, submitted query echoed, no-results vs results as alternative states |
| Footer search | Field + Go | `<label for="footer-q">` with **no** `id="footer-q"`; field is a `<span class="box">` | Working input |

### Interaction notes designers need

- Mega-nav: hover opens, click on "What we do" goes to hub, Escape closes, only one panel at a time. Not written on the mock.
- Filters: multi-select within a group, AND across groups, URL query string, arriving with `?expertise=` opens More filters (T7). None of that is demonstrated.
- Primary versus secondary CTA rule is visible on Home and most closings, then broken on 404 (What we do is the button, Contact is a text link) and Careers (Work for us as button: that one is correct).
- "Arrange a conversation" on CEO Advisory is the right quieter primary. Closing block on that page still says Contact.
- Showreel / films: still placeholders. Annotate "still at launch, film later" on the hero (MURAL / open question 6).
- Cookie bar: Accept, Reject, or settings? Only Accept is shown.

---

## D. Missed from input docs

Status: **Present** = live on the mock as specified. **Partial** = idea is there but incomplete or in the wrong shape. **Missing** = not on the live mock. Evidence is a live path or a doc citation.

### Andy's deck / triangle (Source B, `andy-deck-coverage.md`)

| Source item | Status | Evidence |
|---|---|---|
| Triangle: Growth Strategy, Activation, CEO Advisory | Present | Mega-nav; Home; `/services/` |
| Order Growth Strategy, then Activation, then CEO Advisory (Otter) | Present | Columns left to right |
| Hub named Growth Architecture | Present | `/services/` H1 "Our Growth Architecture", eyebrow "What we do" |
| Strapline "Strategy that works. Execution that delivers." | Present | Home hero; hub hero |
| Positioning line (ambitious leaders / customer-led growth) | Present | Home H1 |
| Triangle line "Strategy first. Activation to deliver it. Advisors alongside." | Present | Home and hub |
| Proposition Innovation under Growth Strategy | Present | Mega-nav; hub offer cards |
| Six Activation services in deck order | Present | Mega-nav; `/services/activation/` |
| Side-by-Side named, never SxS | Present | `/services/ceo-advisory/#side-by-side` |
| Our advisors as people-proof | Present | Mega-nav strand; hub person cards; CEO page `#advisors` |
| Retainer model (virtual or in person, personality-led) | Present | CEO page "How the retainer works" |
| CIVD on Growth Strategy, not in nav | Present | `/services/growth-strategy/#civd`; compact four-cell on hub |
| "So What" as Customer Research Why hook | Partial | Why situations exist; the "multiple versions of the truth / so-what" line is not the named hook on the live page |
| Find, Redesign, Test, Scale | Present | `/services/experience-engineering/` as four H2s |
| 3x EBITDA numbers line | Present | Experience Engineering hero metric |
| AgentLab groups + named agents as entries | Partial | `#agentlab` has four groups and example names in prose, not a 12-entry catalogue list |
| 4 weeks / 6 weeks numbers | Present | AI Agents hero metrics |
| Operating Architecture figure | Partial | Copy + link on Operating Model Design and How we work; no captioned figure |
| Growth Office Culture / Capability / Value | Partial | Page exists; three elements not structured as sub-sections on the live page |
| AI Enablement three programmes + maturity assessment | Partial | Page exists; programmes not broken out as three H2s on the live page |
| Which of the six (operating model vs staff vs tools vs skills) | Present | `/services/activation/` |
| North Star / growth priorities / demand signals / scenario planning | Present | Growth Strategy H2s |
| "c&n" / C and N | Partial | Stub on About and Our people; still an open client question |
| Growth Architects as a people term | Missing | Optional on Team intro; not used |
| Deck one-liners kept off the mega-nav | Present | Pillar lines are the short v4 lines; one-liners live on hub sentences |

### 7 September Otter notes (Source C)

| Source item | Status | Evidence |
|---|---|---|
| Do not design the whole site around CEO Advisory | Present | Third column, narrower, two strands |
| Deck is not website copy; plain language in nav | Present | Strand subtitles from keyword findings |
| Experience Engineering must map to websites / CX | Present | Subtitle "Customer experience and websites"; page H2s |
| Growth Office terminology is hard; say interim team | Present | Subtitle "Interim growth team"; Activation line mentions interim CMO |
| Sectors are proof, not a second services taxonomy | Present | Footer + light landings; not in header |
| Themes are the expertise story, discoverable not shouted | Present | Home text links; Expertise hub; one mega-nav footer link |
| Site should originate, not only reassure after referral | Partial | Problem entry on the hub; origination forms exist; search and 404 are stubs; unknown URLs fail |
| Advisor profiles as credibility | Partial | Placeholder "Advisor name" cards, one profile shell |
| October CEO Advisory event | Missing | Events section has a Pricing Paradox launch line only |

### MURAL keep / drop (`docs/mural-gap-check.md`)

| Source item | Status | Evidence |
|---|---|---|
| Six-item chrome; Our thinking; Careers first-class | Present | Header |
| Trusted partners high | Present | Home, before What we do |
| FT / awards not in the hero | Present | Awards block below work |
| No homepage reports grid | Present | One report + one article |
| Showreel placeholder | Present | Home hero 16:9 |
| Quotes with work | Present | Home, Work featured, cases |
| Reports at top of thinking; no PDFs | Present | `/insights/#reports`; report expands on page |
| Events + Nutshell | Present | `/insights/#events`; `/newsletter/` |
| Origins on About | Present | H3 Origins |
| How we are distinct | Present | About |
| Life at Manifesto on Careers, not duplicated as a section on About | Present | Cross-link from Our people |
| C and N placeholder | Present | About; Our people |
| Growth partner videos on Our approach | Present | `/about/how-we-work/` |
| CIVD keep, new visuals, strategy not Side-by-Side | Present | Growth Strategy module |
| Careers: DEI, benefits, career-change, office visual | Present | `/careers/` Studio placeholder |
| Split Work with us / Work for us | Present | `/contact/#work-with-us` and `#work-for-us` |
| Drop: Our clients as top-nav, blog as nav, old pyramid, FT in hero, PDF packs | Present | Dropped |
| Clients logo wall on About (T11) | Missing | About has story, distinct, leadership, approach teaser, C and N; no logo wall |
| Values and careers teaser as two links on About | Partial | Approach and values linked; Careers not teased as specified |
| Trusted partner logos link only if a case exists | Missing | Logos are inert; Dayinsure and Key Group should link |

### Prior IA report (`docs/client-report-andy.md`) and layouts (`03-page-layouts.md`)

| Source item | Status | Evidence |
|---|---|---|
| Footer, legal, search, 404, catalogue | Partial | Pages exist; 404 not wired; search field is a dummy |
| Service page: People when a lead is flagged | Missing | No people block on Growth Strategy, Experience Engineering, AI Agents |
| Service page: FAQ | Missing | None |
| Service page: Related thinking as report + article | Partial | List rows, not cards |
| Case: related services as cards | Missing | Dayinsure has tags, expertise, thinking; no related service cards; no related work |
| Case: team | Missing | Editorial, but no stub |
| Work: Service filter grouped by pillar | Partial | A few service chips, not grouped; More filters mixes themes and sectors |
| Insights hub H1 "Insights" in T9 vs live "Our thinking" | Present as MURAL label | Live H1 is Our thinking (correct vs MURAL; layouts doc is stale) |
| Mega-nav footer: client report says All services · Expertise · Our work | Present | Live panel |
| `01-primary-navigation.md` still says two footer links (All services, Expertise) | Spec drift | Live and client report have three. Docs disagree with the mock |

### Competitor nav review

| Pattern v5 promised | Status | Evidence |
|---|---|---|
| Two ways in on the hub (problem + capability) | Present | Triangle + seven situations |
| Proof under the offer | Partial | Hub has a case *line* per pillar, not a case card. Service pages put Proof high. Elsewhen-style cards under each group are not there |
| Named system home on the hub | Present | H1 Our Growth Architecture |
| People on the offer page | Partial | CEO Advisory yes; other services no |
| Pillars' logic in one line | Present | Triangle line |
| Coined name explained in first sentence | Present | Activation bridge; Experience Engineering hero line |

### Keyword findings

| Source item | Status | Evidence |
|---|---|---|
| Strand subtitles from adjacent demand | Present | All strands |
| Do not rename the triangle for volume | Present | Labels unchanged |
| Journey mapping / TOM / interim on Activation six lines | Present | `/services/activation/` |
| Theme titles second keyword pass | Missing | Still an open item; theme pages are thin |

### Open client questions (still open, correctly not invented)

C and N; Growth Collective; Events as section vs page; Careers first-class vs nested; Our thinking vs Insights label (mock took Our thinking); showreel still vs film; Email Mark tracking; interim CMO accuracy; brand-strategy language on Growth Strategy.

---

## E. Opportunities (prioritised)

### P0. Do these before the next client review of the mock

1. **Name and distinguish the units.** Apply the vocabulary in section B on every template. Stop using `card offer` for articles, themes and roles. Filled button versus underlined text link versus pill filter versus small page tag. This is Gary's actual objection.
2. **Wire 404 and redirects on Pages.** Unknown URLs must render `/404/`, not unstyled Home. Implement the sitemap redirects: `/sectors/` → `/work/`; `/agentlab/` and `/data-agents/` → `/services/ai-agents-for-marketing/#agentlab`; `/side-by-side/` → `/services/ceo-advisory/`; `/growth-architecture/` → `/services/`.
3. **Stop showing empty states next to results.** One state at a time, or a clearly labelled annotation outside the page chrome.
4. **Mobile nav note, even if the HTML stays simple.** Annotate: hamburger; one accordion for What we do with the same three pillars; Our thinking and About as one-level lists; Contact still a button. Source F asked for fewer nested levels, not "wrap the desktop bar".

### P1. Completeness a designer will ask for

5. Restore missing template blocks: About clients logo wall; case related services + related work; service People and FAQ stubs; Careers empty-roles state; Associates as person cards or an explicit empty.
6. Real form fields: `<input>` / `<select>` / textarea, required, consent, `?topic=` on Work with us, file on Work for us, report-gate button copy ("Send me the report" vs "Read on this page").
7. Interaction annotations on the mega-nav, filters (query string, AND), logo linking rule, cookie dismiss, showreel still-at-launch.
8. Home work row: three real cases or two cases plus the All work text link. Kill the fake "More work" case card.
9. Align `01-primary-navigation.md` mega-nav footer with the live mock (three links) or cut "Our work" from the panel. Pick one.
10. Catalogue as the source of truth for shapes: every type in section B, with a one-line "when to use". (Started in this PR.)

### P2. After the module pass

11. Twelve AgentLab entries as a list, not four group sentences.
12. Operating Architecture as a captioned figure; Growth Office three elements; AI Enablement three programmes.
13. Advisor profile content when Andy supplies names; do not invent.
14. Filter behaviour prototype (one working group).
15. Keyword pass on the five theme titles before those URLs are treated as locked.
16. Decide Growth Collective, Events page, Email Mark, interim CMO language.

---

## F. Recommended next build

A **module-label and visual-shape consistency pass**. Not a brand pass. Not a new IA.

Concrete checklist:

1. Add a type class to every unit: `card offer`, `card case`, `card report`, `card article`, `card person`, `card theme`, `card role`, `tri`, `civd-grid`, `btn`, `text`, `filter`, `page-tags`. Ban untyped `.card`.
2. Chrome rules in CSS only: offer = grey fill; case = image on top; report = portrait doc stub; article = text, white, no fill; theme = outline; role = outline + meta line; person = avatar. Triangle stays the three-up equal panels. CIVD stays four named cells, never numbers.
3. Actions: one filled `.btn` per cluster; secondary is always `.text` underline; filters are pills; tags are small rectangles; pagination is numbered squares.
4. Optional on-canvas `data-mod` or a tiny grey type label in wireframe mode (Hero, Offer card, Case card, …) that can be toggled off. Catalogue stays the index.
5. Then, and only then, fill P1 missing blocks.

This PR does not redesign pages. It adds the vocabulary to the catalogue and tightens CSS so the types are visible there, and so buttons, links, filters and tags no longer share one box.

---

## Appendix: live crawl notes

Crawled 16 September 2026. All listed sitemap pages return 200 with the expected title.

**Broken or surprising paths**

| URL | Expected | Live |
|---|---|---|
| `/this-page-does-not-exist/` | `/404/` | 200 Home HTML; CSS path breaks; unstyled Home |
| `/sectors/` | 301 to `/work/` | 200 Home, unstyled |
| `/agentlab/`, `/data-agents/` | Redirect to AI Agents `#agentlab` | 200 Home |
| `/side-by-side/` | Redirect to CEO Advisory | 200 Home |
| `/growth-architecture/` | Redirect to `/services/` | 200 Home |
| `/civd/`, `/events/`, `/insights/events/` | Redirect or 404 | 200 Home |
| `/404/` | Error page | Works, but only if you type that path |
| Footer search Go | `/search/` | Works |
| Cookie Accept | Dismiss or policy | Goes to cookie policy; bar stays |

**Mega-nav (desktop)**

Hover opens What we do, Our thinking, About. Three pillars, equal ink, CEO Advisory not greyed. Strand subtitles present. Footer row: All services, Expertise, Our work. Clicking a hub heading goes to the pillar page. Escape closes. No click-to-pin on touch.

**Mobile (~390px)**

No hamburger. Header wraps. What we do navigates to the hub; the panel does not open.

**Pages that match the IA well**

Home structure (partners, triangle, thinking, work, awards, themes). Services hub (system name, triangle, situations, pillar sections). Activation group ("which of the six"). CEO Advisory (Side-by-Side, advisors, Arrange a conversation). How we work (five frameworks). Contact split. Thinking reports-then-articles. Careers Life at / DEI / benefits / speculative route.
