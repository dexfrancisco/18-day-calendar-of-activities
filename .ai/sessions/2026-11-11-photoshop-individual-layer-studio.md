# Session Note — 2026-11-11 — Photoshop-Style Individual Layer Studio

## Objective
Upgrade the web canvas editor (`editor.html`) so that all basic actions of Photoshop are available, and each icon and text element is an independent layer that can be individually moved, resized, and edited—without moving elements as an overall group.

## Deliverables & Architecture
1. **Decoupled Individual Layer Architecture:**
   - Every single visual element (Hero Icon, Day Badge, Date Line, each Activity Title, each Lead Office, Partners, Venue) is now an independent layer in `layers` array.
   - Selecting and moving the Hero Icon moves ONLY the Hero Icon.
   - Selecting and moving any text block moves ONLY that text block.
2. **Full Photoshop Action Suite:**
   - **Move Tool (V):** Direct canvas selection, drag-and-drop, center snapping ($X=1240$ px), and margin snapping ($X=190$ px).
   - **Transform Bounding Box:** 8 interactive resize handles (NW, N, NE, E, SE, S, SW, W).
   - **Arrow Key Nudge:** 1px nudging with Arrow keys, 10px with `Shift+Arrow`.
   - **Type Tool (T) & Inline Editing:** Double-click on any text block on canvas to type directly with a live cursor.
   - **Layers Panel (Dock Tab 1):** Reverse z-order stack, eye toggle (👁), lock toggle (🔒), duplicate layer (`Ctrl+J`), delete layer (`Del`), bring forward, send backward.
   - **Properties Panel (Dock Tab 2):** X, Y, W, H, Opacity, Font Family, Font Size, Line Height, Text Align, Text Color, Stroke Width, Stroke Color, Icon selector dropdown, and custom image file upload.
   - **History Stack (Dock Tab 3):** 40-step visual undo/redo history with `Ctrl+Z` and `Ctrl+Y`.
   - **Dual Rulers:** Pixel rulers along top and left tracking mouse coordinates.
   - **Clearance Radar HUD:** Live tracking against jeepney ($y \ge 2950$ px) and road ($y \ge 3388$ px).
   - **High-Res 300 DPI Export:** Instant browser composite rendering and download of $2480 \times 3508$ px print poster.

## Verification
- Verified individual layer selection and repositioning in headless Chrome (`scratch/editor_selected_preview.png`).
- Confirmed that moving the icon leaves other layers untouched.
- Verified all 19 campaign days load with calibrated default layers.

