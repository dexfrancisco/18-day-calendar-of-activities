import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m_r3 = re.search(r'<div class="grid-6 row-3">(.*?)</div>\s*</section>', text, re.DOTALL)
if m_r3:
    print("A3 Row 3 cards:", re.findall(r'class="day-pill">([^<]+)</span>', m_r3.group(1)))

