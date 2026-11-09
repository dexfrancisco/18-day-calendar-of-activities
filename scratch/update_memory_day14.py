import re

with open('.ai/memory/decisions.md', 'r', encoding='utf-8') as f:
    dec_text = f.read()

new_decision = '''## 2026-11-09 — Day 14 Activity Title Expansion
**Decision:**
1. **Day 14 (Dec 8) Activity Name Updated:**
   - Changed Main Activity title to: `Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing`.
   - Maintained `Awarding of Winners` badge cleanly aligned under the main description.
2. **Typography & Layout Adjustments:**
   - Reduced `.single-act-desc.dense` font size to 27.5px / 1.25 line-height (A3) and 20px / 1.20 line-height (A4) to accommodate the comprehensive activity title with zero vertical clipping.
   - Rebalanced December Row 3 column proportions on A3 (`1.16fr 1.14fr 1.30fr 1.14fr 0.90fr 0.68fr`) and Row 2 on A4 Page 2 (`1.02fr 1.14fr 1.42fr 1.12fr 1.02fr`) to allocate optimal horizontal breathing room for Day 14.
**Reason:** Official LGU Cauayan campaign alignment expanding the Day 14 activity to formally include the Orange Exhibit and Orange Bubble Culture Arts advocacy program.
**Alternatives:** Truncating or omitting parts of the full event title.
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
    'Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing + Awarding of Winners',
    'Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing + Awarding of Winners'
)

with open('.ai/memory/requirements.md', 'w', encoding='utf-8') as f:
    f.write(req_text)
print("requirements.md updated.")

new_curr = '''# Current State

## Current feature
Day 14 Activity Title Expansion

## Current task
Updated the Day 14 (Dec 8) activity title to "Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing", refined typography and grid column proportions for zero clipping, re-extracted text, re-rendered 300 DPI PNG deliverables, and synchronized `Final Copy/`.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- **Day 14 (Dec 8):**
  - Updated Main Activity: `Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing`.
  - Maintained badge: `Awarding of Winners`.
  - Lead Office: `PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs`.
  - Partners: `Local Artists, Media, Content Creators` (A3) / `Local Artists, Media, Creators` (A4).
  - Venue: `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum` (A4).
- **Typography & Grid Calibration:**
  - A3 dense activity description adjusted to `27.5px` (line-height `1.25`) with column width `1.14fr`.
  - A4 Page 2 dense activity description adjusted to `20px` (line-height `1.20`) with column width `1.14fr`.
- **Synchronized Deliverables:**
  - `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html` (verified byte-identical)
  - `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`
  - Re-rendered 300 DPI PNGs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`)
  - Updated extracted text files (`18-Day_Campaign_Calendar_Extracted_Text.txt` and `Final Copy/`)

## Last verification
- Rendered 300 DPI screenshots via `render_a3_png.py` and `render_a4_png.py`.
- Verified bottom borders at y=3493 (A3) and y=3481 (A4) with zero clipping or overflow.
- Verified extracted text via `extract_all_text.py` confirming Day 14 expanded title.
- Verified byte-identity between `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.

## Next-session context
- All calendar files, extracts, and high-resolution render assets are fully updated, synchronized, and verified.
'''

with open('.ai/state/CURRENT.md', 'w', encoding='utf-8') as f:
    f.write(new_curr)
print("CURRENT.md updated.")

