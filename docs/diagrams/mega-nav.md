# Diagram: header and What we do mega-nav

Mermaid source. Renders in GitHub, GitLab and most markdown previewers. The authoritative description is `../01-primary-navigation.md`; if the two disagree, the document wins.

## Header

```mermaid
flowchart LR
    Logo["MGA logo → /"]
    WWD["What we do (mega-nav) → /services/"]
    Work["Our work (dropdown) → /work/"]
    Insights["Insights (dropdown) → /insights/"]
    About["About (dropdown) → /about/"]
    Contact["Contact (button) → /contact/"]
    Logo --- WWD --- Work --- Insights --- About --- Contact
```

## What we do mega-nav

```mermaid
flowchart TB
    subgraph MegaNav["What we do: mega-nav panel"]
        direction LR

        subgraph C1["Column 1: Growth Strategy"]
            direction TB
            C1H["Growth Strategy (heading) → /services/growth-strategy/"]
            C1a["Growth Strategy → /services/growth-strategy/"]
            C1b["Proposition Innovation → /services/proposition-innovation/"]
            C1H --> C1a --> C1b
        end

        subgraph C2["Column 2: Activation Services"]
            direction TB
            C2H["Activation Services (heading) → /services/activation/"]
            C2a["Customer Intelligence → /services/customer-intelligence/"]
            C2b["Experience Engineering → /services/experience-engineering/"]
            C2c["Data Agents (AgentLab) → /services/data-agents/"]
            C2d["Operating Architecture → /services/operating-architecture/"]
            C2e["Growth Office → /services/growth-office/"]
            C2f["AI Enablement → /services/ai-enablement/"]
            C2H --> C2a --> C2b --> C2c --> C2d --> C2e --> C2f
        end

        subgraph C3["Column 3: Expertise"]
            direction TB
            C3H["Expertise (heading) → /expertise/"]
            C3a["Loyalty → /expertise/loyalty/"]
            C3b["Membership → /expertise/membership/"]
            C3c["Subscriptions → /expertise/subscriptions/"]
            C3d["Pricing → /expertise/pricing/"]
            C3e["Customer Value → /expertise/customer-value/"]
            C3H --> C3a --> C3b --> C3c --> C3d --> C3e
        end

        subgraph C4["Column 4: Featured"]
            direction TB
            C4a["Featured case study card → /work/{client}/"]
            C4b["How we work → /about/how-we-work/"]
            C4c["Talk to us → /contact/"]
            C4a --> C4b --> C4c
        end
    end

    subgraph Strip["Bottom strip (quieter)"]
        direction LR
        S1["All services → /services/"]
        S2["CEO Advisory: Side-by-Side → /services/ceo-advisory/"]
        S3["Who we work with → /sectors/"]
        S1 --- S2 --- S3
    end

    MegaNav --> Strip
```

## Our work dropdown

```mermaid
flowchart TB
    W0["All work → /work/"]
    subgraph WS["By service"]
        WS1["Growth Strategy → /work/?service=growth-strategy"]
        WS2["Activation → /work/?service=activation"]
    end
    subgraph WE["By expertise (max 3)"]
        WE1["Loyalty → /work/?expertise=loyalty"]
        WE2["Subscriptions → /work/?expertise=subscriptions"]
        WE3["Pricing → /work/?expertise=pricing"]
    end
    subgraph WSec["By sector"]
        WSec1["Financial services → /work/?sector=financial-services"]
        WSec2["Media → /work/?sector=media"]
        WSec3["Consumer → /work/?sector=consumer"]
        WSec4["Retail → /work/?sector=retail"]
    end
    W0 --> WS --> WE --> WSec
```

## Insights dropdown

```mermaid
flowchart LR
    subgraph IB["Column 1: Browse"]
        direction TB
        IB1["Latest insights → /insights/"]
        IB2["Articles → /insights/?type=article"]
        IB3["Reports and guides → /insights/?type=report"]
        IB4["Events and webinars → /insights/?type=event"]
        IB5["Newsletter → /newsletter/"]
        IB1 --> IB2 --> IB3 --> IB4 --> IB5
    end
    subgraph IT["Column 2: By theme"]
        direction TB
        ITH["Explore our expertise → /expertise/"]
        IT1["Loyalty"]
        IT2["Membership"]
        IT3["Subscriptions"]
        IT4["Pricing"]
        IT5["Customer Value"]
        ITH --> IT1 --> IT2 --> IT3 --> IT4 --> IT5
    end
```

## About dropdown

```mermaid
flowchart TB
    A1["About Manifesto → /about/"]
    A2["Our team → /about/team/"]
    A3["How we work → /about/how-we-work/"]
    A4["Careers → /about/careers/"]
    A1 --> A2 --> A3 --> A4
```

## Mobile menu (collapsed header)

```mermaid
flowchart TB
    M["Menu (full-screen panel)"]
    M --> M1["What we do (accordion)"]
    M1 --> M1a["Growth Strategy (open by default): 2 links"]
    M1 --> M1b["Activation Services (closed): 6 links"]
    M1 --> M1c["Expertise (closed): 5 links"]
    M1 --> M1d["All services / CEO Advisory: Side-by-Side"]
    M --> M2["Our work (link + filter list)"]
    M --> M3["Insights (link + type list)"]
    M --> M4["About (accordion): About, Team, How we work, Careers"]
    M --> M5["Contact (link, also pinned button)"]
    M --> M6["Who we work with: 4 sector links (quiet)"]
```
