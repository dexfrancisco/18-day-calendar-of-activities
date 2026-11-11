import json
import os

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# Load schedule data and default layers
with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "r", encoding="utf-8") as f:
    schedule_data = json.load(f)

with open(os.path.join(BASE_DIR, "scratch", "default_layers_by_day.json"), "r", encoding="utf-8") as f:
    default_layers_by_day = json.load(f)

# List available icons
available_icons = sorted([f for f in os.listdir(os.path.join(BASE_DIR, "icons")) if f.lower().endswith(".png")])

schedule_json_str = json.dumps(schedule_data, indent=2, ensure_ascii=False)
layers_json_str = json.dumps(default_layers_by_day, indent=2, ensure_ascii=False)
icons_json_str = json.dumps(available_icons, indent=2, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Photoshop Studio — 18-Day Orange Campaign Poster Editor</title>
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
    --bg-app: #181818;
    --bg-panel: #242424;
    --bg-panel-header: #2c2c2c;
    --bg-toolbar: #202020;
    --bg-input: #151515;
    --bg-input-focus: #0f0f0f;
    --border-color: #383838;
    --border-light: #484848;
    --text-primary: #e6e6e6;
    --text-muted: #8e8e8e;
    --text-dim: #606060;
    --accent-blue: #0078d4;
    --accent-blue-hover: #1084d8;
    --accent-orange: #FF6D00;
    --accent-orange-hover: #ff7f1a;
    --danger: #ff4d4f;
    --success: #52c41a;
    --warning: #faad14;
    --selection-outline: #0078d4;
    --handle-size: 10px;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    user-select: none;
    -webkit-user-select: none;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 12px;
    background-color: var(--bg-app);
    color: var(--text-primary);
    overflow: hidden;
    height: 100vh;
    display: flex;
    flex-direction: column;
}}

/* TOP APP BAR */
.app-header {{
    height: 44px;
    background: var(--bg-panel-header);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 14px;
    z-index: 100;
}}

.app-title-group {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.app-logo-badge {{
    background: #001e36;
    border: 1px solid #005a9e;
    color: #40a9ff;
    font-weight: 900;
    font-size: 13px;
    padding: 3px 7px;
    border-radius: 4px;
    letter-spacing: 0.5px;
}}

.app-title {{
    font-weight: 700;
    font-size: 13px;
    color: #fff;
    letter-spacing: 0.3px;
}}

.day-selector-group {{
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--bg-toolbar);
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid var(--border-color);
}}

.day-selector-group label {{
    font-size: 11px;
    color: var(--text-muted);
    font-weight: 600;
    text-transform: uppercase;
}}

.day-select {{
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    color: #fff;
    font-weight: 700;
    font-size: 12px;
    padding: 4px 10px;
    border-radius: 4px;
    outline: none;
    cursor: pointer;
}}

.day-nav-btn {{
    background: #333;
    border: 1px solid var(--border-color);
    color: #ddd;
    font-size: 11px;
    font-weight: bold;
    padding: 4px 8px;
    border-radius: 4px;
    cursor: pointer;
}}
.day-nav-btn:hover {{
    background: #444;
    color: #fff;
}}

.top-actions {{
    display: flex;
    align-items: center;
    gap: 10px;
}}

.btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    font-size: 12px;
    font-weight: 600;
    border-radius: 4px;
    border: 1px solid transparent;
    cursor: pointer;
    transition: all 0.15s ease;
}}

.btn-default {{
    background: #333;
    border-color: var(--border-light);
    color: #e0e0e0;
}}
.btn-default:hover {{
    background: #404040;
    color: #fff;
}}

.btn-primary {{
    background: var(--accent-blue);
    color: #fff;
}}
.btn-primary:hover {{
    background: var(--accent-blue-hover);
}}

.btn-orange {{
    background: var(--accent-orange);
    color: #fff;
}}
.btn-orange:hover {{
    background: var(--accent-orange-hover);
}}

/* OPTIONS BAR */
.options-bar {{
    height: 38px;
    background: var(--bg-panel);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    padding: 0 14px;
    gap: 16px;
    font-size: 11px;
    z-index: 90;
    overflow-x: auto;
}}

.options-group {{
    display: flex;
    align-items: center;
    gap: 8px;
    border-right: 1px solid var(--border-color);
    padding-right: 14px;
}}
.options-group:last-child {{
    border-right: none;
}}

.opt-label {{
    color: var(--text-muted);
    font-weight: 600;
}}

.opt-input {{
    width: 65px;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    color: #fff;
    padding: 3px 6px;
    border-radius: 3px;
    font-size: 11px;
    outline: none;
}}

.opt-input:focus {{
    border-color: var(--accent-blue);
}}

.tool-badge {{
    background: #303030;
    padding: 3px 8px;
    border-radius: 3px;
    color: #aaa;
    font-weight: 700;
}}

/* CLEARANCE RADAR HUD */
.clearance-pill {{
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid #444;
    padding: 3px 10px;
    border-radius: 14px;
    font-size: 11px;
    font-weight: 600;
    margin-left: auto;
}}

.clearance-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--success);
    box-shadow: 0 0 6px var(--success);
}}

.clearance-pill.danger .clearance-dot {{
    background: var(--danger);
    box-shadow: 0 0 8px var(--danger);
}}

/* MAIN WORKBENCH */
.workbench {{
    flex: 1;
    display: flex;
    overflow: hidden;
    position: relative;
}}

/* LEFT TOOLBAR */
.toolbar {{
    width: 48px;
    background: var(--bg-toolbar);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px 0;
    gap: 6px;
    z-index: 80;
}}

.tool-btn {{
    width: 36px;
    height: 36px;
    border-radius: 4px;
    background: transparent;
    border: 1px solid transparent;
    color: #aaa;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    position: relative;
    transition: all 0.15s ease;
}}

.tool-btn:hover {{
    background: #2e2e2e;
    color: #fff;
}}

.tool-btn.active {{
    background: #383838;
    color: #fff;
    border-color: var(--accent-blue);
}}

.tool-divider {{
    width: 28px;
    height: 1px;
    background: var(--border-color);
    margin: 4px 0;
}}

/* CENTER VIEWPORT */
.viewport-container {{
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #121212;
    overflow: hidden;
    position: relative;
}}

.canvas-viewport {{
    flex: 1;
    position: relative;
    overflow: hidden;
    cursor: default;
    background:
        radial-gradient(circle at center, #1c1c1c 0%, #101010 100%),
        repeating-linear-gradient(0deg, transparent, transparent 19px, #181818 20px),
        repeating-linear-gradient(90deg, transparent, transparent 19px, #181818 20px);
}}

/* RULERS */
.ruler-top {{
    position: absolute;
    top: 0;
    left: 20px;
    right: 0;
    height: 20px;
    background: #1c1c1c;
    border-bottom: 1px solid #333;
    z-index: 50;
    overflow: hidden;
}}

.ruler-left {{
    position: absolute;
    top: 20px;
    left: 0;
    bottom: 0;
    width: 20px;
    background: #1c1c1c;
    border-right: 1px solid #333;
    z-index: 50;
    overflow: hidden;
}}

.ruler-corner {{
    position: absolute;
    top: 0;
    left: 0;
    width: 20px;
    height: 20px;
    background: #242424;
    border-right: 1px solid #333;
    border-bottom: 1px solid #333;
    z-index: 55;
}}

/* CANVAS STAGE (2480 x 3508 px) */
.canvas-stage {{
    position: absolute;
    top: 0;
    left: 0;
    width: 2480px;
    height: 3508px;
    transform-origin: 0 0;
    box-shadow: 0 10px 40px rgba(0,0,0,0.85);
}}

.poster-canvas {{
    position: relative;
    width: 2480px;
    height: 3508px;
    background: #000;
    overflow: hidden;
}}

.template-bg {{
    position: absolute;
    top: 0;
    left: 0;
    width: 2480px;
    height: 3508px;
    pointer-events: none;
    z-index: 1;
}}

/* LAYERS CONTAINER */
.layers-container {{
    position: absolute;
    top: 0;
    left: 0;
    width: 2480px;
    height: 3508px;
    z-index: 10;
}}

/* INDIVIDUAL LAYER ELEMENT */
.layer-node {{
    position: absolute;
    cursor: move;
    box-sizing: border-box;
    display: inline-block;
    transition: outline 0.1s ease;
}}

.layer-node:hover:not(.selected) {{
    outline: 2px dashed rgba(0, 120, 212, 0.65);
    outline-offset: 3px;
}}

.layer-node.selected {{
    outline: 3px solid var(--selection-outline);
    outline-offset: 3px;
}}

.layer-node.locked {{
    cursor: not-allowed !important;
}}

/* TEXT LAYER STYLING */
.layer-text {{
    display: block;
    word-break: break-word;
    user-select: text;
    -webkit-user-select: text;
    cursor: text;
    paint-order: stroke fill;
}}

/* HERO ICON LAYER STYLING */
.layer-image {{
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
    pointer-events: none;
}}

/* TRANSFORM BOUNDING BOX & HANDLES */
.transform-box {{
    position: absolute;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 1000;
    display: none;
}}

.transform-box.active {{
    display: block;
}}

.transform-border {{
    position: absolute;
    border: 2px solid var(--accent-blue);
    pointer-events: none;
}}

.transform-handle {{
    position: absolute;
    width: var(--handle-size);
    height: var(--handle-size);
    background: #ffffff;
    border: 1.5px solid var(--accent-blue);
    border-radius: 2px;
    pointer-events: auto;
    z-index: 1002;
    transform: translate(-50%, -50%);
    box-shadow: 0 1px 4px rgba(0,0,0,0.4);
}}

.transform-handle.nw {{ cursor: nwse-resize; }}
.transform-handle.n  {{ cursor: ns-resize; }}
.transform-handle.ne {{ cursor: nesw-resize; }}
.transform-handle.e  {{ cursor: ew-resize; }}
.transform-handle.se {{ cursor: nwse-resize; }}
.transform-handle.s  {{ cursor: ns-resize; }}
.transform-handle.sw {{ cursor: nesw-resize; }}
.transform-handle.w  {{ cursor: ew-resize; }}

/* SMART SNAP GUIDES */
.guide-line {{
    position: absolute;
    pointer-events: none;
    z-index: 999;
    display: none;
}}
.guide-line.vertical {{
    top: 0;
    bottom: 0;
    width: 1px;
    background: #ff00ff;
    box-shadow: 0 0 4px #ff00ff;
}}
.guide-line.horizontal {{
    left: 0;
    right: 0;
    height: 1px;
    background: #ff00ff;
    box-shadow: 0 0 4px #ff00ff;
}}

/* HAZARD ZONE OVERLAY */
.hazard-overlay {{
    position: absolute;
    left: 0;
    width: 2480px;
    pointer-events: none;
    z-index: 20;
    display: none;
}}
.hazard-overlay.jeepney {{
    top: 2950px;
    height: 558px;
    background: rgba(255, 77, 79, 0.12);
    border-top: 2px dashed #ff4d4f;
}}
.hazard-overlay.road {{
    top: 3388px;
    height: 120px;
    background: rgba(255, 77, 79, 0.22);
    border-top: 2px dashed #ff1100;
}}

.hazard-badge {{
    position: absolute;
    right: 40px;
    top: 10px;
    background: rgba(255, 77, 79, 0.9);
    color: #fff;
    font-weight: 800;
    font-size: 26px;
    padding: 6px 14px;
    border-radius: 6px;
    letter-spacing: 1px;
}}

/* RIGHT DOCK (LAYERS / PROPERTIES / HISTORY) */
.dock {{
    width: 370px;
    background: var(--bg-panel);
    border-left: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    z-index: 80;
}}

.dock-tabs {{
    height: 38px;
    background: var(--bg-panel-header);
    border-bottom: 1px solid var(--border-color);
    display: flex;
}}

.dock-tab {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.15s ease;
}}

.dock-tab:hover {{
    color: #fff;
    background: rgba(255,255,255,0.02);
}}

.dock-tab.active {{
    color: #fff;
    border-bottom-color: var(--accent-blue);
    background: var(--bg-panel);
}}

.dock-body {{
    flex: 1;
    overflow-y: auto;
    position: relative;
}}

.tab-pane {{
    display: none;
    padding: 12px;
}}
.tab-pane.active {{
    display: block;
}}

/* LAYERS PANEL */
.layers-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--border-color);
}}

