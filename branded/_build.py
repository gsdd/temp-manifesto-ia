#!/usr/bin/env python3
"""Generate the BRANDED preview templates at branded/.

A visual skin over the greyscale wireframes in mocks/: same IA, same labels,
same section structure, plus the brand from the October 2026 identity Toolkit
(see branded/README.md). The wires remain the IA source of truth; this build
is a preview exploration for Gary, not production code and not a competing IA.

Content (page registry, nav labels, strand subtitles, body copy) is imported
from mocks/_build.py so the two builds cannot drift. Run from the repo root:

    python3 branded/_build.py

Key templates are fully branded; every other URL gets a branded stub so no
internal link breaks. Findings discovered while building live in
branded/FINDINGS.md.
"""
from __future__ import annotations

import importlib.util
import os
import re
from html import escape as esc
from pathlib import Path

BRANDED = Path(__file__).resolve().parent
ROOT = BRANDED.parent

# Import the wireframe builder as a module: single source for PAGES and copy.
_spec = importlib.util.spec_from_file_location("wires", ROOT / "mocks" / "_build.py")
w = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(w)

rel_href = w.rel_href
file_dir = w.file_dir

# Templates built in full. Everything else gets a branded stub page.
KEY_URLS = {
    "/",
    "/services/",
    "/services/experience-engineering/",
    "/work/",
    "/work/dayinsure/",
    "/work/key-group/",
    "/insights/",
    "/insights/loyalty-without-the-discount/",
    "/insights/pricing-paradox/",
    "/careers/",
    "/catalogue/",
}


def asset(from_url: str, name: str) -> str:
    return os.path.relpath("assets/" + name, file_dir(from_url))


def wires_href(from_url: str, to_url: str | None = None) -> str:
    """Relative link from a branded page to the matching greyscale wireframe."""
    to_url = to_url if to_url is not None else from_url
    dst = "index.html" if to_url == "/" else to_url.strip("/") + "/index.html"
    return os.path.relpath(os.path.join("..", "mocks", dst), file_dir(from_url))


# ---------------------------------------------------------------------------
# Working-name override (client request, Oct 2026). The wires on main say
# "Value Orchestration"; the client's current working name is "Growth Office".
# The source below keeps mirroring the wires; this mapping is applied to the
# rendered HTML and to output paths at write time, so a future rename is a
# change to this one list. Links into the greyscale wires in mocks/ are left
# untouched (the wires keep their own naming).
# ---------------------------------------------------------------------------

WORKING_NAMES = [
    ("Value Orchestration", "Growth Office"),
    ("Value orchestration", "Growth office"),
    ("value orchestration", "growth office"),
    ("value-orchestration", "growth-office"),
]

_WIRES_GUARD = "\x00wires\x00"


def apply_working_names(html: str) -> str:
    html = html.replace("mocks/services/value-orchestration", _WIRES_GUARD)
    for old, new in WORKING_NAMES:
        html = html.replace(old, new)
    return html.replace(_WIRES_GUARD, "mocks/services/value-orchestration")


def output_url(url: str) -> str:
    """Where a wires URL is published in the branded preview."""
    return url.replace("value-orchestration", "growth-office")


# ---------------------------------------------------------------------------
# Navigation data. Labels, order and subtitles mirror mocks/_build.py
# header_html exactly (the wires are the IA source of truth).
# ---------------------------------------------------------------------------

MEGA_PILLARS = [
    ("Growth Strategy", "/services/growth-strategy/", "Where and how you grow", [
        ("Overview", "/services/growth-strategy/", "Where to grow and how to win", True),
        ("Proposition Innovation", "/services/proposition-innovation/", "Value proposition design", False),
    ]),
    ("Activation Services", "/services/activation/", "Turning strategy into results", [
        ("Overview", "/services/activation/", "Hands-on delivery, six services", True),
        ("Customer Research and Insight", "/services/customer-research/", "Research methods and journey mapping", False),
        ("Experience Engineering", "/services/experience-engineering/", "Customer experience and websites", False),
        ("AI Agents for Marketing", "/services/ai-agents-for-marketing/", "AI marketing agents, guided by experts", False),
        ("Operating Model Design", "/services/operating-model-design/", "Target operating model", False),
        ("Value Orchestration", "/services/value-orchestration/", "Interim growth team", False),
        ("AI Enablement", "/services/ai-enablement/", "AI skills and adoption", False),
    ]),
    ("CEO Advisory", "/services/ceo-advisory/", "One-to-one support for leaders", [
        ("Side-by-Side", "/services/ceo-advisory/#side-by-side", "One-to-one advisory retainer", False),
        ("Our advisors", "/services/ceo-advisory/#advisors", "Experienced growth leaders", False),
    ]),
]
MEGA_ROW = [("All services", "/services/"), ("Expertise", "/expertise/"), ("Our work", "/work/")]
THINKING_MENU = [
    ("All thinking", "/insights/"),
    ("Reports", "/insights/#reports"),
    ("Articles", "/insights/#articles"),
    ("News and events", "/insights/#news-events"),
]
ABOUT_MENU = [
    ("Our people", "/about/team/"),
    ("Our approach", "/about/how-we-work/"),
    ("Values and culture", "/about/values/"),
]


def mega_html(h) -> str:
    cols = ""
    for name, url, line, strands in MEGA_PILLARS:
        lis = ""
        for label, surl, sub, overview in strands:
            cls = ' class="strand-overview"' if overview else ""
            lis += f'<li><a{cls} href="{h(surl)}">{esc(label)}<small>{esc(sub)}</small></a></li>'
        cols += f"""
            <div class="pillar">
              <p class="pillar-title"><a class="pillar-hub" href="{h(url)}">{esc(name)} <span class="hub-chevron" aria-hidden="true">&#8594;</span></a></p>
              <p class="line">{esc(line)}</p>
              <ul>{lis}</ul>
            </div>"""
    row = "".join(f'<a href="{h(u)}">{esc(n)}</a>' for n, u in MEGA_ROW)
    return f"""
      <div class="mega" id="megaNav" role="region" aria-label="What we do menu">
        <div class="mega-inner">
          <div class="mega-cols">{cols}
          </div>
          <div class="mega-row">{row}</div>
        </div>
      </div>"""


def dropdown_html(h, label: str, items) -> str:
    lis = "".join(f'<li><a href="{h(u)}">{esc(n)}</a></li>' for n, u in items)
    return f"""
            <div class="dropdown" role="region" aria-label="{esc(label)} menu">
              <ul>{lis}</ul>
            </div>"""


def mobile_menu_html(h) -> str:
    groups = ""
    for name, url, _line, strands in MEGA_PILLARS:
        lis = "".join(
            f'<a href="{h(surl)}">{esc(label)}<small>{esc(sub)}</small></a>'
            for label, surl, sub, _ in strands
        )
        groups += f'<a class="m-sub" href="{h(url)}">{esc(name)}</a>{lis}'
    row = "".join(f'<a href="{h(u)}">{esc(n)}</a>' for n, u in MEGA_ROW)
    thinking = "".join(f'<a href="{h(u)}">{esc(n)}</a>' for n, u in THINKING_MENU)
    about = "".join(f'<a href="{h(u)}">{esc(n)}</a>' for n, u in ABOUT_MENU)
    return f"""
    <nav class="mobile-menu" id="mobileMenu" aria-label="Mobile">
      <div class="m-group">
        <button type="button" class="m-top" aria-expanded="false">What we do <span class="caret">&#9660;</span></button>
        <div class="m-panel">{groups}{row}</div>
      </div>
      <div class="m-group"><a class="m-top" href="{h("/work/")}">Our work</a></div>
      <div class="m-group">
        <button type="button" class="m-top" aria-expanded="false">Our thinking <span class="caret">&#9660;</span></button>
        <div class="m-panel">{thinking}</div>
      </div>
      <div class="m-group">
        <button type="button" class="m-top" aria-expanded="false">About <span class="caret">&#9660;</span></button>
        <div class="m-panel">{about}</div>
      </div>
      <div class="m-group"><a class="m-top" href="{h("/careers/")}">Careers</a></div>
      <a class="btn m-contact" href="{h("/contact/")}">Contact</a>
    </nav>"""


