import re

with open('.ai/memory/decisions.md', 'r', encoding='utf-8') as f:
    dec_text = f.read()

new_decision = '''## 2026-11-05 — Day 15 Expansion: PROJECT ORANGE RISE
**Decision:**
1. **Day 15 (Dec 9) Expanded to 2 Activities:**
   - Converted card from single-activity layout (`.card-body-single`) to 2-activity multi layout (`.card-body-multi` / `.sub-act-item-2`):
     - **Activity 1:** Lead Office: `Culminating Activity led by LGU Cauayan` — Main Activity: `Awarding of all barangays & offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.`
     - **Activity 2:** Lead Office: `GAD Office` — Main Activity: `PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run`
2. **Consolidated Partners with DILG Priority:**
   - Unified all Day 15 partner agencies into the top-of-venue partner box, keeping DILG strictly first:
     `DILG, NAPC, OPAPRU, PCW, CEDIPO, CSWDO, City Budget Office, City Accounting Office, GSO, DTI, TESDA, Cooperatives, Barangay Local Government Units, All Offices, All Partners, CSOs`
3. **Proportional Grid Realignment:**
   - A3 Landscape Row 3 (`.grid-6.row-3`): Realigned grid fractions to `1.20fr 1.05fr 1.35fr 1.15fr 0.92fr 0.68fr` to give Day 15 (Column 3) optimal width for two distinct activity blocks.
   - A4 Portrait Page 2 Row 2 (`.p2-grid-row2`): Realigned column widths to `1.05fr 1.05fr 1.48fr 1.12fr 1.04fr` for balanced card density.
**Reason:** Official LGU Cauayan GAD Office program update integrating the economic enterprise empowerment initiative (PROJECT ORANGE RISE) into the Day 15 Culminating Program.
**Alternatives:** Adding PROJECT ORANGE RISE to another date or keeping Day 15 single-activity.
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
    'Day 15 (Dec 9, Wed): Culminating Activity led by LGU Cauayan – Awarding of all barangays and offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU (Partners: DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs; Venue: F. L. Dy Colliseum).',
    'Day 15 (Dec 9, Wed): 2 Activities – (1) Culminating Activity led by LGU Cauayan: Awarding of all barangays and offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU; (2) GAD Office: PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run (Partners: DILG, NAPC, OPAPRU, PCW, CEDIPO, CSWDO, City Budget Office, City Accounting Office, GSO, DTI, TESDA, Cooperatives, Barangay Local Government Units, All Offices, All Partners, CSOs; Venue: F. L. Dy Colliseum).'
)

with open('.ai/memory/requirements.md', 'w', encoding='utf-8') as f:
    f.write(req_text)
print("requirements.md updated.")

new_curr = '''# Current State

## Current feature
Day 15 Expansion: PROJECT ORANGE RISE

## Current task
Expanded Day 15 on December 9 to a 2-activity card adding PROJECT ORANGE RISE under the GAD Office alongside the Culminating Activity, consolidated partners with DILG first, adjusted grid column proportions on A3 and A4 Page 2, re-extracted text, re-rendered 300 DPI PNG deliverables, and synchronized `Final Copy/`.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- **Day 15 (Dec 9):** Converted to 2-activity layout (`.card-body-multi`):
  - Activity 1: `Culminating Activity led by LGU Cauayan` — Awarding of all barangays & offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.
  - Activity 2: `GAD Office` — PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run.
  - Consolidated Partners (DILG first): `DILG, NAPC, OPAPRU, PCW, CEDIPO, CSWDO, City Budget Office, City Accounting Office, GSO, DTI, TESDA, Cooperatives, Barangay Local Government Units, All Offices, All Partners, CSOs`.
  - Venue: `F. L. Dy Colliseum, District III, Cauayan City, Isabela`.
- **Grid Optimization:**
  - A3 Row 3: Adjusted grid to `1.20fr 1.05fr 1.35fr 1.15fr 0.92fr 0.68fr`.
  - A4 Page 2 Row 2: Adjusted grid to `1.05fr 1.05fr 1.48fr 1.12fr 1.04fr`.
- **Synchronized Deliverables:**
  - `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html` (verified byte-identical)
  - `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`
  - Re-rendered 300 DPI PNGs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`)
  - Updated extracted text files (`18-Day_Campaign_Calendar_Extracted_Text.txt` and `Final Copy/`)

## Last verification
- Rendered 300 DPI screenshots via `render_a3_png.py` and `render_a4_png.py`.
- Verified bottom borders at y=3493 (A3) and y=3481 (A4) with zero clipping or overflow.
- Verified extracted text via `extract_all_text.py` confirming Day 15 dual activities and consolidated partners.
- Verified byte-identity between `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.

## Next-session context
- All calendar files, extracts, and high-resolution render assets are fully updated, synchronized, and verified.
'''

with open('.ai/state/CURRENT.md', 'w', encoding='utf-8') as f:
    f.write(new_curr)
print("CURRENT.md updated.")

