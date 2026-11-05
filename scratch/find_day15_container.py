import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('DAY 15')
idx_art = text.rfind('<article', 0, idx)
print("Before Day 15 article:")
print(text[idx_art-200:idx_art])

