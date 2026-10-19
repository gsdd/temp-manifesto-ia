#!/usr/bin/env python3
"""Generate the clickable full-site IA wireframe and docs/heading-map.md.

Single source of heading maps, page notes and page shells so the HTML and the
markdown map cannot drift. Run from repo root: python3 mocks/_build.py
"""
from __future__ import annotations

import os
from html import escape as esc
from html.parser import HTMLParser
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


def slugify(label: str) -> str:
    out = "".join(c if c.isalnum() else "-" for c in label.lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


# The interim growth team service's name has one source. Andy Bacon (19 Oct):
# naming still being finalised; Growth Office for now. To swap later, change
# GO_NAME, set GO_ALIAS_URL to the outgoing URL, and rebuild: pages, nav,
# links, catalogue, sitemap, heading map and the _redirects alias all follow.
GO_NAME = "Growth Office"
GO_URL = "/services/" + slugify(GO_NAME) + "/"
GO_ALIAS_URL = "/services/value-orchestration/"


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


# ---------------------------------------------------------------------------
# Component vocabulary. One name and one shape per reusable block. Pages mark
# each block with data-module="<name>"; the sidebar inventory and the component
# library at /catalogue/ are both generated from these names, so they cannot
# drift. Kinds are the interaction types a designer has to tell apart.
# ---------------------------------------------------------------------------

COMPONENTS: dict[str, tuple[str, str, str]] = {
    # name: (group, kind, purpose)
    "Header Contact": ("Chrome", "Button", "Primary enquire in the bar. Other nav items stay text links."),
    "Mega-nav hub and strands": ("Chrome", "Text link", "Triangle laid flat. Hub title with chevron, strand, keyword subtitle. Not cards."),
    "Breadcrumb": ("Chrome", "Text link", "Ancestors link. Current page is text. Every page except Home."),
    "Cookie bar": ("Chrome", "Button", "Accept dismisses. Cookie policy is the text link, not the button."),
    "Hero": ("Heroes and bands", "Band", "First block. H1, one support line, optional eyebrow, also-known-as, who-for and metric boxes. Composes a CTA pair and, where a film exists, a Video 16:9. Service and case heroes carry an image placeholder (client layout)."),
    "CTA pair": ("Heroes and bands", "Button", "Primary Button plus secondary Text link. Header Contact is the same Button."),
    "Closing CTA band": ("Heroes and bands", "Band", "Last enquire on the page. One line, a Button and a Text link. Careers uses Work for us."),
    "Prose": ("Heroes and bands", "Static", "Heading plus one to four short paragraphs. Body copy, not a card and not a box."),
    "Metric box": ("Heroes and bands", "Static", "A number the deck already gives. Not a card. Not clickable."),
    "Offer card": ("Cards", "Card", "Buyable service. Grey fill, no image. Whole card goes to the service page."),
    "Theme card": ("Cards", "Card", "Expertise problem. Outline only, no fill. Expertise hub only. Not a nav item."),
    "Case card": ("Cards", "Card", "Proof. Image placeholder, client, one-line result. Whole card goes to the case."),
    "Report card": ("Cards", "Card", "Long-form thinking. Portrait Report placeholder."),
    "Article card": ("Cards", "Card", "Short thinking. No grey fill, no image. Not the Offer card shape."),
    "Person card": ("Cards", "Card", "Someone. Avatar, name, one line."),
    "Role card": ("Cards", "Card", "Open role. Outline with a top rule: location, type, hiring state."),
    "Triangle tile": ("Cards", "Card", "Pillar, not a service. Three tiles plus the triangle line. Links to the pillar page or an in-page anchor. Not an Offer card."),
    "Thought leadership card": ("Cards", "Card", "The one listing card for thinking and case studies (client layout). Rounded frame, image on top, one primary service tag pill, title, short excerpt, a row of small uppercase secondary tags (industry or expertise), Read more link. On Our thinking the tags also drive the live tag filter."),
    "Related trio": ("Cards", "Card", "Three related items in one row at the foot of an article: one article, one service, one report (client layout)."),
    "Culture card": ("Cards", "Card", "Values and culture on Careers (client layout). Four outline cards, one value each, linking to Values and culture."),
    "Page tag": ("Lists and locators", "Tag", "One dimension, max three, except case study heroes, which show service, industry and expertise pills so cross-linking survives (client layout). Small linked label. Not a filter."),
    "Filter bar": ("Lists and locators", "Filter", "Toggle a listing. Pill-shaped buttons, not links. More filters is also a Filter. On Our work the two groups are Industry and Service (client layout)."),
    "Type filter tabs": ("Lists and locators", "Filter", "Listing tabs on Our thinking, in the order All, Reports, Articles, News and events (client layout). The tabs filter the grid in place and each state is a deep-linkable URL; the grid always links every item, so nothing is hidden from search."),
    "Role toggle": ("Lists and locators", "Filter", "Open positions / All on the Careers roles list (client layout). Defaults to Open positions."),
    "Application steps": ("Lists and locators", "Static", "The five hiring steps on Careers (client layout): Application, Interview with Partners, Case study, References, Decision."),
    "Situations list": ("Lists and locators", "Text link", "Prospect language in. Links on the services hub. On a service page the three lines are static text."),
    "Row of text links": ("Lists and locators", "Text link", "Names only, in one row. Home Growth problems we know best. Not cards, not tags."),
    "Link list": ("Lists and locators", "Text link", "Compact list of links: related thinking, which of the six, engagement shapes, search hits. Title left, type right."),
    "Case line": ("Lists and locators", "Text link", "One proof under a pillar. Client, one-line result, Read the case study. Not a Case card."),
    "Link line": ("Lists and locators", "Text link", "One sentence that ends in a text link. Routes without a card."),
    "Pagination": ("Lists and locators", "Text link", "Current page is text. Others are page links. Not buttons."),
    "Empty state": ("Lists and locators", "Static", "No results for this filter or query. Hide when results exist. Clear filters is a Button."),
    "Logo strip": ("Proof and media", "Static", "Trusted partners, awards, or sector clients. Link a logo only if a case exists."),
    "Logo band": ("Proof and media", "Static", "Auto-scrolling client logo band on Our work (client layout). Constant speed, pauses on hover and under reduced motion. Link a logo only if a case exists."),
    "Quote": ("Proof and media", "Static", "Testimonial, attributed with name and role. Lives with work. Not a testimonials page."),
    "Sticky stat rail": ("Proof and media", "Static", "Case study rail (client layout): two Metric boxes and a Contact us Button, pinned on the left while the story scrolls."),
    "Video 16:9": ("Proof and media", "Static", "Showreel, partner film, or case film. Two states: existing asset (solid frame, caption naming the film; the Home showreel / client video) or placeholder (dashed) until a film exists."),
    "Testimony video": ("Proof and media", "Static", "Attributed client testimony as a film on Our work (client layout). 16:9 placeholder with the speaker named beneath."),
    "Profile pop-up": ("Proof and media", "Static", "Overlay profile opened from an expert's Person card (client layout): biography, focus and a link to the full profile page, whose URL keeps working for search."),
    "CIVD four-cell": ("Proof and media", "Static", "Growth Strategy frame. Dashed cells. The text link sits beside it, not on the cells."),
    "Article body": ("Proof and media", "Static", "Long-form paragraphs on a report or article."),
    "Form": ("Forms", "Button", "Stacked fields with labels. Submit is a Button. Variants: Work with us, Work for us, email capture, search, report copy."),
}

COMPONENT_GROUPS = ["Chrome", "Heroes and bands", "Cards", "Lists and locators", "Proof and media", "Forms"]
CHROME_LINE = "Header Contact, Mega-nav hub and strands, Breadcrumb, Cookie bar and the footer are on every page."

WEIGHT_GLOSS = {
    "Canonical": "owns its topic; other pages on the topic link here",
    "Supporting": "supports a canonical page and links up to it",
    "Light": "short landing; proof lives elsewhere",
    "Utility": "functional page; not a search destination",
}

KIND_LABELS = {
    "home": "Home",
    "hub": "Services hub",
    "service": "Service detail",
    "activation": "Activation group",
    "ceo": "CEO Advisory",
    "expertise-hub": "Expertise hub",
    "theme": "Expertise theme",
    "sector": "Sector landing",
    "work-hub": "Work hub",
    "case": "Case study",
    "insights-hub": "Thinking hub",
    "insight": "Article",
    "report": "Report",
    "about": "About",
    "team": "People listing",
    "profile": "Profile",
    "how": "Our approach",
    "values": "Values and culture",
    "careers": "Careers",
    "role": "Role",
    "contact": "Contact",
    "thanks": "Confirmation",
    "legal": "Utility page",
    "notfound": "Not found",
    "catalogue": "Component library",
}


def mod(name: str) -> str:
    """Attribute pair that names a reusable component on the canvas."""
    if name not in COMPONENTS:
        raise SystemExit(f"Unknown component: {name}")
    return f'data-module="{esc(name)}" title="{esc(name)}"'


class _CanvasScan(HTMLParser):
    """Walk a page body and list the components in each top-level block."""

    def __init__(self) -> None:
        super().__init__()
        self.blocks: list[dict] = []
        self.depth = 0
        self.cur: dict | None = None
        self.cur_depth = 0
        self.h2_buf: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.cur is None:
            self.cur = dict(module=None, items=[], h2s=[], h3s=[])
            self.cur_depth = self.depth
            self.blocks.append(self.cur)
            self.cur["module"] = a.get("data-module")
        elif a.get("data-module"):
            self.cur["items"].append(a["data-module"])
        if tag in ("h2", "h3"):
            self.h2_buf = []
        if tag not in VOID_TAGS:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        self.depth -= 1
        if tag in ("h2", "h3") and self.h2_buf is not None and self.cur is not None:
            self.cur[tag + "s"].append(" ".join("".join(self.h2_buf).split()))
            self.h2_buf = None
        if self.cur is not None and self.depth == self.cur_depth:
            self.cur = None

    def handle_data(self, data):
        if self.h2_buf is not None:
            self.h2_buf.append(data)


VOID_TAGS = {"br", "hr", "img", "input", "meta", "link"}


def _collapse(names: list[str]) -> list[str]:
    out: list[tuple[str, int]] = []
    for n in names:
        if out and out[-1][0] == n:
            out[-1] = (n, out[-1][1] + 1)
        else:
            out.append((n, 1))
    return [f"{n} \u00d7{c}" if c > 1 else n for n, c in out]


def component_inventory(body: str) -> list[tuple[str, str]]:
    """(components, block context) per top-level block, in canvas order."""
    scan = _CanvasScan()
    scan.feed(body)
    scan.close()
    rows: list[tuple[str, str]] = []
    for b in scan.blocks:
        names = ([b["module"]] if b["module"] else []) + b["items"]
        if not names:
            names = ["Prose"]
        unknown = [n for n in names if n not in COMPONENTS]
        if unknown:
            raise SystemExit(f"Unknown component(s) on canvas: {unknown}")
        context = " / ".join(b["h2s"] or b["h3s"])
        rows.append((", ".join(_collapse(names)), context))
    return rows


def sidebar_html(page: dict, body: str) -> str:
    e = esc
    url = page["url"]
    sitemap = os.path.relpath("sitemap.html", file_dir(url))
    catalogue = os.path.relpath("catalogue/index.html", file_dir(url))

    def links(items):
        return ", ".join(f'<a href="{rel_href(url, u)}">{e(n)}</a>' for n, u in items)

    primary = page.get("primary") or "none"
    alts = page.get("alts") or []
    kw = f"<p>Primary: {e(primary)}</p>"
    if alts:
        kw += "<ul>" + "".join(f"<li>{e(a)}</li>" for a in alts) + "</ul>"

    rows = [
        f'<p class="k"><strong>URL</strong><code>{e(url)}</code></p>',
        f'<p class="k"><strong>Template</strong>{e(KIND_LABELS[page["kind"]])}. '
        f'{e(page["weight"])}: {e(WEIGHT_GLOSS[page["weight"]])}.</p>',
        f'<p class="k"><strong>H1</strong>{e(page["h1"])}</p>',
        f'<div class="k"><strong>Keywords</strong>{kw}</div>',
    ]
    if page.get("quiet"):
        rows.append(f'<p class="k"><strong>Menu subtitle</strong>{e(page["quiet"])}</p>')
    h2s = page.get("h2s") or []
    h2_html = "<ol>" + "".join(f"<li>{e(x)}</li>" for x in h2s) + "</ol>" if h2s else "<p>None. H1 only.</p>"
    rows.append(f'<div class="k"><strong>H2s (ordered)</strong>{h2_html}</div>')
    h3s = page.get("h3s") or []
    if h3s:
        rows.append('<div class="k"><strong>H3s</strong><ul>' + "".join(f"<li>{e(x)}</li>" for x in h3s) + "</ul></div>")
    rows.append(f'<p class="k"><strong>Intent</strong>{e(page["intent"])}</p>')
    notes = page.get("notes") or []
    if notes:
        rows.append('<div class="k"><strong>Content notes</strong><ul>' + "".join(f"<li>{e(n)}</li>" for n in notes) + "</ul></div>")
    mural = page.get("mural") or []
    if mural:
        rows.append(
            '<div class="k"><strong>Client layout (Mural, 15 Oct)</strong><div class="cmods">'
            + "".join(f"<span>{e(m)}</span>" for m in mural)
            + "</div></div>"
        )
    rel = []
    for label, items in (("Expertise", page.get("themes")), ("Sectors", page.get("sectors")), ("Services", page.get("services"))):
        if items:
            rel.append(f"{label}: {links(items)}")
    if rel:
        rows.append('<p class="k"><strong>Links to</strong>' + " · ".join(rel) + "</p>")

    inv = page["_components"] = component_inventory(body)
    comp_rows = "".join(
        f'<li><span class="mods">{e(names)}</span>'
        + (f'<span class="blk">{e(ctx)}</span>' if ctx else "")
        + "</li>"
        for names, ctx in inv
    )
    return f"""
  <aside class="sidebar" aria-label="Page fundamentals and components">
    <section class="panel">
      <h2>Page fundamentals</h2>
      <p class="map-note"><a href="{sitemap}">All pages</a> · <a href="{catalogue}">Component library</a></p>
      {"".join(rows)}
    </section>
    <section class="panel">
      <h2>Components on this page</h2>
      <p class="map-note">In canvas order. Block heading on the right where the block has one.</p>
      <ol class="comp">{comp_rows}</ol>
      <p class="map-note">{e(CHROME_LINE)} Names match the <a href="{catalogue}">component library</a>.</p>
    </section>
  </aside>"""


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
            <li data-menu="thinking">
              <a class="top-link" href="{h("/insights/")}" aria-haspopup="true" aria-expanded="false"{current("insights")}>Our thinking <span class="caret">&#9660;</span></a>
              <div class="dropdown" role="region" aria-label="Our thinking menu">
                <ul>
                  <li><a href="{h("/insights/")}">All thinking</a></li>
                  <li><a href="{h("/insights/#reports")}">Reports</a></li>
                  <li><a href="{h("/insights/#articles")}">Articles</a></li>
                  <li><a href="{h("/insights/#news-events")}">News and events</a></li>
                </ul>
              </div>
            </li>
            <li data-menu="about">
              <a class="top-link" href="{h("/about/")}" aria-haspopup="true" aria-expanded="false"{current("about")}>About <span class="caret">&#9660;</span></a>
              <div class="dropdown" role="region" aria-label="About menu">
                <ul>
                  <li><a href="{h("/about/team/")}">Our people</a></li>
                  <li><a href="{h("/about/how-we-work/")}">Our approach</a></li>
                  <li><a href="{h("/about/values/")}">Values and culture</a></li>
                </ul>
              </div>
            </li>
            <li><a class="top-link plain" href="{h("/careers/")}"{current("careers")}>Careers</a></li>
          </ul>
          <a class="btn" href="{h("/contact/")}"{current("contact")}>Contact</a>
        </header>
        <div class="mega" id="megaNav" role="region" aria-label="What we do menu">
          <div class="mega-inner">
            <div class="mega-cols">
              <div class="pillar">
                <h3><a class="pillar-hub" href="{h("/services/growth-strategy/")}">Growth Strategy <span class="hub-chevron" aria-hidden="true">&#8594;</span></a></h3>
                <p class="line">Where and how you grow</p>
                <ul>
                  <li><a class="strand-overview" href="{h("/services/growth-strategy/")}">Overview<small>Where to grow and how to win</small></a></li>
                  <li><a href="{h("/services/proposition-innovation/")}">Proposition Innovation<small>Value proposition design</small></a></li>
                </ul>
              </div>
              <div class="pillar">
                <h3><a class="pillar-hub" href="{h("/services/activation/")}">Activation Services <span class="hub-chevron" aria-hidden="true">&#8594;</span></a></h3>
                <p class="line">Turning strategy into results</p>
                <ul>
                  <li><a class="strand-overview" href="{h("/services/activation/")}">Overview<small>Hands-on delivery, six services</small></a></li>
                  <li><a href="{h("/services/customer-research/")}">Customer Research and Insight<small>Research methods and journey mapping</small></a></li>
                  <li><a href="{h("/services/experience-engineering/")}">Experience Engineering<small>Customer experience and websites</small></a></li>
                  <li><a href="{h("/services/ai-agents-for-marketing/")}">AI Agents for Marketing<small>AI marketing agents, guided by experts</small></a></li>
                  <li><a href="{h("/services/operating-model-design/")}">Operating Model Design<small>Target operating model</small></a></li>
                  <li><a href="{h(GO_URL)}">{GO_NAME}<small>Interim growth team</small></a></li>
                  <li><a href="{h("/services/ai-enablement/")}">AI Enablement<small>AI skills and adoption</small></a></li>
                </ul>
              </div>
              <div class="pillar">
                <h3><a class="pillar-hub" href="{h("/services/ceo-advisory/")}">CEO Advisory <span class="hub-chevron" aria-hidden="true">&#8594;</span></a></h3>
                <p class="line">One-to-one support for leaders</p>
                <ul>
                  <li><a href="{h("/services/ceo-advisory/#side-by-side")}">Side-by-Side<small>One-to-one advisory retainer</small></a></li>
                  <li><a href="{h("/services/ceo-advisory/#advisors")}">Our advisors<small>Experienced growth leaders</small></a></li>
                </ul>
              </div>
            </div>
            <div class="mega-row">
              <a href="{h("/services/")}">All services</a>
              <a href="{h("/expertise/")}">Expertise</a>
              <a href="{h("/work/")}">Our work</a>
            </div>
          </div>
        </div>
      </div>
"""


def footer_html(from_url: str) -> str:
    h = lambda u: rel_href(from_url, u)
    return f"""
      <div class="cookie-bar">
        <span>We use cookies to run this site. <a href="{h("/cookie-policy/")}">Cookie policy</a></span>
        <a class="btn" href="{h("/cookie-policy/")}">Accept</a>
      </div>
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
              <li><a href="{h(GO_URL)}">{GO_NAME}</a></li>
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
              <li><a href="{h("/sectors/energy/")}">Energy</a></li>
            </ul>
          </div>
          <div>
            <h4>Company</h4>
            <ul>
              <li><a href="{h("/about/")}">About</a></li>
              <li><a href="{h("/about/team/")}">Our people</a></li>
              <li><a href="{h("/about/how-we-work/")}">Our approach</a></li>
              <li><a href="{h("/about/values/")}">Values and culture</a></li>
              <li><a href="{h("/careers/")}">Careers</a></li>
              <li><a href="{h("/work/")}">Our work</a></li>
              <li><a href="{h("/insights/")}">Our thinking</a></li>
              <li><a href="{h("/newsletter/")}">The Nutshell</a></li>
              <li><a href="{h("/contact/")}">Contact</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <span>Company registration line</span>
          <form class="footer-search" action="{h("/search/")}" method="get">
            <label for="footer-q">Search</label>
            <span class="box" aria-hidden="true"></span>
            <a href="{h("/search/")}">Go</a>
          </form>
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
    css = asset(url, "wireframe.css")
    js = asset(url, "nav.js")
    filter_js = f'\n<script src="{asset(url, "filter.js")}"></script>' if page.get("kind") == "insights-hub" else ""
    solo = page.get("kind") == "catalogue" or page.get("no_sidebar")
    layout_cls = "layout layout-solo" if solo else "layout"
    sidebar = "" if solo else sidebar_html(page, body)
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Manifesto Growth Architects</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="{layout_cls}">
  <div class="browser" id="browser" data-mega-open="false">
    <div class="scrim"></div>
    {header_html(url, section)}
    {crumbs_html(url, page.get("crumbs") or [])}
    <main class="page" id="main">
      {body}
    </main>
    {footer_html(url)}
  </div>
  {sidebar}
</div>
<script src="{js}"></script>{filter_js}
</body>
</html>
"""


CARD_KINDS = {
    # extra: (class, inner placeholder, component name)
    "offer": ("card offer", "", "Offer card"),
    "theme": ("card theme", "", "Theme card"),
    "role": ("card role", "", "Role card"),
    "article": ("card article", "", "Article card"),
    "person": ("card person", '<div class="avatar"></div>', "Person card"),
    "ph": ("card", '<div class="ph">Image</div>', "Case card"),
    "doc": ("card", '<div class="doc">Report</div>', "Report card"),
}


def card(h, href, title, sub, extra="offer"):
    cls, inner, name = CARD_KINDS[extra]
    return f'<a class="{cls}" {mod(name)} href="{h(href)}">{inner}<strong>{title}</strong><span>{sub}</span></a>'


def tags_html(h, items):
    inner = "".join(f'<a href="{h(u)}" {mod("Page tag")}>{n}</a>' for n, u in items)
    return f'<div class="page-tags">{inner}</div>'


def filter_bar(items, on=None, more=False, data_attr=None):
    """With data_attr set (for example "data-tag"), each pill carries that
    attribute with the slug of its label, for client-side filtering."""
    bits = []
    for label in items:
        cls = "filter on" if label == on else "filter"
        da = f' {data_attr}="{slugify(label)}"' if data_attr else ""
        bits.append(f'<button type="button" class="{cls}"{da}>{label}</button>')
    if more:
        bits.append('<button type="button" class="filter more">More filters</button>')
    return f'<div class="filters" {mod("Filter bar")}>{"".join(bits)}</div>'


def tl_card(h, href, title, excerpt, primary, secondary=(), type_label=None, type_slug=None):
    """Thought leadership card (client layout): image, primary tag pill, title,
    excerpt, small uppercase secondary tags, Read more. Type shown where given.
    With type_slug set, the card carries data attributes for client-side filtering."""
    pill = f'<span class="tl-pill">{esc(primary)}</span>'
    kind = f'<span class="tl-type">{esc(type_label)}</span>' if type_label else ""
    tags = ""
    if secondary:
        tags = '<span class="tl-tags">' + "".join(f"<em>{esc(t)}</em>" for t in secondary) + "</span>"
    data = ""
    if type_slug:
        tag_slugs = " ".join(slugify(t) for t in (primary, *secondary))
        data = f' data-type="{type_slug}" data-tags="{tag_slugs}"'
    return (
        f'<a class="card tl" {mod("Thought leadership card")}{data} href="{h(href)}">'
        f'<div class="ph">Image</div><span class="tl-head">{pill}{kind}</span>'
        f'<strong>{title}</strong><span class="tl-excerpt">{excerpt}</span>'
        f'{tags}<span class="tl-more">Read more &#8594;</span></a>'
    )


def logo_band_html(n=10, label="Logo"):
    cells = "".join(f'<span class="logo-ph">{label}</span>' for _ in range(n))
    return (
        f'<div class="logo-band" {mod("Logo band")} aria-label="Client logos">'
        f'<span class="wf-label">Auto-scrolling, constant speed. Pauses on hover and under reduced motion</span>'
        f'<div class="band-track">{cells}</div></div>'
    )


def stat_rail_html(h, stats, cta_label="Contact us", cta_line=None):
    boxes = "".join(
        f'<div class="metric" {mod("Metric box")}><strong>{v}</strong><span>{l}</span></div>' for v, l in stats
    )
    line = f'<p class="rail-line">{cta_line}</p>' if cta_line else ""
    return (
        f'<aside class="stat-rail" {mod("Sticky stat rail")}>'
        f'<span class="wf-label">Static block, pinned while the story scrolls</span>'
        f'{boxes}{line}<a class="btn" href="{h("/contact/")}">{cta_label}</a></aside>'
    )


def testimony_video_html(label="Client testimony film", speaker="Name, role, client (to be confirmed)"):
    return (
        f'<figure class="video-ph testimony" {mod("Testimony video")} aria-label="{label}">'
        f'<span>{label}</span><figcaption>{speaker}</figcaption></figure>'
    )


def steps_html(items):
    inner = "".join(f"<li><span>{esc(s)}</span></li>" for s in items)
    return f'<ol class="steps" {mod("Application steps")}>{inner}</ol>'


def role_toggle_html(on="Open positions"):
    bits = []
    for label in ("Open positions", "All"):
        cls = "filter on" if label == on else "filter"
        bits.append(f'<button type="button" class="{cls}">{label}</button>')
    return f'<div class="filters role-toggle" {mod("Role toggle")}>{"".join(bits)}<span class="wf-label">Defaults to Open positions</span></div>'


def type_tabs_html(items, on="All"):
    bits = []
    for label, anchor in items:
        cls = "type-tab on" if label == on else "type-tab"
        aid = f' id="{anchor}"' if anchor else ""
        dt = f' data-type="{anchor or slugify(label)}"'
        bits.append(f'<button type="button" class="{cls}"{aid}{dt}>{label}</button>')
    return f'<div class="type-tabs" {mod("Type filter tabs")}>{"".join(bits)}</div>'


def popup_html(h, name="Expert name", focus="Focus, one line"):
    return (
        f'<div class="popup-sample" {mod("Profile pop-up")}>'
        f'<span class="wf-label">Pop-up: opens over the page from the Person card. Escape or close to dismiss</span>'
        f'<div class="popup-frame"><div class="avatar"></div><strong>{name}</strong>'
        f'<p>{focus}. Short biography, two or three lines.</p>'
        f'<a href="{h("/about/team/advisor-one/")}">Full profile</a></div></div>'
    )


def related_trio_html(h, article, service, report):
    inner = (
        card(h, article[1], article[0], "Article", "article")
        + card(h, service[1], service[0], "Service", "offer")
        + card(h, report[1], report[0], "Report", "doc")
    )
    return f'<div class="cards trio" {mod("Related trio")}>{inner}</div>'


def pagination_html(pages=("1", "2", "3"), next_label="Next"):
    bits = []
    for i, p in enumerate(pages):
        if i == 0:
            bits.append(f'<span class="on">{p}</span>')
        else:
            bits.append(f'<a href="#">{p}</a>')
    bits.append(f'<a href="#">{next_label}</a>')
    return f'<div class="pagination" {mod("Pagination")} aria-label="Pagination">{"".join(bits)}</div>'


def empty_html(message, btn_href, btn_label="Clear filters"):
    return f"""
          <div class="empty-state" {mod("Empty state")}>
            <p>{message}</p>
            <a class="btn" href="{btn_href}">{btn_label}</a>
          </div>"""


def empty_stub(message, btn_href, btn_label="Clear filters", annotate=False, filter_hook=False):
    note = ann("Static + button") if annotate else ""
    hook = " data-filter-empty" if filter_hook else ""
    label = (
        "Appears when the live filters return no results; Clear filters resets them"
        if filter_hook
        else "Conditional: shown only when there are no results"
    )
    return f"""
        <section class="block"{hook}>
          <span class="wf-label">{label}</span>{note}
          {empty_html(message, btn_href, btn_label)}
        </section>
"""


def form_html(fields, submit, href, extra=""):
    rows = "".join(
        f'<div class="field"><label>{label}</label><div class="box{(" " + box) if box else ""}">{text}</div></div>'
        for label, box, text in fields
    )
    return f"""
          <div class="form" {mod("Form")}>
            {rows}{extra}
            <a class="btn" href="{href}">{submit}</a>
          </div>"""


def ann(label: str) -> str:
    """Wireframe annotation: the interaction type or component name, set as a tiny
    caps label outside the block. Convention for reading the mock, not shipping UI.
    Must sit inside a block so the sidebar inventory does not count it as Prose."""
    return f'<span class="wf-type" aria-hidden="true">{esc(label)}</span>'


def unit(name, sample):
    group, kind, purpose = COMPONENTS[name]
    slug = kind.lower().replace(" ", "-")
    return f"""
          <div class="catalogue-item" id="{name.lower().replace(' ', '-').replace(':', '')}">
            <div class="unit-head">
              <span class="cat-label">{esc(name)}</span>
              <span class="unit-kind unit-{slug}">{kind}</span>
            </div>
            <p class="unit-purpose">{esc(purpose)}</p>
            {sample}
          </div>"""


def logos_html(n=8, label="Logo"):
    cells = "".join(f'<span class="logo-ph">{label}</span>' for _ in range(n))
    return f'<div class="logos" {mod("Logo strip")} aria-label="{label}s">{cells}</div>'


def video_html(label="Video", asset: str | None = None):
    """A 16:9 video block. With `asset`, the film already exists: solid frame, play glyph,
    and a caption naming the asset. Without it, a dashed placeholder for a film to come."""
    if asset:
        return (
            f'<figure class="video-ph asset" {mod("Video 16:9")} aria-label="{label}">'
            f'<span class="play" aria-hidden="true">&#9654;</span><span>{label}</span>'
            f'<figcaption>{asset}</figcaption></figure>'
        )
    return f'<div class="video-ph" {mod("Video 16:9")} aria-label="{label}"><span>{label}</span></div>'


def metrics_html(pairs):
    inner = "".join(
        f'<div class="metric" {mod("Metric box")}><strong>{v}</strong><span>{l}</span></div>' for v, l in pairs
    )
    return f'<div class="metrics">{inner}</div>'


def quote_html(text='"The work changed how we think about growth."', cite="Client"):
    return f'<blockquote class="quote" {mod("Quote")}>{text}<cite>{cite}</cite></blockquote>'


def cta_html(h, primary=("Contact", "/contact/"), secondary=("See our work", "/work/"), extra=""):
    sec = f'<a class="text" href="{h(secondary[1])}">{secondary[0]}</a>' if secondary else ""
    return f'<div class="cta" {mod("CTA pair")}><a class="btn" href="{h(primary[1])}">{primary[0]}</a>{sec}{extra}</div>'


def hero_open(cls=""):
    return f'<section class="block hero{(" " + cls) if cls else ""}" {mod("Hero")}>'


def article_body():
    return f"""
        <div class="article-body" {mod("Article body")}>
          <p class="prose">Opening argument. Two or three sentences that set the problem.</p>
          <p class="prose">The view we take, and why the usual response fails.</p>
          <p class="prose">What we would do next, in brief, with a link to the relevant service.</p>
        </div>
"""


def closing(h, line="Tell us about your growth challenge", cta="Contact", dest="/contact/", secondary_label="See our work", secondary_url="/work/", annotate=False):
    note = ann("Band: button + text link") if annotate else ""
    return f"""
        <section class="block closing" {mod("Closing CTA band")}>
          {note}<p>{line}</p>
          <div class="cta">
            <a class="btn" href="{h(dest)}">{cta}</a>
            <a class="text" href="{h(secondary_url)}">{secondary_label}</a>
          </div>
        </section>
"""


def link_list(items):
    inner = "".join(f'<li><a href="{u}">{label}</a>{("<span>" + meta + "</span>") if meta else ""}</li>' for label, u, meta in items)
    return f'<ul class="list" {mod("Link list")}>{inner}</ul>'


def related_thinking(h):
    return f"""
        <section class="block">
          <h2 class="sec">Related thinking</h2>
          {link_list([("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report"), ("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article")])}
          <a class="more" href="{h("/insights/")}">All thinking</a>
        </section>
"""


def civd_html(compact=False):
    cls = "civd-grid compact" if compact else "civd-grid"
    cells = [
        ("Customer", "Who you grow with."),
        ("Innovation", "What you offer next."),
        ("Value", "Where the economics move."),
        ("Delivery", "Whether it can be executed."),
    ]
    inner = "".join(f'<div class="civd-cell"><strong>{n}</strong><span>{t}</span></div>' for n, t in cells)
    return f'<div class="{cls}" {mod("CIVD four-cell")} aria-label="Customer, Innovation, Value and Delivery">{inner}</div>'


def thinking_feature(h, annotate=False):
    note = ann("Report card + article card") if annotate else ""
    return f"""
        <section class="block">
          <h2 class="sec">Our thinking</h2>{note}
          <div class="thinking-split">
            {card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "Featured report. From tactical lever to growth engine", "doc")}
            <div class="thinking-side">
              {card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Article", "article")}
              <a class="more" href="{h("/insights/")}">All thinking</a>
            </div>
          </div>
        </section>
"""


def tri_html(h, tiles, line=""):
    inner = "".join(
        f'<a href="{h(u) if u.startswith("/") else u}" {mod("Triangle tile")}><strong>{n}</strong><span>{s}</span></a>'
        for n, u, s in tiles
    )
    return f'<div class="tri">{inner}</div>{line}'


PILLAR_TILES = [
    ("Growth Strategy", "/services/growth-strategy/", "Where and how you grow"),
    ("Activation Services", "/services/activation/", "Turning strategy into results"),
    ("CEO Advisory", "/services/ceo-advisory/", "One-to-one support for leaders"),
]


# ---------------------------------------------------------------------------
# Page registry: heading maps + page notes. Bodies are built in body_for().
# ---------------------------------------------------------------------------

T = lambda n, u: (n, u)

# Client modules used by the service-detail template (Mural, 15 Oct), shown in the sidebar.
SERVICE_MURAL = [
    "Hero: name, strapline, image",
    "Overview",
    "Why now?",
    "How can we help you?",
    "Why us?",
    "Our experts + profile pop-up",
    "Related case studies carousel",
    "Contact us band",
]

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
        h2s=["Trusted partners", "What we do", "Our thinking", "Our work", "Awards", "Growth problems we know best"],
        h3s=[],
        intent="Brand and router. Says who Manifesto is for, shows the Growth Architecture triangle once, and routes into services, thinking, work and expertise. Everything here exists in full on another page.",
        crumbs=[],
        kind="home",
        notes=[
            "The existing Manifesto showreel / client video is embedded in the hero (confirmed by Andy, 1 October). It is a live asset, not a placeholder for a future film",
            "Trusted partners sit directly under the hero",
            "Featured thinking (one report, one article) sits after the triangle and before Our work",
            "Client quote sits with the work cards",
            "Awards sit after Work",
            "No long copy, no tags on cards, no reports grid",
        ],
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
        intent="Names the Growth Architecture system and routes to every service. Two ways in: by capability (the triangle) and by problem (seven situations).",
        crumbs=[("Home", "/"), ("What we do", None)],
        kind="hub",
        notes=["Keyword targets for individual services stay on the service pages", "One case line per pillar; the CIVD frame is shown compact and links to its home on Growth Strategy"],
    ),
    dict(
        url="/services/growth-strategy/",
        title="Growth Strategy",
        section="services",
        weight="Canonical",
        primary="growth strategy (~480)",
        alts=["growth strategy consultancy / consultant (~70)", "brand strategy consulting (~390) where true to the offer", "go to market strategy (~880) where true to the offer"],
        quiet="Where to grow and how to win",
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/"), T("Pricing", "/expertise/pricing/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Proposition Innovation", "/services/proposition-innovation/"), T("Activation Services", "/services/activation/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Growth Strategy",
        h2s=["Overview", "Why now?", "How can we help you?", "Customer, Innovation, Value and Delivery", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["North Star", "Growth priorities", "Demand signals", "Scenario planning", "Customer", "Innovation", "Value", "Delivery"],
        intent="Lead offer. Owns growth strategy search. CIVD (Customer, Innovation, Value and Delivery) is the named frame and lives on this page. Client service template applied: every section is a visible H2 or H3, no accordion.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Growth Strategy", None)],
        kind="service",
        notes=["Brand and go-to-market language appears in H2s only where the work is truly that", "CIVD belongs to Growth Strategy, not to Side-by-Side", "Capability headings sit as H3s under How can we help you?; the CIVD frame keeps its anchored H2 home"],
        mural=SERVICE_MURAL,
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
        h2s=["Overview", "Why now?", "How can we help you?", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["Value proposition design", "Loyalty propositions", "Membership propositions", "Subscription propositions", "Direct-to-consumer propositions"],
        intent="Manifesto label in the H1; value proposition design in the menu subtitle, hero and headings so search can see it. Each proposition type hands off to its expertise theme. Client service template applied: every section visible, no accordion.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Proposition Innovation", None)],
        kind="service",
        mural=SERVICE_MURAL,
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
        alts=["customer journey mapping (~2,900) in the Experience Engineering line", "operating model (~880) in the Operating Model Design line", f"interim CMO / interim growth team (~110 to 140) in the {GO_NAME} line"],
        quiet="Hands-on delivery, six services",
        themes=[],
        sectors=[],
        services=[
            T("Customer Research and Insight", "/services/customer-research/"),
            T("Experience Engineering", "/services/experience-engineering/"),
            T("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
            T("Operating Model Design", "/services/operating-model-design/"),
            T(GO_NAME, GO_URL),
            T("AI Enablement", "/services/ai-enablement/"),
        ],
        h1="Activation Services",
        h2s=["The bridge from strategy to results", "Which of the six do you need?", "The six Activation services"],
        h3s=[],
        intent="Explains Activation and routes to the six services. Catches problem-minded searchers in the six lines (journey mapping, operating model, interim leadership) without owning those terms.",
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
        quiet="Research methods and journey mapping",
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Experience Engineering", "/services/experience-engineering/"), T("Proposition Innovation", "/services/proposition-innovation/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/")],
        h1="Customer Research and Insight",
        h2s=["Overview", "Why now?", "How can we help you?", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["Customer research methods", "Customer journey mapping", "Research projects", "Always-on customer insight"],
        intent="Leads with research methods, journey mapping and insight outcomes, not only the consultancy noun. Customer Intelligence is the practice name on the page. Qualitative and quantitative evidence lives here. Client service template applied.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Customer Research and Insight", None)],
        kind="service",
        notes=["Analytical journey mapping lives here; design research lives on Experience Engineering", "The six method names (digital listening, qualitative, quantitative, data analytics, internal knowledge, external market data) are a list under Research projects"],
        mural=SERVICE_MURAL,
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
        h2s=["Overview", "Why now?", "How can we help you?", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["Find", "Redesign", "Test", "Scale", "Customer experience (CX) design", "Website and digital product", "User research and testing"],
        intent="Manifesto label in the H1; the menu subtitle and headings carry the CX, website and journey-mapping search terms (Dayinsure and Key Group are the proof). Find, Redesign, Test, Scale is the How it works sequence. Client service template applied.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Experience Engineering", None)],
        kind="service",
        mural=SERVICE_MURAL,
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
        quiet="AI marketing agents, guided by experts",
        themes=[T("Customer Value", "/expertise/customer-value/"), T("Loyalty", "/expertise/loyalty/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("AI Enablement", "/services/ai-enablement/"), T("Operating Model Design", "/services/operating-model-design/"), T("Customer Research and Insight", "/services/customer-research/")],
        h1="AI Agents for Marketing",
        h2s=["Overview", "Why now?", "How can we help you?", "AgentLab", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["Reporting and Analytics", "Data and Infrastructure", "Strategy and Planning", "Automation and Execution"],
        intent="Marketing-qualified AI page. AgentLab is the named agent catalogue on this page. Bare 'AI agents' is too generic to be the sole target. Client service template applied; AgentLab keeps its anchored H2 home.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("AI Agents for Marketing", None)],
        kind="service",
        mural=SERVICE_MURAL,
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
        quiet="Target operating model",
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/")],
        services=[T(GO_NAME, GO_URL), T("AI Enablement", "/services/ai-enablement/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/")],
        h1="Operating Model Design",
        h2s=["Overview", "Why now?", "How can we help you?", "Our Operating Architecture framework", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["Target operating model", "Adaptive operating model", "High-quality data and tools", "New work units", "Orchestration: culture, value, capability"],
        intent="Strongest Activation search volume after journey and CX. Operating model and target operating model language in the H1 support line and headings. Operating Architecture is the framework name on the page. Client service template applied; the framework keeps its anchored H2 home.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("Operating Model Design", None)],
        kind="service",
        mural=SERVICE_MURAL,
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
        url=GO_URL,
        title=f"{GO_NAME}: interim growth team and programme office",
        section="services",
        weight="Canonical",
        primary="interim cmo / interim growth team (~110 to 140)",
        alts=["growth office (~10, weak; not the primary target)", "programme office / PMO (hero language)", "interim activation then embed (deck shape)"],
        quiet="Interim growth team",
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/")],
        services=[T("Operating Model Design", "/services/operating-model-design/"), T("CEO Advisory", "/services/ceo-advisory/"), T("AI Enablement", "/services/ai-enablement/")],
        h1=GO_NAME,
        h2s=["Overview", "Why now?", "How can we help you?", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["Interim growth team", "Then embed", "Culture", "Capability", "Value"],
        intent=f"{GO_NAME} is the working name (Andy, 19 Oct: naming still being finalised). The menu subtitle and body say interim or embedded growth team, and interim CMO where accurate. The primary search phrase is interim growth team, not the coined label. Client service template applied.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), (GO_NAME, None)],
        kind="service",
        notes=["Working name per Andy (19 Oct); naming still being finalised. The name is one constant in the builder, so a later swap is one change", "The 15 Oct alternative name is retired; its URL redirects here (alias in mocks/_redirects; logged in docs/mural-layout-check-oct.md)"],
        mural=SERVICE_MURAL,
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
        quiet="AI skills and adoption",
        themes=[T("Customer Value", "/expertise/customer-value/")],
        sectors=[T("Consumer", "/sectors/consumer/"), T("Media", "/sectors/media/")],
        services=[T("AI Agents for Marketing", "/services/ai-agents-for-marketing/"), T("Operating Model Design", "/services/operating-model-design/")],
        h1="AI Enablement",
        h2s=["Overview", "Why now?", "How can we help you?", "Related case studies", "Why us?", "Our experts", "How it works"],
        h3s=["AI skills and adoption", "Finding where AI pays off", "New business models with AI"],
        intent="Thin but real niche. Owns 'AI enablement' as primary, supported by adoption, skills and operating-change copy. The expert network is named in the body. Client service template applied.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("Activation Services", "/services/activation/"), ("AI Enablement", None)],
        kind="service",
        mural=SERVICE_MURAL,
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
        quiet="One-to-one advisory retainer",
        themes=[],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T(GO_NAME, GO_URL)],
        h1="CEO Advisory",
        h2s=["Overview", "Why now?", "How can we help you?", "Our advisors", "Related case studies", "Why us?"],
        h3s=["Side-by-Side (the named product, hero and this section, not a second URL)", "How the retainer works"],
        intent="Relationship page at full weight. Two menu strands land here: Side-by-Side (the retainer) and Our advisors (the people). Proof is the people. Coaching language is adjacent, not the offer. Client service template applied where sensible; the #side-by-side and #advisors anchors are unchanged.",
        crumbs=[("Home", "/"), ("What we do", "/services/"), ("CEO Advisory", None)],
        kind="ceo",
        notes=["Side-by-Side is always written in full", "Quieter call to action: Arrange a conversation"],
        mural=SERVICE_MURAL,
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
        intent="Indexes the five expertise themes. Describes the growth problems, not how services are delivered.",
        crumbs=[("Home", "/"), ("Expertise", None)],
        kind="expertise-hub",
        notes=["Theme titles were not fully keyworded in the Sep 2026 pull; second pass before URLs lock"],
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
        intent="Proves we understand the problem, then hands off to services. Describes the problem, never how a service is delivered.",
        crumbs=[("Home", "/"), ("Expertise", "/expertise/"), (name, None)],
        kind="theme",
        notes=["Theme titles were not fully keyworded in the Sep 2026 pull"],
        view=view,
        help_svcs=help_svcs,
    ))

for slug, name, intro, used in [
    (
        "financial-services",
        "Financial services",
        "Banks, insurers and specialist lenders. Quote journeys, member and policyholder value, and the operating models behind them.",
        [
            ("Experience Engineering", "/services/experience-engineering/"),
            ("Customer Research and Insight", "/services/customer-research/"),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
        ],
    ),
    (
        "media",
        "Media",
        "Publishers and media groups. Subscriptions, membership, and getting strategy delivered in newsroom-adjacent businesses.",
        [
            (GO_NAME, GO_URL),
            ("Operating Model Design", "/services/operating-model-design/"),
            ("Proposition Innovation", "/services/proposition-innovation/"),
        ],
    ),
    (
        "consumer",
        "Consumer",
        "Consumer brands, travel and leisure. Short-break, park and travel journeys, and the loyalty and membership offers around them.",
        [
            ("Experience Engineering", "/services/experience-engineering/"),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/"),
            (GO_NAME, GO_URL),
        ],
    ),
    (
        "retail",
        "Retail",
        "Retailers who need offers, journeys and value economics that work in store and direct.",
        [
            ("Proposition Innovation", "/services/proposition-innovation/"),
            ("Customer Research and Insight", "/services/customer-research/"),
            ("Experience Engineering", "/services/experience-engineering/"),
        ],
    ),
    (
        "energy",
        "Energy",
        "Energy providers and the businesses around them. Customer propositions, utilisation economics and the journeys that win and keep customers.",
        [
            ("Proposition Innovation", "/services/proposition-innovation/"),
            ("Growth Strategy", "/services/growth-strategy/"),
            ("Customer Research and Insight", "/services/customer-research/"),
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
        intent="Reassures 'businesses like mine': a short intro plus filtered proof.",
        crumbs=[("Home", "/"), (name, None)],
        kind="sector",
        notes=["Light landing: no sector point-of-view essay and no sector-specific service descriptions"]
        + (["New sector from the unified industry taxonomy (client list merged with ours, Mural pass 15 Oct): Finance folds into Financial services, CPG folds into Consumer, Energy is added"] if slug == "energy" else []),
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
        sectors=[T("Financial services", "/sectors/financial-services/"), T("Media", "/sectors/media/"), T("Consumer", "/sectors/consumer/"), T("Retail", "/sectors/retail/"), T("Energy", "/sectors/energy/")],
        services=[T("Experience Engineering", "/services/experience-engineering/"), T("Growth Strategy", "/services/growth-strategy/")],
        h1="Our work",
        h2s=["Our clients", "All case studies", "Client testimony"],
        h3s=[],
        intent="Proof hub: every case study in one place. One grid with an Industry and Service filter bar and See more (client layout); the nav label and H1 stay Our work, with the client's Our clients idea as the support line and logo band.",
        crumbs=[("Home", "/"), ("Our work", None)],
        kind="work-hub",
        notes=[
            "The separate Featured / All split is removed so one grid does the work",
            "Industries are the unified taxonomy: Financial services, Consumer, Media, Retail, Energy",
            "Client quotes and film snippets live inside each case; the hub carries one testimony video",
            "Cases are tagged by service, expertise and sector; the tags drive these filters and the proof blocks on service, theme and sector pages",
        ],
        mural=["Our clients support line", "Short intro", "Auto-scrolling logo band", "Filter: Industry, Service", "Card grid + See more", "Testimony video", "Contact us band"],
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
        h2s=["The Opportunity", "The Solution", "The Impact", "See more of our case studies"],
        h3s=["Client testimonial (attributed, beside the stat rail)"],
        intent="Case study shell for an Experience Engineering engagement (client layout): hero with tag pills, sticky stat rail with Contact us, attributed testimonial, then Opportunity, Solution and Impact. Tag pills link the service, sector and expertise pages so cross-linking survives.",
        crumbs=[("Home", "/"), ("Our work", "/work/"), ("Dayinsure", None)],
        kind="case",
        notes=["Stats and the quote are placeholders; no client facts are invented", "Impact is written as bullets", "Film snippet sits with the testimonial where one exists", "Read on the page; no PDF download"],
        mural=["Hero: project name, title, tag pills, image", "Sticky stat rail + Contact us", "Attributed testimonial", "The Opportunity", "The Solution", "The Impact (bullets)", "See more of our case studies"],
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
        h2s=["The Opportunity", "The Solution", "The Impact", "See more of our case studies"],
        h3s=["Client testimonial (attributed, beside the stat rail)"],
        intent="Second case study shell, same client-layout template as Dayinsure. Its tags place it in the proof blocks on service, theme and sector pages.",
        crumbs=[("Home", "/"), ("Our work", "/work/"), ("Key Group", None)],
        kind="case",
        notes=["Stats and the quote are placeholders; no client facts are invented", "Impact is written as bullets", "Read on the page; no PDF download"],
        mural=["Hero: project name, title, tag pills, image", "Sticky stat rail + Contact us", "Attributed testimonial", "The Opportunity", "The Solution", "The Impact (bullets)", "See more of our case studies"],
        client="Key Group",
        result="Experience and offer working as one (figure TBC)",
        sector_name="Financial services",
        sector_url="/sectors/financial-services/",
    ),
    dict(
        url="/insights/",
        title="Our thinking",
        section="insights",
        weight="Supporting",
        primary="thought leadership hub (long-tail lives on articles and reports)",
        alts=["Our thinking is the nav label; URL stays /insights/", "reports, articles, events are types, not extra top-nav items"],
        quiet=None,
        themes=[T("Loyalty", "/expertise/loyalty/"), T("Pricing", "/expertise/pricing/")],
        sectors=[],
        services=[],
        h1="Our thinking",
        h2s=["All thinking", "The Nutshell"],
        h3s=[],
        intent="Home of all thinking as one grid with one card design (client layout): type tabs in the order All, Reports, Articles, News and events, then a tag filter, with the type shown on every card. The filters work in this wireframe: tabs and tag pills hide and show cards client-side, and deep links (?type=reports or #reports) from the nav dropdown open the matching state. Every card stays in the HTML, so nothing is hidden from search.",
        crumbs=[("Home", "/"), ("Our thinking", None)],
        kind="insights-hub",
        notes=[
            "Articles and blog posts are one type here; there is no separate blog",
            "News and Events are one merged type: News and events",
            "No downloads from the grid: reports open their own page, where the email gate lives",
            "The grid runs one, two or three across depending on how many items a filter returns",
            "Home shows one featured report and one article, not this grid",
        ],
        mural=["Type tabs: All, Reports, Articles, News and events", "Tag filter", "One card design, type on card", "1 to 3 across grid", "Report gate on the report page, not the grid"],
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
        h2s=["The problem", "What we think", "Related"],
        h3s=[],
        intent="Article shell (client layout): title and image hero, body, then a Related trio of one article, one service and one report. The theme page holds the evergreen position.",
        crumbs=[("Home", "/"), ("Our thinking", "/insights/"), ("Loyalty without the discount", None)],
        kind="insight",
        notes=["Lives under Our thinking; there is no separate blog section", "The Related trio replaces the former How we help block; the service link moves into the trio"],
        mural=["Hero: title + image", "Article body", "Related trio: article, service, report"],
    ),
    dict(
        url="/insights/pricing-paradox/",
        title="The Pricing Paradox",
        section="insights",
        weight="Supporting",
        primary="pricing thought leadership (hands off to /expertise/pricing/)",
        alts=["no PDF download", "report type of Our thinking"],
        quiet=None,
        themes=[T("Pricing", "/expertise/pricing/")],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("Proposition Innovation", "/services/proposition-innovation/")],
        h1="The Pricing Paradox: from tactical lever to growth engine",
        h2s=["What this report covers", "Read it on this page", "How we help"],
        h3s=[],
        intent="Report shell. The report reads on the page; the email gate (full name, work email, company, newsletter opt-in) lives here, never on the grid.",
        crumbs=[("Home", "/"), ("Our thinking", "/insights/"), ("The Pricing Paradox", None)],
        kind="report",
        notes=["No PDF download; gating, if used, is a form not a file", "Gated versus read-on-page detail is an open item with the client", "Reports share the one grid on Our thinking, shown by their type on the card"],
        mural=["Email gate form: full name, work email, company, newsletter opt-in"],
    ),
    dict(
        url="/about/",
        title="About",
        section="about",
        weight="Supporting",
        primary="Manifesto Growth Architects (brand)",
        alts=["growth architects (who we are). The system itself, pillars and services, stays canonical on /services/"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("Our Growth Architecture", "/services/"), T("Growth Strategy", "/services/growth-strategy/"), T("Activation Services", "/services/activation/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="About Manifesto Growth Architects",
        h2s=["Why Growth Architecture", "What a Growth Architect does", "Our Growth Architecture", "Our story", "Our people", "Our approach"],
        h3s=["Growth Architects", "Expert Community", "SxS Advisors"],
        intent="About is framed around Growth Architecture: why Manifesto built it, what a Growth Architect does, and who the Growth Architects are. The system itself (pillars and services) stays canonical on What we do; About says why and who, and links there.",
        crumbs=[("Home", "/"), ("About", None)],
        kind="about",
        notes=[
            "Framing only (Andy, 1 October). Copy comes from the current brand work; no new copy is written here",
            "The triangle is not drawn again on About. Three pillar links and one line point to What we do",
            "Our people previews the three team groups: Growth Architects, Expert Community, SxS Advisors",
            "Life at Manifesto lives on Careers; About links to it",
        ],
    ),
    dict(
        url="/about/team/",
        title="Our people",
        section="about",
        weight="Supporting",
        primary="named-person search (profiles); this page is the listing",
        alts=["Our advisors in the mega-nav land on CEO Advisory, not here"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[T("CEO Advisory", "/services/ceo-advisory/"), T("AI Enablement", "/services/ai-enablement/")],
        h1="Our people",
        h2s=["Growth Architects", "Expert Community", "SxS Advisors"],
        h3s=["Culture over headshots (visual note)"],
        intent="Meet the team in three groups (Andy, 1 October): Growth Architects, the core Manifesto team; Expert Community, the C and N and growth collective profiles; SxS Advisors, the Side-by-Side profiles. Each group has an anchor, an intro line and Person cards. Cross-links to Careers for Life at Manifesto and current opportunities.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("Our people", None)],
        kind="team",
        notes=[
            "Three sections replace Leadership, Consultants, Side-by-Side advisors and Associates. Leadership and consultants are ordered within Growth Architects, not split into sub-sections",
            "Expert Community absorbs the former Associates and expert network group and the C and N placeholder. AI Enablement body copy links here",
            "SxS Advisors keeps the #advisors anchor so the CEO Advisory page and existing links still land on it",
            "Culture over headshots in the visual treatment",
            "The menu strand Our advisors lands on CEO Advisory, not here",
        ],
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
        intent="Profile shell. Every profile names its group (Growth Architects, Expert Community or SxS Advisors) and links to that section of Our people. Advisor note links back to Side-by-Side on the CEO Advisory page.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("Our people", "/about/team/"), ("Advisor name", None)],
        kind="profile",
    ),
    dict(
        url="/about/how-we-work/",
        title="Our approach",
        section="about",
        weight="Supporting",
        primary="methodology (not a product; no service keyword)",
        alts=["Growth Architecture, CIVD, Operating Architecture, AgentLab, Side-by-Side each have one anchored home"],
        quiet="How we partner with clients",
        themes=[],
        sectors=[],
        services=[T("Growth Strategy", "/services/growth-strategy/"), T("AI Agents for Marketing", "/services/ai-agents-for-marketing/"), T("CEO Advisory", "/services/ceo-advisory/")],
        h1="Our approach",
        h2s=["How we partner", "Growth partner videos", "Principles", "Engagement shapes", "Frameworks and tools", "Working with AI"],
        h3s=["Growth Architecture", "Customer, Innovation, Value and Delivery", "Operating Architecture", "AgentLab", "Side-by-Side"],
        intent="Method page: how we partner, principles, engagement shapes, and the five named frameworks, each pointing to its home page. Method is never a product.",
        crumbs=[("Home", "/"), ("About", "/about/"), ("Our approach", None)],
        kind="how",
        notes=["Growth partner films live here", "Qualitative and quantitative evidence is described on Customer Research and Insight"],
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
        notes=["DEI commitments here; hiring context on Careers"],
    ),
    dict(
        url="/careers/",
        title="Careers",
        section="careers",
        weight="Light",
        primary="none",
        alts=["Life at Manifesto is a section here, not a competing About page"],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="Careers at Manifesto",
        h2s=["Life at Manifesto", "Values and culture", "Diversity, equity and inclusion", "Benefits", "Application process", "Roles"],
        h3s=["Career change framing", "We hire from multiple backgrounds", "Pioneers / recent joiners"],
        intent="First-class nav item: Contact is work with us, this page is work for us. Client layout applied: hero with a See open positions anchor button, four values and culture cards, the five-step application process, and a Roles section with an Open positions / All toggle. Life at Manifesto, DEI and Benefits are kept.",
        crumbs=[("Home", "/"), ("Careers", None)],
        kind="careers",
        notes=[
            "Life at Manifesto stays on Careers and separate from Our people",
            "The Roles intro says to get in touch even if no role fits (folds in the former Not hiring for a listed role? section)",
            "The roles toggle defaults to Open positions",
            "Career-change framing and multiple backgrounds in the copy",
            "Role descriptions expand on the role page; no PDFs",
            "Studio film in the hero",
        ],
        mural=["Hero + See open positions button", "Brief description", "Values and culture cards (4)", "Application process (5 steps)", "Roles + Open positions / All toggle", "Reach-out line"],
    ),
    dict(
        url="/careers/growth-architect/",
        title="Growth Architect",
        section="careers",
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
        intent="Role shell (client layout): title, description, then How to apply via LinkedIn, linking to the application page. noindex when the role closes.",
        crumbs=[("Home", "/"), ("Careers", "/careers/"), ("Growth Architect", None)],
        kind="role",
        notes=["No PDF job description", "Applications go through LinkedIn; the wireframe shows the link as a placeholder"],
        mural=["Position title", "Description", "How to apply via LinkedIn"],
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
        h2s=["Work with us", "Work for us", "Direct contact"],
        h3s=["The Nutshell"],
        intent="Two routes: work with us (the client form) and work for us (a speculative form; roles stay on Careers). Links to The Nutshell sign-up.",
        crumbs=[("Home", "/"), ("Contact", None)],
        kind="contact",
        notes=["Email Mark stays as one tracked direct route", "Topic is a select, pre-filled from ?topic= where a service page linked here"],
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
        title="The Nutshell",
        section="insights",
        weight="Utility",
        primary="none",
        alts=[],
        quiet=None,
        themes=[],
        sectors=[],
        services=[],
        h1="The Nutshell",
        h2s=["Sign up"],
        h3s=[],
        intent="Email capture for the newsletter, which is called The Nutshell. Indexed utility page.",
        crumbs=[("Home", "/"), ("The Nutshell", None)],
        kind="legal",
        blurb="The Nutshell: events, thought leadership and what has caught our attention.",
    ),
]

for slug, name, blurb in [
    ("privacy-policy", "Privacy policy", "How we use personal information."),
    ("cookie-policy", "Cookie policy", "Cookies and how to manage them."),
    ("terms", "Terms", "Website terms of use."),
    ("accessibility", "Accessibility statement", "How we work to make this site usable."),
    ("search", "Search", "Search results."),
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

PAGES.append(dict(
    url="/catalogue/",
    title="Component library",
    section="home",
    weight="Utility",
    primary="none (wireframe index, not a live URL)",
    alts=["Not a client sitemap item. Linked from All pages and from every sidebar."],
    quiet=None,
    themes=[],
    sectors=[],
    services=[],
    h1="Component library",
    h2s=["How to read this library"] + COMPONENT_GROUPS + ["Do not mix"],
    h3s=[],
    intent="Wireframe-only index of the reusable components used on every page: one name and one shape per component. Not a proposed live client URL.",
    crumbs=[("Home", "/"), ("Component library", None)],
    kind="catalogue",
))


def body_for(page: dict) -> str:
    url = page["url"]
    h = lambda u: rel_href(url, u)
    kind = page["kind"]

    if kind == "home":
        return f"""
        {hero_open()}
          {ann("Band: hero")}
          <h1>{page["h1"]}</h1>
          <p>Strategy that works. Execution that delivers.</p>
          {ann("Button + text link")}
          {cta_html(h, ("Contact", "/contact/"), ("What we do", "/services/"))}
          {ann("Static: existing asset")}
          {video_html("Manifesto showreel / client video", asset="Existing film, confirmed for Home (Andy, 1 October). Embedded in the hero, not a placeholder.")}
        </section>
        <section class="block">
          <h2 class="sec">Trusted partners</h2>
          {ann("Static")}
          {logos_html(8, "Logo")}
        </section>
        <section class="block">
          <h2 class="sec">What we do</h2>
          {ann("Triangle tile: card")}
          {tri_html(h, PILLAR_TILES, f'<p class="tri-line">Strategy first. Activation to deliver it. Advisors alongside. <a href="{h("/services/")}">Our Growth Architecture</a></p>')}
        </section>
        {thinking_feature(h, annotate=True)}
        <section class="block">
          <h2 class="sec">Our work</h2>
          {ann("Case card")}
          <div class="cards two">
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
            {card(h, "/work/key-group/", "Key Group", "One-line result", "ph")}
          </div>
          {quote_html(cite="Dayinsure")}
          {ann("Text link")}
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        <section class="block">
          <h2 class="sec">Awards</h2>
          {ann("Static")}
          {logos_html(3, "Award")}
        </section>
        <section class="block">
          <h2 class="sec">Growth problems we know best</h2>
          {ann("Text link")}
          <div class="row-links" {mod("Row of text links")}>
            <a href="{h("/expertise/loyalty/")}">Loyalty</a>
            <a href="{h("/expertise/membership/")}">Membership</a>
            <a href="{h("/expertise/subscriptions/")}">Subscriptions</a>
            <a href="{h("/expertise/pricing/")}">Pricing</a>
            <a href="{h("/expertise/customer-value/")}">Customer Value</a>
          </div>
        </section>
        {closing(h, annotate=True)}
"""

    if kind == "hub":
        return f"""
        {hero_open()}
          {ann("Band: hero")}
          <span class="eyebrow">What we do</span>
          <h1>Our Growth Architecture</h1>
          <p>Strategy that works. Execution that delivers.</p>
          <p class="body">The path from strategy to execution has become more complex and fragmented, despite more tools, data and channels than ever.</p>
          <p class="body">Growth Architecture is a better way to unlock customer value growth: market-leading strategic thinking combined with AI-powered, human-led activation.</p>
        </section>
        <section class="block">
          <h2 class="sec">Three ways we work with you</h2>
          {ann("Triangle tile: card")}
          {tri_html(h, [(n, a, s) for (n, _, s), a in zip(PILLAR_TILES, ("#hub-gs", "#hub-act", "#hub-ceo"))], '<p class="tri-line">Strategy first. Activation to deliver it. Advisors alongside.</p>')}
        </section>
        <section class="block">
          <h2 class="plain">Where are you starting from?</h2>
          {ann("Text link")}
          <ul class="situations" {mod("Situations list")}>
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
          {ann("Static")}
          {civd_html(compact=True)}
          <p class="link-line" {mod("Link line")}>The frame lives on Growth Strategy. <a href="{h("/services/growth-strategy/#civd")}">See the CIVD frame</a></p>
          {ann("Offer card")}
          <div class="cards two">
            {card(h, "/services/growth-strategy/", "Growth Strategy", "Customer-led growth strategy: where to focus and how to win", "offer")}
            {card(h, "/services/proposition-innovation/", "Proposition Innovation", "Value proposition design: loyalty, membership, subscription, direct-to-consumer", "offer")}
          </div>
          <p class="case-line" {mod("Case line")}>Key Group, one-line result. <a href="{h("/work/key-group/")}">Read the case study</a></p>
        </section>
        <section class="block pillar-sec" id="hub-act">
          <h2 class="plain"><a href="{h("/services/activation/")}">Activation Services</a></h2>
          <p class="line">Turning strategy into results</p>
          <p class="sentence">We build the bridge from strategy to results: new operating models and AI-powered, human-led delivery. <a href="{h("/services/activation/")}">Which of the six do you need?</a></p>
          {ann("Offer card")}
          <div class="cards">
            {card(h, "/services/customer-research/", "Customer Research and Insight", "Research, surveys, analytics and customer listening, faster with AI", "offer")}
            {card(h, "/services/experience-engineering/", "Experience Engineering", "Customer experience (CX), website and digital design, build and testing", "offer")}
            {card(h, "/services/ai-agents-for-marketing/", "AI Agents for Marketing", "AI marketing agents that clean data and improve performance, guided by experts", "offer")}
            {card(h, "/services/operating-model-design/", "Operating Model Design", "Target operating model: how teams, data and AI agents work together", "offer")}
            {card(h, GO_URL, GO_NAME, "Interim growth team and programme office that gets strategy delivered", "offer")}
            {card(h, "/services/ai-enablement/", "AI Enablement", "AI skills, training and adoption: finding where AI pays off", "offer")}
          </div>
          <p class="case-line" {mod("Case line")}>Dayinsure, one-line result. <a href="{h("/work/dayinsure/")}">Read the case study</a></p>
        </section>
        <section class="block pillar-sec" id="hub-ceo">
          <h2 class="plain"><a href="{h("/services/ceo-advisory/")}">CEO Advisory</a></h2>
          <p class="line">One-to-one support for leaders</p>
          <p class="sentence">Experienced growth leaders alongside you, on retainer, to help you make good decisions.</p>
          {ann("Person card")}
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
          </div>
          {ann("Text link")}
          <a class="more" href="{h("/services/ceo-advisory/#advisors")}">Our advisors</a>
        </section>
        <section class="block">
          <p class="one-line" {mod("Link line")}>We apply these services to the growth problems we know best. <a href="{h("/expertise/")}">Our expertise</a></p>
        </section>
        {closing(h, annotate=True)}
"""

    if kind == "activation":
        six = [
            ("Customer Research and Insight", "/services/customer-research/", "You need to understand customers faster and agree one version of the truth. Methods, journey mapping, insight."),
            ("Experience Engineering", "/services/experience-engineering/", "A journey, product or website is underperforming and you want it found, fixed, tested and scaled."),
            ("AI Agents for Marketing", "/services/ai-agents-for-marketing/", "Your customer data is holding marketing back and you want AI marketing agents doing the work."),
            ("Operating Model Design", "/services/operating-model-design/", "You need to redesign how teams, data and AI agents work together: a target operating model."),
            (GO_NAME, GO_URL, "You need an interim growth team, and sometimes an interim CMO, to get the strategy delivered and the value tracked."),
            ("AI Enablement", "/services/ai-enablement/", "You want your people to use AI well and to find where it pays off."),
        ]
        lines = link_list([(f"<strong>{n}.</strong> {t}", h(u), "") for n, u, t in six])
        cards = "".join(card(h, u, n, t.split(".")[0], "offer") for n, u, t in six)
        return f"""
        {hero_open()}
          <span class="eyebrow">Activation Services</span>
          <h1>Activation Services</h1>
          <p>{page["hero"]}</p>
          <p class="who">{page["who"]}</p>
          {cta_html(h)}
        </section>
        <section class="block">
          <h2 class="plain">The bridge from strategy to results</h2>
          <p class="prose">A brilliant strategy only counts if it gets executed and the value shows up. Activation is how we get you there: hands-on, AI-powered, human-led, and not ongoing operations.</p>
        </section>
        <section class="block">
          <h2 class="plain">Which of the six do you need?</h2>
          {lines}
        </section>
        <section class="block">
          <h2 class="plain">The six Activation services</h2>
          <div class="cards">{cards}</div>
        </section>
        <section class="block">
          <h2 class="plain">Proof</h2>
          <div class="cards two">
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
            {card(h, "/work/key-group/", "Key Group", "One-line result", "ph")}
          </div>
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        {related_thinking(h)}
        {closing(h)}
"""

    if kind == "service":
        sits = "".join(f"<li>{s}</li>" for s in page["situations"])
        aka = f'<p class="aka">Also known as: {page["aka"]}</p>' if page.get("aka") else ""
        nums = ""
        if page.get("numbers"):
            if "3x" in page["numbers"]:
                nums = metrics_html([("3x", "EBITDA return")])
            elif "4 weeks" in page["numbers"]:
                nums = metrics_html([("4 wks", "Data audit"), ("6 wks", "First agents")])
            else:
                nums = metrics_html([("Result", page["numbers"])])
        pillar = (
            f'<p class="pillar-note"><a href="{h(page["pillar"][1])}">{page["pillar"][0]}</a></p>'
            if page.get("pillar") else ""
        )
        extra = service_module(page, h)
        theme_tags = tags_html(h, (page.get("themes") or [])[:3])
        rel_svcs = "".join(card(h, u, n, "Often bought alongside", "offer") for n, u in (page.get("services") or [])[:3])
        return f"""
        {hero_open()}
          <h1>{page["h1"]}</h1>
          {aka}
          <p>{page["hero"]}</p>
          <p class="who">{page["who"]}</p>
          {nums}
          {pillar}
          {cta_html(h)}
          <div class="hero-img" aria-hidden="true">Image</div>
        </section>
        <section class="block">
          <h2 class="plain">Overview</h2>
          <p class="prose">What this service is and the value it creates, in two or three plain sentences.</p>
        </section>
        <section class="block">
          <h2 class="plain">Why now?</h2>
          <ul class="situations" {mod("Situations list")}>{sits}</ul>
          <p class="prose">Two to four short paragraphs on why this matters now.</p>
        </section>
        <section class="block">
          <h2 class="plain">How can we help you?</h2>
          <span class="wf-label">Every section visible on the page: real H3s, no accordion or tabs</span>
          {extra["help"]}
        </section>
        {extra["modules"]}
        <section class="block">
          <h2 class="plain">Related case studies</h2>
          <span class="wf-label">Constant speed carousel; pauses on hover</span>
          <div class="carousel">
            {tl_card(h, "/work/dayinsure/", "Dayinsure", "One-line result (placeholder)", "Experience Engineering", ("Financial services", "Customer value"))}
            {tl_card(h, "/work/key-group/", "Key Group", "One-line result (placeholder)", "Experience Engineering", ("Financial services", "Loyalty"))}
          </div>
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        <section class="block">
          <h2 class="plain">Why us?</h2>
          <p class="prose">Why Manifesto for this work: the team, the method, the results. Plain words, no claims we cannot prove. <a href="{h("/about/how-we-work/")}">Our approach</a>.</p>
        </section>
        <section class="block">
          <h2 class="plain">Our experts</h2>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Expert name", "Role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Expert name", "Role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Expert name", "Role, one line", "person")}
          </div>
          {popup_html(h)}
        </section>
        {extra["how"]}
        <section class="block">
          <h2 class="sec">Related expertise</h2>
          {theme_tags}
        </section>
        <section class="block">
          <h2 class="sec">Related services</h2>
          <div class="cards two">{rel_svcs}</div>
        </section>
        <section class="block">
          <h2 class="sec">Related thinking</h2>
          {link_list([("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report"), ("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article")])}
        </section>
        {closing(h)}
"""

    if kind == "ceo":
        return f"""
        {hero_open()}
          <h1>CEO Advisory</h1>
          <p>{page["hero"]}</p>
          <p class="who">{page["who"]}</p>
          {cta_html(h, ("Arrange a conversation", "/contact/"))}
          <div class="hero-img" aria-hidden="true">Image</div>
        </section>
        <section class="block">
          <h2 class="plain">Overview</h2>
          <p class="prose">One-to-one support for leaders, on retainer, through the Side-by-Side product. What it is and who it is for, in two plain sentences.</p>
        </section>
        <section class="block">
          <h2 class="plain">Why now?</h2>
          <ul class="situations" {mod("Situations list")}>
            <li>I want a sounding board I trust</li>
            <li>Driving customer-led growth is demanding and lonely</li>
            <li>I need advice on speed-dial, not another consulting project</li>
          </ul>
          <p class="prose">Senior leaders who work with you on retainer.</p>
        </section>
        <section class="block">
          <h2 class="plain">How can we help you?</h2>
          <span class="wf-label">Every section visible on the page: real H3s, no accordion or tabs</span>
          <div id="side-by-side">
          <h3 class="plain">Side-by-Side</h3>
          <p class="prose">A select group of senior leaders, armed with Manifesto thinking and frameworks. Adaptive and personality-led. Retainer-based, virtual or in person, so practitioners focus on delivering value, not on selling. This is the named product inside CEO Advisory.</p>
          </div>
          <h3 class="plain">How the retainer works</h3>
          <p class="prose">Disciplined yet flexible. Virtual or in person. Personality-led. The product name is Side-by-Side.</p>
        </section>
        <section class="block" id="advisors">
          <h2 class="plain">Our advisors</h2>
          <p class="prose">The experts on this offer. Profiles live with <a href="{h("/about/team/")}">Our people</a>.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person")}
          </div>
          {popup_html(h, "Advisor name", "Former role, one line")}
          <a class="more" href="{h("/about/team/")}">Our people</a>
        </section>
        <section class="block">
          <h2 class="plain">Related case studies</h2>
          <span class="wf-label">Constant speed carousel; pauses on hover</span>
          <div class="carousel">
            {tl_card(h, "/work/key-group/", "Key Group", "One-line result (placeholder)", "Experience Engineering", ("Financial services", "Loyalty"))}
            {tl_card(h, "/work/dayinsure/", "Dayinsure", "One-line result (placeholder)", "Experience Engineering", ("Financial services", "Customer value"))}
          </div>
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        <section class="block">
          <h2 class="plain">Why us?</h2>
          <p class="prose">The advisors are the proof: experienced growth leaders who have sat in the chair. Plain words, no claims we cannot prove.</p>
        </section>
        {related_thinking(h)}
        {closing(h, "Arrange a conversation")}
"""

    if kind == "expertise-hub":
        cards = "".join(
            card(h, f"/expertise/{s}/", n, "Cases and thinking", "theme")
            for s, n in [
                ("loyalty", "Loyalty"),
                ("membership", "Membership"),
                ("subscriptions", "Subscriptions"),
                ("pricing", "Pricing"),
                ("customer-value", "Customer Value"),
            ]
        )
        return f"""
        {hero_open()}
          <h1>Our expertise</h1>
          <p>The growth problems we are known for. Each cuts across services and sectors.</p>
        </section>
        <section class="block">
          <h2 class="plain">The growth problems we know best</h2>
          <div class="cards">{cards}</div>
        </section>
        <section class="block">
          <h2 class="plain">Latest thinking across themes</h2>
          {link_list([("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article"), ("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report")])}
        </section>
        {closing(h)}
"""

    if kind == "theme":
        helps = link_list([(f"<strong>{n}.</strong> {line}", h(u), "") for n, u, line in page["help_svcs"]])
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
        {hero_open()}
          <h1>{page["h1"]}</h1>
          <p>{page["view"]}</p>
          {cta_html(h)}
        </section>
        <section class="block">
          <h2 class="plain">Our view</h2>
          <p class="prose">Our view of the problem, what tends to fail, and what good looks like.</p>
        </section>
        <section class="block">
          <h2 class="plain">Where we help</h2>
          {helps}
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
          {link_list([("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article")])}
          <a class="more" href="{h("/insights/")}">All thinking</a>
        </section>
        <section class="block">
          <h2 class="sec">Related themes</h2>
          <div class="row-links" {mod("Row of text links")}>{others}</div>
        </section>
        {closing(h)}
"""

    if kind == "sector":
        used = link_list([(n, h(u), "") for n, u in page["services"]])
        return f"""
        {hero_open()}
          <h1>{page["h1"]}</h1>
          <p class="body">{page["intro"]}</p>
        </section>
        <section class="block">
          <h2 class="plain">Clients</h2>
          {logos_html(5, "Logo")}
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
          {used}
        </section>
        {related_thinking(h)}
        {closing(h)}
"""

    if kind == "work-hub":
        return f"""
        {hero_open()}
          {ann("Band: hero")}
          <h1>Our work</h1>
          <p>Our clients: ambitious leaders who want sustainable, customer-led growth.</p>
          <p class="body">Short intro. What the work has in common, in two plain sentences.</p>
        </section>
        <section class="block">
          <h2 class="sec">Our clients</h2>
          {ann("Static: auto-scrolling")}
          {logo_band_html(10, "Logo")}
        </section>
        <section class="block">
          <h2 class="plain">All case studies</h2>
          {ann("Filter: industry")}
          {filter_bar(["All industries", "Financial services", "Consumer", "Media", "Retail", "Energy"], on="All industries")}
          {ann("Filter: service")}
          {filter_bar(["All services", "Growth Strategy", "Proposition Innovation", "Experience Engineering", "Customer Research and Insight"], on="All services", more=True)}
          <span class="wf-label">Revealed by More filters: Expertise</span>
          {ann("Thought leadership card")}
          <div class="cards">
            {tl_card(h, "/work/dayinsure/", "Dayinsure", "One-line result or testimony (placeholder)", "Experience Engineering", ("Financial services", "Customer value"))}
            {tl_card(h, "/work/key-group/", "Key Group", "One-line result or testimony (placeholder)", "Experience Engineering", ("Financial services", "Loyalty"))}
          </div>
          {ann("Text link")}
          <a class="more" href="#">See more</a>
        </section>
        {empty_stub("No case studies match these filters.", h("/work/"), annotate=True)}
        <section class="block">
          <h2 class="plain">Client testimony</h2>
          {ann("Static")}
          {testimony_video_html()}
        </section>
        {related_thinking(h)}
        {closing(h, annotate=True)}
"""

    if kind == "case":
        pills = tags_html(
            h,
            (page.get("services") or [])[:2]
            + [(page["sector_name"], page["sector_url"])]
            + (page.get("themes") or [])[:1],
        )
        other = "/work/key-group/" if page["url"] == "/work/dayinsure/" else "/work/dayinsure/"
        other_name = "Key Group" if page["url"] == "/work/dayinsure/" else "Dayinsure"
        return f"""
        {hero_open()}
          <span class="eyebrow">Case study</span>
          <h1>{page["client"]}</h1>
          <p>Project title: the proposition and the outcome in one line (placeholder).</p>
          {ann("Tag: service, industry, expertise")}
          {pills}
          <div class="hero-img" aria-hidden="true">Case study main image</div>
        </section>
        <div class="case-layout">
          {stat_rail_html(h, [("Stat TBC", "Outcome measure, with the client's words"), ("Stat TBC", "Outcome measure, with the client's words")], "Contact us", "Got a growth challenge like this one?")}
          <div class="case-story">
            <section class="block case-quote">
              <h3 class="plain">Client testimonial</h3>
              {quote_html('"Attributed client quote: what changed and why it mattered. Placeholder, no invented facts."', "Name, role, " + page["client"] + " (to be confirmed)")}
              {video_html("Film snippet, where one exists")}
            </section>
            <section class="block">
              <h2 class="plain">The Opportunity</h2>
              <p class="prose">The challenge the client faced and what they needed, in plain words. Sector: <a href="{h(page["sector_url"])}">{page["sector_name"]}</a>.</p>
            </section>
            <section class="block">
              <h2 class="plain">The Solution</h2>
              <p class="prose">The approach we took, step by step, with the services linked from the work.</p>
            </section>
            <section class="block">
              <h2 class="plain">The Impact</h2>
              <ul class="impact-list">
                <li><strong>Outcome one:</strong> what improved, quantified where permitted (placeholder).</li>
                <li><strong>Outcome two:</strong> what it opened up for the client (placeholder).</li>
                <li><strong>Outcome three:</strong> where the client is now (placeholder).</li>
              </ul>
            </section>
          </div>
        </div>
        <section class="block">
          <h2 class="plain">See more of our case studies</h2>
          <div class="cards two">
            {tl_card(h, other, other_name, "One-line result or testimony (placeholder)", "Experience Engineering", ("Financial services",))}
          </div>
          <a class="more" href="{h("/work/")}">All work</a>
        </section>
        {related_thinking(h)}
        {closing(h)}
"""

    if kind == "insights-hub":
        return f"""
        {hero_open()}
          <h1>Our thinking</h1>
          <p>Reports, articles, news and events: one grid, one card.</p>
        </section>
        <section class="block">
          <h2 class="plain">All thinking</h2>
          {ann("Filter: type tabs, All first")}
          {type_tabs_html([("All", None), ("Reports", "reports"), ("Articles", "articles"), ("News and events", "news-events")], on="All")}
          <span class="wf-label">Live in this wireframe: tabs and tag pills filter the grid in place (small script, no framework). Deep links such as ?type=reports or #reports open the matching state. Every card stays in the HTML, so nothing is hidden from search</span>
          {ann("Filter: tags")}
          {filter_bar(["Loyalty", "Pricing", "Customer Value", "Growth Strategy", "Financial services"], more=True, data_attr="data-tag")}
          {ann("Thought leadership card")}
          <div class="cards" data-filter-grid>
            {tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "From tactical lever to growth engine. Read on its page; no download here.", "Growth Strategy", ("Pricing",), "Report", type_slug="reports")}
            {tl_card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Short excerpt of the argument (placeholder).", "Proposition Innovation", ("Loyalty",), "Article", type_slug="articles")}
            {tl_card(h, "/insights/pricing-paradox/", "Pricing Paradox launch event", "Recap and what was discussed (placeholder).", "Growth Strategy", ("Pricing",), "News and events", type_slug="news-events")}
          </div>
          {ann("Text link")}
          <a class="more" href="#">See more</a>
        </section>
        {empty_stub("No thinking matches these filters.", h("/insights/"), filter_hook=True)}
        <section class="block">
          <h2 class="plain">The Nutshell</h2>
          <p class="prose">Events, thought leadership and what has caught our attention. <a href="{h("/newsletter/")}">Sign up to The Nutshell</a></p>
        </section>
        <section class="block">
          <h2 class="sec">Related services</h2>
          <div class="row-links" {mod("Row of text links")}>
            <a href="{h("/services/")}">What we do</a>
            <a href="{h("/expertise/")}">Expertise</a>
            <a href="{h("/work/")}">Our work</a>
          </div>
        </section>
        {closing(h)}
"""

    if kind == "insight":
        return f"""
        {hero_open()}
          <h1>{page["h1"]}</h1>
          <p class="who">Article · 6 min · Author</p>
          {tags_html(h, [("Loyalty", "/expertise/loyalty/")])}
          <div class="hero-img" aria-hidden="true">Image</div>
        </section>
        <section class="block">
          <h2 class="plain">The problem</h2>
          {article_body()}
        </section>
        <section class="block">
          <h2 class="plain">What we think</h2>
          <p class="prose">One or two arguments. In-line links to <a href="{h("/expertise/loyalty/")}">Loyalty</a> where the argument touches it.</p>
        </section>
        <section class="block">
          <h2 class="plain">Related</h2>
          {related_trio_html(h, ("Next article (placeholder)", "/insights/"), ("Proposition Innovation", "/services/proposition-innovation/"), ("The Pricing Paradox", "/insights/pricing-paradox/"))}
        </section>
        {closing(h)}
"""

    if kind == "report":
        return f"""
        {hero_open()}
          <h1>{page["h1"]}</h1>
          <p class="who">Report · Date · Author</p>
          {tags_html(h, [("Pricing", "/expertise/pricing/")])}
        </section>
        <section class="block">
          <h2 class="plain">What this report covers</h2>
          {article_body()}
        </section>
        <section class="block">
          <h2 class="plain">Read it on this page</h2>
          <p class="prose">The full report continues here. The email gate lives on this page, never on the grid. Whether the body is gated or reads in full on the page is an open item with the client.</p>
          {form_html([("Full name", "", ""), ("Work email", "", ""), ("Company", "", "")], "Submit", h("/contact/thank-you/"), '<p class="field-msg">Optional tick: receive updates on events, thought leadership and The Nutshell.</p>')}
        </section>
        <section class="block">
          <h2 class="plain">How we help</h2>
          <p class="prose">Related: <a href="{h("/services/growth-strategy/")}">Growth Strategy</a> and <a href="{h("/expertise/pricing/")}">Pricing</a>.</p>
        </section>
        {closing(h)}
"""

    if kind == "about":
        return f"""
        {hero_open()}
          <h1>About Manifesto Growth Architects</h1>
          <p>We are Growth Architects. Strategy that works. Execution that delivers.</p>
        </section>
        <section class="block">
          <h2 class="plain">Why Growth Architecture</h2>
          <p class="prose">The path from strategy to execution has become complex and fragmented. Growth Architecture is Manifesto's answer: strategic thinking joined to AI-powered, human-led activation. Copy from the current brand work.</p>
        </section>
        <section class="block">
          <h2 class="plain">What a Growth Architect does</h2>
          <p class="prose">The people mix of agency, client and strategy backgrounds, and what that lets us do for a leadership team. Copy from the current brand work.</p>
        </section>
        <section class="block">
          <h2 class="plain">Our Growth Architecture</h2>
          <p class="prose">Three connected ways we work with you. The system itself lives on <a href="{h("/services/")}">What we do</a>.</p>
          {link_list([
              ("Growth Strategy", h("/services/growth-strategy/"), "Where and how you grow"),
              ("Activation Services", h("/services/activation/"), "Turning strategy into results"),
              ("CEO Advisory", h("/services/ceo-advisory/"), "One-to-one support for leaders"),
          ])}
        </section>
        <section class="block">
          <h2 class="plain">Our story</h2>
          <p class="prose">How Manifesto started and how Growth Architecture grew out of the work. Copy from the current brand work.</p>
        </section>
        <section class="block">
          <h2 class="plain">Our people</h2>
          <p class="prose">Three groups, all on <a href="{h("/about/team/")}">Our people</a>.</p>
          <div class="cards">
            {card(h, "/about/team/#growth-architects", "Growth Architects", "Core Manifesto team", "person")}
            {card(h, "/about/team/#expert-community", "Expert Community", "C and N and growth collective", "person")}
            {card(h, "/about/team/#advisors", "SxS Advisors", "Side-by-Side advisors", "person")}
          </div>
        </section>
        <section class="block">
          <h2 class="plain">Our approach</h2>
          <p class="prose"><a href="{h("/about/how-we-work/")}">Our approach</a>. <a href="{h("/about/values/")}">Values and culture</a>. <a href="{h("/careers/")}">Life at Manifesto</a> is on Careers.</p>
        </section>
        {closing(h)}
"""

    if kind == "team":
        return f"""
        {hero_open()}
          <h1>Our people</h1>
          <p>Three groups: Growth Architects, Expert Community, SxS Advisors. <a href="{h("/careers/")}">Life at Manifesto</a> is on Careers.</p>
          <div class="row-links" {mod("Row of text links")}>
            <a href="#growth-architects">Growth Architects</a>
            <a href="#expert-community">Expert Community</a>
            <a href="#advisors">SxS Advisors</a>
          </div>
        </section>
        <section class="block" id="growth-architects">
          <h2 class="plain">Growth Architects</h2>
          <p class="prose">The core Manifesto team. Leadership first, then consultants.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Name", "Partner", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Partner", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Growth Architect", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Growth Architect", "person")}
          </div>
        </section>
        <section class="block" id="expert-community">
          <h2 class="plain">Expert Community</h2>
          <p class="prose">C and N members and the growth collective: specialist practitioners who work alongside the core team, including the AI practitioners for <a href="{h("/services/ai-enablement/")}">AI Enablement</a>.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Name", "Specialism", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Specialism", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Specialism", "person")}
          </div>
        </section>
        <section class="block" id="advisors">
          <h2 class="plain">SxS Advisors</h2>
          <p class="prose">Side-by-Side advisors: the same people as <a href="{h("/services/ceo-advisory/#advisors")}">Our advisors</a> on CEO Advisory.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role", "person")}
            {card(h, "/about/team/advisor-one/", "Advisor name", "Former role", "person")}
          </div>
        </section>
        <section class="block">
          <p class="one-line" {mod("Link line")}>Interested in joining the team? <a href="{h("/careers/")}">Current opportunities</a></p>
        </section>
"""

    if kind == "profile":
        return f"""
        {hero_open()}
          <h1>Advisor name</h1>
          <p>Role · one-line focus</p>
        </section>
        <section class="block">
          <h2 class="plain">Biography</h2>
          <p class="prose">Two to five paragraphs.</p>
        </section>
        <section class="block">
          <h2 class="plain">Focus</h2>
          <p class="prose">Group: <a href="{h("/about/team/#advisors")}">SxS Advisors</a>. Leads on <a href="{h("/services/ceo-advisory/")}">CEO Advisory</a>. Available through Side-by-Side.</p>
        </section>
        <section class="block">
          <h2 class="plain">Selected work</h2>
          <div class="cards two">{card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}</div>
        </section>
        {closing(h)}
"""

    if kind == "how":
        return f"""
        {hero_open()}
          <h1>Our approach</h1>
          <p>How we partner with clients.</p>
        </section>
        <section class="block">
          <h2 class="plain">How we partner</h2>
          <p class="prose">How we work as a growth partner. Qual and quant evidence sits with <a href="{h("/services/customer-research/")}">Customer Research and Insight</a>.</p>
        </section>
        <section class="block">
          <h2 class="plain">Growth partner videos</h2>
          <p class="prose">Client films on working with Manifesto.</p>
          {video_html("Working with Manifesto")}
        </section>
        <section class="block">
          <h2 class="plain">Principles</h2>
          <p class="prose">Including AI-powered, human-led.</p>
        </section>
        <section class="block">
          <h2 class="plain">Engagement shapes</h2>
          {link_list([
              ("Strategy project", h("/services/growth-strategy/"), ""),
              ("Strategy into activation", h("/services/activation/"), ""),
              (f"Embedded interim growth team ({GO_NAME})", h(GO_URL), ""),
              ("Advisory retainer", h("/services/ceo-advisory/"), ""),
          ])}
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
        {hero_open()}
          <h1>Values and culture</h1>
          <p>What we stand for and how the team works together.</p>
        </section>
        <section class="block">
          <h2 class="plain">Values</h2>
          <p class="prose">Three to six values.</p>
        </section>
        <section class="block">
          <h2 class="plain">Culture</h2>
          <p class="prose">How the team works together.</p>
        </section>
        <section class="block">
          <h2 class="plain">Diversity, equity and inclusion</h2>
          <p class="prose">Commitments. <a href="{h("/careers/")}">Careers</a> covers hiring.</p>
        </section>
"""

    if kind == "careers":
        values = "".join(
            f'<a class="card theme" {mod("Culture card")} href="{h("/about/values/")}"><strong>Value {i}</strong><span>One line on what it means here (placeholder)</span></a>'
            for i in range(1, 5)
        )
        return f"""
        {hero_open()}
          <h1>Careers at Manifesto</h1>
          <p>Brief description: what it is like to work here, and the roles we are hiring for.</p>
          {cta_html(h, ("See open positions", "/careers/#roles"), ("Life at Manifesto", "/careers/#life"))}
          {video_html("Studio")}
        </section>
        <section class="block" id="life">
          <h2 class="plain">Life at Manifesto</h2>
          <p class="prose">What it is like to work here. <a href="{h("/about/values/")}">Values and culture</a>. Meet the team: <a href="{h("/about/team/")}">Our people</a>.</p>
          <h3 class="plain">Career change framing</h3>
          <p class="prose">We hire people who are changing direction, not only those already in the craft.</p>
          <h3 class="plain">We hire from multiple backgrounds</h3>
          <p class="prose">Agency, client and strategy backgrounds.</p>
          <h3 class="plain">Pioneers / recent joiners</h3>
          <p class="prose">Portraits of people who joined recently.</p>
          <div class="cards">
            {card(h, "/about/team/advisor-one/", "Name", "Recent joiner", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Recent joiner", "person")}
            {card(h, "/about/team/advisor-one/", "Name", "Recent joiner", "person")}
          </div>
        </section>
        <section class="block">
          <h2 class="plain">Values and culture</h2>
          <div class="cards four">{values}</div>
        </section>
        <section class="block">
          <h2 class="plain">Diversity, equity and inclusion</h2>
          <p class="prose">Commitments in the hiring context.</p>
        </section>
        <section class="block">
          <h2 class="plain">Benefits</h2>
          <p class="prose">Employee benefits.</p>
        </section>
        <section class="block">
          <h2 class="plain">Application process</h2>
          {steps_html(["Application", "Interview with Partners", "Case study", "References", "Decision"])}
        </section>
        <section class="block" id="roles">
          <h2 class="plain">Roles</h2>
          <p class="prose">Reach out even if the open roles are not what you are after: <a href="{h("/contact/#work-for-us")}">Work for us</a>.</p>
          {role_toggle_html()}
          <div class="cards two">{card(h, "/careers/growth-architect/", "Growth Architect", "Location · type · actively hiring", "role")}</div>
          <span class="wf-label">All shows every role, including those not actively hiring. Full descriptions on the role page</span>
        </section>
        {closing(h, "Interested in joining the team?", "Work for us", "/contact/#work-for-us", "Our people", "/about/team/")}
"""

    if kind == "role":
        return f"""
        {hero_open()}
          <h1>Growth Architect</h1>
          <p>Location · type. Actively hiring.</p>
        </section>
        <section class="block">
          <h2 class="plain">About the role</h2>
          <p class="prose">Description, responsibilities, what we look for.</p>
        </section>
        <section class="block">
          <h2 class="plain">How to apply</h2>
          <p class="prose">Applications go through LinkedIn. <a href="{h("/careers/")}">All roles</a>.</p>
          <div class="cta" {mod("CTA pair")}><a class="btn" href="#">Apply on LinkedIn</a><a class="text" href="{h("/careers/")}">All roles</a></div>
          <span class="wf-label">Button links to the role's application page on LinkedIn (external)</span>
        </section>
"""

    if kind == "contact":
        work_with = form_html(
            [("Name", "", ""), ("Company", "", ""), ("Email", "", ""), ("Topic", "select", "Select a service"), ("Message", "tall", "")],
            "Send", h("/contact/thank-you/"),
        )
        work_for = form_html([("Name", "", ""), ("Email", "", ""), ("Message", "tall", "")], "Send", h("/contact/thank-you/"))
        return f"""
        {hero_open()}
          <h1>Contact</h1>
          <p>Tell us about your growth challenge, or about joining the team.</p>
        </section>
        <section class="block" id="work-with-us">
          <h2 class="plain">Work with us</h2>
          <p class="prose">Tell us about your growth challenge.</p>
          {work_with}
        </section>
        <section class="block" id="work-for-us">
          <h2 class="plain">Work for us</h2>
          <p class="prose">Roles, Life at Manifesto, DEI and benefits live on <a href="{h("/careers/")}">Careers</a>. Speculative applications are welcome.</p>
          {work_for}
        </section>
        <section class="block">
          <h2 class="plain">Direct contact</h2>
          <p class="prose">Email, phone, office address. Response time and confidentiality.</p>
          <h3 class="plain">The Nutshell</h3>
          <p class="prose"><a href="{h("/newsletter/")}">Sign up to The Nutshell</a>: events, thought leadership and what has caught our attention.</p>
        </section>
"""

    if kind == "thanks":
        return f"""
        {hero_open()}
          <h1>Thank you</h1>
          <p>We have your message.</p>
        </section>
        <section class="block">
          <h2 class="plain">While you wait</h2>
          <div class="cards">
            {card(h, "/services/growth-strategy/", "Growth Strategy", "Customer-led growth strategy: where to focus and how to win", "offer")}
            {card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph")}
            {card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Article", "article")}
          </div>
        </section>
"""

    if kind == "legal":
        extra = ""
        if page["url"] == "/search/":
            extra = f"""
        <section class="block">
          <h2 class="plain">Search</h2>
          {form_html([("Query", "", "")], "Search", h("/search/"))}
        </section>
        <section class="block">
          <h2 class="plain">Results</h2>
          {link_list([("Growth Strategy", h("/services/growth-strategy/"), "Service"), ("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report")])}
        </section>
        {empty_stub("No results for this query.", h("/services/"), "Browse services")}
"""
        elif page["url"] == "/newsletter/":
            extra = f"""
        <section class="block">
          <h2 class="plain">Sign up</h2>
          {form_html([("Email", "", "")], "Subscribe", h("/contact/thank-you/"))}
        </section>
"""
        elif page["url"] in {"/privacy-policy/", "/cookie-policy/", "/terms/", "/accessibility/"}:
            extra = f"""
        <section class="block">
          <h2 class="plain">Summary</h2>
          <p class="prose">Stub copy for this utility page. Legal review before launch.</p>
        </section>
"""
            if page["url"] == "/cookie-policy/":
                extra += """
        <section class="block">
          <h2 class="plain">Cookie notice</h2>
          <p class="prose">The site-wide cookie bar sits above the footer on every page. Accept links here.</p>
        </section>
"""
        return f"""
        {hero_open()}
          <h1>{page["h1"]}</h1>
          <p class="body">{page.get("blurb") or ""}</p>
        </section>
        {extra}
"""

    if kind == "notfound":
        return f"""
        {hero_open()}
          <h1>Page not found</h1>
          <p>The page you asked for is not here.</p>
          {cta_html(h, ("What we do", "/services/"), ("Our work", "/work/"), f'<a class="text" href="{h("/contact/")}">Contact</a>')}
        </section>
        <section class="block">
          <h2 class="plain">Search</h2>
          {form_html([("Query", "", "")], "Search", h("/search/"))}
        </section>
"""

    if kind == "catalogue":
        return catalogue_body(h)

    raise KeyError(kind)


def catalogue_samples(h) -> dict[str, str]:
    """One wireframe sample per component, keyed by the vocabulary name."""
    pillar = f'''<div class="pillar" style="max-width:280px">
            <h3><a class="pillar-hub" href="{h("/services/growth-strategy/")}">Growth Strategy <span class="hub-chevron" aria-hidden="true">&#8594;</span></a></h3>
            <p class="line">Where and how you grow</p>
            <ul>
              <li><a class="strand-overview" href="{h("/services/growth-strategy/")}">Overview<small>Where to grow and how to win</small></a></li>
              <li><a href="{h("/services/proposition-innovation/")}">Proposition Innovation<small>Value proposition design</small></a></li>
            </ul>
          </div>'''
    hero = f'''<div class="block hero" style="padding-top:24px;padding-bottom:24px">
            <span class="eyebrow">Eyebrow (optional)</span>
            <h1 style="font-size:24px">H1: one per page</h1>
            <p>One support line. Who this is for.</p>
            {cta_html(h)}
          </div>'''
    forms = (
        '<span class="wf-label">Work with us</span>'
        + form_html([("Name", "", ""), ("Company", "", ""), ("Email", "", ""), ("Topic", "select", "Select a service"), ("Message", "tall", "")], "Send", h("/contact/thank-you/"))
        + '<span class="wf-label" style="margin-top:18px">Work for us</span>'
        + form_html([("Name", "", ""), ("Email", "", ""), ("Message", "tall", "")], "Send", h("/contact/thank-you/"))
        + '<span class="wf-label" style="margin-top:18px">Email capture, with the one error state</span>'
        + form_html([("Email", "error", "")], "Subscribe", h("/contact/thank-you/"), '<span class="field-msg">Enter a valid email.</span>')
    )
    return {
        "Header Contact": f'<a class="btn" href="{h("/contact/")}">Contact</a>',
        "Mega-nav hub and strands": pillar,
        "Breadcrumb": f'<nav class="crumbs" aria-label="Example" style="padding:0"><ol><li><a href="{h("/")}">Home</a></li><li>Component library</li></ol></nav>',
        "Cookie bar": f'''<div class="cookie-bar">
            <span>We use cookies to run this site. <a href="{h("/cookie-policy/")}">Cookie policy</a></span>
            <button type="button" class="btn">Accept</button>
          </div>''',
        "Hero": hero,
        "CTA pair": cta_html(h),
        "Closing CTA band": f'<div class="block closing" style="padding-top:24px;padding-bottom:24px"><p>Tell us about your growth challenge</p><div class="cta"><a class="btn" href="{h("/contact/")}">Contact</a><a class="text" href="{h("/work/")}">See our work</a></div></div>',
        "Prose": '<h2 class="plain" style="font-size:18px">Heading</h2><p class="prose">One to four short paragraphs. Body copy carries the keyword language the H2 promises.</p>',
        "Metric box": metrics_html([("3x", "EBITDA return"), ("4 wks", "Data audit"), ("6 wks", "First agents")]),
        "Offer card": '<div class="cards two">' + card(h, "/services/growth-strategy/", "Growth Strategy", "Customer-led growth strategy: where to focus and how to win", "offer") + card(h, "/services/proposition-innovation/", "Proposition Innovation", "Value proposition design", "offer") + "</div>",
        "Theme card": '<div class="cards two">' + card(h, "/expertise/loyalty/", "Loyalty", "Cases and thinking", "theme") + card(h, "/expertise/pricing/", "Pricing", "Cases and thinking", "theme") + "</div>",
        "Case card": '<div class="cards two">' + card(h, "/work/dayinsure/", "Dayinsure", "One-line result", "ph") + card(h, "/work/key-group/", "Key Group", "One-line result", "ph") + "</div>",
        "Report card": '<div class="cards two">' + card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "Report", "doc") + "</div>",
        "Article card": '<div class="cards two">' + card(h, "/insights/loyalty-without-the-discount/", "Loyalty without the discount", "Article · Loyalty", "article") + "</div>",
        "Person card": '<div class="cards">' + card(h, "/about/team/advisor-one/", "Advisor name", "Former role, one line", "person") + "</div>",
        "Role card": '<div class="cards two">' + card(h, "/careers/growth-architect/", "Growth Architect", "Location · type · actively hiring", "role") + "</div>",
        "Thought leadership card": '<div class="cards two">'
        + tl_card(h, "/insights/pricing-paradox/", "The Pricing Paradox", "Short excerpt, one or two lines (placeholder)", "Growth Strategy", ("Financial services", "Pricing"), type_label="Report")
        + tl_card(h, "/work/dayinsure/", "Dayinsure", "One-line result or testimony (placeholder)", "Experience Engineering", ("Consumer", "Loyalty"))
        + "</div>",
        "Related trio": related_trio_html(
            h,
            ("Loyalty without the discount", "/insights/loyalty-without-the-discount/"),
            ("Proposition Innovation", "/services/proposition-innovation/"),
            ("The Pricing Paradox", "/insights/pricing-paradox/"),
        ),
        "Culture card": '<div class="cards two">'
        + f'<a class="card theme" {mod("Culture card")} href="{h("/about/values/")}"><strong>Value 1</strong><span>One line on what it means here (placeholder)</span></a>'
        + f'<a class="card theme" {mod("Culture card")} href="{h("/about/values/")}"><strong>Value 2</strong><span>One line on what it means here (placeholder)</span></a>'
        + "</div>",
        "Triangle tile": tri_html(h, PILLAR_TILES, '<p class="tri-line">Strategy first. Activation to deliver it. Advisors alongside.</p>'),
        "Page tag": tags_html(h, [("Loyalty", "/expertise/loyalty/"), ("Pricing", "/expertise/pricing/")]),
        "Filter bar": filter_bar(["All services", "Growth Strategy", "Experience Engineering"], on="All services", more=True),
        "Type filter tabs": type_tabs_html([("All", None), ("Reports", None), ("Articles", None), ("News and events", None)], on="All"),
        "Role toggle": role_toggle_html(),
        "Application steps": steps_html(["Application", "Interview with Partners", "Case study", "References", "Decision"]),
        "Situations list": f'''<ul class="situations" {mod("Situations list")}>
            <li><a href="{h("/services/growth-strategy/")}">We need to decide where and how to grow</a></li>
            <li><a href="{h("/services/ceo-advisory/")}">I want a sounding board I trust</a></li>
          </ul>''',
        "Row of text links": f'<div class="row-links" {mod("Row of text links")}><a href="{h("/expertise/loyalty/")}">Loyalty</a><a href="{h("/expertise/pricing/")}">Pricing</a><a href="{h("/expertise/customer-value/")}">Customer Value</a></div>',
        "Link list": link_list([("The Pricing Paradox", h("/insights/pricing-paradox/"), "Report"), ("Loyalty without the discount", h("/insights/loyalty-without-the-discount/"), "Article")]),
        "Case line": f'<p class="case-line" {mod("Case line")}>Key Group, one-line result. <a href="{h("/work/key-group/")}">Read the case study</a></p>',
        "Link line": f'<p class="one-line" {mod("Link line")}>We apply these services to the growth problems we know best. <a href="{h("/expertise/")}">Our expertise</a></p>',
        "Pagination": pagination_html(),
        "Empty state": empty_html("No case studies match these filters.", h("/work/")),
        "Logo strip": logos_html(6, "Logo"),
        "Logo band": logo_band_html(6),
        "Sticky stat rail": '<div style="max-width:280px">' + stat_rail_html(h, [("Stat TBC", "Outcome measure, with the client's words"), ("Stat TBC", "Outcome measure, with the client's words")], "Contact us", "Got a growth challenge like this one?") + "</div>",
        "Quote": quote_html(cite="Dayinsure"),
        "Video 16:9": video_html("Showreel"),
        "Testimony video": testimony_video_html(),
        "Profile pop-up": popup_html(h),
        "CIVD four-cell": civd_html(),
        "Article body": article_body(),
        "Form": forms,
    }


