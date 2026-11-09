import re

with open('.ai/memory/decisions.md', 'r', encoding='utf-8') as f:
    dec_text = f.read()

new_decision = '''## 2026-11-09 — Day 3 Activity 1 Description Update (Sign Language Orientation)
**Decision:**
1. **Day 3 (Nov 27) Activity 1 Updated:**
   - Appended `, and Sign Language Orientation` to Activity 1:
     - **A3:** `Protection of women with disabilities & senior women; inclusive referral and access to support, and Sign Language Orientation.`
     - **A4:** `Protection of women with disabilities & senior women; inclusive referral, support, and Sign Language Orientation.`
   - Maintained zero clipping and proper spacing within `.card-body-4act` and `.sub-act-item-4`.
**Reason:** Official LGU Cauayan PDAO & OSCA activity update integrating Sign Language Orientation into the inclusive support session.
**Alternatives:** Adding as a separate 5th sub-activity (which would overcrowd the Day 3 card).
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
    'Activity 1: PDAO & OSCA – Protection of women with disabilities & senior women; inclusive referral and access to support (Partners: CSWDO, Health Office, PNP).',
    'Activity 1: PDAO & OSCA – Protection of women with disabilities & senior women; inclusive referral and access to support, and Sign Language Orientation (Partners: CSWDO, Health Office, PNP).'
)

with open('.ai/memory/requirements.md', 'w', encoding='utf-8') as f:
    f.write(req_text)
print("requirements.md updated.")

new_curr = '''# Current State

## Current feature
Day 3 Activity 1 Description Update (Sign Language Orientation)

## Current task
Appended ", and Sign Language Orientation" to Activity 1 of Day 3 (Nov 27) under PDAO & OSCA across all A3 and A4 HTML templates, verified zero clipping, re-extracted text, re-rendered 300 DPI PNG deliverables, and synchronized `Final Copy/`.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- **Day 3 (Nov 27):**
  - Updated Activity 1 Description: `Protection of women with disabilities & senior women; inclusive referral and access to support, and Sign Language Orientation.` (A3) / `Protection of women with disabilities & senior women; inclusive referral, support, and Sign Language Orientation.` (A4).
  - Lead Office: `PDAO & OSCA`.
  - Activity 2: `Namnama (PWD Film Viewing)` (Lead: `GAD Office`).
  - Activity 3: `Survivor-centered care management, psychosocial first aid, women and children referral mapping` + `Project S.U.N.S.H.I.N.E. M&E` (Lead: `CSWDO`).
  - Consolidated Venue 1 Partners: `CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group`.
  - Venue 1: `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
  - Activity 4: `KABATAAN PRO-TECT (Teen Empowerment and Care Team): Peer Helping Training on Safe Spaces, Mental Health, and ASRH` (Lead: `City Population Office`).
  - Venue 2 Partners: `City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School`.
  - Venue 2: `Cauayan City Stand Alone Senior High School`.
- **Synchronized Deliverables:**
  - `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html` (verified byte-identical)
  - `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, and `18-day-campaign-calendar-a4.html`
  - Re-rendered 300 DPI PNGs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`)
  - Updated extracted text files (`18-Day_Campaign_Calendar_Extracted_Text.txt` and `Final Copy/`)

## Last verification
- Rendered 300 DPI screenshots via `render_a3_png.py` and `render_a4_png.py`.
- Verified bottom borders at y=3493 (A3) and y=3481 (A4) with zero clipping or overflow.
- Verified extracted text via `extract_all_text.py` confirming Day 3 Activity 1 update.
- Verified byte-identity between `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.

## Next-session context
- All calendar files, extracts, and high-resolution render assets are fully updated, synchronized, and verified.
'''

with open('.ai/state/CURRENT.md', 'w', encoding='utf-8') as f:
    f.write(new_curr)
print("CURRENT.md updated.")

