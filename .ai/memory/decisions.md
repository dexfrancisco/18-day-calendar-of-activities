# Durable Decisions

## 2026-11-11 — Top Header Branding Update: Orange "STUDIO" Badge
**Decision:**
- Replaced the blue "PS" logo badge in `editor.html` with a campaign-matched vibrant orange badge displaying **"STUDIO"**.
- Styled with `background: #FF6D00; border: 1px solid #FFA04D; color: #FFFFFF; font-weight: 900; letter-spacing: 0.8px; text-transform: uppercase;` with a soft orange ambient glow.
**Reason:** User requested replacing "PS" with "STUDIO" in orange color.
**Status:** Completed & Active

## 2026-11-11 — Photoshop Studio CSS Syntax & Relative Path Resolution
**Issue in User Screenshot:**
In the previous build step, a `<style id="dynamicDayStyle"></style>` tag was accidentally placed inside the main `<head><style>` block in `editor.html`. In HTML parsing, as soon as the browser encounters `</style>`, it terminates the stylesheet; all subsequent CSS rules spilled out into the DOM as visible raw text at the top of the browser window. Furthermore, absolute root paths (`src="/icons/..."` and `url('/FABMAT/...')`) failed to resolve when the user opened `editor.html` directly via `file:///`.

**Fix Delivered:**
1. **Separated Style Blocks:** The main workbench CSS is cleanly closed with `</style>`, followed by `<style id="dynamicDayStyle"></style>` as a dedicated standalone tag.
2. **Relative Path Resolution:** Replaced all `/icons/` and `/FABMAT/` root-relative URLs with standard relative paths (`icons/...` and `FABMAT/...`), ensuring $100\%$ offline compatibility whether opened via `file:///` or HTTP.
3. **Verified Clean Execution:** Headless Chrome screenshot verified clean dark top bar, no raw CSS text spill, fully populated canvas, and working Layers and Properties panels.
**Status:** Completed & Active

## 2026-11-11 — Photoshop Studio Layout Preservation & Non-Destructive Layer System
**Root Cause of Layout Distortion:**
In the previous iteration, attempting to decompose the posters into naive absolute-positioned layers stripped away the calibrated CSS flexbox structures (2-column 420px detail grid for Partners/Venue, side-by-side number + text alignment for activities, indented lead office rows with `margin-left: 98px`, and vertical centering of the Day/Date group next to the Hero Icon). Hardcoded arbitrary $(X, Y)$ coordinates and single-string mergers distorted text wrapping, altered typography scales, and destroyed the approved poster layout.

**Resolution & Fixed Architecture:**
1. **100% Layout Preservation (Zero Distortion):**
   - Directly embedded the exact approved HTML and CSS templates from `scratch/final_html/` (the exact source of the approved `FABMAT/` and `output/` 300 DPI posters).
   - Upon initial load of any day (Pre-Campaign through Day 18), the poster renders with $100\%$ visual parity to the approved final posters.
2. **Non-Destructive Photoshop Layer System:**
   - Attached interactive layer handles (`data-layer-id` and `data-layer-name`) to logical visual blocks:
     - `Hero Icon` (`.hero-icon`)
     - `Day Badge & Date` (`.day-date-group`)
     - `Main Title` / `Activities` (each `.act-item` individually)
     - `Partners & Venue Block` (`.bottom-block`)
   - Independent layer movement operates via non-destructive CSS `translate(dx, dy)` offsets.
   - 8-point transform bounding box wraps the exact rendered element bounding box.
   - Nudging with keyboard Arrow keys (1px / 10px with Shift) updates only the selected layer.
   - Double-clicking text enables direct inline typing (`contenteditable`).
   - Layers panel in the right dock provides visibility toggling (👁), position lock (🔒), and selection.
   - Real-time clearance radar calculates dynamic clearance to $y = 2950$ px.
**Status:** Completed & Active

## 2026-11-11 — Photoshop-Style Individual Layer Architecture & Full Tool Suite
**Decision:**
1. **True Individual Layer Independence (No Container Grouping):**
   - Completely decoupled canvas elements into discrete, independently selectable, movable, and editable layers.
   - **Hero Icon Layer:** Independent draggable, 8-handle resizable image layer with custom asset replacement and file upload.
   - **Day Badge & Date Layers:** Independent draggable, editable text layers with full typography controls.
   - **Activity Titles / Numerals / Lead Offices:** Each activity title and lead office is an independent layer that can be individually repositioned, edited in place, or resized without affecting the rest of the canvas.
   - **Partners & Venue Blocks:** Separate independent layers.
   - **Background Template Layer:** Locked base image layer (`FABMAT/fabmat_template.png`).
2. **Complete Photoshop Tooling Suite:**
   - **Move Tool (V):** Direct canvas click-to-select, drag-and-drop repositioning with smart snapping to canvas center ($X=1240$ px) and margins ($X=190$ px).
   - **Transform Bounding Box:** 8 interactive resize handles (NW, N, NE, E, SE, S, SW, W) with live scaling.
   - **Keyboard Arrow Nudge:** Nudge by 1px with Arrow keys, 10px with `Shift+Arrow`.
   - **Type Tool (T) & Inline Editing:** Double-click on any text block on canvas to enter inline contenteditable mode with live text cursor.
   - **Layers Panel:** Photoshop-grade vertical layer stack with visibility toggling (👁), position lock (🔒), layer reordering (Bring Forward / Send Backward), duplication (`Ctrl+J`), and deletion (`Del`).
   - **History Stack (Undo/Redo):** 40-step visual history panel with `Ctrl+Z` (Undo) and `Ctrl+Y` / `Ctrl+Shift+Z` (Redo).
   - **Character & Properties Panel:** Live controls for X, Y, W, H, Opacity, Font Family, Font Size, Line Height, Text Align, Text Color, Stroke Width, and Stroke Color.
   - **Dual Rulers:** Pixel-accurate top and left rulers tracking mouse coordinates.
   - **Anti-Hazard Radar HUD:** Dynamic clearance calculation against jeepney ($y \ge 2950$) and road ($y \ge 3388$).
   - **300 DPI Export:** Native HTML5 canvas compositing and downloading print posters at $2480 \times 3508$ px.
