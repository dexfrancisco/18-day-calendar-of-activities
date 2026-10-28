# UI/UX

> Status: Verified from repository HTML/CSS files (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`) on 2026-10-28.

## Design approach
- **Product context and target users:** Large-format print poster (A3 Landscape) and 2-page handout/bulletin (A4 Portrait) for the City Government of Cauayan, Isabela's 18-Day Orange Campaign to End VAWC (`Nov 25 – Dec 12, 2026`). Read by LGU officials, 65 barangay teams, partner agencies, and citizens.
- **Core user tasks and information hierarchy:**
  1. Immediately identify the campaign title, date span, city, and overarching theme.
  2. Understand the 4 core campaign pillars (Coverage, Convergence Partners, Focus Areas, Integrated Platforms).
  3. Scan chronologically by Month (`NOVEMBER 2026`, `DECEMBER 2026`) and Day (`PRE-CAMPAIGN`, `DAY 1`–`DAY 18`) to locate specific dates, weekdays, Lead Offices, Activities, Partners, and Venues.
- **Desired visual direction and rationale:** High-contrast institutional campaign poster design centered on the official VAWC "Orange Campaign" identity, pairing deep forest-green display typography (`#0b3b2e`) and vibrant orange script/accents (`#ea580c`) with color-coded semantic boxes inside each day card so dense multi-activity schedules remain scannable at a glance.
- **Patterns to avoid and why:**
  - Avoid uniform equal-width columns across rows that mix 5-activity days with single-activity or Sunday online-advocacy days; proportional column widths (`fr`) are required so dense cards do not overflow or clip.
  - Avoid shrinking fonts below legibility thresholds on print canvases or introducing scrollbars (`overflow: hidden` is enforced on `.calendar-canvas` and `.page-canvas`).

## Component library
- **Actual library and version, if verified:** Custom vanilla CSS3 component system embedded in each HTML file (`<style>`), paired with inline SVG icons (`viewBox="0 0 24 24"` and `viewBox="0 0 16 16"`). No external CSS framework (no Tailwind/Bootstrap/shadcn).
- **Existing components to reuse:**
  - `.calendar-canvas` (A3) / `.page-canvas` (A4) with `.canvas-border` (double orange/peach rounded frame)
  - `.header-container` / `.title-block` (`.main-title`, `.sub-title`, `.meta-location`, `.header-theme`)
  - `.pillars-grid` & `.pillar-card` (`.pillar-icon-box` + `.pillar-content`)
  - `.month-section` & `.month-header-bar`
  - `.day-card` variants:
    - `.special-title-card` / `.card-body-special-centered` (Pre-campaign Nov 16–20 card)
    - `.day-card.active-day` with `.card-top-bar` (`.day-pill`, `.date-text`, `.weekday-text`)
    - `.card-body-single` (`.single-lead-block`, `.single-act-block`, `.single-partner-box`, `.card-venue-box`)
    - `.card-body-multi` / `.sub-act-item-2` (2-activity stacked layout)
    - `.card-body-3act` / `.sub-act-item-3` (3-activity stacked layout, plus `.act3-date-pill` for multi-day sub-activities)
    - `.card-body-4act` / `.sub-act-item-4` (4-activity CSS rules defined in stylesheet)
    - `.card-body-5act` / `.sub-act-item-5` (5-activity stacked layout for Day 10)
    - `.day-card.weekend-advocacy-day` / `.card-body-weekend` (`.weekend-icon-box`, `.weekend-badge`, `.weekend-advocacy-text`)
    - Hybrid split cards (Days 11, 17, 18 combining top In-Person activity block and bottom Online Advocacy block)
    - `.card-venue-box` (emerald green location pill with pin SVG)
- **Approved exceptions:** Inline `style="..."` overrides on specific high-density cards (e.g., Day 3 `Project S.U.N.S.H.I.N.E. M&E` badge, Day 11/17/18 hybrid 50/50 split containers, Day 14 `Awarding of Winners` badge) to fine-tune vertical fit inside the fixed-height canvas.

## Design tokens
- **Color roles and token source:**
  - Defined in `:root` across all HTML files:
    - `--primary-orange: #ea580c` / `--orange-600: #ea580c` (primary brand accent, borders, pills, icons)
    - `--primary-dark: #9a3412` (dark orange headings/badges)
    - `--orange-50: #fffaf5` (warm card surface tint)
    - `--orange-100: #ffedd5` (icon box & sub-activity header background)
    - `--orange-200: #fed7aa` (card & sub-block borders)
    - `--orange-500: #f97316` (month header bar gradient end)
    - `--orange-700: #c2410c` (lead tag & theme text)
    - `--slate-900: #0f172a` to `--slate-100: #f1f5f9` (neutral text and backgrounds)
  - Semantic component colors (hardcoded in CSS rules):
    - **Title Dark Green:** `#0b3b2e` (`.main-title .text-dark`), `#0d4637` (`.sub-title`)
    - **Partners Box (Fuchsia/Purple):** background `#fdf4ff`, border `#f0abfc`, text `#701a75`, strong label `#86198f`
    - **Venue Box (Emerald Green):** background `#f0fdf4`, border `#86efac`, text `#065f46`, strong label `#047857`, icon `#059669`
- **Typography scale and font choices:**
  - Loaded from Google Fonts:
    - `'Montserrat', sans-serif` (weights 600–900): Main title (`96px` A3 / `88px` A4), subtitle (`36px` A3 / `33px` A4), month headers (`28px` A3 / `27px` A4), date numbers (`39px` A3 / `30px` A4), day pills (`31px` A3 / `24px` A4), badges, and section labels.
    - `'Satisfy', cursive`: "Orange Campaign" script title (`142px` A3 / `126px` A4).
    - `'Inter', sans-serif` (weights 400–800): Lead office names (`29.5px`–`36px` on A3 depending on card density), activity descriptions (`27px`–`36.5px` on A3), partner lists, and venue text.
  - *Note on Gotham fonts:* Although `Gotham-font-family/` (66 `.otf` files) and `scratch/install_gotham_fonts.ps1` exist in the repository, none of the HTML stylesheets currently reference `Gotham`.
- **Spacing, sizing, radii, borders, shadows:**
  - Canvas border: `8px solid #ea580c` (`border-radius: 36px`, `inset: 14px`) on A3; `7px solid #ea580c` (`border-radius: 28px`, `inset: 26px`) on A4, with inner `box-shadow: inset 0 0 0 3px/4px #fed7aa`.
  - Day cards: `2.5px solid #fed7aa` (A3) / `2px solid #fed7aa` (A4), `border-radius: 0 0 16px 16px` (A3) / `0 0 14px 14px` (A4).
- **Motion and transition rules:** None (static print/poster layout).

## Layout and density
- **Navigation:** None (single-view poster / 2-page print document).
- **Page grid and content width:**
  - **A3 Landscape (`4961x3508` px, `@page { size: 420mm 297mm; margin: 0; }`):**
    - Row 1 (`NOVEMBER 2026`, `.grid-7`): `grid-template-columns: 1.00fr 1.22fr 1.26fr 1.18fr 0.94fr 0.68fr 0.98fr` (Pre-Campaign + Days 1–6).
    - Row 2 (`DECEMBER 2026`, `.grid-6.row-2`): `grid-template-columns: 0.74fr 0.74fr 1.20fr 1.98fr 0.69fr 0.65fr` (Days 7–12; Day 10 gets `1.98fr` for 5 activities).
    - Row 3 (`DECEMBER 2026`, `.grid-6.row-3`): `grid-template-columns: 1.24fr 1.22fr 1.22fr 1.03fr 0.65fr 0.64fr` (Days 13–18).
  - **A4 Portrait (`2480x3508` px per page, `@page { size: 210mm 297mm; margin: 0; }`):**
    - Page 1: Row 1 (`1.00fr 1.25fr 1.35fr 1.25fr` — Pre-Campaign, Days 1–3), Row 2 (`1.18fr 0.74fr 1.18fr` — Days 4–6), Row 3 (`0.82fr 0.82fr 1.71fr` — Days 7–9).
    - Page 2: Row 1 (`2.45fr 0.79fr 0.72fr 1.18fr` — Days 10–13), Row 2 (`1.22fr 1.26fr 1.16fr 0.75fr 0.75fr` — Days 14–18).
- **Data density and table behavior:** High-density multi-card calendar matrix. Typography and padding scale down systematically from 1-activity cards (`.card-body-single`) to 2-activity (`.card-body-multi`), 3-activity (`.card-body-3act`), and 5-activity (`.card-body-5act`) cards so every card fills 100% of its row height cleanly.
- **Responsive breakpoints and behaviors:** None; fixed pixel dimensions for print rasterization, with `@media print` rules in `18-day-campaign-calendar-a4.html` to remove screen preview gaps/shadows and enforce `page-break-after: always`.

## Interaction and states
- Static print layout; no interactive hover/focus/form states.

## Accessibility
- **Contrast:** Dark slate (`#0f172a`, `#1e293b`), deep forest green (`#0b3b2e`), dark orange (`#9a3412`), deep purple (`#701a75`), and dark emerald (`#065f46`) text on white or very pale (`#fffaf5`, `#fdf4ff`, `#f0fdf4`) backgrounds provide strong print legibility.
- **Semantic structure:** Uses `<header>`, `<section>`, `<main>`, and `<article class="day-card">` elements.

## Verification
- **Screens/routes checked:** Inspected source markup of `18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and verified presence of rendered PNG outputs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`).
- **Viewports checked:** Print canvas dimensions configured in `scratch/render_a3_png.py` (`4961x3508`) and `scratch/render_a4_png.py` (`2480x3508`).
- **Browser or automated checks actually run:** Static source/hash inspection and Git diff verification during onboarding (no new browser render was triggered during onboarding per rule 14: make no code/asset changes merely because onboarding ran).
- **Unverified items:** Visual pixel-by-pixel inspection of the rendered PNGs after commit `b342179` was not re-run during onboarding.

## Skill usage notes
When making UI/UX changes, consult the relevant installed global skills, prioritizing `design-taste-frontend` and `ui-ux-pro-max` when available, alongside `design-system` and `ui-ux-design`. Record project-specific design decisions here; do not copy global skill instructions into this file.
