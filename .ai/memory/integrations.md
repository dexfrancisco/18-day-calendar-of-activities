# Integrations

## External services
- **Google Fonts CDN (`https://fonts.googleapis.com` & `https://fonts.gstatic.com`):**
  - Loaded via `<link rel="stylesheet">` in all HTML calendar files.
  - Provides `Montserrat` (weights 600, 700, 800, 900), `Satisfy` (regular cursive), and `Inter` (weights 400, 500, 600, 700, 800).

## APIs
- None. No backend, REST, GraphQL, or third-party data APIs are called.

## Authentication integrations
- None.

## Storage/files
- **Local Filesystem Outputs:**
  - `18-Day_Campaign_Calendar_A3.png` (generated from `18-day-campaign-calendar-a3.html`)
  - `18-Day_Campaign_Calendar_A4_Page1.png` (generated from `18-day-campaign-calendar-a4-page1.html`)
  - `18-Day_Campaign_Calendar_A4_Page2.png` (generated from `18-day-campaign-calendar-a4-page2.html`)
- **Local Font Assets:**
  - `Gotham-font-family/`: 66 `.otf` font files installed into `$env:LOCALAPPDATA\Microsoft\Windows\Fonts` when running `scratch/install_gotham_fonts.ps1`.
- **Source Reference Document:**
  - `original_unedited_calendar/18-Day_Campaign_Cauayan_Isabela_2026_Extracted_Details.docx` (and `extracted_docx_text.txt`).

## Third-party dependencies
- **Google Chrome (`C:\Program Files\Google\Chrome\Application\chrome.exe`):** Invoked via Python `subprocess.run` in headless mode (`--headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=5000`) by `scratch/render_a3_png.py` and `scratch/render_a4_png.py`.
- **Python 3 Standard Library:** `http.server`, `socketserver`, `threading`, `subprocess`, `re`, `html`, `os`, `time`.
- **Windows PresentationCore / Win32 GDI (`gdi32.dll`, `user32.dll`):** Used by `scratch/install_gotham_fonts.ps1` to inspect `.otf` glyph metadata and register fonts in the current user's Windows session.

## Constraints
- Rendering scripts hardcode the workspace path (`r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"`), Chrome executable path (`r"C:\Program Files\Google\Chrome\Application\chrome.exe"`), and local TCP ports (`8991` for A3, `8992` for A4).
- Offline environments without cached Google Fonts will fall back to system `sans-serif` / `cursive` during PNG rendering unless fonts are locally hosted or mapped.