**Reason:** User requested that all basic actions of Photoshop be available, and that the icon and text be individually editable and movable rather than moving as an overall group.
**Status:** Completed & Active

## 2026-11-11 — Interactive Webpage Canvas Studio & Photoshop-Style Live Editor
**Decision:**
1. **Interactive Web Canvas Editor (`editor.html`):**
   - Built a zero-dependency, self-contained interactive web editor (`editor.html`, 74.9 KB) that runs directly in any modern browser (via `file:///` or HTTP).
   - Features full Photoshop-like canvas capabilities:
     - **Hover & Selection Inspection:** Real-time visual bounding boxes, element dimensions, coordinates, and layer badges.
     - **Drag & Drop Repositioning:** Smooth pixel-accurate drag with snapping guides at canvas center ($X=1240$ px) and content left margin ($X=190$ px).
     - **Inline & Sidebar Text Editing:** Double-click on canvas text for direct inline editing or use the right-side inspector textarea.
     - **Live Inspector Sliders & Numeric Inputs:** Real-time adjustment of Top/Left coordinates, Icon Size, Font Size, Line Height, Stroke Width, Font Family, and Spacing Gap.
     - **Full 19-Day Switcher:** Dropdown navigation and prev/next shortcuts across all 19 days (Pre-Campaign through Day 18) with complete schedule data embedded directly as JSON.
     - **Anti-Hazard Clearance Radar (Live HUD):** Dynamically tracks element bounds against the jeepney ($y \ge 2950$ px) and asphalt road ($y \ge 3388$ px), glowing green when safe and alerting red when approaching danger zones.
     - **High-Res Export & Config Copy:** One-click copy of JSON layout configuration and direct high-resolution print download.
2. **Local Server Runner (`run_studio.py`):**
   - Created standalone script that automatically finds an available port starting at 8080, serves the workspace over local HTTP, and launches the default browser.
3. **Design Fidelity:**
   - Embedded licensed Gotham fonts (`Gotham Ultra`, `Gotham Bold`, `Gotham Medium`, `Gotham Book`, `Gotham Medium Italic`).
   - Matched exact flat vector orange outline aesthetics (`#FF6D00` outline, pure white fill `#FFFFFF`, zero shadows).
**Reason:** User requested a webpage where they can hover over elements and adjust poster layouts interactively like Photoshop.
**Status:** Completed & Active

## 2026-11-10 — Revised Activity Titles & Day 10 Combined Forum for Posters (Tarp)
**Decision:**
1. **Activity Title Updates across Master Calendars & Daily Posters:**
   - **Day 2 (Nov 26):**
     - A1: `Economic Empowerment for Women Safe Employment and Anti Trafficking Forum`
     - A2: `Rural Women Protection, Livelihood and Cooperative Support Forum`
     - A3: Retained (`GAD Employee Development, Recognition and Organizational Strengthening Program.`)
   - **Day 3 (Nov 27):**
     - A1: `Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women`
     - A2: Retained (`Namnama (PWD Film Viewing)`)
     - A3: `Project SUNSHINE Survivor – Centered Case Management and Referral Review`
     - A4: Retained (`KABATAAN PRO-TECT...`)
   - **Day 4 (Nov 28):**
     - Activity: `Multi-Stakeholder Dialogue on Accountability to Survivors and Community Partnership`
   - **Day 8 (Dec 2):**
     - A1: `Safe Workplace Compliance and Anti-Sexual Harassment Orientation`
     - A2: Retained (`World Aids Day Celebrations 2026 : “Ending Aids Starts with Access”`)
   - **Day 9 (Dec 3):**
     - A1: `Men as Allies and Men Opposed to Violence Everywhere (MOVE) Forum on Healthy Masculinity and Shared Responsibility`
     - A2: `Safeline 922 Emergency Response Simulation and Referral Drill`
   - **Day 10 (Dec 4):**
     - **Master Calendar (A3 / A4):** Detailed breakdown of A1 through A5 retained.
     - **Daily Posters (Tarp System):** A1–A5 combined into a single prominent title: `End VAWC Action Forum: Enhancing Survivor Healthcare, Legal Frameworks, LCAT-VAW Desk Coordination, and Digital Safety Innovations`. Rendered under `single_activity` layout with 580px icon, 78px title, and full lead office / partners list, achieving `y = 2566` (+384px buffer to jeepney).
   - **Day 13 (Dec 7):**
     - A1: `Deepening Session on GFAsT and the GeRL Tool: Province of Isabela – LGUs Edition`
     - A2 & A3: Retained.
   - **Day 15 (Dec 9):**
     - A1: `Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW`
     - A2: Retained (`PROJECT ORANGE RISE...`).
   - **Days 16–18:** Retained all.
2. **Master Calendar Deliverables Synchronized & Rendered:**
   - `18-Day_Campaign_Calendar_A3.png` (4961 × 3508 px, root and `Final Copy/`)
   - `18-Day_Campaign_Calendar_A4_Page1.png` (2480 × 3508 px)
   - `18-Day_Campaign_Calendar_A4_Page2.png` (2480 × 3508 px)
   - `18-Day_Campaign_Calendar_Extracted_Text.txt` (root and `Final Copy/`)
3. **Daily Poster Suite Synchronized & Rendered:**
   - `FABMAT/`: 19 posters (`00-pre-campaign.png` through `18-day-18.png`), 2480 × 3508 px, 300 DPI.
   - `output/1x/`: 19 native posters (2480 × 3508 px, 300 DPI).
   - `output/2x/`: 19 double-density posters (4960 × 7016 px).
   - `output/18-day-campaign-posters.pdf`: Combined 19-page PDF.
   - Automated clearance audit: $100\%$ of posters verified safe and clear of the jeepney and road.
**Reason:** User revision request for updated activity titles and special Day 10 combined forum title for the posters/tarp.
**Status:** Completed & Active

