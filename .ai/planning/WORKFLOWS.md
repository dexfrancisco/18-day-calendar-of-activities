# Business Workflows

## Workflow 1 — Schedule Content Update & Multi-Format Synchronization
### Actor
Repository Maintainer / Designer

### Preconditions
- Official schedule change (activity title, lead office, partner list, date, or venue) requested by the user / LGU Cauayan GAD Office.

### Steps
1. Update the target day card(s) in `18-day-campaign-calendar-a3.html`.
2. Copy or apply the identical change to `18-day-campaign-calendar.html` so both A3 files remain byte-identical.
3. Apply the corresponding change to `18-day-campaign-calendar-a4.html` and the matching split page (`18-day-campaign-calendar-a4-page1.html` for Pre-Campaign and Days 1–9; `18-day-campaign-calendar-a4-page2.html` for Days 10–18).
4. Adjust card typography classes or grid column fractions (`fr`) if the added content increases vertical card height.

### Validation
- Compare file hashes of `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html`.
- Verify that A4 combined and split page HTML files contain matching schedule text.

### Result
All 5 active root HTML files contain the updated campaign schedule.

### Audit events
- Git diff inspection and commit on `master`.

---

## Workflow 2 — 300 DPI PNG Rendering & Visual Verification
### Actor
Repository Maintainer / Designer

### Preconditions
- Root HTML files are updated and saved.
- Google Chrome is installed at `C:\Program Files\Google\Chrome\Application\chrome.exe` and Python 3 is available.

### Steps
1. Run `python scratch/render_a3_png.py` to serve the workspace on port `8991` and capture `18-Day_Campaign_Calendar_A3.png` (`4961x3508` px).
2. Run `python scratch/render_a4_png.py` to serve the workspace on port `8992` and capture `18-Day_Campaign_Calendar_A4_Page1.png` and `18-Day_Campaign_Calendar_A4_Page2.png` (`2480x3508` px each).
3. Visually inspect the generated PNG files to ensure fonts loaded properly and no `.card-venue-box` or `.sub-partner-box` is clipped by `overflow: hidden`.

### Validation
- Check PNG file timestamps, dimensions, and visual layout completeness.

### Result
Updated 300 DPI print-ready PNG deliverables in the project root.

### Audit events
- Updated PNG binaries tracked in Git commit history.
