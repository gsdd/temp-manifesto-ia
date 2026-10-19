# Branded preview

A first-pass branded skin of the key templates from the greyscale wireframes in `mocks/`. This is a preview exploration, not the source of truth: the wires remain the IA reference, and no wires file is modified.

This folder lives inside `mocks/` because `mocks/` is the Cloudflare Pages output directory: only files under it are deployed. The wires serve at the site root and this preview at `/branded/`. Everything here is additive; deleting `mocks/branded/` restores the repo to the wires alone.

- Live preview (branch build): `https://preview-branded-templates.temp-manifesto-ia.pages.dev/branded/`
- Findings and open decisions: [`FINDINGS.md`](FINDINGS.md) — read this first.
- Branded component library: [`/branded/catalogue/`](catalogue/index.html)

## What is built

Eleven full templates: Home, What we do hub, Service page (Experience Engineering), Our work index, two case studies (Dayinsure with the sticky stat rail, Key Group), Our thinking hub with working filters, Article, Report (with gate), Careers, and the component catalogue. The remaining 35 URLs are stubs that link to their greyscale wireframe so no internal link breaks.

Behaviours are real, not mocked: mega-nav and dropdowns (keyboard accessible, Esc closes), condensing sticky header, full mobile menu with accordions and a focus trap, insight and work filters with deep links, auto-scrolling logo band (pauses on hover, respects reduced motion), sticky stat rail, profile pop-up as an accessible dialog, related case study carousel, report gate.

## How to build

```
python3 mocks/branded/_build.py
```

No dependencies beyond Python 3. The script imports `mocks/_build.py` for all page data, navigation labels and copy, so the branded pages cannot drift from the wires. Generated HTML is committed, as with the wires.

## Structure

- `_build.py` - static site generator; imports the wireframe builder for content
- `assets/brand.css` - the single shared stylesheet: tokens, type, components
- `assets/brand.js` - all behaviour, dependency-free
- `assets/fonts/` - self-hosted Anton and IBM Plex Sans (variable), with OFL licences
- `assets/logos/`, `assets/img/` - artwork from the brand pack

## Working names

The service the wires call "Value Orchestration" is shown here as "Growth Office" at the client's request (October 2026). It is a working name and may change again, so it is implemented as a single mapping (`WORKING_NAMES` in `_build.py`) applied at build time; the build source keeps mirroring the wires, and links into the greyscale wireframes keep the wires' own naming. A future rename is a one-line change plus a rebuild.

## Guideline vs proposal

Everything taken from the brand pack (palette, Anton/Plex roles, square corners, green-as-fill rule, isometric backgrounds, image overlay) is applied as specified. Where the pack is silent - type scale, spacing, grid, button/link/focus states, breakpoints - this build defines a sensible system and documents it in the catalogue as a proposal for Bruno to adopt or replace. The split is itemised in `FINDINGS.md`.
