import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m_all = re.finditer(r'<section class="month-section[^"]*">(.*?)</section>', text, re.DOTALL)
for i, m in enumerate(m_all, 1):
    cards = re.findall(r'class="day-pill">([^<]+)</span>', m.group(1))
    print(f"Month section {i} cards:", cards)

