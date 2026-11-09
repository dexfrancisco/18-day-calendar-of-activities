import re

def inspect_day3(fn):
    print(f"=== {fn} ===")
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'DAY 3.*?ACTIVITY 1.*?</article>', text, re.DOTALL)
    if m:
        act1 = re.search(r'ACTIVITY 1.*?(?=ACTIVITY 2)', m.group(0), re.DOTALL)
        if act1:
            print(act1.group(0))
        else:
            print("ACTIVITY 1 boundary not matched cleanly")
    else:
        print("DAY 3 not found!")

for fn in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar-a4-page1.html']:
    inspect_day3(fn)

