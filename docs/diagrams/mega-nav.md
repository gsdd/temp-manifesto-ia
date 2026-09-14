# Diagram: header and What we do mega-nav (v2)

Mermaid source. Renders in GitHub, GitLab and most markdown previewers. The authoritative description is `../01-primary-navigation.md`; if the two disagree, the document wins.

## Header

```mermaid
flowchart LR
    Logo["MGA logo → /"]
    WWD["What we do (mega-nav) → /services/"]
    Work["Our work (plain link) → /work/"]
    Insights["Insights (dropdown) → /insights/"]
    About["About (dropdown) → /about/"]
    Contact["Contact (button) → /contact/"]
    Logo --- WWD --- Work --- Insights --- About --- Contact
```

## What we do mega-nav: the triangle, three columns

```mermaid
flowchart TB
    Head["Our Growth Architecture → /services/<br/>Strategy that works. Execution that delivers."]

    subgraph Panel["What we do: mega-nav panel"]
        direction LR

        subgraph C1["Growth Strategy<br/>Where to play and how to win. Our core offer."]
            direction TB
            C1a["Growth Strategy → /services/growth-strategy/"]
            C1b["Proposition Innovation → /services/proposition-innovation/"]
            C1a --> C1b
        end

        subgraph C2["Activation Services<br/>The bridge from strategy to execution."]
            direction TB
            C2a["Customer Intelligence → /services/customer-intelligence/"]
            C2b["Experience Engineering → /services/experience-engineering/"]
            C2c["Data Agents → /services/data-agents/"]
            C2d["Operating Architecture → /services/operating-architecture/"]
            C2e["Growth Office → /services/growth-office/"]
            C2f["AI Enablement → /services/ai-enablement/"]
            C2a --> C2b --> C2c --> C2d --> C2e --> C2f
        end

        subgraph C3["CEO Advisory (quieter)<br/>Side-by-Side: support for senior leaders"]
            direction TB
            C3a["Side-by-Side (SxS) → /services/ceo-advisory/"]
            C3b["Meet the advisors → /about/team/#advisors"]
            C3a --> C3b
        end
    end

    subgraph Row["Footer row (one thin line)"]
        direction LR
        R1["All services → /services/"]
        R2["Expertise themes → /expertise/"]
        R3["Contact → /contact/"]
        R1 --- R2 --- R3
    end

    Head --> Panel --> Row
```

Column headings link to the pillar pages: Growth Strategy → `/services/growth-strategy/`, Activation Services → `/services/activation/`, CEO Advisory → `/services/ceo-advisory/`.

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

## Insights dropdown

```mermaid
flowchart LR
    subgraph I1["Insights"]
        direction TB
        I1a["Latest insights → /insights/"]
        I1b["Reports and guides → /insights/?type=report"]
        I1c["Events → /insights/?type=event"]
        I1a --> I1b --> I1c
    end
    subgraph I2["Expertise themes"]
        direction TB
        I2h["All themes → /expertise/"]
        I2a["Loyalty → /expertise/loyalty/"]
        I2b["Membership → /expertise/membership/"]
        I2c["Subscriptions → /expertise/subscriptions/"]
        I2d["Pricing → /expertise/pricing/"]
        I2e["Customer Value → /expertise/customer-value/"]
        I2h --> I2a --> I2b --> I2c --> I2d --> I2e
    end
```

## About dropdown

```mermaid
flowchart TB
    A1["About Manifesto → /about/"]
    A2["Our team → /about/team/"]
    A3["How we work → /about/how-we-work/"]
    A4["Values and culture → /about/values/"]
    A5["Careers → /careers/"]
    A1 --> A2 --> A3 --> A4 --> A5
```

## Mobile menu (collapsed header)

```mermaid
flowchart TB
    M["Menu (full-screen panel)"]
    M --> M1["What we do (accordion): Our Growth Architecture"]
    M1 --> M1a["Growth Strategy (open by default): 2 links"]
    M1 --> M1b["Activation Services (closed): 6 links with subtitles"]
    M1 --> M1c["CEO Advisory (closed, quieter): 2 links"]
    M1 --> M1d["All services / Expertise themes"]
    M --> M2["Our work (plain link)"]
    M --> M3["Insights (accordion): 3 links, then 5 theme links"]
    M --> M4["About (accordion): About, Team, How we work, Values, Careers"]
    M --> M5["Contact (link, also pinned button)"]
    M --> M6["Who we work with: 4 sector links (quiet)"]
```

## Footer

```mermaid
flowchart LR
    subgraph F1["What we do"]
        direction TB
        F1a["8 services, CEO Advisory: Side-by-Side, All services"]
    end
    subgraph F2["Expertise themes"]
        direction TB
        F2a["Loyalty, Membership, Subscriptions, Pricing, Customer Value"]
    end
    subgraph F3["Who we work with"]
        direction TB
        F3a["Financial services, Media, Consumer, Retail"]
    end
    subgraph F4["Company"]
        direction TB
        F4a["About, Our team, How we work, Values and culture, Careers, Our work, Insights, Newsletter, Contact"]
    end
```