def catalogue_body(h) -> str:
    samples = catalogue_samples(h)
    missing = [n for n in COMPONENTS if n not in samples]
    if missing:
        raise SystemExit(f"Component library has no sample for: {missing}")
    groups = ""
    for group in COMPONENT_GROUPS:
        units = "".join(unit(n, samples[n]) for n, (g, _, _) in COMPONENTS.items() if g == group)
        groups += f"""
        <section class="block">
          <h2 class="plain">{group}</h2>{units}
        </section>"""
    # Each interaction type is drawn as a miniature of its real shape, never as a name badge.
    kinds = [
        ("Band", '<span class="spec-band" aria-hidden="true"><i></i><b></b><em></em></span>',
         "A full-width block that composes other components: Hero, Closing CTA band. Bleeds to the edge with a rule top and bottom."),
        ("Button", '<span class="btn" aria-hidden="true">Send</span>',
         "An action: Send, Accept, Clear filters, Search, header Contact, the primary of a CTA pair. Heavy 2px ink frame, light fill, verb only. Never a content-page link except header Contact."),
        ("Text link", '<span class="spec-link" aria-hidden="true">See our work</span>',
         "Navigate: See our work, All thinking, situations, breadcrumbs, footer, mega-nav strands, pagination. Underlined or plain text, never a box."),
        ("Card", '<span class="card" aria-hidden="true"><strong>Title</strong><span>Support line</span></span>',
         "Whole unit is a hit area to one destination page. Solid 1px box. Title plus support line. Seven card types, one shape each."),
        ("Tag", '<span class="page-tags" aria-hidden="true"><span>Loyalty</span><span>Pricing</span></span>',
         "Small linked label. One dimension, max three. Squared corners, quiet border. Not a filter."),
        ("Filter", '<span class="filter on" aria-hidden="true">All</span><span class="filter" aria-hidden="true">Loyalty</span>',
         "Toggle on a listing. Pill-shaped button, not a link. Selected uses a heavier border."),
        ("Static", '<span class="spec-static" aria-hidden="true">Metric</span><span aria-hidden="true" style="color:#555">Prose</span>',
         "Not clickable. Dashed box or plain text: logos, metrics, CIVD, form fields, video, quote, empty message, prose."),
    ]
    legend = "".join(
        f'<li><span class="spec">{shape}</span><span class="spec-text"><strong>{k}.</strong> {t}</span></li>'
        for k, shape, t in kinds
    )
    return f"""
        <section class="block hero" {mod("Hero")}>
          <h1>Component library</h1>
          <p>The reusable blocks every page is built from. One name, one shape, one interaction type per component. The sidebar on each page lists which of these it uses, by the same names.</p>
        </section>
        <section class="block">
          <h2 class="plain">How to read this library</h2>
          <div class="legend">
            <p class="unit-purpose">Seven interaction types. If a rectangle cannot be named from this library, it is a random box and should not be on a page.</p>
            <ul class="legend-list spec-list">{legend}</ul>
          </div>
        </section>
        {groups}
        <section class="block">
          <h2 class="plain">Do not mix</h2>
          <ul class="legend-list">
            <li>A Filter is not a Tag. Tags navigate. Filters toggle.</li>
            <li>A Tag is not a Button. Do not put tags in the header.</li>
            <li>A Triangle tile is not an Offer card. Pillar versus buyable service.</li>
            <li>A Theme card and a Role card are outline cards. An Offer card has the grey fill. An Article card has neither fill nor image.</li>
            <li>A CIVD cell is not a Card. The cells are a static diagram.</li>
            <li>A Metric box is not a Card. Numbers are not destinations.</li>
            <li>A listing link is not a Case card. Home All work is a Text link. Only real cases wear the Case card.</li>
            <li>The sidebar on each page is annotation for this wireframe. Nothing in it is a live component.</li>
          </ul>
        </section>
        {closing(h)}
"""


