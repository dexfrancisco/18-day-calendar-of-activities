import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'DAY 3 \(4 Activities.*?<!-- DAY 4', text, re.DOTALL)
if m:
    print("A3 Day 3:")
    print(m.group(0))

with open('18-day-campaign-calendar-a4-page1.html', 'r', encoding='utf-8') as f:
    p1 = f.read()

m_p1 = re.search(r'DAY 3 \(4 Activities.*?<!-- DAY 4', p1, re.DOTALL)
if m_p1:
    print("A4 P1 Day 3:")
    print(m_p1.group(0))