def header_html(from_url: str, section: str) -> str:
    h = lambda u: rel_href(from_url, u)

    def current(name: str) -> str:
        return ' aria-current="page"' if section == name else ""

    logo = asset(from_url, "logos/logo-two-colour.svg")
    return f"""
    <header class="site-header on-dark" id="siteHeader" data-mega-open="false">
      <div class="bar">
        <a class="logo" href="{h("/")}"><img src="{logo}" alt="Manifesto Growth Architects. Home" width="118" height="65"></a>
        <ul class="primary-nav" id="primaryNav">
          <li data-menu="mega">
            <a class="top-link" href="{h("/services/")}" aria-haspopup="true" aria-expanded="false"{current("services")}>What we do <span class="caret" aria-hidden="true">&#9660;</span></a>
          </li>
          <li><a class="top-link" href="{h("/work/")}"{current("work")}>Our work</a></li>
          <li data-menu="thinking">
            <a class="top-link" href="{h("/insights/")}" aria-haspopup="true" aria-expanded="false"{current("insights")}>Our thinking <span class="caret" aria-hidden="true">&#9660;</span></a>
            {dropdown_html(h, "Our thinking", THINKING_MENU)}
          </li>
          <li data-menu="about">
            <a class="top-link" href="{h("/about/")}" aria-haspopup="true" aria-expanded="false"{current("about")}>About <span class="caret" aria-hidden="true">&#9660;</span></a>
            {dropdown_html(h, "About", ABOUT_MENU)}
          </li>
          <li><a class="top-link" href="{h("/careers/")}"{current("careers")}>Careers</a></li>
        </ul>
        <a class="btn header-contact" href="{h("/contact/")}"{current("contact")}>Get in touch</a>
        <button type="button" class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="mobileMenu" aria-label="Menu">
          <span class="bar-line"></span><span class="bar-line"></span><span class="bar-line"></span>
        </button>
      </div>
      {mega_html(h)}
    </header>
    {mobile_menu_html(h)}
    <div class="scrim" aria-hidden="true"></div>"""


