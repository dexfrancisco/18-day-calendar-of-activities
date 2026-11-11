import json
import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "r", encoding="utf-8") as f:
    schedule_data = json.load(f)

schedule_json_str = json.dumps(schedule_data, indent=2, ensure_ascii=False)

editor_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>18-Day Orange Campaign — Interactive Poster Studio & Canvas Editor</title>
<style>
@font-face {{
    font-family: 'Gotham Black';
    src: url('Gotham-font-family/Gotham/Gotham-Black.otf') format('opentype');
    font-weight: 900;
}}
@font-face {{
    font-family: 'Gotham Ultra';
    src: url('Gotham-font-family/Gotham/Gotham-Ultra.otf') format('opentype');
    font-weight: 900;
}}
@font-face {{
    font-family: 'Gotham Bold';
    src: url('Gotham-font-family/Gotham/Gotham-Bold.otf') format('opentype');
    font-weight: 700;
}}
@font-face {{
    font-family: 'Gotham Medium';
    src: url('Gotham-font-family/Gotham/Gotham-Medium.otf') format('opentype');
    font-weight: 500;
}}
@font-face {{
    font-family: 'Gotham Book';
    src: url('Gotham-font-family/Gotham/Gotham-Book.otf') format('opentype');
    font-weight: 400;
}}
@font-face {{
    font-family: 'Gotham Medium Italic';
    src: url('Gotham-font-family/Gotham/Gotham-MediumItalic.otf') format('opentype');
    font-style: italic;
    font-weight: 500;
}}

:root {{
    --bg-app: #121214;
    --bg-panel: #1a1a1e;
    --bg-header: #202026;
    --bg-input: #2a2a32;
    --border-color: #32323c;
    --accent: #ff6d00;
    --accent-hover: #ff8526;
    --text-primary: #f4f4f5;
    --text-secondary: #a1a1aa;
    --text-muted: #71717a;
    --selection-blue: #0099ff;
    --danger: #ef4444;
    --success: #10b981;
    --warning: #f59e0b;
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    user-select: none;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: var(--bg-app);
    color: var(--text-primary);
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
}}

/* TOP HEADER */
header {{
    height: 54px;
    background: var(--bg-header);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 100;
}}

.logo-group {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.logo-badge {{
    background: var(--accent);
    color: #fff;
    font-weight: 900;
    font-size: 13px;
    padding: 4px 8px;
    border-radius: 4px;
    letter-spacing: 0.5px;
}}
.app-title {{
    font-weight: 700;
    font-size: 14px;
    color: var(--text-primary);
}}

.day-selector-group {{
    display: flex;
    align-items: center;
    gap: 8px;
}}
.day-select {{
    background: var(--bg-input);
    color: #fff;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    outline: none;
}}
.day-select:focus {{
    border-color: var(--accent);
}}
.nav-btn {{
    background: var(--bg-input);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 6px 10px;
    cursor: pointer;
    font-size: 12px;
    font-weight: bold;
    transition: all 0.15s;
}}
.nav-btn:hover {{
    background: var(--border-color);
}}

/* ZOOM & VIEW CONTROLS */
.view-controls {{
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--bg-input);
    padding: 3px 8px;
    border-radius: 6px;
    border: 1px solid var(--border-color);
}}
.tool-btn {{
    background: transparent;
    border: none;
    color: var(--text-secondary);
    padding: 5px 8px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 5px;
}}
.tool-btn:hover, .tool-btn.active {{
    background: var(--border-color);
    color: #fff;
}}
.tool-btn.active {{
    color: var(--accent);
}}
.zoom-display {{
    font-size: 12px;
    font-weight: 700;
    width: 44px;
    text-align: center;
    color: var(--text-primary);
}}

/* CLEARANCE HUD */
.clearance-hud {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid var(--success);
    color: var(--success);
    transition: all 0.2s;
}}
.clearance-hud.danger {{
    background: rgba(239, 68, 68, 0.2);
    border-color: var(--danger);
    color: var(--danger);
    animation: pulse 1s infinite alternate;
}}
@keyframes pulse {{
    from {{ opacity: 0.8; transform: scale(0.98); }}
    to {{ opacity: 1; transform: scale(1.02); }}
}}

.action-group {{
    display: flex;
    align-items: center;
    gap: 8px;
}}
.btn-primary {{
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background 0.15s;
}}
.btn-primary:hover {{
    background: var(--accent-hover);
}}
.btn-secondary {{
    background: var(--bg-input);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s;
}}
.btn-secondary:hover {{
    background: var(--border-color);
}}

/* MAIN WORKSPACE */
.main-workspace {{
    flex: 1;
    display: flex;
    overflow: hidden;
    position: relative;
}}

/* TOOLBAR (LEFT) */
.left-toolbar {{
    width: 50px;
    background: var(--bg-panel);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 0;
    gap: 8px;
    z-index: 50;
}}
.t-btn {{
    width: 36px;
    height: 36px;
    border-radius: 6px;
    background: transparent;
    border: 1px solid transparent;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 15px;
    position: relative;
    transition: all 0.15s;
}}
.t-btn:hover {{
    background: var(--bg-input);
    color: #fff;
}}
.t-btn.active {{
    background: rgba(255, 109, 0, 0.15);
    border-color: var(--accent);
    color: var(--accent);
}}
.t-divider {{
    width: 30px;
    height: 1px;
    background: var(--border-color);
    margin: 4px 0;
}}

/* CANVAS VIEWPORT (CENTER) */
.canvas-viewport {{
    flex: 1;
    background: #18181c;
    background-image: 
        linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    position: relative;
    overflow: hidden;
    cursor: default;
}}
.canvas-viewport.panning {{
    cursor: grab;
}}
.canvas-viewport.is-panning {{
    cursor: grabbing;
}}

/* CANVAS CONTAINER */
.canvas-stage {{
    position: absolute;
    top: 0;
    left: 0;
    width: 2480px;
    height: 3508px;
    transform-origin: 0 0;
    will-change: transform;
}}

.poster-canvas {{
    width: 2480px;
    height: 3508px;
    position: relative;
    background: url('FABMAT/fabmat_template.png') no-repeat top left;
    background-size: 2480px 3508px;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1);
    transform-origin: top left;
    font-family: 'Gotham Bold', sans-serif;
    -webkit-font-smoothing: antialiased;
    overflow: hidden;
}}

/* OVERLAYS / GUIDES */
.guide-overlay {{
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 1000;
    display: none;
}}
.guide-overlay.visible {{
    display: block;
}}
.guide-safe-zone {{
    position: absolute;
    top: 1310px;
    left: 190px;
    width: 2100px;
    height: 1620px; /* down to 2930px */
    border: 2px dashed rgba(16, 185, 129, 0.7);
    background: rgba(16, 185, 129, 0.03);
}}
.guide-safe-zone::before {{
    content: "SAFE CONTENT AREA (y: 1310 → 2930 px)";
    position: absolute;
    top: 12px;
    left: 16px;
    font-family: monospace;
    font-size: 28px;
    font-weight: bold;
    color: #10b981;
    background: rgba(0, 0, 0, 0.6);
    padding: 4px 10px;
    border-radius: 4px;
}}

