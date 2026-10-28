# Next Session

## First thing
Read `.ai/state/CURRENT.md` and `.ai/memory/project-context.md`, then check whether the user wants schedule content edits, layout/typography adjustments, or synchronization of `Final Copy/`.

## Remaining work
- Root calendar files (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`) and root PNG renders (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`) are up to date as of commit `b342179` / `109f0e9`.
- `Final Copy/` still reflects the pre-`b342179` state (2026-10-27) and can be updated if the user requests a new final package export.

## Likely files/modules
- `18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html`
- `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`
- `scratch/render_a3_png.py` & `scratch/render_a4_png.py`
- `Final Copy/`

## Verification
- After any HTML/CSS schedule edit:
  1. Ensure `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html` remain synchronized, and `18-day-campaign-calendar-a4.html` matches `a4-page1.html` + `a4-page2.html`.
  2. Run `python scratch/render_a3_png.py` and `python scratch/render_a4_png.py`.
  3. Visually inspect `18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, and `18-Day_Campaign_Calendar_A4_Page2.png` to confirm zero text clipping or card overflow.

## Pending decisions
- Whether `Final Copy/` should be updated to match the latest root `b342179` revision.
- Whether the bundled `Gotham-font-family/` OTF fonts should be applied to any typography roles or remain as optional local assets.