def crumbs_html(from_url: str, crumbs) -> str:
    if not crumbs:
        return ""
    items = []
    for label, url in crumbs:
        if url:
            items.append(f'<li><a href="{rel_href(from_url, url)}">{esc(label)}</a></li>')
        else:
            items.append(f'<li aria-current="page">{esc(label)}</li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def footer_html(from_url: str) -> str:
    h = lambda u: rel_href(from_url, u)
    logo = asset(from_url, "logos/logo-two-colour.svg")
    cols = [
        ("What we do", [(n, u) for n, u, *_ in [
            ("Growth Strategy", "/services/growth-strategy/"),
            ("Proposition Innovation", "/services/proposition-innovation/"),
            ("Customer Research and Insight", "/services/customer-research/"),
            ("Experience Engineering", "/services/experience-engineering/"),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
            ("Operating Model Design", "/services/operating-model-design/"),
            ("Value Orchestration", "/services/value-orchestration/"),
            ("AI Enablement", "/services/ai-enablement/"),
            ("CEO Advisory", "/services/ceo-advisory/"),
            ("All services", "/services/"),
        ]]),
        ("Expertise", [
            ("Loyalty", "/expertise/loyalty/"),
            ("Membership", "/expertise/membership/"),
            ("Subscriptions", "/expertise/subscriptions/"),
            ("Pricing", "/expertise/pricing/"),
            ("Customer Value", "/expertise/customer-value/"),
        ]),
        ("Who we work with", [
            ("Financial services", "/sectors/financial-services/"),
            ("Media", "/sectors/media/"),
            ("Consumer", "/sectors/consumer/"),
            ("Retail", "/sectors/retail/"),
            ("Energy", "/sectors/energy/"),
        ]),
        ("Company", [
            ("About", "/about/"),
            ("Our people", "/about/team/"),
            ("Our approach", "/about/how-we-work/"),
            ("Values and culture", "/about/values/"),
            ("Careers", "/careers/"),
            ("Our work", "/work/"),
            ("Our thinking", "/insights/"),
            ("The Nutshell", "/newsletter/"),
            ("Contact", "/contact/"),
        ]),
    ]
    col_html = ""
    for title, links in cols:
        lis = "".join(f'<li><a href="{h(u)}">{esc(n)}</a></li>' for n, u in links)
        col_html += f'<div><p class="footer-col-title">{esc(title)}</p><ul>{lis}</ul></div>'
    return f"""
    <footer class="site-footer on-dark">
      <div class="wrap">
        <div class="footer-logo"><img src="{logo}" alt="Manifesto Growth Architects" width="128" height="71"></div>
        <div class="footer-cols">{col_html}</div>
        <div class="footer-bottom">
          <span>Company registration line</span>
          <a href="{h("/search/")}">Search</a>
          <a href="{h("/privacy-policy/")}">Privacy policy</a>
          <a href="{h("/cookie-policy/")}">Cookie policy</a>
          <a href="{h("/terms/")}">Terms</a>
          <a href="{h("/accessibility/")}">Accessibility statement</a>
          <span>Social links</span>
        </div>
      </div>
    </footer>
    <div class="cookie-bar on-dark" id="cookieBar" role="region" aria-label="Cookies">
      <span>We use cookies to run this site. <a href="{h("/cookie-policy/")}">Cookie policy</a></span>
      <button type="button" class="btn" data-cookie-accept>Accept</button>
    </div>"""


def wrap_page(page: dict, body: str, extra_head: str = "") -> str:
    url = page["url"]
    title = esc(page["title"])
    css = asset(url, "brand.css")
    js = asset(url, "brand.js")
    wires = wires_href(url)
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{title} | Manifesto Growth Architects (branded preview)</title>
<link rel="stylesheet" href="{css}">{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="preview-note">Branded preview exploration. Not the source of truth: the <a href="{wires}">greyscale wireframe</a> remains the IA reference.</div>
{header_html(url, page["section"])}
{crumbs_html(url, page.get("crumbs") or [])}
<main id="main">
{body}
</main>
{footer_html(url)}
{profile_dialog_html()}
<script src="{js}"></script>
</body>
</html>
"""


def profile_dialog_html() -> str:
    return """
    <dialog class="profile-dialog" id="profileDialog" aria-labelledby="profileName">
      <div class="dialog-inner">
        <button type="button" class="dialog-close" aria-label="Close">&#10005;</button>
        <div class="dialog-head">
          <div class="avatar" aria-hidden="true"></div>
          <div>
            <h3 id="profileName" data-d-name>Name</h3>
            <p class="dialog-role" data-d-role>Role</p>
          </div>
        </div>
        <p data-d-bio>Short biography.</p>
        <a class="more" data-d-link href="#">Full profile</a>
      </div>
    </dialog>"""


# ---------------------------------------------------------------------------
# Branded component helpers
# ---------------------------------------------------------------------------

def img_ph(label: str = "Image", cls: str = "") -> str:
    return f'<div class="img-ph {cls}" role="img" aria-label="Image placeholder: {esc(label)}"><span class="ph-label">{esc(label)}</span></div>'


def section(inner: str, cls: str = "", sid: str = "") -> str:
    idattr = f' id="{sid}"' if sid else ""
    return f'<section class="section {cls}"{idattr}><div class="wrap">{inner}</div></section>'


def sec_head(h2: str, eyebrow: str = "", lead: str = "") -> str:
    e = f'<span class="eyebrow">{esc(eyebrow)}</span>' if eyebrow else ""
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="sec-head">{e}<h2>{h2}</h2>{l}</div>'


def cta(h, primary=("Get in touch", "/contact/"), secondary=("See our work", "/work/")) -> str:
    sec = f'<a class="btn-text" href="{h(secondary[1])}">{esc(secondary[0])}</a>' if secondary else ""
    return f'<div class="cta"><a class="btn" href="{h(primary[1])}">{esc(primary[0])}</a>{sec}</div>'


def closing_band(h, line="Tell us about your growth challenge", btn=("Get in touch", "/contact/"), text=("See our work", "/work/")) -> str:
    return f"""
    <section class="closing on-dark">
      <div class="wrap">
        <p class="line">{esc(line)}</p>
        {cta(h, btn, text)}
      </div>
    </section>"""


def offer_card(h, href, title, sub) -> str:
    return (f'<a class="card offer" href="{h(href)}"><span class="card-title">{esc(title)}</span>'
            f'<span class="card-sub">{esc(sub)}</span><span class="card-arrow">Explore</span></a>')


def person_card(h, name, role, bio="Short biography, two or three lines (placeholder).") -> str:
    """Person card that opens the accessible profile pop-up. The full profile
    page stays a plain link inside the card for search and no-JS."""
    return f"""<div class="card person">
      <span class="avatar" aria-hidden="true"></span>
      <span class="card-title">{esc(name)}</span>
      <span class="card-sub">{esc(role)}</span>
      <button type="button" class="card-arrow" data-profile-trigger data-name="{esc(name)}" data-role="{esc(role)}" data-bio="{esc(bio)}" style="text-align:left">Quick view</button>
      <a class="link small" href="{h("/about/team/advisor-one/")}">Full profile</a>
    </div>"""


def tl_card(h, href, title, excerpt, primary, secondary=(), type_label=None, type_slug=None, data_dims="") -> str:
    pill = f'<span class="tl-pill">{esc(primary)}</span>'
    kind = f'<span class="tl-type">{esc(type_label)}</span>' if type_label else ""
    tags = ""
    if secondary:
        tags = '<span class="tl-tags">' + "".join(f"<em>{esc(t)}</em>" for t in secondary) + "</span>"
    data = ""
    if type_slug:
        tag_slugs = " ".join(w.slugify(t) for t in (primary, *secondary))
        data = f' data-type="{type_slug}" data-tags="{tag_slugs}"'
    return (
        f'<a class="card tl"{data}{data_dims} href="{h(href)}">{img_ph(title)}'
        f'<span class="tl-body"><span class="tl-head">{pill}{kind}</span>'
        f'<span class="card-title">{esc(title)}</span><span class="tl-excerpt">{esc(excerpt)}</span>'
        f'{tags}<span class="tl-more">Read more</span></span></a>'
    )


def metrics(pairs) -> str:
    inner = "".join(f'<div class="metric"><strong>{esc(v)}</strong><span>{esc(l)}</span></div>' for v, l in pairs)
    return f'<div class="metrics">{inner}</div>'


def quote(text='"The work changed how we think about growth."', cite="Client") -> str:
    return f'<blockquote class="quote"><p>{esc(text)}</p><cite>{esc(cite)}</cite></blockquote>'


def video(label="Video", caption: str | None = None) -> str:
    cap = f"<figcaption>{esc(caption)}</figcaption>" if caption else ""
    return (f'<figure class="video"><div class="video-ph" role="img" aria-label="Video placeholder: {esc(label)}">'
            f'<span class="play" aria-hidden="true">&#9654;</span></div>{cap}</figure>')


def logos(n=8, label="Logo") -> str:
    cells = "".join(f'<span class="logo-ph">{esc(label)} {i + 1}</span>' for i in range(n))
    return f'<div class="logos" aria-label="{esc(label)}s">{cells}</div>'


def logo_band(n=10) -> str:
    cells = "".join(f'<span class="logo-ph">Logo {i + 1}</span>' for i in range(n))
    return f'<div class="logo-band" aria-label="Client logos"><div class="band-track">{cells}</div></div>'


def tags(h, items) -> str:
    inner = "".join(f'<a href="{h(u)}">{esc(n)}</a>' for n, u in items)
    return f'<div class="page-tags">{inner}</div>'


def link_list(items) -> str:
    lis = "".join(
        f'<li><a href="{u}">{label}</a>{("<span class=\'meta\'>" + esc(meta) + "</span>") if meta else ""}</li>'
        for label, u, meta in items
    )
    return f'<ul class="list">{lis}</ul>'


def situations(items, linked=True) -> str:
    lis = ""
    for item in items:
        if linked and isinstance(item, tuple):
            label, u = item
            lis += f'<li><a href="{u}">{esc(label)}</a></li>'
        else:
            lis += f"<li><span>{esc(item)}</span></li>"
    return f'<ul class="situations">{lis}</ul>'


def carousel(cards_html: str, label="Related case studies") -> str:
    return f"""
      <div class="carousel" data-carousel>
        <div class="carousel-track" role="group" aria-label="{esc(label)}" tabindex="0">{cards_html}</div>
        <div class="carousel-controls">
          <button type="button" class="carousel-btn" data-prev aria-label="Previous">&#8592;</button>
          <button type="button" class="carousel-btn" data-next aria-label="Next">&#8594;</button>
        </div>
      </div>"""


def empty_state(message, btn_label="Clear filters") -> str:
    return f"""
      <div data-filter-empty style="display:none">
        <div class="empty-state"><p>{esc(message)}</p><a class="btn" href="#">{esc(btn_label)}</a></div>
      </div>"""


def form_field(label, ftype="text", name="", hint="", error_msg="") -> str:
    name = name or w.slugify(label)
    hint_html = f'<span class="field-hint">{esc(hint)}</span>' if hint else ""
    err = f'<span class="field-msg" hidden>{esc(error_msg)}</span>' if error_msg else ""
    if ftype == "textarea":
        control = f'<textarea id="f-{name}" name="{name}"></textarea>'
    elif ftype == "select":
        control = (f'<select id="f-{name}" name="{name}"><option>Select a service</option>'
                   "<option>Growth Strategy</option><option>Activation Services</option><option>CEO Advisory</option></select>")
    else:
        control = f'<input id="f-{name}" name="{name}" type="{ftype}">'
    return f'<div class="field"><label for="f-{name}">{esc(label)}</label>{control}{err}{hint_html}</div>'


def stat_rail(h, stats, cta_line, cta_label="Contact us") -> str:
    boxes = "".join(f'<div class="metric"><strong>{esc(v)}</strong><span>{esc(l)}</span></div>' for v, l in stats)
    return (f'<aside class="stat-rail on-dark" aria-label="Results at a glance">{boxes}'
            f'<p class="rail-line">{esc(cta_line)}</p><a class="btn" href="{h("/contact/")}">{esc(cta_label)}</a></aside>')


def steps(items) -> str:
    lis = "".join(f"<li><span>{esc(s)}</span></li>" for s in items)
    return f'<ol class="steps">{lis}</ol>'


def tri(h, line="") -> str:
    tiles = "".join(
        f'<a href="{h(u)}"><strong>{esc(n)}</strong><span>{esc(s)}</span></a>'
        for n, u, s in w.PILLAR_TILES
    )
    tl = f'<p class="tri-line">{line}</p>' if line else ""
    return f'<div class="tri on-dark">{tiles}</div>{tl}'


def civd(compact=False) -> str:
    cls = "civd-grid compact" if compact else "civd-grid"
    cells = [
        ("Customer", "Who you grow with."),
        ("Innovation", "What you offer next."),
        ("Value", "Where the economics move."),
        ("Delivery", "Whether it can be executed."),
    ]
    inner = "".join(f'<div class="civd-cell"><strong>{n}</strong><span>{t}</span></div>' for n, t in cells)
    return f'<div class="{cls}" aria-label="Customer, Innovation, Value and Delivery">{inner}</div>'


# ---------------------------------------------------------------------------
# Page bodies for the key templates
# ---------------------------------------------------------------------------

def home_body(page) -> str:
    h = lambda u: rel_href("/", u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <h1>Manifesto partner with ambitious leaders<span class="accent">to deliver sustainable, customer-led growth.</span></h1>
        <p class="lead">Strategy that works. Execution that delivers.</p>
        {cta(h, ("Get in touch", "/contact/"), ("What we do", "/services/"))}
        <div class="hero-media">{video("Manifesto showreel / client video", "Existing film, confirmed for Home (Andy, 1 October). Embedded in the hero, not a placeholder.")}</div>
      </div>
    </section>"""
    partners = section(sec_head("Trusted partners", eyebrow="Who we work with") + logos(8, "Logo"), cls="band-stone")
    what = section(
        sec_head("What we do", eyebrow="Our Growth Architecture")
        + tri(h, f'Strategy first. Activation to deliver it. Advisors alongside. <a class="link" href="{h("/services/")}">Our Growth Architecture</a>'),
    )
    thinking = f"""
    <section class="band-slate on-dark">
      <div class="wrap">
        {sec_head("Our thinking", eyebrow="Latest insights and reports")}
        <div class="cards">
          {tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "Featured report. From tactical lever to growth engine.", "Growth Strategy", ("Pricing",), "Report")}
          {tl_card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Short excerpt of the argument (placeholder).", "Proposition Innovation", ("Loyalty",), "Article")}
          {tl_card(h, "/insights/pricing-paradox/", "Pricing Paradox launch event", "Recap and what was discussed (placeholder).", "Growth Strategy", ("Pricing",), "News and events")}
        </div>
        <a class="more" href="{h("/insights/")}">All thinking</a>
      </div>
    </section>"""
    work = section(
        sec_head("Our work", eyebrow="Proof")
        + f"""<div class="cards two">
          {tl_card(h, "/work/dayinsure/", "Dayinsure", "One-line result (placeholder).", "Experience Engineering", ("Financial services",))}
          {tl_card(h, "/work/key-group/", "Key Group", "One-line result (placeholder).", "Experience Engineering", ("Financial services",))}
        </div>"""
        + quote('"Attributed client quote: what changed and why it mattered. Placeholder, no invented facts."', "Name, role, Dayinsure (to be confirmed)")
        + f'<a class="more" href="{h("/work/")}">All work</a>',
    )
    awards = section(sec_head("Awards") + logos(3, "Award"), cls="band-stone iso-edge")
    problems = section(
        sec_head("Growth problems we know best", eyebrow="Expertise")
        + f"""<div class="row-links">
          <a href="{h("/expertise/loyalty/")}">Loyalty</a>
          <a href="{h("/expertise/membership/")}">Membership</a>
          <a href="{h("/expertise/subscriptions/")}">Subscriptions</a>
          <a href="{h("/expertise/pricing/")}">Pricing</a>
          <a href="{h("/expertise/customer-value/")}">Customer Value</a>
        </div>""",
    )
    return hero + partners + what + thinking + work + awards + problems + closing_band(h)


def hub_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">What we do</span>
        <h1>Our Growth Architecture</h1>
        <p class="lead">Strategy that works. Execution that delivers.</p>
        <p class="lead">The path from strategy to execution has become more complex and fragmented, despite more tools, data and channels than ever.</p>
        <p class="lead">Growth Architecture is a better way to unlock customer value growth: market-leading strategic thinking combined with AI-powered, human-led activation.</p>
      </div>
    </section>"""
    three = section(
        sec_head("Three ways we work with you")
        + f"""<div class="tri on-dark">
            <a href="#hub-gs"><strong>Growth Strategy</strong><span>Where and how you grow</span></a>
            <a href="#hub-act"><strong>Activation Services</strong><span>Turning strategy into results</span></a>
            <a href="#hub-ceo"><strong>CEO Advisory</strong><span>One-to-one support for leaders</span></a>
          </div><p class="tri-line">Strategy first. Activation to deliver it. Advisors alongside.</p>""",
    )
    starting = section(
        sec_head("Where are you starting from?")
        + situations([
            ("We need to decide where and how to grow", h("/services/growth-strategy/")),
            ("We need a new proposition, loyalty or membership offer", h("/services/proposition-innovation/")),
            ("We need to understand our customers better", h("/services/customer-research/")),
            ("Our journeys or website are not converting", h("/services/experience-engineering/")),
            ("Our strategy is not turning into results", h("/services/activation/")),
            ("We want AI to pay off", h("/services/ai-enablement/")),
            ("I want a sounding board I trust", h("/services/ceo-advisory/")),
        ]),
        cls="band-stone",
    )
    gs = section(
        f'<div class="sec-head"><span class="eyebrow">Pillar</span><h2><a class="link" href="{h("/services/growth-strategy/")}">Growth Strategy</a></h2>'
        f'<p class="lead">Where and how you grow</p></div>'
        f'<p class="prose measure">We work out where the growth is and design the propositions that win it, using our '
        f'<a href="{h("/services/growth-strategy/#civd")}">Customer, Innovation, Value and Delivery</a> frame.</p>'
        + civd(compact=True)
        + f'<p class="prose link-line">The frame lives on Growth Strategy. <a href="{h("/services/growth-strategy/#civd")}">See the CIVD frame</a></p>'
        + f"""<div class="cards two">
            {offer_card(h, "/services/growth-strategy/", "Growth Strategy", "Customer-led growth strategy: where to focus and how to win")}
            {offer_card(h, "/services/proposition-innovation/", "Proposition Innovation", "Value proposition design: loyalty, membership, subscription, direct-to-consumer")}
          </div>"""
        + f'<p class="prose case-line">Key Group, one-line result. <a href="{h("/work/key-group/")}">Read the case study</a></p>',
        sid="hub-gs",
    )
    act = section(
        f'<div class="sec-head"><span class="eyebrow">Pillar</span><h2><a class="link" href="{h("/services/activation/")}">Activation Services</a></h2>'
        f'<p class="lead">Turning strategy into results</p></div>'
        f'<p class="prose measure">We build the bridge from strategy to results: new operating models and AI-powered, human-led delivery. '
        f'<a href="{h("/services/activation/")}">Which of the six do you need?</a></p>'
        + f"""<div class="cards">
            {offer_card(h, "/services/customer-research/", "Customer Research and Insight", "Research, surveys, analytics and customer listening, faster with AI")}
            {offer_card(h, "/services/experience-engineering/", "Experience Engineering", "Customer experience (CX), website and digital design, build and testing")}
            {offer_card(h, "/services/ai-agents-for-marketing/", "AI Agents for Marketing", "AI marketing agents that clean data and improve performance, guided by experts")}
            {offer_card(h, "/services/operating-model-design/", "Operating Model Design", "Target operating model: how teams, data and AI agents work together")}
            {offer_card(h, "/services/value-orchestration/", "Value Orchestration", "Interim growth team and programme office that gets strategy delivered")}
            {offer_card(h, "/services/ai-enablement/", "AI Enablement", "AI skills, training and adoption: finding where AI pays off")}
          </div>"""
        + f'<p class="prose case-line">Dayinsure, one-line result. <a href="{h("/work/dayinsure/")}">Read the case study</a></p>',
        cls="band-stone",
        sid="hub-act",
    )
    ceo = section(
        f'<div class="sec-head"><span class="eyebrow">Pillar</span><h2><a class="link" href="{h("/services/ceo-advisory/")}">CEO Advisory</a></h2>'
        f'<p class="lead">One-to-one support for leaders</p></div>'
        f'<p class="prose measure">Experienced growth leaders alongside you, on retainer, to help you make good decisions.</p>'
        + f"""<div class="cards">
            {person_card(h, "Advisor name", "Former role, one line")}
            {person_card(h, "Advisor name", "Former role, one line")}
            {person_card(h, "Advisor name", "Former role, one line")}
          </div>"""
        + f'<a class="more" href="{h("/services/ceo-advisory/#advisors")}">Our advisors</a>',
        sid="hub-ceo",
    )
    expertise = section(
        f'<p class="prose lead">We apply these services to the growth problems we know best. <a href="{h("/expertise/")}">Our expertise</a></p>'
    )
    return hero + three + starting + gs + act + ceo + expertise + closing_band(h)


def service_body(page) -> str:
    """Service detail, following the client (Mural, 15 Oct) layout in the wires:
    Hero > Overview > Why now? > How can we help you? > Related case studies
    (carousel) > Why us? > Our experts (pop-up) > How it works > Related."""
    url = page["url"]
    h = lambda u: rel_href(url, u)
    mod_parts = w.service_module(page, h)

    sits = situations(page["situations"], linked=False)
    nums = metrics([("3x", "EBITDA return on investment, consistently")]) if page.get("numbers") and "3x" in page["numbers"] else ""
    pillar = (f'<p class="pillar-note"><a href="{h(page["pillar"][1])}">{esc(page["pillar"][0])}</a></p>'
              if page.get("pillar") else "")
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">{esc(page["pillar"][0].replace("Part of ", "") if page.get("pillar") else "Service")}</span>
        <h1>{esc(page["h1"])}</h1>
        <p class="lead">{esc(page["hero"])}</p>
        <p class="who">{esc(page["who"])}</p>
        {nums}
        {pillar}
        {cta(h)}
        <div class="hero-media">{img_ph("Service image", "wide slate-ph")}</div>
      </div>
    </section>"""
    overview = section(sec_head("Overview") + '<p class="prose measure">What this service is and the value it creates, in two or three plain sentences.</p>')
    why_now = section(sec_head("Why now?") + sits + '<p class="prose measure">Two to four short paragraphs on why this matters now.</p>', cls="band-stone")
    help_sec = section('<div class="prose">' + sec_head("How can we help you?") + mod_parts["help"] + "</div>")
    cases = section(
        sec_head("Related case studies", eyebrow="Proof")
        + carousel(
            tl_card(h, "/work/dayinsure/", "Dayinsure", "One-line result (placeholder).", "Experience Engineering", ("Financial services", "Customer value"))
            + tl_card(h, "/work/key-group/", "Key Group", "One-line result (placeholder).", "Experience Engineering", ("Financial services", "Loyalty"))
            + tl_card(h, "/work/", "All our work", "Every case study, filterable by industry and service.", "Our work")
        )
        + f'<a class="more" href="{h("/work/")}">All work</a>',
        cls="band-stone",
    )
    why_us = section(sec_head("Why us?") + f'<p class="prose measure">Why Manifesto for this work: the team, the method, the results. Plain words, no claims we cannot prove. <a href="{h("/about/how-we-work/")}">Our approach</a>.</p>')
    experts = section(
        sec_head("Our experts")
        + f"""<div class="cards">
            {person_card(h, "Expert name", "Role, one line")}
            {person_card(h, "Expert name", "Role, one line")}
            {person_card(h, "Expert name", "Role, one line")}
          </div>""",
        cls="band-stone",
    )
    how = section('<div class="prose">' + sec_head("How it works") + '<p class="prose measure">Find, Redesign, Test, Scale: the sequence an engagement runs in.</p></div>')
    related = section(
        sec_head("Related")
        + "<h3>Related expertise</h3>" + tags(h, (page.get("themes") or [])[:3])
        + "<h3>Related services</h3>"
        + '<div class="cards two">'
        + "".join(offer_card(h, u, n, "Often bought alongside") for n, u in (page.get("services") or [])[:2])
        + "</div>"
        + "<h3>Related thinking</h3>"
        + link_list([
            ("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report"),
            ("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article"),
        ]),
    )
    return hero + overview + why_now + help_sec + cases + why_us + experts + how + related + closing_band(h)


def work_hub_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Our work</span>
        <h1>Our work</h1>
        <p class="lead">Our clients: ambitious leaders who want sustainable, customer-led growth.</p>
        <p class="lead">Short intro. What the work has in common, in two plain sentences.</p>
      </div>
    </section>"""
    clients = section(sec_head("Our clients", eyebrow="Trusted partners") + logo_band(10), cls="band-stone")

    def case(href, title, industry, service, themes):
        dims = f' data-industry="{w.slugify(industry)}" data-service="{w.slugify(service)}"'
        return tl_card(h, href, title, "One-line result or testimony (placeholder).", service, (industry,) + themes, data_dims=dims)

    industries = ["Financial services", "Consumer", "Media", "Retail", "Energy"]
    services = ["Growth Strategy", "Proposition Innovation", "Experience Engineering", "Customer Research and Insight"]
    ind_bar = ('<div class="filters" role="group" aria-label="Filter by industry"><span class="group-label">Industry</span>'
               + '<button type="button" class="filter on" data-filter-industry="" aria-pressed="true">All industries</button>'
               + "".join(f'<button type="button" class="filter" data-filter-industry="{w.slugify(i)}" aria-pressed="false">{esc(i)}</button>' for i in industries)
               + "</div>")
    svc_bar = ('<div class="filters" role="group" aria-label="Filter by service"><span class="group-label">Service</span>'
               + '<button type="button" class="filter on" data-filter-service="" aria-pressed="true">All services</button>'
               + "".join(f'<button type="button" class="filter" data-filter-service="{w.slugify(s)}" aria-pressed="false">{esc(s)}</button>' for s in services)
               + "</div>")
    listing = section(
        sec_head("All case studies")
        + ind_bar + svc_bar
        + '<div class="cards" data-work-grid>'
        + case("/work/dayinsure/", "Dayinsure", "Financial services", "Experience Engineering", ("Customer value",))
        + case("/work/key-group/", "Key Group", "Financial services", "Experience Engineering", ("Loyalty",))
        + "</div>"
        + empty_state("No case studies match these filters.")
        + f'<a class="more" href="{h("/work/")}">See more</a>',
    )
    testimony = section(
        sec_head("Client testimony")
        + video("Client testimony film", "Name, role, client (to be confirmed)"),
        cls="band-stone",
    )
    related = section(
        sec_head("Related thinking")
        + link_list([
            ("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report"),
            ("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article"),
        ])
        + f'<a class="more" href="{h("/insights/")}">All thinking</a>',
    )
    return hero + clients + listing + testimony + related + closing_band(h)


def case_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    pills = tags(
        h,
        (page.get("services") or [])[:2]
        + [(page["sector_name"], page["sector_url"])]
        + (page.get("themes") or [])[:1],
    )
    other = "/work/key-group/" if url == "/work/dayinsure/" else "/work/dayinsure/"
    other_name = "Key Group" if url == "/work/dayinsure/" else "Dayinsure"
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Case study</span>
        <h1>{esc(page["client"])}</h1>
        <p class="lead">Project title: the proposition and the outcome in one line (placeholder).</p>
        {pills}
        <div class="hero-media">{img_ph("Case study main image", "wide slate-ph")}</div>
      </div>
    </section>"""
    story = f"""
    <section class="section">
      <div class="wrap">
        <div class="case-layout">
          {stat_rail(h, [("Stat TBC", "Outcome measure, with the client's words"), ("Stat TBC", "Outcome measure, with the client's words")], "Got a growth challenge like this one?")}
          <div class="case-story">
            <h2>Client testimonial</h2>
            {quote('"Attributed client quote: what changed and why it mattered. Placeholder, no invented facts."', "Name, role, " + page["client"] + " (to be confirmed)")}
            {video("Film snippet, where one exists")}
            <div class="prose">
              <h2>The Opportunity</h2>
              <p>The challenge the client faced and what they needed, in plain words. Sector: <a href="{h(page["sector_url"])}">{esc(page["sector_name"])}</a>.</p>
              <h2>The Solution</h2>
              <p>The approach we took, step by step, with the services linked from the work.</p>
              <h2>The Impact</h2>
              <ul class="impact-list">
                <li><strong>Outcome one:</strong> what improved, quantified where permitted (placeholder).</li>
                <li><strong>Outcome two:</strong> what it opened up for the client (placeholder).</li>
                <li><strong>Outcome three:</strong> where the client is now (placeholder).</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>"""
    more = section(
        sec_head("See more of our case studies")
        + f"""<div class="cards two">
          {tl_card(h, other, other_name, "One-line result or testimony (placeholder).", "Experience Engineering", ("Financial services",))}
        </div>"""
        + f'<a class="more" href="{h("/work/")}">All work</a>',
        cls="band-stone",
    )
    related = section(
        sec_head("Related thinking")
        + link_list([
            ("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report"),
            ("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article"),
        ])
        + f'<a class="more" href="{h("/insights/")}">All thinking</a>',
    )
    return hero + story + more + related + closing_band(h)


def insights_hub_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Our thinking</span>
        <h1>Our thinking</h1>
        <p class="lead">Reports, articles, news and events: one grid, one card.</p>
      </div>
    </section>"""
    tabs = ('<div class="type-tabs" role="group" aria-label="Filter by type">'
            '<button type="button" class="type-tab on" data-type="all" aria-pressed="true">All</button>'
            '<button type="button" class="type-tab" data-type="reports" id="reports" aria-pressed="false">Reports</button>'
            '<button type="button" class="type-tab" data-type="articles" id="articles" aria-pressed="false">Articles</button>'
            '<button type="button" class="type-tab" data-type="news-events" id="news-events" aria-pressed="false">News and events</button>'
            "</div>")
    pills = ('<div class="filters" role="group" aria-label="Filter by tag">'
             + "".join(
                 f'<button type="button" class="filter" data-tag="{w.slugify(t)}" aria-pressed="false">{esc(t)}</button>'
                 for t in ["Loyalty", "Pricing", "Customer Value", "Growth Strategy", "Financial services"])
             + "</div>")
    grid = ('<div class="cards" data-filter-grid>'
            + tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "From tactical lever to growth engine. Read on its page; no download here.", "Growth Strategy", ("Pricing",), "Report", type_slug="reports")
            + tl_card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Short excerpt of the argument (placeholder).", "Proposition Innovation", ("Loyalty",), "Article", type_slug="articles")
            + tl_card(h, "/insights/pricing-paradox/", "Pricing Paradox launch event", "Recap and what was discussed (placeholder).", "Growth Strategy", ("Pricing",), "News and events", type_slug="news-events")
            + "</div>")
    listing = section(
        sec_head("All thinking")
        + tabs + pills + grid
        + empty_state("No thinking matches these filters.")
        + f'<a class="more" href="{h("/insights/")}">See more</a>',
    )
    nutshell = section(
        sec_head("The Nutshell")
        + f'<p class="prose measure">Events, thought leadership and what has caught our attention. <a href="{h("/newsletter/")}">Sign up to The Nutshell</a></p>',
        cls="band-stone iso-edge",
    )
    related = section(
        sec_head("Related services")
        + f"""<div class="row-links">
          <a href="{h("/services/")}">What we do</a>
          <a href="{h("/expertise/")}">Expertise</a>
          <a href="{h("/work/")}">Our work</a>
        </div>""",
    )
    return hero + listing + nutshell + related + closing_band(h)


def insight_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Our thinking</span>
        <h1>{esc(page["h1"])}</h1>
        <p class="article-meta">Article &middot; 6 min &middot; Author</p>
        {tags(h, [("Loyalty", "/expertise/loyalty/")])}
        <div class="hero-media">{img_ph("Article image", "wide")}</div>
      </div>
    </section>"""
    body = section(
        '<div class="prose article-body">'
        + "<h2>The problem</h2>"
        + "<p>Opening argument. Two or three sentences that set the problem.</p>"
        + "<p>The view we take, and why the usual response fails.</p>"
        + "<p>What we would do next, in brief, with a link to the relevant service.</p>"
        + "<h2>What we think</h2>"
        + f'<p>One or two arguments. In-line links to <a href="{h("/expertise/loyalty/")}">Loyalty</a> where the argument touches it.</p>'
        + "</div>",
    )
    related = section(
        sec_head("Related")
        + '<div class="cards">'
        + tl_card(h, "/insights/", "Next article (placeholder)", "Where the argument goes next.", "Our thinking", (), "Article")
        + offer_card(h, "/services/proposition-innovation/", "Proposition Innovation", "Value proposition design")
        + tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "From tactical lever to growth engine.", "Growth Strategy", ("Pricing",), "Report")
        + "</div>",
        cls="band-stone",
    )
    return hero + body + related + closing_band(h)


def report_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Insights</span>
        <h1>{esc(page["h1"])}</h1>
        <p class="article-meta">Report &middot; Date &middot; Author</p>
        {tags(h, [("Pricing", "/expertise/pricing/")])}
      </div>
    </section>"""
    covers = section(
        '<div class="prose">'
        + sec_head("What this report covers")
        + "<p>Opening argument. Two or three sentences that set the problem.</p>"
        + "<p>The view we take, and why the usual response fails.</p>"
        + "<p>What we would do next, in brief, with a link to the relevant service.</p>"
        + "</div>",
    )
    gate = section(
        sec_head("Read it on this page")
        + '<p class="prose measure">The full report continues here. The email gate lives on this page, never on the grid. Whether the body is gated or reads in full on the page is an open item with the client.</p>'
        + f"""
        <div class="gate">
          <h3>Get the full report</h3>
          <form id="gateForm" novalidate>
            {form_field("Full name")}
            {form_field("Work email", "email", error_msg="Enter a valid work email.")}
            {form_field("Company")}
            {form_field("Receive updates on events, thought leadership and The Nutshell (optional)", "checkbox", name="updates")}
            <button type="submit" class="btn">Submit</button>
            <p class="gate-note">Preview behaviour: submitting reveals the report on this page. Nothing is sent anywhere.</p>
          </form>
        </div>
        <div class="gated-body prose" id="gatedBody" hidden>
          <h3>The full report</h3>
          <p>Full report body continues on the page (placeholder). Section one of the argument.</p>
          <p>Section two of the argument, with charts built from isometric shapes.</p>
          <p>Section three: what to do about it, linking to <a href="{h("/services/growth-strategy/")}">Growth Strategy</a>.</p>
        </div>""",
        cls="band-stone",
    )
    how = section(
        sec_head("How we help")
        + f'<p class="prose measure">Related: <a href="{h("/services/growth-strategy/")}">Growth Strategy</a> and <a href="{h("/expertise/pricing/")}">Pricing</a>.</p>',
    )
    return hero + covers + gate + how + closing_band(h)


def careers_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Careers</span>
        <h1>Careers at Manifesto</h1>
        <p class="lead">Brief description: what it is like to work here, and the roles we are hiring for.</p>
        <div class="cta">
          <a class="btn" href="#roles">See open positions</a>
          <a class="btn-text" href="#life">Life at Manifesto</a>
        </div>
        <div class="hero-media">{video("Studio film")}</div>
      </div>
    </section>"""
    life = section(
        '<div class="prose">'
        + sec_head("Life at Manifesto")
        + f'<p class="measure">What it is like to work here. <a href="{h("/about/values/")}">Values and culture</a>. Meet the team: <a href="{h("/about/team/")}">Our people</a>.</p>'
        + "<h3>Career change framing</h3><p class='measure'>We hire people who are changing direction, not only those already in the craft.</p>"
        + "<h3>We hire from multiple backgrounds</h3><p class='measure'>Agency, client and strategy backgrounds.</p>"
        + "<h3>Pioneers / recent joiners</h3><p class='measure'>Portraits of people who joined recently.</p>"
        + "</div>"
        + f"""<div class="cards">
          {person_card(h, "Name", "Recent joiner")}
          {person_card(h, "Name", "Recent joiner")}
          {person_card(h, "Name", "Recent joiner")}
        </div>""",
        sid="life",
    )
    values = section(
        sec_head("Values and culture")
        + '<div class="cards four">'
        + "".join(
            f'<a class="card theme" href="{h("/about/values/")}"><span class="card-title">Value {i}</span>'
            f'<span class="card-sub">One line on what it means here (placeholder)</span></a>'
            for i in range(1, 5))
        + "</div>",
        cls="band-stone",
    )
    dei = section(sec_head("Diversity, equity and inclusion") + '<p class="prose measure">Commitments in the hiring context.</p>')
    benefits = section(sec_head("Benefits") + '<p class="prose measure">Employee benefits.</p>', cls="band-stone iso-edge")
    process = section(sec_head("Application process") + steps(["Application", "Interview with Partners", "Case study", "References", "Decision"]))
    role_toggle = ('<div class="filters" role="group" aria-label="Filter roles">'
                   '<button type="button" class="filter on" data-role-filter="open" aria-pressed="true">Open positions</button>'
                   '<button type="button" class="filter" data-role-filter="all" aria-pressed="false">All</button>'
                   "</div>")
    roles = section(
        sec_head("Roles")
        + f'<p class="prose measure">Reach out even if the open roles are not what you are after: <a href="{h("/contact/#work-for-us")}">Work for us</a>.</p>'
        + role_toggle
        + '<div class="cards two" data-role-list>'
        + f'<a class="card role" data-hiring="true" href="{h("/careers/growth-architect/")}"><span class="meta">London &middot; Full time &middot; Actively hiring</span>'
        + '<span class="card-title">Growth Architect</span><span class="card-sub">Full description on the role page.</span><span class="card-arrow">View role</span></a>'
        + f'<a class="card role" data-hiring="false" href="{h("/careers/growth-architect/")}"><span class="meta">Location TBC &middot; Not actively hiring</span>'
        + '<span class="card-title">Example closed role (placeholder)</span><span class="card-sub">Shown by the All toggle to prove the behaviour. Not a real vacancy.</span><span class="card-arrow">View role</span></a>'
        + "</div>",
        cls="band-stone",
        sid="roles",
    )
    return (hero + life + values + dei + benefits + process + roles
            + closing_band(h, "Interested in joining the team?", ("Work for us", "/contact/#work-for-us"), ("Our people", "/about/team/")))


# ---------------------------------------------------------------------------
# Branded component library (mirrors /catalogue/ and adds the proposed system)
# ---------------------------------------------------------------------------

def unit(name: str, sample: str, dark=False) -> str:
    group, kind, purpose = w.COMPONENTS[name]
    cls = "catalogue-item on-slate on-dark" if dark else "catalogue-item"
    return f"""
      <div class="{cls}" id="{w.slugify(name)}">
        <div class="unit-head"><span class="cat-label">{esc(name)}</span><span class="unit-kind">{esc(kind)}</span></div>
        <p class="unit-purpose">{esc(purpose)}</p>
        {sample}
      </div>"""


def swatch(name, hexc, note="", border=False) -> str:
    b = " bordered" if border else ""
    return (f'<div class="swatch"><div class="chip{b}" style="background:{hexc}"></div>'
            f'<div class="info"><strong>{esc(name)}</strong><code>{hexc}</code>{(" &middot; " + esc(note)) if note else ""}</div></div>')


def catalogue_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    logo_white = asset(url, "logos/logo-white.svg")

    hero = f"""
    <section class="hero on-dark">
      <div class="wrap">
        <span class="eyebrow">Branded preview</span>
        <h1>Component library</h1>
        <p class="lead">Every reusable block from the wireframe library, skinned with the October 2026 identity. Where the Toolkit is silent (type scale, spacing, grid, states), the system shown here is a proposal for Bruno to accept, adapt or replace. Findings and open questions live in branded/FINDINGS.md.</p>
      </div>
    </section>"""

    palette = section(
        sec_head("Colour", eyebrow="Foundations", lead="Palette as printed in the Toolkit (p4). Green is a fill with Slate text, or text on Slate. Green text on White fails contrast (1.5:1) and is never used.")
        + "<h3>Core</h3><div class='swatches'>"
        + swatch("Slate", "#00211f") + swatch("Manifesto Green", "#b7e226")
        + swatch("White", "#ffffff", "assumed", border=True)
        + "</div><h3>Neutrals</h3><div class='swatches'>"
        + swatch("Clay", "#e4dfdb", border=True) + swatch("Stone", "#f7f2ef", border=True)
        + "</div><h3>Background tints (Toolkit p5)</h3><div class='swatches'>"
        + swatch("Slate 95", "#0d2c2a") + swatch("Slate 90", "#1a3735")
        + swatch("Green 85", "#c2e646") + swatch("Green 70", "#cdeb67")
        + swatch("Clay 85", "#e8e4e1", border=True) + swatch("Clay 70", "#ece9e6", border=True)
        + "</div><h3>Secondary (sparingly: infographics and report covers, not page chrome)</h3><div class='swatches'>"
        + swatch("Turquoise", "#39be9e", "printed hex conflicts, see FINDINGS")
        + swatch("Purple", "#645faa") + swatch("Blue", "#286fb7") + swatch("Yellow", "#fdb941")
        + "</div>",
    )

    type_scale = section(
        sec_head("Typography", eyebrow="Foundations", lead="Anton for headlines and caption headers only, sentence case. IBM Plex Sans for everything else. Both self-hosted (SIL OFL). The scale is a proposal built from the ratios in the Toolkit p15 website mock.")
        + """<div class="type-specimen"><span class="spec-meta">H1 / Anton / clamp 40 to 80px / 1.12</span><span class="display" style="font-size:var(--fs-h1)">Every business wants to grow.</span></div>
        <div class="type-specimen"><span class="spec-meta">H2 / Anton / clamp 28 to 44px / 1.15</span><span class="display" style="font-size:var(--fs-h2)">Businesses set growth targets.</span></div>
        <div class="type-specimen"><span class="spec-meta">H3 / Plex SemiBold / 20px (Anton below 24px loses legibility, see FINDINGS)</span><h3 style="margin:0">A third-level heading in Plex</h3></div>
        <div class="type-specimen"><span class="spec-meta">Lead / Plex Medium / 18 to 22px</span><p class="lead" style="margin:0">The questions that unlock growth rarely sit neatly within one team, function or discipline.</p></div>
        <div class="type-specimen"><span class="spec-meta">Body / Plex / 17px / 1.55</span><p style="margin:0">Body copy carries the keyword language the heading promises. No em dashes. British English.</p></div>
        <div class="type-specimen"><span class="spec-meta">Eyebrow / Plex SemiBold / 13px / uppercase, tracked 0.14em</span><span class="eyebrow" style="margin:0">Why Manifesto Growth Architects</span></div>""",
        cls="band-stone",
    )

    layout = section(
        sec_head("Spacing, grid, radii, elevation", eyebrow="Foundations (all proposals)")
        + """<table class="spec-table">
        <tr><th>Spacing</th><td>4px base scale: 4, 8, 12, 16, 24, 32, 48, 64, 96. Section padding clamp(48px, fluid, 96px).</td></tr>
        <tr><th>Grid</th><td>Content max 1240px with fluid gutters (20 to 40px); the Toolkit mock shows roughly 89% content width at 1440. Cards run 3 across desktop, 2 at 960px, 1 at 640px.</td></tr>
        <tr><th>Radii</th><td>0 everywhere. The identity is square-cornered and isometric; the wireframe's pill filters and rounded listing card become square here (see FINDINGS).</td></tr>
        <tr><th>Elevation</th><td>No blur shadows. Hover lifts use a solid offset slab in Green (an isometric extrusion), 6px by 6px.</td></tr>
        <tr><th>Imagery</th><td>No photography in this preview. The supplied isometric backgrounds stand in, and every image placeholder carries the green overlay radiating from the top left (Toolkit p3).</td></tr>
        <tr><th>Focus</th><td>3px outline, 2px offset: Slate on light grounds, Green on dark grounds.</td></tr>
        </table>""",
    )

    buttons = section(
        sec_head("Buttons and links", eyebrow="Foundations (states are proposals)")
        + """<h3>Primary button</h3>
        <div class="state-row"><span class="state-label">Default</span><span class="btn">Get in touch</span></div>
        <div class="state-row"><span class="state-label">Hover</span><span class="btn demo-hover">Get in touch</span></div>
        <div class="state-row"><span class="state-label">Focus</span><span class="btn demo-focus">Get in touch</span></div>
        <div class="state-row"><span class="state-label">Active</span><span class="btn demo-active">Get in touch</span></div>
        <div class="state-row"><span class="state-label">Disabled</span><span class="btn is-disabled">Get in touch</span></div>
        <h3>Secondary button</h3>
        <div class="state-row"><span class="state-label">Default</span><span class="btn-secondary">See our work</span></div>
        <div class="state-row"><span class="state-label">Hover</span><span class="btn-secondary demo-hover">See our work</span></div>
        <h3>Text button and inline link</h3>
        <div class="state-row"><span class="state-label">Text</span><span class="btn-text">Life at Manifesto</span></div>
        <div class="state-row"><span class="state-label">Inline</span><p class="prose" style="margin:0">Body copy with an <a href="#buttons">inline link</a>: Slate text, Green underline.</p></div>
        <div class="state-row"><span class="state-label">Arrow</span><span class="more" style="margin:0">All work</span></div>""",
        cls="band-stone",
        sid="buttons",
    )

    # Component samples, one per vocabulary name, in the wires' groups.
    samples: dict[str, str] = {
        "Header Contact": '<a class="btn" href="#">Get in touch</a>',
        "Mega-nav hub and strands": f"""<div class="pillar" style="max-width:320px">
            <p class="pillar-title"><a class="pillar-hub" href="#">Growth Strategy <span class="hub-chevron" aria-hidden="true">&#8594;</span></a></p>
            <p class="line">Where and how you grow</p>
            <ul>
              <li><a class="strand-overview" href="#">Overview<small>Where to grow and how to win</small></a></li>
              <li><a href="#">Proposition Innovation<small>Value proposition design</small></a></li>
            </ul>
          </div>""",
        "Breadcrumb": '<nav aria-label="Breadcrumb example" class="crumbs" style="background:none;border:0"><ol style="padding:0"><li><a href="#">Home</a></li><li><a href="#">Our work</a></li><li>Dayinsure</li></ol></nav>',
        "Cookie bar": """<div class="cookie-bar on-dark" style="position:static" role="presentation">
            <span>We use cookies to run this site. <a href="#">Cookie policy</a></span>
            <button type="button" class="btn">Accept</button>
          </div>""",
        "Hero": f"""<div class="hero on-dark" style="padding:2.5rem 0">
            <div class="wrap"><span class="eyebrow">What we do</span>
            <p class="display" style="font-size:2.25rem;line-height:1.12;margin:0 0 1rem;max-width:15em">Every business wants to grow.<span class="accent">Few are built to make it happen.</span></p>
            <p class="lead">One support line. Who this is for.</p>
            {cta(h)}</div>
          </div>""",
        "CTA pair": cta(h),
        "Closing CTA band": f"""<div class="closing on-dark" style="padding:2.5rem 0">
            <div class="wrap"><p class="line">Tell us about your growth challenge</p>{cta(h)}</div>
          </div>""",
        "Prose": '<div class="prose"><h3 style="margin-top:0">Heading</h3><p class="measure" style="margin:0">One to four short paragraphs. Body copy carries the keyword language the heading promises.</p></div>',
        "Metric box": metrics([("3x", "EBITDA return"), ("4 wks", "Data audit"), ("6 wks", "First agents")]),
        "Offer card": '<div class="cards two">' + offer_card(h, "/services/growth-strategy/", "Growth Strategy", "Customer-led growth strategy: where to focus and how to win") + offer_card(h, "/services/proposition-innovation/", "Proposition Innovation", "Value proposition design") + "</div>",
        "Theme card": '<div class="cards two"><a class="card theme" href="#"><span class="card-title">Loyalty</span><span class="card-sub">Cases and thinking</span><span class="card-arrow">Explore</span></a><a class="card theme" href="#"><span class="card-title">Pricing</span><span class="card-sub">Cases and thinking</span><span class="card-arrow">Explore</span></a></div>',
        "Case card": f'<div class="cards two"><a class="card case" href="#">{img_ph("Dayinsure")}<span class="case-body"><span class="card-title">Dayinsure</span><span class="card-sub">One-line result</span><span class="card-arrow">Read the case</span></span></a></div>',
        "Report card": '<div class="cards">' + f"""<a class="card report" href="#">
          <span class="report-cover">
            <span class="cover-top"><img src="{logo_white}" alt="" width="72" height="40"><span class="cover-label">Insights</span></span>
            <span class="cover-title">The Pricing Paradox</span>
          </span>
          <span class="card-title">The Pricing Paradox</span>
          <span class="card-sub">Report. From tactical lever to growth engine</span>
        </a>""" + "</div>",
        "Article card": '<div class="cards two"><a class="card" href="#"><span class="card-title">Loyalty without the discount</span><span class="card-sub">Article &middot; Loyalty</span><span class="card-arrow">Read more</span></a></div>',
        "Person card": '<div class="cards">' + person_card(h, "Advisor name", "Former role, one line") + "</div>",
        "Role card": '<div class="cards two"><a class="card role" href="#"><span class="meta">London &middot; Full time &middot; Actively hiring</span><span class="card-title">Growth Architect</span><span class="card-sub">Full description on the role page.</span><span class="card-arrow">View role</span></a></div>',
        "Triangle tile": tri(h, "Strategy first. Activation to deliver it. Advisors alongside."),
        "Thought leadership card": '<div class="cards two">' + tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "From tactical lever to growth engine.", "Growth Strategy", ("Pricing", "Financial services"), "Report") + "</div>",
        "Related trio": '<div class="cards">'
            + tl_card(h, "/insights/", "Next article (placeholder)", "Where the argument goes next.", "Our thinking", (), "Article")
            + offer_card(h, "/services/proposition-innovation/", "Proposition Innovation", "Service")
            + tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "Report.", "Growth Strategy", (), "Report")
            + "</div>",
        "Culture card": '<div class="cards four">' + "".join(f'<a class="card theme" href="#"><span class="card-title">Value {i}</span><span class="card-sub">One line on what it means here</span></a>' for i in range(1, 5)) + "</div>",
        "Page tag": tags(h, [("Experience Engineering", "/services/experience-engineering/"), ("Financial services", "/sectors/financial-services/"), ("Customer Value", "/expertise/customer-value/")]),
        "Filter bar": '<div class="filters"><span class="group-label">Industry</span><button type="button" class="filter on">All industries</button><button type="button" class="filter">Financial services</button><button type="button" class="filter">Consumer</button><button type="button" class="filter">Media</button></div>',
        "Type filter tabs": '<div class="type-tabs"><button type="button" class="type-tab on">All</button><button type="button" class="type-tab">Reports</button><button type="button" class="type-tab">Articles</button><button type="button" class="type-tab">News and events</button></div>',
        "Role toggle": '<div class="filters"><button type="button" class="filter on">Open positions</button><button type="button" class="filter">All</button></div>',
        "Application steps": steps(["Application", "Interview with Partners", "Case study", "References", "Decision"]),
        "Situations list": situations([("We need to decide where and how to grow", "#"), ("I want a sounding board I trust", "#")]),
        "Row of text links": '<div class="row-links"><a href="#">Loyalty</a><a href="#">Pricing</a><a href="#">Customer Value</a></div>',
        "Link list": link_list([("The Pricing Paradox", "#", "Report"), ("Loyalty without the discount", "#", "Article")]),
        "Case line": '<p class="prose case-line" style="margin:0">Key Group, one-line result. <a href="#">Read the case study</a></p>',
        "Link line": '<p class="prose" style="margin:0">We apply these services to the growth problems we know best. <a href="#">Our expertise</a></p>',
        "Pagination": '<div class="pagination" aria-label="Pagination"><span class="on">1</span><a href="#">2</a><a href="#">3</a><a href="#">Next</a></div>',
        "Empty state": '<div class="empty-state"><p>No case studies match these filters.</p><a class="btn" href="#">Clear filters</a></div>',
        "Logo strip": logos(6),
        "Logo band": logo_band(8),
        "Quote": quote('"The work changed how we think about growth."', "Name, role, Dayinsure (to be confirmed)"),
        "Sticky stat rail": '<div style="max-width:320px">' + stat_rail(h, [("Stat TBC", "Outcome measure"), ("Stat TBC", "Outcome measure")], "Got a growth challenge like this one?") + "</div>",
        "Video 16:9": video("Showreel", "Caption naming the film, where one exists"),
        "Testimony video": video("Client testimony film", "Name, role, client (to be confirmed)"),
        "Profile pop-up": '<div class="cards" style="max-width:320px">' + person_card(h, "Expert name", "Role, one line") + '</div><p class="unit-purpose" style="margin-top:12px">Quick view opens an accessible dialog (native focus trap, Escape and backdrop close, focus returns to the opener). The full profile stays a plain link.</p>',
        "CIVD four-cell": civd(),
        "Article body": '<div class="prose article-body"><p>Opening argument. Two or three sentences that set the problem.</p><p>The view we take, and why the usual response fails.</p></div>',
        "Form": ('<div class="form"><form>'
                 + form_field("Name") + form_field("Company")
                 + form_field("Work email", "email")
                 + form_field("Topic", "select")
                 + form_field("Message", "textarea")
                 + '<button type="button" class="btn">Send</button></form></div>'
                 + '<div class="field is-error" style="margin-top:24px;max-width:560px"><label for="f-err">Email capture, error state</label><input id="f-err" type="email"><span class="field-msg">Enter a valid email.</span></div>'),
    }

    missing = [n for n in w.COMPONENTS if n not in samples]
    if missing:
        raise SystemExit(f"Branded catalogue has no sample for: {missing}")

    DARK = {"Mega-nav hub and strands", "Header Contact"}
    groups_html = ""
    for group in w.COMPONENT_GROUPS:
        units = "".join(unit(n, samples[n], dark=(n in DARK)) for n, (g, _, _) in w.COMPONENTS.items() if g == group)
        groups_html += section(sec_head(group, eyebrow="Components") + units)

    return hero + palette + type_scale + layout + buttons + groups_html + closing_band(h)


