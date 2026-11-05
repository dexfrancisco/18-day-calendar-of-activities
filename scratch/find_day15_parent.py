import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('DAY 15')
idx_open = text.rfind('<div class="', 0, idx)
print(text[idx_open:idx_open+100])

