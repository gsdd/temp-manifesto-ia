#!/usr/bin/env python3
"""Generate the clickable full-site IA wireframe and docs/heading-map.md.

Single source of heading maps, chips and page shells so the HTML and the
markdown map cannot drift. Run from repo root: python3 mocks/_build.py
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOCKS = Path(__file__).resolve().parent
DOCS = ROOT / "docs"


def file_dir(url: str) -> str:
    if url == "/":
        return "."
    return url.strip("/")


def rel_href(from_url: str, to_url: str) -> str:
    frag = ""
    if "#" in to_url:
        to_url, frag = to_url.split("#", 1)
        frag = "#" + frag
    if to_url != "/" and not to_url.endswith("/"):
        to_url += "/"
    src = file_dir(from_url)
    dst = "index.html" if to_url == "/" else to_url.strip("/") + "/index.html"
    return os.path.relpath(dst, src) + frag


def asset(from_url: str, name: str) -> str:
    return os.path.relpath("assets/" + name, file_dir(from_url))


def crumbs_html(from_url: str, crumbs: list[tuple[str, str | None]]) -> str:
    if not crumbs:
        return ""
    items = []
    for label, url in crumbs:
        if url:
            items.append(f'<li><a href="{rel_href(from_url, url)}">{label}</a></li>')
        else:
            items.append(f"<li>{label}</li>")
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def chips_html(page: dict) -> str:
    chips = [f'<span class="chip weight">{page["weight"]}</span>']
    if page.get("primary"):
        chips.append(f'<span class="chip kw">Primary: {page["primary"]}</span>')
    else:
        chips.append('<span class="chip muted">Primary: no keyword target</span>')
    if page.get("quiet"):
        chips.append(f'<span class="chip quiet">Quiet line: {page["quiet"]}</span>')
    for label, items in (
        ("Themes", page.get("themes") or []),
        ("Sectors", page.get("sectors") or []),
        ("Services", page.get("services") or []),
    ):
        if not items:
            continue
        links = ", ".join(
            f'<a href="{rel_href(page["url"], u)}">{n}</a>' for n, u in items
        )
        chips.append(f'<span class="chip">{label}: {links}</span>')
    return (
        '<div class="ia-chips" aria-label="Page chips">'
        '<span class="label">Page chips</span>'
        f'<div class="chips">{"".join(chips)}</div>'
        "</div>"
    )


def heading_map_html(page: dict) -> str:
    alts = page.get("alts") or []
    alts_html = (
        "<ul>" + "".join(f"<li>{a}</li>" for a in alts) + "</ul>"
        if alts
        else "<p class=\"map-note\">None in this pull, or not a search page.</p>"
    )
    h2s = page.get("h2s") or []
    h3s = page.get("h3s") or []
    h2_html = "<ol>" + "".join(f"<li>{x}</li>" for x in h2s) + "</ol>" if h2s else "<p class=\"map-note\">None.</p>"
    h3_html = "<ul>" + "".join(f"<li>{x}</li>" for x in h3s) + "</ul>" if h3s else "<p class=\"map-note\">None required.</p>"
    primary = page.get("primary") or "none"
    return f"""
<aside class="heading-map" aria-label="Outside page / SEO heading map">
  <h2>Outside page / SEO heading map</h2>
  <p class="map-note">Annotation for content and SEO. Not part of the live page. UK volumes from DataForSEO, Sep 2026. One-line intent only; not body copy.</p>
  <p class="k"><strong>URL</strong><code>{page["url"]}</code></p>
  <p class="k"><strong>H1 (one)</strong>{page["h1"]}</p>
  <p class="k"><strong>Primary keyword</strong>{primary}</p>
  <div class="k"><strong>Alts (2 to 4)</strong>{alts_html}</div>
  <div class="k"><strong>H2s (ordered)</strong>{h2_html}</div>
  <div class="k"><strong>H3s where useful</strong>{h3_html}</div>
  <p class="intent"><strong>Intent.</strong> {page["intent"]}</p>
</aside>
"""


def header_html(from_url: str, section: str) -> str:
    h = lambda u: rel_href(from_url, u)

    def current(name: str) -> str:
        return ' aria-current="page"' if section == name else ""

    return f"""
      <div class="header-zone">
        <header class="site-header" id="siteHeader" data-mega-open="false">
          <a class="logo" href="{h("/")}">MGA logo</a>
          <ul class="primary-nav" id="primaryNav">
            <li data-menu="mega">
              <a class="top-link" href="{h("/services/")}" aria-haspopup="true" aria-expanded="false"{current("services")}>What we do <span class="caret">&#9660;</span></a>
            </li>
            <li><a class="top-link plain" href="{h("/work/")}"{current("work")}>Our work</a></li>
            <li><a class="top-link plain" href="{h("/insights/")}"{current("insights")}>Insights</a></li>
            <li data-menu="about">
              <a class="top-link" href="{h("/about/")}" aria-haspopup="true" aria-expanded="false"{current("about")}>About <span class="caret">&#9660;</span></a>
              <div class="dropdown" role="region" aria-label="About menu">
                <ul>
                  <li><a href="{h("/about/team/")}">Our team</a></li>
                  <li><a href="{h("/about/how-we-work/")}">How we work</a></li>
                  <li><a href="{h("/about/values/")}">Values and culture</a></li>
                  <li><a href="{h("/careers/")}">Careers</a></li>
                </ul>
              </div>
            </li>
          </ul>
          <a class="btn" href="{h("/contact/")}"{current("contact")}>Contact</a>
        </header>
        <div class="mega" id="megaNav" role="region" aria-label="What we do menu">
          <div class="mega-inner">
            <div class="mega-cols">
              <div class="pillar">
                <h3><a href="{h("/services/growth-strategy/")}">Growth Strategy</a></h3>
                <p class="line">Where and how you grow</p>
                <ul>
                  <li><a href="{h("/services/proposition-innovation/")}">Proposition Innovation</a></li>
                </ul>
              </div>
              <div class="pillar">
                <h3><a href="{h("/services/activation/")}">Activation Services</a></h3>
                <p class="line">Turning strategy into results</p>
                <ul>
                  <li><a href="{h("/services/customer-research/")}">Customer Research and Insight</a></li>
                  <li><a href="{h("/services/experience-engineering/")}">Experience Engineering<small>Customer experience and websites</small></a></li>
                  <li><a href="{h("/services/ai-agents-for-marketing/")}">AI Agents for Marketing</a></li>
                  <li><a href="{h("/services/operating-model-design/")}">Operating Model Design</a></li>
                  <li><a href="{h("/services/growth-office/")}">Growth Office<small>Interim growth team</small></a></li>
                  <li><a href="{h("/services/ai-enablement/")}">AI Enablement</a></li>
                </ul>
              </div>
              <div class="pillar quiet">
                <h3><a href="{h("/services/ceo-advisory/")}">CEO Advisory</a></h3>
                <p class="line">One-to-one support for leaders</p>
                <ul>
                  <li><a href="{h("/services/ceo-advisory/#advisors")}">Our advisors</a></li>
                </ul>
              </div>
            </div>
            <div class="mega-row">
              <a href="{h("/services/")}">All services</a>
              <a href="{h("/expertise/")}">Expertise</a>
            </div>
          </div>
        </div>
      </div>
"""


def footer_html(from_url: str) -> str:
    h = lambda u: rel_href(from_url, u)
    return f"""
      <footer class="site-footer">
        <div class="footer-cols">
          <div>
            <h4>What we do</h4>
            <ul>
              <li><a href="{h("/services/growth-strategy/")}">Growth Strategy</a></li>
              <li><a href="{h("/services/proposition-innovation/")}">Proposition Innovation</a></li>
              <li><a href="{h("/services/customer-research/")}">Customer Research and Insight</a></li>
              <li><a href="{h("/services/experience-engineering/")}">Experience Engineering</a></li>
              <li><a href="{h("/services/ai-agents-for-marketing/")}">AI Agents for Marketing</a></li>
              <li><a href="{h("/services/operating-model-design/")}">Operating Model Design</a></li>
              <li><a href="{h("/services/growth-office/")}">Growth Office</a></li>
              <li><a href="{h("/services/ai-enablement/")}">AI Enablement</a></li>
              <li><a href="{h("/services/ceo-advisory/")}">CEO Advisory</a></li>
              <li><a href="{h("/services/")}">All services</a></li>
            </ul>
          </div>
          <div>
            <h4>Expertise</h4>
            <ul>
              <li><a href="{h("/expertise/loyalty/")}">Loyalty</a></li>
              <li><a href="{h("/expertise/membership/")}">Membership</a></li>
              <li><a href="{h("/expertise/subscriptions/")}">Subscriptions</a></li>
              <li><a href="{h("/expertise/pricing/")}">Pricing</a></li>
              <li><a href="{h("/expertise/customer-value/")}">Customer Value</a></li>
            </ul>
          </div>
          <div>
            <h4>Who we work with</h4>
            <ul>
              <li><a href="{h("/sectors/financial-services/")}">Financial services</a></li>
              <li><a href="{h("/sectors/media/")}">Media</a></li>
              <li><a href="{h("/sectors/consumer/")}">Consumer</a></li>
              <li><a href="{h("/sectors/retail/")}">Retail</a></li>
            </ul>
          </div>
          <div>
            <h4>Company</h4>
            <ul>
              <li><a href="{h("/about/")}">About</a></li>
              <li><a href="{h("/about/team/")}">Our team</a></li>
              <li><a href="{h("/about/how-we-work/")}">How we work</a></li>
              <li><a href="{h("/about/values/")}">Values and culture</a></li>
              <li><a href="{h("/careers/")}">Careers</a></li>
              <li><a href="{h("/work/")}">Our work</a></li>
              <li><a href="{h("/insights/")}">Insights</a></li>
              <li><a href="{h("/newsletter/")}">Newsletter</a></li>
              <li><a href="{h("/contact/")}">Contact</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <span>Company registration line</span>
          <a href="{h("/privacy-policy/")}">Privacy policy</a>
          <a href="{h("/cookie-policy/")}">Cookie policy</a>
          <a href="{h("/terms/")}">Terms</a>
          <a href="{h("/accessibility/")}">Accessibility statement</a>
          <span>Social links</span>
        </div>
      </footer>
"""


def wrap(page: dict, body: str) -> str:
    url = page["url"]
    section = page["section"]
    title = page["title"]
    sitemap = os.path.relpath("sitemap.html", file_dir(url))
    css = asset(url, "wireframe.css")
    js = asset(url, "nav.js")
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Manifesto Growth Architects (IA wireframe)</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="top">
  <span>MGA website IA. Wireframe, not design. Click through the site; the right-hand panel is the SEO heading map.</span>
  <span><a href="{sitemap}">All pages</a></span>
</div>
<div class="layout">
  <div class="browser" id="browser" data-mega-open="false">
    <div class="bar"><span class="url">manifestogrowth.example{url}</span></div>
    <div class="scrim"></div>
    {header_html(url, section)}
    {crumbs_html(url, page.get("crumbs") or [])}
    {chips_html(page)}
    <main class="page" id="main">
      {body}
    </main>
    {footer_html(url)}
  </div>
  {heading_map_html(page)}
</div>
<script src="{js}"></script>
</body>
</html>
"""


