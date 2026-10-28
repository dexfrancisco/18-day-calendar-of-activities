# Project Context

## Project name
18-Day Campaign to End Violence Against Women and Their Children (Orange Campaign) — Calendar of Activities (2026)

## Purpose
Design, maintain, and render print-ready (300 DPI A3 Landscape and 2-Page A4 Portrait) HTML/CSS calendar layouts and PNG graphic deliverables for the City Government of Cauayan, Isabela's 2026 18-Day Orange Campaign (`November 25 – December 12, 2026`, with pre-campaign validation `November 16 – 20, 2026`), anchored on the theme *"Project S.U.N.S.H.I.N.E. for Safe, Inclusive and Technology-Responsive Communities"*.

## Users/roles
- **Campaign Organizers / Owners:** City Government of Cauayan (LGU Cauayan), Gender and Development (GAD) Office, Office of the City Mayor.
- **Activity Lead Offices:** LGU Cauayan departments, councils, and partner sector leads scheduled across Days 1–18 (GAD Office, PESO/COOP/CEDIPO, City Agriculture & Cooperative Office, City Accounting Office, PDAO & OSCA, CSWDO, City Youth Development Office / Kalinga Kabataan Program, CHRMO & CODI, MOVE, CDRRMO / Rescue 922 / Safe Line, City Health Office, City Legal Office, PNP-WCPD / LCAT-VAWC / BJMP / Justice Sector, Liga ng mga Barangay / VAW Desks, JCD GAD CONNECT, CPDO / GAD KMS Team, City Tourism / Culture Office / PIO).
- **Convergence & Community Partners:** 65 Barangays, Province of Isabela, RGADC 2, NAPC, OPAPRU, PCW, PNP, BJMP, BFP, DILG, DepEd (SDO Cauayan City, DepEd RO2), DOLE, OWWA, DTI, DA, COA, PAO, City Prosecutor's Office, Hospitals/RHUs, CSOs, POs, OGP Partners, Faith-based Groups, Youth Groups, JCI, Isabela Artist Club (ISAC), Women with Disabilities Group, Local Artists, Media, PLDT, and Tech Partners.
- **Print & Digital Operators:** Staff maintaining the HTML/CSS layouts and generating high-resolution PNG exports via the Python + headless Chrome rendering scripts.

## Stack
- **Language:** HTML5, CSS3 (inline `<style>` with CSS custom properties, CSS Grid, Flexbox, `@page` print rules), Python 3 (standard library utility scripts), PowerShell 5.1+ (Windows font installation script).
- **Framework/version:** None (vanilla self-contained HTML/CSS documents).
- **Runtime:** Web browser / Google Chrome Headless (`C:\Program Files\Google\Chrome\Application\chrome.exe`) + Python 3 (`http.server`, `subprocess`, `re`, `html`).
- **Package manager:** None (no `package.json`, `requirements.txt`, or third-party package dependencies).
- **Database:** None (all campaign schedule data is embedded directly in HTML markup).
- **UI/component library:** Custom inline CSS design system with inline SVG iconography and Google Fonts (`Montserrat`, `Satisfy`, `Inter`).
- **Authentication:** None (static documents and local CLI scripts).
- **Authorization:** None (filesystem/Git access only).

## Deployment
- Local static HTML rendering to high-resolution PNG files (`18-Day_Campaign_Calendar_A3.png` at `4961x3508` px and `18-Day_Campaign_Calendar_A4_Page1.png` / `18-Day_Campaign_Calendar_A4_Page2.png` at `2480x3508` px) for physical large-format/office printing and digital publication.
- No hosted web server or cloud deployment is configured in the repository.

## Major modules
- **A3 Landscape Master Calendar (`18-day-campaign-calendar-a3.html` & `18-day-campaign-calendar.html`):** Identical single-page `420mm x 297mm` (`4961x3508` px) layouts containing the full 18-day schedule plus the Nov 16–20 pre-campaign card across 3 horizontal rows.
- **A4 Portrait Combined Calendar (`18-day-campaign-calendar-a4.html`):** Two-page `210mm x 297mm` (`2480x3508` px per page) print layout with `@media print` page breaks.
- **A4 Portrait Split Render Pages (`18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`):** Individual page HTML files used by headless Chrome to export `18-Day_Campaign_Calendar_A4_Page1.png` (Pre-Campaign + Days 1–9) and `18-Day_Campaign_Calendar_A4_Page2.png` (Days 10–18).
- **Automation & Extraction Scripts (`scratch/`):**
  - `scratch/render_a3_png.py`: Renders A3 HTML to PNG via local Python HTTP server (port `8991`) and headless Chrome.
  - `scratch/render_a4_png.py`: Renders A4 Page 1 and Page 2 HTML files to PNG via local Python HTTP server (port `8992`) and headless Chrome.
  - `scratch/extract_calendar_text.py`: Parses `18-day-campaign-calendar-a3.html` and prints a structured plain-text schedule summary.
  - `scratch/install_gotham_fonts.ps1`: Installs the 66 `.otf` font files from `Gotham-font-family/` into the Windows user font directory and registry.
- **Archive & Reference Snapshots:**
  - `original_unedited_calendar/`: Initial source `.docx` (`18-Day_Campaign_Cauayan_Isabela_2026_Extracted_Details.docx`), `extracted_docx_text.txt`, and initial HTML/PNG baseline.
  - `Final Copy/`: Previous milestone copy of A3 HTML, PNG, and `18-Day_Campaign_Calendar_Extracted_Text.txt`.
  - `keep copy/` and `do not touch/`: Historical backup snapshots.

## Business rules
- All 18 campaign days (`November 25 – December 12, 2026`) plus the Pre-Campaign validation block (`November 16 – 20, 2026`) must be represented accurately with their designated Date, Day number, Weekday, Lead Office(s), Main Activity / Sub-activities, Partner organizations, and Venue.
- Schedule changes must be synchronized across all active root HTML variants (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`) and re-rendered to the root PNG outputs (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`).
- Fixed print canvas dimensions (`4961x3508` px for A3 Landscape, `2480x3508` px for A4 Portrait) have `overflow: hidden`; any content additions or font adjustments must fit strictly inside the canvas without clipping or overflowing card boundaries.

## Constraints
- Do not modify files inside `do not touch/`, `keep copy/`, or `original_unedited_calendar/` unless explicitly instructed by the user.
- Headless PNG rendering requires Google Chrome installed at `C:\Program Files\Google\Chrome\Application\chrome.exe` and network access to `fonts.googleapis.com` / `fonts.gstatic.com` (for `Montserrat`, `Satisfy`, and `Inter`).
