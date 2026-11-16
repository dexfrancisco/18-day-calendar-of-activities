import os
import json
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

OLD_ACT1_DESC = '<div class="sub-act-desc">Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW</div>'

# 1. Master Calendar A3 & Standard HTMLs
A3_BULLET_BLOCK = """<div class="sub-act-desc" style="display: flex; flex-direction: column; gap: 4px; font-size: 27px; line-height: 1.2;">
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <span style="color: #ea580c; font-weight: 800; flex-shrink: 0;">&bull;</span>
              <span>Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW</span>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <span style="color: #ea580c; font-weight: 800; flex-shrink: 0;">&bull;</span>
              <span>Awarding for the Most Disaster Ready and Resilient Barangay</span>
            </div>
          </div>"""

a3_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html"),
]

for fpath in a3_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    assert OLD_ACT1_DESC in content, f"Target not found in {fpath}"
    assert content.count(OLD_ACT1_DESC) == 1, f"Multiple matches in {fpath}"
    content = content.replace(OLD_ACT1_DESC, A3_BULLET_BLOCK)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated A3/standard calendar: {os.path.relpath(fpath, BASE_DIR)}")

# 2. Master Calendar A4 HTMLs
A4_BULLET_BLOCK = """<div class="sub-act-desc" style="display: flex; flex-direction: column; gap: 3px; font-size: 20.5px; line-height: 1.16;">
              <div style="display: flex; align-items: flex-start; gap: 6px;">
                <span style="color: #ea580c; font-weight: 800; flex-shrink: 0;">&bull;</span>
                <span>Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW</span>
              </div>
              <div style="display: flex; align-items: flex-start; gap: 6px;">
                <span style="color: #ea580c; font-weight: 800; flex-shrink: 0;">&bull;</span>
                <span>Awarding for the Most Disaster Ready and Resilient Barangay</span>
              </div>
            </div>"""

a4_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page2.html"),
]

for fpath in a4_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    assert OLD_ACT1_DESC in content, f"Target not found in {fpath}"
    assert content.count(OLD_ACT1_DESC) == 1, f"Multiple matches in {fpath}"
    content = content.replace(OLD_ACT1_DESC, A4_BULLET_BLOCK)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated A4 calendar: {os.path.relpath(fpath, BASE_DIR)}")

# 3. Day 15 FABMAT HTML
h15_path = os.path.join(BASE_DIR, "scratch", "final_html", "15-day-15.html")
with open(h15_path, "r", encoding="utf-8") as f:
    h15 = f.read()

old_css_block = """        .safe-zone {
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            gap: 28px;
        }
        .hero-icon { width: 600px; height: 600px; }
        .stroke-day { font-size: 142px; }
        .stroke-date { font-size: 64px; }
        .acts-block {
            display: flex;
            flex-direction: column;
            gap: 26px;
            width: 100%;
        }
        .act-item {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .act-header-row {
            display: flex;
            align-items: baseline;
            gap: 18px;
        }
        .act-num {
            font-size: 72px;
            flex-shrink: 0;
            width: 68px;
        }
        .act-desc {
            font-size: 68px;
            line-height: 1.18;
            flex: 1;
        }
        .act-lead-row {
            display: flex;
            align-items: baseline;
            gap: 18px;
            margin-left: 78px;
        }
        .act-lead-lbl {
            font-size: 46px;
            flex-shrink: 0;
        }
        .act-lead-val {
            font-size: 50px;
            flex: 1;
        }
        .bottom-block {
            display: flex;
            flex-direction: column;
            gap: 16px;
            width: 100%;
        }
        .detail-label-col { width: 420px; flex-shrink: 0; font-size: 52px; }
        .detail-val-col { flex: 1; font-size: 52px; line-height: 1.2; }"""

new_css_block = """        .safe-zone {
            position: absolute;
            top: 1310px;
            left: 190px;
            width: 2100px;
            display: flex;
            flex-direction: column;
            gap: 22px;
        }
        .hero-icon { width: 600px; height: 600px; }
        .stroke-day { font-size: 142px; }
        .stroke-date { font-size: 64px; }
        .acts-block {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;
        }
        .act-item {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .act-header-row {
            display: flex;
            align-items: baseline;
            gap: 18px;
        }
        .act-num {
            font-size: 64px;
            flex-shrink: 0;
            width: 64px;
        }
        .act-desc {
            font-size: 60px;
            line-height: 1.16;
            flex: 1;
        }
        .act-lead-row {
            display: flex;
            align-items: baseline;
            gap: 18px;
            margin-left: 82px;
        }
        .act-lead-lbl {
            font-size: 44px;
            flex-shrink: 0;
        }
        .act-lead-val {
            font-size: 48px;
            flex: 1;
        }
        .bottom-block {
            display: flex;
            flex-direction: column;
            gap: 12px;
            width: 100%;
        }
        .detail-label-col { width: 420px; flex-shrink: 0; font-size: 48px; }
        .detail-val-col { flex: 1; font-size: 48px; line-height: 1.18; }"""

