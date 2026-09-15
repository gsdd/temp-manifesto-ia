# Diagram: header and What we do mega-nav (v4)

Mermaid source. Renders in GitHub, GitLab and most markdown previewers. The authoritative description is `../01-primary-navigation.md`; if the two disagree, the document wins.

## Header

```mermaid
flowchart LR
    Logo["MGA logo → /"]
    WWD["What we do (mega-nav) → /services/"]
    Work["Our work → /work/"]
    Insights["Insights → /insights/"]
    About["About (dropdown) → /about/"]
    Contact["Contact (button) → /contact/"]
    Logo --- WWD --- Work --- Insights --- About --- Contact
```

One mega-nav, one small dropdown. Our work and Insights are plain links.

## What we do mega-nav: the triangle, three columns, labels only

```mermaid
flowchart TB
    subgraph Panel["What we do: mega-nav panel"]
        direction LR

        subgraph C1["Growth Strategy → /services/growth-strategy/<br/><i>Where and how you grow</i>"]
            direction TB
            C1a["Proposition Innovation → /services/proposition-innovation/"]
        end

        subgraph C2["Activation Services → /services/activation/<br/><i>Turning strategy into results</i>"]
            direction TB
            C2a["Customer Research and Insight → /services/customer-research/"]
            C2b["Experience Engineering → /services/experience-engineering/<br/><i>Customer experience and websites</i>"]
            C2c["AI Agents for Marketing → /services/ai-agents-for-marketing/"]
            C2d["Operating Model Design → /services/operating-model-design/"]
            C2e["Growth Office → /services/growth-office/<br/><i>Interim growth team</i>"]
            C2f["AI Enablement → /services/ai-enablement/"]
            C2a --> C2b --> C2c --> C2d --> C2e --> C2f
        end

        subgraph C3["CEO Advisory (quieter) → /services/ceo-advisory/<br/><i>One-to-one advice for senior leaders</i>"]
            direction TB
            C3a["(no items: the heading is the link)"]
        end
    end

    subgraph Row["Footer row (one thin line)"]
        direction LR
        R1["All services → /services/"]
        R2["Expertise → /expertise/"]
        R3["Contact → /contact/"]
        R1 --- R2 --- R3
    end

    Panel --> Row
```

Column headings are the pillar links. Italic lines under the headings are the three pillar lines; the two italic lines under Experience Engineering and Growth Office are the only item-level text in the panel. There is no heading line above the columns. 13 links, 12 destinations, about 45 words. See `../v4-simplification.md` for what was removed from v3.

## The triangle as Andy draws it (Source B) and how it maps to the nav

```mermaid
flowchart TB
    T1["CEO Advisory<br/>(top of the triangle; newest; quietest in the nav)"]
    T2["Growth Strategy<br/>(middle; bread and butter; first in the nav)"]
    T3["Activation Services<br/>(base; six services; second in the nav)"]
    T1 --> T2 --> T3
    T2 -. "column 1" .-> N1["Mega-nav column 1"]
    T3 -. "column 2" .-> N2["Mega-nav column 2"]
    T1 -. "column 3" .-> N3["Mega-nav column 3"]
```

## About dropdown

```mermaid
flowchart TB
    A1["Our team → /about/team/"]
    A2["How we work → /about/how-we-work/"]
    A3["Values and culture → /about/values/"]
    A4["Careers → /careers/"]
    A1 --> A2 --> A3 --> A4
```

Clicking About itself goes to `/about/`.

## Mobile menu (collapsed header)

```mermaid
flowchart TB
    M["Menu (full-screen panel)"]
    M --> M1["What we do (expands; open by default)"]
    M1 --> M1a["Growth Strategy (small label, link): Proposition Innovation"]
    M1 --> M1b["Activation Services (small label, link): 6 services, two quiet lines"]
    M1 --> M1c["CEO Advisory (small label, link, quieter)"]
    M1 --> M1d["All services / Expertise"]
    M --> M2["Our work"]
    M --> M3["Insights"]
    M --> M4["About (expands): Our team, How we work, Values and culture, Careers"]
    M --> M5["Contact (also the pinned button)"]
```

Two levels deep. No pillar sub-accordions and no sectors block; sectors are in the page footer.

## Footer

```mermaid
flowchart LR
    subgraph F1["What we do"]
        direction TB
        F1a["Growth Strategy, Proposition Innovation, Customer Research and Insight, Experience Engineering, AI Agents for Marketing, Operating Model Design, Growth Office, AI Enablement, CEO Advisory, All services"]
    end
    subgraph F2["Expertise"]
        direction TB
        F2a["Loyalty, Membership, Subscriptions, Pricing, Customer Value"]
    end
    subgraph F3["Who we work with (heading is plain text)"]
        direction TB
        F3a["Financial services, Media, Consumer, Retail"]
    end
    subgraph F4["Company"]
        direction TB
        F4a["About, Our team, How we work, Values and culture, Careers, Our work, Insights, Newsletter, Contact"]
    end
```
