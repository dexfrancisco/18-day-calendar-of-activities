import re

with open('.ai/memory/decisions.md', 'r', encoding='utf-8') as f:
    dec_text = f.read()

new_decision = '''## 2026-10-28 — Removal of 4 Top Pillars & Canvas Readability Expansion
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
    '2. **4 Core Pillars Banner:** Display Coverage, Convergence Partners, Focus Areas, and Integrated Platforms at the top of the calendar.',
    '2. **Header Layout (Pillars Removed):** The top 4 pillar boxes (Coverage, Convergence Partners, Focus Areas, Integrated Platforms) are removed from the canvas header to maximize vertical space and card legibility.'
)

with open('.ai/memory/requirements.md', 'w', encoding='utf-8') as f:
    f.write(req_text)
print("requirements.md updated.")

with open('.ai/state/CURRENT.md', 'r', encoding='utf-8') as f:
    curr_text = f.read()

new_curr = '''# Current State

## Current feature
Removal of 4 Top Pillar Boxes & Canvas Readability Expansion

## Current task
Removed the top 4 pillar boxes across all A3 and A4 HTML templates, reallocated vertical canvas space to expand card padding, gaps, and font sizes for superior readability, restored both "Display of Orange Exhibits" and "Posting of Accomplishment Reports" on Day 18, re-extracted text, re-rendered 300 DPI PNG deliverables, and synchronized `Final Copy/`.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- **Pillars Grid Removed:** Removed `.pillars-grid` (Coverage, Convergence Partners, Focus Areas, Integrated Platforms) from all calendar templates (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`).
- **Day 18 Dual In-Person Activities:** Restored `Display of Orange Exhibits` as Activity 1 alongside `Posting of Accomplishment Reports for the 18-day Campaign` as Activity 2 (both Lead: `GAD Office`), plus the `ONLINE ADVOCACY` block.
- **Card Readability Expansion:**
  - Day 3 (4 activities, 2 venues, 2 partner boxes): Increased lead office to 28px (A3) / 22.5px (A4), descriptions to 25px (A3) / 20px (A4), partner boxes to 22px (A3) / 18.5px (A4), and venue boxes to 24.5px (A3) / 19.5px (A4).
  - Day 10 (5 activities): Increased lead office to 31px (A3) / 23px (A4), descriptions to 28.5px (A3) / 21px (A4).
  - Single cards: Increased lead names to 36px (A3) / 27px (A4), descriptions to 33px (A3) / 25px (A4).
  - Multi-activity cards: Increased lead titles to 33px (A3) / 26.5px (A4), descriptions to 30px (A3) / 24px (A4).
  - Month header bars: Increased to 32px (A3) / 27px (A4) with increased padding.
- **Synchronized Deliverables:**
  - `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html` (verified byte-identical)
  - `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`
  - Re-rendered 300 DPI PNGs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`)
  - Updated extracted text files (`18-Day_Campaign_Calendar_Extracted_Text.txt` and `Final Copy/`)

## Last verification
- Rendered 300 DPI screenshots via `render_a3_png.py` and `render_a4_png.py`.
- Verified bottom borders at y=3493 (A3) and y=3481 (A4) with zero clipping or overflow.
- Verified extracted text via `extract_all_text.py` confirming Day 18 dual activities.
- Verified byte-identity between `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.

## Next-session context
- All calendar files, extracts, and high-resolution render assets are fully updated, synchronized, and verified.
'''

with open('.ai/state/CURRENT.md', 'w', encoding='utf-8') as f:
    f.write(new_curr)
print("CURRENT.md updated.")