## 2026-11-10 — Expanded Typography & Bottom Canvas Clearance Calibration across All 19 Posters
**Decision:**
1. **Scaled-Up Typography across All Day Types:**
   - Pre-Campaign & Single-Activity Days: Titles scaled to `108px`-`112px` (standard) and `86px`-`92px` (long copy on Days 6 & 14); subtitles at `76px` / `62px`.
   - Multi-Activity Days: Descriptions scaled to `74px` (Days 1, 8, 16), `68px` (Day 9), `58px` (Days 2, 13, 15), `48px` (Day 3), and `44px` (Day 10). Numerals scaled to `64px`-`76px` in Gotham Ultra.
   - Partners & Venue Blocks: Labels scaled up to `50px`-`54px` Gotham Ultra (`width: 400px-420px`), values scaled to `52px`-`58px` Gotham Bold across all posters.
   - Online Advocacy Days: Track tags scaled to `68px`, descriptions to `96px`-`100px`.
2. **Spacing Optimization:**
   - Tightened line heights to `1.15`-`1.16` and reduced inner gaps (6px-8px) to eliminate unnatural empty space between sentences and blocks.
3. **Strict Bottom Artwork Clearance ($100\%$ Verified via Pixel Diff):**
   - Utilized the lower canvas without touching the jeepney artwork ($x \in [1567, 2399], y \ge 2950-3043$ px) or asphalt road ($y \ge 3388$ px).
   - Every single poster finishes above $y = 2930$ px with verified positive buffer:
     `00: y=2743 (+207px)`, `01: y=2918 (+32px)`, `02: y=2838 (+112px)`, `03: y=2882 (+68px)`, `04: y=2837 (+113px)`, `05: y=2572 (+378px)`, `06: y=2739 (+211px)`, `07: y=2631 (+319px)`, `08: y=2769 (+181px)`, `09: y=2765 (+185px)`, `10: y=2842 (+108px)`, `11: y=2546 (+404px)`, `12: y=2572 (+378px)`, `13: y=2771 (+179px)`, `14: y=2808 (+142px)`, `15: y=2680 (+270px)`, `16: y=2683 (+267px)`, `17: y=2627 (+323px)`, `18: y=2509 (+441px)`.
4. **All Deliverables Synchronized:**
   - `FABMAT/`: 19 daily posters (`00-pre-campaign.png` through `18-day-18.png`), 2480 × 3508 px, 300 DPI.
   - `output/1x/`: 19 native posters (2480 × 3508 px, 300 DPI).
   - `output/2x/`: 19 double-density posters (4960 × 7016 px).
   - `output/18-day-campaign-posters.pdf`: Combined 19-page PDF.
**Reason:** User instruction to utilize available bottom space, make titles, partners, and venues larger across all days, and lessen large spacing while strictly preventing text from touching the car or road.
**Status:** Completed & Active

## 2026-11-10 — Full 19-Poster Generation: Flat Header-Matched Orange Outline & Zero Shadows
**Decision:**
1. **Flat Vector Aesthetics (Zero Shadows):**
   - Eliminated all drop-shadows and blur filters from both text elements and transparent hero icons across all 19 posters.
   - Text is rendered flat and clean with pure white fill (`#FFFFFF`) and vivid orange vector outline (`#FF6D00` / `#FA5400`) directly sampled from the template header banner *"18-Day Orange Campaign"*.
2. **Hero Icon Sizing & Top Row:**
   - Standardized hero icons on the left: 750px for single-activity/online days, 640px for 2-activity days, 540px for 3-activity days, 480px for Day 3, and 420px for Day 10.
   - Day badge + Date line stacked on the right.
3. **Activity Section Typography & Alignment:**
   - Single activity days (Pre-Campaign, Days 4, 6, 7, 14): Titles and subtitles centered horizontally in the middle.
   - Multi-activity days (Days 1, 2, 8, 9, 10, 13, 15, 16): Plain numbered items with numbers on the left, lead offices directly below each item, and partners/venue at the very bottom.
   - Strictly zero occurrences of the words "Activity" or "Main Activity".
4. **All User Revisions Incorporated:**
   - Day 14: Title updated to `Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing` with `Awarding of Winners` badge.
   - Day 3: Activity 1 includes `, and Sign Language Orientation.`.
   - Day 7: Title updated to `Gender Sensitivity Training for LGU Employees and LDC Members`.
5. **Deliverables Synchronized:**
   - `FABMAT/`: 19 posters (2480 × 3508 px, 300 DPI)
   - `output/1x/`: 19 native posters (2480 × 3508 px, 300 DPI)
   - `output/2x/`: 19 double-density posters (4960 × 7016 px)
   - `output/18-day-campaign-posters.pdf`: Combined 19-page PDF (18.33 MB)
**Reason:** User praise and confirmation ("WOW, now that looks so Good") of the flat, shadow-free, orange-outline styling.
**Status:** Completed & Active



## 2026-11-10 — Pre-Campaign Fine-Tuning: 750px Hero Icon, Unified White Text, Minimized Spacing
**Decision:**
1. **Hero Icon Enlargement:**
   - Increased hero icon from 570px to **750px**, creating a commanding presence that balances the header block.
2. **Unified White Typography (Matching the Title):**
   - Changed all text fills (Date line, Subtitle, `LEAD OFFICE:`, `PARTNERS:`, `VENUE:`, and detail values) from yellow to **pure white (`#FFFFFF`)**, directly matching the title color.
   - Retained the high-contrast deep purple outline (`#240546`) with `paint-order: stroke fill`.
3. **Minimized Spacing:**
   - Replaced large vertical gaps with tight, compact spacing (~45px between major blocks, 16px between title/subtitle, 18px between detail rows) to ensure sentences and sections are visually cohesive.
4. **Deliverable Updated:**
   - Exported to `FABMAT/00-pre-campaign.png` (2480 × 3508 px, 300 DPI).
**Reason:** User instruction to make the icon bigger, change text color to match the title (white), and minimize spacing.
**Status:** Active (Awaiting User Review)

## 2026-11-10 — Full 19-Poster Generation: Calibrated Direct Canvas, Text Stroke Outlines, Zero Boxes
**Decision:**
1. **Direct Canvas Rendering with Deep Purple Text Stroke:**
   - Text is rendered directly on the template orange background with zero cards, panels, or container boxes.
   - Contrast is established using vector-level `-webkit-text-stroke` with `paint-order: stroke fill` in deep purple (`#240546`) matching the template banner, paired with soft drop-shadows. This guarantees razor-sharp legibility without occluding letter interiors.