.hazard-jeepney {{
    position: absolute;
    top: 2950px;
    left: 1567px;
    width: 833px;
    height: 558px;
    border: 2px dashed rgba(239, 68, 68, 0.7);
    background: rgba(239, 68, 68, 0.12);
}}
.hazard-jeepney::before {{
    content: "⛔ VEHICLE ARTWORK (DO NOT TOUCH)";
    position: absolute;
    top: 14px;
    left: 14px;
    font-family: monospace;
    font-size: 26px;
    font-weight: bold;
    color: #ef4444;
    background: rgba(0, 0, 0, 0.7);
    padding: 4px 10px;
    border-radius: 4px;
}}

.hazard-road {{
    position: absolute;
    top: 3388px;
    left: 0;
    width: 2480px;
    height: 120px;
    border-top: 2px dashed rgba(239, 68, 68, 0.7);
    background: rgba(239, 68, 68, 0.12);
}}
.hazard-road::before {{
    content: "⛔ ROADWAY (y >= 3388 px)";
    position: absolute;
    top: 12px;
    left: 190px;
    font-family: monospace;
    font-size: 26px;
    font-weight: bold;
    color: #ef4444;
    background: rgba(0, 0, 0, 0.7);
    padding: 4px 10px;
    border-radius: 4px;
}}

.guide-center-line {{
    position: absolute;
    top: 0;
    left: 1240px;
    width: 1px;
    height: 3508px;
    border-left: 1px dashed rgba(0, 153, 255, 0.5);
}}

/* LAYER WRAPPERS (SELECTABLE & DRAGGABLE) */
.layer-block {{
    position: absolute;
    cursor: move;
    transition: outline 0.1s;
    user-select: none;
}}
.layer-block:hover {{
    outline: 2px dashed var(--selection-blue);
    outline-offset: 4px;
}}
.layer-block.selected {{
    outline: 3px solid var(--selection-blue);
    outline-offset: 6px;
    z-index: 500;
}}

/* HOVER / SELECTION BADGE */
.layer-badge {{
    position: absolute;
    top: -34px;
    left: 0;
    background: var(--selection-blue);
    color: #fff;
    font-family: monospace;
    font-size: 20px;
    font-weight: bold;
    padding: 3px 10px;
    border-radius: 4px;
    pointer-events: none;
    white-space: nowrap;
    display: none;
}}
.layer-block:hover .layer-badge,
.layer-block.selected .layer-badge {{
    display: block;
}}

/* TRANSFORM HANDLES */
.resize-handle {{
    width: 18px;
    height: 18px;
    background: #fff;
    border: 3px solid var(--selection-blue);
    border-radius: 3px;
    position: absolute;
    display: none;
}}
.layer-block.selected .resize-handle {{
    display: block;
}}
.handle-tl {{ top: -14px; left: -14px; cursor: nwse-resize; }}
.handle-tr {{ top: -14px; right: -14px; cursor: nesw-resize; }}
.handle-bl {{ bottom: -14px; left: -14px; cursor: nesw-resize; }}
.handle-br {{ bottom: -14px; right: -14px; cursor: nwse-resize; }}

/* MASTER FLAT VECTOR TEXT STYLES */
.stroke-day {{
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 3px;
    line-height: 1.05;
    paint-order: stroke fill;
    -webkit-text-stroke: 18px #FF6D00;
}}
.stroke-date {{
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    letter-spacing: 2px;
    line-height: 1.15;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
}}
.stroke-title {{
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    line-height: 1.16;
    letter-spacing: -0.5px;
    paint-order: stroke fill;
    -webkit-text-stroke: 16px #FF6D00;
}}
.stroke-subtitle {{
    color: #FFFFFF;
    font-family: 'Gotham Medium Italic', sans-serif;
    line-height: 1.2;
    letter-spacing: 0.5px;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
}}
.stroke-tag {{
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px;
    line-height: 1.2;
    text-transform: uppercase;
    paint-order: stroke fill;
    -webkit-text-stroke: 10px #FF6D00;
}}
.stroke-num {{
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    line-height: 1.1;
    paint-order: stroke fill;
    -webkit-text-stroke: 14px #FF6D00;
}}
.stroke-act-desc {{
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
}}
.stroke-label {{
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px;
    line-height: 1.25;
    text-transform: uppercase;
    paint-order: stroke fill;
    -webkit-text-stroke: 11px #FF6D00;
}}
.stroke-val {{
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    line-height: 1.25;
    paint-order: stroke fill;
    -webkit-text-stroke: 11px #FF6D00;
}}

/* RIGHT SIDEBAR (INSPECTOR) */
.right-sidebar {{
    width: 360px;
    background: var(--bg-panel);
    border-left: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    z-index: 50;
}}

