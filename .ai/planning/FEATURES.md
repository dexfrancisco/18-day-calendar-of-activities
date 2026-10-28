# Feature Map

## Core
- **A3 Landscape Print Calendar (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`):** Single-page `4961x3508` px (300 DPI `420mm x 297mm`) poster layout covering the Pre-Campaign validation (`Nov 16–20, 2026`) and all 18 Campaign Days (`Nov 25 – Dec 12, 2026`) with proportional column sizing.
- **A4 Portrait 2-Page Print Calendar (`18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`):** Two-page `2480x3508` px (300 DPI `210mm x 297mm`) portrait layout splitting Pre-Campaign + Days 1–9 onto Page 1 and Days 10–18 onto Page 2.
- **4 Core Pillars Header Framework:** Visual summary cards for Coverage, Convergence Partners, Focus Areas, and Integrated Platforms.
- **Multi-Variant Day Card System:** Specialized CSS card layouts for Pre-Campaign, Single-Activity, 2-Activity, 3-Activity, 5-Activity, Pure Weekend Online Advocacy, and Hybrid In-Person + Online Advocacy days.

## Supporting
- **Headless Chrome PNG Rasterization (`scratch/render_a3_png.py`, `scratch/render_a4_png.py`):** Automated 300 DPI PNG generation using Python's `http.server` and Google Chrome `--headless=new`.
- **Gotham Font Installer (`scratch/install_gotham_fonts.ps1`):** PowerShell script to install the 66 bundled `.otf` fonts from `Gotham-font-family/` into the current Windows user profile.

## Administrative
- **Archive & Milestone Snapshots:** Historical baselines stored in `original_unedited_calendar/`, `do not touch/`, `keep copy/`, and `Final Copy/`.

## Reporting
- **Plain-Text Schedule Extractor (`scratch/extract_calendar_text.py`):** Regex-based script to extract text summaries from `18-day-campaign-calendar-a3.html` (currently requires regex update for multi-activity and inline hybrid cards).

## Future
- Synchronization of `Final Copy/` with the latest root schedule revisions (`b342179`).
- Optional templating or single-source data generation if frequent schedule changes continue across A3 and A4 files.
