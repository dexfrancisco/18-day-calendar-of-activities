import re

files = [
    '18-day-campaign-calendar-a3.html',
    '18-day-campaign-calendar.html',
    'Final Copy/18-day-campaign-calendar-a3.html',
    'Final Copy/18-day-campaign-calendar.html',
    '18-day-campaign-calendar-a4.html',
    '18-day-campaign-calendar-a4-page2.html'
]

for fp in files:
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            c = f.read()
        m = re.search(r'day-card.*?DAY 10.*?(?=day-card|\Z)', c, re.DOTALL)
        if m:
            v_m = re.search(r'class=["\']card-venue-box["\'][^>]*>(.*?)</div>', m.group(0), re.DOTALL)
            print(f'{fp}:')
            print('  Venue:', v_m.group(1).strip() if v_m else 'Not found')
        else:
            print(f'{fp}: DAY 10 card not found')
    except Exception as e:
        print(f'{fp}: {e}')

