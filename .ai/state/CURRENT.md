# Current State

## Current feature
18-Day Orange Campaign — Calendar & Poster Day 9 and Day 10 Exchange (ICON Venue & Full Re-renders)

## Current task
Completed exchanging activities, partners, and venues between Day 9 and Day 10:
- **Day 9 (Dec 3, 2026 | Thursday):**
  - Activities: End VAWC Action Forum (Survivor Healthcare, Legal Frameworks, LCAT-VAW Desk, and Digital Safety) [Activities 1-5 in calendar / combined forum title on poster].
  - Partners: DILG, PNP, BJMP, City Prosecutor's Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI.
  - Venue: **ICON, San Fermin, Cauayan City, Isabela**.
- **Day 10 (Dec 4, 2026 | Friday):**
  - Activity 1: Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility (Lead: GAD Office & MOVE).
  - Activity 2: Safeline 922 Emergency Response Simulation and Referral Drill (Lead: CDRRMO / Rescue 922 / Safe Line).
  - Partners: PNP, BFP, BJMP, CDRRMO, MDRRMO, All Teams, JCI, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan.
  - Venue: **F. L. Dy Colliseum, District III, Cauayan City, Isabela**.
- **Regenerated & Verified:**
  - `18-Day_Campaign_Calendar_Extracted_Text.txt`
  - `18-day-campaign-calendar-a3.html` & `18-Day_Campaign_Calendar_A3.png`
  - `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html` (`A4_Page1.png`), `18-day-campaign-calendar-a4-page2.html` (`A4_Page2.png`)
  - `18-day-campaign-calendar.html` and `Final Copy/` mirrors
  - `scratch/schedule_data.json`, `scratch/final_html/09-day-09.html`, `scratch/final_html/10-day-10.html`
  - 300 DPI Posters: `FABMAT/09-day-09.png`, `FABMAT/10-day-10.png`, `output/1x/`, `output/2x/`, `output/18-day-campaign-posters.pdf`
  - Interactive STUDIO Editor: `editor.html` updated and verified

## Status
Completed & Verified

## Branch
`master`

## Blocker
None

## Last meaningful change
- Swapped activity definitions and partners between Day 9 and Day 10 across all calendar HTML files and poster generator.
- Set Day 9 venue to ICON and Day 10 venue to F. L. Dy Coliseum.
- Re-rendered all 19 300 DPI posters (`generate_posters.py`) and calendar layouts (`render_calendars.py`).
- Re-baked `editor.html` via `build_clean_editor.py`.

## Last verification
- Bounding box measurement in Chrome: Day 9 bottom $y=2566$ px (384 px safe clearance), Day 10 bottom $y=2844$ px (106 px safe clearance).
- Template verification script (`check_editor_templates.py`): Day 9 has End VAWC Forum + ICON = True; Day 10 has MOVE + Safeline + F. L. Dy = True.
- Output crops generated and saved in artifact directory: `crop_day9_swapped.png`, `crop_day10_swapped.png`, `crop_calendar_d9_d10.png`.
