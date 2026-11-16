import os
import json
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# 1. Update scratch/schedule_data.json
sched_path = os.path.join(BASE_DIR, "scratch", "schedule_data.json")
with open(sched_path, "r", encoding="utf-8") as f:
    sched_data = json.load(f)

for day in sched_data:
    if day.get("filename") == "14-day-14.png":
        day["lead_office"] = "GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs"
        print("Updated Day 14 in schedule_data.json")

with open(sched_path, "w", encoding="utf-8") as f:
    json.dump(sched_data, f, indent=2, ensure_ascii=False)

# 2. Update scratch/final_html/14-day-14.html
h14_path = os.path.join(BASE_DIR, "scratch", "final_html", "14-day-14.html")
with open(h14_path, "r", encoding="utf-8") as f:
    h14_content = f.read()

old_lead_html = '<div class="detail-val-col stroke-val">PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs</div>'
new_lead_html = '<div class="detail-val-col stroke-val">GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs</div>'

assert old_lead_html in h14_content, "old_lead_html not found in 14-day-14.html"
h14_content = h14_content.replace(old_lead_html, new_lead_html)
with open(h14_path, "w", encoding="utf-8") as f:
    f.write(h14_content)
print("Updated 14-day-14.html")

# 3. Update Calendar HTML files
calendar_files = [
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar-a3.html"),
    os.path.join(BASE_DIR, "Final Copy", "18-day-campaign-calendar.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4.html"),
    os.path.join(BASE_DIR, "18-day-campaign-calendar-a4-page2.html"),
]

old_cal_lead = "PIO, GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs"
new_cal_lead = "GAD Office, DepEd, ISU-Cauayan, Tourism Office, ISAC, CSOs"

for cpath in calendar_files:
    if os.path.exists(cpath):
        with open(cpath, "r", encoding="utf-8") as f:
            ccontent = f.read()
        if old_cal_lead in ccontent:
            ccontent = ccontent.replace(old_cal_lead, new_cal_lead)
            with open(cpath, "w", encoding="utf-8") as f:
                f.write(ccontent)
            print(f"Updated {os.path.relpath(cpath, BASE_DIR)}")
        else:
            print(f"Warning: pattern not found in {os.path.relpath(cpath, BASE_DIR)}")

# 4. Update extracted text files
txt_files = [
    os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_Extracted_Text.txt"),
    os.path.join(BASE_DIR, "Final Copy", "18-Day_Campaign_Calendar_Extracted_Text.txt"),
]

for tpath in txt_files:
    if os.path.exists(tpath):
        with open(tpath, "r", encoding="utf-8") as f:
            tcontent = f.read()
        if old_cal_lead in tcontent:
            tcontent = tcontent.replace(old_cal_lead, new_cal_lead)
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(tcontent)
            print(f"Updated {os.path.relpath(tpath, BASE_DIR)}")