.layer-list {{
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-bottom: 12px;
}}

.layer-item {{
    display: flex;
    align-items: center;
    padding: 6px 10px;
    background: #1c1c1c;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    gap: 10px;
    cursor: pointer;
    font-size: 12px;
    transition: all 0.12s ease;
}}

.layer-item:hover {{
    background: #2a2a2a;
}}

.layer-item.active {{
    background: #094771;
    border-color: #0078d4;
    color: #fff;
}}

.layer-item-icon {{
    font-size: 13px;
    color: #888;
    width: 16px;
    text-align: center;
}}
.layer-item.active .layer-item-icon {{
    color: #fff;
}}

.layer-item-name {{
    flex: 1;
    font-weight: 600;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}}

.layer-btn-icon {{
    background: transparent;
    border: none;
    color: #777;
    cursor: pointer;
    font-size: 13px;
    padding: 2px 4px;
    border-radius: 3px;
}}
.layer-btn-icon:hover {{
    color: #fff;
    background: rgba(255,255,255,0.1);
}}
.layer-btn-icon.active {{
    color: #40a9ff;
}}

.layers-footer-toolbar {{
    display: flex;
    gap: 6px;
    padding-top: 8px;
    border-top: 1px solid var(--border-color);
}}

/* PROPERTIES PANEL */
.prop-section {{
    margin-bottom: 14px;
    background: #1e1e1e;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 10px;
}}

.prop-title {{
    font-size: 11px;
    font-weight: 700;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}}

.prop-row {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}}
.prop-row:last-child {{
    margin-bottom: 0;
}}

.prop-col {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 4px;
}}

.prop-label {{
    font-size: 10px;
    color: #aaa;
    font-weight: 600;
}}

.prop-control {{
    width: 100%;
    background: var(--bg-input);
    border: 1px solid var(--border-color);
    color: #fff;
    padding: 5px 8px;
    border-radius: 4px;
    font-size: 12px;
    outline: none;
}}

.prop-control:focus {{
    border-color: var(--accent-blue);
}}

.prop-slider-wrap {{
    display: flex;
    align-items: center;
    gap: 8px;
}}

.prop-slider {{
    flex: 1;
    accent-color: var(--accent-orange);
    cursor: pointer;
}}

.color-swatches {{
    display: flex;
    gap: 6px;
    margin-top: 6px;
}}

.swatch {{
    width: 22px;
    height: 22px;
    border-radius: 4px;
    border: 1px solid #444;
    cursor: pointer;
    transition: transform 0.1s ease;
}}
.swatch:hover {{
    transform: scale(1.15);
}}

/* HISTORY PANEL */
.history-list {{
    display: flex;
    flex-direction: column;
    gap: 2px;
}}

.history-item {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 10px;
    background: #1c1c1c;
    border-radius: 3px;
    font-size: 11px;
    color: #aaa;
    cursor: pointer;
}}

.history-item:hover {{
    background: #282828;
    color: #fff;
}}

.history-item.active {{
    background: #003a6c;
    color: #fff;
    font-weight: 600;
}}

/* BOTTOM STATUS BAR */
.status-bar {{
    height: 26px;
    background: var(--bg-panel-header);
    border-top: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 12px;
    font-size: 11px;
    color: var(--text-muted);
    z-index: 100;
}}

.status-left, .status-right {{
    display: flex;
    align-items: center;
    gap: 16px;
}}

.status-item strong {{
    color: #fff;
}}

/* TOAST NOTIFICATION */
.toast {{
    position: fixed;
    bottom: 36px;
    left: 50%;
    transform: translateX(-50%);
    background: #333;
    color: #fff;
    padding: 8px 18px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    box-shadow: 0 4px 16px rgba(0,0,0,0.5);
    z-index: 10000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease, transform 0.2s ease;
}}
.toast.show {{
    opacity: 1;
    transform: translateX(-50%) translateY(-10px);
}}

</style>
</head>
<body>

<!-- TOP APP HEADER -->
<header class="app-header">
    <div class="app-title-group">
        <span class="app-logo-badge">PS</span>
        <span class="app-title">18-Day Orange Campaign Poster Studio</span>
    </div>

    <!-- DAY SELECTOR -->
    <div class="day-selector-group">
        <button class="day-nav-btn" id="prevDayBtn" title="Previous Day (Ctrl+Left)">◀ Prev</button>
        <label for="daySelect">Active Poster:</label>
        <select id="daySelect" class="day-select"></select>
        <button class="day-nav-btn" id="nextDayBtn" title="Next Day (Ctrl+Right)">Next ▶</button>
    </div>

    <!-- ACTIONS -->
    <div class="top-actions">
        <button class="btn btn-default" id="undoBtn" title="Undo (Ctrl+Z)">↶ Undo</button>
        <button class="btn btn-default" id="redoBtn" title="Redo (Ctrl+Y)">↷ Redo</button>
        <button class="btn btn-default" id="resetDayBtn" title="Reset current poster to calibrated default">↺ Reset Layout</button>
        <button class="btn btn-default" id="copyJsonBtn" title="Copy layout coordinates to clipboard">📋 Copy JSON</button>
        <button class="btn btn-orange" id="downloadPngBtn" title="Render 300 DPI High-Resolution PNG">⬇ Download 300 DPI PNG</button>
    </div>
</header>

<!-- OPTIONS BAR -->
<div class="options-bar">
    <div class="options-group">
        <span class="tool-badge" id="currentToolBadge">Tool: Move (V)</span>
    </div>

    <div class="options-group" id="optTransformGroup">
        <span class="opt-label">Layer:</span>
        <span id="optLayerName" style="color: #fff; font-weight: bold; max-width: 130px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">None</span>
        <span class="opt-label">X:</span>
        <input type="number" id="optX" class="opt-input">
        <span class="opt-label">Y:</span>
        <input type="number" id="optY" class="opt-input">
        <span class="opt-label">W:</span>
        <input type="number" id="optW" class="opt-input">
        <span class="opt-label">H:</span>
        <input type="number" id="optH" class="opt-input">
    </div>

    <div class="options-group">
        <span class="opt-label">Align:</span>
        <button class="btn btn-default" id="btnAlignLeft" title="Align Left">⇤</button>
        <button class="btn btn-default" id="btnAlignCenter" title="Align Center (X=1240)">⇥⇤</button>
        <button class="btn btn-default" id="btnAlignRight" title="Align Right">⇥</button>
    </div>

    <div class="options-group">
        <span class="opt-label">Order:</span>
        <button class="btn btn-default" id="btnBringForward" title="Bring Forward (Ctrl+])">▲</button>
        <button class="btn btn-default" id="btnSendBackward" title="Send Backward (Ctrl+[)">▼</button>
    </div>

    <!-- RADAR HUD -->
    <div class="clearance-pill" id="radarHud">
        <span class="clearance-dot" id="radarDot"></span>
        <span id="radarText">Clearance Safe (+185px)</span>
    </div>
</div>

