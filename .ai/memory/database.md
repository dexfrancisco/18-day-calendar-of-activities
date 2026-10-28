# Database

## Engine/version
None. This project does not use a database engine.

## Schema overview
Not applicable. Campaign schedule data is stored directly as structured HTML markup (`<article class="day-card ...">`) inside the root `.html` files and summarized in plain-text reference files (`Final Copy/18-Day_Campaign_Calendar_Extracted_Text.txt` and `original_unedited_calendar/extracted_docx_text.txt`).

## Important tables/relations
None (static HTML/CSS repository).Logical domain entities represented in the HTML markup include:
- **Campaign Header & Metadata:** Title, subtitle, LGU location, date range (`November 25 – December 12, 2026`), and campaign theme.
- **Core Pillars (4 items):** Coverage, Convergence Partners, Focus Areas, Integrated Platforms.
- **Pre-Campaign Card (1 item):** `November 16 - 20, 2026` — Barangay Validation of Outstanding GAD Champions (OGAD Champions).
- **Daily Schedule Cards (Days 1–18):** Day number (`DAY 1`–`DAY 18`), calendar date (`NOV 25`–`DEC 12`), weekday (`WED`–`SAT`), card type (Single Activity, Multi-Activity 2/3/5 items, Pure Online Advocacy Weekend, or Hybrid In-Person + Online Advocacy), Lead Office(s), Activity Description(s), Special Event/Initiative badges, Partner Organizations, and Venue.

## Migration policy
Not applicable. Schedule revisions are tracked via Git commits and synchronized across the root HTML layout files.

## Indexing
Not applicable.

## Transactions
Not applicable.

## Audit implementation
No database or server-side audit logging exists. Content changes are audited by comparing Git diffs and running `python scratch/extract_calendar_text.py`.

## Sensitive fields/redaction
None. All schedule information in the repository represents public LGU Cauayan campaign programming and institutional partner listings.
