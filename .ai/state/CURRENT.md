# Current State

## Current feature
18-Day Orange Campaign — Master Calendar & Daily Posters Synchronized with Revised Activity Titles and Day 10 Tarp Action Forum

## Current task
Completed applying the latest activity title revisions across both the master calendar deliverables and the daily poster suite:
1. **Activity Title Revisions Applied:**
   - Day 2 A1 & A2 updated to formal forum titles (`Economic Empowerment for Women Safe Employment and Anti Trafficking Forum`, `Rural Women Protection, Livelihood and Cooperative Support Forum`).
   - Day 3 A1 & A3 updated (`Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women`, `Project SUNSHINE Survivor – Centered Case Management and Referral Review`).
   - Day 4 updated (`Multi-Stakeholder Dialogue on Accountability to Survivors and Community Partnership`).
   - Day 8 A1 updated (`Safe Workplace Compliance and Anti-Sexual Harassment Orientation`).
   - Day 9 A1 & A2 updated (`Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility`, `Safeline 922 Emergency Response Simulation and Referral Drill`).
   - Day 10: Retained individual A1–A5 details on the master calendar; combined into `End VAWC Action Forum: Enhancing Survivor Healthcare, Legal Frameworks, LCAT-VAW Desk Coordination, and Digital Safety Innovations` for the daily poster/tarp.
   - Day 13 A1 updated (`Deepening Session on GFAsT and the GeRL Tool: Province of Isabela – LGUs Edition`).
   - Day 15 A1 updated (`Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW`).
2. **Master Calendar Deliverables Rendered:**
   - `18-day-campaign-calendar-a3.html` & `18-Day_Campaign_Calendar_A3.png` (root and `Final Copy/`).
   - `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`.
   - `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`.
   - `18-Day_Campaign_Calendar_Extracted_Text.txt` (root and `Final Copy/`).
3. **Daily Poster Suite Rendered:**
   - `FABMAT/`: 19 daily posters (`00-pre-campaign.png` through `18-day-18.png`), 2480 × 3508 px, 300 DPI.
   - `output/1x/`: 19 native posters (2480 × 3508 px, 300 DPI).
   - `output/2x/`: 19 double-density posters (4960 × 7016 px).
   - `output/18-day-campaign-posters.pdf`: Combined 19-page PDF.
   - Automated clearance audit: All 19 posters finish above $y = 2930$ px with positive buffer to the jeepney ($y \ge 2950$ px) and road ($y \ge 3388$ px).

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- Updated activity titles in `18-Day_Campaign_Calendar_Extracted_Text.txt` and all HTML calendar templates.
- Re-rendered master calendar PNGs (A3 landscape, A4 2-page portraits).
- Built updated `scratch/schedule_data.json` with Day 10 combined action forum for tarp posters.
- Re-rendered 1x and 2x posters in `FABMAT/`, `output/1x/`, `output/2x/`, and compiled the 19-page PDF.
- Verified $100\%$ bottom artwork clearance across all 19 posters via automated pixel analysis.

## Last verification
- Automated clearance audit on all 19 posters in `FABMAT/`: all 19 finish before $y = 2930$ px with positive buffer to the jeepney ($y \ge 2950$ px) and road ($y \ge 3388$ px).
- Re-rendered and verified `18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`.
