# Durable Decisions

## 2026-10-22 — Dual Print Format Architecture (A3 Landscape + 2-Page A4 Portrait)
**Decision:** Maintain the 18-Day Campaign Calendar in two fixed-resolution 300 DPI HTML/CSS canvas formats: a single-page A3 Landscape poster (`4961x3508` px / `420mm x 297mm`) and a two-page A4 Portrait document (`2480x3508` px / `210mm x 297mm` per page, split into `page1` and `page2` files for headless Chrome PNG export).
**Reason:** Supports both large-format wall poster printing (A3) and standard office/handout printing (A4) while using deterministic headless Chrome rasterization.
**Alternatives:** Responsive single-file fluid web layout, or desktop publishing binaries (InDesign/Canva) that cannot be version-controlled and diffed as code.
**Impact:** Every schedule change must be applied to both the A3 HTML files (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`) and the A4 HTML files (`18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`), followed by running `scratch/render_a3_png.py` and `scratch/render_a4_png.py`.
**Status:** Active

## 2026-10-27 — Removal of Participation Targets Footer & Proportional Grid Weighting
**Decision:** Remove the bottom "Participation Targets" footer bar (Male: 975, Female: 1215, Total: 2190) from the rendered HTML body and use non-uniform proportional CSS Grid column widths (`fr` units) tailored to each day's activity count.
**Reason:** Multi-activity days (such as 5-activity Day 10 and 3-activity Days 2 and 3) required significantly more vertical and horizontal area to remain legible at print scale without clipping.
**Alternatives:** Uniform equal-width 6/7-column grids with much smaller font sizes.
**Impact:** Maximizes calendar grid height and gives dense multi-activity cards wider columns (e.g., `1.98fr` on A3 and `2.45fr` on A4 Page 2 for Day 10) while keeping weekend online advocacy cards compact (`0.64fr`–`0.75fr`).
**Status:** Active

## 2026-10-28 — Schedule Revisions on Day 1, Day 3, and Day 14 (Commit `b342179`)
**Decision:**
1. **Day 1 (Nov 25):** Split into 2 activities — Activity 1: GAD Office (*Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries*, Partners: BJMP, PNP, CSWD) and Activity 2: GAD Office & Office of the City Mayor (*Opening Program, Orange Campaign Kickoff, Parade around the City, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch*), with Venue set to *City Sports Complex, Tagaran*.
2. **Day 3 (Nov 27):** Expanded to 3 activities by inserting Activity 2: GAD Office — *Namnama (PWD Film Viewing)* (Partners: Isabela Artist Club (ISAC), Women with Disabilities Group) between PDAO & OSCA (Activity 1) and CSWDO (Activity 3, with shortened badge *Project S.U.N.S.H.I.N.E. M&E*).
3. **Day 14 (Dec 8):** Updated Main Activity text to *Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing* (with *Awarding of Winners* badge).
4. Removed root `18-Day_Campaign_Calendar_Extracted_Text.txt` (commit `109f0e9`).
**Reason:** Reflects the latest official LGU Cauayan GAD Office campaign schedule adjustments.
**Alternatives:** Keeping original single-activity Day 1 and 2-activity Day 3 schedule.
**Impact:** Root HTML and PNG files reflect these updates; `Final Copy/` still holds the pre-`b342179` snapshot unless explicitly synced.
**Status:** Active

## 2026-10-28 — V5 Project-Local AI Context Onboarding
**Decision:** Onboard the repository into the Antigravity V5 project-local `.ai/` memory, state, and planning system without modifying any existing campaign HTML, CSS, script, or image files.
**Reason:** Provides persistent, verified architectural and schedule context for future sessions while strictly preserving working project deliverables.
**Alternatives:** Ad-hoc session discovery without persistent project memory.
**Impact:** Future tasks must consult and maintain `.ai/memory/` and `.ai/state/` in accordance with `GEMINI.md` and `.ai/workflows/memory-update.md`.
**Status:** Active
