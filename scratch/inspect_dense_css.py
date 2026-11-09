import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\.single-act-desc\.dense\s*\{([^}]+)\}', text)
if m:
    print("A3 dense CSS:", m.group(0))

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2 = f.read()

m2 = re.search(r'\.single-act-desc\.dense\s*\{([^}]+)\}', p2)
if m2:
    print("A4 P2 dense CSS:", m2.group(0))

