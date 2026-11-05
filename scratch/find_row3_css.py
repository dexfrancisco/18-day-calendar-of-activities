import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'row-3.*?\{([^}]+)\}', text)
if m:
    print(m.group(0))
else:
    print("row-3 not found in CSS!")

