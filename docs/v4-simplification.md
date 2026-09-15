# v4: simplifying the whole concept

Gary's feedback on v3 (15 September, evening): **it still feels too complicated as a full concept.** Not only the subtitles. The mega-nav is trying to say too much, the page chips are busy, the homepage has too much going on, and the mock is fussy around the edges. Simplify the idea first, then the UI.

This document is the record of what v4 cut, what it kept, and why. It is written to be read on its own. The detailed specifications are in `01-primary-navigation.md`, `02-sitemap.md` and `03-page-layouts.md`; the decisions are logged as D-34 to D-45 in `06-decisions-log.md`.

---

## The idea in one line

**The What we do menu is the triangle and nothing else: three headings, three short lines, seven service labels, one thin row of links.** Everything that explains, qualifies or cross-references lives on a page, not in the chrome.

A prospect opening the menu should read Growth Strategy, Activation Services, CEO Advisory in under two seconds, and see that the middle column is where most of the services are. That is the whole message of the menu. The homepage repeats it once, as three blocks, and then gets out of the way.

---

## What was too complicated in v3

v1 was rejected for a four-column mega-nav. v2 fixed the structure (three columns). v3 fixed the words. But each version kept adding explanatory material to make the structure legible: a heading line and strapline above the columns, a subtitle under every one of thirteen items, a footer row that listed five theme names, a two-column Insights dropdown, a three-level mobile accordion, a homepage with seven blocks including a pyramid diagram, and a mock with a striped banner, an intro box, a review toggle, tabs, legends, badges and helper notes.

Each piece was justified on its own. Together they made a simple idea look complicated. Gary's test is not "is every item explained?" but "does it feel obvious?".

| Where | v3 | Why it felt busy |
|---|---|---|
| Mega-nav | 1 heading line with strapline, 3 column headings, 3 pillar subtitles, 10 items each with a subtitle, footer row with 5 theme names. Around 200 words. | Thirteen lines of grey subtitle text under thirteen labels reads as a page of copy, not a menu. Two items pointed at the same page as their column heading. |
| Insights dropdown | Two columns: three type filters and six expertise links. | A second content menu competing with the mega-nav. Type filters belong on the hub, as already decided for Our work in v2. |
| Mobile menu | Menu, then What we do, then three pillar accordions, then items with subtitles. Three levels. A sectors block at the bottom. | Too many taps and too much reading to reach a service. |
| Homepage | Seven blocks. Triangle drawn twice (three cards plus a pyramid diagram with a caption). Expertise strip of five themes with descriptors. Featured work cards carrying service and theme tags. | The triangle was explained twice. Tags on cards plus a theme strip plus a logo strip read as a dashboard. |
| Page chips | Case study heroes showed sector, services and themes. Service pages showed related expertise, related services and previous/next links. Theme pages showed a sectors row. Work hub showed three filter groups open at once. | Every page tried to show all three dimensions at once. The cross-referencing model leaked into the chrome. |
| Mock | Striped banner, intro paragraphs, "show what changed" toggle with amber annotations, three tabs, behaviour notes, a sitemap tab with a legend and five badge types, a side panel of notes next to the phone, a toast on every click. | The mock explained itself instead of showing the nav. Gary had to read past the chrome to judge the density. |

---

## What v4 does

### 1. Mega-nav: labels, not copy

```
Growth Strategy              Activation Services              CEO Advisory
Where and how you grow       Turning strategy into results    One-to-one advice for senior leaders

Proposition Innovation       Customer Research and Insight
                             Experience Engineering
                               Customer experience and websites
                             AI Agents for Marketing
                             Operating Model Design
                             Growth Office
                               Interim growth team
                             AI Enablement

All services   Expertise   Contact
```

- **Three columns stay.** Growth Strategy, Activation Services, CEO Advisory, in that order. CEO Advisory narrower and lighter. Nothing else is reintroduced.
- **Column headings are the pillar links.** Growth Strategy heads column 1 and links to `/services/growth-strategy/`. The v3 list item "Growth Strategy" underneath it, which went to the same page, is cut. Same in column 3: the heading CEO Advisory is the link, and the "Side-by-Side" item beneath it (same page) is cut. Side-by-Side is named on the CEO Advisory page.
- **One short line per pillar, none per item.** Three pillar lines of four to six words. The thirteen item subtitles are gone.
- **Two quiet lines, for the two coined names that need them.** Experience Engineering ("Customer experience and websites") and Growth Office ("Interim growth team"). These are the two labels Andy flagged as opaque on the 7 September call. Every other label is already the searched term, or is close enough to stand alone (Proposition Innovation, AI Enablement).
- **"Meet the advisors" is cut.** About, Our team lists the advisors under `#advisors`, and the CEO Advisory page surfaces their profiles as its main block. The menu did not need a second route.
- **The heading line is cut.** "Our Growth Architecture / Strategy that works. Execution that delivers." was a line to read before reaching the pillars. Growth Architecture is the subheading of `/services/` and is in the company name; the strapline is hero copy on Home and the Services hub.
- **Footer row: three words.** All services, Expertise, Contact. The five theme names are gone from the menu.

