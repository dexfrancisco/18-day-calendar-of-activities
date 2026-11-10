"""
18-Day Orange Campaign Daily Poster Generator (Official Header-Matched Orange Outline & Zero-Shadow Architecture)
Outputs:
  - 19 Native 1x posters in FABMAT/ and output/1x/ (2480 x 3508 px, 300 DPI)
  - 19 Double-density 2x posters in output/2x/ (4960 x 7016 px)
  - 1 Combined 19-page PDF at output/18-day-campaign-posters.pdf

Design System:
  - Direct Canvas: Zero panels, zero white cards, zero container boxes around text or icons.
  - Master Text Outlines: -webkit-text-stroke with paint-order: stroke fill in header orange (#FF6D00).
  - Pure Flat Vector: Zero drop-shadows on text and zero drop-shadows on icons.
  - Typography: Licensed Gotham family (Gotham Ultra, Gotham Bold, Gotham Medium Italic) in pure white (#FFFFFF).
  - Header Row: Hero icon on the left (as-is, clean, enlarged 750px on light days), Day badge + Date line on the right.
  - Middle: Single activity titles/subtitles centered in the middle; multi-activity days numbered cleanly on left.
  - Bottom: Minimized spacing between sections; LEAD OFFICE, PARTNERS, VENUE grid.
  - Safe Content Zone: y in [1300, 2960] px (strictly clears top banner and bottom jeepney/logo).
"""

import os
import sys
import json
import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
from pypdf import PdfWriter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "Gotham-font-family", "Gotham")
ICONS_DIR = os.path.join(BASE_DIR, "icons")
TEMPLATE_PATH = os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")
SCHEDULE_DATA_JSON = os.path.join(BASE_DIR, "scratch", "schedule_data.json")

OUT_DIR = os.path.join(BASE_DIR, "output")
OUT_1X = os.path.join(OUT_DIR, "1x")
OUT_2X = os.path.join(OUT_DIR, "2x")
OUT_PDF = os.path.join(OUT_DIR, "18-day-campaign-posters.pdf")
FABMAT_DIR = os.path.join(BASE_DIR, "FABMAT")
HTML_DIR = os.path.join(BASE_DIR, "scratch", "final_html")
THUMBS_DIR = os.path.join(BASE_DIR, "scratch", "final_thumbs")

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9198

os.makedirs(OUT_1X, exist_ok=True)
os.makedirs(OUT_2X, exist_ok=True)
os.makedirs(FABMAT_DIR, exist_ok=True)
os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

COMMON_CSS = """
@font-face {
    font-family: 'Gotham Black';
    src: url('/Gotham-font-family/Gotham/Gotham-Black.otf') format('opentype');
    font-weight: 900;
}
@font-face {
    font-family: 'Gotham Ultra';
    src: url('/Gotham-font-family/Gotham/Gotham-Ultra.otf') format('opentype');
    font-weight: 900;
}
@font-face {
    font-family: 'Gotham Bold';
    src: url('/Gotham-font-family/Gotham/Gotham-Bold.otf') format('opentype');
    font-weight: 700;
}
@font-face {
    font-family: 'Gotham Medium';
    src: url('/Gotham-font-family/Gotham/Gotham-Medium.otf') format('opentype');
    font-weight: 500;
}
@font-face {
    font-family: 'Gotham Book';
    src: url('/Gotham-font-family/Gotham/Gotham-Book.otf') format('opentype');
    font-weight: 400;
}
@font-face {
    font-family: 'Gotham Medium Italic';
    src: url('/Gotham-font-family/Gotham/Gotham-MediumItalic.otf') format('opentype');
    font-style: italic;
    font-weight: 500;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    width: 2480px;
    height: 3508px;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: url('/FABMAT/fabmat_template.png') no-repeat top left;
    background-size: 2480px 3508px;
    font-family: 'Gotham Bold', sans-serif;
    -webkit-font-smoothing: antialiased;
}

.hero-icon {
    object-fit: contain;
    flex-shrink: 0;
}

.top-row {
    display: flex;
    align-items: center;
    gap: 45px;
    width: 100%;
}

.day-date-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.stroke-day {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 3px;
    line-height: 1.05;
    paint-order: stroke fill;
    -webkit-text-stroke: 18px #FF6D00;
}

.stroke-date {
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    letter-spacing: 2px;
    line-height: 1.15;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
}

.stroke-title {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    line-height: 1.16;
    letter-spacing: -0.5px;
    paint-order: stroke fill;
    -webkit-text-stroke: 16px #FF6D00;
}

.stroke-subtitle {
    color: #FFFFFF;
    font-family: 'Gotham Medium Italic', sans-serif;
    line-height: 1.2;
    letter-spacing: 0.5px;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
}

.stroke-tag {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px;
    line-height: 1.2;
    text-transform: uppercase;
    paint-order: stroke fill;
    -webkit-text-stroke: 10px #FF6D00;
}

.stroke-num {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    line-height: 1.1;
    paint-order: stroke fill;
    -webkit-text-stroke: 14px #FF6D00;
}

.stroke-act-desc {
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00;
}

.stroke-label {
    color: #FFFFFF;
    font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px;
    line-height: 1.25;
    text-transform: uppercase;
    paint-order: stroke fill;
    -webkit-text-stroke: 11px #FF6D00;
}

.stroke-val {
    color: #FFFFFF;
    font-family: 'Gotham Bold', sans-serif;
    line-height: 1.25;
    paint-order: stroke fill;
    -webkit-text-stroke: 11px #FF6D00;
}

.detail-row {
    display: flex;
    align-items: baseline;
    gap: 20px;
}
"""

