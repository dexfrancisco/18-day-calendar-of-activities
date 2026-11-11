import json
import os
import sys

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
sys.path.append(BASE_DIR)
import generate_posters

# 1. Update Day 9 in schedule_data.json to have all 5 activities
with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

# The 5 activities
acts_5 = [
    {
        "num": 1,
        "lead_office": "City Health Office",
        "description": "Health response, mental health, reproductive health, medico-legal awareness, and support services for survivors."
    },
    {
        "num": 2,
        "lead_office": "City Legal Office",
        "description": "Orientation on RA 9262, Safe Spaces Act, Anti-Trafficking, cyber-related VAWC and online crimes; legal referral pathways."
    },
    {
        "num": 3,
        "lead_office": "PNP-WCPD / LCAT-VAWC / BJMP / Justice Sector",
        "description": "Case documentation, law enforcement coordination, protection procedures, and anti-online exploitation response."
    },
    {
        "num": 4,
        "lead_office": "Liga ng mga Barangay / VAW Desks",
        "description": "Barangay action planning, desk strengthening, community watch, and referral readiness."
    },
    {
        "num": 5,
        "lead_office": "JCD GAD CONNECT and CDRRMO",
        "description": "Digital Safety Day: demo of Project S.U.N.S.H.I.N.E., iReport VAWC, Safe Line, online reporting, cyber safety & digital evidence awareness."
    }
]

data[9]["layout_type"] = "standard_activities"
data[9]["activities"] = acts_5
data[9]["icon_filename"] = "DAY 10.png"
data[9]["venue"] = "ICON"
data[9].pop("main_activity", None)

with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Updated schedule_data.json: Day 9 now has 5 activities!")

# 2. Render HTML for Day 9
html = generate_posters.render_day_html(data[9])
h_path = os.path.join(BASE_DIR, "scratch", "final_html", "09-day-09.html")
with open(h_path, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Wrote scratch/final_html/09-day-09.html with 5 activities")
