# Architecture

## Current architecture
The repository uses a **static, self-contained HTML/CSS print-canvas architecture** paired with lightweight **Python + Headless Chrome CLI rendering scripts**:
- Each layout variant is a standalone `.html` file containing embedded CSS (`<style>`) and inline SVG icons, eliminating external CSS/JS bundle dependencies.
- Layout synchronization is manual across the active root HTML files:
  - `18-day-campaign-calendar-a3.html` and `18-day-campaign-calendar.html` are maintained as byte-identical copies (verified SHA256 prefix `88697860F04E`) for the single-sheet A3 landscape poster (`4961x3508` px).
  - `18-day-campaign-calendar-a4.html` combines both A4 portrait pages into one printable document (`2480x3508` px per `.page-canvas`).
  - `18-day-campaign-calendar-a4-page1.html` and `18-day-campaign-calendar-a4-page2.html` isolate Page 1 (Pre-Campaign + Days 1–9) and Page 2 (Days 10–18) so headless Chrome's `--screenshot` flag can capture each page at exact `2480x3508` pixel dimensions.

## Directory conventions
- `/` (Project Root): Active working HTML layouts (`18-day-campaign-calendar*.html`), latest rendered PNG deliverables (`18-Day_Campaign_Calendar_*.png`), `GEMINI.md` instructions.
- `scratch/`: Python and PowerShell utility scripts (`render_a3_png.py`, `render_a4_png.py`, `extract_calendar_text.py`, `install_gotham_fonts.ps1`).
- `Gotham-font-family/`: Bundled Gotham OpenType (`.otf`) font families (`Gotham`, `Gotham Condensed`, `Gotham Narrow`, `Gotham Rounded`, `Gotham ScreenSmart` — 66 files total).
- `Final Copy/`: Milestone snapshot directory containing earlier A3 HTML/PNG copies and `18-Day_Campaign_Calendar_Extracted_Text.txt`.
- `original_unedited_calendar/`: Source specification `.docx` (`18-Day_Campaign_Cauayan_Isabela_2026_Extracted_Details.docx`), raw text dump (`extracted_docx_text.txt`), and original baseline calendar.
- `do not touch/` & `keep copy/`: Protected historical layout backups.
- `.ai/` & `docs/`: V5 project-local AI memory, state, planning, rules, and workflow documentation.

## Request/data flow
1. **Content Authoring:** Campaign schedule updates (lead offices, activities, partners, venues, dates) are edited directly in the root HTML files (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`).
2. **Local HTTP Serving & Rendering:**
   - `python scratch/render_a3_png.py` starts a daemon `http.server.SimpleHTTPRequestHandler` on `localhost:8991` and invokes `chrome.exe --headless=new --window-size=4961,3508 --virtual-time-budget=5000` against `18-day-campaign-calendar-a3.html` to produce `18-Day_Campaign_Calendar_A3.png`.
   - `python scratch/render_a4_png.py` starts a daemon HTTP server on `localhost:8992` and invokes `chrome.exe --headless=new --window-size=2480,3508 --virtual-time-budget=5000` against `18-day-campaign-calendar-a4-page1.html` and `18-day-campaign-calendar-a4-page2.html` to produce `18-Day_Campaign_Calendar_A4_Page1.png` and `18-Day_Campaign_Calendar_A4_Page2.png`.
3. **Text Verification:** `python scratch/extract_calendar_text.py` parses `<article class="day-card ...">` blocks from `18-day-campaign-calendar-a3.html` using regular expressions to output a human-readable text audit of all cards.

## Major modules
| File | Role | Dimensions / Scope |
|---|---|---|
| `18-day-campaign-calendar-a3.html` | Primary A3 landscape calendar source | `4961x3508` px (`420mm x 297mm`), Pre-Campaign + Days 1–18 |
| `18-day-campaign-calendar.html` | Mirror of A3 landscape calendar | Identical to `18-day-campaign-calendar-a3.html` |
| `18-day-campaign-calendar-a4.html` | Combined 2-page A4 portrait calendar | Two `2480x3508` px (`210mm x 297mm`) `.page-canvas` sections |
| `18-day-campaign-calendar-a4-page1.html` | A4 portrait Page 1 render source | `2480x3508` px, Header + Pillars + Pre-Campaign + Days 1–9 |
| `18-day-campaign-calendar-a4-page2.html` | A4 portrait Page 2 render source | `2480x3508` px, Header + Pillars + Days 10–18 |
| `scratch/render_a3_png.py` | A3 PNG renderer | Outputs `18-Day_Campaign_Calendar_A3.png` |
| `scratch/render_a4_png.py` | A4 PNG renderer | Outputs `18-Day_Campaign_Calendar_A4_Page1.png` & `Page2.png` |
| `scratch/extract_calendar_text.py` | Schedule text extractor | Audits `18-day-campaign-calendar-a3.html` |
| `scratch/install_gotham_fonts.ps1` | Windows font installer | Installs `.otf` files from `Gotham-font-family/` |

## Integrations
- **Google Fonts CDN:** Loads `Montserrat` (600, 700, 800, 900), `Satisfy` (regular), and `Inter` (400, 500, 600, 700, 800).
- **Google Chrome CLI:** Used in headless mode (`--headless=new`) for deterministic rasterization to PNG.

## Important dependencies
- Python 3.x (standard library only: `subprocess`, `time`, `os`, `http.server`, `socketserver`, `threading`, `re`, `html`).
- Google Chrome installed at `C:\Program Files\Google\Chrome\Application\chrome.exe`.
- Active internet connection when rendering (for Google Fonts CDN).

## Constraints
- Canvas containers (`.calendar-canvas` and `.page-canvas`) use fixed pixel dimensions with `overflow: hidden`. Multi-activity cards (especially 3-activity Days 2 and 3, and 5-activity Day 10) require carefully tuned proportional column widths (`grid-template-columns`) and compact typography scales so no venue or partner box is clipped.

## Decisions that must not change casually
- **Fixed 300 DPI Print Canvas Dimensions:** `4961x3508` px for A3 Landscape and `2480x3508` px for A4 Portrait.
- **Proportional Grid Column Widths:** Column fractions (`fr`) in `.grid-7`, `.grid-6.row-2`, `.grid-6.row-3`, `.p1-grid-row*`, and `.p2-grid-row*` are intentionally weighted to give 2-, 3-, and 5-activity days wider horizontal space while keeping 1-activity and weekend online advocacy cards compact.
- **Removal of Participation Targets Footer:** The numerical Participation Targets footer (Male: 975, Female: 1215, Total: 2190 from the original draft) was intentionally removed from the active A3 and A4 layouts to maximize vertical space for daily activity cards.
- **Archive Preservation:** `do not touch/`, `keep copy/`, and `original_unedited_calendar/` must remain untouched as historical baselines.