# Normalize CRLF vs LF when matching
h15_norm = h15.replace("\r\n", "\n")
assert old_css_block in h15_norm, "old_css_block not found in 15-day-15.html"
h15_norm = h15_norm.replace(old_css_block, new_css_block)

old_act1_html = """            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">1.</div>
                    <div class="stroke-act-desc act-desc">Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">Culminating Activity led by LGU Cauayan</span>
                </div>
            </div>"""

new_act1_html = """            <div class="act-item">
                <div class="act-header-row" style="align-items: flex-start;">
                    <div class="stroke-num act-num">1.</div>
                    <div style="display: flex; flex-direction: column; gap: 10px; flex: 1;">
                        <div style="display: flex; align-items: baseline; gap: 14px;">
                            <span class="stroke-act-desc act-desc" style="flex: 0 0 auto;">&bull;</span>
                            <span class="stroke-act-desc act-desc">Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW</span>
                        </div>
                        <div style="display: flex; align-items: baseline; gap: 14px;">
                            <span class="stroke-act-desc act-desc" style="flex: 0 0 auto;">&bull;</span>
                            <span class="stroke-act-desc act-desc">Awarding for the Most Disaster Ready and Resilient Barangay</span>
                        </div>
                    </div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">Culminating Activity led by LGU Cauayan</span>
                </div>
            </div>"""

assert old_act1_html in h15_norm, "old_act1_html not found in 15-day-15.html"
h15_norm = h15_norm.replace(old_act1_html, new_act1_html)

with open(h15_path, "w", encoding="utf-8") as f:
    f.write(h15_norm)
print("Updated scratch/final_html/15-day-15.html")

# 4. scratch/schedule_data.json & Extracted Text Files
sched_path = os.path.join(BASE_DIR, "scratch", "schedule_data.json")
with open(sched_path, "r", encoding="utf-8") as f:
    sched_data = json.load(f)

updated_sched = False
for day in sched_data:
    if day.get("filename") == "15-day-15.png":
        for act in day.get("activities", []):
            if act.get("num") == 1:
                act["description"] = "• Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW\n• Awarding for the Most Disaster Ready and Resilient Barangay"
                updated_sched = True
assert updated_sched, "Day 15 Activity 1 not found in schedule_data.json"

with open(sched_path, "w", encoding="utf-8") as f:
    json.dump(sched_data, f, indent=2, ensure_ascii=False)
print("Updated scratch/schedule_data.json")

txt_files = [
    os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_Extracted_Text.txt"),
    os.path.join(BASE_DIR, "Final Copy", "18-Day_Campaign_Calendar_Extracted_Text.txt"),
]

old_txt_act1 = "  Description: Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW"
new_txt_act1 = "  Description:\n    • Culminating and Awarding Ceremony: 2026 18-Day Campaign to End VAW\n    • Awarding for the Most Disaster Ready and Resilient Barangay"
old_txt_act2 = "  Description: PROJECT ORANGE RISE: Empowering 12 Women in Economic Enterprise through the Proceeds of Orange Run"
new_txt_act2 = "  Description: PROJECT ORANGE RISE: Empowering Women in Economic Enterprise through the Proceeds of Orange Run"

for tpath in txt_files:
    with open(tpath, "r", encoding="utf-8") as f:
        tcontent = f.read()
    tcontent_norm = tcontent.replace("\r\n", "\n")
    assert old_txt_act1 in tcontent_norm, f"old_txt_act1 not found in {tpath}"
    tcontent_norm = tcontent_norm.replace(old_txt_act1, new_txt_act1)
    if old_txt_act2 in tcontent_norm:
        tcontent_norm = tcontent_norm.replace(old_txt_act2, new_txt_act2)
    with open(tpath, "w", encoding="utf-8") as f:
        f.write(tcontent_norm)
    print(f"Updated extracted text: {os.path.relpath(tpath, BASE_DIR)}")
