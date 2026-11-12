with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<article class="day-card[^"]*">\s*<div class="card-top-bar">\s*<span class="day-pill">DAY 11</span>(.*?)</article>', text, re.DOTALL)
if m:
    print(m.group(1))

