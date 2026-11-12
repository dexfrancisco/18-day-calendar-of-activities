import json
import glob
import re

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== CHECKING SCHEDULE DATA ===")
for day in data:
    acts = day.get('activities', [])
    online_acts = []
    other_acts = []
    for act in acts:
        desc = act.get('description', '')
        lead = act.get('lead_office', '')
        full = f"{desc} {lead}"
        if 'online' in full.lower():
            online_acts.append(act)
        else:
            other_acts.append(act)
    if online_acts:
        print(f"\n{day['filename']} (Day {day.get('day_num')}):")
        print(f"  Total activities: {len(acts)}")
        print(f"  Online activities ({len(online_acts)}): {[a.get('description') for a in online_acts]}")
        print(f"  Other activities ({len(other_acts)}): {[a.get('description') for a in other_acts]}")
        print(f"  Venue: {day.get('venue')}")
        print(f"  Partners: {day.get('partners')}")

print("\n=== CHECKING FINAL HTML FILES ===")
for hfile in sorted(glob.glob('scratch/final_html/*.html')):
    with open(hfile, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'online' in html.lower():
        # find where online appears
        matches = re.findall(r'.{0,50}online.{0,50}', html, re.IGNORECASE)
        print(f"\n{hfile}:")
        for m in matches[:5]:
            print(f"   ... {m.strip()} ...")

