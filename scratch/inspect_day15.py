import re

def inspect_day15(fn):
    print(f"=== {fn} ===")
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'<!-- DAY 15.*?-->\s*<article.*?</article>', text, re.DOTALL)
    if not m:
        m = re.search(r'DAY 15.*?</article>', text, re.DOTALL)
    if m:
        print(m.group(0))
    else:
        print("DAY 15 not found!")

for fn in ['18-day-campaign-calendar-a3.html', '18-day-campaign-calendar-a4-page2.html']:
    inspect_day15(fn)

