# Session Note — 2026-11-11 — Photoshop Studio Layout Preservation Fix

## Objective
Address user feedback: *"why did when you make it layers the layout got destroyed?"*  
Diagnose why the layout degraded when decomposed into layers and implement an architecture that preserves 100% of the approved poster design while providing independent layer control.

## Diagnosis
- In the initial layering step, elements were extracted into a flat array of absolute-positioned `div`s with arbitrary estimated coordinates.
- This discarded the carefully calibrated CSS flexbox rules:
  1. The 2-column details block (`width: 420px` label column + flex value column) was flattened into single strings.
  2. The multi-activity items lost the side-by-side arrangement of numeral (`.act-num`, width 80px) and description (`.act-desc`), as well as the indented lead office row (`margin-left: 98px`).
  3. The Day Badge and Date lost vertical centering alignment next to the 750px/720px Hero Icon.
  4. Line wrapping and spacing degraded across all posters.

## Resolution
- Replaced naive coordinate flattening with a template-embedded non-destructive layer system.
- Injected the exact approved CSS and HTML structures from `scratch/final_html/*.html` into `editor.html`.
- Attached interactive layer handles to each visual unit (`.hero-icon`, `.day-date-group`, `.stroke-title`, each `.act-item`, `.bottom-block`).
- Independent movement is handled via `transform: translate(dx, dy)`.
- Maintained all Photoshop features: 8-handle transform box, double-click inline typing, Arrow key nudging, Layers panel (👁 / 🔒), Character panel, and clearance radar HUD.

## Verification
- Headless Chrome rendered `scratch/editor_preview.png` and `scratch/perfect_studio_tested.png`.
- Visual comparison confirmed exact layout match with approved `FABMAT/` posters.

