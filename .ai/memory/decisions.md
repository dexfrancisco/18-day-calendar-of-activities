# Durable Decisions

## 2026-10-29 — Venue Realignment (Days 1, 2, 10) & Day 8 World AIDS Day Expansion
**Decision:**
1. **Day 1 (Nov 25) Venue Updated to CITYWIDE:**
   - Changed venue from `City Sports Complex, Tagaran` to `CITYWIDE`.
2. **Day 2 (Nov 26) Venue Updated to F. L. Dy Coliseum:**
   - Changed venue from `Isabela Convention Center (ICON)` to `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
3. **Day 8 (Dec 2) Expanded to 2 Activities:**
   - Added Activity 2 — Lead Office: `City Health Office (CHO)`, Main Activity: `World Aids Day Celebrations 2026 : "Ending Aids Starts with Access"`.
   - Card converted from single-activity to 2-activity multi layout (`.card-body-multi` / `.sub-act-item-2`).
   - Consolidated partners (`DILG, HR Office, GAD Office, CSOs`) placed directly above venue box with DILG first.
   - On A4 Page 1, balanced Row 3 column proportions (`0.82fr 1.25fr 1.35fr`).
4. **Day 10 (Dec 4) Venue Updated to Isabela Convention Center (ICON):**
   - Changed venue from `F. L. Dy Colliseum` to `Isabela Convention Center, San Fermin, Cauayan City, Isabela` (A3) / `Isabela Convention Center (ICON)` (A4).
**Reason:** Official venue scheduling swaps and integration of the 2026 World AIDS Day commemoration under the City Health Office on Day 8.
**Alternatives:** Retaining preliminary venue assignments.
**Impact:** Synchronized across all 5 HTML templates (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, `18-day-campaign-calendar-a4.html`, and `Final Copy/`), text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-10-28 — Removal of 4 Top Pillars & Canvas Readability Expansion
**Decision:**
1. **Removal of Top Pillars Grid:** Removed `<section class="pillars-grid">` (Coverage, Convergence Partners, Focus Areas, Integrated Platforms) from the header across all calendar layouts (A3 Landscape and A4 Portrait Pages 1 & 2).
2. **Reallocation of Vertical Space:** Reallocated ~130–150px of freed-up vertical space to `.calendar-main` and individual day cards, substantially increasing typography size, element padding, and item spacing across all cards.
3. **Restoration of Dual Activities on Day 18:** Explicitly formatted Day 18 to include BOTH in-person GAD Office activities:
   - Activity 1: `Display of Orange Exhibits`
   - Activity 2: `Posting of Accomplishment Reports for the 18-day Campaign`
   Plus the `ONLINE ADVOCACY` track.
4. **Enhanced Typography & Spacing:**
   - Day 3 (4 activities + 2 venues): Lead office increased to 28px (A3) / 22.5px (A4), descriptions to 25px (A3) / 20px (A4), venue and partner boxes enlarged with increased breathing room.
   - Day 10 (5 activities + venue): Lead office increased to 31px (A3) / 23px (A4), descriptions to 28.5px (A3) / 21px (A4).
   - Single cards: Lead names increased to 36px (A3) / 27px (A4), descriptions to 33px (A3) / 25px (A4).
   - Month headers: Expanded to 32px font size with 28px icons and wider letter-spacing.
**Reason:** User requested removal of the 4 pillar boxes to free up vertical canvas space and readjust card heights and text sizes for optimal readability.
**Alternatives:** Retaining the pillar cards at reduced height or footer placement.
**Impact:** Synchronized across all 4 HTML templates, text extracts in root and `Final Copy/`, and freshly re-rendered 300 DPI exports.
**Status:** Active

## 2026-10-28 — Multi-Activity Card Consolidated Partner Architecture & Universal DILG Priority
**Decision:**
1. **Consolidated Card Partner Box Above Venue:**
   - In all multi-activity cards, sub-activity partner boxes (.sub-partner-box) were removed from individual items.
   - All partners across the activities under that venue are consolidated into a single, shared partner box (.card-partner-box) placed directly above the venue box (.card-venue-box).
   - Duplicate partners across activities within each card are deduplicated.
2. **Universal DILG First Position Rule:**
   - In any partner list where DILG is present, DILG must always be listed first:
     - **Pre-Campaign:** DILG, LGU Offices, Liga ng mga Barangay, CCGLO
     - **Day 7 & Day 8:** DILG, HR Office, GAD Office, CSOs
     - **Day 10 (Consolidated):** DILG, PNP, BJMP, City Prosecutor's Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI
     - **Day 13 (Consolidated):** DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS, IT Office, Planning Office, All Offices
     - **Day 15:** DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs
3. **Dual-Venue Scope (Day 3):**
   - For activities under Venue 1 (Activities 1, 2, 3), their partners are consolidated into .card-partner-box directly above Venue 1:
     CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group
   - For Activity 4 under Venue 2, its partners go directly above Venue 2:
     City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School
4. **Other Consolidated Multi-Activity Cards:**
   - **Day 1:** All City Offices, Barangays, PNP, BFP, BJMP, CSWD, Academe, CSOs
   - **Day 2:** DA, DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector
   - **Day 9:** PNP, BFP, BJMP, CDRRMO, MDRRMO, All Teams, JCI, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan
   - **Day 16:** DEPED RO2, SDO Cauayan City, CSOs
**Reason:** Eliminates redundant partner rows across sub-activities in multi-activity cards, dramatically improves card vertical hierarchy and legibility, prevents text clipping, and standardizes governance prominence by placing DILG first across all collaborative matrices.
**Alternatives:** Retaining individual sub-partner tags on every activity item, which crowded Day 10 and Day 3.
**Impact:** Synchronized across all 4 HTML layouts (18-day-campaign-calendar-a3.html, 18-day-campaign-calendar.html, 18-day-campaign-calendar-a4-page1.html, 18-day-campaign-calendar-a4-page2.html, 18-day-campaign-calendar-a4.html, and Final Copy/), text extractions, and 300 DPI PNG exports.
**Status:** Active

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
**Status:** Superseded by 2026-10-28 Partner Expansions and Day 3 Dual-Venue Architecture.

## 2026-10-28 — Partner Expansions & Day 3 Dual-Venue 4-Activity Architecture
**Decision:**
1. **Pre-Campaign (Nov 16–20):** Updated partners to `DILG, LGU Offices, Liga ng mga Barangay, CCGLO`.
2. **Day 1 (Nov 25):** In Activity 2, replaced trailing generic `Partners` with `PNP, BFP, BJMP, Academe, CSOs` (total partner list: `All City Offices, Barangays, PNP, BFP, BJMP, Academe, CSOs`).
3. **Day 2 (Nov 26):** In Activity 2, added `MSMES` after `Cooperatives` and `CSOs` after `Barangays` (total partner list: `DA, Cooperatives, MSMES, Barangays, CSOs`).
4. **Day 3 (Nov 27):**
   - Added `ISAC` to Activity 3 partners (`Health Office, PNP-WCPD, NGAs, CSOs, ISAC`).
   - Added Activity 4 under Venue 1 with its own Venue 2:
     - Lead Office: `City Population Office`
     - Main Activity: `KABATAAN PRO-TECT (Teen Empowerment and Care Team): Peer Helping Training on Safe Spaces, Mental Health, and ASRH`
     - Partners: `City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School`
     - Venue 2: `Cauayan City Stand Alone Senior High School`
   - Added `.card-body-4act` and `.sub-act-item-4` CSS styling, adjusted typography (19px/21px), and widened column 4 (`1.30fr` on A3 landscape, `1.38fr` on A4 portrait) to ensure zero clipping.
**Reason:** Official program expansion by LGU Cauayan GAD Office, integrating adolescent sexual and reproductive health / teen empowerment training at Cauayan City Stand Alone Senior High School.
**Alternatives:** Stacking Activity 4 inside Venue 1 or moving to a separate day.
**Impact:** Synchronized across all 4 HTML layouts (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`), text extractions, and 300 DPI PNG renders (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`).
**Status:** Active

## 2026-10-28 — Partner and Leadership Refinements (Days 6, 7, 8, 9, 10, 13)
**Decision:**
1. **Day 6 (Nov 30):**
   - Lead Office expanded to: `City Youth Development Office, SK Federation of Cauayan City / Kalinga Kabataan Program`.
   - Partners updated to: `DepEd, SK, VM Office, Sangguniang Panlungsod, Youth Groups, Faith Groups, PNP, Legal Office`.
2. **Days 7 & 8 (Dec 1–2):**
   - Replaced `HR Units` with `HR Office` and added `GAD Office` immediately after: `HR Office, GAD Office, DILG, CSOs`.
3. **Day 9 (Dec 3):**
   - In Activity 1 partners: removed `CSOs`, added `JCI, PNP, BJMP, CDRRMO, BFP` in front of `Faith Groups`, and appended `MASON, ROTARY Club of Cauayan` after `DepEd`:
     `JCI, PNP, BJMP, CDRRMO, BFP, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan`.
4. **Day 10 (Dec 4):**
   - Activity 1 partners: added `Barangay Officials` (`Hospitals, RHUs, NGOs, Mental Health Partners, BJMP, Barangay Officials`).
   - Activity 2 partners: added `Barangay` (`City Prosecutor's Office, PNP, DILG, BJMP, Barangay`).
   - Activity 5 partners: removed `PLDT`, added `JCI, Barangay Officials` (`GAD Office, PNP, Tech Partners, BJMP, JCI, Barangay Officials`).
5. **Day 13 (Dec 7):**
   - Activity 1 partners: added `DILG` in front of `PCW` (`DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS`).
**Reason:** Official agency and partner alignment by LGU Cauayan GAD Office.
**Alternatives:** Retaining previous generic groupings.
**Impact:** Synchronized across all 4 HTML templates, root and `Final Copy/` text extractions, and 300 DPI PNG exports (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`).
**Status:** Active

## 2026-10-28 — Program Revisions for Culminating & Regional Activities (Days 14, 15, 16, 17)
**Decision:**
1. **Day 14 (Dec 8):**
   - In Lead Office, removed `City Tourism / Culture Office` and added after `GAD Office`: `DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs`.
   - Full Lead Office line: `PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs`.
2. **Day 15 (Dec 9):**
   - Added `DILG` before `NAPC` and `Barangay, CSOs` after `All Partners`:
     `DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs`.
3. **Day 16 (Dec 10):**
   - Reordered partners to move `DEPED RO2` to the left of `SDO Cauayan City`, and appended `CSOs`:
     `DEPED RO2, SDO Cauayan City, CSOs`.
4. **Day 17 (Dec 11):**
   - Updated Main Activity to `Regional Educational Research Conference`.
   - On A4 Page 2, upgraded Day 17 card to active format displaying this in-person conference, venue, and partners, while balancing row proportions.
**Reason:** Official LGU Cauayan GAD Office program updates for the culminating week and regional research partnerships.
**Alternatives:** Retaining preliminary activity titles and partner sets.
**Impact:** Synchronized across all 4 HTML templates, root and `Final Copy/` text extractions, and 300 DPI PNG exports.
**Status:** Superseded by 2026-10-28 Rescheduling & Realignment.

## 2026-10-28 — Activity Rescheduling & Realignment (Days 13, 16, 17, 18)
**Decision:**
1. **Day 13 (Dec 7):** Added Activity 3 — Lead Office: `GAD Office`, Main Activity: `Display of Orange Exhibits` (card upgraded to `.card-body-3act` / `.sub-act-item-3` with 3 activities).
2. **Day 16 (Dec 10):** Copied the in-person conference from Day 17 (`Regional Educational Research Conference`, Partners: `SDO Cauayan City, DEPED RO2`) as Activity 2 alongside Activity 1 (`GAD in Action`). Card converted to a 2-activity layout (`.card-body-multi` / `.sub-act-item-2`).
3. **Day 17 (Dec 11):** Retained `Regional Educational Research Conference` alongside `ONLINE ADVOCACY` (2-day conference across both Days 16 and 17).
4. **Day 18 (Dec 12):** Replaced `Display of Orange Exhibits` with: Lead Office: `GAD Office`, Main Activity: `Posting of Accomplishment Reports for the 18-day Campaign` (alongside `ONLINE ADVOCACY`).
**Reason:** Clarified user requirement confirming that `Regional Educational Research Conference` is copied onto Day 16 while remaining active on Day 17 (multi-day regional educational research program).
**Alternatives:** Moving the activity and stripping Day 17 to pure online advocacy.
**Impact:** Synchronized across all 4 HTML templates, root and `Final Copy/` text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-10-28 — V5 Project-Local AI Context Onboarding
**Decision:** Onboard the repository into the Antigravity V5 project-local `.ai/` memory, state, and planning system without modifying any existing campaign HTML, CSS, script, or image files.
**Reason:** Provides persistent, verified architectural and schedule context for future sessions while strictly preserving working project deliverables.
**Alternatives:** Ad-hoc session discovery without persistent project memory.
**Impact:** Future tasks must consult and maintain `.ai/memory/` and `.ai/state/` in accordance with `GEMINI.md` and `.ai/workflows/memory-update.md`.
**Status:** Active
