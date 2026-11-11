import json

with open('scratch/schedule_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for day in data:
    dnum = day.get('day_number')
    print(f"--- Day {dnum} ---")
    print(f"Icon: {day.get('icon_filename')}")
    print(f"Venue: {day.get('venue')}")
    if 'main_activity' in day:
        print(f"Main Activity: {day.get('main_activity')}")
    if 'activities' in day:
        for a in day['activities']:
            print(f"Act {a.get('num')}: {a.get('description')}")
    if 'activities_detailed' in day:
        print(f"Detailed acts count: {len(day['activities_detailed'])}")
    if 'group1' in day:
        for a in day['group1']['activities']:
            print(f"G1 Act {a.get('num')}: {a.get('description')}")
        print(f"G2 Act {day['group2']['activity'].get('num')}: {day['group2']['activity'].get('description')}")

