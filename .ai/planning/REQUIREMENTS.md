# Project Requirements

## Goal
Deliver print-ready A3 Landscape and 2-page A4 Portrait HTML/CSS layouts and 300 DPI PNG graphic files for the City Government of Cauayan, Isabela's **18-Day Campaign to End Violence Against Women and Their Children (Orange Campaign)** (`November 25 – December 12, 2026`, plus `November 16 – 20, 2026` pre-campaign validation).

## Users
- LGU Cauayan GAD Office and Office of the City Mayor
- LGU department lead offices and 65 Barangays
- Multi-sectoral convergence partners (NGAs, PNP, DepEd, CSOs, POs, Youth Groups, OGP Partners)
- Graphic/print operators

## Roles
- **Campaign Lead:** GAD Office & Office of the City Mayor
- **Activity Lead Offices:** Scheduled LGU offices and sector leads for Pre-Campaign and Days 1–18
- **Convergence Partners:** Partner agencies and community organizations per activity
- **Maintainer / Operator:** Edits HTML schedule markup and runs headless Chrome rendering scripts

## Core workflows
1. **Schedule Content Revision:** Edit activity details across `18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, and `18-day-campaign-calendar-a4-page2.html`.
2. **PNG Rasterization:** Execute `python scratch/render_a3_png.py` and `python scratch/render_a4_png.py` to regenerate `18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, and `18-Day_Campaign_Calendar_A4_Page2.png`.
3. **Visual Quality Verification:** Inspect rendered PNGs to verify zero text clipping or box overflow inside the fixed `4961x3508` and `2480x3508` canvases.

## Functional requirements
- Accurate representation of the campaign header, theme (*"Project S.U.N.S.H.I.N.E. for Safe, Inclusive and Technology-Responsive Communities"*), 4 Core Pillars, Pre-Campaign validation card, and Days 1–18 cards.
- Distinct visual styling for Lead Offices, Activity descriptions, Special Event/Initiative badges, Partners, Venues, and Online Advocacy tracks.
- Synchronized content across A3 and A4 layouts.

## Non-functional requirements
- Exact 300 DPI canvas dimensions (`4961x3508` px for A3 landscape; `2480x3508` px per page for A4 portrait).
- High print legibility and exact color reproduction (`print-color-adjust: exact`).

## Security
- Static local HTML/CSS/PNG assets; no credentials or personal data stored.

## Audit
- Version control via Git commits on `master`.

## Reporting
- High-resolution PNG deliverables and plain-text schedule summaries (`Final Copy/18-Day_Campaign_Calendar_Extracted_Text.txt`).

## Constraints
- Preserve historical folders (`do not touch/`, `keep copy/`, `original_unedited_calendar/`) untouched.
