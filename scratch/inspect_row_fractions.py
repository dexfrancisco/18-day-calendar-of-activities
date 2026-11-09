import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'row-3.*?\{([^}]+)\}', text)
if m:
    print("A3 Row 3:", m.group(0))

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2 = f.read()

m2 = re.search(r'\.p2-grid-row2.*?\{([^}]+)\}', p2)
if m2:
    print("A4 P2 Row 2:", m2.group(0))