def service_module(page: dict, h) -> dict:
    """Per-service content for the client service template. Returns three parts:
    `help` (H3 blocks under How can we help you?), `modules` (anchored framework
    sections that keep their H2 homes, D-51) and `how` (the How it works section)."""
    url = page["url"]

    def how_section(text: str) -> str:
        return f"""
        <section class="block">
          <h2 class="plain">How it works</h2>
          <p class="prose">{text}</p>
        </section>
"""

    if url == "/services/growth-strategy/":
        return dict(
            help=f"""
          <h3 class="plain">North Star</h3>
          <p class="prose">The North Star the business will follow.</p>
          <h3 class="plain">Growth priorities</h3>
          <p class="prose">Where the bets sit.</p>
          <h3 class="plain">Demand signals</h3>
          <p class="prose">What you watch to know the strategy is working.</p>
          <h3 class="plain">Scenario planning</h3>
          <p class="prose">How the strategy holds when the market moves.</p>""",
            modules=f"""
        <section class="block" id="civd">
          <h2 class="plain">Customer, Innovation, Value and Delivery</h2>
          <p class="prose">The CIVD frame. Customer, Innovation, Value and Delivery. Next: <a href="{h("/services/proposition-innovation/")}">Proposition Innovation</a>.</p>
          {civd_html()}
          <h3 class="plain">Customer</h3>
          <p class="prose">Who you grow with.</p>
          <h3 class="plain">Innovation</h3>
          <p class="prose">What you offer next.</p>
          <h3 class="plain">Value</h3>
          <p class="prose">Where the economics move.</p>
          <h3 class="plain">Delivery</h3>
          <p class="prose">Whether it can be executed. Hands off to Activation.</p>
        </section>
""",
            how=how_section(f'Shape of a strategy engagement. Method detail: <a href="{h("/about/how-we-work/")}">Our approach</a>.'),
        )
    if url == "/services/proposition-innovation/":
        items = [
            ("Loyalty propositions", "/expertise/loyalty/"),
            ("Membership propositions", "/expertise/membership/"),
            ("Subscription propositions", "/expertise/subscriptions/"),
            ("Direct-to-consumer propositions", "/expertise/customer-value/"),
        ]
        blocks = "".join(
            f'<h3 class="plain">{n}</h3><p class="prose">How we design {n.lower()}. See <a href="{h(u)}">{n.split()[0]}</a>.</p>'
            for n, u in items
        )
        return dict(
            help=f"""
          <h3 class="plain">Value proposition design</h3>
          <p class="prose">What we do in this service, in plain words.</p>{blocks}""",
            modules="",
            how=how_section("Shape of a proposition engagement."),
        )
    if url == "/services/customer-research/":
        return dict(
            help=f"""
          <h3 class="plain">Customer research methods</h3>
          <p class="prose">Techniques, companies, and how the work is done.</p>
          <h3 class="plain">Customer journey mapping</h3>
          <p class="prose">Analytical mapping lives here. Design research lives on <a href="{h("/services/experience-engineering/#research-and-testing")}">Experience Engineering</a>.</p>
          <h3 class="plain">Research projects</h3>
          <p class="prose">Bespoke qualitative, quantitative, surveys and digital listening. The methods: digital listening, qualitative research, quantitative research, customer data analytics, internal knowledge, external market data.</p>
          <h3 class="plain">Always-on customer insight</h3>
          <p class="prose">Voice of the customer tools, panels and intelligence platforms.</p>""",
            modules="",
            how=how_section("Insight project or capability build."),
        )
    if url == "/services/experience-engineering/":
        return dict(
            help=f"""
          <h3 class="plain">Find</h3>
          <p class="prose">Audit existing performance.</p>
          <h3 class="plain">Redesign</h3>
          <p class="prose">Better journey flows, CX design and digital build.</p>
          <h3 class="plain">Test</h3>
          <p class="prose">Build and test with target audiences.</p>
          <h3 class="plain">Scale</h3>
          <p class="prose">Roll out the journeys that move value.</p>
          <div id="customer-experience">
          <h3 class="plain">Customer experience (CX) design</h3>
          <p class="prose">Customer experience design for the journeys that matter.</p>
          </div>
          <div id="website-and-digital">
          <h3 class="plain">Website and digital product</h3>
          <p class="prose">Website and digital product design, build and testing.</p>
          </div>
          <div id="research-and-testing">
          <h3 class="plain">User research and testing</h3>
          <p class="prose">Journey research for design, with customer and value analytics. <a href="{h("/services/customer-research/")}">Customer Research and Insight</a> owns analytical research.</p>
          </div>""",
            modules="",
            how=how_section("Find, Redesign, Test, Scale: the sequence an engagement runs in."),
        )
    if url == "/services/ai-agents-for-marketing/":
        return dict(
            help="""
          <p class="prose">What we do in this service, in plain words: audit the customer data, then deploy marketing and data agents from AgentLab, guided by experts.</p>""",
            modules="""
        <section class="block" id="agentlab">
          <h2 class="plain">AgentLab</h2>
          <p class="prose">Named catalogue of marketing and data agents.</p>
          <h3 class="plain">Reporting and Analytics</h3>
          <p class="prose">Effectiveness, attribution mapping, performance planning.</p>
          <h3 class="plain">Data and Infrastructure</h3>
          <p class="prose">CDP data clean-up, tagging and data collection, integration discovery.</p>
          <h3 class="plain">Strategy and Planning</h3>
          <p class="prose">Segmentation builder, customer journey mapping agent, audience opportunity.</p>
          <h3 class="plain">Automation and Execution</h3>
          <p class="prose">Channel optimisation, test and learn, QA and deployment.</p>
        </section>
""",
            how=how_section(f'4 weeks audit. 6 weeks first agents. Ongoing portfolio. <a href="{h("/services/ai-enablement/")}">AI Enablement</a> if you are earlier in the journey.'),
        )
    if url == "/services/operating-model-design/":
        return dict(
            help="""
          <h3 class="plain">Target operating model</h3>
          <p class="prose">How teams should work when they need a new operating model.</p>
          <h3 class="plain">Adaptive operating model</h3>
          <p class="prose">Grounded in customer value growth. Fuelled by high-quality data. Redesigned around humans and AI agents. Orchestrated and linked to impact.</p>""",
            modules=f"""
        <section class="block" id="operating-architecture">
          <h2 class="plain">Our Operating Architecture framework</h2>
          <h3 class="plain">High-quality data and tools</h3>
          <p class="prose">Data quality, security and governance; knowledge architecture; tech platforms; AI tools.</p>
          <h3 class="plain">New work units</h3>
          <p class="prose">Key functions, capabilities and workflows.</p>
          <h3 class="plain">Orchestration: culture, value, capability</h3>
          <p class="prose">The same three words as <a href="{h(GO_URL)}">{GO_NAME}</a>, which staffs what this page designs.</p>
        </section>
""",
            how=how_section("Diagnose the current model, design the adaptive model, implement."),
        )
    if url == GO_URL:
        return dict(
            help="""
          <h3 class="plain">Interim growth team</h3>
          <p class="prose">Lean teams of interim growth experts. Interim CMO and senior cover where the engagement needs it.</p>
          <h3 class="plain">Then embed</h3>
          <p class="prose">Establish the new ways of working required for ongoing delivery. Not a permanent outsource.</p>
          <h3 class="plain">Culture</h3>
          <p class="prose">Winning hearts and minds through engagement, proof points and AI literacy.</p>
          <h3 class="plain">Capability</h3>
          <p class="prose">Orchestrating delivery teams to build capabilities and automate priority workflows.</p>
          <h3 class="plain">Value</h3>
          <p class="prose">Tracking impact against baseline plans and course-correcting on lead indicators.</p>""",
            modules="",
            how=how_section(f'Two phases: interim activation support, then embed. <a href="{h("/services/operating-model-design/")}">Operating Model Design</a> designs; this page staffs.'),
        )
    if url == "/services/ai-enablement/":
        return dict(
            help=f"""
          <h3 class="plain">AI skills and adoption</h3>
          <p class="prose">Building the skills and tools for day-to-day AI use.</p>
          <h3 class="plain">Finding where AI pays off</h3>
          <p class="prose">Value case targeting and re-engineering key workflows.</p>
          <h3 class="plain">New business models with AI</h3>
          <p class="prose">Working with leadership to identify and qualify transformational opportunities.</p>""",
            modules="",
            how=how_section(f'Maturity assessment, then a bespoke programme. Practitioners from our expert network. Tooling: <a href="{h("/services/ai-agents-for-marketing/")}">AI Agents for Marketing</a>.'),
        )
    return dict(
        help='<p class="prose">What we do in this service, in plain words.</p>',
        modules="",
        how=how_section("Engagement shape."),
    )


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
        ("Our thinking", [p["url"] for p in PAGES if p["url"].startswith("/insights/") or p["url"] == "/newsletter/"]),
        ("About", [p["url"] for p in PAGES if p["url"].startswith("/about/")]),
        ("Careers", [p["url"] for p in PAGES if p["url"].startswith("/careers/")]),
        ("Contact", [p["url"] for p in PAGES if p["url"].startswith("/contact/")]),
        ("Utility", [p["url"] for p in PAGES if p["url"] in {"/privacy-policy/", "/cookie-policy/", "/terms/", "/accessibility/", "/search/", "/404/"}]),
        ("Wireframe tools", ["/catalogue/"]),
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
<title>Sitemap | Manifesto Growth Architects</title>
<link rel="stylesheet" href="assets/wireframe.css">
</head>
<body>
<div class="wrap" style="max-width:900px;margin:24px auto 48px;padding:0 12px">
  <p class="map-note" style="margin:0 0 16px"><a href="index.html">Home</a> · <a href="catalogue/index.html">Component library</a></p>
  <div class="sitemap">
    <ul>
      {"".join(lis)}
    </ul>
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
        "Header chrome is MURAL-informed (see `docs/mural-gap-check.md`). Mega-nav group titles are linked hubs with Overview or strand children. Buyer language sits in strand subtitles, H1 support, H2/H3s and page notes.",
        "",
        "Volumes are average monthly Google Ads search volume for the United Kingdom. Exact Manifesto product phrases are often thin; adjacent demand is the useful signal.",
        "",
        "Source of truth for structure: `docs/02-sitemap.md` and the IA report. This file is the SEO heading layer on top of that IA, not a competing sitemap.",
        "Each page also lists the reusable components on its canvas, in order, by the names in the component library (`mocks/catalogue/`).",
        "",
    ]
    for p in PAGES:
        lines.append(f"## `{p['url']}`: {p['title']}")
        lines.append("")
        lines.append(f"- **Template:** {KIND_LABELS[p['kind']]}")
        lines.append(f"- **Weight:** {p['weight']} ({WEIGHT_GLOSS[p['weight']]})")
        lines.append(f"- **Primary keyword:** {p.get('primary') or 'none'}")
        if p.get("quiet"):
            lines.append(f"- **Menu subtitle:** {p['quiet']}")
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
        if p.get("notes"):
            lines.append("- **Content notes:**")
            for n in p["notes"]:
                lines.append(f"  - {n}")
        if p.get("_components"):
            lines.append("- **Components (canvas order):**")
            for names, ctx in p["_components"]:
                lines.append(f"  - {names}" + (f" ({ctx})" if ctx else ""))
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
        body = body_for(page)
        if page["kind"] == "catalogue":
            component_inventory(body)  # validates the library's own samples
        dest.write_text(wrap(page, body), encoding="utf-8")
        print("wrote", dest.relative_to(ROOT))