2. **Icon Treatment & Header Layout:**
   - Transparent PNG icons used **as-is** with a natural drop shadow; no circular backgrounds, glowing halos, or borders around the icon.
   - Top row features the hero icon on the left (570px standard, 540px for 2-act, 460px for 3-act, 390px for Day 10) and Day badge + Date line on the right.
3. **Activity Section Typography & Alignment:**
   - Single activity days (Pre-Campaign, Days 4, 6, 7, 14): Title and Subtitle centered horizontally in the middle.
   - Multi-activity days (Days 1, 2, 8, 9, 10, 13, 15, 16): Plain numbered items with yellow numerals (`1.`) on the left, white descriptions, and `LEAD OFFICE:` directly below each item. Strictly zero occurrences of the words "Activity" or "Main Activity".
   - Bottom metadata: `LEAD OFFICE`, `PARTNERS`, and `VENUE` anchored cleanly at the bottom.
4. **All User Revisions Incorporated:**
   - Day 14: Title updated to `Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing` with `Awarding of Winners` badge.
   - Day 3: Activity 1 includes `, and Sign Language Orientation.`.
   - Day 7: Title updated to `Gender Sensitivity Training for LGU Employees and LDC Members`.
5. **Deliverables Synchronized:**
   - `FABMAT/`: 19 posters (2480 × 3508 px, 300 DPI)
   - `output/1x/`: 19 native posters (2480 × 3508 px, 300 DPI)
   - `output/2x/`: 19 double-density posters (4960 × 7016 px)
   - `output/18-day-campaign-posters.pdf`: Combined 19-page PDF (19.33 MB)
**Reason:** User approval of the Pre-Campaign layout and instruction to generate the entire series under the exact same design system.
**Status:** Completed & Active



## 2026-11-10 — Poster Redesign: Grand Luminous Glassmorphic Relayout (High Readability, Eye Comfort, Uniform Icons, Proportional Space Filling)
**Decision:**
1. **Luminous Royal Plum Glassmorphic Plate:**
   - Overcame the low-contrast optical vibration of raw white/yellow text on bare orange by introducing a single unified translucent plate (`linear-gradient(160deg, rgba(34, 6, 62, 0.78) 0%, rgba(16, 2, 30, 0.84) 100%)`) with `backdrop-filter: blur(28px)` and warm golden amber border (`rgba(255, 183, 77, 0.55)`).
   - Lets the underlying orange/purple template gradient shine through with depth and luminosity while guaranteeing a certified **14:1 contrast ratio**.
   - Strictly avoided nested box anti-patterns by using clean, open typography directly on the glass plate.
2. **Standardized Hero Icon Presentation:**
   - Unified icon containers across all 19 posters (320px/340px) with warm ambient radial glow and drop shadow.
3. **Proportional Vertical Space Distribution:**
   - *Single-Activity Days (Pre-Campaign, Days 4, 6, 7, 14):* Centered hero icon, bold orange day badge (72px), bright golden yellow date (46px), commanding 78px Gotham Ultra headline, and generous bottom metadata grid.
   - *2-Activity Days (Days 1, 2, 8, 9, 13, 15, 16):* Header row with hero icon on left; two spacious activity cards with 58px golden numeral badges, 42px bold white titles, and 30px amber lead offices distributed with `justify-content: space-evenly;` to eliminate empty caverns.
   - *3–5 Activity Days (Days 3, 10):* Compact header, 40px golden numeral badges, 30px bold descriptions, and structured metadata footer.
   - *Online & Hybrid Days (Days 5, 11, 12, 17, 18):* Distinct visual treatment for digital advocacy tracks and in-person highlights.
4. **Safe Zone Bounds Verified:**
   - Container positioned at $y \in [1290, 2940]$ px, strictly preserving the header title banner ($y < 1280$) and footer artwork ($y > 2964$) with 100% automated pass.
**Reason:** User feedback to relayout the posters for superior readability, eye comfort, uniform icon sizing, and eliminating dead vertical spaces.
**Impact:** Synchronized in `generate_posters.py`, regenerating all 19 1x posters, 19 2x posters, and the combined 19-page PDF.
**Status:** Active

## 2026-11-10 — Direct-on-Orange Design Architecture: Zero Panels/Cards, Layout A & Layout B, Double Drop-Shadows
**Decision:**
1. **Eliminated All Panels and Containers:**
   - Removed all white background cards, semi-opaque containers, boxes, and pill wrappers around activities.
   - Text is rendered directly onto the template's warm orange/purple background.
2. **Two Complementary Layout Architectures:**
   - **Layout A (Standard Days: Pre-Campaign, Days 4, 5, 6, 7, 12, 14):**
     - Hero icon (520–660 px) centered with 50px soft white glow, deep purple drop-shadow, and 2–3 four-point yellow sparkles.
     - Centered Day label in Gotham Ultra/Black (`#FFFFFF`, 170–190 px).
     - Centered Date line in Gotham Bold (`#FFE650`, 70–80 px).
     - Centered 7px thick white divider line (1400 px wide, rounded).
     - Centered Activity title in Gotham Bold (`#FFFFFF`, 74–96 px) + yellow italic subtitle (Pre-Campaign).
     - Left-aligned 2-column details grid from 270 px (labels in yellow small-caps 54 px, values in white 58 px, yellow pin icon for venue).
   - **Layout B (Heavy Days: Days 1, 2, 3, 8, 9, 10, 11, 13, 15, 16, 17, 18):**
     - Compact horizontal header: hero icon (310 px) on left, day badge (175 px, white) + date line (58 px, yellow) stacked on right.
     - 7px thick white divider spanning the 1940 px content column.
     - Numbered activities as plain text (yellow numeral, white description 42–46 px, yellow/white Lead Office).
     - Compact details grid (labels yellow 40 px, values white 42 px, yellow pin icon for venue).
     - Activity date ranges next to descriptions; tags (`IN-PERSON` / `ONLINE`) for hybrid days.
3. **Contrast and Shadow Formulation:**
   - White (`#FFFFFF`) and yellow (`#FFE650`) text only.
   - Deep-purple double drop-shadow (`rgba(59, 22, 120, 0.45)` blur 14px offset 8px; `rgba(59, 22, 120, 0.60)` blur 3px offset 4px) ensures crisp legibility directly over the bright orange canvas without any background panel.
