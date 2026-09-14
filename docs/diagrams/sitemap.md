# Diagram: sitemap (v2)

Mermaid source. The authoritative list is `../02-sitemap.md`; if the two disagree, the document wins.

Legend for node styling: Canonical pages are bold-bordered, Supporting pages normal, Light pages dashed, Utility pages grey.

## Full sitemap tree

```mermaid
flowchart TB
    classDef canonical stroke-width:3px
    classDef supporting stroke-width:1px
    classDef light stroke-dasharray: 5 5
    classDef utility fill:#eeeeee,stroke:#999999,color:#555555

    Home["/ Home"]:::canonical

    %% Services: the triangle
    Home --> S["/services/ What we do: Growth Architecture"]:::canonical
    S --> S1["/services/growth-strategy/ (pillar 1 and lead service)"]:::canonical
    S1 --> S2["/services/proposition-innovation/"]:::canonical
    S --> SA["/services/activation/ (pillar 2, group page)"]:::supporting
    SA --> S3["/services/customer-intelligence/"]:::canonical
    SA --> S4["/services/experience-engineering/"]:::canonical
    SA --> S5["/services/data-agents/"]:::canonical
    SA --> S6["/services/operating-architecture/"]:::canonical
    SA --> S7["/services/growth-office/"]:::canonical
    SA --> S8["/services/ai-enablement/"]:::canonical
    S --> S9["/services/ceo-advisory/ (pillar 3, Side-by-Side)"]:::supporting

    %% Expertise
    Home --> E["/expertise/ Hub"]:::supporting
    E --> E1["/expertise/loyalty/"]:::supporting
    E --> E2["/expertise/membership/"]:::supporting
    E --> E3["/expertise/subscriptions/"]:::supporting
    E --> E4["/expertise/pricing/"]:::supporting
    E --> E5["/expertise/customer-value/"]:::supporting

    %% Sectors
    Home --> Sec["/sectors/ Index"]:::light
    Sec --> Sec1["/sectors/financial-services/"]:::light
    Sec --> Sec2["/sectors/media/"]:::light
    Sec --> Sec3["/sectors/consumer/"]:::light
    Sec --> Sec4["/sectors/retail/"]:::light

    %% Work
    Home --> W["/work/ Hub, filterable"]:::canonical
    W --> W1["/work/{client}/ Case study (n)"]:::supporting
    W --> Wf["/work/?service= ?expertise= ?sector= (noindex)"]:::utility

    %% Insights
    Home --> I["/insights/ Hub, filterable"]:::supporting
    I --> I1["/insights/{slug}/ Article, report, event (n)"]:::supporting
    I --> If["/insights/?type= ?expertise= (noindex)"]:::utility
    Home --> N["/newsletter/"]:::utility

    %% About
    Home --> A["/about/"]:::supporting
    A --> A1["/about/team/"]:::supporting
    A1 --> A1a["/about/team/{name}/ Profile (n), advisors flagged"]:::light
    A --> A2["/about/how-we-work/ Methodology"]:::supporting
    A --> A3["/about/values/ Values, culture, DEI"]:::light

    %% Careers
    Home --> Car["/careers/ Hub"]:::light
    Car --> Car1["/careers/{role}/ (n)"]:::light

    %% Contact
    Home --> C["/contact/"]:::utility
    C --> C1["/contact/thank-you/ (noindex)"]:::utility

    %% Utility
    Home --> U["Legal: /privacy-policy/ /cookie-policy/ /terms/ /accessibility/"]:::utility
    Home --> U2["/search/ /404/ /sitemap.xml /robots.txt"]:::utility
```

Notes:
- Proposition Innovation and the six Activation services are shown under their pillar for readability. All service URLs are flat under `/services/` (see D-12 in `../06-decisions-log.md`).
- Home is a page with no child URLs. The arrows from Home show top-level sections, not parent-child paths.

## The three dimensions and how they intersect

```mermaid
flowchart LR
    subgraph Services["Services: the triangle (Canonical spine)"]
        direction TB
        subgraph P1["Growth Strategy"]
            GS["Growth Strategy"]
            PI["Proposition Innovation"]
        end
        subgraph P2["Activation Services"]
            CI["Customer Intelligence"]
            EE["Experience Engineering"]
            DA["Data Agents"]
            OA["Operating Architecture"]
            GO["Growth Office"]
            AI["AI Enablement"]
        end
        subgraph P3["CEO Advisory"]
            SxS["Side-by-Side"]
        end
    end

    subgraph Themes["Expertise themes (Supporting)"]
        L["Loyalty"]
        M["Membership"]
        Sub["Subscriptions"]
        P["Pricing"]
        CV["Customer Value"]
    end

    subgraph Sectors["Sectors (Light)"]
        FS["Financial services"]
        Med["Media"]
        Con["Consumer"]
        Ret["Retail"]
    end

    Proof["Case studies and insights (tagged to all three)"]
    Advisors["Advisor profiles (/about/team/)"]

    Themes -- "Where we help: links to" --> Services
    Sectors -- "Services most used here: auto links to" --> Services
    Proof -- "surfaces on" --> Services
    Proof -- "surfaces on" --> Themes
    Proof -- "surfaces on" --> Sectors
    Advisors -- "surface on" --> P3
```

Reading the diagram: content flows one way. Themes and sectors point into services. Proof (case studies and insights) is tagged with services, themes and sectors and appears automatically on all three. Advisor profiles are the substance behind the CEO Advisory pillar. Services never point "down" into a theme-specific or sector-specific copy of themselves, because none exist.

## Visitor journey the IA is built around

```mermaid
flowchart LR
    Q1["1. What can you do?"] --> Services["/services/ (the triangle)"]
    Q2["2. Do you understand my problem?"] --> Themes["/expertise/…"]
    Q3["3. Businesses like mine?"] --> Sectors["/sectors/… (light)"]
    Q4["4. Prove it"] --> Work["/work/… and /insights/…"]
    Services --> Work
    Themes --> Services
    Themes --> Work
    Sectors --> Work
    Work --> Contact["/contact/"]
```
