# Proposed website information architecture

**To:** Andy
**From:** Gary
**Re:** Manifesto Growth Architects site structure, navigation and wireframe

This is the proposed information architecture for the new site: what it contains, how it is organised, how people move through it, and which page owns which topic. It is built around your Growth Architecture triangle, in language a prospect who has never heard of Manifesto would actually use.

The current site works as a credibility check after a referral. This rebuild has to originate enquiries from people who have not.

A clickable wireframe of the whole sitemap sits in the repo. How to open it is at the end.

---

## Primary navigation

Six items in the header, plus the logo and a Contact button:

**What we do** | **Our work** | **Our thinking** | **About** | **Careers** | **Contact**

That is the cap. Nothing else joins the top bar. Careers is first-class so Contact can honestly split “work with us” from “work for us”. Our thinking is Manifesto’s name for the insights library. About is a small dropdown: Our people, Our approach, Values and culture.

What we do is the only mega-nav. It is your triangle, laid flat, in the order we agreed: Growth Strategy first, Activation Services second, CEO Advisory third and quieter.

---

## What we do: the triangle as a menu

Each column is a **hub**. The group title is a link, with a visible arrow, so it is obvious you can open the pillar page. Under it, **strands** sit as siblings.

| Growth Strategy | Activation Services | CEO Advisory |
|---|---|---|
| Where and how you grow | Turning strategy into results | One-to-one support for leaders |
| Overview | Overview | Side-by-Side |
| Proposition Innovation | Customer Research and Insight | Our advisors |
| | Experience Engineering *(Customer experience and websites)* | |
| | AI Agents for Marketing | |
| | Operating Model Design | |
| | Growth Office *(Interim growth team)* | |
| | AI Enablement | |

A thin row under the three columns: All services, Expertise.

Growth Strategy is both the pillar and the lead service: Overview is the hub page, Proposition Innovation is the child. Activation is the fat column because that is where most of the buyable work lives; Overview goes to the group page that explains the bridge from strategy to results and helps someone pick which of the six they need. CEO Advisory shows both strands: **Side-by-Side** (the retainer) and **Our advisors** (the people). The column is still quieter by width and type. We are not designing the site around it, but it is visibly a pillar.

Experience Engineering and Growth Office keep a short quiet line (websites, CX; interim growth team). Everything else stands alone. Deck one-liners, the AgentLab catalogue and methodology live on pages, not in the menu.

Services stay **flat** under `/services/`. Grouping is a menu concern. URLs survive if the packaging changes.

---

## How the rest of the site is organised

Three dimensions, one home each.

**Services are the spine.** Every capability topic has one canonical page. The services hub is the Growth Architecture page: it names the system, shows how the three pillars connect (“Strategy first. Activation to deliver it. Advisors alongside.”), and offers a second way in by problem (“Where are you starting from?” with seven situations).

**Expertise themes are supporting.** Loyalty, Membership, Subscriptions, Pricing, Customer Value. Real pages and cross-links, one Expertise link in the menu footer, and a row of five names on Home. They prove you understand the growth problem, then hand off to services. They are not a second mega-nav column.

**Sectors are light.** Financial services, Media, Consumer, Retail. Footer, filters, and a short landing each. Not in the header. Proof that you have worked with businesses like mine lives in case studies, not in a clients section competing with work.

Our work is the proof engine. Testimonials live inside cases. Our thinking is reports, articles, events and news. Method (how you partner, named frameworks, engagement shapes) sits on Our approach, not in What we do.

One rule throughout: one canonical page per important topic. Everything else links in and out.

---

## Home, and where thinking sits

Home is a page, not a hub. It should answer, in order: who you are for, what you do, that you have a point of view, that you can prove it.

1. **Hero** with the positioning line from the deck, plus a showreel placeholder (still or visual at launch; film later).
2. **Trusted partners**, high: client logos, not buried.
3. **What we do**: the three pillars, the connecting line, a link through to Growth Architecture.
4. **Our thinking**: one featured report and one article, then “All thinking”.
5. **Our work**, with a quote sitting with the cases.
6. **Awards**, including FT, lower on the page, not in the hero.
7. **Growth problems we know best**: the five theme names as plain links.
8. **Contact**.

Thinking is not a dump at the bottom. After the offer and before cases is the point: you have a view, then you can prove delivery. It is still a teaser. The library lives on Our thinking. We are not replicating a reports grid on Home.

---

## Modules worth calling out

**Showreel and trusted partners.** Social proof sits high. Awards do not. FT is real; it is just not the first thing.

**CIVD.** Customer, Innovation, Value and Delivery is still in the deck as the Growth Strategy frame. It is an on-page module: a four-part diagram on Growth Strategy, and a compact version on the Services hub under that pillar. It is named once, with a link, on Our approach. It is not a nav item, not a Home block, and not a page of its own. If the frame is later replaced, those modules change and no URL has to.

**Named frameworks** each have one home: Growth Architecture on the services hub, CIVD on Growth Strategy, Operating Architecture on Operating Model Design, AgentLab on AI Agents for Marketing, Side-by-Side on CEO Advisory. Our approach lists them once. Method is never sold as a product. Growth partner language and the partner films live there too, not as a sold service in the menu.

---

## Careers and Contact

Careers is in the header so it is not nested under About and then asked to do employer and client jobs at once.

**Our people** is the client-facing listing, including Side-by-Side advisors. **Careers** is Life at Manifesto, DEI, benefits and open roles, plus a route for people who want to join even if a listed role is not open. **Contact** splits **Work with us** and **Work for us**. The Nutshell sits in the footer and on Contact.

Life at Manifesto and Meet the team stay on separate pages, with a cross-link.

---

## The wireframe

There is a full-site clickable wireframe so you can walk the structure rather than imagine it.

In the repo: open `mocks/index.html` in a browser. No build step, no login. Click through as you would on the live site. Greyscale placeholders, not a visual design. The left column is the page. The right column is working notes for us (weight, keywords, headings). Those notes are not a proposal for the live site.

Useful starting clicks: Home, What we do (hover the mega-nav, then land on All services), Growth Strategy (CIVD), CEO Advisory (Side-by-Side and advisors), Our thinking, Careers, Contact.

---

## Language and search

Nav labels are Manifesto labels, in plain English: what a prospect would type, not coined names where those names fight search. Customer Research and Insight, AI Agents for Marketing and Operating Model Design sit in the menu; Customer Intelligence, Data Agents and Operating Architecture are named on the page. Side-by-Side is a strand and a page term; SxS is not used on the site.

UK search demand has informed quiet lines, H1 support and H2s (CX and websites under Experience Engineering; interim growth team under Growth Office). It has not been allowed to rewrite the top nav.

---

## Open questions

Three that still need a view from you. Everything else can be decided in copy and CMS.

1. **C and N members.** Placeholder on About and Our people. Named network, membership body, or internal group? We will not invent a sold service around it.
2. **Growth Collective.** On the current site. Footer, a strand under Our thinking, or drop? Out of the header on purpose.
3. **Events.** Recaps sit as a section on Our thinking for now. A separate page only if there is enough content to sustain it.

Happy to walk the wireframe with you. The structure is stable enough to brief content, design and build against; the open items above do not block that.
