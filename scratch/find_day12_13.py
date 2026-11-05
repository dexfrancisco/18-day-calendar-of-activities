import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx12 = text.find('<!-- DAY 12 -->')
idx13 = text.find('<!-- DAY 13')
print(text[idx12:idx13+50])