def card(h, href, title, sub, extra=""):
    cls = "card flat" if extra == "flat" else ("card person" if extra == "person" else "card")
    ph = '<div class="avatar"></div>' if extra == "person" else ('<div class="ph"></div>' if extra == "ph" else "")
    return f'<a class="{cls}" href="{h(href)}">{ph}<strong>{title}</strong><span>{sub}</span></a>'


def closing(h, line="Tell us about your growth challenge"):
    return f"""
        <section class="block closing">
          <p>{line}</p>
          <a class="btn" href="{h("/contact/")}">Contact</a>
        </section>
"""


# ---------------------------------------------------------------------------
# Page registry: heading maps + chips. Bodies are built in body_for().
# ---------------------------------------------------------------------------

T = lambda n, u: (n, u)

PAGES: list[dict] = [
    dict(
        url="/",
        title="Home",
        section="home",
        weight="Canonical",
        primary="growth architecture (~50) / brand",
        alts=["Manifesto Growth Architects (brand)", "customer-led growth (positioning, not a target)"],
        quiet=None,
        themes=[T("Loyalty", "/expertise/loyalty/"), T("Membership", "/expertise/membership/"), T("Subscriptions", "/expertise/subscriptions/"), T("Pricing", "/expertise/pricing/"), T("Customer Value", "/expertise/customer-value/")],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("Activation Services", "/services/activation/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Manifesto partner with ambitious leaders to deliver sustainable, customer-led growth.",
        h2s=["What we do", "Our work", "Growth problems we know best", "Latest insights"],
        h3s=[],
        intent="Brand and router. Name who you are for, show the triangle, send people into services, work and insights. Not a service keyword page.",
        crumbs=[],
        kind="home",
    ),
    dict(
        url="/services/",
        title="What we do: our Growth Architecture",
        section="services",
        weight="Canonical",
        primary="growth architecture (~50)",
        alts=["strategy that works / execution that delivers (strapline, not a volume target)", "growth strategy (~480) caught on the lead service page, not here"],
        quiet=None,
        themes=[T("Expertise hub", "/expertise/")],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("Activation Services", "/services/activation/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Our Growth Architecture",
        h2s=["Three ways we work with you", "Where are you starting from?", "Growth Strategy", "Activation Services", "CEO Advisory"],
        h3s=[],
        intent="Name the system. Two ways in: capability (triangle) and problem (seven situations). Do not target individual service terms here.",
        crumbs=[("Home", "/"), ("What we do", None)],
        kind="hub",
    ),
    dict(
        url="/services/growth-strategy/",
        title="Growth Strategy",
        section="services",
        weight="Canonical",
        primary="growth strategy (~480)",
        alts=["growth strategy consultancy / consultant (~70)", "brand strategy consulting (~390) where true to the offer", "go to market strategy (~880) where true to the offer"],
        quiet=None,
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/"), T("Pricing", "/expertise/pricing/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Proposition Innovation", "/services/proposition-innovation/"), T("Activation Services", "/services/activation/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Growth Strategy",
        h2s=["Why this, now", "What we do", "North Star", "Growth priorities", "Demand signals", "Scenario planning", "Customer, Innovation, Value and Delivery", "Proof", "How it works"],
        h3s=["Customer", "Innovation", "Value", "Delivery"],
        intent="Lead offer. Keep the nav label. H2s take brand / GTM language only where the work is truly that. CIVD is the named frame.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Growth Strategy", None)],
        kind="service",
        hero="Customer-led growth strategy: where to focus and how to win",
        who="For leadership teams deciding where and how to grow.",
        aka=None,
        numbers=None,
        pillar=None,
        situations=[
            "We need to decide where and how to grow",
            "Growth is uneven and we cannot agree the bets",
            "We have a plan, but not a North Star the business will follow",
        ],
    ),
    dict(
        url="/services/proposition-innovation/",
        title="Proposition Innovation",
        section="services",
        weight="Canonical",
        primary="value proposition design (~140)",
        alts=["value proposition (broad, noisy)", "proposition design (~20)", "brand proposition (~90)"],
        quiet="Value proposition design",
        themes=[T("Loyalty", "/expertise/loyalty/"), T("Membership", "/expertise/membership/"), T("Subscriptions", "/expertise/subscriptions/")],
        sectors=[T("Retail", "/sectors/retail/"), T("Consumer", "/sectors/consumer/"), T("Financial services", "/sectors/financial-services/")],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("Customer Research and Insight", "/services/customer-research/")],
        h1="Proposition Innovation",
        h2s=["Why this, now", "Value proposition design", "Loyalty propositions", "Membership propositions", "Subscription propositions", "Direct-to-consumer propositions", "Proof", "How it works"],
        h3s=[],
        intent="Keep Manifesto label in the H1. Put value / proposition design in the quiet line, hero and H2s so search can see it. Each proposition type hands off to its theme.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Proposition Innovation", None)],
        kind="service",
        hero="New offers and business models: loyalty, membership, subscription, direct-to-consumer",
        who="For teams who need a new offer, not only a new campaign.",
        aka=None,
        numbers=None,
        pillar=("Part of Growth Strategy", "/services/growth-strategy/"),
        situations=[
            "We need a new proposition, loyalty or membership offer",
            "The offer is no longer worth what we charge",
            "We want to go direct to consumer without breaking the brand",
        ],
    ),
    dict(
        url="/services/activation/",
        title="Activation Services",
        section="services",
        weight="Supporting",
        primary="strategy to execution (group page; no single volume target)",
        alts=["customer journey mapping (~2,900) in the Experience Engineering line", "operating model (~880) in the Operating Model Design line", "interim CMO / interim growth team (~110 to 140) in the Growth Office line"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[
            T("Customer Research and Insight", "/services/customer-research/"),
            T("Experience Engineering", "/services/experience-engineering/"),
            T("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
            T("Operating Model Design", "/services/operating-model-design/"),
            T("Growth Office", "/services/growth-office/"),
            T("AI Enablement", "/services/ai-enablement/"),
        ],
        h1="Activation Services",
        h2s=["The bridge from strategy to results", "Which of the six do you need?", "The six Activation services"],
        h3s=[],
        intent="Explain Activation and route. Catch problem-minded searchers in the six lines (journey mapping, operating model, interim leadership) without owning those terms.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", None)],
        kind="activation",
        hero="Hands-on delivery that turns strategy into results",
        who="For teams whose strategy is not showing up in the numbers.",
    ),
    dict(
        url="/services/customer-research/",
        title="Customer Research and Insight",
        section="services",
        weight="Canonical",
        primary="customer research methods / companies (~720)",
        alts=["customer journey mapping (~2,900)", "customer research techniques (~880)", "customer research agency (~20)"],
        quiet=None,
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Experience Engineering", "/services/experience-engineering/"), T("Proposition Innovation", "/services/proposition-innovation/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/")],
        h1="Customer Research and Insight",
        h2s=["Why this, now", "Customer research methods", "Customer journey mapping", "Research projects", "Always-on customer insight", "Proof", "How it works"],
        h3s=["Digital listening", "Qualitative research", "Quantitative research", "Customer data analytics", "Internal knowledge", "External market data"],
        intent="Label stays. Lead with methods, journey mapping and insight outcomes, not only the consultancy noun. Customer Intelligence is the practice name on the page.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Customer Research and Insight", None)],
        kind="service",
        hero="Research, surveys, analytics and customer listening, faster with AI",
        who="For teams who need one version of the customer truth.",
        aka="Our Customer Intelligence practice",
        numbers=None,
        pillar=("Part of Activation Services", "/services/activation/"),
        situations=[
            "We need to understand our customers better",
            "Every team has a different version of the customer",
            "Research is slow, and the so-what arrives too late",
        ],
    ),
    dict(
        url="/services/experience-engineering/",
        title="Experience Engineering: customer experience and websites",
        section="services",
        weight="Canonical",
        primary="experience engineering (~90), with CX / journey H2s",
        alts=["customer journey mapping (~2,900)", "cx consultancy (~70)", "website design consultancy (~70)", "experience design agency (~110)"],
        quiet="Customer experience and websites",
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Customer Research and Insight", "/services/customer-research/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/")],
        h1="Experience Engineering",
        h2s=["Why this, now", "Find", "Redesign", "Test", "Scale", "Customer experience (CX) design", "Website and digital product", "User research and testing", "Proof"],
        h3s=["Customer and value analytics (under research and testing)"],
        intent="Keep the Manifesto label. Quiet line and H2s do the CX, website and journey-mapping job (Dayinsure / Key Group pattern). Find / Redesign / Test / Scale is How it works from the deck.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Experience Engineering", None)],
        kind="service",
        hero="Customer experience (CX), website and digital design, build and testing",
        who="For teams whose journeys or website are not converting.",
        aka=None,
        numbers="Over 3x EBITDA return on investment, consistently",
        pillar=("Part of Activation Services", "/services/activation/"),
        situations=[
            "Our journeys or website are not converting",
            "We know the experience is the problem, not the offer",
            "We need to find, fix, test and scale the journeys that matter",
        ],
    ),
    dict(
        url="/services/ai-agents-for-marketing/",
        title="AI Agents for Marketing",
        section="services",
        weight="Canonical",
        primary="ai marketing agents (~390)",
        alts=["ai agents for marketing (~70)", "marketing automation consultancy (~90)", "do not use bare ai agents (~9,900) as the sole target"],
        quiet=None,
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("AI Enablement", "/services/ai-enablement/"), T("Operating Model Design", "/services/operating-model-design/"), T("Customer Research and Insight", "/services/customer-research/")],
        h1="AI Agents for Marketing",
        h2s=["Why this, now", "What we do", "AgentLab", "How it works", "Proof"],
        h3s=["Reporting and Analytics", "Data and Infrastructure", "Strategy and Planning", "Automation and Execution"],
        intent="Stay marketing-qualified. AgentLab is the named catalogue on this page, not in the nav. Bare 'AI agents' is too generic to be the sole target.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("AI Agents for Marketing", None)],
        kind="service",
        hero="AI-powered performance marketing, guided by experts",
        who="For marketing teams whose customer data is holding performance back.",
        aka="Data Agents, built in AgentLab",
        numbers="4 weeks to audit your data. 6 weeks to your first agents.",
        pillar=("Part of Activation Services", "/services/activation/"),
        situations=[
            "Our customer data is a mess and marketing cannot trust it",
            "We want AI agents doing the marketing work, not another slide",
            "We have tools, but no agents tied to a clear ROI",
        ],
    ),
    dict(
        url="/services/operating-model-design/",
        title="Operating Model Design",
        section="services",
        weight="Canonical",
        primary="operating model (~880)",
        alts=["target operating model (~1,600)", "operating model design (~140)", "operating model consultancy (~10)"],
        quiet=None,
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/")],
        services=[T("Growth Office", "/services/growth-office/"), T("AI Enablement", "/services/ai-enablement/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/")],
        h1="Operating Model Design",
        h2s=["Why this, now", "Target operating model", "Adaptive operating model", "Our Operating Architecture framework", "Proof", "How it works"],
        h3s=["High-quality data and tools", "New work units", "Orchestration: culture, value, capability"],
        intent="Strongest Activation volume case after journey / CX. Use operating model / target operating model language in H1 support and H2s. Operating Architecture is the framework name on the page.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Operating Model Design", None)],
        kind="service",
        hero="How your teams, data and AI agents should work together",
        who="For leaders who need a new way of working, not a new tool.",
        aka="Our Operating Architecture framework",
        numbers=None,
        pillar=("Part of Activation Services", "/services/activation/"),
        situations=[
            "We are experimenting with AI, but the operating model has not moved",
            "Work is stuck between teams, data and new tools",
            "We need a target operating model that can still change",
        ],
    ),
    dict(
        url="/services/growth-office/",
        title="Growth Office: interim growth team and programme office",
        section="services",
        weight="Canonical",
        primary="interim cmo / interim growth team (~110 to 140)",
        alts=["growth office (~10, weak; do not primary-target)", "programme office / PMO (hero language)", "interim activation then embed (deck shape)"],
        quiet="Interim growth team",
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Operating Model Design", "/services/operating-model-design/"), T("CEO Advisory", "/services/ceo-advisory/"), T("AI Enablement", "/services/ai-enablement/")],
        h1="Growth Office",
        h2s=["Why this, now", "Interim growth team", "Then embed", "Culture", "Capability", "Value", "Proof", "How it works"],
        h3s=["Interim CMO and senior cover (where the engagement needs it)"],
        intent="Keep Growth Office as the label. Quiet line and body must say interim / embedded growth team, and interim CMO where accurate. Do not SEO-target 'growth office' as the primary phrase.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Growth Office", None)],
        kind="service",
        hero="Interim growth team and programme office that gets strategy delivered",
        who="For leadership teams who need strategy executed and the value tracked.",
        aka=None,
        numbers=None,
        pillar=("Part of Activation Services", "/services/activation/"),
        situations=[
            "The strategy is agreed, but it is not being delivered",
            "We need an interim growth team, not a permanent hire yet",
            "Value is not showing up against the plan",
        ],
    ),
    dict(
        url="/services/ai-enablement/",
        title="AI Enablement",
        section="services",
        weight="Canonical",
        primary="ai enablement (~170)",
        alts=["ai transformation consultancy (~10)", "ai adoption / skills (supporting copy; no volume in this pull for 'ai adoption consultancy')", "where AI pays off (value cases, plain language)"],
        quiet=None,
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Consumer", "/sectors/consumer/"), T("Media", "/sectors/media/")],
        services=[T("AI Agents for Marketing", "/services/ai-agents-for-marketing/"), T("Operating Model Design", "/services/operating-model-design/")],
        h1="AI Enablement",
        h2s=["Why this, now", "AI skills and adoption", "Finding where AI pays off", "New business models with AI", "Proof", "How it works"],
        h3s=[],
        intent="Thin but real niche. Own 'AI enablement' as primary. Support with adoption, skills and operating-change copy. Expert network named in body.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("AI Enablement", None)],
        kind="service",
        hero="AI skills, training and adoption: finding where AI pays off",
        who="For organisations experimenting with AI who need a structured path to value.",
        aka=None,
        numbers=None,
        pillar=("Part of Activation Services", "/services/activation/"),
        situations=[
            "We want AI to pay off",
            "People are using tools, but there is no shared way of working",
            "We need to know which workflows are worth changing",
        ],
    ),
    dict(
        url="/services/ceo-advisory/",
        title="CEO Advisory",
        section="services",
        weight="Supporting",
        primary="ceo advisory (~10)  /  relationship page, not volume-led",
        alts=["board advisor (~90), adjacent", "ceo coach (~320), adjacent only, not identical to Side-by-Side", "executive advisor (~30)"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("Growth Office", "/services/growth-office/")],
        h1="CEO Advisory",
        h2s=["Why this, now", "What we do", "Our advisors", "How the retainer works"],
        h3s=["Side-by-Side (named in the hero and this section, not in the nav)"],
        intent="Nav stays CEO Advisory. Proof is the people. Coaching language is adjacent, not the offer. SxS is not used on the site.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("CEO Advisory", None)],
        kind="ceo",
        hero="One-to-one support for leaders. Side-by-Side.",
        who="For CEOs and senior leaders who want a sounding board they trust.",
    ),
    dict(
        url="/expertise/",
        title="Expertise",
        section="services",
        weight="Supporting",
        primary="growth problems we know best (hub; theme titles not fully keyworded in this pull)",
        alts=["loyalty / membership / subscriptions / pricing / customer value (second pass before URLs lock if they need a search job)"],
        quiet=None,
        themes=[T("Loyalty", "/expertise/loyalty/"), T("Membership", "/expertise/membership/"), T("Subscriptions", "/expertise/subscriptions/"), T("Pricing", "/expertise/pricing/"), T("Customer Value", "/expertise/customer-value/")],
        sectors=[],
        services=[T("All services", "/services/")],
        h1="Our expertise",
        h2s=["The growth problems we know best", "Latest insights across themes"],
        h3s=[],
        intent="Index the five themes. Do not restate how services are delivered. Themes were not fully keyworded in the Sep 2026 pull.",
        crumbs=[("Home", "/"), ("Expertise", None)],
        kind="expertise-hub",
    ),
]

