# 02. Sitemap (v4)

Every URL on the site, grouped by section. Each entry has a slug, a page type (which maps to a template in `03-page-layouts.md`), a one-line purpose, and a weight.

The structure follows Source A (Gary's suggested IA). The services taxonomy follows Source B (Andy's Growth Architecture triangle). Weighting follows Source C and Source D: Growth Strategy first, Activation second, CEO Advisory third and quieter, themes real but calm, sectors light. Service names and slugs follow the v3 wording pass (Source C, Source E). See `nav-wording-decisions.md`.

v4 (Source F, `v4-simplification.md`) does not explode or reshape the sitemap. One page is cut: the sector index `/sectors/`, which duplicated the footer (D-44). Weights are unchanged: services Canonical, themes Supporting, sectors Light. Fixed pages at launch go from 41 to 40.

Related: `diagrams/sitemap.md` shows this structure as a tree.

---

## Weight definitions

| Weight | Meaning | Content expectation | Indexed | SEO investment |
|---|---|---|---|---|
| **Canonical** | The single page that owns a topic. Everything else on the site that mentions the topic links here. | Full, unique, regularly maintained. Typically 800 to 1,500 words plus modules. | Yes | High. Target keywords, structured data, internal links pointed here. |
| **Supporting** | Substantial, indexable content that strengthens the canonicals by adding proof, context or a different entry point. Never restates a canonical. | Unique, 400 to 1,000 words plus modules. | Yes | Medium. Owns secondary or long-tail terms. Links up to canonicals. |
| **Light** | A short landing or listing that mostly aggregates and routes. Exists for findability and filtering, not as an SEO destination. | 150 to 300 words of unique intro, then aggregated modules. | Yes, if the content threshold is met. Otherwise noindex until it is. | Low. No dedicated keyword targets. |
| **Utility** | Functional pages needed to run the site. | Whatever the function needs. | Mostly no | None |

Rule of thumb: services are Canonical, expertise themes and work are Supporting, sectors are Light.

---

## URL conventions

- Lowercase, words separated by hyphens, trailing slash on all directory-style pages.
- No dates, IDs or file extensions in slugs.
- Maximum depth is three levels below the root (for example `/about/team/{name}/`).
- Service URLs are flat under `/services/` even though the nav groups them by pillar. Grouping is a presentation concern; flat URLs survive repackaging (`06-decisions-log.md`, D-12).
- A service slug is the plain, searched form of its nav label. When a label is renamed, the slug follows and the old slug becomes a 301 (`04-canonicals-and-seo.md`, section 7).
- Filter and sort states use query strings (`?service=`, `?expertise=`, `?sector=`, `?type=`) and are never given their own paths.
- `{slug}` placeholders are filled from the CMS. Client case study slugs use the client name only (for example `/work/dayinsure/`).

---