# ---------------------------------------------------------------------------
# Stub pages for everything not yet skinned
# ---------------------------------------------------------------------------

def stub_body(page) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    wires = wires_href(url)
    lead = esc(page.get("hero") or page.get("intent") or "")
    return f"""
    <section class="hero hero-light">
      <div class="wrap">
        <span class="eyebrow">{esc(w.KIND_LABELS[page["kind"]])}</span>
        <h1>{esc(page["h1"])}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <div class="stub-note prose">
          <h3 style="margin-top:0">Not yet skinned in this preview</h3>
          <p>This page exists so no link breaks, but only the key templates are branded. The structure and content for this page are defined in the greyscale wireframe, which remains the IA source of truth.</p>
          <p><a href="{wires}">Open the wireframe for this page</a> &middot; <a href="{h("/")}">Branded home</a> &middot; <a href="{h("/catalogue/")}">Branded component library</a></p>
        </div>
      </div>
    </section>
    {closing_band(h)}"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

BODY_BUILDERS = {
    "home": home_body,
    "hub": hub_body,
    "service": service_body,
    "work-hub": work_hub_body,
    "case": case_body,
    "insights-hub": insights_hub_body,
    "insight": insight_body,
    "report": report_body,
    "careers": careers_body,
    "catalogue": catalogue_body,
}

# "Value Orchestration" is renamed by WORKING_NAMES; seeing it in output means
# the override missed a spot. The em dash is banned by the content rules.
BANNED = ["Value Orchestration", "\u2014"]


def build() -> None:
    written = 0
    for page in w.PAGES:
        url = output_url(page["url"])
        dest = BRANDED / "index.html" if url == "/" else BRANDED / url.strip("/") / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if page["url"] in KEY_URLS:
            body = BODY_BUILDERS[page["kind"]](page)
        else:
            body = stub_body(page)
        html = apply_working_names(wrap_page(page, body))
        for b in BANNED:
            if b in html:
                raise SystemExit(f"Banned wording {b!r} in {url}")
        dest.write_text(html, encoding="utf-8")
        written += 1
    print(f"wrote {written} branded pages ({len(KEY_URLS)} full templates, {written - len(KEY_URLS)} stubs)")


if __name__ == "__main__":
    build()
