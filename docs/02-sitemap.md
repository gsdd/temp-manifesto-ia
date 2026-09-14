# 02. Sitemap

Every URL on the site, grouped by section. Each entry has a slug, a page type (which maps to a template in `03-page-layouts.md`), a one-line purpose, and a weight.

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
- Service URLs are flat under `/services/` even though the nav groups them. Grouping is a presentation concern; flat URLs survive repackaging (see `06-decisions-log.md`, decision D-03).
- Filter and sort states use query strings (`?service=`, `?expertise=`, `?sector=`, `?type=`) and are never given their own paths.
- `{slug}` placeholders are filled from the CMS. Client case study slugs use the client name only (for example `/work/dayinsure/`).

---

## 1. Home

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/` | Home | Say who MGA is for, name the core offer, route visitors into Services, Expertise and Work within one screen. | Canonical |

Home is a page, not a hub. There are no child URLs under `/`. Every other section is a top-level path.

---

## 2. Services (What we do)

The SEO spine of the site. Every capability topic has exactly one canonical home here.

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/services/` | Service hub | Explain the triangle (Growth Strategy, Activation, CEO Advisory) and route to each service. | Canonical |
| `/services/growth-strategy/` | Service detail | The lead offer. Customer-led growth strategy for boards and exec teams. Owns the topic "growth strategy consultancy". | Canonical |
| `/services/proposition-innovation/` | Service detail | Designing and validating new propositions (the CIVD approach in Source B). Owns "proposition design / proposition innovation". | Canonical |
| `/services/activation/` | Service group | Explain what Activation means at MGA: taking a strategy into live execution with AI-powered tooling, not running operations forever. Lists the six activation services. | Supporting |
| `/services/customer-intelligence/` | Service detail | Customer research, segmentation, insight and value analytics that feed strategy and activation. Owns "customer intelligence / customer insight consultancy". | Canonical |
| `/services/experience-engineering/` | Service detail | Designing and building customer experiences, websites and journeys, with research built in. Written to be found for CX, website and research searches. Owns "experience engineering" and the CX / website / research cluster. | Canonical |
| `/services/data-agents/` | Service detail | AgentLab and the catalogue of data agents (reporting, data infrastructure, automation, QA, channel optimisation, test and learn, attribution, segmentation, CDP clean-up, tagging, journey mapping). Owns "data agents / AI agents for marketing and data teams". | Canonical |
| `/services/operating-architecture/` | Service detail | Adaptive operating models: data and tools, work units, orchestration culture, value streams combining humans and AI. Owns "operating model design / operating architecture". | Canonical |
| `/services/growth-office/` | Service detail | Interim growth experts embedded in the client team to build culture, capability and value. Owns "interim growth leadership / growth office". | Canonical |
| `/services/ai-enablement/` | Service detail | AI adoption, value cases and business model innovation. Owns "AI enablement consultancy". | Canonical |
| `/services/ceo-advisory/` | Service detail (downweighted) | Side-by-Side retainer for senior leaders. Personality-led, speed-dial access. Present for those who look for it; not promoted. | Supporting |

Notes:
- `/services/activation/` is a group page, not a service. It exists because "Activation" needs explaining and because the six services are sold as a set as often as individually. It is Supporting, not Canonical, because it owns no capability topic of its own.
- There is no `/services/growth-strategy-group/` equivalent. Growth Strategy is both the group name and the lead service; `/services/growth-strategy/` serves both roles.
- Individual data agents do not get their own URLs in v1. They are sections of `/services/data-agents/`. If AgentLab is later productised, agents can become Light pages under `/services/data-agents/{agent}/` (see `06-decisions-log.md`, decision D-11).

---

## 3. Expertise themes