## 1. Home

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/` | Home | Say who MGA is for, show the Growth Architecture triangle, route into services, work and insights within one screen. | Canonical |

Home is a page, not a hub (Source A). There are no child URLs under `/`. Every other section is a top-level path. Home is reached by the logo.

---

## 2. What we do: Services

The SEO spine of the site and the home of the triangle. Every capability topic has exactly one canonical page here.

Source A suggested a separate Growth Architecture page alongside a services hub. v2 merges them: `/services/` **is** the Growth Architecture page. One hub, the triangle on it, the services under it (`06-decisions-log.md`, D-03).

| URL | Page type | Pillar | Purpose | Weight |
|---|---|---|---|---|
| `/services/` | Services hub (Growth Architecture) | All three | Present the triangle: Growth Strategy, Activation Services, CEO Advisory. Route to every service. Carries the Growth Architecture positioning from Source B ("Strategy that works. Execution that delivers."). | Canonical |
| `/services/growth-strategy/` | Service detail | Growth Strategy | The lead offer (Source C: bread and butter). Customer value growth strategy: where to play, how to win. Home of the CIVD frame (Customer, Innovation, Value, Delivery) from the Source B Growth Strategy slide. Owns "growth strategy consultancy". | Canonical |
| `/services/proposition-innovation/` | Service detail | Growth Strategy | Designing new value propositions that grow sustainable customer value: loyalty, membership, subscription and D2C propositions (Source C). Owns "proposition design / proposition innovation". | Canonical |
| `/services/activation/` | Service group | Activation Services | Explain Activation in plain terms: hands-on delivery that turns strategy into results, AI-powered and human-led, not ongoing operations (Source C). Lists the six services. | Supporting |
| `/services/customer-research/` | Service detail | Activation Services | **Customer Research and Insight** (deck: Customer Intelligence). AI-powered research, surveys, analytics and customer listening. Insight projects and intelligence capabilities (Source B). Owns "customer research / customer insight consultancy / market research / voice of the customer". "Customer Intelligence" is named on the page as the practice. | Canonical |
| `/services/experience-engineering/` | Service detail | Activation Services | **Experience Engineering**. Finding, redesigning, testing and scaling experiences that drive disproportionate value. Customer experience (CX), website and digital design, build and testing (Source B). Written so customer experience, website and research searches land here (Source C). Owns "experience engineering" and the CX / website / digital product cluster. | Canonical |
| `/services/ai-agents-for-marketing/` | Service detail | Activation Services | **AI Agents for Marketing** (deck: Data Agents). AI that cleans up customer data and improves marketing performance, guided by experts. AgentLab and the agent catalogue (Source B). Owns "AI agents for marketing / marketing AI / customer data quality / data agents". "Data Agents" and "AgentLab" are named on the page. | Canonical |
| `/services/operating-model-design/` | Service detail | Activation Services | **Operating Model Design** (deck: Operating Architecture / Operating Models). How teams, data and AI agents work together: grounded in customer value, fuelled by data, redesigned around humans and AI agents, orchestrated for impact (Source B). Owns "operating model design / operating model consultancy / operating architecture". | Canonical |
| `/services/growth-office/` | Service detail | Activation Services | **Growth Office**. Interim growth team and programme office bridging strategy and delivery through culture, capability and value (Source B). Owns "growth office / interim growth leadership / transformation programme office". | Canonical |
| `/services/ai-enablement/` | Service detail | Activation Services | **AI Enablement**. AI skills, training and adoption; finding where AI pays off; business model innovation (Source B). Owns "AI enablement / AI adoption / AI training for leadership teams". | Canonical |
| `/services/ceo-advisory/` | Service detail (third pillar, quieter) | CEO Advisory | **CEO Advisory**. Side-by-Side named in the hero. One-to-one advice for CEOs and senior leaders from experienced growth leaders, retainer-based, virtual or in person (Source B). Surfaces advisor profiles as its main block; this is the route to the advisors now that the mega-nav item is cut (D-36). Present and visible as the third pillar; not promoted above the other two. "SxS" is not used on the site. | Supporting |

Notes:
- `/services/activation/` is a group page, not a service. It exists because "Activation" is MGA's own term and needs explaining, and because the six services are sold as a set as often as individually. It is Supporting because it owns no capability topic of its own.
- There is no Growth Strategy group page. Growth Strategy is both the pillar name and the lead service; `/services/growth-strategy/` serves both roles.
- There is no separate CEO Advisory group page. `/services/ceo-advisory/` is the pillar and the offer.
- Individual data agents do not get their own URLs. They are catalogue entries on `/services/ai-agents-for-marketing/` (`06-decisions-log.md`, D-15).
- Three slugs changed in v3 with their labels: `/services/customer-intelligence/` became `/services/customer-research/`, `/services/data-agents/` became `/services/ai-agents-for-marketing/`, `/services/operating-architecture/` became `/services/operating-model-design/`. The v2 slugs are listed as redirects in `04-canonicals-and-seo.md`, section 7.
- Marketing shortcuts `/growth-architecture/`, `/agentlab/`, `/data-agents/` and `/side-by-side/` are redirects, not pages (see `04-canonicals-and-seo.md`, section 7).

---

## 3. Expertise themes

The intersecting dimension (Source A). Each theme page answers "do you understand my problem?" and routes to the services that solve it, the work that proves it and the insights that explore it. Theme pages never describe how a service is delivered.

Themes are the expertise story: "loyalty and membership experts who work cross-sector", not "FS experts who do loyalty" (Source C).

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/expertise/` | Expertise hub | Introduce the five growth themes and show how they cut across services and sectors. | Supporting |
| `/expertise/loyalty/` | Expertise theme | Loyalty as a growth lever: what goes wrong, what good looks like, which services apply, proof. | Supporting |
| `/expertise/membership/` | Expertise theme | Membership models and member economics. | Supporting |
| `/expertise/subscriptions/` | Expertise theme | Subscription growth, retention and churn. | Supporting |
| `/expertise/pricing/` | Expertise theme | Pricing strategy and value-based pricing. | Supporting |
| `/expertise/customer-value/` | Expertise theme | Customer lifetime value, value management and customer-led growth economics. | Supporting |