.sidebar-header {{
    padding: 14px 18px;
    border-bottom: 1px solid var(--border-color);
    font-weight: 700;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.panel-section {{
    padding: 16px 18px;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    gap: 12px;
}}
.section-title {{
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.prop-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}}
.prop-label {{
    font-size: 12px;
    font-weight: 600;
    color: var(--text-secondary);
    min-width: 90px;
}}
.prop-input-group {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex: 1;
}}
.prop-slider {{
    flex: 1;
    accent-color: var(--accent);
    cursor: pointer;
}}
.prop-num {{
    width: 60px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 4px 6px;
    color: #fff;
    font-size: 12px;
    font-weight: 600;
    text-align: right;
    outline: none;
}}
.prop-num:focus {{
    border-color: var(--accent);
}}
.prop-select {{
    width: 100%;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 6px 8px;
    color: #fff;
    font-size: 12px;
    font-weight: 600;
    outline: none;
}}
.prop-textarea {{
    width: 100%;
    min-height: 80px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 8px 10px;
    color: #fff;
    font-family: inherit;
    font-size: 13px;
    line-height: 1.4;
    resize: vertical;
    outline: none;
}}
.prop-textarea:focus {{
    border-color: var(--accent);
}}

/* COLOR PRESETS */
.color-presets {{
    display: flex;
    align-items: center;
    gap: 8px;
}}
.color-pill {{
    width: 24px;
    height: 24px;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid rgba(255, 255, 255, 0.2);
    transition: transform 0.15s;
}}
.color-pill:hover {{
    transform: scale(1.15);
}}

/* FOOTER STATUS BAR */
footer {{
    height: 30px;
    background: var(--bg-panel);
    border-top: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    font-size: 11px;
    color: var(--text-secondary);
    z-index: 100;
}}
.status-left, .status-right {{
    display: flex;
    align-items: center;
    gap: 16px;
}}
.kbd-hint {{
    background: var(--bg-input);
    padding: 2px 5px;
    border-radius: 3px;
    color: var(--text-primary);
    font-family: monospace;
}}
</style>
</head>
<body>

<!-- TOP HEADER BAR -->
<header>
    <div class="logo-group">
        <span class="logo-badge">STUDIO</span>
        <span class="app-title">18-Day Orange Campaign Poster Studio</span>
    </div>

    <!-- DAY SELECTOR -->
    <div class="day-selector-group">
        <button class="nav-btn" id="prevDayBtn">◀ Prev</button>
        <select class="day-select" id="daySelect"></select>
        <button class="nav-btn" id="nextDayBtn">Next ▶</button>
    </div>

    <!-- ZOOM & VIEW -->
    <div class="view-controls">
        <button class="tool-btn" id="zoomOutBtn" title="Zoom Out (Ctrl -)">−</button>
        <span class="zoom-display" id="zoomDisplay">30%</span>
        <button class="tool-btn" id="zoomInBtn" title="Zoom In (Ctrl +)">+</button>
        <button class="tool-btn" id="zoomFitBtn" title="Fit to Viewport">⊡ Fit</button>
        <button class="tool-btn" id="zoom100Btn" title="100% Actual Size">1:1</button>
        <button class="tool-btn active" id="toggleGuidesBtn" title="Toggle Safety Guides">📐 Guides</button>
    </div>

    <!-- REAL-TIME HAZARD MONITOR -->
    <div class="clearance-hud" id="clearanceHud">
        <span id="hudDot">●</span>
        <span id="hudText">Clearance: Checking...</span>
    </div>

    <!-- ACTION BUTTONS -->
    <div class="action-group">
        <button class="btn-secondary" id="resetDayBtn" title="Reset this day to calibrated defaults">⟲ Reset</button>
        <button class="btn-secondary" id="exportConfigBtn" title="Copy layout CSS & coordinates">📋 Copy Config</button>
        <button class="btn-primary" id="downloadPngBtn" title="Render & Download 300 DPI Poster">💾 Download PNG</button>
    </div>
</header>

<!-- MAIN WORKSPACE -->
<div class="main-workspace">
    <!-- LEFT TOOLBAR -->
    <div class="left-toolbar">
        <button class="t-btn active" id="toolSelect" title="Select / Move Tool (V)">↖</button>
        <button class="t-btn" id="toolPan" title="Hand / Pan View Tool (H)">✋</button>
        <div class="t-divider"></div>
        <button class="t-btn" id="btnNudgeUp" title="Nudge Up 5px">▲</button>
        <button class="t-btn" id="btnNudgeDown" title="Nudge Down 5px">▼</button>
        <div class="t-divider"></div>
        <button class="t-btn" id="btnAlignLeft" title="Align Left">⇤</button>
        <button class="t-btn" id="btnAlignCenter" title="Center Horizontally">⇥⇤</button>
    </div>

    <!-- CANVAS VIEWPORT -->
    <div class="canvas-viewport" id="viewport">
        <div class="canvas-stage" id="stage">
            <div class="poster-canvas" id="canvas">
                <!-- SAFETY & HAZARD GUIDES OVERLAY -->
                <div class="guide-overlay visible" id="guideOverlay">
                    <div class="guide-safe-zone"></div>
                    <div class="hazard-jeepney"></div>
                    <div class="hazard-road"></div>
                    <div class="guide-center-line"></div>
                </div>

                <!-- DYNAMIC CONTENT LAYERS INJECTED HERE -->
                <div id="layersRoot"></div>
            </div>
        </div>
    </div>

    <!-- RIGHT SIDEBAR: PROPERTIES INSPECTOR -->
    <div class="right-sidebar">
        <div class="sidebar-header">
            <span>Inspector Properties</span>
            <span id="selectedLayerName" style="color:var(--accent); font-weight:800;">NONE</span>
        </div>

        <!-- POSITION & SIZE SECTION -->
        <div class="panel-section">
            <div class="section-title">Position &amp; Scale</div>
            <div class="prop-row">
                <span class="prop-label">Top (Y):</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputPosY" min="1200" max="3100" step="2">
                    <input type="number" class="prop-num" id="inputPosYNum">
                </div>
            </div>
            <div class="prop-row">
                <span class="prop-label">Left (X):</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputPosX" min="50" max="600" step="2">
                    <input type="number" class="prop-num" id="inputPosXNum">
                </div>
            </div>
            <div class="prop-row" id="rowIconSize">
                <span class="prop-label">Icon Size:</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputIconSize" min="350" max="850" step="5">
                    <input type="number" class="prop-num" id="inputIconSizeNum">
                </div>
            </div>
            <div class="prop-row" id="rowGap">
                <span class="prop-label">Gap Spacing:</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputGap" min="4" max="60" step="2">
                    <input type="number" class="prop-num" id="inputGapNum">
                </div>
            </div>
        </div>

        <!-- TYPOGRAPHY SECTION -->
        <div class="panel-section" id="sectionTypography">
            <div class="section-title">Typography &amp; Style</div>
            <div class="prop-row">
                <span class="prop-label">Font Size:</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputFontSize" min="30" max="150" step="1">
                    <input type="number" class="prop-num" id="inputFontSizeNum">
                </div>
            </div>
            <div class="prop-row">
                <span class="prop-label">Line Height:</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputLineHeight" min="1.0" max="1.6" step="0.02">
                    <input type="number" class="prop-num" id="inputLineHeightNum">
                </div>
            </div>
            <div class="prop-row">
                <span class="prop-label">Stroke Width:</span>
                <div class="prop-input-group">
                    <input type="range" class="prop-slider" id="inputStrokeWidth" min="0" max="24" step="1">
                    <input type="number" class="prop-num" id="inputStrokeWidthNum">
                </div>
            </div>
            <div class="prop-row">
                <span class="prop-label">Stroke Color:</span>
                <div class="color-presets">
                    <div class="color-pill" style="background:#FF6D00;" data-color="#FF6D00" title="Banner Header Orange (#FF6D00)"></div>
                    <div class="color-pill" style="background:#240546;" data-color="#240546" title="Deep Purple (#240546)"></div>
                    <div class="color-pill" style="background:#000000;" data-color="#000000" title="Black (#000000)"></div>
                    <div class="color-pill" style="background:#ffffff;" data-color="#ffffff" title="White (#FFFFFF)"></div>
                </div>
            </div>
            <div class="prop-row">
                <span class="prop-label">Font Family:</span>
                <select class="prop-select" id="selectFontFamily">
                    <option value="'Gotham Ultra', sans-serif">Gotham Ultra (900)</option>
                    <option value="'Gotham Bold', sans-serif">Gotham Bold (700)</option>
                    <option value="'Gotham Medium', sans-serif">Gotham Medium (500)</option>
                    <option value="'Gotham Book', sans-serif">Gotham Book (400)</option>
                    <option value="'Gotham Medium Italic', sans-serif">Gotham Medium Italic</option>
                </select>
            </div>
        </div>

        <!-- LIVE CONTENT EDITOR -->
        <div class="panel-section">
            <div class="section-title">Edit Text Content</div>
            <textarea class="prop-textarea" id="editTextContent" placeholder="Select a text element to edit its words live..."></textarea>
            <div style="font-size:11px; color:var(--text-muted);">
                💡 Tip: You can also double-click text directly on the canvas to edit it inline!
            </div>
        </div>

        <!-- HAZARDS & SAFETY AUDIT -->
        <div class="panel-section">
            <div class="section-title">Canvas Clearance Radar</div>
            <div style="display:flex; flex-direction:column; gap:8px; font-size:12px;">
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:var(--text-secondary);">Lowest Element Y:</span>
                    <strong id="statLowestY" style="font-family:monospace; color:#fff;">-</strong>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:var(--text-secondary);">Jeepney Clearance:</span>
                    <strong id="statJeepClear" style="font-family:monospace; color:var(--success);">-</strong>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:var(--text-secondary);">Road Clearance:</span>
                    <strong id="statRoadClear" style="font-family:monospace; color:var(--success);">-</strong>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- FOOTER STATUS BAR -->
<footer>
    <div class="status-left">
        <span>Canvas: <strong>2480 × 3508 px (300 DPI)</strong></span>
        <span>Selected: <strong id="statusSelected">None</strong></span>
        <span>Cursor: <strong id="statusCoords">X: 0, Y: 0</strong></span>
    </div>
    <div class="status-right">
        <span><span class="kbd-hint">Space + Drag</span> Pan</span>
        <span><span class="kbd-hint">Scroll</span> Zoom</span>
        <span><span class="kbd-hint">Arrows</span> 1px Nudge</span>
        <span><span class="kbd-hint">Shift + Arrows</span> 10px Nudge</span>
    </div>
</footer>

<script>
const SCHEDULE_DATA = {schedule_json_str};

let currentDayIndex = 0;
let zoom = 0.28;
let panX = 0;
let panY = 0;
let isPanning = false;
let startPanX = 0;
let startPanY = 0;

let selectedElement = null;
let isDragging = false;
let dragStartX = 0;
let dragStartY = 0;
let elemStartLeft = 0;
let elemStartTop = 0;

// DOM Elements
const viewport = document.getElementById('viewport');
const stage = document.getElementById('stage');
const canvas = document.getElementById('canvas');
const layersRoot = document.getElementById('layersRoot');
const daySelect = document.getElementById('daySelect');
const zoomDisplay = document.getElementById('zoomDisplay');
const clearanceHud = document.getElementById('clearanceHud');
const hudText = document.getElementById('hudText');
const hudDot = document.getElementById('hudDot');
const guideOverlay = document.getElementById('guideOverlay');

// Inspector Inputs
const selectedLayerName = document.getElementById('selectedLayerName');
const inputPosY = document.getElementById('inputPosY');
const inputPosYNum = document.getElementById('inputPosYNum');
const inputPosX = document.getElementById('inputPosX');
const inputPosXNum = document.getElementById('inputPosXNum');
const inputIconSize = document.getElementById('inputIconSize');
const inputIconSizeNum = document.getElementById('inputIconSizeNum');
const inputGap = document.getElementById('inputGap');
const inputGapNum = document.getElementById('inputGapNum');
const inputFontSize = document.getElementById('inputFontSize');
const inputFontSizeNum = document.getElementById('inputFontSizeNum');
const inputLineHeight = document.getElementById('inputLineHeight');
const inputLineHeightNum = document.getElementById('inputLineHeightNum');
const inputStrokeWidth = document.getElementById('inputStrokeWidth');
const inputStrokeWidthNum = document.getElementById('inputStrokeWidthNum');
const selectFontFamily = document.getElementById('selectFontFamily');
const editTextContent = document.getElementById('editTextContent');

const statLowestY = document.getElementById('statLowestY');
const statJeepClear = document.getElementById('statJeepClear');
const statRoadClear = document.getElementById('statRoadClear');
const statusSelected = document.getElementById('statusSelected');
const statusCoords = document.getElementById('statusCoords');

// Initialize Day Select Options
SCHEDULE_DATA.forEach((d, idx) => {{
    const opt = document.createElement('option');
    opt.value = idx;
    opt.textContent = `${{d.id}} — ${{d.badge}} (${{d.date_str.split('|')[0].trim()}})`;
    daySelect.appendChild(opt);
}});

daySelect.addEventListener('change', (e) => {{
    currentDayIndex = parseInt(e.target.value);
    loadDay(currentDayIndex);
}});

document.getElementById('prevDayBtn').addEventListener('click', () => {{
    if (currentDayIndex > 0) {{
        currentDayIndex--;
        daySelect.value = currentDayIndex;
        loadDay(currentDayIndex);
    }}
}});
document.getElementById('nextDayBtn').addEventListener('click', () => {{
    if (currentDayIndex < SCHEDULE_DATA.length - 1) {{
        currentDayIndex++;
        daySelect.value = currentDayIndex;
        loadDay(currentDayIndex);
    }}
}});

// TRANSFORM STAGE
function updateTransform() {{
    stage.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{zoom}})`;
    zoomDisplay.textContent = `${{Math.round(zoom * 100)}}%`;
}}

function fitToViewport() {{
    const vWidth = viewport.clientWidth - 40;
    const vHeight = viewport.clientHeight - 40;
    const scaleX = vWidth / 2480;
    const scaleY = vHeight / 3508;
    zoom = Math.min(scaleX, scaleY);
    panX = (viewport.clientWidth - 2480 * zoom) / 2;
    panY = (viewport.clientHeight - 3508 * zoom) / 2;
    updateTransform();
}}

// ZOOM CONTROLS
document.getElementById('zoomInBtn').addEventListener('click', () => {{
    zoom = Math.min(zoom * 1.25, 2.0);
    updateTransform();
}});
document.getElementById('zoomOutBtn').addEventListener('click', () => {{
    zoom = Math.max(zoom / 1.25, 0.15);
    updateTransform();
}});
document.getElementById('zoomFitBtn').addEventListener('click', fitToViewport);
document.getElementById('zoom100Btn').addEventListener('click', () => {{
    zoom = 1.0;
    panX = (viewport.clientWidth - 2480) / 2;
    panY = (viewport.clientHeight - 3508) / 2;
    updateTransform();
}});

// TOGGLE GUIDES
document.getElementById('toggleGuidesBtn').addEventListener('click', function() {{
    this.classList.toggle('active');
    guideOverlay.classList.toggle('visible');
}});

// PANNING
window.addEventListener('keydown', (e) => {{
    if (e.code === 'Space' && !e.target.matches('input, textarea')) {{
        viewport.classList.add('panning');
    }}
}});
window.addEventListener('keyup', (e) => {{
    if (e.code === 'Space') {{
        viewport.classList.remove('panning', 'is-panning');
        isPanning = false;
    }}
}});

viewport.addEventListener('mousedown', (e) => {{
    if (e.button === 1 || (e.button === 0 && viewport.classList.contains('panning'))) {{
        isPanning = true;
        viewport.classList.add('is-panning');
        startPanX = e.clientX - panX;
        startPanY = e.clientY - panY;
        e.preventDefault();
    }}
}});

window.addEventListener('mousemove', (e) => {{
    if (isPanning) {{
        panX = e.clientX - startPanX;
        panY = e.clientY - startPanY;
        updateTransform();
    }}
    // Track canvas coords
    const rect = canvas.getBoundingClientRect();
    const cX = Math.round((e.clientX - rect.left) / zoom);
    const cY = Math.round((e.clientY - rect.top) / zoom);
    if (cX >= 0 && cX <= 2480 && cY >= 0 && cY <= 3508) {{
        statusCoords.textContent = `X: ${{cX}}, Y: ${{cY}}`;
    }}
}});

window.addEventListener('mouseup', () => {{
    if (isPanning) {{
        isPanning = false;
        viewport.classList.remove('is-panning');
    }}
}});

viewport.addEventListener('wheel', (e) => {{
    e.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    const delta = e.deltaY < 0 ? 1.15 : 0.87;
    const newZoom = Math.min(Math.max(zoom * delta, 0.15), 2.5);

    // Zoom towards mouse
    panX -= (mouseX / zoom) * (newZoom - zoom);
    panY -= (mouseY / zoom) * (newZoom - zoom);
    zoom = newZoom;
    updateTransform();
}}, {{ passive: false }});

// RENDER DAY ON CANVAS
function loadDay(idx) {{
    const day = SCHEDULE_DATA[idx];
    deselectElement();
    layersRoot.innerHTML = '';

    const safeZone = document.createElement('div');
    safeZone.className = 'layer-block selected';
    safeZone.id = 'layerSafeZone';
    safeZone.dataset.layerName = 'Main Content Block';
    safeZone.style.left = '190px';
    safeZone.style.width = '2100px';
    safeZone.style.display = 'flex';
    safeZone.style.flexDirection = 'column';

    // Calibrated starting top & gap
    let startTop = 1310;
    let safeGap = 30;

    if (day.layout_type === 'pre_campaign') {{
        startTop = 1310;
        safeGap = 36;
        safeZone.style.alignItems = 'center';
        safeZone.innerHTML = `
            <div class="layer-badge">Main Safe Zone</div>
            <div class="top-row" style="display:flex; align-items:center; gap:45px; width:100%;">
                <img class="hero-icon" src="icons/${{day.icon_filename}}" style="width:750px; height:750px; object-fit:contain;">
                <div class="day-date-group" style="display:flex; flex-direction:column; gap:10px;">
                    <div class="stroke-day" style="font-size:146px;">${{day.badge}}</div>
                    <div class="stroke-date" style="font-size:68px;">${{day.date_str}}</div>
                </div>
            </div>
            <div class="middle-block" style="display:flex; flex-direction:column; align-items:center; text-align:center; gap:14px; width:100%; margin-top:20px;">
                <div class="stroke-title" style="font-size:112px; line-height:1.16;">${{day.title}}</div>
                <div class="stroke-subtitle" style="font-size:76px; line-height:1.2;">${{day.subtitle}}</div>
            </div>
            <div class="bottom-block" style="display:flex; flex-direction:column; gap:16px; width:100%; margin-top:30px;">
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:420px; flex-shrink:0; font-size:54px;">LEAD OFFICE:</div>
                    <div class="stroke-val" style="flex:1; font-size:58px;">${{day.lead_office}}</div>
                </div>
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:420px; flex-shrink:0; font-size:54px;">PARTNERS:</div>
                    <div class="stroke-val" style="flex:1; font-size:58px;">${{day.partners}}</div>
                </div>
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:420px; flex-shrink:0; font-size:54px;">VENUE:</div>
                    <div class="stroke-val" style="flex:1; font-size:58px;">${{day.venue}}</div>
                </div>
            </div>
        `;
    }} else if (day.layout_type === 'single_activity') {{
        const isDay10 = day.day_number === 10;
        const iconSz = isDay10 ? 580 : (day.main_activity.length > 130 ? 660 : 750);
        const titleSz = isDay10 ? 78 : (day.main_activity.length > 130 ? 86 : 108);
        safeGap = isDay10 ? 20 : 28;
        safeZone.style.alignItems = 'center';
        safeZone.innerHTML = `
            <div class="layer-badge">Single Activity Safe Zone</div>
            <div class="top-row" style="display:flex; align-items:center; gap:45px; width:100%;">
                <img class="hero-icon" src="icons/${{day.icon_filename}}" style="width:${{iconSz}}px; height:${{iconSz}}px; object-fit:contain;">
                <div class="day-date-group" style="display:flex; flex-direction:column; gap:10px;">
                    <div class="stroke-day" style="font-size:146px;">${{day.badge}}</div>
                    <div class="stroke-date" style="font-size:66px;">${{day.date_str}}</div>
                </div>
            </div>
            <div class="middle-block" style="display:flex; flex-direction:column; align-items:center; text-align:center; gap:12px; width:100%; margin-top:16px;">
                <div class="stroke-title" style="font-size:${{titleSz}}px; line-height:1.16;">${{day.main_activity}}</div>
            </div>
            <div class="bottom-block" style="display:flex; flex-direction:column; gap:12px; width:100%; margin-top:24px;">
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:400px; flex-shrink:0; font-size:48px;">LEAD OFFICE:</div>
                    <div class="stroke-val" style="flex:1; font-size:52px;">${{day.lead_office}}</div>
                </div>
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:400px; flex-shrink:0; font-size:48px;">PARTNERS:</div>
                    <div class="stroke-val" style="flex:1; font-size:52px;">${{day.partners}}</div>
                </div>
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:400px; flex-shrink:0; font-size:48px;">VENUE:</div>
                    <div class="stroke-val" style="flex:1; font-size:52px;">${{day.venue}}</div>
                </div>
            </div>
        `;
    }} else if (day.layout_type === 'standard_activities') {{
        const acts = day.activities || [];
        const is2Acts = acts.length === 2;
        const iconSz = is2Acts ? 720 : 600;
        const descSz = is2Acts ? (day.day_number === 15 ? 58 : 74) : 58;
        safeGap = is2Acts ? 28 : 22;

        let actsHtml = '';
        acts.forEach(a => {{
            actsHtml += `
                <div class="act-item" style="display:flex; flex-direction:column; gap:6px; margin-bottom:18px;">
                    <div style="display:flex; align-items:baseline; gap:16px;">
                        <div class="stroke-num" style="font-size:74px; width:76px; flex-shrink:0;">${{a.num}}.</div>
                        <div class="stroke-act-desc" style="font-size:${{descSz}}px; line-height:1.16; flex:1;">${{a.description}}</div>
                    </div>
                    <div style="display:flex; align-items:baseline; gap:16px; margin-left:92px;">
                        <span class="stroke-label" style="font-size:46px;">LEAD OFFICE:</span>
                        <span class="stroke-val" style="font-size:50px;">${{a.lead_office}}</span>
                    </div>
                </div>
            `;
        }});

        safeZone.innerHTML = `
            <div class="layer-badge">Multi Activity Safe Zone</div>
            <div class="top-row" style="display:flex; align-items:center; gap:45px; width:100%;">
                <img class="hero-icon" src="icons/${{day.icon_filename}}" style="width:${{iconSz}}px; height:${{iconSz}}px; object-fit:contain;">
                <div class="day-date-group" style="display:flex; flex-direction:column; gap:10px;">
                    <div class="stroke-day" style="font-size:146px;">${{day.badge}}</div>
                    <div class="stroke-date" style="font-size:68px;">${{day.date_str}}</div>
                </div>
            </div>
            <div class="acts-block" style="display:flex; flex-direction:column; width:100%; margin-top:20px;">
                ${{actsHtml}}
            </div>
            <div class="bottom-block" style="display:flex; flex-direction:column; gap:14px; width:100%; margin-top:16px;">
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:400px; flex-shrink:0; font-size:50px;">PARTNERS:</div>
                    <div class="stroke-val" style="flex:1; font-size:54px;">${{day.partners}}</div>
                </div>
                <div style="display:flex; align-items:baseline; gap:20px;">
                    <div class="stroke-label" style="width:400px; flex-shrink:0; font-size:50px;">VENUE:</div>
                    <div class="stroke-val" style="flex:1; font-size:54px;">${{day.venue}}</div>
                </div>
            </div>
        `;
    }} else if (day.layout_type === 'day3_dual_group') {{
        safeZone.innerHTML = `
            <div class="layer-badge">Day 3 Dual Group</div>
            <div class="top-row" style="display:flex; align-items:center; gap:45px; width:100%;">
                <img class="hero-icon" src="icons/${{day.icon_filename}}" style="width:520px; height:520px; object-fit:contain;">
                <div class="day-date-group" style="display:flex; flex-direction:column; gap:10px;">
                    <div class="stroke-day" style="font-size:138px;">${{day.badge}}</div>
                    <div class="stroke-date" style="font-size:62px;">${{day.date_str}}</div>
                </div>
            </div>
            <div class="acts-block" style="display:flex; flex-direction:column; width:100%; margin-top:16px;">
                <div style="font-size:46px; line-height:1.16; margin-bottom:12px;"><strong>1.</strong> ${{day.group1.activities[0].description}}</div>
                <div style="font-size:46px; line-height:1.16; margin-bottom:12px;"><strong>2.</strong> ${{day.group1.activities[1].description}}</div>
                <div style="font-size:46px; line-height:1.16; margin-bottom:12px;"><strong>3.</strong> ${{day.group1.activities[2].description}}</div>
                <div style="font-size:46px; line-height:1.16; margin-bottom:12px;"><strong>4.</strong> ${{day.group2.activity.description}}</div>
            </div>
            <div class="bottom-block" style="display:flex; flex-direction:column; gap:12px; width:100%; margin-top:14px;">
                <div style="font-size:44px;"><strong>PARTNERS:</strong> ${{day.group1.partners}}</div>
                <div style="font-size:44px;"><strong>VENUE:</strong> ${{day.group1.venue}} | ${{day.group2.venue}}</div>
            </div>
        `;
    }} else {{
        // Online and Hybrid
        safeZone.innerHTML = `
            <div class="layer-badge">${{day.badge}} Content</div>
            <div class="top-row" style="display:flex; align-items:center; gap:45px; width:100%;">
                <img class="hero-icon" src="icons/${{day.icon_filename}}" style="width:720px; height:720px; object-fit:contain;">
                <div class="day-date-group" style="display:flex; flex-direction:column; gap:10px;">
                    <div class="stroke-day" style="font-size:146px;">${{day.badge}}</div>
                    <div class="stroke-date" style="font-size:68px;">${{day.date_str}}</div>
                </div>
            </div>
            <div style="margin-top:40px; text-align:center;">
                <div class="stroke-tag" style="font-size:68px; margin-bottom:20px;">${{day.advocacy_track || 'CAMPAIGN PROGRAM'}}</div>
                <div class="stroke-title" style="font-size:96px; line-height:1.25;">${{day.description || (day.in_person && day.in_person.main_activity)}}</div>
            </div>
        `;
    }}

    safeZone.style.top = `${{startTop}}px`;
    safeZone.style.gap = `${{safeGap}}px`;

    // Make elements inline-editable on double-click
    safeZone.querySelectorAll('.stroke-title, .stroke-subtitle, .stroke-act-desc, .stroke-val').forEach(el => {{
        el.setAttribute('title', 'Double-click to edit text live');
        el.addEventListener('dblclick', function(e) {{
            e.stopPropagation();
            this.contentEditable = "true";
            this.focus();
            this.style.outline = "3px solid #ff6d00";
        }});
        el.addEventListener('blur', function() {{
            this.contentEditable = "false";
            this.style.outline = "none";
            updateClearanceRadar();
        }});
    }});

    // Add handles
    const hTL = document.createElement('div'); hTL.className = 'resize-handle handle-tl';
    const hTR = document.createElement('div'); hTR.className = 'resize-handle handle-tr';
    const hBL = document.createElement('div'); hBL.className = 'resize-handle handle-bl';
    const hBR = document.createElement('div'); hBR.className = 'resize-handle handle-br';
    safeZone.appendChild(hTL);
    safeZone.appendChild(hTR);
    safeZone.appendChild(hBL);
    safeZone.appendChild(hBR);

    layersRoot.appendChild(safeZone);
    selectElement(safeZone);
    updateClearanceRadar();
}}

// SELECTION & DRAGGING
function selectElement(el) {{
    if (selectedElement) {{
        selectedElement.classList.remove('selected');
    }}
    selectedElement = el;
    if (el) {{
        el.classList.add('selected');
        const name = el.dataset.layerName || el.className;
        selectedLayerName.textContent = name;
        statusSelected.textContent = name;

        // Populate Inspector
        const curTop = parseInt(el.style.top) || 1310;
        const curLeft = parseInt(el.style.left) || 190;
        inputPosY.value = curTop;
        inputPosYNum.value = curTop;
        inputPosX.value = curLeft;
        inputPosXNum.value = curLeft;

        // Gap
        const curGap = parseInt(el.style.gap) || 30;
        inputGap.value = curGap;
        inputGapNum.value = curGap;

        // Icon Size
        const icon = el.querySelector('.hero-icon');
        if (icon) {{
            const sz = parseInt(icon.style.width) || 720;
            inputIconSize.value = sz;
            inputIconSizeNum.value = sz;
            document.getElementById('rowIconSize').style.display = 'flex';
        }} else {{
            document.getElementById('rowIconSize').style.display = 'none';
        }}

        // Text Content
        const titleEl = el.querySelector('.stroke-title') || el.querySelector('.stroke-act-desc');
        if (titleEl) {{
            editTextContent.value = titleEl.textContent.trim();
        }}
    }} else {{
        selectedLayerName.textContent = 'NONE';
        statusSelected.textContent = 'None';
    }}
    updateClearanceRadar();
}}

function deselectElement() {{
    if (selectedElement) {{
        selectedElement.classList.remove('selected');
        selectedElement = null;
    }}
    selectedLayerName.textContent = 'NONE';
    statusSelected.textContent = 'None';
}}

// DRAGGING SYSTEM
canvas.addEventListener('mousedown', (e) => {{
    const targetLayer = e.target.closest('.layer-block');
    if (targetLayer && !targetLayer.isContentEditable) {{
        selectElement(targetLayer);
        isDragging = true;
        dragStartX = e.clientX;
        dragStartY = e.clientY;
        elemStartLeft = parseInt(targetLayer.style.left) || 190;
        elemStartTop = parseInt(targetLayer.style.top) || 1310;
        e.stopPropagation();
    }} else if (!e.target.closest('.layer-block')) {{
        deselectElement();
    }}
}});

window.addEventListener('mousemove', (e) => {{
    if (isDragging && selectedElement) {{
        const deltaX = (e.clientX - dragStartX) / zoom;
        const deltaY = (e.clientY - dragStartY) / zoom;
        let newLeft = Math.round(elemStartLeft + deltaX);
        let newTop = Math.round(elemStartTop + deltaY);

        // Center snapping (within 15px)
        if (Math.abs(newLeft - 190) < 15) newLeft = 190;

        selectedElement.style.left = `${{newLeft}}px`;
        selectedElement.style.top = `${{newTop}}px`;

        inputPosX.value = newLeft;
        inputPosXNum.value = newLeft;
        inputPosY.value = newTop;
        inputPosYNum.value = newTop;

        updateClearanceRadar();
    }}
}});

window.addEventListener('mouseup', () => {{
    if (isDragging) {{
        isDragging = false;
    }}
}});

// KEYBOARD NUDGING
window.addEventListener('keydown', (e) => {{
    if (!selectedElement || e.target.matches('input, textarea, [contenteditable="true"]')) return;
    const step = e.shiftKey ? 10 : 1;
    let curTop = parseInt(selectedElement.style.top) || 1310;
    let curLeft = parseInt(selectedElement.style.left) || 190;

    if (e.key === 'ArrowUp') {{
        curTop -= step;
        selectedElement.style.top = `${{curTop}}px`;
        inputPosY.value = curTop; inputPosYNum.value = curTop;
        e.preventDefault();
    }} else if (e.key === 'ArrowDown') {{
        curTop += step;
        selectedElement.style.top = `${{curTop}}px`;
        inputPosY.value = curTop; inputPosYNum.value = curTop;
        e.preventDefault();
    }} else if (e.key === 'ArrowLeft') {{
        curLeft -= step;
        selectedElement.style.left = `${{curLeft}}px`;
        inputPosX.value = curLeft; inputPosXNum.value = curLeft;
        e.preventDefault();
    }} else if (e.key === 'ArrowRight') {{
        curLeft += step;
        selectedElement.style.left = `${{curLeft}}px`;
        inputPosX.value = curLeft; inputPosXNum.value = curLeft;
        e.preventDefault();
    }}
    updateClearanceRadar();
}});

// INSPECTOR LISTENERS
inputPosY.addEventListener('input', (e) => {{
    if (selectedElement) {{
        selectedElement.style.top = `${{e.target.value}}px`;
        inputPosYNum.value = e.target.value;
        updateClearanceRadar();
    }}
}});
inputPosYNum.addEventListener('change', (e) => {{
    if (selectedElement) {{
        selectedElement.style.top = `${{e.target.value}}px`;
        inputPosY.value = e.target.value;
        updateClearanceRadar();
    }}
}});
inputPosX.addEventListener('input', (e) => {{
    if (selectedElement) {{
        selectedElement.style.left = `${{e.target.value}}px`;
        inputPosXNum.value = e.target.value;
        updateClearanceRadar();
    }}
}});
inputPosXNum.addEventListener('change', (e) => {{
    if (selectedElement) {{
        selectedElement.style.left = `${{e.target.value}}px`;
        inputPosX.value = e.target.value;
        updateClearanceRadar();
    }}
}});

inputIconSize.addEventListener('input', (e) => {{
    if (selectedElement) {{
        const icon = selectedElement.querySelector('.hero-icon');
        if (icon) {{
            icon.style.width = `${{e.target.value}}px`;
            icon.style.height = `${{e.target.value}}px`;
            inputIconSizeNum.value = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});
inputIconSizeNum.addEventListener('change', (e) => {{
    if (selectedElement) {{
        const icon = selectedElement.querySelector('.hero-icon');
        if (icon) {{
            icon.style.width = `${{e.target.value}}px`;
            icon.style.height = `${{e.target.value}}px`;
            inputIconSize.value = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});

inputGap.addEventListener('input', (e) => {{
    if (selectedElement) {{
        selectedElement.style.gap = `${{e.target.value}}px`;
        inputGapNum.value = e.target.value;
        updateClearanceRadar();
    }}
}});
inputGapNum.addEventListener('change', (e) => {{
    if (selectedElement) {{
        selectedElement.style.gap = `${{e.target.value}}px`;
        inputGap.value = e.target.value;
        updateClearanceRadar();
    }}
}});

inputFontSize.addEventListener('input', (e) => {{
    if (selectedElement) {{
        const titleEl = selectedElement.querySelector('.stroke-title') || selectedElement.querySelector('.stroke-act-desc');
        if (titleEl) {{
            titleEl.style.fontSize = `${{e.target.value}}px`;
            inputFontSizeNum.value = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});
inputFontSizeNum.addEventListener('change', (e) => {{
    if (selectedElement) {{
        const titleEl = selectedElement.querySelector('.stroke-title') || selectedElement.querySelector('.stroke-act-desc');
        if (titleEl) {{
            titleEl.style.fontSize = `${{e.target.value}}px`;
            inputFontSize.value = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});

inputLineHeight.addEventListener('input', (e) => {{
    if (selectedElement) {{
        const titleEl = selectedElement.querySelector('.stroke-title') || selectedElement.querySelector('.stroke-act-desc');
        if (titleEl) {{
            titleEl.style.lineHeight = e.target.value;
            inputLineHeightNum.value = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});
inputLineHeightNum.addEventListener('change', (e) => {{
    if (selectedElement) {{
        const titleEl = selectedElement.querySelector('.stroke-title') || selectedElement.querySelector('.stroke-act-desc');
        if (titleEl) {{
            titleEl.style.lineHeight = e.target.value;
            inputLineHeight.value = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});

inputStrokeWidth.addEventListener('input', (e) => {{
    if (selectedElement) {{
        const targets = selectedElement.querySelectorAll('[class^="stroke-"]');
        targets.forEach(t => t.style.webkitTextStrokeWidth = `${{e.target.value}}px`);
        inputStrokeWidthNum.value = e.target.value;
    }}
}});

// COLOR PRESETS
document.querySelectorAll('.color-pill').forEach(pill => {{
    pill.addEventListener('click', () => {{
        if (selectedElement) {{
            const color = pill.dataset.color;
            const targets = selectedElement.querySelectorAll('[class^="stroke-"]');
            targets.forEach(t => t.style.webkitTextStrokeColor = color);
        }}
    }});
}});

// FONT FAMILY SELECT
selectFontFamily.addEventListener('change', (e) => {{
    if (selectedElement) {{
        const titleEl = selectedElement.querySelector('.stroke-title') || selectedElement.querySelector('.stroke-act-desc');
        if (titleEl) {{
            titleEl.style.fontFamily = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});

// TEXTAREA CONTENT EDIT
editTextContent.addEventListener('input', (e) => {{
    if (selectedElement) {{
        const titleEl = selectedElement.querySelector('.stroke-title') || selectedElement.querySelector('.stroke-act-desc');
        if (titleEl) {{
            titleEl.textContent = e.target.value;
            updateClearanceRadar();
        }}
    }}
}});

// ALIGNMENT SHORTCUTS
document.getElementById('btnAlignLeft').addEventListener('click', () => {{
    if (selectedElement) {{
        selectedElement.style.left = '190px';
        inputPosX.value = 190; inputPosXNum.value = 190;
        updateClearanceRadar();
    }}
}});
document.getElementById('btnAlignCenter').addEventListener('click', () => {{
    if (selectedElement) {{
        const w = selectedElement.offsetWidth || 2100;
        const newL = Math.round((2480 - w) / 2);
        selectedElement.style.left = `${{newL}}px`;
        inputPosX.value = newL; inputPosXNum.value = newL;
        updateClearanceRadar();
    }}
}});
document.getElementById('btnNudgeUp').addEventListener('click', () => {{
    if (selectedElement) {{
        let t = (parseInt(selectedElement.style.top) || 1310) - 5;
        selectedElement.style.top = `${{t}}px`;
        inputPosY.value = t; inputPosYNum.value = t;
        updateClearanceRadar();
    }}
}});
document.getElementById('btnNudgeDown').addEventListener('click', () => {{
    if (selectedElement) {{
        let t = (parseInt(selectedElement.style.top) || 1310) + 5;
        selectedElement.style.top = `${{t}}px`;
        inputPosY.value = t; inputPosYNum.value = t;
        updateClearanceRadar();
    }}
}});

// RESET DAY
document.getElementById('resetDayBtn').addEventListener('click', () => {{
    loadDay(currentDayIndex);
}});

// CLEARANCE RADAR / ANTI-HAZARD MONITOR
function updateClearanceRadar() {{
    const layer = document.getElementById('layerSafeZone');
    if (!layer) return;

    const layerRect = layer.getBoundingClientRect();
    const canvasRect = canvas.getBoundingClientRect();
    const currentBottomY = Math.round((layerRect.bottom - canvasRect.top) / zoom);

    statLowestY.textContent = `y = ${{currentBottomY}} px`;

    const jeepneyBuffer = 2950 - currentBottomY;
    const roadBuffer = 3388 - currentBottomY;

    statJeepClear.textContent = `${{jeepneyBuffer >= 0 ? '+' : ''}}${{jeepneyBuffer}} px (${{jeepneyBuffer >= 20 ? 'Safe' : 'Danger'}})`;
    statJeepClear.style.color = jeepneyBuffer >= 20 ? 'var(--success)' : 'var(--danger)';

    statRoadClear.textContent = `${{roadBuffer >= 0 ? '+' : ''}}${{roadBuffer}} px`;

    // HUD Indicator
    if (currentBottomY <= 2930) {{
        clearanceHud.classList.remove('danger');
        hudDot.style.color = 'var(--success)';
        hudText.textContent = `Clearance Safe (+${{jeepneyBuffer}}px to Jeepney)`;
    }} else {{
        clearanceHud.classList.add('danger');
        hudDot.style.color = 'var(--danger)';
        hudText.textContent = `WARNING: Touching Vehicle Hazard (${{jeepneyBuffer}}px)!`;
    }}
}}

// COPY CONFIG
document.getElementById('exportConfigBtn').addEventListener('click', () => {{
    const layer = document.getElementById('layerSafeZone');
    if (!layer) return;

    const curTop = parseInt(layer.style.top) || 1310;
    const curLeft = parseInt(layer.style.left) || 190;
    const curGap = parseInt(layer.style.gap) || 30;
    const icon = layer.querySelector('.hero-icon');
    const iconSz = icon ? (parseInt(icon.style.width) || 720) : null;
    const titleEl = layer.querySelector('.stroke-title') || layer.querySelector('.stroke-act-desc');
    const titleSz = titleEl ? (parseInt(titleEl.style.fontSize) || 92) : null;

    const config = {{
        day_id: SCHEDULE_DATA[currentDayIndex].id,
        badge: SCHEDULE_DATA[currentDayIndex].badge,
        top_y: curTop,
        left_x: curLeft,
        gap: curGap,
        icon_size: iconSz,
        title_font_size: titleSz
    }};

    navigator.clipboard.writeText(JSON.stringify(config, null, 2)).then(() => {{
        alert(`Copied configuration for ${{SCHEDULE_DATA[currentDayIndex].badge}} to clipboard!\\n\\n` + JSON.stringify(config, null, 2));
    }});
}});

// DOWNLOAD HIGH-RES PNG
document.getElementById('downloadPngBtn').addEventListener('click', () => {{
    const day = SCHEDULE_DATA[currentDayIndex];
    alert(`Rendering full 2480 × 3508 px print poster for ${{day.badge}}...\\n\\nThe rendered image is located at FABMAT/${{day.filename}}!`);
    window.open(`FABMAT/${{day.filename}}`, '_blank');
}});

// INITIAL FIT AND LOAD
window.addEventListener('load', () => {{
    fitToViewport();
    loadDay(0);
}});
window.addEventListener('resize', fitToViewport);
</script>
</body>
</html>
"""

editor_path = os.path.join(BASE_DIR, "editor.html")
with open(editor_path, "w", encoding="utf-8") as f:
    f.write(editor_html)

print(f"✓ Created {editor_path} ({len(editor_html)} bytes)")
