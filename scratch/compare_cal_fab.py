import json
import re

with open('scratch/fabmat_extracted_dump.json', 'r', encoding='utf-8') as f:
    fabmats = json.load(f)

with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'r', encoding='utf-8') as f:
    cal_text = f.read()

# Let's inspect each day one by one and compare
print("="*80)
print("COMPREHENSIVE DAY-BY-DAY AUDIT: CALENDAR VS FABMAT")
print("="*80)

days = [
    ("00-pre-campaign", "PRE-CAMPAIGN"),
    ("01-day-01", "DAY 1"),
    ("02-day-02", "DAY 2"),
    ("03-day-03", "DAY 3"),
    ("04-day-04", "DAY 4"),
    ("05-day-05", "DAY 5"),
    ("06-day-06", "DAY 6"),
    ("07-day-07", "DAY 7"),
    ("08-day-08", "DAY 8"),
    ("09-day-09", "DAY 9"),
    ("10-day-10", "DAY 10"),
    ("11-day-11", "DAY 11"),
    ("12-day-12", "DAY 12"),
    ("13-day-13", "DAY 13"),
    ("14-day-14", "DAY 14"),
    ("15-day-15", "DAY 15"),
    ("16-day-16", "DAY 16"),
    ("17-day-17", "DAY 17"),
    ("18-day-18", "DAY 18"),
]

for file_key, day_name in days:
    fab = fabmats.get(file_key, {})
    print(f"\n[{file_key.upper()}] ({day_name})")
    print(f"  FABMAT Day:     {fab.get('day')}")
    print(f"  FABMAT Date:    {fab.get('date')}")
    print(f"  FABMAT Title:   {fab.get('title')}")
    print(f"  FABMAT Sub:     {fab.get('subtitle')}")
    print(f"  FABMAT Acts:    {len(fab.get('acts', []))} activities")
    for idx, act in enumerate(fab.get('acts', [])):
        print(f"    Act {idx+1}: {act.get('num')} | Lead: {act.get('lead_val')}")
        print(f"           Desc: {act.get('desc')}")
    print(f"  FABMAT Details: {fab.get('details')}")

