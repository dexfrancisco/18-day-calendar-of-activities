import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('DAY 15')
print("Surrounding Day 15:")
print(text[idx-200:idx+400])

