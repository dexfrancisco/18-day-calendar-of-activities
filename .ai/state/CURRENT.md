# Current State

## Current feature
18-Day Orange Campaign Daily Poster Generator — Expanded Typography & Bottom Canvas Clearance Calibration across All 19 Posters

## Current task
Completed typography scaling, spacing tightening, and full batch generation of all 19 daily posters:
1. **Scaled Up Titles, Descriptions, Partners & Venue:**
   - Single activity titles scaled to `108px`-`112px` (standard) and `86px`-`92px` (long copy); subtitles `76px` / `62px`.
   - Multi-activity descriptions scaled to `74px` (Days 1, 8, 16), `68px` (Day 9), `58px` (Days 2, 13, 15), `48px` (Day 3), and `44px` (Day 10). Numerals `64px`-`76px` in Gotham Ultra.
   - Partners & Venue labels scaled up to `50px`-`54px` Gotham Ultra (`width: 400px-420px`), values scaled to `52px`-`58px` Gotham Bold across all 19 posters.
2. **Tightened Spacing:**
   - Line heights set to `1.15`-`1.16` and gaps minimized to `6px`-`8px` between titles and lead offices to eliminate large empty voids.
3. **Strict Bottom Artwork Clearance ($100\%$ Verified via Pixel Diff):**
   - Text utilizes the lower canvas without touching the jeepney artwork ($x \in [1567, 2399], y \ge 2950-3043$ px) or road ($y \ge 3388$ px).
   - Every single poster finishes safely above $y = 2930$ px with verified positive buffer.
4. **Deliverables:**
   - `FABMAT/`: 19 daily posters (`00-pre-campaign.png` through `18-day-18.png`), 2480 × 3508 px, 300 DPI.
   - `output/1x/`: 19 native posters (2480 × 3508 px, 300 DPI).
   - `output/2x/`: 19 double-density posters (4960 × 7016 px).
   - `output/18-day-campaign-posters.pdf`: Combined 19-page PDF.

## Status
Completed

## Branch
`master`

## Blocker
None

## Last meaningful change
- Scaled up titles, descriptions, partners, and venues across all 19 posters.
- Tightened line heights and internal spacing.
- Synchronized calibrated layout logic to `generate_posters.py`.
- Generated 1x, 2x, and combined PDF deliverables.
- Verified $100\%$ bottom artwork clearance across all 19 posters via automated pixel analysis.

## Last verification
- Automated clearance audit on all 19 posters in `FABMAT/`: all 19 finish before $y = 2930$ px with positive buffer to the jeepney ($y \ge 2950$ px) and road ($y \ge 3388$ px).
- Visual inspection of rendered thumbnails and bottom crop comparisons.
- Confirmed file existence and dimensions in `FABMAT/`, `output/1x/`, `output/2x/`, and `output/18-day-campaign-posters.pdf`.
