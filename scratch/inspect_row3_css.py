import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\.grid-6\.row-3\s*\{([^}]+)\}', text)
if m:
    print(".grid-6.row-3:", m.group(1).strip())

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2 = f.read()

m2 = re.search(r'\.p2-grid-row2\s*\{([^}]+)\}', p2)
if m2:
    print(".p2-grid-row2:", m2.group(1).strip())

