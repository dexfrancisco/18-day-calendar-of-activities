import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'        <!-- DAY 8 -->.*?</article>', text, re.DOTALL)
if m:
    print("A3 DAY 8 EXACT:")
    print(repr(m.group(0)))

with open('18-day-campaign-calendar-a4-page1.html', 'r', encoding='utf-8') as f:
    text_p1 = f.read()

m_p1 = re.search(r'        <!-- DAY 8 -->.*?</article>', text_p1, re.DOTALL)
if m_p1:
    print("A4 P1 DAY 8 EXACT:")
    print(repr(m_p1.group(0)))