# Theme pages
for slug, name, view, help_svcs, primary, alts, h2s in [
    (
        "loyalty",
        "Loyalty",
        "Most loyalty programmes reward behaviour the customer would have shown anyway.",
        [
            ("Proposition Innovation", "/services/proposition-innovation/", "Design the loyalty offer and the economics behind it"),
            ("Customer Research and Insight", "/services/customer-research/", "Measure who is loyal, and why"),
            ("Experience Engineering", "/services/experience-engineering/", "Build the journeys that make the programme felt"),
        ],
        "loyalty strategy / loyalty programme (not in this UK pull)",
        ["loyalty economics (theme POV, not a service)", "related service terms live on Proposition Innovation and Customer Research"],
        ["Our view", "Where we help", "Proof", "Insights"],
    ),
    (
        "membership",
        "Membership",
        "Membership only works when the member gets more valuable over time, not when the card gets more discounts.",
        [
            ("Proposition Innovation", "/services/proposition-innovation/", "Design the membership model"),
            ("Customer Research and Insight", "/services/customer-research/", "Member needs and economics"),
            ("Growth Strategy", "/services/growth-strategy/", "Where membership sits in the growth bets"),
        ],
        "membership models / member economics (not in this UK pull)",
        ["hands off 'how we design the offer' to Proposition Innovation"],
        ["Our view", "Where we help", "Proof", "Insights"],
    ),
    (
        "subscriptions",
        "Subscriptions",
        "Subscription growth fails in the same places: weak reason to stay, fuzzy value, and churn spotted too late.",
        [
            ("Proposition Innovation", "/services/proposition-innovation/", "The subscription offer"),
            ("Customer Research and Insight", "/services/customer-research/", "Retention and churn insight"),
            ("Experience Engineering", "/services/experience-engineering/", "Join, use and renew journeys"),
        ],
        "subscription growth / churn / retention (not in this UK pull)",
        ["theme owns the problem; services own the how"],
        ["Our view", "Where we help", "Proof", "Insights"],
    ),
    (
        "pricing",
        "Pricing",
        "Price is a growth decision, not only a finance one. Value-based pricing needs a proposition the customer will pay for.",
        [
            ("Growth Strategy", "/services/growth-strategy/", "Where price sits in the growth bets"),
            ("Proposition Innovation", "/services/proposition-innovation/", "The offer that can hold the price"),
            ("Customer Research and Insight", "/services/customer-research/", "Willingness to pay and value analytics"),
        ],
        "pricing strategy / value-based pricing (not in this UK pull)",
        ["do not turn this into a pricing-consultancy product page"],
        ["Our view", "Where we help", "Proof", "Insights"],
    ),
    (
        "customer-value",
        "Customer Value",
        "Customer-led growth is an economics problem: which customers create value, and which experiences move it.",
        [
            ("Growth Strategy", "/services/growth-strategy/", "Where value growth comes from"),
            ("Customer Research and Insight", "/services/customer-research/", "Value analytics and segmentation"),
            ("Experience Engineering", "/services/experience-engineering/", "Journeys that move customer value"),
        ],
        "customer lifetime value / customer value management (not in this UK pull)",
        ["customer-led growth language also lives on Growth Strategy"],
        ["Our view", "Where we help", "Proof", "Insights"],
    ),
]:
    PAGES.append(dict(
        url=f"/expertise/{slug}/",
        title=name,
        section="services",
        weight="Supporting",
        primary=primary,
        alts=alts,
        quiet=None,
        themes=[],
        sectors=[],
        services=[(a, b) for a, b, _ in help_svcs],
        h1=name,
        h2s=h2s,
        h3s=[],
        intent="Prove we understand the problem, then hand off to services. Never describe how a service is delivered. Theme titles were not fully keyworded in this pull.",
        crumbs=[("Home", "/"), ("Expertise", "/expertise/"), (name, None)],
        kind="theme",
        view=view,
        help_svcs=help_svcs,
    ))

for slug, name, intro, used in [
    (
        "financial-services",
        "Financial services",
        "Banks, insurers and specialist lenders. Quote journeys, member and policyholder value, and the operating models behind them. Proof, not a sector point of view.",
        [
            ("Experience Engineering", "/services/experience-engineering/"),
            ("Customer Research and Insight", "/services/customer-research/"),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
        ],
    ),
    (
        "media",
        "Media",
        "Publishers and media groups. Subscriptions, membership, and getting strategy delivered in newsroom-adjacent businesses. Proof, not a sector point of view.",
        [
            ("Growth Office", "/services/growth-office/"),
            ("Operating Model Design", "/services/operating-model-design/"),
            ("Proposition Innovation", "/services/proposition-innovation/"),
        ],
    ),
    (
        "consumer",
        "Consumer",
        "Consumer brands, travel and leisure. Short-break, park and travel journeys, and the loyalty and membership offers around them. Proof, not a sector point of view.",
        [
            ("Experience Engineering", "/services/experience-engineering/"),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
            ("Growth Office", "/services/growth-office/"),
        ],
    ),
    (
        "retail",
        "Retail",
        "Retailers who need offers, journeys and value economics that work in store and direct. Proof, not a sector point of view.",
        [
            ("Proposition Innovation", "/services/proposition-innovation/"),
            ("Customer Research and Insight", "/services/customer-research/"),
            ("Experience Engineering", "/services/experience-engineering/"),
        ],
    ),
]:
    PAGES.append(dict(
        url=f"/sectors/{slug}/",
        title=name,
        section="work",
        weight="Light",
        primary="no dedicated keyword target (light landing)",
        alts=["sector + consultancy queries are opportunistic only", "proof lives on case studies"],
        quiet=None,
        themes=[],
        sectors=[],
        services=used,
        h1=name,
        h2s=["Clients", "Case studies", "Services most used here"],
        h3s=[],
        intent="Reassure 'businesses like mine'. Short intro plus filtered proof. No sector POV essay. No sector-specific service descriptions.",
        crumbs=[("Home", "/"), (name, None)],
        kind="sector",
        intro=intro,
    ))