<!-- MAIN WORKBENCH -->
<div class="workbench">
    <!-- LEFT TOOLBAR -->
    <aside class="toolbar">
        <button class="tool-btn active" id="toolMove" title="Move Tool (V) — Select, drag, resize with handles">✦</button>
        <button class="tool-btn" id="toolText" title="Type Tool (T) — Double click canvas or add text">T</button>
        <button class="tool-btn" id="toolHand" title="Hand Tool (H) — Pan canvas (or hold Spacebar)">✋</button>
        <button class="tool-btn" id="toolZoom" title="Zoom Tool (Z) — Click to zoom in / Alt+Click out">🔍</button>
        <div class="tool-divider"></div>
        <button class="tool-btn" id="btnAddTextLayer" title="Add New Text Layer">+T</button>
        <button class="tool-btn" id="btnAddIconLayer" title="Add New Icon Layer">+🖼</button>
        <div class="tool-divider"></div>
        <button class="tool-btn" id="toolToggleHazard" title="Toggle Jeepney & Road Hazard Guide (G)">⚠️</button>
        <button class="tool-btn" id="toolToggleSnap" title="Toggle Smart Center Snapping (S)">🧲</button>
        <button class="tool-btn" id="btnFitScreen" title="Fit to Screen (Ctrl+0)">⊡</button>
    </aside>

    <!-- CENTER VIEWPORT -->
    <main class="viewport-container" id="viewportContainer">
        <!-- RULERS -->
        <div class="ruler-corner"></div>
        <canvas class="ruler-top" id="rulerTop"></canvas>
        <canvas class="ruler-left" id="rulerLeft"></canvas>

        <div class="canvas-viewport" id="canvasViewport">
            <div class="canvas-stage" id="canvasStage">
                <div class="poster-canvas" id="posterCanvas">
                    <!-- BACKGROUND TEMPLATE -->
                    <img src="FABMAT/fabmat_template.png" class="template-bg" alt="Template Background" id="templateBg">

                    <!-- HAZARD OVERLAYS -->
                    <div class="hazard-overlay jeepney" id="jeepneyHazard">
                        <span class="hazard-badge">⚠️ JEEPNEY HAZARD ZONE (Y ≥ 2950)</span>
                    </div>
                    <div class="hazard-overlay road" id="roadHazard">
                        <span class="hazard-badge">⛔ ROAD ZONE (Y ≥ 3388)</span>
                    </div>

                    <!-- SMART GUIDES -->
                    <div class="guide-line vertical" id="guideCenterX" style="left: 1240px;"></div>
                    <div class="guide-line vertical" id="guideLeftMargin" style="left: 190px;"></div>
                    <div class="guide-line vertical" id="guideRightMargin" style="left: 2290px;"></div>
                    <div class="guide-line horizontal" id="guideSafeTop" style="top: 1310px;"></div>

                    <!-- LAYERS CONTAINER -->
                    <div class="layers-container" id="layersContainer"></div>

                    <!-- TRANSFORM BOX -->
                    <div class="transform-box" id="transformBox">
                        <div class="transform-border" id="transformBorder"></div>
                        <div class="transform-handle nw" data-handle="nw"></div>
                        <div class="transform-handle n"  data-handle="n"></div>
                        <div class="transform-handle ne" data-handle="ne"></div>
                        <div class="transform-handle e"  data-handle="e"></div>
                        <div class="transform-handle se" data-handle="se"></div>
                        <div class="transform-handle s"  data-handle="s"></div>
                        <div class="transform-handle sw" data-handle="sw"></div>
                        <div class="transform-handle w"  data-handle="w"></div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- RIGHT DOCK -->
    <aside class="dock">
        <!-- TABS -->
        <div class="dock-tabs">
            <div class="dock-tab active" data-tab="layersTab">Layers</div>
            <div class="dock-tab" data-tab="propsTab">Properties</div>
            <div class="dock-tab" data-tab="historyTab">History</div>
        </div>

        <div class="dock-body">
            <!-- TAB 1: LAYERS -->
            <div class="tab-pane active" id="layersTab">
                <div class="layers-header">
                    <span style="font-weight: 700; color: #fff;">Layers Stack</span>
                    <span id="layersCount" style="color: #888;">0 layers</span>
                </div>
                <div class="layer-list" id="layersList"></div>
                <div class="layers-footer-toolbar">
                    <button class="btn btn-default" style="flex:1;" id="dockAddTextBtn">+ Text</button>
                    <button class="btn btn-default" style="flex:1;" id="dockDuplicateBtn">Duplicate</button>
                    <button class="btn btn-default" style="flex:1; color: var(--danger);" id="dockDeleteBtn">Delete</button>
                </div>
            </div>

            <!-- TAB 2: PROPERTIES -->
            <div class="tab-pane" id="propsTab">
                <!-- TRANSFORM SECTION -->
                <div class="prop-section">
                    <div class="prop-title">Transform & Position</div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">X (Left px)</span>
                            <input type="number" id="propX" class="prop-control">
                        </div>
                        <div class="prop-col">
                            <span class="prop-label">Y (Top px)</span>
                            <input type="number" id="propY" class="prop-control">
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Width (px)</span>
                            <input type="number" id="propW" class="prop-control">
                        </div>
                        <div class="prop-col">
                            <span class="prop-label">Height (px)</span>
                            <input type="number" id="propH" class="prop-control">
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Opacity</span>
                            <div class="prop-slider-wrap">
                                <input type="range" id="propOpacity" class="prop-slider" min="0" max="1" step="0.05" value="1">
                                <span id="propOpacityVal" style="width: 35px; text-align: right; color:#fff;">100%</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- IMAGE SPECIFIC SECTION -->
                <div class="prop-section" id="sectionImageProps" style="display: none;">
                    <div class="prop-title">Hero Icon Asset</div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Select Icon</span>
                            <select id="propIconSelect" class="prop-control"></select>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Or Upload Custom Icon</span>
                            <input type="file" id="propIconUpload" accept="image/*" class="prop-control">
                        </div>
                    </div>
                </div>

                <!-- TEXT SPECIFIC SECTION -->
                <div class="prop-section" id="sectionTextProps">
                    <div class="prop-title">Character & Typography</div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Text Content</span>
                            <textarea id="propTextContent" class="prop-control" rows="3" style="resize: vertical;"></textarea>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Font Family</span>
                            <select id="propFontFamily" class="prop-control">
                                <option value="Gotham Ultra">Gotham Ultra (900 Heavy)</option>
                                <option value="Gotham Black">Gotham Black (900)</option>
                                <option value="Gotham Bold">Gotham Bold (700)</option>
                                <option value="Gotham Medium">Gotham Medium (500)</option>
                                <option value="Gotham Medium Italic">Gotham Medium Italic</option>
                                <option value="Gotham Book">Gotham Book (400)</option>
                            </select>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Font Size (px)</span>
                            <div class="prop-slider-wrap">
                                <input type="range" id="propFontSizeSlider" class="prop-slider" min="20" max="220" step="2" value="70">
                                <input type="number" id="propFontSizeNum" class="prop-control" style="width: 60px;" value="70">
                            </div>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Line Height</span>
                            <input type="number" id="propLineHeight" class="prop-control" step="0.05" min="0.8" max="2.5" value="1.15">
                        </div>
                        <div class="prop-col">
                            <span class="prop-label">Alignment</span>
                            <select id="propTextAlign" class="prop-control">
                                <option value="left">Left Align</option>
                                <option value="center">Center Align</option>
                                <option value="right">Right Align</option>
                            </select>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Fill Color</span>
                            <input type="color" id="propTextColor" class="prop-control" value="#ffffff" style="height: 32px; padding: 2px;">
                            <div class="color-swatches">
                                <div class="swatch" style="background:#ffffff;" data-color="#ffffff"></div>
                                <div class="swatch" style="background:#FFE650;" data-color="#FFE650"></div>
                                <div class="swatch" style="background:#FF6D00;" data-color="#FF6D00"></div>
                                <div class="swatch" style="background:#240546;" data-color="#240546"></div>
                                <div class="swatch" style="background:#000000;" data-color="#000000"></div>
                            </div>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Outline Stroke Width (px)</span>
                            <div class="prop-slider-wrap">
                                <input type="range" id="propStrokeWidthSlider" class="prop-slider" min="0" max="40" step="1" value="16">
                                <input type="number" id="propStrokeWidthNum" class="prop-control" style="width: 60px;" value="16">
                            </div>
                        </div>
                    </div>
                    <div class="prop-row">
                        <div class="prop-col">
                            <span class="prop-label">Stroke Outline Color</span>
                            <input type="color" id="propStrokeColor" class="prop-control" value="#FF6D00" style="height: 32px; padding: 2px;">
                            <div class="color-swatches">
                                <div class="swatch" style="background:#FF6D00;" data-stroke="#FF6D00"></div>
                                <div class="swatch" style="background:#FA5400;" data-stroke="#FA5400"></div>
                                <div class="swatch" style="background:#240546;" data-stroke="#240546"></div>
                                <div class="swatch" style="background:#000000;" data-stroke="#000000"></div>
                                <div class="swatch" style="background:transparent; border: 1px dashed #888;" data-stroke="transparent" title="No stroke"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: HISTORY -->
            <div class="tab-pane" id="historyTab">
                <div class="prop-title" style="margin-bottom: 8px;">Photoshop State History</div>
                <div class="history-list" id="historyList"></div>
            </div>
        </div>
    </aside>
</div>

<!-- BOTTOM STATUS BAR -->
<footer class="status-bar">
    <div class="status-left">
        <span class="status-item">Canvas: <strong>2480 × 3508 px (300 DPI)</strong></span>
        <span class="status-item">Zoom: <strong id="statusZoom">28%</strong></span>
        <span class="status-item" id="statusSelected">Selected: <strong>None</strong></span>
    </div>
    <div class="status-right">
        <span class="status-item">Jeepney Safe Limit: <strong>Y &lt; 2950 px</strong></span>
        <span class="status-item">Road Safe Limit: <strong>Y &lt; 3388 px</strong></span>
    </div>
</footer>

<!-- TOAST -->
<div class="toast" id="toastMsg">Action completed</div>

<!-- HIDDEN CANVAS FOR HIGH RES PNG RENDERING -->
<canvas id="exportCanvas" width="2480" height="3508" style="display:none;"></canvas>

<script>
// --- EMBEDDED DATA ---
const SCHEDULE_DATA = {schedule_json_str};
const DEFAULT_LAYERS_BY_DAY = {layers_json_str};
const AVAILABLE_ICONS = {icons_json_str};

// --- APP STATE ---
let currentDayId = "00";
let layers = [];
let selectedLayerId = null;
let currentTool = "move"; // move, text, hand, zoom
let snapToGuides = true;
let showHazardOverlay = true;

// Viewport Transform
let zoom = 0.28;
let panX = 0;
let panY = 0;
let isPanning = false;
let startPanX = 0;
let startPanY = 0;

