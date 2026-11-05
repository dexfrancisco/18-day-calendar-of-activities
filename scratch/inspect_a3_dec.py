import re

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<div class="([^"]*grid[^"]*)">', text):
    print("Found grid class:", m.group(1))

m_dec = re.search(r'<!-- === ROW 2: DECEMBER 2026 === -->.*?</section>', text, re.DOTALL)
if m_dec:
    print("Found Dec section!")
    grids = re.findall(r'<div class="([^"]*)">', m_dec.group(0))
    print("Div classes in Dec:", grids[:10])
    cards = re.findall(r'class="day-pill">([^<]+)</span>', m_dec.group(0))
    print("Cards in Dec:", cards)

