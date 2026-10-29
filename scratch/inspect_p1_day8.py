import re

with open('18-day-campaign-calendar-a4-page1.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<div class="(p1-grid-row\d+)">', text):
    print('Row:', m.group(1))

# Check where Day 8 is located
idx8 = text.find('DAY 8')
print("Surrounding text for Day 8:")
print(text[idx8-100:idx8+500])