Notes:
- Five themes at launch. Adding a sixth requires at least two published case studies and two insights tagged to it.
- Theme pages are indexable and target the theme as a problem space (for example "loyalty strategy consultancy"). They do not target service terms.
- Nav weight is deliberately lower than in v1: themes are reached from one "Expertise" link in the mega-nav footer row, the Home expertise row, the footer, and the More filters on Work and Insights (`06-decisions-log.md`, D-04, D-38). The v3 Insights dropdown that also listed them is gone.
- The visitor-facing label for this section is "Expertise" (footer heading, footer-row link). "Expertise themes" is the IA name for the dimension. The URL stays `/expertise/`.

---

## 4. Sectors (Who we work with)

Light landings only (Source C: sector-agnostic services, no sector POV pages; Gary: light landings for SEO and AI search, H1 plus proof, buried a bit, no children).

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/sectors/financial-services/` | Sector light landing | Short intro, client logos, filtered case studies and insights. | Light |
| `/sectors/media/` | Sector light landing | As above for media and publishing. | Light |
| `/sectors/consumer/` | Sector light landing | As above for consumer brands, travel and leisure. | Light |
| `/sectors/retail/` | Sector light landing | As above for retail. | Light |

Notes:
- Four sectors from Source A. Travel and leisure clients (Merlin, Parkdean, IAG) sit under Consumer. Technology clients (Meta, Microsoft) appear in Our work without a sector landing (`06-decisions-log.md`, D-09).
- **There is no `/sectors/` index page** (v4, D-44). v3 had one as the footer heading target; it duplicated the footer's own list. The footer heading "Who we work with" is plain text, and `/sectors/` redirects to `/work/` (`04-canonicals-and-seo.md`, section 7).
- A sector landing is indexed only when it has at least 150 words of unique intro, three published case studies and two insights tagged to it. Below that it is noindex, follow.
- No pages under a sector. Ever.

---

## 5. Our work

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/work/` | Work hub (filterable) | Every case study in one place. Service filter open on load; expertise and sector behind More filters (D-43). Testimonials live inside case studies (Source A). | Canonical |
| `/work/{client}/` | Case study | One engagement: challenge, approach, result, quote, services used, themes, sector. Examples from Source B: `/work/dayinsure/`, `/work/key-group/`, `/work/transfergo/`, `/work/merlin/`, `/work/wsj/`, `/work/parkdean/`, `/work/tsb/`, `/work/post-office/`, `/work/mars/`, `/work/bbc/`. | Supporting |
| `/work/?service={slug}` | Filtered view | Case studies for one service. Canonical to `/work/`. | Utility (noindex) |
| `/work/?expertise={slug}` | Filtered view | Case studies for one theme. Canonical to `/work/`. | Utility (noindex) |
| `/work/?sector={slug}` | Filtered view | Case studies for one sector. Canonical to `/work/`. | Utility (noindex) |