// Layer Dragging State
let isDraggingLayer = false;
let dragStartX = 0;
let dragStartY = 0;
let layerStartPositions = {{}};

// Transform Handles State
let activeHandle = null;
let handleStartX = 0;
let handleStartY = 0;
let handleInitialRect = {{}};

// History Stack
let history = [];
let historyIndex = -1;
const MAX_HISTORY = 40;

// DOM Elements
const canvasViewport = document.getElementById('canvasViewport');
const canvasStage = document.getElementById('canvasStage');
const posterCanvas = document.getElementById('posterCanvas');
const layersContainer = document.getElementById('layersContainer');
const transformBox = document.getElementById('transformBox');
const transformBorder = document.getElementById('transformBorder');
const daySelect = document.getElementById('daySelect');
const layersList = document.getElementById('layersList');
const historyList = document.getElementById('historyList');
const radarHud = document.getElementById('radarHud');
const radarDot = document.getElementById('radarDot');
const radarText = document.getElementById('radarText');
const toastMsg = document.getElementById('toastMsg');
const statusZoom = document.getElementById('statusZoom');
const statusSelected = document.getElementById('statusSelected');
const jeepneyHazard = document.getElementById('jeepneyHazard');
const roadHazard = document.getElementById('roadHazard');

// Rulers
const rulerTop = document.getElementById('rulerTop');
const rulerLeft = document.getElementById('rulerLeft');

// Top Options Inputs
const optLayerName = document.getElementById('optLayerName');
const optX = document.getElementById('optX');
const optY = document.getElementById('optY');
const optW = document.getElementById('optW');
const optH = document.getElementById('optH');

// Property Panel Inputs
const propX = document.getElementById('propX');
const propY = document.getElementById('propY');
const propW = document.getElementById('propW');
const propH = document.getElementById('propH');
const propOpacity = document.getElementById('propOpacity');
const propOpacityVal = document.getElementById('propOpacityVal');

const sectionImageProps = document.getElementById('sectionImageProps');
const propIconSelect = document.getElementById('propIconSelect');
const propIconUpload = document.getElementById('propIconUpload');

const sectionTextProps = document.getElementById('sectionTextProps');
const propTextContent = document.getElementById('propTextContent');
const propFontFamily = document.getElementById('propFontFamily');
const propFontSizeSlider = document.getElementById('propFontSizeSlider');
const propFontSizeNum = document.getElementById('propFontSizeNum');
const propLineHeight = document.getElementById('propLineHeight');
const propTextAlign = document.getElementById('propTextAlign');
const propTextColor = document.getElementById('propTextColor');
const propStrokeWidthSlider = document.getElementById('propStrokeWidthSlider');
const propStrokeWidthNum = document.getElementById('propStrokeWidthNum');
const propStrokeColor = document.getElementById('propStrokeColor');

// --- HELPER FUNCTIONS ---
function showToast(msg) {{
    toastMsg.textContent = msg;
    toastMsg.classList.add('show');
    setTimeout(() => toastMsg.classList.remove('show'), 2500);
}}

function deepClone(obj) {{
    return JSON.parse(JSON.stringify(obj));
}}

function getSelectedLayer() {{
    return layers.find(l => l.id === selectedLayerId) || null;
}}

// --- HISTORY SYSTEM ---
function pushHistory(actionName) {{
    if (historyIndex < history.length - 1) {{
        history = history.slice(0, historyIndex + 1);
    }}
    history.push({{
        name: actionName,
        layers: deepClone(layers),
        selectedLayerId: selectedLayerId
    }});
    if (history.length > MAX_HISTORY) {{
        history.shift();
    }} else {{
        historyIndex++;
    }}
    updateHistoryUI();
}}

function undo() {{
    if (historyIndex > 0) {{
        historyIndex--;
        restoreHistoryState(history[historyIndex]);
        showToast(`Undo: ${{history[historyIndex].name}}`);
    }}
}}

function redo() {{
    if (historyIndex < history.length - 1) {{
        historyIndex++;
        restoreHistoryState(history[historyIndex]);
        showToast(`Redo: ${{history[historyIndex].name}}`);
    }}
}}

function restoreHistoryState(state) {{
    layers = deepClone(state.layers);
    selectedLayerId = state.selectedLayerId;
    renderLayers();
    updateLayersPanel();
    updatePropertiesPanel();
    updateTransformBox();
    updateRadar();
    updateHistoryUI();
}}

function updateHistoryUI() {{
    historyList.innerHTML = '';
    history.forEach((step, idx) => {{
        const item = document.createElement('div');
        item.className = 'history-item' + (idx === historyIndex ? ' active' : '');
        item.innerHTML = `<span>◷</span> <span>${{step.name}}</span>`;
        item.addEventListener('click', () => {{
            historyIndex = idx;
            restoreHistoryState(history[idx]);
        }});
        historyList.appendChild(item);
    }});
    historyList.scrollTop = historyList.scrollHeight;
}}

// --- INITIALIZATION ---
function initApp() {{
    // Populate Day Selector
    daySelect.innerHTML = '';
    SCHEDULE_DATA.forEach(d => {{
        const opt = document.createElement('option');
        opt.value = d.id;
        opt.textContent = `${{d.badge}} — ${{d.title || (d.activities && d.activities[0] ? d.activities[0].description : d.main_activity || 'Activity')}}`;
        daySelect.appendChild(opt);
    }});

    // Populate Icon Selector
    propIconSelect.innerHTML = '';
    AVAILABLE_ICONS.forEach(ic => {{
        const opt = document.createElement('option');
        opt.value = `icons/${{ic}}`;
        opt.textContent = ic;
        propIconSelect.appendChild(opt);
    }});

    // Load initial day
    loadDay("00");

    // Center canvas in viewport
    fitToScreen();
    drawRulers();
}}

function loadDay(dayId) {{
    currentDayId = dayId;
    daySelect.value = dayId;

    // Check localStorage first, otherwise fallback to defaults
    const saved = localStorage.getItem(`poster_layers_${{dayId}}`);
    if (saved) {{
        try {{
            layers = JSON.parse(saved);
        }} catch (e) {{
            layers = deepClone(DEFAULT_LAYERS_BY_DAY[dayId] || []);
        }}
    }} else {{
        layers = deepClone(DEFAULT_LAYERS_BY_DAY[dayId] || []);
    }}

    selectedLayerId = null;
    history = [];
    historyIndex = -1;
    pushHistory(`Load ${{daySelect.options[daySelect.selectedIndex].text.split('—')[0].trim()}}`);

    renderLayers();
    updateLayersPanel();
    updatePropertiesPanel();
    updateTransformBox();
    updateRadar();
}}

// --- VIEWPORT TRANSFORM (ZOOM & PAN) ---
function updateTransform() {{
    canvasStage.style.transform = `scale(${{zoom}}) translate(${{panX}}px, ${{panY}}px)`;
    statusZoom.textContent = `${{Math.round(zoom * 100)}}%`;
    drawRulers();
}}

function fitToScreen() {{
    const rect = canvasViewport.getBoundingClientRect();
    const margin = 40;
    const availW = rect.width - margin * 2;
    const availH = rect.height - margin * 2;

    const scaleW = availW / 2480;
    const scaleH = availH / 3508;
    zoom = Math.min(scaleW, scaleH);

    panX = Math.round((availW - 2480 * zoom) / (2 * zoom)) + Math.round(margin / zoom);
    panY = Math.round((availH - 3508 * zoom) / (2 * zoom)) + Math.round(margin / zoom);

    updateTransform();
}}

// Zoom with mouse wheel centered on mouse
canvasViewport.addEventListener('wheel', (e) => {{
    e.preventDefault();
    const zoomFactor = e.deltaY < 0 ? 1.12 : 0.89;
    const newZoom = Math.min(Math.max(zoom * zoomFactor, 0.08), 2.5);

    const rect = canvasViewport.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    panX -= (mouseX / newZoom - mouseX / zoom);
    panY -= (mouseY / newZoom - mouseY / zoom);
    zoom = newZoom;

    updateTransform();
}}, {{ passive: false }});

// --- RULERS RENDERING ---
function drawRulers() {{
    const w = canvasViewport.clientWidth;
    const h = canvasViewport.clientHeight;

    rulerTop.width = w;
    rulerTop.height = 20;
    rulerLeft.width = 20;
    rulerLeft.height = h;

    const ctxT = rulerTop.getContext('2d');
    const ctxL = rulerLeft.getContext('2d');

    ctxT.fillStyle = '#1c1c1c';
    ctxT.fillRect(0, 0, w, 20);
    ctxT.strokeStyle = '#555';
    ctxT.fillStyle = '#888';
    ctxT.font = '9px sans-serif';

    ctxL.fillStyle = '#1c1c1c';
    ctxL.fillRect(0, 0, 20, h);
    ctxL.strokeStyle = '#555';
    ctxL.fillStyle = '#888';
    ctxL.font = '9px sans-serif';

    // Top Ruler
    const startX = panX * zoom;
    const step = 100 * zoom;
    for (let x = 0; x <= 2480; x += 100) {{
        const screenX = startX + x * zoom;
        if (screenX >= 0 && screenX <= w) {{
            const isMajor = x % 500 === 0;
            ctxT.beginPath();
            ctxT.moveTo(screenX, isMajor ? 0 : 12);
            ctxT.lineTo(screenX, 20);
            ctxT.stroke();
            if (isMajor) {{
                ctxT.fillText(x.toString(), screenX + 3, 11);
            }}
        }}
    }}

    // Left Ruler
    const startY = panY * zoom;
    for (let y = 0; y <= 3508; y += 100) {{
        const screenY = startY + y * zoom;
        if (screenY >= 0 && screenY <= h) {{
            const isMajor = y % 500 === 0;
            ctxL.beginPath();
            ctxL.moveTo(isMajor ? 0 : 12, screenY);
            ctxL.lineTo(20, screenY);
            ctxL.stroke();
            if (isMajor) {{
                ctxL.save();
                ctxL.translate(11, screenY + 3);
                ctxL.rotate(-Math.PI / 2);
                ctxL.fillText(y.toString(), 0, 0);
                ctxL.restore();
            }}
        }}
    }}
}}

