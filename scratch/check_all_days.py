import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    acts = d.get('activities', [])
    print(f"Day {d['day_number']:2d} ({d['badge']}): layout={d.get('layout_type')}, acts={len(acts)}, title={bool(d.get('title'))}")