The intersecting dimension. Each theme page answers "do you understand my problem?" and routes to the services that solve it, the work that proves it and the insights that explore it. Theme pages never describe how a service is delivered; they link to the service for that.

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/expertise/` | Expertise hub | Introduce the five growth themes and explain how they cut across services and sectors. | Supporting |
| `/expertise/loyalty/` | Expertise theme | Loyalty as a growth lever: what goes wrong, what good looks like, which MGA services apply, proof. | Supporting |
| `/expertise/membership/` | Expertise theme | Membership models and member economics. | Supporting |
| `/expertise/subscriptions/` | Expertise theme | Subscription growth, retention and churn. | Supporting |
| `/expertise/pricing/` | Expertise theme | Pricing strategy and value-based pricing. | Supporting |
| `/expertise/customer-value/` | Expertise theme | Customer lifetime value, value management and customer-led growth economics. | Supporting |

Notes:
- Five themes in v1. Adding a sixth requires at least two published case studies and two insights tagged to it, so the page is not thin on launch.
- Theme pages are indexable and target the theme as a problem space (for example "loyalty strategy consultancy"). They do not target service terms.

---

## 4. Sectors (Who we work with)

Light landings only. Each sector page is a short intro followed by filtered proof. There are no sector points of view, no sector-specific service descriptions, and no sector-specific insights sections beyond a filtered list.

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/sectors/` | Sector index | List the four sectors with client logos and a sentence each. | Light |
| `/sectors/financial-services/` | Sector light landing | Short intro, client logos, filtered case studies and insights for financial services. | Light |
| `/sectors/media/` | Sector light landing | As above for media and publishing. | Light |
| `/sectors/consumer/` | Sector light landing | As above for consumer brands, travel and leisure. | Light |
| `/sectors/retail/` | Sector light landing | As above for retail. | Light |

Notes:
- The four sectors follow Source A. Travel and leisure clients (Merlin, Parkdean, IAG) are grouped under Consumer for v1 rather than given a fifth sector. Technology clients (Meta, Microsoft) appear in Our work but do not justify a sector landing on launch (see `06-decisions-log.md`, decision D-08).
- A sector landing is indexed only when it has at least 150 words of unique intro, three published case studies and two insights tagged to it. Below that threshold it is noindex, follow (see `04-canonicals-and-seo.md`).

---

## 5. Our work

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/work/` | Work hub (filterable) | Every case study in one place, filterable by service, expertise and sector. The proof engine for the whole site. | Canonical |
| `/work/{client}/` | Case study | One engagement: challenge, approach, result, services used, themes, sector. Examples: `/work/dayinsure/`, `/work/key-group/`, `/work/transfergo/`, `/work/merlin/`, `/work/wsj/`, `/work/parkdean/`, `/work/tsb/`, `/work/post-office/`. | Supporting |
| `/work/?service={slug}` | Filtered view | Case studies for one service. Canonical to `/work/`. | Utility (noindex) |
| `/work/?expertise={slug}` | Filtered view | Case studies for one theme. Canonical to `/work/`. | Utility (noindex) |
| `/work/?sector={slug}` | Filtered view | Case studies for one sector. Canonical to `/work/`. | Utility (noindex) |

Notes:
- One case study per engagement. If a client has several engagements, either combine into one page with chapters or use `/work/{client}-{topic}/` (for example `/work/key-group-membership/`). Do not create a client hub.
- Case studies can be anonymised. Anonymised slugs describe the sector and outcome (for example `/work/uk-retail-bank-loyalty/`).
- Every case study must be tagged with at least one service. Expertise and sector tags are optional but expected.

---

## 6. Insights

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/insights/` | Insights hub (filterable) | All articles, reports and events, newest first, filterable by type, expertise, service and sector. | Supporting |
| `/insights/{slug}/` | Insight article | One piece of thinking. Tagged to services, themes and sectors so it surfaces on the right pages. | Supporting (Light if under 500 words or event listings) |
| `/insights/?type={article\|report\|event}` | Filtered view | Insights of one type. Canonical to `/insights/`. | Utility (noindex) |
| `/insights/?expertise={slug}` | Filtered view | Insights for one theme. Canonical to `/insights/`. | Utility (noindex) |
| `/newsletter/` | Newsletter sign-up | Capture email sign-ups for MGA's regular newsletter. | Utility (indexed) |