4. **Safe Content Zone Calibration:**
   - Safe zone: $y \in [1280, 2964]$ (36.5% to 84.5% page height) and 11% side margins ($x \in [270, 2210]$ px).
   - Container positioned at `top: 1316px; height: 1612px;` to account for icon white glow (+26px top spread) and text shadow (+14px bottom spread).
   - 100% of all 19 posters passed pixel-level bounding box audit.
**Reason:** User requirement for a clean, direct-on-template look with zero card containers, maximum visual impact, distinct standard vs heavy layouts, and guaranteed safe-zone compliance.
**Impact:** Synchronized in `generate_posters.py`, regenerating all 19 1x posters, 19 2x posters, and the combined 19-page PDF.
**Status:** Active

## 2026-11-10 — Poster Redesign: Removal of White Background, Uniform Icon Sizing, Free Space Filling, High-Contrast Typography
**Decision:**
1. **Removed White Card Background:**
   - Completely removed the large semi-opaque white panel (`.poster-card`) that previously covered the poster.
   - The template's native orange/peach gradient background now shows through across the entire poster canvas.
   - Content is structured in rich deep royal purple translucent containers (`rgba(36, 8, 70, 0.90)`) with warm orange accent borders (`#FF9800`) and soft shadows.
2. **Unified Hero Icon Sizing:**
   - Standardized all 19 posters to have the exact same hero icon size: `360px × 360px` in a 360px high header block.
3. **Vertical Free Space Distribution:**
   - Safe zone height calibrated to 1670px ($y \in [1268, 2938]$).
   - Layouts employ flexible height distribution (`flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;`), eliminating large empty voids on light and medium days.
4. **Enhanced Typography & Readability:**
   - Body text set in pure white (`#FFFFFF`) on deep royal purple cards at 38px to 62px Gotham Medium/Bold with 1.3 to 1.45 line-heights for optimal visual comfort.
   - Section and lead labels set in golden amber (`#FFD54F` / `#FFB74D`) uppercase small-caps.
   - Partners text set in soft lavender (`#E2D7F3`).
   - Day badge in deep purple with white text, and date in deep purple with soft outline.
**Reason:** User feedback to remove the white background, make icons uniform in size across all pages, expand elements to occupy empty vertical spaces, and optimize readability.
**Impact:** Synchronized in `generate_posters.py`, regenerating all 19 1x posters, 19 2x posters, and the combined 19-page PDF.
**Status:** Active

## 2026-11-10 — Day 7 Activity Title Realignment (Gender Sensitivity Training)
**Decision:**
1. **Day 7 (Dec 1) Activity Title Updated:**
   - Changed Main Activity to: `Gender Sensitivity Training for LGU Employees and LDC Members`.
   - Lead Office: `CHRMO & CODI`.
   - Partners: `DILG, HR Office, GAD Office, CSOs` (DILG first).
   - Venue: `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
2. **Preserved Layout Quality:**
   - Maintained clean single-activity layout hierarchy (`.card-body-single`) with zero clipping and optimal vertical breathing space.
**Reason:** Official LGU Cauayan campaign realignment updating the Day 7 capacity-building focus to Gender Sensitivity Training for LGU employees and Local Development Council members.
**Alternatives:** Retaining preliminary "Safe workplace, anti-sexual harassment" general description.
**Impact:** Synchronized across all 5 HTML templates (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, `18-day-campaign-calendar-a4.html`, and `Final Copy/`), text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-11-09 — Day 3 Activity 1 Description Update (Sign Language Orientation)
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

## 2026-11-09 — Day 14 Activity Title Expansion
**Decision:**
1. **Day 14 (Dec 8) Activity Name Updated:**
   - Changed Main Activity title to: `Orange Exhibit and Orange Bubble Culture Arts and Public Advocacy: Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing`.
   - Maintained `Awarding of Winners` badge cleanly aligned under the main description.
2. **Typography & Layout Adjustments:**
   - Reduced `.single-act-desc.dense` font size to 27.5px / 1.25 line-height (A3) and 20px / 1.20 line-height (A4) to accommodate the comprehensive activity title with zero vertical clipping.
   - Rebalanced December Row 3 column proportions on A3 (`1.16fr 1.14fr 1.30fr 1.14fr 0.90fr 0.68fr`) and Row 2 on A4 Page 2 (`1.02fr 1.14fr 1.42fr 1.12fr 1.02fr`) to allocate optimal horizontal breathing room for Day 14.
**Reason:** Official LGU Cauayan campaign alignment expanding the Day 14 activity to formally include the Orange Exhibit and Orange Bubble Culture Arts advocacy program.
**Alternatives:** Truncating or omitting parts of the full event title.
**Impact:** Synchronized across all 5 HTML templates (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, `18-day-campaign-calendar-a4.html`, and `Final Copy/`), text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-11-05 — Day 15 Expansion: PROJECT ORANGE RISE
**Decision:**
1. **Day 15 (Dec 9) Expanded to 2 Activities:**
   - Converted card from single-activity layout (`.card-body-single`) to 2-activity multi layout (`.card-body-multi` / `.sub-act-item-2`):
     - **Activity 1:** Lead Office: `Culminating Activity led by LGU Cauayan` — Main Activity: `Awarding of all barangays & offices, recognition of partners, presentation of commitments, and ceremonial signing of Memorandum of Partnership with NAPC and OPAPRU.`
     - **Activity 2:** Lead Office: `GAD Office` — Main Activity: `PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run`
2. **Consolidated Partners with DILG Priority:**
   - Unified all Day 15 partner agencies into the top-of-venue partner box, keeping DILG strictly first:
     `DILG, NAPC, OPAPRU, PCW, CEDIPO, CSWDO, City Budget Office, City Accounting Office, GSO, DTI, TESDA, Cooperatives, Barangay Local Government Units, All Offices, All Partners, CSOs`
3. **Proportional Grid Realignment:**
   - A3 Landscape Row 3 (`.grid-6.row-3`): Realigned grid fractions to `1.20fr 1.05fr 1.35fr 1.15fr 0.92fr 0.68fr` to give Day 15 (Column 3) optimal width for two distinct activity blocks.
   - A4 Portrait Page 2 Row 2 (`.p2-grid-row2`): Realigned column widths to `1.05fr 1.05fr 1.48fr 1.12fr 1.04fr` for balanced card density.
**Reason:** Official LGU Cauayan GAD Office program update integrating the economic enterprise empowerment initiative (PROJECT ORANGE RISE) into the Day 15 Culminating Program.
**Alternatives:** Adding PROJECT ORANGE RISE to another date or keeping Day 15 single-activity.
**Impact:** Synchronized across all 5 HTML templates (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, `18-day-campaign-calendar-a4.html`, and `Final Copy/`), text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-10-29 — Venue Realignment (Days 1, 2, 10) & Day 8 World AIDS Day Expansion
**Decision:**
1. **Day 1 (Nov 25) Venue Updated to CITYWIDE:**
   - Changed venue from `City Sports Complex, Tagaran` to `CITYWIDE`.
2. **Day 2 (Nov 26) Venue Updated to F. L. Dy Coliseum:**
   - Changed venue from `Isabela Convention Center (ICON)` to `F. L. Dy Colliseum, District III, Cauayan City, Isabela` (A3) / `F. L. Dy Colliseum, District III` (A4).
3. **Day 8 (Dec 2) Expanded to 2 Activities:**
   - Added Activity 2 — Lead Office: `City Health Office (CHO)`, Main Activity: `World Aids Day Celebrations 2026 : "Ending Aids Starts with Access"`.
   - Card converted from single-activity to 2-activity multi layout (`.card-body-multi` / `.sub-act-item-2`).
   - Consolidated partners (`DILG, HR Office, GAD Office, CSOs`) placed directly above venue box with DILG first.
   - On A4 Page 1, balanced Row 3 column proportions (`0.82fr 1.25fr 1.35fr`).
4. **Day 10 (Dec 4) Venue Updated to Isabela Convention Center (ICON):**
   - Changed venue from `F. L. Dy Colliseum` to `Isabela Convention Center, San Fermin, Cauayan City, Isabela` (A3) / `Isabela Convention Center (ICON)` (A4).
**Reason:** Official venue scheduling swaps and integration of the 2026 World AIDS Day commemoration under the City Health Office on Day 8.
**Alternatives:** Retaining preliminary venue assignments.
**Impact:** Synchronized across all 5 HTML templates (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`, `18-day-campaign-calendar-a4.html`, and `Final Copy/`), text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-10-28 — Removal of 4 Top Pillars & Canvas Readability Expansion
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

