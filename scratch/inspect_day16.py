import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m16 = re.search(r'<!-- DAY 16.*?-->\s*<article.*?</article>', text, re.DOTALL)
if m16:
    print("A3 DAY 16:")
    print(m16.group(0))

with open('18-day-campaign-calendar-a4-page2.html', 'r', encoding='utf-8') as f:
    p2_text = f.read()

m16_p2 = re.search(r'<!-- DAY 16.*?-->\s*<article.*?</article>', p2_text, re.DOTALL)
if m16_p2:
    print("A4 P2 DAY 16:")
    print(m16_p2.group(0))

