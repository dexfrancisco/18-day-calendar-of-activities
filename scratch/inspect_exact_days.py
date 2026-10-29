import re

def inspect_days(fn):
    print(f"=== {fn} ===")
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()

    articles = re.findall(r'<article class="day-card\s+([^"]*)">(.*?)</article>', text, re.DOTALL)
    for cls, body in articles:
        dp = re.search(r'<span class="day-pill">([^<]+)</span>', body)
        if dp and dp.group(1) in ['DAY 1', 'DAY 2', 'DAY 8', 'DAY 10']:
            v_m = re.search(r'<div class="card-venue-box[^>]*>.*?<span>(.*?)</span>', body, re.DOTALL)
            v_str = v_m.group(1).replace('\n', ' ').strip() if v_m else "NO VENUE"
            print(f"  {dp.group(1)}: {v_str}")

for fn in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar-a4-page1.html', '18-day-campaign-calendar-a4-page2.html']:
    inspect_days(fn)

