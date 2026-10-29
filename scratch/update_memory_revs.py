import re

with open('.ai/memory/decisions.md', 'r', encoding='utf-8') as f:
    dec_text = f.read()

new_decision = '''## 2026-10-29 — Venue Realignment (Days 1, 2, 10) & Day 8 World AIDS Day Expansion
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

'''

idx = dec_text.find('## 2026-')
if idx != -1:
    dec_text = dec_text[:idx] + new_decision + dec_text[idx:]
    with open('.ai/memory/decisions.md', 'w', encoding='utf-8') as f:
        f.write(dec_text)
    print("decisions.md updated.")

with open('.ai/memory/requirements.md', 'r', encoding='utf-8') as f:
    req_text = f.read()

req_text = req_text.replace(
    'Venue: City Sports Complex, Tagaran.',
    'Venue: CITYWIDE.'
)
req_text = req_text.replace(
    'Venue: Isabela Convention Center, San Fermin); (3) Nov 26',
    'Venue: F. L. Dy Colliseum, District III, Cauayan City, Isabela); (3) Nov 26'
)
req_text = req_text.replace(
    'Days 7 & 8 (Dec 1–2, Tue–Wed): CHRMO & CODI – Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms (Partners: HR Office, GAD Office, DILG, CSOs; Venue: F. L. Dy Colliseum).',
    'Day 7 (Dec 1, Tue): CHRMO & CODI – Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms (Partners: DILG, HR Office, GAD Office, CSOs; Venue: F. L. Dy Colliseum).\n   - **Day 8 (Dec 2, Wed):** 2 Activities – (1) CHRMO & CODI: Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms; (2) City Health Office (CHO): World Aids Day Celebrations 2026 : "Ending Aids Starts with Access" (Partners: DILG, HR Office, GAD Office, CSOs; Venue: F. L. Dy Colliseum).'
)
req_text = req_text.replace(
    '(Partners: GAD Office, PNP, Tech Partners, BJMP, JCI, Barangay Officials; Venue: F. L. Dy Colliseum).',
    '(Partners: DILG, PNP, BJMP, City Prosecutor\'s Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI; Venue: Isabela Convention Center, San Fermin).'
)

with open('.ai/memory/requirements.md', 'w', encoding='utf-8') as f:
    f.write(req_text)
print("requirements.md updated.")

new_curr = '''# Current State

## Current feature
Venue Realignments (Days 1, 2, 10) & Day 8 World AIDS Day Activity

## Current task
Updated Day 1 venue to CITYWIDE, Day 2 venue to F. L. Dy Coliseum, Day 10 venue to Isabela Convention Center (ICON), and expanded Day 8 to 2 activities (adding CHO World AIDS Day Celebrations 2026) across all A3 and A4 HTML templates, re-extracted text, re-rendered 300 DPI PNG deliverables, and synchronized `Final Copy/`.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- **Day 1 (Nov 25):** Venue changed to `CITYWIDE`.
- **Day 2 (Nov 26):** Venue changed to `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
- **Day 8 (Dec 2):** Converted to 2-activity layout (`.card-body-multi`):
  - Activity 1: `CHRMO & CODI` — Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms.
  - Activity 2: `City Health Office (CHO)` — World Aids Day Celebrations 2026 : "Ending Aids Starts with Access".
  - Partners: `DILG, HR Office, GAD Office, CSOs` placed directly above venue box.
  - Venue: `F. L. Dy Colliseum, District III, Cauayan City, Isabela`.
  - Balanced A4 Page 1 Row 3 grid proportions to `0.82fr 1.25fr 1.35fr`.
- **Day 10 (Dec 4):** Venue changed to `Isabela Convention Center, San Fermin, Cauayan City, Isabela` (A3) / `Isabela Convention Center (ICON)` (A4).
- **Synchronized Deliverables:**
  - `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html` (verified byte-identical)
  - `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`
  - Re-rendered 300 DPI PNGs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`)
  - Updated extracted text files (`18-Day_Campaign_Calendar_Extracted_Text.txt` and `Final Copy/`)

## Last verification
- Rendered 300 DPI screenshots via `render_a3_png.py` and `render_a4_png.py`.
- Verified bottom borders at y=3493 (A3) and y=3481 (A4) with zero clipping or overflow.
- Verified extracted text via `extract_all_text.py` confirming Day 1 CITYWIDE, Day 2 FLDY Coliseum, Day 8 dual activities, and Day 10 ICON.
- Verified byte-identity between `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.

## Next-session context
- All calendar files, extracts, and high-resolution render assets are fully updated, synchronized, and verified.
'''

with open('.ai/state/CURRENT.md', 'w', encoding='utf-8') as f:
    f.write(new_curr)
print("CURRENT.md updated.")