## 2026-10-28 — Multi-Activity Card Consolidated Partner Architecture & Universal DILG Priority
**Decision:**
1. **Consolidated Card Partner Box Above Venue:**
   - In all multi-activity cards, sub-activity partner boxes (.sub-partner-box) were removed from individual items.
   - All partners across the activities under that venue are consolidated into a single, shared partner box (.card-partner-box) placed directly above the venue box (.card-venue-box).
   - Duplicate partners across activities within each card are deduplicated.
2. **Universal DILG First Position Rule:**
   - In any partner list where DILG is present, DILG must always be listed first:
     - **Pre-Campaign:** DILG, LGU Offices, Liga ng mga Barangay, CCGLO
     - **Day 7 & Day 8:** DILG, HR Office, GAD Office, CSOs
     - **Day 10 (Consolidated):** DILG, PNP, BJMP, City Prosecutor's Office, PAO, Barangays, Barangay Officials, BSWDO, Hospitals, RHUs, NGOs, Mental Health Partners, GAD Office, Tech Partners, JCI
     - **Day 13 (Consolidated):** DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS, IT Office, Planning Office, All Offices
     - **Day 15:** DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs
3. **Dual-Venue Scope (Day 3):**
   - For activities under Venue 1 (Activities 1, 2, 3), their partners are consolidated into .card-partner-box directly above Venue 1:
     CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group
   - For Activity 4 under Venue 2, its partners go directly above Venue 2:
     City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School
4. **Other Consolidated Multi-Activity Cards:**
   - **Day 1:** All City Offices, Barangays, PNP, BFP, BJMP, CSWD, Academe, CSOs
   - **Day 2:** DA, DOLE, DTI, OWWA, COA, Cooperatives, MSMES, Barangays, CSOs, Private Sector
   - **Day 9:** PNP, BFP, BJMP, CDRRMO, MDRRMO, All Teams, JCI, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan
   - **Day 16:** DEPED RO2, SDO Cauayan City, CSOs