def render_day_html(day):
    layout_type = day.get("layout_type")
    icon_fn = day.get("icon_filename")
    badge = day.get("badge")
    date_str = day.get("date_str")
    day_num = day.get("day_number")

    # 1. PRE-CAMPAIGN
    if layout_type == "pre_campaign":
        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
        .safe-zone {{
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 36px;
        }}
        .hero-icon {{ width: 750px; height: 750px; }}
        .stroke-day {{ font-size: 146px; }}
        .stroke-date {{ font-size: 68px; }}
        .middle-block {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 14px;
            width: 100%;
        }}
        .stroke-title {{ font-size: 112px; }}
        .stroke-subtitle {{ font-size: 76px; }}
        .bottom-block {{ display: flex; flex-direction: column; gap: 16px; width: 100%; }}
        .detail-label-col {{ width: 420px; flex-shrink: 0; font-size: 54px; }}
        .detail-val-col {{ flex: 1; font-size: 58px; }}
        </style></head><body>
        <div class="safe-zone">
            <div class="top-row">
                <img class="hero-icon" src="/icons/{icon_fn}">
                <div class="day-date-group">
                    <div class="stroke-day">{badge}</div>
                    <div class="stroke-date">{date_str}</div>
                </div>
            </div>
            <div class="middle-block">
                <div class="stroke-title">{day.get('title')}</div>
                <div class="stroke-subtitle">{day.get('subtitle')}</div>
            </div>
            <div class="bottom-block">
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">LEAD OFFICE:</div>
                    <div class="detail-val-col stroke-val">{day.get('lead_office')}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">PARTNERS:</div>
                    <div class="detail-val-col stroke-val">{day.get('partners')}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">VENUE:</div>
                    <div class="detail-val-col stroke-val">{day.get('venue')}</div>
                </div>
            </div>
        </div>
        </body></html>"""

    # 2. SINGLE ACTIVITY (Days 4, 6, 7, 14)
    elif layout_type == "single_activity":
        title = day.get("main_activity")
        special_badge = day.get("special_badge")
        special_html = f'<div class="stroke-subtitle" style="font-size:62px; margin-top:4px;">★ {special_badge} ★</div>' if special_badge else ''
        
        # Sizing calibrated for text length
        if day_num == 10:
            icon_sz = 580
            title_font_size = 78
            safe_gap = 20
            mid_gap = 10
            bottom_gap = 10
            bot_lbl_sz = 44
            bot_val_sz = 46
        elif len(title) > 130:
            icon_sz = 660
            title_font_size = 86
            safe_gap = 28
            mid_gap = 12
            bottom_gap = 12
            bot_lbl_sz = 50
            bot_val_sz = 54
        elif len(title) > 85 or day_num == 6:
            icon_sz = 680
            title_font_size = 92
            safe_gap = 28
            mid_gap = 12
            bottom_gap = 12
            bot_lbl_sz = 52
            bot_val_sz = 56
        else:
            icon_sz = 750
            title_font_size = 108
            safe_gap = 36
            mid_gap = 16
            bottom_gap = 16
            bot_lbl_sz = 54
            bot_val_sz = 58

        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
        .safe-zone {{
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: {safe_gap}px;
        }}
        .hero-icon {{ width: {icon_sz}px; height: {icon_sz}px; }}
        .stroke-day {{ font-size: 146px; }}
        .stroke-date {{ font-size: 66px; }}
        .middle-block {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: {mid_gap}px;
            width: 100%;
        }}
        .stroke-title {{ font-size: {title_font_size}px; line-height: 1.16; }}
        .bottom-block {{ display: flex; flex-direction: column; gap: {bottom_gap}px; width: 100%; }}
        .detail-label-col {{ width: 420px; flex-shrink: 0; font-size: {bot_lbl_sz}px; }}
        .detail-val-col {{ flex: 1; font-size: {bot_val_sz}px; }}
        </style></head><body>
        <div class="safe-zone">
            <div class="top-row">
                <img class="hero-icon" src="/icons/{icon_fn}">
                <div class="day-date-group">
                    <div class="stroke-day">{badge}</div>
                    <div class="stroke-date">{date_str}</div>
                </div>
            </div>
            <div class="middle-block">
                <div class="stroke-title">{title}</div>
                {special_html}
            </div>
            <div class="bottom-block">
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">LEAD OFFICE:</div>
                    <div class="detail-val-col stroke-val">{day.get('lead_office')}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">PARTNERS:</div>
                    <div class="detail-val-col stroke-val">{day.get('partners')}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">VENUE:</div>
                    <div class="detail-val-col stroke-val">{day.get('venue')}</div>
                </div>
            </div>
        </div>
        </body></html>"""

    # 3. ONLINE ONLY (Days 5, 12)
    elif layout_type == "online_only":
        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
        .safe-zone {{
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 40px;
        }}
        .hero-icon {{ width: 750px; height: 750px; }}
        .stroke-day {{ font-size: 146px; }}
        .stroke-date {{ font-size: 68px; }}
        .middle-block {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 28px;
            width: 100%;
            margin-top: 20px;
        }}
        .stroke-title {{ font-size: 96px; line-height: 1.25; max-width: 1850px; }}
        .online-pill {{ font-size: 68px; letter-spacing: 3px; }}
        </style></head><body>
        <div class="safe-zone">
            <div class="top-row">
                <img class="hero-icon" src="/icons/{icon_fn}">
                <div class="day-date-group">
                    <div class="stroke-day">{badge}</div>
                    <div class="stroke-date">{date_str}</div>
                </div>
            </div>
            <div class="middle-block">
                <div class="stroke-tag online-pill">{day.get('advocacy_track')}</div>
                <div class="stroke-title">{day.get('description')}</div>
            </div>
        </div>
        </body></html>"""

    # 4. STANDARD MULTI-ACTIVITY (Days 1, 2, 8, 9, 10, 13, 15, 16)
    elif layout_type == "standard_activities":
        acts = day.get("activities", [])
        num_acts = len(acts)

        if day_num == 10 or num_acts >= 5:
            # Day 10 (5 activities) - scaled up and well grouped
            icon_sz = 460
            day_font_sz = 132
            date_font_sz = 60
            num_sz = 50
            num_w = 58
            act_desc_sz = 44
            line_h = 1.15
            lead_lbl_sz = 36
            lead_val_sz = 38
            lead_gap = 5
            lead_indent = 76
            act_gap = 14
            safe_gap = 22
            bottom_lbl_sz = 42
            bottom_val_sz = 44
            bottom_gap = 10
            lbl_w = 350
        elif num_acts == 2:
            if day_num == 15:
                # Day 15 has extensive text (awardings + project orange rise + 4 lines of partners)
                icon_sz = 600
                day_font_sz = 142
                date_font_sz = 64
                num_sz = 64
                num_w = 68
                act_desc_sz = 58
                line_h = 1.15
                lead_lbl_sz = 40
                lead_val_sz = 44
                lead_gap = 6
                lead_indent = 78
                act_gap = 18
                safe_gap = 20
                bottom_lbl_sz = 46
                bottom_val_sz = 48
                bottom_gap = 10
                lbl_w = 380
            elif day_num == 9:
                # Day 9 has 3 lines of partners
                icon_sz = 660
                day_font_sz = 146
                date_font_sz = 68
                num_sz = 72
                num_w = 76
                act_desc_sz = 68
                line_h = 1.15
                lead_lbl_sz = 46
                lead_val_sz = 50
                lead_gap = 6
                lead_indent = 90
                act_gap = 22
                safe_gap = 24
                bottom_lbl_sz = 50
                bottom_val_sz = 52
                bottom_gap = 12
                lbl_w = 400
            else:
                # 2 Activities (Days 1, 8, 16) - Prominent, larger text & details!
                icon_sz = 720
                day_font_sz = 146
                date_font_sz = 68
                num_sz = 76
                num_w = 80
                act_desc_sz = 74
                line_h = 1.16
                lead_lbl_sz = 48
                lead_val_sz = 52
                lead_gap = 8
                lead_indent = 98
                act_gap = 30
                safe_gap = 30
                bottom_lbl_sz = 54
                bottom_val_sz = 58
                bottom_gap = 16
                lbl_w = 420
        else:
            # 3 Activities (Day 2, Day 13)
            icon_sz = 600
            day_font_sz = 142
            date_font_sz = 64
            num_sz = 66
            num_w = 72
            act_desc_sz = 58
            line_h = 1.16
            lead_lbl_sz = 44
            lead_val_sz = 48
            lead_gap = 6
            lead_indent = 88
            act_gap = 22
            safe_gap = 26
            bottom_lbl_sz = 50
            bottom_val_sz = 54
            bottom_gap = 14
            lbl_w = 400

        acts_html = ""
        for a in acts:
            num = a.get("num")
            desc = a.get("description")
            date_range = a.get("date_range")
            range_badge = f' <span class="stroke-tag" style="font-size:38px; margin-left:12px;">({date_range})</span>' if date_range else ''
            acts_html += f"""
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">{num}.</div>
                    <div class="stroke-act-desc act-desc">{desc}{range_badge}</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">{a.get('lead_office')}</span>
                </div>
            </div>
            """

        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
        .safe-zone {{
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            gap: {safe_gap}px;
        }}
        .hero-icon {{ width: {icon_sz}px; height: {icon_sz}px; }}
        .stroke-day {{ font-size: {day_font_sz}px; }}
        .stroke-date {{ font-size: {date_font_sz}px; }}
        .acts-block {{
            display: flex;
            flex-direction: column;
            gap: {act_gap}px;
            width: 100%;
        }}
        .act-item {{
            display: flex;
            flex-direction: column;
            gap: {lead_gap}px;
        }}
        .act-header-row {{
            display: flex;
            align-items: baseline;
            gap: 18px;
        }}
        .act-num {{
            font-size: {num_sz}px;
            flex-shrink: 0;
            width: {num_w}px;
        }}
        .act-desc {{
            font-size: {act_desc_sz}px;
            line-height: {line_h};
            flex: 1;
        }}
        .act-lead-row {{
            display: flex;
            align-items: baseline;
            gap: 18px;
            margin-left: {lead_indent}px;
        }}
        .act-lead-lbl {{
            font-size: {lead_lbl_sz}px;
            flex-shrink: 0;
        }}
        .act-lead-val {{
            font-size: {lead_val_sz}px;
            flex: 1;
        }}
        .bottom-block {{
            display: flex;
            flex-direction: column;
            gap: {bottom_gap}px;
            width: 100%;
        }}
        .detail-label-col {{ width: {lbl_w}px; flex-shrink: 0; font-size: {bottom_lbl_sz}px; }}
        .detail-val-col {{ flex: 1; font-size: {bottom_val_sz}px; }}
        </style></head><body>
        <div class="safe-zone">
            <div class="top-row">
                <img class="hero-icon" src="/icons/{icon_fn}">
                <div class="day-date-group">
                    <div class="stroke-day">{badge}</div>
                    <div class="stroke-date">{date_str}</div>
                </div>
            </div>
            <div class="acts-block">
                {acts_html}
            </div>
            <div class="bottom-block">
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">PARTNERS:</div>
                    <div class="detail-val-col stroke-val">{day.get('partners')}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">VENUE:</div>
                    <div class="detail-val-col stroke-val">{day.get('venue')}</div>
                </div>
            </div>
        </div>
        </body></html>"""

    # 5. DUAL GROUP DAY 3
    elif layout_type == "day3_dual_group":
        g1 = day.get("group1", {})
        g2 = day.get("group2", {})
        icon_sz = 520
        day_font_sz = 138
        date_font_sz = 62
        num_sz = 54
        num_w = 60
        act_desc_sz = 48
        line_h = 1.16
        lead_lbl_sz = 38
        lead_val_sz = 42
        lead_gap = 6
        lead_indent = 78
        act_gap = 18
        safe_gap = 24
        bottom_lbl_sz = 46
        bottom_val_sz = 48
        bottom_gap = 12
        lbl_w = 380

        acts_html = ""
        for a in g1.get("activities", []):
            num = a.get("num")
            desc = a.get("description")
            acts_html += f"""
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">{num}.</div>
                    <div class="stroke-act-desc act-desc">{desc}</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">{a.get('lead_office')}</span>
                </div>
            </div>
            """
        act4 = g2.get("activity", {})
        acts_html += f"""
        <div class="act-item">
            <div class="act-header-row">
                <div class="stroke-num act-num">{act4.get('num')}.</div>
                <div class="stroke-act-desc act-desc">{act4.get('description')}</div>
            </div>
            <div class="act-lead-row">
                <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                <span class="stroke-val act-lead-val">{act4.get('lead_office')}</span>
            </div>
        </div>
        """

        partners_comb = f"{g1.get('partners')} | {g2.get('partners')}"
        venue_comb = f"{g1.get('venue')} | {g2.get('venue')}"

        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
        .safe-zone {{
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            gap: {safe_gap}px;
        }}
        .hero-icon {{ width: {icon_sz}px; height: {icon_sz}px; }}
        .stroke-day {{ font-size: {day_font_sz}px; }}
        .stroke-date {{ font-size: {date_font_sz}px; }}
        .acts-block {{
            display: flex;
            flex-direction: column;
            gap: {act_gap}px;
            width: 100%;
        }}
        .act-item {{
            display: flex;
            flex-direction: column;
            gap: {lead_gap}px;
        }}
        .act-header-row {{
            display: flex;
            align-items: baseline;
            gap: 18px;
        }}
        .act-num {{
            font-size: {num_sz}px;
            flex-shrink: 0;
            width: {num_w}px;
        }}
        .act-desc {{
            font-size: {act_desc_sz}px;
            line-height: {line_h};
            flex: 1;
        }}
        .act-lead-row {{
            display: flex;
            align-items: baseline;
            gap: 18px;
            margin-left: {lead_indent}px;
        }}
        .act-lead-lbl {{
            font-size: {lead_lbl_sz}px;
            flex-shrink: 0;
        }}
        .act-lead-val {{
            font-size: {lead_val_sz}px;
            flex: 1;
        }}
        .bottom-block {{
            display: flex;
            flex-direction: column;
            gap: {bottom_gap}px;
            width: 100%;
        }}
        .detail-label-col {{ width: {lbl_w}px; flex-shrink: 0; font-size: {bottom_lbl_sz}px; }}
        .detail-val-col {{ flex: 1; font-size: {bottom_val_sz}px; }}
        </style></head><body>
        <div class="safe-zone">
            <div class="top-row">
                <img class="hero-icon" src="/icons/{icon_fn}">
                <div class="day-date-group">
                    <div class="stroke-day">{badge}</div>
                    <div class="stroke-date">{date_str}</div>
                </div>
            </div>
            <div class="acts-block">
                {acts_html}
            </div>
            <div class="bottom-block">
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">PARTNERS:</div>
                    <div class="detail-val-col stroke-val">{partners_comb}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label-col stroke-label">VENUE:</div>
                    <div class="detail-val-col stroke-val">{venue_comb}</div>
                </div>
            </div>
        </div>
        </body></html>"""

    # 6. HYBRID DAYS (Days 11, 17, 18)
    elif layout_type in ["hybrid_day", "day18_hybrid", "hybrid_inperson_online"]:
        inp = day.get("in_person", {})
        onl = day.get("online", {})
        icon_sz = 680
        day_font_sz = 146
        date_font_sz = 66
        safe_gap = 32
        bottom_gap = 14
        lbl_w = 400

        if "activities" in inp:
            inp_html = ""
            for a in inp["activities"]:
                num = a.get("num")
                desc = a.get("description") or a.get("title")
                inp_html += f"""
                <div style="display:flex; align-items:baseline; gap:16px;">
                    <div class="stroke-num" style="font-size:58px; width:66px; flex-shrink:0;">{num}.</div>
                    <div class="stroke-act-desc" style="font-size:58px; line-height:1.18;">{desc}</div>
                </div>
                """
        else:
            main_act = inp.get("main_activity") or inp.get("title")
            inp_html = f"""
            <div class="stroke-act-desc" style="font-size:64px; line-height:1.18;">{main_act}</div>
            """

        lead_val = inp.get("lead_office", "GAD Office")
        partners_val = day.get("partners") or inp.get("partners", "")
        venue_val = day.get("venue") or inp.get("venue", "")

        partners_html = f"""
        <div class="detail-row">
            <div class="detail-label-col stroke-label">PARTNERS:</div>
            <div class="detail-val-col stroke-val">{partners_val}</div>
        </div>
        """ if partners_val else ""

        venue_html = f"""
        <div class="detail-row">
            <div class="detail-label-col stroke-label">VENUE:</div>
            <div class="detail-val-col stroke-val">{venue_val}</div>
        </div>
        """ if venue_val else ""

        return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{COMMON_CSS}
        .safe-zone {{
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            gap: {safe_gap}px;
        }}
        .hero-icon {{ width: {icon_sz}px; height: {icon_sz}px; }}
        .stroke-day {{ font-size: {day_font_sz}px; }}
        .stroke-date {{ font-size: {date_font_sz}px; }}
        .hybrid-container {{
            display: flex;
            flex-direction: column;
            gap: 22px;
            width: 100%;
        }}
        .track-block {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .track-tag {{
            font-size: 46px;
            align-self: flex-start;
        }}
        .bottom-block {{
            display: flex;
            flex-direction: column;
            gap: {bottom_gap}px;
            width: 100%;
        }}
        .detail-label-col {{ width: {lbl_w}px; flex-shrink: 0; font-size: 50px; }}
        .detail-val-col {{ flex: 1; font-size: 54px; }}
        </style></head><body>
        <div class="safe-zone">
            <div class="top-row">
                <img class="hero-icon" src="/icons/{icon_fn}">
                <div class="day-date-group">
                    <div class="stroke-day">{badge}</div>
                    <div class="stroke-date">{date_str}</div>
                </div>
            </div>
            <div class="hybrid-container">
                <div class="track-block">
                    <div class="stroke-tag track-tag">IN-PERSON ACTIVITY</div>
                    {inp_html}
                    <div style="display:flex; align-items:baseline; gap:16px; margin-top:2px;">
                        <span class="stroke-label" style="font-size:46px;">LEAD OFFICE:</span>
                        <span class="stroke-val" style="font-size:48px;">{lead_val}</span>
                    </div>
                </div>
                <div class="track-block">
                    <div class="stroke-tag track-tag">ONLINE ADVOCACY</div>
                    <div class="stroke-act-desc" style="font-size:56px; line-height:1.18;">{onl.get('description')}</div>
                </div>
            </div>
            <div class="bottom-block">
                {partners_html}
                {venue_html}
            </div>
        </div>
        </body></html>"""