Count: 13 links (3 headings, 7 items, 3 footer) and 12 destinations, about 45 words. v3 had 17 links, 14 destinations and about 200 words. v1 had 22 links.

### 2. Header: one mega-nav, one small dropdown

- **Insights is a plain link.** The v3 dropdown (Latest, Reports and guides, Events, then Expertise with five themes) is gone. Type filters live on the Insights hub, exactly as Work filters live on the Work hub (v2, D-07). Expertise is reached from the mega-nav footer row, the site footer, the Home expertise row and the hub filters.
- **About dropdown: four items.** Our team, How we work, Values and culture, Careers. "About Manifesto" duplicated the About link itself.
- Header labels unchanged: What we do, Our work, Insights, About, Contact.

### 3. Mobile: two levels, not three

Menu opens to five rows. What we do expands once into a single flat list with three small pillar labels above their services (no sub-accordions). Then All services and Expertise. About expands once into four links. Our work, Insights and Contact are plain rows. The sectors block is removed from the menu; sectors are in the page footer on every device.

### 4. Homepage: six blocks, one row of expertise links, one triangle

| # | v3 | v4 |
|---|---|---|
| 1 | Hero with two CTAs | Hero: one line, one CTA (Contact), one text link (What we do). Client logos as a thin row inside the hero block. |
| 2 | Client logo strip | Folded into 1 |
| 3 | Triangle as three cards with Source B one-liners, plus a pyramid diagram and caption | Triangle as three blocks: label plus the same short pillar line as the mega-nav. No diagram. |
| 4 | Featured work, cards with service and theme tags | Work: three case studies, client and one-line result. No tags. |
| 5 | Expertise strip: five themes with one-line descriptors | Expertise: one heading line and five plain text links. This is the only row of topic links on the page. Cap is five. |
| 6 | Latest insights | Latest insights: three, title and date only. No tags. |
| 7 | Closing CTA | Closing CTA |

Home has one chip set (the five expertise links), one CTA path (Contact, repeated once at the bottom), and no sector, service or type tags anywhere.

### 5. Page chips: one dimension per page type, three visible

| Page type | The one dimension shown as chips | Cap | What moved or went |
|---|---|---|---|
| Service detail | Expertise (Related expertise block) | 3 | Previous / next service links cut. Related services stays as two or three cards, not chips. No sector chips. |
| Case study | Services used (hero) | 3 | Sector and theme chips removed from the hero. Both remain as CMS tags driving filters and auto modules. Related expertise appears once, at the foot, capped at 3. |
| Insight | Expertise (hero) | 3 | Related services block stays, max 2, as a block not chips. No sector chips. |
| Work hub cards | Service | 1 | Theme tag removed from cards. |
| Insights hub cards | Expertise | 1 | Type shown as a word in the meta line, not a chip. |
| Expertise theme | None | | "Sectors where this matters" row cut. Where we help is a list of services with a line each, not chips. |
| Sector landing | None | | "Themes that matter here" row cut. |
| Home | Expertise (one row) | 5 | See above. |

Work hub filters: Service is the one filter group open on load, grouped by pillar. Expertise and Sector sit behind a "More filters" control. Insights hub: Type open on load; Expertise, Service and Sector behind "More filters". Sectors belong in Work filters and the footer, not on every page.

### 6. Sitemap: one page cut, weights unchanged

- `/sectors/` (the sector index, Light) is cut. It duplicated the footer's Who we work with column. The footer heading becomes plain text; the four landings stay. Fixed pages at launch: 40, of which 11 are Canonical.
- Services stay Canonical, themes Supporting, sectors Light. No other page is added or removed.
- Otter is still honoured: "customer experience", "website", "research", "loyalty", "membership" and the rest are findable, but on service and expertise pages (H1, H2s, title tags, FAQs), not in the menu.

### 7. Mock: a quiet wireframe

