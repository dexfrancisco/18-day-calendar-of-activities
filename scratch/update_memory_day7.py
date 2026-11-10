import re

with open('.ai/memory/decisions.md', 'r', encoding='utf-8') as f:
    dec_text = f.read()

new_decision = '''## 2026-11-10 — Day 7 Activity Title Realignment (Gender Sensitivity Training)
**Decision:**
1. **Day 7 (Dec 1) Activity Title Updated:**
   - Changed Main Activity to: `Gender Sensitivity Training for LGU Employees and LDC Members`.
   - Lead Office: `CHRMO & CODI`.
   - Partners: `DILG, HR Office, GAD Office, CSOs` (DILG first).
   - Venue: `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
2. **Preserved Layout Quality:**
   - Maintained clean single-activity layout hierarchy (`.card-body-single`) with zero clipping and optimal vertical breathing space.
**Reason:** Official LGU Cauayan campaign realignment updating the Day 7 capacity-building focus to Gender Sensitivity Training for LGU employees and Local Development Council members.
**Alternatives:** Retaining preliminary "Safe workplace, anti-sexual harassment" general description.
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
    'Day 7 (Dec 1, Tue): CHRMO & CODI – Safe workplace, anti-sexual harassment, internal reporting and protection mechanisms (Partners: DILG, HR Office, GAD Office, CSOs; Venue: F. L. Dy Colliseum).',
    'Day 7 (Dec 1, Tue): CHRMO & CODI – Gender Sensitivity Training for LGU Employees and LDC Members (Partners: DILG, HR Office, GAD Office, CSOs; Venue: F. L. Dy Colliseum).'
)

with open('.ai/memory/requirements.md', 'w', encoding='utf-8') as f:
    f.write(req_text)
print("requirements.md updated.")

new_curr = '''# Current State

## Current feature
Day 7 Activity Title Realignment (Gender Sensitivity Training)

## Current task
Updated the Day 7 (Dec 1) activity title to "Gender Sensitivity Training for LGU Employees and LDC Members", re-extracted text, re-rendered 300 DPI PNG deliverables, and synchronized `Final Copy/`.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- **Day 7 (Dec 1):**
  - Updated Main Activity: `Gender Sensitivity Training for LGU Employees and LDC Members`.
  - Lead Office: `CHRMO & CODI`.
  - Partners: `DILG, HR Office, GAD Office, CSOs` (DILG strictly first).
  - Venue: `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
- **Synchronized Deliverables:**
  - `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html` (verified byte-identical)
  - `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`
  - Re-rendered 300 DPI PNGs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`)
  - Updated extracted text files (`18-Day_Campaign_Calendar_Extracted_Text.txt` and `Final Copy/`)

## Last verification
- Rendered 300 DPI screenshots via `render_a3_png.py` and `render_a4_png.py`.
- Verified bottom borders at y=3493 (A3) and y=3481 (A4) with zero clipping or overflow.
- Verified extracted text via `extract_all_text.py` confirming Day 7 title update.
- Verified byte-identity between `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.

## Next-session context
- All calendar files, extracts, and high-resolution render assets are fully updated, synchronized, and verified.
'''

with open('.ai/state/CURRENT.md', 'w', encoding='utf-8') as f:
    f.write(new_curr)
print("CURRENT.md updated.")

