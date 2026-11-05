import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'(\.grid-[^\s{]+)\s*\{([^}]+)\}', text):
    print("A3 Grid:", m.group(1), m.group(2).strip())

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2 = f.read()

m_row2 = re.search(r'<div class="p2-grid-row2">(.*?)</div>\s*</section>', p2, re.DOTALL)
if m_row2:
    print("P2 Row 2 cards:", re.findall(r'class="day-pill">([^<]+)</span>', m_row2.group(1)))