def check_vocabulary() -> None:
    """Every named component appears on at least one page or in the chrome."""
    used = {n for p in PAGES for names, _ in p.get("_components") or [] for n in names.split(", ")}
    used = {n.split(" \u00d7")[0] for n in used}
    unused = [n for n, (g, _, _) in COMPONENTS.items() if g != "Chrome" and n not in used]
    if unused:
        print("note: in the library but on no page:", ", ".join(unused))
    banned = ["chip", "MURAL", "previous build", "not at the top", "banner up", "Canonical<", "Value Orchestration", "value-orchestration", "value orchestration"]
    for path in MOCKS.rglob("index.html"):
        text = path.read_text(encoding="utf-8")
        for b in banned:
            if b in text:
                raise SystemExit(f"Banned wording {b!r} in {path.relative_to(ROOT)}")


def write_redirects() -> None:
    """Cloudflare Pages alias: the retired 15 Oct name's URL lands on the
    working name's page (see GO_NAME). One source, regenerated with the site."""
    lines = f"{GO_ALIAS_URL} {GO_URL} 301\n{GO_ALIAS_URL.rstrip('/')} {GO_URL} 301\n"
    (MOCKS / "_redirects").write_text(lines, encoding="utf-8")
    print("wrote", (MOCKS / "_redirects").relative_to(ROOT))


if __name__ == "__main__":
    write_pages()
    write_sitemap_html()
    write_heading_map_md()
    write_redirects()
    check_vocabulary()
    print(f"pages: {len(PAGES)}")
