# Findings from the branded first pass

What came up while applying the brand to the wireframes. Each item says what the problem is, a suggested fix, and who needs to decide. Items are grouped: things that will break or confuse first, then judgement calls, then small loose ends.

The short version: the brand holds up well on the web. The two core colours, Anton plus Plex, square corners and the isometric language translate into a clean, confident consultancy look without much fighting. The real gaps are the ones the guidelines never had to answer in print: colour contrast for text, a type scale, interactive states, and a couple of places where the wireframes and the brand rules point in different directions.

---

## Problems and conflicts

### 1. Manifesto Green fails as text on white, and white fails as text on green
Green (#b7e226) on white has a contrast ratio of about 1.5:1; accessibility rules need 4.5:1 for body text. White text on a green button fails the same way. The brand pack already hints at this ("green works best as a fill"), and this build follows it strictly: green is only ever a fill with Slate text on it, or an accent on Slate backgrounds. But this means no green links, no green headings on white pages, which may surprise anyone expecting the site to read "greener" than the mocks.
**Fix:** keep the rule as implemented. If more green is wanted on light pages, use it as blocks, rules and fills, not text.
**Decision:** none needed if everyone is happy with how the preview looks; worth Bruno confirming he will design within this constraint.

### 2. The wires describe the thought leadership card with a "rounded frame", the brand says square corners everywhere
The brand's isometric system and button style are emphatically square. A rounded card would be the only rounded thing on the site. This build sets every radius to 0, including that card and the filter pills (drawn as rounded pills in the wires, built square here).
**Fix:** accept square corners site-wide, or carve out a deliberate exception for pills/tags only.
**Decision:** Bruno, with Gary's sign-off since it changes how the wires read.

### 3. Anton becomes illegible at small sizes
Anton is a condensed display face. Below roughly 24px it turns into a wall of strokes, so it cannot be used for card titles, H3s or UI labels. This build uses Anton only for H1, H2 and large standalone numbers; everything smaller is IBM Plex Sans semibold. The brand pack says "headlines and caption headers" but never defines where headlines stop.
**Fix:** adopt the rule in this build: Anton at 28px and above only.
**Decision:** Dan (brand) and Bruno (how far down the hierarchy Anton goes).

### 4. Six nav items plus a button do not fit between 768px and ~1080px
With uppercase, wide-tracked labels, the header overflows well above tablet width. This build switches to the mobile menu below 1080px, which means iPads in portrait get the burger menu.
**Fix:** either accept the 1080px breakpoint, shorten a label or two, or reduce letter-spacing in the nav.
**Decision:** Bruno, flagging to Gary that tablets see the mobile menu.

### 5. The isometric backgrounds are too busy to put text straight onto
The 2400px pattern renders are lively; headline text sitting directly on them fails contrast in patches. This build adds a dark gradient scrim over hero backgrounds, heaviest at the text side. That slightly mutes the pattern.
**Fix:** keep the scrim, or have Bruno produce calmer "web hero" variants of the backgrounds with built-in quiet zones.
**Decision:** Bruno.

### 6. The two-tone logo is only safe on Slate
The brand pack is explicit that the two-colour logo only works on dark grey. The header and footer here are Slate so this is fine, but it locks the header to dark for good. A future light header would need the all-Slate logo and a different nav treatment.
**Fix:** none needed now; record it as a constraint.
**Decision:** none.

### 7. Discrepancy in the turquoise secondary colour
The brand PDF prints the turquoise as #39bc9e in one place and gives RGB values that compute to #39be9e in another. Trivial, but one of them is wrong in the master document.
**Fix:** Dan to confirm the correct hex and correct the pack.
**Decision:** Dan.

### 8. Logo files were extracted from the PDF, not supplied as master artwork
The SVGs in this build were rebuilt from the brand pack. They look right, but clear space and minimum size are not specified anywhere, and production should use Dan's master files.
**Fix:** Dan to supply master SVG/EPS artwork plus clear-space and minimum-size rules.
**Decision:** Dan.

### 9. Dan's toolkit page 15 web mock has outdated navigation labels
The nav in the toolkit render does not match the agreed wires (it predates the Mural pass). This build follows the wires, as briefed, but anyone comparing the preview to the toolkit will see a mismatch.
**Fix:** tell Dan so the toolkit mock does not get treated as a nav spec.
**Decision:** none, just communication.

---

## Judgement calls made in this build (proposals, not guidelines)

These are places where the brand pack is silent. Each is implemented as a concrete proposal so there is something to react to; all are easy to change.

### 10. Type scale, spacing and grid
Proposed: a fluid type scale (H1 ~76px at 1440 down to 40px on mobile, matching the proportions of Dan's p15 mock), an 8px spacing scale, 1240px max content width, 12-column behaviour via CSS grid. Documented in `/branded/catalogue/`.
**Decision:** Bruno to adopt, adjust or replace.

### 11. Button, link and focus states
Proposed: primary button is green fill with Slate text, hover inverts to Slate fill with white text (white fill with Slate text on dark grounds); square corners; a solid offset "slab" shadow on hover echoing the isometric extrusion instead of a soft blur; visible focus rings (Slate on light, Green on dark) on everything. All shown with forced states in the catalogue.
**Decision:** Bruno.

### 12. The two-tone headline rule is undefined
Slate-page heroes set the H1 in white with one line in green (as in the toolkit mock), but nothing says which line goes green. This build greens the final line/phrase.
**Fix:** Dan to state the rule (emphasis word? last line? editor's choice?).
**Decision:** Dan.

### 13. Secondary palette is barely used
Plum, turquoise, orange and the rest appear nowhere in these templates except the catalogue swatches. The brand says "sparingly"; the proposal is to reserve them for infographics, charts and report covers, keeping pages to Slate/Green/Clay/Stone.
**Decision:** Bruno.

### 14. No icon set exists
The brand pack ships no icons. This build uses text glyphs and simple geometric shapes (the hexagon bullet, arrows). A real site needs a small icon set drawn to the 90/30 isometric language.
**Fix:** Bruno to draw one.
**Decision:** Bruno.

### 15. Cookie notice placement
The wires show the cookie notice inline; this build makes it a fixed bottom bar so it is visible on long pages without pushing content.
**Decision:** Bruno/Gary, minor.

### 16. Report gate
The report template includes a working email gate as drawn in the wires. Whether reports are actually gated (and what the data capture promise is) is a business decision, and affects the template's prominence.
**Decision:** Gary.

### 17. Mega-nav footer row
The wires give the mega-nav footer three links (All services, Expertise, Our work); the build brief mentioned only two. This build follows the wires.
**Decision:** Gary, trivial.

### 18. Client logo band
The auto-scrolling logo band uses placeholder marks. Real client logos will arrive in mixed colours and shapes; the brand treatment (all-white? all-Slate? contained in tiles?) is undefined and makes a big difference to how calm that band feels.
**Fix:** propose single-colour (Clay on Slate, or Slate on Stone) logo treatments.
**Decision:** Bruno, with Gary checking clients permit recolouring.

---

## Loose ends

19. **Imagery:** the green top-left overlay is implemented as a CSS gradient on placeholders. It behaves well, but the rule ("a touch of green radiating from the top left") needs a strength spec before real photography arrives, or every image will be treated differently. Dan/Bruno.
20. **Fonts:** IBM Plex Sans is self-hosted as a subsetted variable font (~230KB per style). Fine for launch; worth a check that the OFL licence note ships with the site (it is included in `branded/assets/fonts/`). None.
21. **Stubs:** 35 of the 46 URLs are unskinned stubs that link back to their greyscale wireframe. Anyone clicking around the preview will hit them; this is intentional so no internal link is broken, but worth saying in the demo so it does not read as broken. None.
22. **Working name "Growth Office":** the client renamed Value Orchestration to Growth Office (October 2026) and warned it may change again. The preview applies the new name everywhere, including the `/services/growth-office/` URL, through a single build-time mapping so the next rename is trivial. The greyscale wires still use the old name until main gets the same revert; the cross-links between the two builds handle this. Once the name settles, Gary should confirm it and the wires and preview should be reconciled. Gary.
