# Roadmap

## Phase 1 — Baseline Extraction & A3 Layout (Completed)
- Extract campaign schedule from `original_unedited_calendar/18-Day_Campaign_Cauayan_Isabela_2026_Extracted_Details.docx`.
- Design and build the single-page A3 Landscape HTML/CSS calendar (`4961x3508` px) and headless Chrome PNG renderer (`scratch/render_a3_png.py`).
- Bundle `Gotham-font-family/` assets and Windows font installer (`scratch/install_gotham_fonts.ps1`).

## Phase 2 — Multi-Activity Realignment & A4 Portrait Split (Completed)
- Expand calendar to support 2-, 3-, and 5-activity days, hybrid in-person + online advocacy days, and the Pre-Campaign OGAD Champions validation card (`Nov 16–20, 2026`).
- Build 2-page A4 Portrait layouts (`18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`) and renderer (`scratch/render_a4_png.py`).
- Remove footer participation targets to maximize daily card space.

## Phase 3 — Schedule Refinements & V5 AI Onboarding (Completed)
- Apply Oct 28, 2026 schedule updates (commit `b342179`) to Day 1 (2 activities + City Sports Complex, Tagaran venue), Day 3 (3 activities including *Namnama (PWD Film Viewing)*), and Day 14 (*Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing*).
- Establish V5 `.ai/` project memory, state, and planning baseline (2026-10-28).

## Future
- Sync `Final Copy/` directory with the latest root HTML/PNG deliverables when finalized by the user.
- Apply any subsequent LGU Cauayan GAD Office schedule or venue adjustments prior to the November 16 / November 25, 2026 campaign launch.
