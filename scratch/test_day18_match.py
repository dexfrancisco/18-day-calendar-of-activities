import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'      <!-- DAY 18 -->.*?</article>', text, re.DOTALL)
if m:
    print('Found Day 18:')
    print(ascii(m.group(0)))

