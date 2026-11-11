import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    num = d.get('day_number')
    if num in [3, 11, 17, 18]:
        print(f"=== DAY {num} ===")
        print(json.dumps(d, indent=2))

