import re

def check_file(fn):
    print(f"=== {fn} ===")
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()

    for d in [1, 2, 8, 10]:
        m = re.search(rf'DAY {d}\b.*?</article>', text, re.DOTALL)
        if m:
            v_m = re.search(r'Venue:.*?</span>', m.group(0))
            v_str = v_m.group(0) if v_m else "NO VENUE"
            print(f"  Day {d}: {v_str}")
        else:
            print(f"  Day {d}: NOT FOUND in {fn}")

for fn in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar-a4-page1.html', '18-day-campaign-calendar-a4-page2.html']:
    check_file(fn)