// --- RENDER LAYERS ON CANVAS ---
function renderLayers() {{
    layersContainer.innerHTML = '';

    layers.forEach(layer => {{
        if (layer.type === 'background') return; // Handled by templateBg

        const el = document.createElement('div');
        el.className = 'layer-node' + (layer.id === selectedLayerId ? ' selected' : '') + (layer.locked ? ' locked' : '');
        el.id = `node_${{layer.id}}`;
        el.dataset.layerId = layer.id;

        el.style.left = `${{layer.x}}px`;
        el.style.top = `${{layer.y}}px`;
        if (layer.width && layer.width !== 'auto') el.style.width = `${{layer.width}}px`;
        if (layer.height && layer.height !== 'auto') el.style.height = `${{layer.height}}px`;
        el.style.display = layer.visible ? 'block' : 'none';
        el.style.opacity = layer.opacity !== undefined ? layer.opacity : 1.0;

        if (layer.type === 'image') {{
            const img = document.createElement('img');
            img.src = layer.src;
            img.className = 'layer-image';
            img.alt = layer.name;
            el.appendChild(img);
        }} else if (layer.type === 'text') {{
            const textEl = document.createElement('div');
            textEl.className = 'layer-text';
            textEl.textContent = layer.text;
            textEl.style.fontFamily = layer.fontFamily || 'Gotham Bold';
            textEl.style.fontSize = `${{layer.fontSize || 60}}px`;
            textEl.style.lineHeight = layer.lineHeight || 1.15;
            textEl.style.textAlign = layer.textAlign || 'left';
            textEl.style.color = layer.color || '#FFFFFF';
            textEl.style.textTransform = layer.textTransform || 'none';

            if (layer.strokeWidth && layer.strokeWidth > 0 && layer.strokeColor && layer.strokeColor !== 'transparent') {{
                textEl.style.webkitTextStroke = `${{layer.strokeWidth}}px ${{layer.strokeColor}}`;
            }} else {{
                textEl.style.webkitTextStroke = '0px transparent';
            }}

            // Double click to edit inline!
            el.addEventListener('dblclick', (e) => {{
                e.stopPropagation();
                enterInlineEdit(layer, textEl);
            }});

            el.appendChild(textEl);
        }}

        // Layer Selection & Dragging
        el.addEventListener('mousedown', (e) => {{
            if (e.target.isContentEditable) return;
            if (currentTool === 'move') {{
                e.stopPropagation();
                selectLayer(layer.id);
                if (!layer.locked) {{
                    startLayerDrag(e);
                }}
            }}
        }});

        layersContainer.appendChild(el);
    }});
}}

// --- INLINE TEXT EDITING ---
function enterInlineEdit(layer, textDom) {{
    textDom.contentEditable = 'true';
    textDom.focus();
    transformBox.classList.remove('active');

    function commit() {{
        textDom.contentEditable = 'false';
        const newText = textDom.textContent;
        if (newText !== layer.text) {{
            layer.text = newText;
            pushHistory(`Edit Text: ${{layer.name}}`);
            updatePropertiesPanel();
            updateTransformBox();
            updateRadar();
        }}
    }}

    textDom.addEventListener('blur', commit, {{ once: true }});
    textDom.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') {{
            textDom.textContent = layer.text;
            textDom.blur();
        }}
    }});
}}

// --- SELECTION & TRANSFORM BOX ---
function selectLayer(id) {{
    selectedLayerId = id;

    // Update canvas classes
    document.querySelectorAll('.layer-node').forEach(n => {{
        n.classList.toggle('selected', n.dataset.layerId === id);
    }});

    const layer = getSelectedLayer();
    if (layer) {{
        statusSelected.innerHTML = `Selected: <strong>${{layer.name}}</strong>`;
    }} else {{
        statusSelected.innerHTML = `Selected: <strong>None</strong>`;
    }}

    updateTransformBox();
    updateLayersPanel();
    updatePropertiesPanel();
    updateOptionsBar();
}}

function deselectLayer() {{
    selectedLayerId = null;
    document.querySelectorAll('.layer-node').forEach(n => n.classList.remove('selected'));
    transformBox.classList.remove('active');
    statusSelected.innerHTML = `Selected: <strong>None</strong>`;
    updateLayersPanel();
    updatePropertiesPanel();
    updateOptionsBar();
}}

function updateTransformBox() {{
    const layer = getSelectedLayer();
    if (!layer || !layer.visible || layer.locked) {{
        transformBox.classList.remove('active');
        return;
    }}

    const node = document.getElementById(`node_${{layer.id}}`);
    if (!node) return;

    const w = node.offsetWidth;
    const h = node.offsetHeight;

    transformBox.classList.add('active');
    transformBox.style.left = `${{layer.x}}px`;
    transformBox.style.top = `${{layer.y}}px`;
    transformBox.style.width = `${{w}}px`;
    transformBox.style.height = `${{h}}px`;

    transformBorder.style.width = `${{w}}px`;
    transformBorder.style.height = `${{h}}px`;

    // Position handles
    const hMap = {{
        nw: [0, 0],
        n:  [w/2, 0],
        ne: [w, 0],
        e:  [w, h/2],
        se: [w, h],
        s:  [w/2, h],
        sw: [0, h],
        w:  [0, h/2]
    }};

    Object.entries(hMap).forEach(([hKey, [hx, hy]]) => {{
        const el = transformBox.querySelector(`.transform-handle.${{hKey}}`);
        if (el) {{
            el.style.left = `${{hx}}px`;
            el.style.top = `${{hy}}px`;
        }}
    }});
}}

// --- DRAG TO MOVE LAYER ---
function startLayerDrag(e) {{
    isDraggingLayer = true;
    dragStartX = e.clientX;
    dragStartY = e.clientY;

    const layer = getSelectedLayer();
    layerStartPositions = {{
        x: layer.x,
        y: layer.y
    }};

    window.addEventListener('mousemove', onLayerDragMove);
    window.addEventListener('mouseup', onLayerDragEnd);
}}

function onLayerDragMove(e) {{
    if (!isDraggingLayer) return;

    const dx = (e.clientX - dragStartX) / zoom;
    const dy = (e.clientY - dragStartY) / zoom;

    const layer = getSelectedLayer();
    let targetX = Math.round(layerStartPositions.x + dx);
    let targetY = Math.round(layerStartPositions.y + dy);

    // Smart Center Snap (1240px)
    if (snapToGuides) {{
        const node = document.getElementById(`node_${{layer.id}}`);
        const w = node ? node.offsetWidth : (layer.width || 0);
        const centerX = targetX + w / 2;
        if (Math.abs(centerX - 1240) < 15) {{
            targetX = 1240 - w / 2;
            document.getElementById('guideCenterX').style.display = 'block';
        }} else {{
            document.getElementById('guideCenterX').style.display = 'none';
        }}

        // Margin snap (190px)
        if (Math.abs(targetX - 190) < 15) {{
            targetX = 190;
            document.getElementById('guideLeftMargin').style.display = 'block';
        }} else {{
            document.getElementById('guideLeftMargin').style.display = 'none';
        }}
    }}

    layer.x = targetX;
    layer.y = targetY;

    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        node.style.left = `${{layer.x}}px`;
        node.style.top = `${{layer.y}}px`;
    }}

    updateTransformBox();
    updateOptionsBar();
    updatePropertiesPanel();
    updateRadar();
}}

function onLayerDragEnd() {{
    if (!isDraggingLayer) return;
    isDraggingLayer = false;
    document.querySelectorAll('.guide-line').forEach(g => g.style.display = 'none');
    window.removeEventListener('mousemove', onLayerDragMove);
    window.removeEventListener('mouseup', onLayerDragEnd);

    const layer = getSelectedLayer();
    pushHistory(`Move ${{layer.name}}`);
    saveCurrentDay();
}}

// --- TRANSFORM HANDLES (RESIZING) ---
document.querySelectorAll('.transform-handle').forEach(handle => {{
    handle.addEventListener('mousedown', (e) => {{
        e.stopPropagation();
        activeHandle = handle.dataset.handle;
        handleStartX = e.clientX;
        handleStartY = e.clientY;

        const layer = getSelectedLayer();
        const node = document.getElementById(`node_${{layer.id}}`);
        handleInitialRect = {{
            x: layer.x,
            y: layer.y,
            w: node.offsetWidth,
            h: node.offsetHeight,
            fontSize: layer.fontSize || 60
        }};

        window.addEventListener('mousemove', onHandleMove);
        window.addEventListener('mouseup', onHandleEnd);
    }});
}});

function onHandleMove(e) {{
    if (!activeHandle) return;

    const dx = (e.clientX - handleStartX) / zoom;
    const dy = (e.clientY - handleStartY) / zoom;

    const layer = getSelectedLayer();
    const init = handleInitialRect;

    if (activeHandle === 'se') {{
        layer.width = Math.max(init.w + dx, 50);
        if (layer.type === 'image') {{
            layer.height = layer.width; // 1:1 aspect ratio
        }}
    }} else if (activeHandle === 'e') {{
        layer.width = Math.max(init.w + dx, 50);
    }} else if (activeHandle === 's') {{
        if (layer.type === 'image') {{
            layer.height = Math.max(init.h + dy, 50);
            layer.width = layer.height;
        }}
    }} else if (activeHandle === 'nw') {{
        layer.x = init.x + dx;
        layer.y = init.y + dy;
        layer.width = Math.max(init.w - dx, 50);
        if (layer.type === 'image') {{
            layer.height = layer.width;
        }}
    }}

    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        node.style.left = `${{layer.x}}px`;
        node.style.top = `${{layer.y}}px`;
        node.style.width = `${{layer.width}}px`;
        if (layer.height) node.style.height = `${{layer.height}}px`;
    }}

    updateTransformBox();
    updateOptionsBar();
    updatePropertiesPanel();
    updateRadar();
}}

function onHandleEnd() {{
    if (!activeHandle) return;
    activeHandle = null;
    window.removeEventListener('mousemove', onHandleMove);
    window.removeEventListener('mouseup', onHandleEnd);

    const layer = getSelectedLayer();
    pushHistory(`Resize ${{layer.name}}`);
    saveCurrentDay();
}}