Notes:
- One case study per engagement. If a client has several engagements, combine into one page with chapters or use `/work/{client}-{topic}/`. Do not create a client hub.
- Case studies can be anonymised. Anonymised slugs describe the sector and outcome (for example `/work/uk-retail-bank-loyalty/`).
- Every case study must be tagged with at least one service. Expertise and sector tags are optional but expected.
- No separate testimonials page (Source A: redundant).

---

## 6. Insights

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/insights/` | Insights hub (filterable) | All articles, reports and events, newest first ("latest" is a section, not a page, per Source A). Type filter open on load; expertise, service and sector behind More filters (D-43). This is where the v3 Insights dropdown's type links now live (D-38). | Supporting |
| `/insights/{slug}/` | Insight | One article, report or event. Tagged to services, themes and sectors. | Supporting (Light if under 500 words or an event listing) |
| `/insights/?type={article\|report\|event}` | Filtered view | Insights of one type. Canonical to `/insights/`. | Utility (noindex) |
| `/insights/?expertise={slug}` | Filtered view | Insights for one theme. Canonical to `/insights/`. | Utility (noindex) |
| `/newsletter/` | Newsletter sign-up | Capture email sign-ups. | Utility (indexed) |

Notes:
- Reports that need a download form use the same `/insights/{slug}/` template with a gated download module. No separate `/resources/` section.
- Events are insights of type "event" and drop out of the default list after the event date, remaining reachable by URL.
- No author, tag or category archive pages. Filters and team profiles cover these.
- Any insight on loyalty links back to `/expertise/loyalty/` (Source A).

---

## 7. About

Source A asked for a clear About hub and a clear Careers hub instead of "Life at Manifesto" doing both jobs. v2 follows that split.

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/about/` | About | Who we are and our story: the positioning (sustainable customer-led growth, strategy plus AI-powered activation), what makes MGA different, senior team preview. | Supporting |
| `/about/team/` | Team listing | Everyone client-facing, grouped by role. Side-by-Side advisors are a named group with the anchor `#advisors`, linked from the CEO Advisory page (no longer from the mega-nav, D-36). | Supporting |
| `/about/team/{name}/` | Team profile | One person: role, focus, selected work, insights authored, contact route. Advisor profiles carry the Side-by-Side link. | Light |
| `/about/how-we-work/` | Methodology | Ways of working, frameworks, engagement models. Kept separate from services so method is never mistaken for product (Source A). | Supporting |
| `/about/values/` | Values and culture | Values, culture and DEI on one page (Source A lists Values / Culture and DEI; combined to avoid two thin pages). | Light |

Notes:
- Team profiles exist for senior consultants and advisors. Junior team members can be listed on `/about/team/` without a profile page.
- Profiles are indexed because named-person searches are a real referral path. Profiles under 100 words are noindex until completed.
- Advisor profiles matter (Source C: showcase heavyweight advisor profiles). They are the substance behind the third pillar.

---

## 8. Careers

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/careers/` | Careers hub | Life at Manifesto, benefits and the current open roles on one page. | Light |
| `/careers/{role}/` | Role | One open role with how to apply. | Light (noindex when closed) |

Notes:
- Source A lists Life at Manifesto, Benefits and Open Roles as children of Careers. At MGA's size these are sections of one page, not three pages. If the roles list grows past ten, split `/careers/roles/` out.
- Careers is not in the header. It is reached from the About dropdown and the footer.

---

## 9. Contact

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/contact/` | Contact | Enquiry form with a topic selector (service, theme or general), direct contact details, office address. | Utility (indexed) |
| `/contact/thank-you/` | Confirmation | Confirm the enquiry and suggest next reads. | Utility (noindex) |
| `/contact/?topic={slug}` | Pre-filled contact | Same page with the topic pre-selected. Canonical to `/contact/`. | Utility (noindex) |

---