`mocks/index.html` is rebuilt. Gone: the striped banner, the intro box, the review toggle and amber annotations, the behaviour notes, the sitemap legend and badges, the side notes next to the phone, the toast. What remains: one line of small grey text naming the file, three plain view switches (Navigation, Homepage, Mobile) and a plain-text sitemap list below the mobile view. The Navigation view opens with the mega-nav already open so density can be judged at a glance. Clicking a link writes its URL into the frame's address bar instead of popping a message.

---

## Old to new, structural changes only

| v3 | v4 |
|---|---|
| Mega-nav heading line "Our Growth Architecture" with strapline | Removed from the menu. Subheading on `/services/`; strapline in Home and hub heroes. |
| Column 1 items: Growth Strategy, Proposition Innovation | Heading Growth Strategy (link), item Proposition Innovation |
| Column 3 items: Side-by-Side, Meet the advisors | Heading CEO Advisory (link) with one line. No items. |
| 13 item subtitles | 2 quiet lines (Experience Engineering, Growth Office) |
| 3 pillar subtitles, seven to nine words | 3 pillar lines, four to six words |
| Footer row: All services, "Expertise: loyalty, membership, subscriptions, pricing, customer value", Contact | All services, Expertise, Contact |
| Insights: two-column dropdown | Insights: plain link |
| About dropdown: 5 items | 4 items (About Manifesto removed) |
| Mobile: three levels, subtitles, sectors block | Two levels, labels only plus the two quiet lines, no sectors block |
| Home: 7 blocks, pyramid diagram, tagged cards | 6 blocks, no diagram, no tags, one row of 5 expertise links |
| Case study hero: sector, services, themes | Services only, max 3 |
| Work hub: three filter groups open | Service open; Expertise and Sector behind More filters |
| `/sectors/` index page | Cut; footer heading is plain text |
| Mock: banner, intro, toggle, tabs, legend, notes, toast | One title line, three view switches, address bar shows the URL |

Nothing changed: the five header items; the three pillars and their order; the seven service labels and their slugs from v3; every URL except `/sectors/`; the weight of every remaining page; the canonical ownership and linking rules; the footer's four columns.

---

## Where the explanation went

The words v3 put in the menu are not lost. They moved to the place a visitor reads them when they want them.

| v3 menu text | v4 home |
|---|---|
| "Strategy that works. Execution that delivers." | Home hero, Services hub hero |
| Pillar subtitles (seven to nine words) | Shortened to four to six words; same three lines used on Home and the Services hub triangle (shared data) |
| "Customer experience (CX), website and digital design, build and testing" | Experience Engineering: quiet line "Customer experience and websites" in the menu; H2s "Customer experience (CX) design", "Website and digital product design and build", "User research and testing"; title tag "Experience Engineering: customer experience and websites" |
| "Interim growth team and programme office that gets strategy delivered" | Growth Office: quiet line "Interim growth team" in the menu; "programme office" in the page H2s and title tag |
| "Research, surveys, analytics and customer listening, faster with AI" | Customer Research and Insight page: H2s and meta description |
| "New offers and business models: loyalty, membership, subscription, direct-to-consumer" | Proposition Innovation page: H2 per proposition type, each linking to its expertise theme |
| "AI that cleans up customer data and improves marketing performance" | AI Agents for Marketing page: hero line and H2s |
| "How your teams, data and AI agents should work together" | Operating Model Design page: hero line |
| "AI skills, training and adoption: finding where AI pays off" | AI Enablement page: H2s |
| "Our advisory retainer: an experienced growth leader on call"; Side-by-Side; Meet the advisors | CEO Advisory page: hero names Side-by-Side; advisor profiles are the page's main block; Our team `#advisors` |
| Five theme names in the footer row and Insights dropdown | Home expertise row; site footer; `/expertise/` hub; Work and Insights filters |

---

## Tests v4 has to pass

1. Open the Navigation view of the mock. Name the three pillars without reading anything in grey. Under two seconds.
2. Count the words in the open mega-nav. Under fifty.
3. Open the Homepage view. Find the tag cloud. There is not one: five plain links in one row is the most topic links on the page.
4. On any page template in `03-page-layouts.md`, count the chip dimensions. One.
5. Look at the edges of the mock. No banner, no legend, no toggle, no note explaining the mock.

---

## What this does not do

- Does not reintroduce Expertise or Featured columns, or any fourth column.
- Does not rename any service. The v3 labels and slugs stand, pending Andy's sign-off on the three renames (still an open item).
- Does not invent offerings or pages. One page is removed (`/sectors/`); none are added.
- Does not create a Google Doc.