// --- PANNING WITH HAND TOOL OR SPACEBAR ---
canvasViewport.addEventListener('mousedown', (e) => {{
    if (e.target === canvasViewport || e.target === canvasStage || e.target === posterCanvas || currentTool === 'hand' || e.spaceKey) {{
        isPanning = true;
        startPanX = e.clientX - panX * zoom;
        startPanY = e.clientY - panY * zoom;
        canvasViewport.style.cursor = 'grabbing';
    }} else if (e.target.classList.contains('canvas-viewport') || e.target.classList.contains('poster-canvas')) {{
        deselectLayer();
    }}
}});

window.addEventListener('mousemove', (e) => {{
    if (!isPanning) return;
    panX = (e.clientX - startPanX) / zoom;
    panY = (e.clientY - startPanY) / zoom;
    updateTransform();
}});

window.addEventListener('mouseup', () => {{
    if (isPanning) {{
        isPanning = false;
        canvasViewport.style.cursor = currentTool === 'hand' ? 'grab' : 'default';
    }}
}});

// --- KEYBOARD SHORTCUTS (PHOTOSHOP PARADIGM) ---
window.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable) {{
        return;
    }}

    // V: Move Tool
    if (e.key === 'v' || e.key === 'V') {{
        setTool('move');
    }}
    // T: Text Tool
    else if (e.key === 't' || e.key === 'T') {{
        setTool('text');
    }}
    // H: Hand Tool
    else if (e.key === 'h' || e.key === 'H') {{
        setTool('hand');
    }}
    // Z: Zoom Tool
    else if (e.key === 'z' && !e.ctrlKey && !e.metaKey) {{
        setTool('zoom');
    }}
    // G: Toggle Hazard Overlay
    else if (e.key === 'g' || e.key === 'G') {{
        toggleHazard();
    }}
    // S: Toggle Snap
    else if (e.key === 's' && !e.ctrlKey) {{
        toggleSnap();
    }}
    // Ctrl+Z: Undo
    else if ((e.ctrlKey || e.metaKey) && (e.key === 'z' || e.key === 'Z') && !e.shiftKey) {{
        e.preventDefault();
        undo();
    }}
    // Ctrl+Y or Ctrl+Shift+Z: Redo
    else if (((e.ctrlKey || e.metaKey) && (e.key === 'y' || e.key === 'Y')) || ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'z' || e.key === 'Z'))) {{
        e.preventDefault();
        redo();
    }}
    // Ctrl+J: Duplicate Layer
    else if ((e.ctrlKey || e.metaKey) && (e.key === 'j' || e.key === 'J')) {{
        e.preventDefault();
        duplicateSelectedLayer();
    }}
    // Delete / Backspace: Delete Layer
    else if (e.key === 'Delete' || e.key === 'Backspace') {{
        e.preventDefault();
        deleteSelectedLayer();
    }}
    // Ctrl+0: Fit to Screen
    else if ((e.ctrlKey || e.metaKey) && e.key === '0') {{
        e.preventDefault();
        fitToScreen();
    }}
    // Ctrl+1: 100% Zoom
    else if ((e.ctrlKey || e.metaKey) && e.key === '1') {{
        e.preventDefault();
        zoom = 1.0;
        updateTransform();
    }}
    // Arrow Keys: Nudge 1px (or 10px with Shift)
    else if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {{
        const layer = getSelectedLayer();
        if (layer && !layer.locked) {{
            e.preventDefault();
            const step = e.shiftKey ? 10 : 1;
            if (e.key === 'ArrowUp') layer.y -= step;
            if (e.key === 'ArrowDown') layer.y += step;
            if (e.key === 'ArrowLeft') layer.x -= step;
            if (e.key === 'ArrowRight') layer.x += step;

            const node = document.getElementById(`node_${{layer.id}}`);
            if (node) {{
                node.style.left = `${{layer.x}}px`;
                node.style.top = `${{layer.y}}px`;
            }}
            updateTransformBox();
            updateOptionsBar();
            updatePropertiesPanel();
            updateRadar();
            pushHistory(`Nudge ${{layer.name}}`);
            saveCurrentDay();
        }}
    }}
}});

// --- TOOL SWITCHING ---
function setTool(tool) {{
    currentTool = tool;
    document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('currentToolBadge').textContent = `Tool: ${{tool.toUpperCase()}} (${{tool[0].toUpperCase()}})`;

    if (tool === 'move') {{
        document.getElementById('toolMove').classList.add('active');
        canvasViewport.style.cursor = 'default';
    }} else if (tool === 'text') {{
        document.getElementById('toolText').classList.add('active');
        canvasViewport.style.cursor = 'text';
    }} else if (tool === 'hand') {{
        document.getElementById('toolHand').classList.add('active');
        canvasViewport.style.cursor = 'grab';
    }} else if (tool === 'zoom') {{
        document.getElementById('toolZoom').classList.add('active');
        canvasViewport.style.cursor = 'zoom-in';
    }}
}}

document.getElementById('toolMove').addEventListener('click', () => setTool('move'));
document.getElementById('toolText').addEventListener('click', () => setTool('text'));
document.getElementById('toolHand').addEventListener('click', () => setTool('hand'));
document.getElementById('toolZoom').addEventListener('click', () => setTool('zoom'));

function toggleHazard() {{
    showHazardOverlay = !showHazardOverlay;
    jeepneyHazard.style.display = showHazardOverlay ? 'block' : 'none';
    roadHazard.style.display = showHazardOverlay ? 'block' : 'none';
    showToast(`Hazard Guides: ${{showHazardOverlay ? 'ON' : 'OFF'}}`);
}}
document.getElementById('toolToggleHazard').addEventListener('click', toggleHazard);

function toggleSnap() {{
    snapToGuides = !snapToGuides;
    document.getElementById('toolToggleSnap').classList.toggle('active', snapToGuides);
    showToast(`Center Snapping: ${{snapToGuides ? 'ON' : 'OFF'}}`);
}}
document.getElementById('toolToggleSnap').addEventListener('click', toggleSnap);

document.getElementById('btnFitScreen').addEventListener('click', fitToScreen);

// --- CLEARANCE RADAR CALCULATION ---
function updateRadar() {{
    let maxBottomY = 0;
    let lowestLayer = null;

    layers.forEach(layer => {{
        if (!layer.visible || layer.type === 'background') return;
        const node = document.getElementById(`node_${{layer.id}}`);
        const h = node ? node.offsetHeight : (layer.height || 0);
        const bottomY = layer.y + h;
        if (bottomY > maxBottomY) {{
            maxBottomY = bottomY;
            lowestLayer = layer;
        }}
    }});

    const jeepBuffer = 2950 - maxBottomY;
    const roadBuffer = 3388 - maxBottomY;

    if (maxBottomY <= 2930) {{
        radarHud.classList.remove('danger');
        radarDot.style.background = 'var(--success)';
        radarDot.style.boxShadow = '0 0 6px var(--success)';
        radarText.textContent = `Clearance Safe (+${{jeepBuffer}}px to Jeepney)`;
    }} else {{
        radarHud.classList.add('danger');
        radarDot.style.background = 'var(--danger)';
        radarDot.style.boxShadow = '0 0 10px var(--danger)';
        radarText.textContent = `WARNING: Touching Hazard Zone (${{jeepBuffer}}px)!`;
    }}
}}

// --- DOCK PANELS & PROPERTIES SYNC ---
function updateLayersPanel() {{
    layersList.innerHTML = '';
    const countEl = document.getElementById('layersCount');
    countEl.textContent = `${{layers.length - 1}} layers`;

    // Render in reverse order (Photoshop top-to-bottom stack)
    for (let i = layers.length - 1; i >= 0; i--) {{
        const layer = layers[i];
        if (layer.type === 'background') continue;

        const row = document.createElement('div');
        row.className = 'layer-item' + (layer.id === selectedLayerId ? ' active' : '');

        const iconBadge = document.createElement('span');
        iconBadge.className = 'layer-item-icon';
        iconBadge.textContent = layer.type === 'image' ? '🖼' : 'T';

        const nameSpan = document.createElement('span');
        nameSpan.className = 'layer-item-name';
        nameSpan.textContent = layer.name;

        // Eye button (visibility)
        const eyeBtn = document.createElement('button');
        eyeBtn.className = 'layer-btn-icon' + (layer.visible ? ' active' : '');
        eyeBtn.innerHTML = layer.visible ? '👁' : '─';
        eyeBtn.title = 'Toggle Visibility';
        eyeBtn.addEventListener('click', (e) => {{
            e.stopPropagation();
            layer.visible = !layer.visible;
            renderLayers();
            updateTransformBox();
            updateLayersPanel();
            updateRadar();
            pushHistory(`Toggle Visibility: ${{layer.name}}`);
            saveCurrentDay();
        }});

        // Lock button
        const lockBtn = document.createElement('button');
        lockBtn.className = 'layer-btn-icon' + (layer.locked ? ' active' : '');
        lockBtn.innerHTML = layer.locked ? '🔒' : '🔓';
        lockBtn.title = 'Lock Position';
        lockBtn.addEventListener('click', (e) => {{
            e.stopPropagation();
            layer.locked = !layer.locked;
            renderLayers();
            updateTransformBox();
            updateLayersPanel();
            saveCurrentDay();
        }});

        row.appendChild(iconBadge);
        row.appendChild(nameSpan);
        row.appendChild(eyeBtn);
        row.appendChild(lockBtn);

        row.addEventListener('click', () => {{
            selectLayer(layer.id);
        }});

        layersList.appendChild(row);
    }}
}}