## 10. Utility and system pages

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/privacy-policy/` | Legal | Privacy notice. | Utility (indexed) |
| `/cookie-policy/` | Legal | Cookie notice and preferences. | Utility (indexed) |
| `/terms/` | Legal | Website terms of use. | Utility (indexed) |
| `/accessibility/` | Legal | Accessibility statement. | Utility (indexed) |
| `/search/` | Search results | Site search. | Utility (noindex) |
| `/404/` | Error | Not found page with links to Services, Work and Contact. | Utility (noindex) |
| `/sitemap.xml` | System | XML sitemap listing all indexable URLs. | Utility |
| `/robots.txt` | System | Crawl directives. | Utility |

---

## 11. Sitemap summary

| Section | Canonical | Supporting | Light | Utility |
|---|---|---|---|---|
| Home | 1 | | | |
| Services | 9 (hub + 8 details) | 2 (Activation group, CEO Advisory) | | |
| Expertise | | 6 (hub + 5 themes) | | |
| Sectors | | | 4 (landings; no index) | |
| Work | 1 (hub) | n (case studies) | | 3 filter patterns |
| Insights | | 1 (hub) + n (insights) | | 2 filter patterns, newsletter |
| About | | 3 (About, Team, How we work) | 1 (Values) + n (profiles) | |
| Careers | | | 1 (hub) + n (roles) | |
| Contact | | | | 2 pages + 1 pattern |
| System | | | | 8 |

Fixed pages at launch (excluding case studies, insights, profiles, roles and filter patterns): 40, of which 11 are Canonical. v3 had 41; the sector index was cut in v4.

---

## 12. Pages deliberately not in the sitemap

| Excluded | Reason |
|---|---|
| A separate `/growth-architecture/` page | Merged into `/services/`. One hub carries the triangle. `/growth-architecture/` redirects there. |
| A `/sectors/` index page | Cut in v4 (D-44). It listed the four sectors, which the footer already does. `/sectors/` redirects to `/work/`. |
| A separate `/side-by-side/` or advisors page | Side-by-Side is the CEO Advisory offer and is named on `/services/ceo-advisory/`; the advisors are that page's main block and a group on `/about/team/`. `/side-by-side/` redirects. |
| A separate CIVD page | CIVD is the Growth Strategy frame (Source B). It is a module on `/services/growth-strategy/` and is explained once in How we work. |
| Sector point-of-view pages (for example `/sectors/retail/loyalty-in-retail/`) | Source C: sector-agnostic services. Sector content is a filter and a light landing, not a destination. |
| Theme pages inside other sections (for example `/services/loyalty/`, `/insights/loyalty/`) | Themes have one home at `/expertise/`. Everything else links to it (Source A's one-canonical-home rule). |
| Home child pages (for example `/why-manifesto/`) | Home is a page, not a hub. That content belongs on `/about/`. |
| Separate CX, UX or website service pages | Entry keywords for `/services/experience-engineering/`, not separate offers. The page's hero line, H2 sections and title tag carry them (and the menu's quiet line "Customer experience and websites"). |
| A separate "research" or "market research" page | Customer research is `/services/customer-research/`; user research and testing is an H2 of Experience Engineering. Two homes already; a third would compete. |
| Pages under the deck names (`/services/customer-intelligence/`, `/services/data-agents/`, `/services/operating-architecture/`) | Renamed in v3 to the searched terms. The deck slugs are 301s, not pages. |
| A generic `/services/ai/` page | "AI" is caught by two labels (AI Agents for Marketing, AI Enablement) plus the Customer Research and Operating Model Design hero lines. A generic AI page would be thin and compete with them. |
| Methodology pages under `/services/` | Method is not a product. Lives at `/about/how-we-work/`. |
| A separate testimonials page | Testimonials live inside case studies (Source A). |
| Client hub pages (`/work/{client}/` with children) | One engagement, one page. |
| Author, tag and category archives | Filters and team profiles cover these needs without thin pages. |
| A separate AgentLab microsite or `/agentlab/` page | AgentLab is the named product inside AI Agents for Marketing. `/agentlab/` redirects to `/services/ai-agents-for-marketing/`. |
| Separate Life at Manifesto, Benefits and Open roles pages | Sections of `/careers/` at current scale. |