**Reason:** Eliminates redundant partner rows across sub-activities in multi-activity cards, dramatically improves card vertical hierarchy and legibility, prevents text clipping, and standardizes governance prominence by placing DILG first across all collaborative matrices.
**Alternatives:** Retaining individual sub-partner tags on every activity item, which crowded Day 10 and Day 3.
**Impact:** Synchronized across all 4 HTML layouts (18-day-campaign-calendar-a3.html, 18-day-campaign-calendar.html, 18-day-campaign-calendar-a4-page1.html, 18-day-campaign-calendar-a4-page2.html, 18-day-campaign-calendar-a4.html, and Final Copy/), text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-10-22 — Dual Print Format Architecture (A3 Landscape + 2-Page A4 Portrait)
**Decision:** Maintain the 18-Day Campaign Calendar in two fixed-resolution 300 DPI HTML/CSS canvas formats: a single-page A3 Landscape poster (`4961x3508` px / `420mm x 297mm`) and a two-page A4 Portrait document (`2480x3508` px / `210mm x 297mm` per page, split into `page1` and `page2` files for headless Chrome PNG export).
**Reason:** Supports both large-format wall poster printing (A3) and standard office/handout printing (A4) while using deterministic headless Chrome rasterization.
**Alternatives:** Responsive single-file fluid web layout, or desktop publishing binaries (InDesign/Canva) that cannot be version-controlled and diffed as code.
**Impact:** Every schedule change must be applied to both the A3 HTML files (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`) and the A4 HTML files (`18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`, `18-day-campaign-calendar-a4-page2.html`), followed by running `scratch/render_a3_png.py` and `scratch/render_a4_png.py`.
**Status:** Active

## 2026-10-27 — Removal of Participation Targets Footer & Proportional Grid Weighting
**Decision:** Remove the bottom "Participation Targets" footer bar (Male: 975, Female: 1215, Total: 2190) from the rendered HTML body and use non-uniform proportional CSS Grid column widths (`fr` units) tailored to each day's activity count.
**Reason:** Multi-activity days (such as 5-activity Day 10 and 3-activity Days 2 and 3) required significantly more vertical and horizontal area to remain legible at print scale without clipping.
**Alternatives:** Uniform equal-width 6/7-column grids with much smaller font sizes.
**Impact:** Maximizes calendar grid height and gives dense multi-activity cards wider columns (e.g., `1.98fr` on A3 and `2.45fr` on A4 Page 2 for Day 10) while keeping weekend online advocacy cards compact (`0.64fr`–`0.75fr`).
**Status:** Active

## 2026-10-28 — Schedule Revisions on Day 1, Day 3, and Day 14 (Commit `b342179`)
**Decision:**
1. **Day 1 (Nov 25):** Split into 2 activities — Activity 1: GAD Office (*Wellness and Essential Care Distribution for Project S.U.N.S.H.I.N.E Beneficiaries*, Partners: BJMP, PNP, CSWD) and Activity 2: GAD Office & Office of the City Mayor (*Opening Program, Orange Campaign Kickoff, Parade around the City, Policy Call to Action, Project S.U.N.S.H.I.N.E. public launch*), with Venue set to *City Sports Complex, Tagaran*.
2. **Day 3 (Nov 27):** Expanded to 3 activities by inserting Activity 2: GAD Office — *Namnama (PWD Film Viewing)* (Partners: Isabela Artist Club (ISAC), Women with Disabilities Group) between PDAO & OSCA (Activity 1) and CSWDO (Activity 3, with shortened badge *Project S.U.N.S.H.I.N.E. M&E*).
3. **Day 14 (Dec 8):** Updated Main Activity text to *Painting Competition, Spoken Poetry, Declamation and Wearable Fashion Designing* (with *Awarding of Winners* badge).
4. Removed root `18-Day_Campaign_Calendar_Extracted_Text.txt` (commit `109f0e9`).
**Reason:** Reflects the latest official LGU Cauayan GAD Office campaign schedule adjustments.
**Alternatives:** Keeping original single-activity Day 1 and 2-activity Day 3 schedule.
**Impact:** Root HTML and PNG files reflect these updates; `Final Copy/` still holds the pre-`b342179` snapshot unless explicitly synced.
**Status:** Superseded by 2026-10-28 Partner Expansions and Day 3 Dual-Venue Architecture.

## 2026-10-28 — Partner Expansions & Day 3 Dual-Venue 4-Activity Architecture
**Decision:**
1. **Pre-Campaign (Nov 16–20):** Updated partners to `DILG, LGU Offices, Liga ng mga Barangay, CCGLO`.
2. **Day 1 (Nov 25):** In Activity 2, replaced trailing generic `Partners` with `PNP, BFP, BJMP, Academe, CSOs` (total partner list: `All City Offices, Barangays, PNP, BFP, BJMP, Academe, CSOs`).
3. **Day 2 (Nov 26):** In Activity 2, added `MSMES` after `Cooperatives` and `CSOs` after `Barangays` (total partner list: `DA, Cooperatives, MSMES, Barangays, CSOs`).
4. **Day 3 (Nov 27):**
   - Added `ISAC` to Activity 3 partners (`Health Office, PNP-WCPD, NGAs, CSOs, ISAC`).
   - Added Activity 4 under Venue 1 with its own Venue 2:
     - Lead Office: `City Population Office`
     - Main Activity: `KABATAAN PRO-TECT (Teen Empowerment and Care Team): Peer Helping Training on Safe Spaces, Mental Health, and ASRH`
     - Partners: `City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School`
     - Venue 2: `Cauayan City Stand Alone Senior High School`
   - Added `.card-body-4act` and `.sub-act-item-4` CSS styling, adjusted typography (19px/21px), and widened column 4 (`1.30fr` on A3 landscape, `1.38fr` on A4 portrait) to ensure zero clipping.
**Reason:** Official program expansion by LGU Cauayan GAD Office, integrating adolescent sexual and reproductive health / teen empowerment training at Cauayan City Stand Alone Senior High School.
**Alternatives:** Stacking Activity 4 inside Venue 1 or moving to a separate day.
**Impact:** Synchronized across all 4 HTML layouts (`18-day-campaign-calendar-a3.html`, `18-day-campaign-calendar.html`, `18-day-campaign-calendar-a4.html`, `18-day-campaign-calendar-a4-page1.html`), text extractions, and 300 DPI PNG renders (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`, and `Final Copy/`).
**Status:** Active

## 2026-10-28 — Partner and Leadership Refinements (Days 6, 7, 8, 9, 10, 13)
**Decision:**
1. **Day 6 (Nov 30):**
   - Lead Office expanded to: `City Youth Development Office, SK Federation of Cauayan City / Kalinga Kabataan Program`.
   - Partners updated to: `DepEd, SK, VM Office, Sangguniang Panlungsod, Youth Groups, Faith Groups, PNP, Legal Office`.
2. **Days 7 & 8 (Dec 1–2):**
   - Replaced `HR Units` with `HR Office` and added `GAD Office` immediately after: `HR Office, GAD Office, DILG, CSOs`.
3. **Day 9 (Dec 3):**
   - In Activity 1 partners: removed `CSOs`, added `JCI, PNP, BJMP, CDRRMO, BFP` in front of `Faith Groups`, and appended `MASON, ROTARY Club of Cauayan` after `DepEd`:
     `JCI, PNP, BJMP, CDRRMO, BFP, Faith Groups, Youth Groups, Academe, DepEd, MASON, ROTARY Club of Cauayan`.
4. **Day 10 (Dec 4):**
   - Activity 1 partners: added `Barangay Officials` (`Hospitals, RHUs, NGOs, Mental Health Partners, BJMP, Barangay Officials`).
   - Activity 2 partners: added `Barangay` (`City Prosecutor's Office, PNP, DILG, BJMP, Barangay`).
   - Activity 5 partners: removed `PLDT`, added `JCI, Barangay Officials` (`GAD Office, PNP, Tech Partners, BJMP, JCI, Barangay Officials`).
