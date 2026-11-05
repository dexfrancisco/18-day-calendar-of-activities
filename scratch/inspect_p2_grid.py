import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'/\* MONTH 2 \(DECEMBER\) GRID \*/.*?(?=/\* DAY 10)', text, re.DOTALL)
if m:
    print("A3 Grid Dec:")
    print(m.group(0))

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2_text = f.read()

m2 = re.search(r'\.p2-grid-row[12]\s*\{[^}]+\}', p2_text)
for m in re.finditer(r'(\.p2-grid-row[12])\s*\{([^}]+)\}', p2_text):
    print("A4 P2 Grid:", m.group(1), m.group(2).strip())