Notes:
- Reports and guides that need a download form use the same `/insights/{slug}/` template with a gated download module. No separate `/resources/` section.
- Events are insights of type "event" and expire from the hub's default list after the event date, remaining reachable by URL.
- No author archive pages. Authors link to their `/about/team/{name}/` profile instead.
- No tag or category archive pages. Filters replace them.

---

## 7. About

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/about/` | About | Who MGA is, the positioning (sustainable customer-led growth, strategy plus AI-powered activation), what makes the firm different, senior team preview. | Supporting |
| `/about/team/` | Team listing | Everyone client-facing, grouped by role, with advisors identified. | Supporting |
| `/about/team/{name}/` | Team profile | One person: role, focus, sectors, selected work, insights authored, contact route. Advisor profiles carry the Side-by-Side offer link. | Light |
| `/about/how-we-work/` | Methodology | Ways of working, frameworks, engagement models and what a typical engagement looks like. Kept separate from services so method is never mistaken for product. | Supporting |
| `/about/careers/` | Careers | Open roles and what it is like to work at MGA. | Light |

Notes:
- Team profiles exist for senior consultants and advisors. Junior team members can be listed on `/about/team/` without a profile page.
- Profiles are indexed because named-person searches are a real referral path. Profiles with fewer than 100 words of unique content are noindex until completed.

---

## 8. Contact

| URL | Page type | Purpose | Weight |
|---|---|---|---|
| `/contact/` | Contact | Enquiry form with a topic selector (service, theme or general), direct contact details, office address. | Utility (indexed) |
| `/contact/thank-you/` | Confirmation | Confirm the enquiry and suggest next reads. | Utility (noindex) |
| `/contact/?topic={slug}` | Pre-filled contact | Same page with the topic pre-selected. Canonical to `/contact/`. | Utility (noindex) |

---

## 9. Utility and system pages

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

## 10. Sitemap summary

| Section | Canonical | Supporting | Light | Utility |
|---|---|---|---|---|
| Home | 1 | | | |
| Services | 9 (hub + 8 details) | 2 (Activation group, CEO Advisory) | | |
| Expertise | | 6 (hub + 5 themes) | | |
| Sectors | | | 5 (index + 4 landings) | |
| Work | 1 (hub) | n (case studies) | | 3 filter patterns |
| Insights | | 1 (hub) + n (articles) | | 2 filter patterns, newsletter |
| About | | 3 (About, Team, How we work) | 1 (Careers) + n (profiles) | |
| Contact | | | | 2 pages + 1 pattern |
| System | | | | 8 |

Fixed pages at launch (excluding case studies, insights and profiles, and excluding filter patterns): 40, of which 11 are Canonical.

---

## 11. Pages deliberately not in the sitemap

| Excluded | Reason |
|---|---|
| Sector point-of-view pages (for example `/sectors/retail/loyalty-in-retail/`) | Client preference and the services-canonical rule. Sector content is a filter, not a destination. |
| Theme pages inside other sections (for example `/services/loyalty/`, `/insights/loyalty/`) | Themes have one home at `/expertise/`. Everything else links to it. |
| Home child pages (for example `/why-manifesto/`) | Home is a page, not a hub. That content belongs on `/about/`. |
| Separate CX, UX, website or research service pages | These are entry keywords for `/services/experience-engineering/`, not separate offers. |
| Methodology pages under `/services/` | Method is not a product. Lives at `/about/how-we-work/`. |
| Client hub pages (`/work/{client}/` with children) | One engagement, one page. |
| Author, tag and category archives | Filters and team profiles cover these needs without thin pages. |
| A separate AgentLab microsite or `/agentlab/` | AgentLab is the named product inside Data Agents. A redirect from `/agentlab/` to `/services/data-agents/` is acceptable for marketing use. |