PAGES += [
    dict(
        url="/work/",
        title="Our work",
        section="work",
        weight="Canonical",
        primary="case studies (proof engine; not a service keyword)",
        alts=["client-name searches land on individual case studies"],
        quiet=None,
        themes=[],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/"), T("Retail", "/sectors/retail/")],
        services=[T("Experience Engineering", "/services/experience-engineering/"), T("Growth Strategy", "/services/growth-strategy/")],
        h1="Our work",
        h2s=["Featured", "All case studies"],
        h3s=[],
        intent="Proof hub. Service filter open on load. Expertise and sector behind More filters. No testimonials page.",
        crumbs=[("Home", "/"), ("Our work", None)],
        kind="work-hub",
    ),
    dict(
        url="/work/dayinsure/",
        title="Dayinsure",
        section="work",
        weight="Supporting",
        primary="client-name / proof (not a service keyword)",
        alts=["Experience Engineering is the canonical for the capability"],
        quiet=None,
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Financial services", "/sectors/financial-services/")],
        services=[T("Experience Engineering", "/services/experience-engineering/"), T("Customer Research and Insight", "/services/customer-research/")],
        h1="Dayinsure",
        h2s=["At a glance", "The challenge", "What we did", "The result"],
        h3s=[],
        intent="Shell for an Experience Engineering engagement. Links to service, theme and sector. Testimonials live here.",
        crumbs=[("Home", "/"), ("Our work", "/work/"), ("Dayinsure", None)],
        kind="case",
        client="Dayinsure",
        result="Quote journey rebuilt; conversion and value up (figure TBC)",
        sector_name="Financial services",
        sector_url="/sectors/financial-services/",
    ),
    dict(
        url="/work/key-group/",
        title="Key Group",
        section="work",
        weight="Supporting",
        primary="client-name / proof (not a service keyword)",
        alts=["Experience Engineering is the canonical for the capability"],
        quiet=None,
        themes=[T("Loyalty", "/expertise/loyalty/"), T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Financial services", "/sectors/financial-services/")],
        services=[T("Experience Engineering", "/services/experience-engineering/"), T("Proposition Innovation", "/services/proposition-innovation/")],
        h1="Key Group",
        h2s=["At a glance", "The challenge", "What we did", "The result"],
        h3s=[],
        intent="Second case-study shell. Same template as Dayinsure. Tags drive the auto modules on service, theme and sector pages.",
        crumbs=[("Home", "/"), ("Our work", "/work/"), ("Key Group", None)],
        kind="case",
        client="Key Group",
        result="Experience and offer working as one (figure TBC)",
        sector_name="Financial services",
        sector_url="/sectors/financial-services/",
    ),
    dict(
        url="/insights/",
        title="Insights",
        section="insights",
        weight="Supporting",
        primary="thought leadership hub (long-tail lives on articles)",
        alts=["type filters are query strings, not pages"],
        quiet=None,
        themes=[T("Loyalty", "/expertise/loyalty/")],
        sectors=[],
        services=[],
        h1="Insights",
        h2s=["Latest", "All insights"],
        h3s=[],
        intent="Filterable hub. Latest is a section, not a page. Type filter open on load.",
        crumbs=[("Home", "/"), ("Insights", None)],
        kind="insights-hub",
    ),
    dict(
        url="/insights/loyalty-without-the-discount/",
        title="Loyalty without the discount",
        section="insights",
        weight="Supporting",
        primary="long-tail loyalty thinking (hands off to the theme)",
        alts=["canonical problem page is /expertise/loyalty/"],
        quiet=None,
        themes=[T("Loyalty", "/expertise/loyalty/")],
        sectors=[T("Retail", "/sectors/retail/")],
        services=[T("Proposition Innovation", "/services/proposition-innovation/")],
        h1="Loyalty without the discount",
        h2s=["The problem", "What we think", "How we help"],
        h3s=[],
        intent="Article shell. Dated point of view. Theme page stays the evergreen position. Related services as a block, not extra nav.",
        crumbs=[("Home", "/"), ("Insights", "/insights/"), ("Loyalty without the discount", None)],
        kind="insight",
    ),
    dict(
        url="/about/",
        title="About",
        section="about",
        weight="Supporting",
        primary="Manifesto Growth Architects (brand)",
        alts=["Growth Architecture as named system lives on /services/"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("Our Growth Architecture", "/services/")],
        h1="About Manifesto Growth Architects",
        h2s=["Who we are and our story", "What makes us different", "Leadership", "How we work"],
        h3s=[],
        intent="Story and positioning. Method is a teaser to How we work. Not a service page.",
        crumbs=[("Home", "/"), ("About", None)],
        kind="about",
    ),
    dict(
        url="/about/team/",
        title="Our team",
        section="about",
        weight="Supporting",
        primary="named-person search (profiles); this page is the listing",
        alts=["Our advisors in the mega-nav land on CEO Advisory, not here"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Our team",
        h2s=["Leadership", "Consultants", "Side-by-Side advisors", "Associates and expert network"],
        h3s=[],
        intent="Everyone client-facing. Advisors group is present; mega-nav Our advisors still lands on the offer page.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("Our team", None)],
        kind="team",
    ),
    dict(
        url="/about/team/advisor-one/",
        title="Advisor name",
        section="about",
        weight="Light",
        primary="named-person search",
        alts=["offer described on CEO Advisory, not here"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Advisor name",
        h2s=["Biography", "Focus", "Selected work"],
        h3s=[],
        intent="Profile shell. Advisor note links back to Side-by-Side on the CEO Advisory page.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("Our team", "/about/team/"), ("Advisor name", None)],
        kind="profile",
    ),
    dict(
        url="/about/how-we-work/",
        title="How we work",
        section="about",
        weight="Supporting",
        primary="methodology (not a product; no service keyword)",
        alts=["Growth Architecture, CIVD, Operating Architecture, AgentLab, Side-by-Side each have one anchored home"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="How we work",
        h2s=["Principles", "Engagement shapes", "Frameworks and tools", "Working with AI"],
        h3s=["Growth Architecture", "Customer, Innovation, Value and Delivery", "Operating Architecture", "AgentLab", "Side-by-Side"],
        intent="Method is never a product. Named frameworks listed once here, each linking to its anchored service-page home.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("How we work", None)],
        kind="how",
    ),
    dict(
        url="/about/values/",
        title="Values and culture",
        section="about",
        weight="Light",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Values and culture",
        h2s=["Values", "Culture", "Diversity, equity and inclusion"],
        h3s=[],
        intent="Light culture page. Careers is the jobs destination.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("Values and culture", None)],
        kind="values",
    ),
    dict(
        url="/careers/",
        title="Careers",
        section="about",
        weight="Light",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Careers at Manifesto",
        h2s=["Life at Manifesto", "Benefits", "Open roles"],
        h3s=[],
        intent="Life, benefits and roles on one page at current scale.",
        crumbs=[("Home", "/"), ("Careers", None)],
        kind="careers",
    ),
    dict(
        url="/careers/growth-architect/",
        title="Growth Architect",
        section="about",
        weight="Light",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Growth Architect",
        h2s=["About the role", "How to apply"],
        h3s=[],
        intent="Role shell. noindex when closed.",
        crumbs=[("Home", "/"), ("Careers", "/careers/"), ("Growth Architect", None)],
        kind="role",
    ),
    dict(
        url="/contact/",
        title="Contact",
        section="contact",
        weight="Utility",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Contact",
        h2s=["Get in touch", "Direct contact"],
        h3s=[],
        intent="Enquiry form. Topic selector can be pre-filled from ?topic=.",
        crumbs=[("Home", "/"), ("Contact", None)],
        kind="contact",
    ),
    dict(
        url="/contact/thank-you/",
        title="Thank you",
        section="contact",
        weight="Utility",
        primary="none (noindex)",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("What we do", "/services/"), T("Our work", "/work/")],
        h1="Thank you",
        h2s=["While you wait"],
        h3s=[],
        intent="Confirmation only. Suggest a service, a case and an insight.",
        crumbs=[("Home", "/"), ("Contact", "/contact/"), ("Thank you", None)],
        kind="thanks",
    ),
    dict(
        url="/newsletter/",
        title="Newsletter",
        section="insights",
        weight="Utility",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Newsletter",
        h2s=["Sign up"],
        h3s=[],
        intent="Email capture. Indexed utility.",
        crumbs=[("Home", "/"), ("Newsletter", None)],
        kind="legal",
        blurb="Short sign-up. Insights keep an inline route here.",
    ),
]

for slug, name, blurb in [
    ("privacy-policy", "Privacy policy", "Privacy notice shell."),
    ("cookie-policy", "Cookie policy", "Cookie notice and preferences shell."),
    ("terms", "Terms", "Website terms of use shell."),
    ("accessibility", "Accessibility statement", "Accessibility statement shell."),
    ("search", "Search", "Site search results. noindex."),
]:
    PAGES.append(dict(
        url=f"/{slug}/",
        title=name,
        section="home",
        weight="Utility",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1=name,
        h2s=[],
        h3s=[],
        intent=blurb + " Not a search destination.",
        crumbs=[("Home", "/"), (name, None)],
        kind="legal",
        blurb=blurb,
    ))

PAGES.append(dict(
    url="/404/",
    title="Page not found",
    section="home",
    weight="Utility",
    primary="none (noindex)",
    alts=[],
    quiet=None,
    themes=[],
    sectors=[],
    services=[T("What we do", "/services/"), T("Our work", "/work/"), T("Contact", "/contact/")],
    h1="Page not found",
    h2s=[],
    h3s=[],
    intent="Error page with routes to Services, Work and Contact.",
    crumbs=[("Home", "/"), ("Page not found", None)],
    kind="notfound",
))


def body_for(page: dict) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    kind = page["kind"]

    if kind == "home":
        return f"""
        <section class="block hero">
          <h1>{page["h1"]}</h1>
          <p>Strategy that works. Execution that delivers.</p>
          <div class="cta">
            <a class="btn" href="{h("/contact/")}">Contact</a>
            <a class="text" href="{h("/services/")}">What we do</a>
          </div>
          <div class="logos" aria-label="Client logos"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
        </section>
        <section class="block">
          <h2 class="sec">What we do</h2>
          <div class="tri">
            <a href="{h("/services/growth-strategy/")}"><strong>Growth Strategy</strong><span>Where and how you grow</span></a>
            <a href="{h("/services/activation/")}"><strong>Activation Services</strong><span>Turning strategy into results</span></a>
            <a class="quiet" href="{h("/services/ceo-advisory/")}"><strong>CEO Advisory</strong><span>One-to-one support for leaders</span></a>
          </div>
          <p class="tri-line">Strategy first. Activation to deliver it. Advisors alongside. <a href="{h("/services/")}">Our Growth Architecture</a></p>
        </section>
        <section class="block">
          <h2 class="sec">Our work</h2>
          <div class="cards">
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
            {card(h, "/work/key-group/", "Key Group", "One-line result", "ph")}
            {card(h, "/work/", "More work", "All case studies", "ph")}
          </div>
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        <section class="block">
          <h2 class="sec">Growth problems we know best</h2>
          <div class="row-links">
            <a href="{h("/expertise/loyalty/")}">Loyalty</a>
            <a href="{h("/expertise/membership/")}">Membership</a>
            <a href="{h("/expertise/subscriptions/")}">Subscriptions</a>
            <a href="{h("/expertise/pricing/")}">Pricing</a>
            <a href="{h("/expertise/customer-value/")}">Customer Value</a>
          </div>
        </section>
        <section class="block">
          <h2 class="sec">Latest insights</h2>
          <ul class="list">
            <li><a href="{h("/insights/loyalty-without-the-discount/")}">Loyalty without the discount</a><span>Date</span></li>
            <li><a href="{h("/insights/")}">Insight title</a><span>Date</span></li>
            <li><a href="{h("/insights/")}">Insight title</a><span>Date</span></li>
          </ul>
          <a class="more" href="{h("/insights/")}">All insights</a>
        </section>
        {closing(h)}
"""

    if kind == "hub":
        return f"""
        <section class="block hero">
          <span class="eyebrow">What we do</span>
          <h1>Our Growth Architecture</h1>
          <p>Strategy that works. Execution that delivers.</p>
          <p class="body">The path from strategy to execution has become more complex and fragmented, despite more tools, data and channels than ever.</p>
          <p class="body">Growth Architecture is a better way to unlock customer value growth: market-leading strategic thinking combined with AI-powered, human-led activation.</p>
        </section>
        <section class="block">
          <h2 class="sec">Three ways we work with you</h2>
          <div class="tri">
            <a href="#hub-gs"><strong>Growth Strategy</strong><span>Where and how you grow</span></a>
            <a href="#hub-act"><strong>Activation Services</strong><span>Turning strategy into results</span></a>
            <a class="quiet" href="#hub-ceo"><strong>CEO Advisory</strong><span>One-to-one support for leaders</span></a>
          </div>
          <p class="tri-line">Strategy first. Activation to deliver it. Advisors alongside.</p>
        </section>
        <section class="block">
          <h2 class="plain">Where are you starting from?</h2>
          <ul class="situations">
            <li><a href="{h("/services/growth-strategy/")}">We need to decide where and how to grow</a></li>
            <li><a href="{h("/services/proposition-innovation/")}">We need a new proposition, loyalty or membership offer</a></li>
            <li><a href="{h("/services/customer-research/")}">We need to understand our customers better</a></li>
            <li><a href="{h("/services/experience-engineering/")}">Our journeys or website are not converting</a></li>
            <li><a href="{h("/services/activation/")}">Our strategy is not turning into results</a></li>
            <li><a href="{h("/services/ai-enablement/")}">We want AI to pay off</a></li>
            <li><a href="{h("/services/ceo-advisory/")}">I want a sounding board I trust</a></li>
          </ul>
        </section>
        <section class="block pillar-sec" id="hub-gs">
          <h2 class="plain"><a href="{h("/services/growth-strategy/")}">Growth Strategy</a></h2>
          <p class="line">Where and how you grow</p>
          <p class="sentence">We work out where the growth is and design the propositions that win it, using our <a href="{h("/services/growth-strategy/#civd")}">Customer, Innovation, Value and Delivery</a> frame.</p>
          <div class="cards two">
            {card(h, "/services/growth-strategy/", "Growth Strategy", "Customer-led growth strategy: where to focus and how to win", "flat")}
            {card(h, "/services/proposition-innovation/", "Proposition Innovation", "Value proposition design: loyalty, membership, subscription, direct-to-consumer", "flat")}
          </div>
          <p class="case-line">Key Group, one-line result. <a href="{h("/work/key-group/")}">Read the case study</a></p>
        </section>
        <section class="block pillar-sec" id="hub-act">
          <h2 class="plain"><a href="{h("/services/activation/")}">Activation Services</a></h2>
          <p class="line">Turning strategy into results</p>
          <p class="sentence">We build the bridge from strategy to results: new operating models and AI-powered, human-led delivery. <a href="{h("/services/activation/")}">Which of the six do you need?</a></p>
          <div class="cards">
            {card(h, "/services/customer-research/", "Customer Research and Insight", "Research, surveys, analytics and customer listening, faster with AI", "flat")}
            {card(h, "/services/experience-engineering/", "Experience Engineering", "Customer experience (CX), website and digital design, build and testing", "flat")}
            {card(h, "/services/ai-agents-for-marketing/", "AI Agents for Marketing", "AI marketing agents that clean data and improve performance, guided by experts", "flat")}
            {card(h, "/services/operating-model-design/", "Operating Model Design", "Target operating model: how teams, data and AI agents work together", "flat")}
            {card(h, "/services/growth-office/", "Growth Office", "Interim growth team and programme office that gets strategy delivered", "flat")}
            {card(h, "/services/ai-enablement/", "AI Enablement", "AI skills, training and adoption: finding where AI pays off", "flat")}
          </div>
          <p class="case-line">Dayinsure, one-line result. <a href="{h("/work/dayinsure/")}">Read the case study</a></p>
        </section>
        <section class="block pillar-sec quiet" id="hub-ceo">
          <h2 class="plain"><a href="{h("/services/ceo-advisory/")}">CEO Advisory</a></h2>
          <p class="line">One-to-one support for leaders</p>
          <p class="sentence">Experienced growth leaders alongside you, on retainer, to help you make good decisions.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
          </div>
          <a class="more" href="{h("/services/ceo-advisory/#advisors")}">Our advisors</a>
        </section>
        <section class="block">
          <p class="one-line">We apply these services to the growth problems we know best. <a href="{h("/expertise/")}">Our expertise</a></p>
        </section>
        {closing(h)}
"""

    if kind == "activation":
        six = [
            ("Customer Research and Insight", "/services/customer-research/", "You need to understand customers faster and agree one version of the truth. Methods, journey mapping, insight."),
            ("Experience Engineering", "/services/experience-engineering/", "A journey, product or website is underperforming and you want it found, fixed, tested and scaled."),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/", "Your customer data is holding marketing back and you want AI marketing agents doing the work."),
            ("Operating Model Design", "/services/operating-model-design/", "You need to redesign how teams, data and AI agents work together: a target operating model."),
            ("Growth Office", "/services/growth-office/", "You need an interim growth team, and sometimes an interim CMO, to get the strategy delivered and the value tracked."),
            ("AI Enablement", "/services/ai-enablement/", "You want your people to use AI well and to find where it pays off."),
        ]
        lines = "".join(f'<li><a href="{h(u)}"><strong>{n}.</strong> {t}</a></li>' for n, u, t in six)
        cards = "".join(card(h, u, n, t.split(".")[0], "flat") for n, u, t in six)
        return f"""
        <section class="block hero">
          <span class="eyebrow">Activation Services</span>
          <h1>Activation Services</h1>
          <p>{page["hero"]}</p>
          <p class="who">{page["who"]}</p>
          <div class="cta"><a class="btn" href="{h("/contact/")}">Contact</a></div>
        </section>
        <section class="block">
          <h2 class="plain">The bridge from strategy to results</h2>
          <p class="prose">A brilliant strategy only counts if it gets executed and the value shows up. Activation is how we get you there: hands-on, AI-powered, human-led, and not ongoing operations.</p>
        </section>
        <section class="block">
          <h2 class="plain">Which of the six do you need?</h2>
          <ul class="list">{lines}</ul>
        </section>
        <section class="block">
          <h2 class="plain">The six Activation services</h2>
          <div class="cards">{cards}</div>
        </section>
        {closing(h)}
"""

    if kind == "service":
        sits = "".join(f"<li>{s}</li>" for s in page["situations"])
        aka = f'<p class="aka">Also known as: {page["aka"]}</p>' if page.get("aka") else ""
        nums = f'<p class="numbers">{page["numbers"]}</p>' if page.get("numbers") else ""
        pillar = (
            f'<p class="pillar-note"><a href="{h(page["pillar"][1])}">{page["pillar"][0]}</a></p>'
            if page.get("pillar") else ""
        )
        extra = service_module(page, h)
        theme_chips = "".join(
            f'<a class="chip" href="{h(u)}">{n}</a>' for n, u in (page.get("themes") or [])[:3]
        )
        rel_svcs = "".join(card(h, u, n, "Often bought alongside", "flat") for n, u in (page.get("services") or [])[:3])
        what_h2 = page["h2s"][1]
        what_block = ""
        if what_h2 in ("What we do", "Value proposition design"):
            what_block = f"""
        <section class="block">
          <h2 class="plain">{what_h2}</h2>
          <p class="prose">Wireframe: the canonical description. Search terms live in this block and the H2s below, not in the nav.</p>
        </section>"""
        return f"""
        <section class="block hero">
          <h1>{page["h1"]}</h1>
          {aka}
          <p>{page["hero"]}</p>
          <p class="who">{page["who"]}</p>
          {nums}
          {pillar}
          <div class="cta"><a class="btn" href="{h("/contact/")}">Contact</a></div>
        </section>
        <section class="block">
          <h2 class="plain">Why this, now</h2>
          <ul class="situations">{sits}</ul>
          <p class="prose">Wireframe: two to four short paragraphs from the deck Why, in plain words. Not finished copy.</p>
        </section>
        {what_block}
        <section class="block">
          <h2 class="plain">Proof</h2>
          <div class="cards two">
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
            {card(h, "/work/key-group/", "Key Group", "One-line result", "ph")}
          </div>
        </section>
        {extra}
        <section class="block">
          <h2 class="sec">Related expertise</h2>
          <div class="chips">{theme_chips or '<span class="chip muted">None tagged</span>'}</div>
        </section>
        <section class="block">
          <h2 class="sec">Related services</h2>
          <div class="cards two">{rel_svcs}</div>
        </section>
        {closing(h)}
"""

    if kind == "ceo":
        return f"""
        <section class="block hero">
          <h1>CEO Advisory</h1>
          <p>{page["hero"]}</p>
          <p class="who">{page["who"]}</p>
          <div class="cta"><a class="btn" href="{h("/contact/")}">Arrange a conversation</a></div>
        </section>
        <section class="block">
          <h2 class="plain">Why this, now</h2>
          <ul class="situations">
            <li>I want a sounding board I trust</li>
            <li>Driving customer-led growth is demanding and lonely</li>
            <li>I need advice on speed-dial, not another consulting project</li>
          </ul>
          <p class="prose">Relationship and proof led. Low search demand. Advisor / board language is used carefully; coaching is adjacent, not the offer.</p>
        </section>
        <section class="block">
          <h2 class="plain">What we do</h2>
          <p class="prose">A select group of senior leaders, armed with Manifesto thinking and frameworks. Adaptive and personality-led. Retainer-based, virtual or in person, so practitioners focus on delivering value, not on selling.</p>
        </section>
        <section class="block" id="advisors">
          <h2 class="plain">Our advisors</h2>
          <p class="prose">The mega-nav item 'Our advisors' lands here. Profiles are pulled from Our team.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
          </div>
          <a class="more" href="{h("/about/team/")}">All of our team</a>
        </section>
        <section class="block">
          <h2 class="plain">How the retainer works</h2>
          <p class="prose">Disciplined yet flexible. Virtual or in person. Personality-led. The product name on this page is Side-by-Side. SxS is not used.</p>
        </section>
        {closing(h, "Arrange a conversation")}
"""

    if kind == "expertise-hub":
        cards = "".join(
            card(h, f"/expertise/{s}/", n, "Theme page · case and insight counts", "flat")
            for s, n in [
                ("loyalty", "Loyalty"),
                ("membership", "Membership"),
                ("subscriptions", "Subscriptions"),
                ("pricing", "Pricing"),
                ("customer-value", "Customer Value"),
            ]
        )
        return f"""
        <section class="block hero">
          <h1>Our expertise</h1>
          <p>The growth problems we are known for. Each cuts across services and sectors.</p>
        </section>
        <section class="block">
          <h2 class="plain">The growth problems we know best</h2>
          <div class="cards">{cards}</div>
        </section>
        <section class="block">
          <h2 class="plain">Latest insights across themes</h2>
          <ul class="list">
            <li><a href="{h("/insights/loyalty-without-the-discount/")}">Loyalty without the discount</a><span>Article</span></li>
            <li><a href="{h("/insights/")}">Insight title</a><span>Article</span></li>
          </ul>
        </section>
        {closing(h)}
"""

    if kind == "theme":
        helps = "".join(
            f'<li><a href="{h(u)}"><strong>{n}.</strong> {line}</a></li>'
            for n, u, line in page["help_svcs"]
        )
        others = " ".join(
            f'<a href="{h(u)}">{n}</a>'
            for n, u in [
                ("Loyalty", "/expertise/loyalty/"),
                ("Membership", "/expertise/membership/"),
                ("Subscriptions", "/expertise/subscriptions/"),
                ("Pricing", "/expertise/pricing/"),
                ("Customer Value", "/expertise/customer-value/"),
            ]
            if n != page["h1"]
        )
        return f"""
        <section class="block hero">
          <h1>{page["h1"]}</h1>
          <p>{page["view"]}</p>
          <div class="cta"><a class="btn" href="{h("/contact/")}">Contact</a></div>
        </section>
        <section class="block">
          <h2 class="plain">Our view</h2>
          <p class="prose">Wireframe: 300 to 600 words on the problem, failure modes and what good looks like. This page does not explain how a service is delivered.</p>
        </section>
        <section class="block">
          <h2 class="plain">Where we help</h2>
          <ul class="list">{helps}</ul>
        </section>
        <section class="block">
          <h2 class="plain">Proof</h2>
          <div class="cards two">
            {card(h, "/work/key-group/", "Key Group", "One-line result", "ph")}
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
          </div>
        </section>
        <section class="block">
          <h2 class="plain">Insights</h2>
          <ul class="list">
            <li><a href="{h("/insights/loyalty-without-the-discount/")}">Loyalty without the discount</a><span>Article</span></li>
          </ul>
          <a class="more" href="{h("/insights/")}">All insights</a>
        </section>
        <section class="block">
          <h2 class="sec">Related themes</h2>
          <div class="row-links">{others}</div>
        </section>
        {closing(h)}
"""

    if kind == "sector":
        used = "".join(f'<li><a href="{h(u)}">{n}</a></li>' for n, u in page["services"])
        return f"""
        <section class="block hero">
          <h1>{page["h1"]}</h1>
          <p class="body">{page["intro"]}</p>
        </section>
        <section class="block">
          <h2 class="plain">Clients</h2>
          <div class="logos" aria-label="Client logos"><span></span><span></span><span></span><span></span><span></span></div>
        </section>
        <section class="block">
          <h2 class="plain">Case studies</h2>
          <div class="cards two">
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
            {card(h, "/work/key-group/", "Key Group", "One-line result", "ph")}
          </div>
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        <section class="block">
          <h2 class="plain">Services most used here</h2>
          <ul class="list">{used}</ul>
        </section>
        {closing(h)}
"""

    if kind == "work-hub":
        return f"""
        <section class="block hero">
          <h1>Our work</h1>
          <p>Case studies. Service filter open. Expertise and sector behind More filters.</p>
        </section>
        <section class="block">
          <h2 class="plain">Featured</h2>
          {card(h, "/work/dayinsure/", "Dayinsure", "Quote journey rebuilt", "ph")}
        </section>
        <section class="block">
          <h2 class="plain">All case studies</h2>
          <div class="filters">
            <span class="filter on">Growth Strategy</span>
            <span class="filter on">Proposition Innovation</span>
            <span class="filter on">Experience Engineering</span>
            <span class="filter">Customer Research and Insight</span>
            <span class="filter more">More filters</span>
          </div>
          <div class="cards">
            {card(h, "/work/dayinsure/", "Dayinsure", "Experience Engineering", "ph")}
            {card(h, "/work/key-group/", "Key Group", "Experience Engineering", "ph")}
          </div>
        </section>
        {closing(h)}
"""

    if kind == "case":
        svc_chips = "".join(
            f'<a class="chip" href="{h(u)}">{n}</a>' for n, u in (page.get("services") or [])[:3]
        )
        theme_chips = "".join(
            f'<a class="chip" href="{h(u)}">{n}</a>' for n, u in (page.get("themes") or [])[:3]
        )
        return f"""
        <section class="block hero">
          <h1>{page["client"]}</h1>
          <p>{page["result"]}</p>
          <div class="chips">{svc_chips}</div>
        </section>
        <section class="block">
          <h2 class="plain">At a glance</h2>
          <p class="prose">Three or four headline numbers. Wireframe only.</p>
        </section>
        <section class="block">
          <h2 class="plain">The challenge</h2>
          <p class="prose">What the client needed. Sector: <a href="{h(page["sector_url"])}">{page["sector_name"]}</a>.</p>
        </section>
        <section class="block">
          <h2 class="plain">What we did</h2>
          <p class="prose">Narrative of the approach. Services linked, not restated.</p>
        </section>
        <section class="block">
          <h2 class="plain">The result</h2>
          <p class="prose">Outcomes, quantified where permitted. Client quote lives here.</p>
        </section>
        <section class="block">
          <h2 class="sec">Related expertise</h2>
          <div class="chips">{theme_chips}</div>
        </section>
        {closing(h)}
"""

    if kind == "insights-hub":
        return f"""
        <section class="block hero">
          <h1>Insights</h1>
          <p>Articles, reports and events. Latest is a section, not a page.</p>
        </section>
        <section class="block">
          <h2 class="plain">Latest</h2>
          {card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Article · date", "flat")}
        </section>
        <section class="block">
          <h2 class="plain">All insights</h2>
          <div class="filters">
            <span class="filter on">Article</span>
            <span class="filter">Report</span>
            <span class="filter">Event</span>
            <span class="filter more">More filters</span>
          </div>
          <ul class="list">
            <li><a href="{h("/insights/loyalty-without-the-discount/")}">Loyalty without the discount</a><span>Loyalty</span></li>
          </ul>
          <a class="more" href="{h("/newsletter/")}">Newsletter</a>
        </section>
"""

    if kind == "insight":
        return f"""
        <section class="block hero">
          <h1>Loyalty without the discount</h1>
          <p class="who">Article · Date · 6 min · Author</p>
          <div class="chips"><a class="chip" href="{h("/expertise/loyalty/")}">Loyalty</a></div>
        </section>
        <section class="block">
          <h2 class="plain">The problem</h2>
          <p class="prose">Wireframe body. Dated point of view. The evergreen position stays on the Loyalty theme page.</p>
        </section>
        <section class="block">
          <h2 class="plain">What we think</h2>
          <p class="prose">One or two arguments. Not a service description.</p>
        </section>
        <section class="block">
          <h2 class="plain">How we help</h2>
          <p class="prose">Hand-off: <a href="{h("/services/proposition-innovation/")}">Proposition Innovation</a> and <a href="{h("/expertise/loyalty/")}">Loyalty</a>.</p>
        </section>
        {closing(h)}
"""

    if kind == "about":
        return f"""
        <section class="block hero">
          <h1>About Manifesto Growth Architects</h1>
          <p>Sustainable, customer-led growth. Strategy plus AI-powered activation.</p>
        </section>
        <section class="block">
          <h2 class="plain">Who we are and our story</h2>
          <p class="prose">Origin, what we believe about growth, why customer-led. Full version lives here; Home only teases it.</p>
        </section>
        <section class="block">
          <h2 class="plain">What makes us different</h2>
          <p class="prose">One of the points is the Growth Architecture model. The system itself is on <a href="{h("/services/")}">What we do</a>.</p>
        </section>
        <section class="block">
          <h2 class="plain">Leadership</h2>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Partner name", "Role", "person")}
            {card(h, "/about/team/", "Our team", "Everyone client-facing", "person")}
          </div>
        </section>
        <section class="block">
          <h2 class="plain">How we work</h2>
          <p class="prose">Method is separate from services. <a href="{h("/about/how-we-work/")}">How we work</a>. <a href="{h("/about/values/")}">Values and culture</a>. <a href="{h("/careers/")}">Careers</a>.</p>
        </section>
        {closing(h)}
"""

    if kind == "team":
        return f"""
        <section class="block hero">
          <h1>Our team</h1>
          <p>Our Growth Architects. Client-facing people, grouped by role.</p>
        </section>
        <section class="block">
          <h2 class="plain">Leadership</h2>
          <div class="cards">{card(h, "/about/team/advisor-one/", "Name", "Role", "person")}</div>
        </section>
        <section class="block">
          <h2 class="plain">Consultants</h2>
          <div class="cards">{card(h, "/about/team/advisor-one/", "Name", "Role", "person")}</div>
        </section>
        <section class="block" id="advisors">
          <h2 class="plain">Side-by-Side advisors</h2>
          <p class="prose">The mega-nav 'Our advisors' lands on <a href="{h("/services/ceo-advisory/#advisors")}">CEO Advisory</a>. This group is the same people.</p>
          <div class="cards">{card(h, "/about/team/advisor-one/", "Advisor name", "Former role", "person")}</div>
        </section>
        <section class="block">
          <h2 class="plain">Associates and expert network</h2>
          <p class="prose">Optional. AI practitioners for AI Enablement, and associate advisors.</p>
        </section>
        <p class="one-line" style="padding:0 0 36px"><a href="{h("/careers/")}">Careers</a></p>
"""

    if kind == "profile":
        return f"""
        <section class="block hero">
          <h1>Advisor name</h1>
          <p>Role · one-line focus</p>
        </section>
        <section class="block">
          <h2 class="plain">Biography</h2>
          <p class="prose">Two to five paragraphs. Under 100 words means noindex.</p>
        </section>
        <section class="block">
          <h2 class="plain">Focus</h2>
          <p class="prose">Leads on <a href="{h("/services/ceo-advisory/")}">CEO Advisory</a>. Available through Side-by-Side.</p>
        </section>
        <section class="block">
          <h2 class="plain">Selected work</h2>
          <div class="cards two">{card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}</div>
        </section>
        {closing(h)}
"""

    if kind == "how":
        return f"""
        <section class="block hero">
          <h1>How we work</h1>
          <p>Method, not a product. Frameworks are listed once here and live on their service pages.</p>
        </section>
        <section class="block">
          <h2 class="plain">Principles</h2>
          <p class="prose">Including AI-powered, human-led.</p>
        </section>
        <section class="block">
          <h2 class="plain">Engagement shapes</h2>
          <ul class="list">
            <li><a href="{h("/services/growth-strategy/")}">Strategy project</a></li>
            <li><a href="{h("/services/activation/")}">Strategy into activation</a></li>
            <li><a href="{h("/services/growth-office/")}">Embedded growth office / interim growth team</a></li>
            <li><a href="{h("/services/ceo-advisory/")}">Advisory retainer</a></li>
          </ul>
        </section>
        <section class="block">
          <h2 class="plain">Frameworks and tools</h2>
          <h3 class="plain">Growth Architecture</h3>
          <p class="prose">The system: strategy, activation, advisory. Home: <a href="{h("/services/")}">What we do</a>.</p>
          <h3 class="plain">Customer, Innovation, Value and Delivery</h3>
          <p class="prose">The Growth Strategy frame. Home: <a href="{h("/services/growth-strategy/#civd")}">Growth Strategy</a>.</p>
          <h3 class="plain">Operating Architecture</h3>
          <p class="prose">The adaptive operating model. Home: <a href="{h("/services/operating-model-design/#operating-architecture")}">Operating Model Design</a>.</p>
          <h3 class="plain">AgentLab</h3>
          <p class="prose">The catalogue of marketing and data agents. Home: <a href="{h("/services/ai-agents-for-marketing/#agentlab")}">AI Agents for Marketing</a>.</p>
          <h3 class="plain">Side-by-Side</h3>
          <p class="prose">The advisory retainer. Home: <a href="{h("/services/ceo-advisory/")}">CEO Advisory</a>.</p>
        </section>
        <section class="block">
          <h2 class="plain">Working with AI</h2>
          <p class="prose">How AI-powered activation works in practice. <a href="{h("/services/ai-agents-for-marketing/")}">AI Agents for Marketing</a> and <a href="{h("/services/ai-enablement/")}">AI Enablement</a>.</p>
        </section>
        {closing(h)}
"""

    if kind == "values":
        return f"""
        <section class="block hero">
          <h1>Values and culture</h1>
        </section>
        <section class="block">
          <h2 class="plain">Values</h2>
          <p class="prose">Three to six values. Wireframe only.</p>
        </section>
        <section class="block">
          <h2 class="plain">Culture</h2>
          <p class="prose">How the team works together.</p>
        </section>
        <section class="block">
          <h2 class="plain">Diversity, equity and inclusion</h2>
          <p class="prose">Commitments. Combined here to avoid a second thin page.</p>
          <a class="more" href="{h("/careers/")}">Careers</a>
        </section>
"""

    if kind == "careers":
        return f"""
        <section class="block hero">
          <h1>Careers at Manifesto</h1>
        </section>
        <section class="block">
          <h2 class="plain">Life at Manifesto</h2>
          <p class="prose">What it is like to work here. <a href="{h("/about/values/")}">Values and culture</a>.</p>
        </section>
        <section class="block">
          <h2 class="plain">Benefits</h2>
          <p class="prose">List. Wireframe only.</p>
        </section>
        <section class="block">
          <h2 class="plain">Open roles</h2>
          <div class="cards two">{card(h, "/careers/growth-architect/", "Growth Architect", "Location · type", "flat")}</div>
        </section>
"""

    if kind == "role":
        return f"""
        <section class="block hero">
          <h1>Growth Architect</h1>
          <p>Location · type</p>
        </section>
        <section class="block">
          <h2 class="plain">About the role</h2>
          <p class="prose">Description, responsibilities, what we look for.</p>
        </section>
        <section class="block">
          <h2 class="plain">How to apply</h2>
          <p class="prose">Form or email. <a href="{h("/careers/")}">All roles</a>.</p>
        </section>
"""

    if kind == "contact":
        return f"""
        <section class="block hero">
          <h1>Contact</h1>
          <p>Tell us about your growth challenge. We will come back to you.</p>
        </section>
        <section class="block">
          <h2 class="plain">Get in touch</h2>
          <div class="form">
            <div class="field"><label>Name</label><div class="box"></div></div>
            <div class="field"><label>Company</label><div class="box"></div></div>
            <div class="field"><label>Email</label><div class="box"></div></div>
            <div class="field"><label>Topic</label><div class="box"></div></div>
            <div class="field"><label>Message</label><div class="box tall"></div></div>
            <a class="btn" href="{h("/contact/thank-you/")}">Send</a>
          </div>
        </section>
        <section class="block">
          <h2 class="plain">Direct contact</h2>
          <p class="prose">Email, phone, office address. Response time and confidentiality.</p>
        </section>
"""

    if kind == "thanks":
        return f"""
        <section class="block hero">
          <h1>Thank you</h1>
          <p>We have your message.</p>
        </section>
        <section class="block">
          <h2 class="plain">While you wait</h2>
          <div class="cards">
            {card(h, "/services/", "What we do", "Our Growth Architecture", "flat")}
            {card(h, "/work/dayinsure/", "Dayinsure", "Case study", "flat")}
            {card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Insight", "flat")}
          </div>
        </section>
"""

    if kind == "legal":
        return f"""
        <section class="block hero">
          <h1>{page["h1"]}</h1>
          <p class="body">{page.get("blurb") or ""}</p>
        </section>
        <section class="block">
          <p class="prose">Utility shell so every footer link resolves. Not a search destination.</p>
        </section>
"""

    if kind == "notfound":
        return f"""
        <section class="block hero">
          <h1>Page not found</h1>
          <p>This URL is not in the sitemap.</p>
          <div class="cta">
            <a class="btn" href="{h("/services/")}">What we do</a>
            <a class="text" href="{h("/work/")}">Our work</a>
            <a class="text" href="{h("/contact/")}">Contact</a>
          </div>
        </section>
"""

    raise KeyError(kind)


def service_module(page: dict, h) -> str:
    url = page["url"]
    if url == "/services/growth-strategy/":
        return f"""
        <section class="block">
          <h2 class="plain">North Star</h2>
          <p class="prose">Candidate H2 from the deck appendix. Andy's Growth Strategy slide is still marked to be updated.</p>
          <h2 class="plain">Growth priorities</h2>
          <p class="prose">Where the bets sit.</p>
          <h2 class="plain">Demand signals</h2>
          <p class="prose">What you watch to know the strategy is working.</p>
          <h2 class="plain">Scenario planning</h2>
          <p class="prose">How the strategy holds when the market moves.</p>
        </section>
        <section class="block" id="civd">
          <h2 class="plain">Customer, Innovation, Value and Delivery</h2>
          <p class="prose">The CIVD frame. Natural next step: <a href="{h("/services/proposition-innovation/")}">Proposition Innovation</a>.</p>
          <h3 class="plain">Customer</h3>
          <p class="prose">Who you grow with.</p>
          <h3 class="plain">Innovation</h3>
          <p class="prose">What you offer next.</p>
          <h3 class="plain">Value</h3>
          <p class="prose">Where the economics move.</p>
          <h3 class="plain">Delivery</h3>
          <p class="prose">Whether it can be executed. Hands off to Activation.</p>
        </section>
        <section class="block">
          <h2 class="plain">How it works</h2>
          <p class="prose">Shape of a strategy engagement. Method detail: <a href="{h("/about/how-we-work/")}">How we work</a>.</p>
        </section>
"""
    if url == "/services/proposition-innovation/":
        items = [
            ("Loyalty propositions", "/expertise/loyalty/"),
            ("Membership propositions", "/expertise/membership/"),
            ("Subscription propositions", "/expertise/subscriptions/"),
            ("Direct-to-consumer propositions", "/expertise/customer-value/"),
        ]
        blocks = "".join(
            f'<h2 class="plain">{n}</h2><p class="prose">One H2 per type, linking to <a href="{h(u)}">{n.split()[0]}</a>.</p>'
            for n, u in items
        )
        return f"""
        <section class="block">{blocks}
          <h2 class="plain">How it works</h2>
          <p class="prose">Shape of a proposition engagement. Andy's slide is still marked to be updated.</p>
        </section>
"""
    if url == "/services/customer-research/":
        return f"""
        <section class="block">
          <h2 class="plain">Customer research methods</h2>
          <p class="prose">Buyer language from the UK pull (~720). Techniques, companies, how the work is done.</p>
          <h2 class="plain">Customer journey mapping</h2>
          <p class="prose">Strong adjacent demand (~2,900). Analytical mapping lives here; design research lives on <a href="{h("/services/experience-engineering/#research-and-testing")}">Experience Engineering</a>.</p>
          <h2 class="plain">Research projects</h2>
          <p class="prose">Bespoke qualitative, quantitative, surveys and digital listening. Getting to the so-what faster.</p>
          <h3 class="plain">Digital listening</h3>
          <h3 class="plain">Qualitative research</h3>
          <h3 class="plain">Quantitative research</h3>
          <h3 class="plain">Customer data analytics</h3>
          <h3 class="plain">Internal knowledge</h3>
          <h3 class="plain">External market data</h3>
          <h2 class="plain">Always-on customer insight</h2>
          <p class="prose">Voice of the customer tools, panels and intelligence platforms.</p>
          <h2 class="plain">How it works</h2>
          <p class="prose">Insight project or capability build.</p>
        </section>
"""
    if url == "/services/experience-engineering/":
        return f"""
        <section class="block">
          <h2 class="plain">Find</h2>
          <p class="prose">Audit existing performance. Deck module: Find / Redesign / Test / Scale.</p>
          <h2 class="plain">Redesign</h2>
          <p class="prose">Better journey flows, CX design and digital build.</p>
          <h2 class="plain">Test</h2>
          <p class="prose">Build and test with target audiences.</p>
          <h2 class="plain">Scale</h2>
          <p class="prose">Roll out the journeys that move value.</p>
        </section>
        <section class="block" id="customer-experience">
          <h2 class="plain">Customer experience (CX) design</h2>
          <p class="prose">CX consultancy language (~70) as a section, not a nav rename.</p>
        </section>
        <section class="block" id="website-and-digital">
          <h2 class="plain">Website and digital product</h2>
          <p class="prose">Website design consultancy language (~70). Dayinsure / Key Group pattern.</p>
        </section>
        <section class="block" id="research-and-testing">
          <h2 class="plain">User research and testing</h2>
          <p class="prose">Journey research for design. <a href="{h("/services/customer-research/")}">Customer Research and Insight</a> owns analytical research.</p>
          <h3 class="plain">Customer and value analytics</h3>
        </section>
"""
    if url == "/services/ai-agents-for-marketing/":
        return f"""
        <section class="block" id="agentlab">
          <h2 class="plain">AgentLab</h2>
          <p class="prose">Named catalogue on this page. Individual agents are entries, not URLs, and are not in the mega-nav.</p>
          <h3 class="plain">Reporting and Analytics</h3>
          <p class="prose">Effectiveness, attribution mapping, performance planning.</p>
          <h3 class="plain">Data and Infrastructure</h3>
          <p class="prose">CDP data clean-up, tagging and data collection, integration discovery.</p>
          <h3 class="plain">Strategy and Planning</h3>
          <p class="prose">Segmentation builder, customer journey mapping agent, audience opportunity.</p>
          <h3 class="plain">Automation and Execution</h3>
          <p class="prose">Channel optimisation, test and learn, QA and deployment.</p>
        </section>
        <section class="block">
          <h2 class="plain">How it works</h2>
          <p class="prose">4 weeks audit. 6 weeks first agents. Ongoing portfolio. <a href="{h("/services/ai-enablement/")}">AI Enablement</a> if you are earlier in the journey.</p>
        </section>
"""
    if url == "/services/operating-model-design/":
        return f"""
        <section class="block">
          <h2 class="plain">Target operating model</h2>
          <p class="prose">Strong adjacent demand (~1,600). The searched phrase for 'we need a new operating model'.</p>
          <h2 class="plain">Adaptive operating model</h2>
          <p class="prose">Grounded in customer value growth. Fuelled by high-quality data. Redesigned around humans and AI agents. Orchestrated and linked to impact.</p>
        </section>
        <section class="block" id="operating-architecture">
          <h2 class="plain">Our Operating Architecture framework</h2>
          <h3 class="plain">High-quality data and tools</h3>
          <p class="prose">Data quality, security and governance; knowledge architecture; tech platforms; AI tools.</p>
          <h3 class="plain">New work units</h3>
          <p class="prose">Key functions, capabilities and workflows.</p>
          <h3 class="plain">Orchestration: culture, value, capability</h3>
          <p class="prose">The same three words as <a href="{h("/services/growth-office/")}">Growth Office</a>, which staffs what this page designs.</p>
        </section>
        <section class="block">
          <h2 class="plain">How it works</h2>
          <p class="prose">Diagnose the current model, design the adaptive model, implement.</p>
        </section>
"""
    if url == "/services/growth-office/":
        return f"""
        <section class="block">
          <h2 class="plain">Interim growth team</h2>
          <p class="prose">Lean teams of interim growth experts. Quiet line and primary SEO phrase. Interim CMO where the engagement needs senior cover (~110 to 140).</p>
          <h3 class="plain">Interim CMO and senior cover (where the engagement needs it)</h3>
          <h2 class="plain">Then embed</h2>
          <p class="prose">Establish the new ways of working required for ongoing delivery. Not a permanent outsource.</p>
          <h2 class="plain">Culture</h2>
          <p class="prose">Winning hearts and minds through engagement, proof points and AI literacy.</p>
          <h2 class="plain">Capability</h2>
          <p class="prose">Orchestrating delivery teams to build capabilities and automate priority workflows.</p>
          <h2 class="plain">Value</h2>
          <p class="prose">Tracking impact against baseline plans and course-correcting on lead indicators.</p>
          <h2 class="plain">How it works</h2>
          <p class="prose">Two phases from the deck: interim activation support, then embed. <a href="{h("/services/operating-model-design/")}">Operating Model Design</a> designs; this page staffs.</p>
        </section>
"""
    if url == "/services/ai-enablement/":
        return f"""
        <section class="block">
          <h2 class="plain">AI skills and adoption</h2>
          <p class="prose">Building the skills and tools for day-to-day AI use. Own the phrase AI enablement (~170).</p>
          <h2 class="plain">Finding where AI pays off</h2>
          <p class="prose">Value case targeting and re-engineering key workflows.</p>
          <h2 class="plain">New business models with AI</h2>
          <p class="prose">Working with leadership to identify and qualify transformational opportunities.</p>
          <h2 class="plain">How it works</h2>
          <p class="prose">Maturity assessment, then a bespoke programme. Practitioners from our expert network. Tooling: <a href="{h("/services/ai-agents-for-marketing/")}">AI Agents for Marketing</a>.</p>
        </section>
"""
    return '<section class="block"><h2 class="plain">How it works</h2><p class="prose">Engagement shape.</p></section>'


def sitemap_page() -> str:
    """Clickable sitemap index (wireframe tool, not a live URL)."""
    # Build using wrap() on a synthetic page, but custom body.
    page = dict(
        url="/",
        title="Sitemap (wireframe index)",
        section="home",
        weight="Utility",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Sitemap",
        h2s=[],
        h3s=[],
        intent="Wireframe index of every page. Not part of the live site.",
        crumbs=[],
        kind="legal",
        blurb="",
    )
    # Custom file at mocks/sitemap.html  /  not at /
    # We'll write it separately.
    return page


def write_sitemap_html() -> None:
    # Standalone clickable sitemap at mocks/sitemap.html
    groups: list[tuple[str, list[dict]]] = []
    order = [
        ("Home", ["/"]),
        ("Services", [p["url"] for p in PAGES if p["url"].startswith("/services/")]),
        ("Expertise", [p["url"] for p in PAGES if p["url"].startswith("/expertise/")]),
        ("Sectors", [p["url"] for p in PAGES if p["url"].startswith("/sectors/")]),
        ("Work", [p["url"] for p in PAGES if p["url"].startswith("/work/")]),
        ("Insights", [p["url"] for p in PAGES if p["url"].startswith("/insights/") or p["url"] == "/newsletter/"]),
        ("About", [p["url"] for p in PAGES if p["url"].startswith("/about/")]),
        ("Careers", [p["url"] for p in PAGES if p["url"].startswith("/careers/")]),
        ("Contact", [p["url"] for p in PAGES if p["url"].startswith("/contact/")]),
        ("Utility", [p["url"] for p in PAGES if p["url"] in {"/privacy-policy/", "/cookie-policy/", "/terms/", "/accessibility/", "/search/", "/404/"}]),
    ]
    by_url = {p["url"]: p for p in PAGES}
    lis = []
    for heading, urls in order:
        inner = []
        for u in urls:
            p = by_url[u]
            href = rel_href("/", u) if u != "/" else "index.html"
            # sitemap.html sits next to index.html
            if u == "/":
                href = "index.html"
            else:
                href = u.strip("/") + "/index.html"
            inner.append(
                f'<li><a href="{href}"><span class="u">{u}</span> {p["h1"]}</a> <span class="w">{p["weight"]}</span></li>'
            )
        lis.append(f'<li class="sec">{heading}<ul>{"".join(inner)}</ul></li>')
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sitemap | Manifesto Growth Architects (IA wireframe)</title>
<link rel="stylesheet" href="assets/wireframe.css">
</head>
<body>
<div class="top">
  <span>MGA website IA. Wireframe, not design. Every sitemap URL below is a real HTML page.</span>
  <span><a href="index.html">Home</a></span>
</div>
<div class="wrap" style="max-width:900px;margin:0 auto 48px;padding:0 12px">
  <div class="sitemap">
    <ul>
      {"".join(lis)}
    </ul>
    <p>Open <a href="index.html">mocks/index.html</a> to start. Primary nav, mega-nav and footer work on every page. Each page has chips and an outside heading map. Filter states are query strings, not pages.</p>
  </div>
</div>
</body>
</html>
"""
    (MOCKS / "sitemap.html").write_text(html, encoding="utf-8")


def write_heading_map_md() -> None:
    lines = [
        "# Heading map (full-site wireframe)",
        "",
        "Recommended H1 (one), H2s (ordered) and H3s for every URL in the clickable wireframe.",
        "Tied to UK DataForSEO volumes (Sep 2026) and Andy's Growth Architecture Services deck.",
        "Nav labels are unchanged. Buyer language sits in quiet lines, H1 support, H2/H3s and page chips.",
        "",
        "Volumes are average monthly Google Ads search volume for the United Kingdom. Exact Manifesto product phrases are often thin; adjacent demand is the useful signal.",
        "",
        "Source of truth for structure: `docs/02-sitemap.md` and the IA report. This file is the SEO heading layer on top of that IA, not a competing sitemap.",
        "",
    ]
    for p in PAGES:
        lines.append(f"## `{p['url']}`: {p['title']}")
        lines.append("")
        lines.append(f"- **Weight:** {p['weight']}")
        lines.append(f"- **Primary keyword:** {p.get('primary') or 'none'}")
        if p.get("quiet"):
            lines.append(f"- **Quiet line:** {p['quiet']}")
        if p.get("alts"):
            lines.append("- **Alts:**")
            for a in p["alts"]:
                lines.append(f"  - {a}")
        lines.append(f"- **H1:** {p['h1']}")
        if p.get("h2s"):
            lines.append("- **H2s (ordered):**")
            for i, h2 in enumerate(p["h2s"], 1):
                lines.append(f"  {i}. {h2}")
        if p.get("h3s"):
            lines.append("- **H3s:**")
            for h3 in p["h3s"]:
                lines.append(f"  - {h3}")
        lines.append(f"- **Intent:** {p['intent']}")
        rels = []
        if p.get("themes"):
            rels.append("themes: " + ", ".join(n for n, _ in p["themes"]))
        if p.get("sectors"):
            rels.append("sectors: " + ", ".join(n for n, _ in p["sectors"]))
        if p.get("services"):
            rels.append("services: " + ", ".join(n for n, _ in p["services"]))
        if rels:
            lines.append(f"- **Related:** {'; '.join(rels)}")
        lines.append("")
    (DOCS / "heading-map.md").write_text("\n".join(lines), encoding="utf-8")


def write_pages() -> None:
    seen = set()
    for page in PAGES:
        url = page["url"]
        if url in seen:
            raise SystemExit(f"Duplicate URL {url}")
        seen.add(url)
        dest = MOCKS / "index.html" if url == "/" else MOCKS / url.strip("/") / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(wrap(page, body_for(page)), encoding="utf-8")
        print("wrote", dest.relative_to(ROOT))


if __name__ == "__main__":
    write_pages()
    write_sitemap_html()
    write_heading_map_md()
    print(f"pages: {len(PAGES)}")
