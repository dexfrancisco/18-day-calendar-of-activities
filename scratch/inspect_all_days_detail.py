import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    print(f"--- Day {d['day_number']} ({d['badge']}) layout={d.get('layout_type')} ---")
    for k, v in d.items():
        if k not in ['id', 'day_number', 'filename', 'badge', 'layout_type']:
            if isinstance(v, list):
                print(f"  {k}: {len(v)} items")
                for item in v:
                    print(f"    - {item}")
            elif isinstance(v, str) and len(v) > 60:
                print(f"  {k}: {v[:60]}...")
            else:
                print(f"  {k}: {v}")