function updatePropertiesPanel() {{
    const layer = getSelectedLayer();
    if (!layer) {{
        sectionImageProps.style.display = 'none';
        sectionTextProps.style.display = 'none';
        propX.value = '';
        propY.value = '';
        propW.value = '';
        propH.value = '';
        return;
    }}

    propX.value = layer.x;
    propY.value = layer.y;
    propW.value = layer.width || '';
    propH.value = layer.height || '';
    propOpacity.value = layer.opacity !== undefined ? layer.opacity : 1.0;
    propOpacityVal.textContent = `${{Math.round((layer.opacity !== undefined ? layer.opacity : 1.0) * 100)}}%`;

    if (layer.type === 'image') {{
        sectionImageProps.style.display = 'block';
        sectionTextProps.style.display = 'none';
        propIconSelect.value = layer.src;
    }} else if (layer.type === 'text') {{
        sectionImageProps.style.display = 'none';
        sectionTextProps.style.display = 'block';

        propTextContent.value = layer.text;
        propFontFamily.value = layer.fontFamily || 'Gotham Ultra';
        propFontSizeSlider.value = layer.fontSize || 60;
        propFontSizeNum.value = layer.fontSize || 60;
        propLineHeight.value = layer.lineHeight || 1.15;
        propTextAlign.value = layer.textAlign || 'left';
        propTextColor.value = layer.color || '#FFFFFF';
        propStrokeWidthSlider.value = layer.strokeWidth || 0;
        propStrokeWidthNum.value = layer.strokeWidth || 0;
        propStrokeColor.value = layer.strokeColor && layer.strokeColor !== 'transparent' ? layer.strokeColor : '#FF6D00';
    }}
}}

function updateOptionsBar() {{
    const layer = getSelectedLayer();
    if (!layer) {{
        optLayerName.textContent = 'None';
        optX.value = '';
        optY.value = '';
        optW.value = '';
        optH.value = '';
        return;
    }}

    optLayerName.textContent = layer.name;
    optX.value = layer.x;
    optY.value = layer.y;
    optW.value = layer.width || '';
    optH.value = layer.height || '';
}}

// --- INPUT LISTENERS FOR PROPERTIES & OPTIONS ---
function bindInputSync(inputEl, propName, isNum = true, actionName = 'Change') {{
    inputEl.addEventListener('input', () => {{
        const layer = getSelectedLayer();
        if (!layer) return;
        layer[propName] = isNum ? parseFloat(inputEl.value) || 0 : inputEl.value;
        const node = document.getElementById(`node_${{layer.id}}`);
        if (node) {{
            if (propName === 'x') node.style.left = `${{layer.x}}px`;
            if (propName === 'y') node.style.top = `${{layer.y}}px`;
            if (propName === 'width') node.style.width = `${{layer.width}}px`;
            if (propName === 'height') node.style.height = `${{layer.height}}px`;
        }}
        updateTransformBox();
        updateOptionsBar();
        updateRadar();
    }});
    inputEl.addEventListener('change', () => {{
        const layer = getSelectedLayer();
        if (layer) {{
            pushHistory(`${{actionName}} ${{layer.name}}`);
            saveCurrentDay();
        }}
    }});
}}

bindInputSync(optX, 'x', true, 'Move');
bindInputSync(optY, 'y', true, 'Move');
bindInputSync(optW, 'width', true, 'Resize');
bindInputSync(optH, 'height', true, 'Resize');

bindInputSync(propX, 'x', true, 'Move');
bindInputSync(propY, 'y', true, 'Move');
bindInputSync(propW, 'width', true, 'Resize');
bindInputSync(propH, 'height', true, 'Resize');

// Opacity
propOpacity.addEventListener('input', () => {{
    const layer = getSelectedLayer();
    if (!layer) return;
    layer.opacity = parseFloat(propOpacity.value);
    propOpacityVal.textContent = `${{Math.round(layer.opacity * 100)}}%`;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) node.style.opacity = layer.opacity;
}});
propOpacity.addEventListener('change', () => {{
    pushHistory('Change Opacity');
    saveCurrentDay();
}});

// Text Content Input
propTextContent.addEventListener('input', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.text = propTextContent.value;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) textDom.textContent = layer.text;
    }}
    updateTransformBox();
    updateRadar();
}});
propTextContent.addEventListener('change', () => {{
    pushHistory('Edit Text');
    saveCurrentDay();
}});

// Font Family
propFontFamily.addEventListener('change', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.fontFamily = propFontFamily.value;
    renderLayers();
    updateTransformBox();
    pushHistory('Change Font');
    saveCurrentDay();
}});

// Font Size
function updateFontSize(val) {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.fontSize = parseInt(val) || 60;
    propFontSizeSlider.value = layer.fontSize;
    propFontSizeNum.value = layer.fontSize;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) textDom.style.fontSize = `${{layer.fontSize}}px`;
    }}
    updateTransformBox();
    updateRadar();
}}
propFontSizeSlider.addEventListener('input', () => updateFontSize(propFontSizeSlider.value));
propFontSizeSlider.addEventListener('change', () => {{ pushHistory('Change Font Size'); saveCurrentDay(); }});
propFontSizeNum.addEventListener('input', () => updateFontSize(propFontSizeNum.value));
propFontSizeNum.addEventListener('change', () => {{ pushHistory('Change Font Size'); saveCurrentDay(); }});

// Line Height
propLineHeight.addEventListener('input', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.lineHeight = parseFloat(propLineHeight.value) || 1.15;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) textDom.style.lineHeight = layer.lineHeight;
    }}
    updateTransformBox();
    updateRadar();
}});
propLineHeight.addEventListener('change', () => {{ pushHistory('Change Line Height'); saveCurrentDay(); }});

// Text Alignment
propTextAlign.addEventListener('change', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.textAlign = propTextAlign.value;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) textDom.style.textAlign = layer.textAlign;
    }}
    pushHistory('Change Alignment');
    saveCurrentDay();
}});

// Fill Color
propTextColor.addEventListener('input', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.color = propTextColor.value;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) textDom.style.color = layer.color;
    }}
}});
propTextColor.addEventListener('change', () => {{ pushHistory('Change Text Color'); saveCurrentDay(); }});

// Fill Swatches
document.querySelectorAll('[data-color]').forEach(sw => {{
    sw.addEventListener('click', () => {{
        const layer = getSelectedLayer();
        if (!layer || layer.type !== 'text') return;
        layer.color = sw.dataset.color;
        propTextColor.value = layer.color;
        const node = document.getElementById(`node_${{layer.id}}`);
        if (node) {{
            const textDom = node.querySelector('.layer-text');
            if (textDom) textDom.style.color = layer.color;
        }}
        pushHistory('Change Text Color');
        saveCurrentDay();
    }});
}});

// Stroke Width
function updateStrokeWidth(val) {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.strokeWidth = parseInt(val) || 0;
    propStrokeWidthSlider.value = layer.strokeWidth;
    propStrokeWidthNum.value = layer.strokeWidth;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) {{
            textDom.style.webkitTextStroke = layer.strokeWidth > 0 ? `${{layer.strokeWidth}}px ${{layer.strokeColor || '#FF6D00'}}` : '0px transparent';
        }}
    }}
}}
propStrokeWidthSlider.addEventListener('input', () => updateStrokeWidth(propStrokeWidthSlider.value));
propStrokeWidthSlider.addEventListener('change', () => {{ pushHistory('Change Stroke Width'); saveCurrentDay(); }});
propStrokeWidthNum.addEventListener('input', () => updateStrokeWidth(propStrokeWidthNum.value));
propStrokeWidthNum.addEventListener('change', () => {{ pushHistory('Change Stroke Width'); saveCurrentDay(); }});

// Stroke Color
propStrokeColor.addEventListener('input', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'text') return;
    layer.strokeColor = propStrokeColor.value;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const textDom = node.querySelector('.layer-text');
        if (textDom) textDom.style.webkitTextStroke = `${{layer.strokeWidth || 16}}px ${{layer.strokeColor}}`;
    }}
}});
propStrokeColor.addEventListener('change', () => {{ pushHistory('Change Stroke Color'); saveCurrentDay(); }});

// Stroke Swatches
document.querySelectorAll('[data-stroke]').forEach(sw => {{
    sw.addEventListener('click', () => {{
        const layer = getSelectedLayer();
        if (!layer || layer.type !== 'text') return;
        layer.strokeColor = sw.dataset.stroke;
        if (layer.strokeColor !== 'transparent') propStrokeColor.value = layer.strokeColor;
        const node = document.getElementById(`node_${{layer.id}}`);
        if (node) {{
            const textDom = node.querySelector('.layer-text');
            if (textDom) {{
                textDom.style.webkitTextStroke = layer.strokeColor === 'transparent' ? '0px transparent' : `${{layer.strokeWidth || 16}}px ${{layer.strokeColor}}`;
            }}
        }}
        pushHistory('Change Stroke Color');
        saveCurrentDay();
    }});
}});

// Icon Select
propIconSelect.addEventListener('change', () => {{
    const layer = getSelectedLayer();
    if (!layer || layer.type !== 'image') return;
    layer.src = propIconSelect.value;
    const node = document.getElementById(`node_${{layer.id}}`);
    if (node) {{
        const img = node.querySelector('img');
        if (img) img.src = layer.src;
    }}
    pushHistory('Swap Hero Icon');
    saveCurrentDay();
}});

// Custom Icon Upload
propIconUpload.addEventListener('change', (e) => {{
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (ev) => {{
        const layer = getSelectedLayer();
        if (!layer) return;
        layer.src = ev.target.result;
        layer.type = 'image';
        renderLayers();
        updateTransformBox();
        pushHistory('Upload Custom Icon');
        saveCurrentDay();
    }};
    reader.readAsDataURL(file);
}});

// --- ALIGNMENT CONTROLS ---
document.getElementById('btnAlignLeft').addEventListener('click', () => {{
    const layer = getSelectedLayer();
    if (!layer) return;
    layer.x = 190;
    renderLayers();
    updateTransformBox();
    updateOptionsBar();
    updatePropertiesPanel();
    pushHistory('Align Left');
    saveCurrentDay();
}});

document.getElementById('btnAlignCenter').addEventListener('click', () => {{
    const layer = getSelectedLayer();
    if (!layer) return;
    const node = document.getElementById(`node_${{layer.id}}`);
    const w = node ? node.offsetWidth : (layer.width || 0);
    layer.x = Math.round(1240 - w / 2);
    renderLayers();
    updateTransformBox();
    updateOptionsBar();
    updatePropertiesPanel();
    pushHistory('Align Center');
    saveCurrentDay();
}});