def main():
    print("="*60)
    print("STARTING FULL POSTER GENERATOR (FLAT ORANGE OUTLINE)")
    print("="*60)

    # 1. Verify Fonts
    required_fonts = [
        "Gotham-Black.otf", "Gotham-Ultra.otf", "Gotham-Bold.otf",
        "Gotham-Medium.otf", "Gotham-Book.otf", "Gotham-MediumItalic.otf"
    ]
    for font_file in required_fonts:
        p = os.path.join(FONTS_DIR, font_file)
        if not os.path.exists(p):
            print(f"Error: Required Gotham font missing: {p}")
            sys.exit(1)
    print("✓ All required Gotham fonts verified in local fonts folder.")

    with open(SCHEDULE_DATA_JSON, "r", encoding="utf-8") as f:
        schedule_data = json.load(f)
    print(f"Loaded {len(schedule_data)} days.")

    # Start HTTP server
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    print(f"HTTP server running on port {PORT}")

    # Generate HTMLs
    for day in schedule_data:
        fn = day["filename"].replace(".png", "")
        h = render_day_html(day)
        h_path = os.path.join(HTML_DIR, f"{fn}.html")
        with open(h_path, "w", encoding="utf-8") as f:
            f.write(h)

    print("HTML files written. Rendering 1x posters...")

    # Render 1x posters and copy to FABMAT
    for day in schedule_data:
        fn = day["filename"].replace(".png", "")
        out_png = os.path.join(OUT_1X, f"{fn}.png")
        fabmat_png = os.path.join(FABMAT_DIR, f"{fn}.png")
        thumb_png = os.path.join(THUMBS_DIR, f"{fn}_thumb.png")
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--window-size=2480,3508",
            f"--screenshot={os.path.abspath(out_png)}",
            f"http://127.0.0.1:{PORT}/scratch/final_html/{fn}.html"
        ]
        t0 = time.time()
        subprocess.run(cmd, check=True)
        dt = time.time() - t0
        
        # Save to FABMAT and create thumb
        img = Image.open(out_png)
        img.save(fabmat_png, dpi=(300, 300))
        img.thumbnail((800, 1132))
        img.save(thumb_png)
        print(f"  [1x] Rendered & saved {fn}.png in {dt:.2f}s")

    # Render 2x posters
    print("\nRendering 2x posters...")
    for day in schedule_data:
        fn = day["filename"].replace(".png", "")
        out_png = os.path.join(OUT_2X, f"{fn}.png")
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=2",
            "--window-size=2480,3508",
            f"--screenshot={os.path.abspath(out_png)}",
            f"http://127.0.0.1:{PORT}/scratch/final_html/{fn}.html"
        ]
        t0 = time.time()
        subprocess.run(cmd, check=True)
        dt = time.time() - t0
        print(f"  [2x] Rendered {fn}.png in {dt:.2f}s")

    # Generate Combined PDF from 1x posters
    print("\nGenerating combined 19-page PDF...")
    pdf_writer = PdfWriter()
    temp_pdf_files = []
    for day in schedule_data:
        fn = day["filename"].replace(".png", "")
        src_png = os.path.join(OUT_1X, f"{fn}.png")
        temp_pdf = os.path.join(OUT_DIR, f"temp_{fn}.pdf")
        img = Image.open(src_png).convert("RGB")
        img.save(temp_pdf, "PDF", resolution=300.0)
        temp_pdf_files.append(temp_pdf)
        pdf_writer.append(temp_pdf)

    with open(OUT_PDF, "wb") as f:
        pdf_writer.write(f)

    # Clean up temp pdfs
    for tp in temp_pdf_files:
        try:
            os.remove(tp)
        except:
            pass

    print(f"✓ Combined PDF written to {OUT_PDF}")
    print("\nAll 19 posters generated successfully in FABMAT/, output/1x/, output/2x/, and output/18-day-campaign-posters.pdf!")

if __name__ == "__main__":
    main()
