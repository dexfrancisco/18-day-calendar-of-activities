import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for day in data:
    if day.get('filename') in ['05-day-05.png', '09-day-09.png', '11-day-11.png', '12-day-12.png', '17-day-17.png', '18-day-18.png']:
        print(f"=== {day['filename']} ===")
        print(f"Title: {day.get('title')}")
        print(f"Subtitle: {day.get('subtitle')}")
        print(f"Activities: {len(day.get('activities', []))}")
        for a in day.get('activities', []):
            print(f"  - {a}")
        print(f"Partners: {day.get('partners')}")
        print(f"Venue: {day.get('venue')}")

