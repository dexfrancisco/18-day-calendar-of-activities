# Known Issues

## Bugs
- **`scratch/extract_calendar_text.py` Regex Mismatch on Multi-Activity & Hybrid Cards:**
  - `extract_calendar_text.py` (line 84) searches for `<div class="(?:sub-act-item-\d+|sub-act-item)">(.*?)</div>`, which terminates at the first inner `</div>` (`<div class="sub-act-header">`), and expects `card-body-single` or `weekend-lead-title` classes that differ from the inline-styled hybrid cards on Days 11, 17, and 18. Running `extract_calendar_text.py` without updating its parser will miss or truncate fields on multi-activity and hybrid cards.

## Technical debt
- **Manual Multi-File Duplication:**
  - The same schedule data is duplicated across 5 root HTML files (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`). Any text edit must be applied consistently to all relevant files to prevent drift.
- **`Final Copy/` Drift After Commit `b342179`:**
  - Root HTML and PNG files were updated in commit `b342179` (2026-10-28) for Day 1 (split into 2 activities + City Sports Complex, Tagaran venue), Day 3 (added Activity 2: GAD Office — *Namnama (PWD Film Viewing)*), and Day 14 (updated to *Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing*), whereas `Final Copy/18-day-campaign-calendar-a3.html`, `Final Copy/18-day-campaign-calendar.html`, `Final Copy/18-Day_Campaign_Calendar_A3.png`, and `Final Copy/18-Day_Campaign_Calendar_Extracted_Text.txt` still contain the pre-`b342179` (2026-10-27) version.
- **Unused Bundled Font Assets & Dead CSS Rules:**
  - `Gotham-font-family/` (66 `.otf` files) and `scratch/install_gotham_fonts.ps1` are committed in the repository, but all HTML files currently use Google Fonts (`Montserrat`, `Satisfy`, `Inter`).
  - Unused CSS classes remain in `18-day-campaign-calendar-a3.html` from earlier iterations (e.g., `.vacated-day` / `.card-body-vacated` from when Day 3 was temporarily vacated, `.card-body-4act` / `.sub-act-item-4`, and `.footer-section` / `.targets-block` after the footer was removed from the HTML body).
- **Spelling in Venue Name:**
  - "F. L. Dy Colliseum" (spelled with double `l`) appears consistently across the HTML files (`Days 3, 6, 7, 8, 9, 10, 14, 15, 16, 17`). Do not alter unless requested by the user.

## Environment problems
- **Hardcoded Paths and Ports in Render Scripts:**
  - `scratch/render_a3_png.py` and `scratch/render_a4_png.py` hardcode `DIRECTORY = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"`, `chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"`, and ports `8991` / `8992`.

## Workarounds
- To render both pages of the A4 portrait layout to separate PNG files via headless Chrome `--screenshot`, Page 1 and Page 2 are maintained as separate standalone HTML files (`18-day-campaign-calendar-a4-page1.html` and `18-day-campaign-calendar-a4-page2.html`) alongside the combined `18-day-campaign-calendar-a4.html`.

## Risks
- **Vertical Overflow Clipping on Dense Cards:** Because `.calendar-canvas` (`4961x3508`) and `.page-canvas` (`2480x3508`) set `overflow: hidden`, adding extra lines of text or activities to dense cards (such as Day 2, Day 3, or Day 10) without adjusting font sizes, padding, or grid column fractions (`fr`) can push the bottom `.card-venue-box` out of the card boundary. Always render and visually inspect the PNGs after content edits.