document.getElementById('btnAlignRight').addEventListener('click', () => {{
    const layer = getSelectedLayer();
    if (!layer) return;
    const node = document.getElementById(`node_${{layer.id}}`);
    const w = node ? node.offsetWidth : (layer.width || 0);
    layer.x = 2290 - w;
    renderLayers();
    updateTransformBox();
    updateOptionsBar();
    updatePropertiesPanel();
    pushHistory('Align Right');
    saveCurrentDay();
}});

// --- LAYER REORDERING ---
function moveLayerOrder(step) {{
    const idx = layers.findIndex(l => l.id === selectedLayerId);
    if (idx === -1) return;
    const newIdx = idx + step;
    if (newIdx <= 0 || newIdx >= layers.length) return; // index 0 is background

    const [moved] = layers.splice(idx, 1);
    layers.splice(newIdx, 0, moved);

    renderLayers();
    updateLayersPanel();
    pushHistory(step > 0 ? 'Bring Forward' : 'Send Backward');
    saveCurrentDay();
}}

document.getElementById('btnBringForward').addEventListener('click', () => moveLayerOrder(1));
document.getElementById('btnSendBackward').addEventListener('click', () => moveLayerOrder(-1));

// --- LAYER CREATION & DELETION ---
function addNewTextLayer() {{
    const newId = `custom_text_${{Date.now()}}`;
    const newLayer = {{
        id: newId,
        name: `New Text Layer`,
        type: 'text',
        x: 300,
        y: 1900,
        width: 1800,
        height: 'auto',
        text: 'Editable Text Block',
        fontFamily: 'Gotham Bold',
        fontSize: 70,
        lineHeight: 1.15,
        color: '#FFFFFF',
        strokeColor: '#FF6D00',
        strokeWidth: 16,
        textAlign: 'center',
        locked: false,
        visible: true,
        opacity: 1.0
    }};
    layers.push(newLayer);
    renderLayers();
    selectLayer(newId);
    pushHistory('Add Text Layer');
    saveCurrentDay();
}}

function addNewIconLayer() {{
    const newId = `custom_icon_${{Date.now()}}`;
    const newLayer = {{
        id: newId,
        name: `New Icon Layer`,
        type: 'image',
        x: 940,
        y: 1400,
        width: 600,
        height: 600,
        src: 'icons/DAY 1.png',
        locked: false,
        visible: true,
        opacity: 1.0
    }};
    layers.push(newLayer);
    renderLayers();
    selectLayer(newId);
    pushHistory('Add Icon Layer');
    saveCurrentDay();
}}

document.getElementById('btnAddTextLayer').addEventListener('click', addNewTextLayer);
document.getElementById('dockAddTextBtn').addEventListener('click', addNewTextLayer);
document.getElementById('btnAddIconLayer').addEventListener('click', addNewIconLayer);

function duplicateSelectedLayer() {{
    const layer = getSelectedLayer();
    if (!layer || layer.type === 'background') return;

    const dup = deepClone(layer);
    dup.id = `dup_${{Date.now()}}`;
    dup.name = `${{layer.name}} (Copy)`;
    dup.x += 40;
    dup.y += 40;

    layers.push(dup);
    renderLayers();
    selectLayer(dup.id);
    pushHistory(`Duplicate ${{layer.name}}`);
    saveCurrentDay();
}}
document.getElementById('dockDuplicateBtn').addEventListener('click', duplicateSelectedLayer);

function deleteSelectedLayer() {{
    const layer = getSelectedLayer();
    if (!layer || layer.type === 'background') return;

    const idx = layers.findIndex(l => l.id === layer.id);
    if (idx !== -1) {{
        layers.splice(idx, 1);
        selectedLayerId = null;
        renderLayers();
        updateTransformBox();
        updateLayersPanel();
        updatePropertiesPanel();
        updateRadar();
        pushHistory(`Delete ${{layer.name}}`);
        saveCurrentDay();
    }}
}}
document.getElementById('dockDeleteBtn').addEventListener('click', deleteSelectedLayer);

// --- DAY SWITCHING & NAVIGATION ---
daySelect.addEventListener('change', () => {{
    loadDay(daySelect.value);
}});

document.getElementById('prevDayBtn').addEventListener('click', () => {{
    let idx = daySelect.selectedIndex - 1;
    if (idx < 0) idx = daySelect.options.length - 1;
    daySelect.selectedIndex = idx;
    loadDay(daySelect.value);
}});

document.getElementById('nextDayBtn').addEventListener('click', () => {{
    let idx = daySelect.selectedIndex + 1;
    if (idx >= daySelect.options.length) idx = 0;
    daySelect.selectedIndex = idx;
    loadDay(daySelect.value);
}});

// RESET DAY
document.getElementById('resetDayBtn').addEventListener('click', () => {{
    if (confirm(`Reset ${{daySelect.options[daySelect.selectedIndex].text}} to default calibrated layout?`)) {{
        localStorage.removeItem(`poster_layers_${{currentDayId}}`);
        layers = deepClone(DEFAULT_LAYERS_BY_DAY[currentDayId] || []);
        renderLayers();
        updateLayersPanel();
        updatePropertiesPanel();
        updateTransformBox();
        updateRadar();
        pushHistory('Reset to Default');
        showToast('Reset to calibrated layout!');
    }}
}});

// LOCAL STORAGE PERSISTENCE
function saveCurrentDay() {{
    localStorage.setItem(`poster_layers_${{currentDayId}}`, JSON.stringify(layers));
}}

// COPY JSON
document.getElementById('copyJsonBtn').addEventListener('click', () => {{
    const exportData = {{
        day_id: currentDayId,
        badge: daySelect.options[daySelect.selectedIndex].text.split('—')[0].trim(),
        layers: layers
    }};
    navigator.clipboard.writeText(JSON.stringify(exportData, null, 2)).then(() => {{
        showToast('Copied layer coordinates to clipboard!');
    }});
}});

// UNDO / REDO BUTTONS
document.getElementById('undoBtn').addEventListener('click', undo);
document.getElementById('redoBtn').addEventListener('click', redo);

// DOCK TABS
document.querySelectorAll('.dock-tab').forEach(tab => {{
    tab.addEventListener('click', () => {{
        document.querySelectorAll('.dock-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        tab.classList.add('active');
        document.getElementById(tab.dataset.tab).classList.add('active');
    }});
}});

// --- HIGH RESOLUTION 300 DPI EXPORT (HTML5 CANVAS COMPOSITE) ---
document.getElementById('downloadPngBtn').addEventListener('click', async () => {{
    showToast('Compositing 2480 × 3508 px print poster...');
    const expCanvas = document.getElementById('exportCanvas');
    const ctx = expCanvas.getContext('2d');

    ctx.clearRect(0, 0, 2480, 3508);

    // 1. Draw template background
    const bgImg = new Image();
    bgImg.src = 'FABMAT/fabmat_template.png';
    await new Promise(r => bgImg.onload = r);
    ctx.drawImage(bgImg, 0, 0, 2480, 3508);

    // 2. Draw each visible layer in order
    for (const layer of layers) {{
        if (!layer.visible || layer.type === 'background') continue;

        ctx.save();
        ctx.globalAlpha = layer.opacity !== undefined ? layer.opacity : 1.0;

        if (layer.type === 'image') {{
            const img = new Image();
            img.src = layer.src;
            await new Promise(r => img.onload = r);
            ctx.drawImage(img, layer.x, layer.y, layer.width, layer.height || layer.width);
        }} else if (layer.type === 'text') {{
            const node = document.getElementById(`node_${{layer.id}}`);
            const textDom = node ? node.querySelector('.layer-text') : null;

            ctx.font = `${{layer.fontSize || 60}}px "${{layer.fontFamily || 'Gotham Bold'}}"`;
            ctx.textAlign = layer.textAlign || 'left';
            ctx.textBaseline = 'top';

            let drawX = layer.x;
            if (layer.textAlign === 'center') {{
                drawX = layer.x + (layer.width || 2100) / 2;
            }} else if (layer.textAlign === 'right') {{
                drawX = layer.x + (layer.width || 2100);
            }}

            // Word wrap text
            const maxW = layer.width || 2100;
            const words = layer.text.split(' ');
            let line = '';
            let lineY = layer.y;
            const lineHeightPx = (layer.fontSize || 60) * (layer.lineHeight || 1.15);

            for (let n = 0; n < words.length; n++) {{
                const testLine = line + words[n] + ' ';
                const metrics = ctx.measureText(testLine);
                if (metrics.width > maxW && n > 0) {{
                    drawTextLine(ctx, line.trim(), drawX, lineY, layer);
                    line = words[n] + ' ';
                    lineY += lineHeightPx;
                }} else {{
                    line = testLine;
                }}
            }}
            drawTextLine(ctx, line.trim(), drawX, lineY, layer);
        }}
        ctx.restore();
    }}

    // Trigger download
    const link = document.createElement('a');
    link.download = `${{SCHEDULE_DATA.find(d => d.id === currentDayId).filename.replace('.png', '')}}_Custom_300DPI.png`;
    link.href = expCanvas.toDataURL('image/png');
    link.click();
    showToast('Download started!');
}});

function drawTextLine(ctx, text, x, y, layer) {{
    if (layer.strokeWidth && layer.strokeWidth > 0 && layer.strokeColor && layer.strokeColor !== 'transparent') {{
        ctx.lineWidth = layer.strokeWidth * 2;
        ctx.strokeStyle = layer.strokeColor;
        ctx.lineJoin = 'miter';
        ctx.miterLimit = 2;
        ctx.strokeText(text, x, y);
    }}
    ctx.fillStyle = layer.color || '#FFFFFF';
    ctx.fillText(text, x, y);
}}

// START APPLICATION
window.addEventListener('load', initApp);
window.addEventListener('resize', () => {{
    fitToScreen();
    drawRulers();
}});
</script>
</body>
</html>
"""

editor_path = os.path.join(BASE_DIR, "editor.html")
with open(editor_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✓ Successfully generated Photoshop-grade {editor_path} ({len(html_template)} bytes)")