5. **Day 13 (Dec 7):**
   - Activity 1 partners: added `DILG` in front of `PCW` (`DILG, PCW, Province of Isabela GFPS, Cauayan City GFPS`).
**Reason:** Official agency and partner alignment by LGU Cauayan GAD Office.
**Alternatives:** Retaining previous generic groupings.
**Impact:** Synchronized across all 4 HTML templates, root and `Final Copy/` text extractions, and 300 DPI PNG exports (`18-Day_Campaign_Calendar_A3.png`, `18-Day_Campaign_Calendar_A4_Page1.png`, `18-Day_Campaign_Calendar_A4_Page2.png`).
**Status:** Active

## 2026-10-28 — Program Revisions for Culminating & Regional Activities (Days 14, 15, 16, 17)
**Decision:**
1. **Day 14 (Dec 8):**
   - In Lead Office, removed `City Tourism / Culture Office` and added after `GAD Office`: `DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs`.
   - Full Lead Office line: `PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs`.
2. **Day 15 (Dec 9):**
   - Added `DILG` before `NAPC` and `Barangay, CSOs` after `All Partners`:
     `DILG, NAPC, OPAPRU, PCW, All Offices, All Partners, Barangay, CSOs`.
3. **Day 16 (Dec 10):**
   - Reordered partners to move `DEPED RO2` to the left of `SDO Cauayan City`, and appended `CSOs`:
     `DEPED RO2, SDO Cauayan City, CSOs`.
4. **Day 17 (Dec 11):**
   - Updated Main Activity to `Regional Educational Research Conference`.
   - On A4 Page 2, upgraded Day 17 card to active format displaying this in-person conference, venue, and partners, while balancing row proportions.
**Reason:** Official LGU Cauayan GAD Office program updates for the culminating week and regional research partnerships.
**Alternatives:** Retaining preliminary activity titles and partner sets.
**Impact:** Synchronized across all 4 HTML templates, root and `Final Copy/` text extractions, and 300 DPI PNG exports.
**Status:** Superseded by 2026-10-28 Rescheduling & Realignment.

## 2026-10-28 — Activity Rescheduling & Realignment (Days 13, 16, 17, 18)
**Decision:**
1. **Day 13 (Dec 7):** Added Activity 3 — Lead Office: `GAD Office`, Main Activity: `Display of Orange Exhibits` (card upgraded to `.card-body-3act` / `.sub-act-item-3` with 3 activities).
2. **Day 16 (Dec 10):** Copied the in-person conference from Day 17 (`Regional Educational Research Conference`, Partners: `SDO Cauayan City, DEPED RO2`) as Activity 2 alongside Activity 1 (`GAD in Action`). Card converted to a 2-activity layout (`.card-body-multi` / `.sub-act-item-2`).
3. **Day 17 (Dec 11):** Retained `Regional Educational Research Conference` alongside `ONLINE ADVOCACY` (2-day conference across both Days 16 and 17).
4. **Day 18 (Dec 12):** Replaced `Display of Orange Exhibits` with: Lead Office: `GAD Office`, Main Activity: `Posting of Accomplishment Reports for the 18-day Campaign` (alongside `ONLINE ADVOCACY`).
**Reason:** Clarified user requirement confirming that `Regional Educational Research Conference` is copied onto Day 16 while remaining active on Day 17 (multi-day regional educational research program).
**Alternatives:** Moving the activity and stripping Day 17 to pure online advocacy.
**Impact:** Synchronized across all 4 HTML templates, root and `Final Copy/` text extractions, and 300 DPI PNG exports.
**Status:** Active

## 2026-10-28 — V5 Project-Local AI Context Onboarding
**Decision:** Onboard the repository into the Antigravity V5 project-local `.ai/` memory, state, and planning system without modifying any existing campaign HTML, CSS, script, or image files.
**Reason:** Provides persistent, verified architectural and schedule context for future sessions while strictly preserving working project deliverables.
**Alternatives:** Ad-hoc session discovery without persistent project memory.
**Impact:** Future tasks must consult and maintain `.ai/memory/` and `.ai/state/` in accordance with `GEMINI.md` and `.ai/workflows/memory-update.md`.
**Status:** Active

## 2026-11-10 — Multi-Activity Poster Layout Fine-Tuning & Automated Safe Clearance
**Decision:**
1. **Layout Direction for Multi-Activity Days:** Implemented user-selected **Option 1 (Structured Left-Aligned)**:
   - Numerals (`1.`, `2.`, etc.) placed on the left in their own bold column (`68px` / `76px` Gotham Ultra with `#FF6D00` vector outline). Strictly omitted words "Activity" or "Main Activity".
   - Activity descriptions scaled up to bold, authoritative sizes (`66px` on 2-activity days, `52px` on 3-activity days, `40px` on 5-activity days, `44px` on Day 3 dual-group) with tight `1.16` line height to maximize canvas fill and avoid empty space.
   - Lead Office indented directly under each description with bold label and value.
   - Partners and Venue anchored at the very bottom.
2. **Top-Row Alignment Fix:** Centered `.top-row` flex container in `COMMON_CSS` so that hero icons (`680px` / `750px`) and Day/Date text blocks sit side-by-side on every day type, preventing vertical stacking and ensuring all content strictly finishes above $y = 2850$ px.
3. **Single-Activity Responsive Calibration:** Single-activity days with long titles (Days 4, 6, 14) scaled dynamically (`640px` icon, `76px`-`82px` title) to ensure $100\%$ safe clearance above bottom jeepney graphics.
4. **Automated Verification:** Verified that all 19 posters in `FABMAT/` have positive clearance ($> 0$ px) above the bottom artwork boundary ($y = 2850$ px).
**Reason:** User requested layout adjustment for multiple-activity days to maximize presence, tighten spacing, and align with the approved Pre-Campaign visual identity.
**Alternatives:** Centered activities (rejected in user poll); looser spacing with space-between (rejected due to excessive voids).
**Impact:** `generate_posters.py` updated and executed; all 19 posters regenerated in `FABMAT/`, `output/1x/`, `output/2x/`, and `output/18-day-campaign-posters.pdf`.
**Status:** Active
