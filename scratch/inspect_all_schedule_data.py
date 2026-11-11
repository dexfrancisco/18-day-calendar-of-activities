import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    num = d.get('day_number')
    print(f"=== DAY {num} ({d.get('badge')}) ===")
    if 'activities' in d:
        for a in d['activities']:
            print(f"  A{a.get('num')}: {a.get('description')}")
    if 'main_activity' in d:
        print(f"  Main: {d.get('main_activity')}")
    if 'title' in d:
        print(f"  Title: {d.get('title')}")
    if 'description' in d and 'activities' not in d:
        print(f"  Desc: {d.get('description')}")
    print(f"  Venue: {d.get('venue')}")

